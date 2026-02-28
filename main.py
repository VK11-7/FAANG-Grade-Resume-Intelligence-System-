import streamlit as st
import PyPDF2
import io
import re
import numpy as np
import matplotlib.pyplot as plt

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage


# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(page_title="AI Resume Intelligence", page_icon="📄", layout="wide")

st.title("📄 AI Resume Intelligence System")
st.markdown("ATS Match • Section Scoring • Radar Visualization")


# ==========================
# LOAD MODEL
# ==========================
@st.cache_resource
def load_model():
    return ChatOllama(model="llama3")

model = load_model()


# ==========================
# FILE UPLOAD
# ==========================
uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
job_description = st.text_area("Paste Job Description (Required for ATS Match)")
analyse_button = st.button("🚀 Analyse Resume")


# ==========================
# PDF TEXT EXTRACTION
# ==========================
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text


# ==========================
# SIMPLE ATS MATCH (Keyword-Based)
# ==========================
def calculate_ats_score(resume_text, job_desc):
    resume_words = set(re.findall(r"\b\w+\b", resume_text.lower()))
    job_words = set(re.findall(r"\b\w+\b", job_desc.lower()))

    common = resume_words.intersection(job_words)

    if len(job_words) == 0:
        return 0

    return round((len(common) / len(job_words)) * 100)


# ==========================
# LLM SECTION SCORING
# ==========================
def get_section_scores(resume_text, job_desc):

    prompt = f"""
You are a professional resume evaluator.

Based on the resume and job description below:

Provide numeric scores out of 10 for:
- Skills
- Experience
- Education
- Impact & Quantification
- ATS Optimization

Respond ONLY in this exact JSON format:

{{
"skills": X,
"experience": X,
"education": X,
"impact": X,
"ats": X
}}

Resume:
{resume_text}

Job Description:
{job_desc}
"""

    response = model.invoke([HumanMessage(content=prompt)])

    try:
        scores = eval(response.content)
    except:
        scores = {
            "skills": 5,
            "experience": 5,
            "education": 5,
            "impact": 5,
            "ats": 5
        }

    return scores


# ==========================
# RADAR CHART
# ==========================
def plot_radar(scores):
    labels = list(scores.keys())
    values = list(scores.values())

    values += values[:1]
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 10)

    return fig


# ==========================
# MAIN ANALYSIS
# ==========================
if analyse_button and uploaded_file and job_description:

    with st.spinner("Analyzing Resume..."):

        resume_text = extract_text_from_pdf(io.BytesIO(uploaded_file.read()))

        if not resume_text.strip():
            st.error("Could not extract text from PDF.")
            st.stop()

        # ATS Score
        ats_score = calculate_ats_score(resume_text, job_description)

        # Section Scores
        section_scores = get_section_scores(resume_text, job_description)

        # Overall Score
        overall_score = round(sum(section_scores.values()) / len(section_scores), 1)

    # ==========================
    # DISPLAY RESULTS
    # ==========================
    st.subheader("📊 Resume Analysis Results")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Overall Resume Score (LLM)", f"{overall_score}/10")
        st.metric("ATS Match Percentage", f"{ats_score}%")

    with col2:
        st.write("### Section-wise Scores")
        for key, value in section_scores.items():
            st.write(f"{key.capitalize()}: {value}/10")

    # Radar Chart
    st.subheader("📈 Performance Radar")
    fig = plot_radar(section_scores)
    st.pyplot(fig)

    # ==========================
    # Detailed Feedback
    # ==========================
    st.subheader("🧠 AI Feedback")

    feedback_prompt = f"""
Provide structured feedback on this resume.
Highlight strengths, weaknesses, and 5 specific improvements.

Resume:
{resume_text}

Job Description:
{job_description}
"""

    feedback_response = model.invoke([HumanMessage(content=feedback_prompt)])
    st.write(feedback_response.content)


elif analyse_button:
    st.warning("Please upload resume and paste job description.")


st.markdown("---")
st.markdown("Powered by Ollama + Streamlit")