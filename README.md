# 🚀 FAANG-Grade Resume Intelligence System

An AI-powered resume evaluation and ranking system that analyzes how well a candidate’s resume aligns with a given job description using advanced NLP, embeddings, and LLM-based scoring.

---

## 📌 Overview

This project is designed to simulate a **FAANG-level resume screening system** by combining:

- Semantic similarity using embeddings
- LLM-based structured evaluation
- Keyword gap analysis
- Role-based weighted scoring

The system provides **actionable insights, scoring breakdowns, and automated PDF reports**, helping candidates optimize their resumes for specific roles.

---

## 🧠 Key Features

- 🔍 **Semantic Matching**
  - Uses `all-MiniLM-L6-v2` embeddings + cosine similarity
  - Measures contextual similarity between resume and job description

- 🤖 **LLM-Based Evaluation**
  - Uses **Llama3 (via Ollama)** for structured scoring
  - Evaluates:
    - Skills relevance
    - Experience alignment
    - Project quality
    - Overall fit

- 🧩 **Keyword Gap Analysis**
  - Identifies missing or weak keywords
  - Highlights improvement areas for ATS optimization

- ⚖️ **Role-Based Weighted Scoring**
  - Assigns weights to different evaluation components
  - Produces a final composite score

- 📊 **Interactive Streamlit Dashboard**
  - Upload resume + job description
  - View real-time evaluation and insights

- 📄 **Automated PDF Report Generation**
  - Generates detailed performance reports
  - Includes scores, feedback, and recommendations

---

## 🏗️ System Architecture

Resume + Job Description <br>
│ <br>
▼ <br>
Text Preprocessing <br>
│ <br>
▼ <br>
Embedding Generation (MiniLM) <br>
│ <br>
▼ <br>
Cosine Similarity Scoring <br>
│ <br>
▼ <br>
LLM Evaluation (Llama3) <br>
│ <br>
▼ <br>
Keyword Gap Analysis <br>
│ <br>
▼ <br>
Weighted Score Aggregation <br>
│ <br>
▼ <br>
Streamlit UI + PDF Report <br>

---

## 🛠️ Tech Stack

- **Frontend/UI:** Streamlit  
- **NLP & Embeddings:** SentenceTransformers (`all-MiniLM-L6-v2`)  
- **LLM:** Llama3 (via Ollama)  
- **Vector DB:** ChromaDB  
- **ML Utilities:** Scikit-learn  
- **Data Processing:** NumPy  
- **Report Generation:** ReportLab  

---

## ⚙️ Installation

```bash:
# Clone the repository
git clone https://github.com/your-username/resume-intelligence-system.git
cd resume-intelligence-system

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
---

📈 Evaluation Metrics
Semantic Similarity Score <br>
LLM-Based Structured Score <br>
Keyword Match Percentage <br>
Final Weighted Score <br>

---

Varadharajan K
