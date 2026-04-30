import cv2
import time
import os


class VideoPlayer:
    def __init__(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Video not found: {path}")

        self.path = path
        self.cap = cv2.VideoCapture(path)

        # Detect video FPS (critical fix)
        self.video_fps = self.cap.get(cv2.CAP_PROP_FPS)
        if self.video_fps <= 0:
            self.video_fps = 25  # fallback safe value

        self.frame_delay = 1 / self.video_fps
        self.last_frame_time = time.time()

        print(f"Loaded video @ {self.video_fps:.2f} FPS")

    def get_frame(self, width, height):
        # 🔹 FPS SYNC (prevents fast playback)
        now = time.time()
        elapsed = now - self.last_frame_time
        if elapsed < self.frame_delay:
            time.sleep(self.frame_delay - elapsed)

        self.last_frame_time = time.time()

        # 🔹 Read frame
        ret, frame = self.cap.read()

        # 🔹 Loop video safely
        if not ret or frame is None:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = self.cap.read()

        if frame is None:
            return None

        # Resize to portrait output
        frame = cv2.resize(frame, (width, height))
        return frame

    def release(self):
        if self.cap.isOpened():
            self.cap.release()