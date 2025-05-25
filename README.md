# ASR_Nvidia_Nemo
![FastAPI - Swagger UI - Brave 5_25_2025 12_52_31 PM](https://github.com/user-attachments/assets/85fccab5-17d4-42d1-8081-2aba163ff972)
![Windows PowerShell 5_25_2025 12_52_20 PM](https://github.com/user-attachments/assets/7fb16c04-43fa-4fc5-b89d-93fd212e8f84)
# NeMo ASR with FastAPI

This project is a lightweight speech-to-text microservice using NVIDIA NeMo for automatic speech recognition (ASR), exposed via a FastAPI REST API.

---

## Features

- Upload `.wav` audio and get real-time transcriptions
-  FastAPI-based inference API
- Uses pretrained NeMo ASR model
- Docker-ready deployment
-  Easily extendable for CI/CD and async inference

---

## Project Structure
nemo_asr_fastapi/
├── main.py # FastAPI app with /transcribe endpoint
├── model.py # Loads and caches the NeMo ASR model
├── requirements.txt # Python dependencies
├── Dockerfile # Container definition
├── Audio.wav # Sample audio for testing
└── README.md
## Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/nemo_asr_fastapi.git
cd nemo_asr_fastapi

## 2. Create & Activate Virtual Environment

python -m venv venv
## .\venv\Scripts\activate       # Windows

## 3. Install Dependencies

pip install -r requirements.txt
## Run FastAPI Server
uvicorn main:app --reload



## Docker Deployment

docker build -t nemo-asr .
docker run -p 8000:8000 nemo-asr

##API Reference
POST /transcribe
Upload a .wav file and receive the transcription.

Request:
Content-Type: multipart/form-data

File: audio/wav

## ⚠️ Notes & Limitations
- Current version supports `.wav` mono 16kHz files
- Larger models may require GPU for best performance
- Async inference and streaming not yet implemented


🧩 Complications & Learnings
FastAPI & file uploads: Faced curl: (26) issues due to incorrect path formats; resolved by proper bracketed paste handling in Git Bash.

Model loading issues: Required careful attention to model checkpoints and tokenizer compatibility in NeMo.

Docker container build: Needed to optimize image size and runtime dependencies for NeMo.

UX testing: Swagger UI was critical for debugging during development.
