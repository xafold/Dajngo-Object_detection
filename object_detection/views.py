from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import UploadImgData
import cv2
import numpy as np
import base64
import os
# Create your views here.

class UploadImgView(CreateView):
    template_name = "object_detection/upload_img.html"
    model = UploadImgData
    fields = "__all__"
    success_url = "/"

    def get(self, request, *args, **kwargs):
        folder_path = r"C:\Users\Xafold\Desktop\python oop\Django\ObjectDetection\uploads\images"
        file_path = os.path.join(folder_path, "uploaded_image.jpg")
        if os.path.isfile(file_path):
            os.remove(file_path)
        return super().get(request, *args, **kwargs)
    
def yolo_detection(request):
    # Load Yolo
    net = cv2.dnn.readNet("C:/Users/Xafold/Downloads/Compressed/yolo_object_detection/yolov3.weights", 
                        "C:/Users/Xafold/Downloads/Compressed/yolo_object_detection/yolov3.cfg")
    classes = []
    with open("C:/Users/Xafold/Downloads/Compressed/yolo_object_detection/coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]

    layers_names = net.getLayerNames()
    output_layers = [layers_names[i - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    # Loading image
    img = cv2.imread(r"C:\Users\Xafold\Downloads\Compressed\yolo_object_detection\room_ser.jpg")
    img = cv2.resize(img, None, fx=0.2, fy=0.3)
    height, width, channels = img.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []
    labels = []  # Store the labels for each bounding box
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
                labels.append(classes[class_id])  # Store the label

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Storing bounding box coordinates
    bounding_boxes = {}
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = labels[i]  # Get the label for the current bounding box
            if label not in bounding_boxes:
                bounding_boxes[label] = []
            bounding_boxes[label].append((x, y, w, h))

    # Encode the image to base64
    _, img_encoded = cv2.imencode('.jpg', img)
    img_base64 = base64.b64encode(img_encoded).decode('utf-8')

    # Pass the bounding box coordinates, labels, and image size to the template
    context = {
        'bounding_boxes': bounding_boxes,
        'image': img_base64,
        'image_width': width,
        'image_height': height
    }
    return render(request, 'object_detection/yolo_detection.html', context)
