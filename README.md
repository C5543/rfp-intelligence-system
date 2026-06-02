# RFP Intelligence System (RAG) 📄🤖

A Retrieval-Augmented Generation (RAG) system designed to help proposal writers and RFP managers retrieve company knowledge and generate grounded responses from internal documents.



---

## 📌 Project Overview

This project builds an RFP Intelligence System using Retrieval-Augmented Generation (RAG).

The system ingests company documents, converts them into vector embeddings, stores them in FAISS, retrieves relevant information based on user questions, and generates grounded responses using GPT-4o-mini.

---

## 🎯 Objectives

- Ingest internal company documents
- Build a searchable knowledge base
- Perform semantic retrieval
- Generate grounded answers using LLMs
- Evaluate retrieval and generation quality
- Deploy the solution through FastAPI

---

## 🏗️ Architecture

<p align="center">

PDF / DOCX / XLSX

↓

Chunking

↓

Embeddings

↓

FAISS

↓

Similarity Search

↓

GPT-4o-mini

↓

Response

</p>

---

## 📂 Data Processing Pipeline

### Step 1: Document Ingestion

Supported document types:

- PDF
- DOCX
- XLSX

### Step 2: Chunking

Documents are split using:

- RecursiveCharacterTextSplitter
- Chunk Size: 500
- Chunk Overlap: 100

### Step 3: Embeddings

Embedding Model:

- BAAI/bge-small-en-v1.5

### Step 4: Vector Storage

Vector Database:

- FAISS

---

## 🔍 Retrieval Layer

Implemented retrieval features:

- Top-K Similarity Search
- Semantic Retrieval
- Context Extraction

Current configuration:

- k = 4 retrieved chunks

---

## 🤖 Generation Layer

### LLM

- GPT-4o-mini

### Prompt Strategy

- Use only retrieved context
- Avoid hallucinations
- Return concise and structured answers
- Refuse unsupported answers

Example:

```text
You are an RFP assistant.

Use ONLY the provided context.

If answer is missing, say:
"I don't know."
```

---

## 📊 Evaluation

### Evaluation Dataset

- What is this RFP about?
- What services are mentioned?
- What is the business problem?
- Who is the client?

### Metrics Evaluated

- Retrieval Success
- Answer Relevance
- Grounded Responses

### Output

```text
evaluation_results.json
```

---

## 🚀 Deployment

### Deployment Tool

- FastAPI

### Endpoint

```http
POST /ask
```

### Request

```json
{
  "query": "What is this RFP about?"
}
```

### Response

```json
{
  "answer": "..."
}
```

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|------------|
| Language | Python |
| Framework | LangChain |
| API | FastAPI |
| Embeddings | BAAI/bge-small-en-v1.5 |
| Vector Database | FAISS |
| LLM | GPT-4o-mini |
| Evaluation | Custom Evaluation Script |

---

## 📁 Repository Structure

```text
rfp_intelligence_system/
│
├── ingestion.py
├── rag_chain.py
├── evaluation.py
├── main.py
├── llm.py
├── prompt.py
│
├── faiss_index/
│
├── evaluation_results.json
│
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Build Vector Database

```bash
python ingestion.py
```

### Run Evaluation

```bash
python evaluation.py
```

### Run API

```bash
uvicorn main:app --reload
```

### Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

## 🔐 Environment Variables

```env
OPENAI_API_KEY=your_api_key
```

---

## 📚 Key Features

- Document Ingestion
- Chunking & Embeddings
- FAISS Vector Database
- Semantic Search
- GPT-4o-mini Answer Generation
- Evaluation Framework
- FastAPI Deployment

---

## 🎓 Project Outcome

This project demonstrates:

- Retrieval-Augmented Generation (RAG)
- Knowledge Retrieval
- Grounded Response Generation
- Evaluation of RAG Systems
- API Deployment using FastAPI
