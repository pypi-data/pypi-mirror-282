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
