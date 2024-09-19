import cv2
from ultralytics import YOLO

model = YOLO("/Users/glenn/detecting_with_yolo/yolov8s.pt")

# Start the webcam capture

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        print("failed to open frame")
        break
    
    results = model(frame)
    annotaed_frame = results[0].plot()
    
    cv2.imshow("Yolow 8 interference", annotaed_frame)
    
    # We want to break the loop so we can shutdown program 
    
    if cv2.waitKey(1)== 27: # 27 is the Ascii code for esc
        print(" Program is aborted by user")
        break
    
    # Relaese the capture
    
cap.release()
cv2.destroyAllWindows
    
