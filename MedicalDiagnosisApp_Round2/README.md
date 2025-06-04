# 🩻 AI-Powered Medical Diagnosis Web App

A full-stack application that predicts medical conditions like COVID-19 or Pneumonia from chest X-ray images and analyzes uploaded PDF medical reports for symptoms and diagnostic context.

## 🔧 Tech Stack
- **Frontend:** Streamlit
- **Backend:** FastAPI
- **Model:** ResNet18 (PyTorch)
- **PDF Parsing:** PyMuPDF
- **Image Classification:** Torch + torchvision

## 🚀 Features
- Upload Chest X-ray and get predictions (COVID-19, Normal, Pneumonia)
- Upload medical reports (PDF) and extract key symptoms and highlights
- Clean UI with expandable keyword summary

## 📂 Folder Structure
See the project structure above.

## ⚙️ Running the App
1. **Start the FastAPI server:**
```bash
uvicorn app.main:app --reload
