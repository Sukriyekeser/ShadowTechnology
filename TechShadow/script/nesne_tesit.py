from yolov5 import YOLO

class NesneTespit:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
    
    def detect(self, frame):
        detections = self.model.detect(frame)
        return detections