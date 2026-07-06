#  Ahmet's CV Analyzer

A practice project that demonstrates **Retrieval-Augmented Generation (RAG)** by building an AI assistant capable of answering questions about **Ahmet's CV**.

The application retrieves relevant information from the resume using vector search and generates context-aware responses with an LLM.

---

##  Features

-  Reads a PDF resume
-  Splits the document into chunks
-  Generates embeddings using Sentence Transformers
-  Stores embeddings in ChromaDB
-  Retrieves the most relevant sections with semantic search
-  Generates answers using an LLM through LiteLLM
-  Interactive chat interface built with Streamlit

---

##  Tech Stack

- Python
- Streamlit
- ChromaDB
- Sentence Transformers
- LiteLLM
- PyPDF
- python-dotenv

---

##  Project Structure

```
.
├── app.py              # Streamlit interface
├── ingest.py           # Creates embeddings from the CV
├── answer.py           # Retrieves context and generates answers
├── cv.pdf              # Resume used for the demo
├── cv_chromadb/        # ChromaDB vector database
├── requirements.txt
└── README.md
```

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/cv-analyzer.git
cd cv-analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
```

---

##  Usage

### 1. Generate embeddings

```bash
python ingest.py
```

### 2. Launch the application

```bash
streamlit run app.py
```

Open the URL provided by Streamlit in your browser.

---

##  Example Questions

- Tell me about Ahmet's education.
- What programming languages does Ahmet know?
- What AI technologies has Ahmet worked with?
- Does Ahmet have Flutter experience?
- Summarize Ahmet's projects.

---

##  Purpose

This repository was created as a **learning project** to explore the fundamentals of **Retrieval-Augmented Generation (RAG)**, vector databases, semantic search, and LLM-powered question answering.

The assistant is specifically designed to answer questions about **Ahmet's CV** and is intended for educational purposes rather than production use.

---


## Author
Ahmet Hamdi ÇINAROĞLU
