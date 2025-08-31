---

# Real-Time Object & Human Pose Detection 🕵️‍♂️🚗

A cutting-edge project that **detects and highlights objects** (like humans, cars, etc.) using **YOLOv8**, while simultaneously tracking **human skeletal landmarks** using **MediaPipe Pose**. This demonstrates how combining multiple ML frameworks enables efficient **real-time object and pose analysis**.

---

## Key Features

* **YOLOv8 Object Detection** → Detects humans, cars, and other objects in HD video.
* **MediaPipe Pose Estimation** → Extracts and visualizes human skeletal landmarks.
* **OpenCV Integration** → Annotates frames and outputs processed video.
* **Real-Time Processing** → Works with both video files and webcam input.
* **Customizable Pipelines** → Enable/disable YOLO or MediaPipe as needed.

---

## Installation

1. **Clone the repository**

```bash
https://github.com/amit-chakdhare09/Integrated-Object-Pose-Detection-Pipeline.git

cd real-time-object-pose
```

2. **Install dependencies**

```bash
pip install ultralytics mediapipe opencv-python
```

> Ensure you have **Python 3.8+** installed.

---

## Usage

1. **Configure the script**:

```python
input_video = "path_to_your_video.mp4"
output_video = "output_video.mp4"

USE_YOLO = True       # Enable object detection
USE_MEDIAPIPE = True  # Enable human pose estimation
```

2. **Run the script**

```bash
IntegratedObjectPoseDetectionPipeline.py
```

**What happens:**

* YOLO highlights detected objects like humans, cars, etc.
* MediaPipe overlays human skeletons and extra landmark connections.
* Processed video is saved to the path specified in `output_video`.

---

## Why It Matters

* Demonstrates **multi-framework ML integration** in real-time.
* Useful for **surveillance, sports analytics, autonomous vehicles, and robotics**.
* Provides **object-level awareness** alongside **human pose understanding** in a single system.

---

## Customization

* **Toggle Detection Pipelines:** Use `USE_YOLO` or `USE_MEDIAPIPE` to enable/disable each pipeline.
* **YOLO Model Choice:** Swap `yolov8n.pt` with `yolov8s.pt` or `yolov8m.pt` for higher accuracy.
* **Pose Detection Confidence:** Adjust `min_detection_confidence` and `min_tracking_confidence` in MediaPipe Pose.

---

## Tech Stack

**Python | YOLOv8 | MediaPipe | OpenCV**

---

## References

* [YOLOv8 Documentation](https://docs.ultralytics.com/)
* [MediaPipe Pose Documentation](https://drone-vis.readthedocs.io/en/latest/pose/mediapipe.html)
* [OpenCV Python Documentation](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)

---

## License

**MIT License** © 2025 Amit Omprakash Chakdhare

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

---

