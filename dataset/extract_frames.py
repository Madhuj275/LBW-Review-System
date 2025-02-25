import cv2
import os

# Videos ka folder path
videos_folder = "C:\\Users\\madhu\\Documents\\lbw\\LBW-Review-System\\dataset\\lbw-dataset"

# Frames save karne ka folder
output_folder = "C:\\Users\\madhu\\Documents\\lbw\\LBW-Review-System\\dataset\\images\\train"
os.makedirs(output_folder, exist_ok=True)

# Sabhi videos ke naam list mein daalein
videos = os.listdir(videos_folder)

# Har video ke liye loop chalayein
for video_name in videos:
    # Video ka full path
    video_path = os.path.join(videos_folder, video_name)
    
    # Video open karein
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    # Har frame ko extract karein
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Frame ko image ke roop mein save karein
        frame_filename = f"{video_name}_frame_{frame_count}.jpg"
        cv2.imwrite(os.path.join(output_folder, frame_filename), frame)
        frame_count += 1

    cap.release()
    print(f"{video_name} se {frame_count} frames extract ho gaye hain.")

print("Sabhi videos se frames extract ho chuke hain.")