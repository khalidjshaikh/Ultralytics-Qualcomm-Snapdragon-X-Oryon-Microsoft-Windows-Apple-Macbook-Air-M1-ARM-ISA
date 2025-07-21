import sys
import ultralytics
import numpy
import cv2

print(f"Python version: {sys.version}")
print(f"Ultralytics version: {ultralytics.__version__}")
print(f"NumPy version: {numpy.__version__}")
print(f"OpenCV (cv2) version: {cv2.__version__}")

from ultralytics import YOLO
from numpy import * 

model = YOLO('yolov8n.pt') 
cap = cv2.VideoCapture(0) 

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(frame)  # or video stream
    for r in results:
        for det in r.boxes:  # Accessing individual detections
            x_center, y_center, width, height = array(det.xywhn.tolist()).flatten()  # Normalized coordinates
            x1, y1, x2, y2 = array(det.xyxy.tolist()).flatten()  # Absolute pixel coordinates (top-left, bottom-right)
            class_id = det.cls.item()
            confidence = det.conf.item()
            #mprint(f"Class ID: {class_id}, Confidence: {confidence}")
            frame = cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
            frame = cv2.putText(frame, f"{model.names[class_id]} {confidence:.1f}", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    cv2.imshow("Camera Feed", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break
    # break

cap.release()
cv2.destroyAllWindows()

___

test