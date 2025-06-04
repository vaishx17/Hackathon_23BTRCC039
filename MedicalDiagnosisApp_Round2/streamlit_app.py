import streamlit as st
import requests
import fitz  # PyMuPDF
import re
from html import escape
def format_for_display(text, keywords):
    # Keyword highlighting (bold)
    keywords_sorted = sorted(set(keywords), key=len, reverse=True)
    for kw in keywords_sorted:
        pattern = re.compile(re.escape(kw), re.IGNORECASE)
        text = pattern.sub(f"**{kw}**", text)
    # Clean up and structure known sections
    replacements = {
        "Medical Report": "📋 **Medical Report**",
        "Patient Information": "\n👤 **Patient Information**",
        "Name:": "- **Name:**",
        "Age:": "- **Age:**",
        "Gender:": "- **Gender:**",
        "Patient ID:": "- **Patient ID:**",
        "Date of Examination:": "\n📅 **Date of Examination:**",
        "Clinical Findings": "\n🩺 **Clinical Findings:**",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    # Improve paragraph spacing
    text = re.sub(r"\n{2,}", "\n", text)
    text = text.replace("\n", "\n\n")
# REMOVE Vital signs section entirely
    # Remove 'signs at the time of examination were...' and everything after it
    text = re.sub(r"\s*signs at the time of examination were:.*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*Vital.*", "", text, flags=re.IGNORECASE)

    return text.strip()

# Streamlit layout
st.set_page_config(page_title="Medical Diagnosis", layout="centered")
st.title("🩻 AI-Powered Medical Diagnosis")
# Upload Chest X-ray
image_file = st.file_uploader("📤 Upload Chest X-ray Image", type=["jpg", "jpeg", "png"])
# Upload Medical Report PDF
report_file = st.file_uploader("📑 Upload Medical Report (PDF)", type=["pdf"])
# Extract and show PDF content
if report_file:
    st.subheader("📄 Extracted Text from Medical Report:")
    doc = fitz.open(stream=report_file.read(), filetype="pdf")
    text = "\n".join([page.get_text() for page in doc])
    st.text_area("Report Content", text, height=300)
# Predict button
if image_file and st.button("🔍 Predict Diagnosis"):
    files = {"file": image_file}
    if report_file:
        report_file.seek(0)
        files["report"] = report_file
    try:
        response = requests.post("http://127.0.0.1:8000/predict", files=files)
        if response.status_code == 200:
            result = response.json()
            st.success(f"🩺 Prediction: {result['prediction']['class']}")
            st.info(f"📊 Confidence: {float(result['prediction']['confidence']) * 100:.2f}%")
            
            if "report_analysis" in result["prediction"]:
                st.subheader("📊 Medical Report Analysis")
                keywords = result["prediction"]["report_analysis"]["keywords_found"]
                raw_excerpt = result["prediction"]["report_analysis"]["raw_text_excerpt"]
                st.markdown("🔑 **Keywords Found:** " + ", ".join(keywords))
                formatted_text = format_for_display(raw_excerpt, keywords)
                with st.expander("📃 Highlighted Summary"):
                    st.markdown(formatted_text)

        else:
            st.error("❌ Prediction failed. Server error.")
    except Exception as e:
        st.error(f"❌ Request failed: {str(e)}")