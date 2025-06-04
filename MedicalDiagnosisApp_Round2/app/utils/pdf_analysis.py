# app/utils/pdf_analysis.py

import fitz  # PyMuPDF
import re

def extract_text_from_pdf(file_bytes):
    """Extract text from uploaded PDF file."""
    try:
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        text = "\n".join([page.get_text() for page in doc])
        return text
    except Exception as e:
        return f"PDF parsing failed: {str(e)}"

def analyze_text(text):
    """Perform basic NLP analysis: extract keywords and summary."""
    medical_keywords = [
        "COVID-19", "Pneumonia", "Antibiotics", "RT-PCR", "Chest X-ray",
        "fever", "cough", "oxygen", "infection", "respiratory",
        "broad-spectrum", "breathing", "wheezing", "opacities", "fatigue",
        "pleural effusion", "shortness of breath", "chest pain"
    ]

    found_keywords = [kw for kw in medical_keywords if kw.lower() in text.lower()]

    summary = extract_summary_sections(text)

    return {
        "keywords": found_keywords,
        "summary": summary
    }

def extract_summary_sections(text):
    """Try to extract major report sections using regex (optional)."""
    sections = ["Chief Complaint", "Clinical Findings", "Radiology Findings", "Diagnosis", "Recommendations"]
    extracted = {}

    for section in sections:
        pattern = rf"{section}[:\-]?\s*(.*?)(?=\n\S|\Z)"
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            extracted[section] = match.group(1).strip()

    return extracted
