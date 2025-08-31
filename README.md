# Real-Time Human Pose & Object Detection 🕺🎯

A project that **tracks human movements in real-time video** using **YOLOv8** for object detection and **MediaPipe Pose** for skeletal landmark estimation. Combines multiple ML frameworks for **efficient human motion analysis**.  

---

## Key Highlights

- **YOLOv8** → Robust object detection in HD video.  
- **MediaPipe Pose** → Extracts and visualizes detailed human skeletal landmarks.  
- **OpenCV** → Processes video frames and generates annotated output.  
- Real-time tracking and visualization.  

---

## How It Works

1. Detect humans/objects in video using YOLOv8.  
2. Estimate human skeleton landmarks using MediaPipe Pose.  
3. Overlay detections and pose connections on the video frame.  
4. Save processed video with annotations.  

---

### Demo Video
<video width="480" controls>
  <source src="yolo(1)(1)(1).mp4" type="video/mp4">
</video>


## Usage

```bash
python human_pose_detection.py
