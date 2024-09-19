from ultralytics import YOLO

#Create model

model = YOLO("yolov8s.pt")

# Perfor the detection in picture 
results = model("/Users/glenn/detecting_with_yolo/yolo_project_detect/20180523-ErinWasson42991.jpg.webp", save=True)

# Save a picture of result 

results[0].save("/Users/glenn/detecting_with_yolo/yolo_project_detect/output.jpg")

