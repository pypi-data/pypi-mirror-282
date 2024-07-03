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
