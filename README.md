# 🔍 Dynamic URL RAG Playground

An end-to-end Retrieval-Augmented Generation (RAG) system that dynamically scrapes any web URL, retrieves relevant content using embeddings, and generates answers using customizable decoding strategies through an interactive Streamlit UI.

---
DEMO Vedio:
1)StreamLit:https://youtu.be/Y_tANhJKFrw
2)FASTAPI:https://youtu.be/wNCoJl0fCoM
## Project Overview

This project implements a **Dynamic RAG pipeline** where users can:

- Paste any public web URL
- Ask a question about the content
- Retrieve semantically relevant context
- Generate answers using multiple decoding strategies
- Experiment with temperature, top-k, top-p, beam search, and repetition penalty

Unlike static RAG demos, this system builds the retrieval index **on-the-fly** for any provided URL.

---

##  Architecture

### 1️ Ingestion Layer
- Web scraping
- HTML cleaning
- Text chunking
- Embedding generation
- Vector storage

### 2️ Retrieval Layer
- Query embedding
- Semantic similarity search
- Top-k context retrieval

### 3️ Generation Layer
- Prompt construction
- LLM-based response generation
- Multiple decoding strategies:
  - Greedy Search
  - Beam Search
  - Top-K Sampling
  - Top-P (Nucleus) Sampling

### 4️ Interface Layer
- **FastAPI** backend for model serving
- **Streamlit** frontend for interactive experimentation

---

##  Decoding Strategies Supported

| Strategy  | Description |
|------------|-------------|
| Greedy     | Deterministic token selection |
| Beam Search | Explores multiple candidate sequences |
| Top-K      | Samples from top-k probable tokens |
| Top-P      | Samples from cumulative probability mass |

Adjustable parameters:
- Temperature
- Top-K
- Top-P
- Repetition Penalty
- Beam Width
- Max Tokens

---

##  Tech Stack

- Python
- PyTorch
- Hugging Face Transformers
- FastAPI
- Streamlit
- Sentence Transformers
- BeautifulSoup
- Uvicorn


---

## ⚙ Installation

### 1️ Clone Repository

git clone https://github.com/your-username/dynamic-url-rag.git
cd dynamic-url-rag

Create Virtual Environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

Install Dependencies:
pip install -r requirements.txt

Running the Application:
Step 1 — Start FastAPI Backend:

uvicorn server.api:app --reload


Step 2 — Start Streamlit Frontend (New Terminal):

streamlit run playground/streamlit_app.py

