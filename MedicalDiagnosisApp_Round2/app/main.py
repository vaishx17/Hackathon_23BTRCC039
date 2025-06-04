# main.py

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from app.utils.predict import predict_image
from app.utils.pdf_analysis import extract_text_from_pdf, analyze_text

app = FastAPI()

# Enable CORS for frontend (Streamlit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Medical Diagnosis API is working."}

@app.post("/predict")
async def predict(file: UploadFile = File(...), report: UploadFile = File(None)):
    # Read image bytes
    image_bytes = await file.read()

    # Get prediction and confidence
    pred_class, confidence = predict_image(image_bytes)

    # Base response
    prediction = {
        "class": pred_class,
        "confidence": confidence
    }

    # If PDF report is provided
    if report is not None:
        try:
            report_bytes = await report.read()
            text = extract_text_from_pdf(report_bytes)
            analysis = analyze_text(text)

            prediction["report_analysis"] = {
                "keywords_found": analysis.get("keywords", []),
                "summary": analysis.get("summary", ""),
                "raw_text_excerpt": text[:300]
            }
        except Exception as e:
            prediction["report_analysis"] = {
                "error": f"Failed to analyze report: {str(e)}"
            }

    return {"prediction": prediction}
