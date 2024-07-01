import cv2
from ultralytics import YOLO
import pickle
import math

model_path = "yolov8n-pose.pt"
model = YOLO(model_path)

def process_image(image_path):
    frame = cv2.imread(image_path)
    results = model(frame, verbose=False)

    bbox = results[0].boxes.cpu().xyxyn.tolist()
    keypoints = results[0].keypoints.cpu().numpy().xyn.tolist()

    data = {
        "bbox": bbox[0],
        "keypoints": keypoints[0],
        "image_id": pickle.dumps(frame)
    }

    return data

# take distance between each keypoints by comparing data of two images and export the distance list
def take_diffrence(data1, data2):
    k1 = data1["keypoints"]
    k2 = data2["keypoints"]

    diff = []
    for i in range(len(k1)):
        diff.append(math.dist(k1[i], k2[i]))

    return diff


pass