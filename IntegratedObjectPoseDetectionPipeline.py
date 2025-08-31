import cv2
import mediapipe as mp
from ultralytics import YOLO
import os

input_video = "/content/videoplayback.mp4"
output_video = "yolo.mp4"

USE_MEDIAPIPE = True
USE_YOLO = True

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=2,
    smooth_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) if USE_MEDIAPIPE else None

yolo_model = YOLO("yolov8n.pt") if USE_YOLO else None

cap = cv2.VideoCapture(input_video)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) or 30.0

out = cv2.VideoWriter(
    output_video,
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (frame_width, frame_height)
)

frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f" Processing {frame_count} frames from {input_video}...")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if yolo_model:
        yolo_results = yolo_model(frame, verbose=False)
        frame = yolo_results[0].plot()

    if pose:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb_frame)

        if results.pose_landmarks:
            landmark_spec = mp_draw.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2)
            connection_spec = mp_draw.DrawingSpec(color=(255, 255, 255), thickness=2)

            mp_draw.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_spec,
                connection_spec
            )

            landmarks = results.pose_landmarks.landmark

            def draw_extra_connection(p1, p2):
                x1 = int(landmarks[p1].x * frame_width)
                y1 = int(landmarks[p1].y * frame_height)
                x2 = int(landmarks[p2].x * frame_width)
                y2 = int(landmarks[p2].y * frame_height)
                cv2.line(frame, (x1, y1), (x2, y2), (255, 255, 255), 2)

            extra_connections = [
                (0, 1), (0, 4), (9, 10),
                (11, 13), (12, 14),
                (13, 15), (14, 16),
                (23, 24), (11, 23), (12, 24),
                (23, 25), (24, 26),
                (25, 27), (26, 28),
                (27, 31), (28, 32)
            ]

            for connection in extra_connections:
                draw_extra_connection(*connection)

    out.write(frame)

cap.release()
out.release()
print(f"✅ Saved processed video to: {output_video}")