# 🩻 AI-Powered Medical Diagnosis Web App

A full-stack application that predicts medical conditions like COVID-19 and Pneumonia from chest X-ray images using deep learning, and analyzes uploaded PDF medical reports for medical keywords and diagnosis context.

## 🔧 Tech Stack
- **Frontend:** Streamlit
- **Backend API:** FastAPI
- **Model:** ResNet18 (PyTorch)
- **PDF Parsing:** PyMuPDF (fitz)
- **Image Processing:** torchvision, Pillow

## 🚀 Features
- ✅ Upload chest X-ray image and receive AI-based prediction
- ✅ Upload medical report (PDF) for keyword and symptom extraction
- ✅ Keyword highlighting in extracted medical summaries
- ✅ Streamlit frontend with interactive UI and expandable sections

📁 **Note:** The X-ray dataset is excluded from this repository due to size limits. You may use your own dataset or contact the author to request it.

## 📂 Folder Structure
MedicalDiagnosisApp_Round2/
├── app/
│ ├── main.py # FastAPI backend
│ └── utils/
│ ├── predict.py # Model prediction logic
│ └── pdf_analysis.py # PDF text extraction & analysis
├── models/ # Trained model (model.pth)
├── chest_xray/Data/ # Empty structure with .gitkeep
├── streamlit_app.py # Frontend UI
├── requirements.txt # Required packages
├── README.md



## ⚙️ How to Run the App

### 1. Install Requirements
```bash
pip install -r requirements.txt

uvicorn app.main:app --reload
streamlit run streamlit_app.py


🧠 Model Info
Architecture: ResNet18
Classes: COVID-19, NORMAL, PNEUMONIA
Trained on labeled chest X-ray images (not included in repo)
