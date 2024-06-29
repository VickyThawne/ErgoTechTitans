from ultralytics import YOLO
from config import vision_model
import pickle

class VisionInference:
    def __init__():
        self.model = YOLO(vision_model)

    def process_frame(frame):
        results = model(frame, verbose=False)

        bbox = results[0].boxes.xyxy.tolist()
        keypoints = results[0].keypoints.numpy().xy.tolist()

        all_data = []
        for i in range(len(bbox)):
            data = {
                "bbox": bbox[i],
                "keypoints": keypoints[i],
                "person_id": i,
                "image_id": pickle.dumps(frame)
            }
            all_data.append(data)

        return all_data
