
# LBW Review System 🏏  

The **LBW (Leg Before Wicket) Review System** is a **computer vision-based** project that analyzes cricket match videos to determine if a batsman is out or not based on **LBW rules**.  

This system utilizes **YOLOv8 for object detection** and **Flask for the backend** to process cricket match videos.  

---

## 🚀 Features  

✅ **Video Upload** – Upload cricket match videos for analysis.  
✅ **Object Detection** – Detects ball, batsman, stumps, and pitch using **YOLOv8**.  
✅ **LBW Decision System** – Applies cricket **LBW rules** to determine if the batsman is out.  
✅ **User Interface** – Simple web-based UI for easy interaction.  

---


## 🛠 Installation  

### **Prerequisites**  
- Python **3.8+**  
- pip (Python package manager)  
- Git installed  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-username/LBW-Review-System.git
cd LBW-Review-System
```

### **2️⃣ Install Dependencies**  
```bash
pip install -r backend/requirements.txt
```

### **3️⃣ Download YOLOv8 Model**  
- Download **`yolov8n.pt`** from the [Ultralytics Repository](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt).  
- Place it in the `models/` folder.  

### **4️⃣ Prepare Dataset**  
- Store training data inside `dataset/` folder.  
- Annotate using **LabelImg** ([GitHub](https://github.com/tzutalin/labelImg)).  
- Modify `dataset/dataset.yaml` accordingly.  

### **5️⃣ Train the Model (Optional)**  
```bash
python backend/train.py
```

### **6️⃣ Run the Backend Server**  
```bash
python backend/app.py
```

### **7️⃣ Open the Frontend**  
- Open `frontend/index.html` in a browser.  
- Upload a cricket match video and get LBW results.  

---

## 🎮 How to Use  

1️⃣ **Upload a cricket match video** via the web interface.  
2️⃣ **System processes the video** using **YOLOv8** for object detection.  
3️⃣ **LBW logic** is applied to detect if the batsman is **Out or Not Out**.  
4️⃣ **Results** are displayed on the web interface.  

---

## 📊 Dataset Structure  

```
dataset/
├── images/
│   ├── train/            # Training images
│   └── val/              # Validation images
├── labels/
│   ├── train/            # YOLO format labels for training
│   └── val/              # YOLO format labels for validation
└── dataset.yaml          # Dataset configuration
```

- Use [LabelImg](https://github.com/tzutalin/labelImg) to annotate images.  
- Save annotations in **YOLO format**.  

---

## 🧠 Model Training  

1️⃣ Ensure dataset is properly structured.  
2️⃣ Train model using:  
```bash
python backend/train.py
```
3️⃣ Trained model is saved at `runs/detect/train/weights/best.pt`.  
4️⃣ Move `best.pt` to the `models/` folder for inference.  

---



