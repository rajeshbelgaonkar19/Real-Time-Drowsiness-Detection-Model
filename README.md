# Drowsiness Detection System

This repository contains a complete solution for real-time drowsiness detection and object detection using deep learning. The project is divided into three main components:

- **Drowsiness-Detection-Final**: Full-stack web application (Frontend + Backend) for real-time driver drowsiness detection.
- **Newmodel**: Standalone backend for drowsiness detection with a simple API.
- **Jupyter Notebook**: Experiments for object detection (vehicles and people) and drowsiness/awake state classification using YOLO models.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Functionalities](#functionalities)
- [Benefits](#benefits)
- [Setup & Installation](#setup--installation)
  - [1. Drowsiness-Detection-Final (Full Stack)](#1-drowsiness-detection-final-full-stack)
  - [2. Newmodel (Backend Only)](#2-newmodel-backend-only)
  - [3. Jupyter Notebook (Object Detection)](#3-jupyter-notebook-object-detection)
- [Usage](#usage)
- [References](#references)

---

## Project Structure

```
Drowsiness Detection/
│
├── Drowsiness-Detection-Final/
│   ├── backend/         # Flask backend for drowsiness detection
│   └── frontend/        # React frontend for user interaction
│
├── Newmodel/            # Standalone backend for drowsiness detection
│
├── Drowiness Detection.ipynb  # Jupyter Notebook for object detection experiments
│
└── README.md            # Project documentation
```

---

## Functionalities

### Drowsiness-Detection-Final

- **Backend (Flask):**
  - Real-time video capture and facial landmark detection.
  - Eye Aspect Ratio (EAR) and Mouth Aspect Ratio (MAR) calculation.
  - Triggers alarm and visual alerts if drowsiness or yawning is detected.
  - API endpoints for frontend communication.

- **Frontend (React + Vite):**
  - User-friendly interface to start/stop detection.
  - Real-time status display (Active, Drowsy, Sleeping, Yawning).
  - Visual feedback and statistics.

### Newmodel

- Standalone Flask backend for drowsiness detection.
- Simple API to start detection (`/start` endpoint).
- Uses OpenCV, dlib, and pygame for detection and alarm.

### Jupyter Notebook

- Object detection using YOLOv5/YOLOv8 models.
- Detects vehicles and people in images and videos.
- Classifies people as "awake" or "sleepy" based on model predictions.
- Visualization of detection results.

---

## Benefits

- **Safety**: Helps prevent accidents by alerting drowsy drivers in real time.
- **Automation**: Fully automated detection using computer vision and deep learning.
- **Extensible**: Modular codebase for easy extension and integration.
- **User-Friendly**: Web interface for easy operation and monitoring.
- **Research-Ready**: Jupyter notebook for experimentation and further development.

---

## Setup & Installation

### 1. Drowsiness-Detection-Final (Full Stack)

#### Prerequisites

- Python 3.x
- Node.js & npm
- (Recommended) Virtual environment for Python

#### Backend Setup

```sh
cd Drowsiness-Detection-Final/backend
pip install -r requirements.txt  # If requirements.txt exists, else install:
pip install opencv-python numpy dlib pygame imutils flask flask-cors
python app.py
```

#### Frontend Setup

```sh
cd Drowsiness-Detection-Final/frontend
npm install
npm run dev
```

- The frontend will be available at [http://localhost:5173](http://localhost:5173)
- The backend runs at [http://localhost:5000](http://localhost:5000)

### 2. Newmodel (Backend Only)

#### Prerequisites

- Python 3.x

#### Setup

```sh
cd Newmodel
pip install -r requirements.txt  # Or manually install:
pip install opencv-python numpy dlib pygame imutils flask flask-cors
python app.py
```

- Starts backend server at [http://localhost:5000](http://localhost:5000)
- POST to `/start` to begin detection.

### 3. Jupyter Notebook (Object Detection)

#### Prerequisites

- Python 3.x
- Jupyter Notebook or Google Colab

#### Setup

Install dependencies (in notebook or terminal):

```sh
pip install torch torchvision torchaudio ultralytics opencv-python numpy matplotlib
```

#### Usage

- Open `Drowiness Detection.ipynb` in Jupyter or Colab.
- Run cells to perform object detection on images, videos, or webcam.
- Detects vehicles, people, and classifies drowsiness/awake state.

---

## Usage

- **For full-stack app:** Start both backend and frontend as described above. Use the web interface to monitor drowsiness in real time.
- **For backend only:** Start the backend and trigger detection via API.
- **For research/experiments:** Use the Jupyter notebook for detection and visualization.

---

## References

- [Scikit-Learn Documentation](https://scikit-learn.org/)
- [Python for Machine Learning](https://docs.python.org/3/)
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)
- [OpenCV](https://opencv.org/)
- [dlib](http://dlib.net/)

---

**Contributors:**  
- [Your Name Here]

**License:**  
- [Specify your license here]
