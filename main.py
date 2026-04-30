import cv2
from processing.video_player import VideoPlayer
from output.virtual_camera import start_virtual_camera

TARGET_WIDTH = 720
TARGET_HEIGHT = 1280
FPS = 15

video_player = VideoPlayer("assets/videos/presentation.mp4")


def frame_stream():
    print("Press Q to quit")

    while True:
        frame = video_player.get_frame(TARGET_WIDTH, TARGET_HEIGHT)

        if frame is None:
            continue

        # Preview window (for debugging/demo)
        cv2.imshow("VirtualCam Preview", frame)

        # Handle quit safely
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            print("Exiting...")
            break

        yield frame

    video_player.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    start_virtual_camera(frame_stream(), TARGET_WIDTH, TARGET_HEIGHT, FPS)