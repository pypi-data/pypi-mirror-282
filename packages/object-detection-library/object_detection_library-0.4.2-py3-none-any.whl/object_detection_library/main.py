import argparse
import json
import os
import cv2
from time import sleep, time
from bson import BSON
from base64 import b64encode
# from OpImageProcUtils import load_model, get_detected_objects
# from OpCameraUtils import captureFrame, releaseCamera
# from mqtt_client import publish_data


# Global constants
FRAMES_TO_PROCESS = 1
POLLING_INTERVAL = 0.3  # 300 milliseconds
VIDEO_SAMPLE_LENGTH = 1.0  # 1 second (not used now)
INTERESTED_OBJECT_IDS = {"Object010", "Object004", "Object011"}  # Example objects

def save_detected_objects_as_json(detected_objects, frame, video_file):
    folder_name = "JSON_Files"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    _, img_buffer = cv2.imencode('.jpg', frame)
    img_bson = BSON.encode({"image": img_buffer.tobytes(), "mime_type": "image/jpeg"})
    img_bson_encoded = b64encode(img_bson).decode('utf-8')

    vdo_bson_encoded = None
    if video_file:
        with open(video_file, 'rb') as f:
            vdo_bson = BSON.encode({"video": f.read(), "mime_type": "video/mp4"})
            vdo_bson_encoded = b64encode(vdo_bson).decode('utf-8')

    for obj in detected_objects:
        obj["ImgBson"] = {"data": img_bson_encoded, "mime_type": "image/jpeg"}
        if vdo_bson_encoded:
            obj["VdoBson"] = {"data": vdo_bson_encoded, "mime_type": "video/mp4"}
        file_name = f"{folder_name}/detected_{obj['label'].replace(' ', '_')}_{obj['timestamp'].replace(':', '-')}.json"
        with open(file_name, 'w') as f:
            json.dump(obj, f, indent=2)

def check_for_events(frame, model, conf_threshold, video_file):
    detected_objects = get_detected_objects(frame, model, conf_threshold)
    return_list = []

    # Filter detected objects to only include those in INTERESTED_OBJECT_IDS
    filtered_objects = [obj for obj in detected_objects if obj['label'] in INTERESTED_OBJECT_IDS]

    if filtered_objects:
        save_detected_objects_as_json(filtered_objects, frame, video_file)
        for obj in filtered_objects:
            publish_data(obj)
    
    return filtered_objects

def main(args):
    model = load_model(args.model)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    frame_folder = "image_frames"
    video_folder = "video_clips"  # Folder for video clips

    if not os.path.exists(frame_folder):
        os.makedirs(frame_folder)
    if not os.path.exists(video_folder):
        os.makedirs(video_folder)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Corrected cv4 to cv2
    out = None
    recording = False
    video_file = None

    start_time = time()

    while True:
        ret, frame = cap.read()
        if not ret:
            print(f"Camera read error: {ret}")
            break

        return_list = check_for_events(frame, model, args.conf, video_file)

        if return_list:
            frame_file = os.path.join(frame_folder, f"frame_{len(os.listdir(frame_folder))}.jpg")
            cv2.imwrite(frame_file, frame)
            print(f"Frame saved as {frame_file}")

            if not recording:
                video_file = os.path.join(video_folder, f"detected_instance_{len(os.listdir(video_folder))}.avi")
                out = cv2.VideoWriter(video_file, fourcc, 20.0, (frame.shape[1], frame.shape[0]))
                recording = True

            if recording and out is not None:
                out.write(frame)

        elif recording:
            recording = False
            if out is not None:
                out.release()
                out = None
                print(f"Video saved as {video_file}")

            # Save the detected objects and the corresponding video file information
            save_detected_objects_as_json(return_list, frame, video_file)

        # Display the live video feed
        if args.show:
            cv2.imshow('YOLOv8 Prediction', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        sleep(POLLING_INTERVAL)

    if recording and out is not None:
        out.release()

    releaseCamera(cap)
    cv2.destroyAllWindows()


import base64
import cv2
import numpy as np

def convertToJpeg(bson_object):
    # Decode the base64-encoded BSON image
    image_data = base64.b64decode(bson_object)
    # Convert bytes data to numpy array
    image_array = np.frombuffer(image_data, dtype=np.uint8)
    # Decode image array to image
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    return image

def writeToFile(image, image_file_name):
    # Save the image as a JPEG file
    cv2.imwrite(image_file_name, image)
    print(f"Image saved as {image_file_name}")


import cv2
from ultralytics import YOLO
from datetime import datetime
import base64

# Global constants
INTERESTED_OBJECT_IDS = {"Object010", "Object004", "Object011"}

def load_model(model_path):
    return YOLO(model_path)

def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def encode_image_to_bson(image):
    _, buffer = cv2.imencode('.jpg', image)
    return base64.b64encode(buffer).decode('utf-8')

def get_detected_objects(frame, model, conf_threshold):
    results = model.predict(frame)
    detected_objects = []
    
    filtered_results = []

    for result in results:
        for detection in result.boxes.data:
            xmin, ymin, xmax, ymax, conf, cls = detection[:6].cpu().numpy().flatten()
            if conf >= conf_threshold:
                obj_label = model.names[int(cls)]
                
                # Check if the detected object is in the list of interested objects
                if obj_label in INTERESTED_OBJECT_IDS:
                    filtered_results.append(f"{obj_label}: {conf:.2f}")
                    label = f'{obj_label}: {conf:.2f}'
                    cv2.rectangle(frame, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 0), 2)
                    cv2.putText(frame, label, (int(xmin), int(ymin) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                    
                    print(f'Timestamp: {get_current_timestamp()}, Object: {obj_label}')
                    encoded_image = encode_image_to_bson(frame)

                    data = {
                        'timestamp': get_current_timestamp(),
                        'label': obj_label,
                        'image': encoded_image,
                        'mime': "image/jpeg"
                    }
                    detected_objects.append(data)
                    
    if filtered_results:
        print(f"Detected objects: {filtered_results}")
                
    return detected_objects


import cv2

def captureFrame(video_capture):
    ret, frame = video_capture.read()
    if not ret:
        print("Camera read error")
        return None
    return frame

def releaseCamera(video_capture):
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='YOLOv8 Webcam Object Detection with BSON-embedded JSON Save')
    parser.add_argument('--model', type=str, required=True, help='Path to the model file')
    parser.add_argument('--conf', type=float, default=0.5, help='Confidence threshold')
    parser.add_argument('--show', action='store_true', help='Display the live video feed with detections')
    args = parser.parse_args()

    main(args)
