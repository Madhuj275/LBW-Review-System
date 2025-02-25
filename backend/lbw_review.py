from ultralytics import YOLO
import cv2

def process_video(video_path):
    # Load the trained YOLO model
    model = YOLO("models/best.pt")  # Use your trained model
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    ball_positions = []
    
    # Process each frame of the video
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Detect objects in the frame
        results = model(frame)
        for box in results[0].boxes:
            if model.names[int(box.cls)] == 'ball':  # Detect ball
                x, y = box.xywh[0][:2].cpu().numpy()
                ball_positions.append((x, y))
    
    # Release the video file
    cap.release()
    
    # Dummy decision logic (replace with actual logic)
    if len(ball_positions) > 0:
        return "Out"
    else:
        return "Not Out"