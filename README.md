# YOLOv8 Webcam Inference

This project demonstrates how to perform real-time object detection using a YOLOv8 model with a webcam feed. The YOLOv8 model is loaded, and the webcam feed is processed frame-by-frame to detect objects, annotate the frames, and display them in real-time.

Features

Uses YOLOv8 for real-time object detection.
Captures and processes webcam video streams.
Displays annotated frames with detected objects.
Graceful shutdown of the program via ESC key.
Prerequisites

## What you need to run project

1. Python 3.x: Ensure you have Python installed.
2. OpenCV: For video capture and frame rendering.   pip install opencv-python
3. Ultralytics YOLO: The library used for YOLOv8 model handling.  pip install ultralytics


Webcam Capture: The script captures video input from the default webcam using cv2.VideoCapture(0).
Object Detection: Each frame is processed using the YOLOv8 model, and the results are drawn directly on the frames.
Exit the Program: Press the ESC key (ASCII code 27) to safely exit the application and release resources.


