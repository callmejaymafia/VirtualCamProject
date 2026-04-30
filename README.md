Virtual Camera Video Call Project

This project streams a pre-recorded video as a webcam using OBS Virtual Camera.
It allows the video to appear as your camera in Zoom, Google Meet, Teams and similar apps.

Requirements
Python 3.9+
OBS Studio (Virtual Camera enabled)

Install Python libraries:

pip install -r requirements.txt

requirements.txt

opencv-python
pyvirtualcam
numpy
Project Structure
VirtualCamProject/
│
├── main.py
├── requirements.txt
│
├── processing/
│   └── video_player.py
│
├── output/
│   └── virtual_camera.py
│
└── assets/
    └── videos/
        └── presentation.mp4
Setup
Install OBS Studio and start the Virtual Camera once.
Place your video file in:
assets/videos/presentation.mp4

Recommended format: portrait (720x1280 or 1080x1920).

Run the Project
python main.py

You should see:

Virtual camera started: OBS Virtual Camera
Use in Video Call Apps

Open Zoom / Meet / Teams and set the camera to:

OBS Virtual Camera

Your video will appear as your webcam.

Clone the Project
git clone https://github.com/YOUR_USERNAME/VirtualCamProject.git
cd VirtualCamProject
pip install -r requirements.txt
python main.py
