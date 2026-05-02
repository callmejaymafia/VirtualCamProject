# 🎥 Virtual Camera Video Call Project

This project streams any pre-recorded video as a webcam using **OBS Virtual Camera**.  
The video appears as your camera in Zoom, Google Meet, Microsoft Teams, and similar apps.

> ✨ The app now allows users to **choose any video file at startup**.

---

## 📋 Requirements

- Python 3.9+
- OBS Studio (Virtual Camera enabled)

Install libraries:

```bash
pip install -r requirements.txt
```

**`requirements.txt`**

```
opencv-python
pyvirtualcam
numpy
```

---

## 📁 Project Structure

```
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
```

---

## ⚙️ Setup

1. Install **OBS Studio**
2. Open OBS once and click **Start Virtual Camera**, then close OBS.  
   > This installs the virtual webcam driver required by the app.

---

## ▶️ Run the Project

```bash
python main.py
```

**What happens next:**

1. A file picker window opens
2. Select any video file (`mp4` recommended)
3. The virtual camera starts automatically

**Expected terminal output:**

```
Virtual camera started: OBS Virtual Camera
```

> Press **Q** to exit.

---

## 📹 Use in Video Call Apps

Open **Zoom / Google Meet / Microsoft Teams** and set your camera to:

```
OBS Virtual Camera
```

Your selected video will appear as your webcam.

---

## 🚀 Clone and Run

```bash
git clone https://github.com/callmejaymafia/VirtualCamProject.git
cd VirtualCamProject
pip install -r requirements.txt
python main.py
```

---

## 📝 Notes

- Recommended video format: portrait (`720x1280` or `1080x1920`)
- Works best with **Telegram**, **Zoom**, **Google Meet**, **Microsoft Teams**, **Discord**, and **Skype**
- ⚠️ Some apps (e.g., WhatsApp Desktop/Web) do not support virtual cameras