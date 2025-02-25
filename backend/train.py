from ultralytics import YOLO

# YOLOv8 model load karein
model = YOLO("yolov8n.pt")

# Model ko train karein
results = model.train(data="C:/Users/madhu/Documents/lbw/LBW-Review-System/dataset/dataset.yaml", epochs=50, imgsz=640, batch=16)

# Model ka evaluation karein
metrics = model.val()
print(f"mAP: {metrics.box.map}")  # mAP (mean Average Precision)