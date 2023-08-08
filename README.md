# Object Detection Web Application

A web application that utilizes YOLO (You Only Look Once) object detection to identify and display objects within uploaded images. Users can upload images, and the application processes them to highlight and label detected objects.

## Features

- Upload images for object detection.
- Utilizes the YOLO v4 model for real-time object detection.
- Displays detected objects in bounding boxes with labels.
- Supports interactive removal of bounding boxes.

## Prerequisites

- Python 3.x
- Django
- OpenCV (cv2)
- Numpy
- Base64

## Setup

1. Clone the repository to your local machine:
   ```shell
   git clone https://github.com/your-username/object-detection-app.git
   cd object-detection-app
   ```
2. Install the required dependencies:
   ```shell
    pip install -r requirements.txt
   ```
3. Run the Django development server:
   ```shell
    python manage.py runserver
   ```
4. Open your web browser and navigate to `http://localhost:8000` to access the application.

## Usage
1. Upload an image through the "Upload Image" page.
2. Navigate to the "YOLO Detection" page to view the uploaded image with detected objects highlighted.
   
## Download Yolo Model and COCO dataset
Link to download the Yolo V4 and COCO dataset used in this project `https://pysource.com/2019/06/27/yolo-object-detection-using-opencv-with-python/`

