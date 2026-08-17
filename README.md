# RTSP Stream Viewer

This project streams video from an IP camera using RTSP protocol and displays it in real-time with OpenCV.

## 📌 Prerequisites
- Python 3.12+
- `opencv-python` and `pyrtsp` packages (install via `pip install -r requirements.txt`)
- System dependencies: `libgl1`, `libglib2.0-0`, `libsm6`, `libxrender1`, `libfontconfig1`, `ffmpeg`

## 🛠️ Installation
1. Clone or extract the project directory.
2. Create a virtual environment:
   ```bash
   python3 -m venv env && source env/bin/activate
   ```
3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure system libraries are installed (if issues occur):
   ```bash
   sudo apt update && sudo apt install -y libgl1 libglib2.0-0 libsm6 libxrender1 libfontconfig1 ffmpeg
   ```

## 🎥 Usage
Run the script:
```bash
python rtsp_stream.py
```

## 🔐 RTSP Configuration
Edit the `rtsp_url` variable in `rtsp_stream.py` with your camera credentials and IP address.
Example:
```python
rtsp_url = "rtsp://bradj:7334@192.168.68.54:554/live/ch1"
```

## ⚠️ Notes
- If running without GUI (e.g., headless server), modify the script to save video to a file instead of displaying it.
- Ensure your network allows access to `192.168.68.54:554`.