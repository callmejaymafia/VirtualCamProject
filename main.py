import cv2
import tkinter as tk
from tkinter import filedialog
from processing.video_player import VideoPlayer
from output.virtual_camera import start_virtual_camera

TARGET_WIDTH = 720
TARGET_HEIGHT = 1280


def pick_video_file():
    root = tk.Tk()
    root.withdraw()  # hide main window
    file_path = filedialog.askopenfilename(
        title="Select a video for your virtual camera",
        filetypes=[("Video files", "*.mp4 *.mov *.avi *.mkv")]
    )
    return file_path


def frame_stream(video_player):
    while True:
        frame = video_player.get_frame(TARGET_WIDTH, TARGET_HEIGHT)

        if frame is None:
            continue

        cv2.imshow("VirtualCam Preview", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        yield frame

    cv2.destroyAllWindows()


if __name__ == "__main__":
    print("Choose a video file...")
    video_path = pick_video_file()

    if not video_path:
        print("No video selected. Exiting.")
        exit()

    print("Selected video:", video_path)

    video_player = VideoPlayer(video_path)
    start_virtual_camera(frame_stream(video_player), TARGET_WIDTH, TARGET_HEIGHT, 15)