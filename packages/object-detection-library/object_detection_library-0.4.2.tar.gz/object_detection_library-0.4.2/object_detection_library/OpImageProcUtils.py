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
