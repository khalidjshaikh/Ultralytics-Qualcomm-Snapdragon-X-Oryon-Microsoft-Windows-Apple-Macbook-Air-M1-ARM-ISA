import cv2

print(f"OpenCV version: {cv2.__version__}")

avaiable = []
i=0
while True:
    cap = cv2.VideoCapture(i)
    
    if not cap.read()[0]:
        print(f"Camera index {i:02d} not found...")
        break
    
    avaiable.append(i)
    cap.release()
    
    print(f"Camera index {i:02d} OK!")
    i += 1

print(f"Cameras found: {avaiable}")