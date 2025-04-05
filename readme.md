# 🧠 Wanderlens

A secure, modular Flask-based API server that integrates:

- 📸 Facial recognition using **Dlib**
- 🧠 AI suggestions powered by **Gemini**
- 📦 Trip data management using **MongoDB**
- 🖼️ Bulk image processing for face analysis
- 🌐 Fully CORS-enabled for cross-origin support

---

## 🚀 Features

- **Flask REST API** with professional and predictable endpoints
- **CORS (Cross-Origin Resource Sharing)** security using `flask-cors`
- **Dlib-powered Facial Recognition** (HOG/CNN based)
- **Gemini AI Integration** for content/suggestion generation
- **MongoDB-backed** storage for trip data
- **Robust file handling** with `tempfile` for safe image uploads
- **Structured JSON responses** for easy frontend integration

---

## 📡 API Endpoints

| Endpoint                     | Method | Description                          |
|-----------------------------|--------|--------------------------------------|
| `/`                         | GET    | Welcome message                      |
| `/api/trips`                | GET    | Fetch recent trip entries            |
| `/api/trips`                | POST   | Create a new trip entry              |
| `/api/ai/suggestions`       | POST   | Get AI-generated suggestions         |
| `/api/faces/process`        | POST   | Upload & process images for faces    |

---

## 🛠 Tech Stack

- **Backend:** Python Flask
- **Database:** MongoDB
- **AI Model:** Google Gemini (`gemini-2.0-flash`)
- **Facial Recognition:** Dlib, OpenCV
- **Deployment:** Render
- **Other:** dotenv, logging, NumPy, Pandas

---

## 📁 Project Structure
Wanderlens-Server/
│
├── __pycache__/                # Auto-generated Python cache files
│
├── mongo/                     # MongoDB utility functions
│   └── db.py                  # Handles insert and fetch operations
│
├── .gitignore                 # Git ignore rules
├── GenAI.py                   # Handles AI (Gemini) interactions
├── Main.py                    # Main Flask app with API endpoints
├── har_default.xml            # Haar Cascade model for face detection
├── model.py                   # Dlib-based facial recognition logic
├── readme.md                  # Project README file
├── requirements.txt           # Python dependencies
├── solovsgroup.py             # Classifier for solo vs group images
├── startup.sh                 # Shell script for startup (Render or other hosts)
├── yolo11n.pt                 # YOLOv5/YOLOv7/YOLOv8 model for image classification
└── yunet.onnx                 # ONNX model for face detection (YuNet)

