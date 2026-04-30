import pyvirtualcam
from pyvirtualcam import PixelFormat

def start_virtual_camera(frame_generator, width, height, fps=15):
    try:
        with pyvirtualcam.Camera(width=width, height=height, fps=fps, fmt=PixelFormat.BGR) as cam:
            print(f"Virtual camera started: {cam.device}")

            for frame in frame_generator:
                cam.send(frame)
                cam.sleep_until_next_frame()

    except KeyboardInterrupt:
        print("Virtual camera stopped.")