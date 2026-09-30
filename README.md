# OpenCV & Face Recognition Project

This repository contains a comprehensive collection of computer vision scripts, ranging from basic OpenCV image processing techniques to an advanced, robust Face Recognition and Tracking system.

## 🚀 Overview

The project is divided into two main parts:
1. **OpenCV Fundamentals:** A series of modular scripts covering the basics of image manipulation, drawing, video processing, blurring, edge detection, and object detection.
2. **Advanced Face Recognition System (`project1`):** A fully functional video processing pipeline that detects, identifies, and tracks individuals across video frames. It features robust tracking that correctly handles temporary occlusions and absences, counting actual entry and re-entry events.

## 📁 Project Structure

```text
opencv_project/
├── 1_image_handling_basics/       # Loading, saving, displaying, and grayscale conversion
├── 2_image_resizing_shaping/      # Image resizing and shaping techniques
├── 3_image_drawing_function/      # Drawing shapes and text on images
├── 4_video_functions/             # Video capturing and processing basics
├── 5_blour_functions/             # Image blurring and smoothing
├── 6_edges_declaration_opencv/    # Edge detection algorithms
├── 7_contour_and_shapes_detections/ # Contour mapping and shape analysis
├── 8_face_object_detection/       # Haar Cascade object/face detection
└── project1/                      # Advanced Face Recognition System
    └── project.py                 # Main tracking script
```

## 🧠 Advanced Face Recognition System (`project1`)

Located in the `project1/` directory, this system uses the `face_recognition` library to accurately track individuals in a video stream. 

### Key Features:
- **Persistent Tracking:** Identifies unique individuals (e.g., Person 1, Person 2) and remembers them even if they leave and return.
- **Smart Appearance Counting:** Intelligently counts appearances based on actual entry and exit events.
- **Time-Based Grace Period:** Uses a configurable time window (`MISSING_GRACE_SECONDS`) to prevent false "exits" caused by temporary detection failures (e.g., looking away, head turning).
- **Dynamic Encoding Bank:** Keeps a diverse set of facial encodings for each person, making re-identification robust to changes in lighting and angles.
- **Annotated Output:** Generates an output video with bounding boxes, labels, and real-time tracking information.

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd opencv_project
   ```

2. **Set up a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required dependencies:**
   Ensure you have `cmake` installed on your system (required for `dlib` which is a dependency of `face_recognition`).
   ```bash
   pip install opencv-python numpy face_recognition
   ```
   *(Note: Depending on your OS, you may need to install `dlib` separately if it fails to build).*

## 💻 Usage

To run the main Face Recognition System:

```bash
cd project1
python project.py
```

The script will process the configured input video, display real-time progress, and output a final appearance report to the console along with an annotated output video.

## ⚙️ Configuration (`project1/project.py`)

You can tune the system for different environments by modifying the constants at the top of `project1/project.py`:

- `INPUT_VIDEO` / `OUTPUT_VIDEO`: Paths to your source and destination videos.
- `FACE_MATCH_THRESHOLD` (Default: `0.55`): Lower values enforce stricter matching, while higher values are more tolerant.
- `MISSING_GRACE_SECONDS` (Default: `5.0`): The time in seconds a person can be absent (undetected) before the system counts it as a genuine exit. Tune this to prevent false re-entries.
- `SCALE` (Default: `0.5`): Resizes the video for faster processing.
- `ENCODING_SAMPLE_INTERVAL` (Default: `5`): Adds a new encoding to the person's memory bank every N frames to handle varying facial angles over time.
