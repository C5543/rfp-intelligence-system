

# RFP Intelligence System (RAG) 📄🤖

A Retrieval-Augmented Generation (RAG) system designed to help proposal writers and RFP managers retrieve company knowledge and generate grounded responses from internal documents.
<br><br><br>

---

## 📌 Project Overview

This project builds an RFP Intelligence System using Retrieval-Augmented Generation (RAG).

The system ingests company documents, converts them into vector embeddings, stores them in FAISS, retrieves relevant information based on user questions, and generates grounded responses using GPT-4o-mini.
<br><br><br>

---

## 🎯 Objectives

- Ingest internal company documents
- Build a searchable knowledge base
- Perform semantic retrieval
- Generate grounded answers using LLMs
- Evaluate retrieval and generation quality
- Deploy the solution through FastAPI
<br><br><br>
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

## Project Structure

rfp_intelligence_system/

├── app.py
├── main.py
├── rag_chain.py
├── bid_decision.py
├── requirements.txt
├── faiss_index/
└── documents/

---
## Tech Stack

- Python
- LangChain
- OpenAI GPT-4o-mini
- HuggingFace Embeddings
- FAISS
- FastAPI
- Streamlit

  ---

## 📂 Data Processing Pipeline

### Step 1: Document Ingestion
- PDF
- DOCX
- XLSX

### Step 2: Chunking
- RecursiveCharacterTextSplitter
- Chunk Size: 500
- Chunk Overlap: 100

### Step 3: Embeddings
- BAAI/bge-small-en-v1.5

### Step 4: Vector Storage
- FAISS



---

## 🔍 Retrieval Layer

- Top-K Similarity Search (k=4)
- Semantic Retrieval
- Context Extraction



---

## 🤖 Generation Layer

### LLM
- GPT-4o-mini

### Prompt Rules
- Use ONLY retrieved context  
- No hallucinations  
- Structured answers  
- Say "I don't know" if missing info  


---

## 📊 Evaluation

- Retrieval Success  
- Answer Relevance  
- Grounded Responses  
<br><br><br>
---
## Features

- Question & Answer over RFP documents
- Source document retrieval
- Semantic search using FAISS
- Bid / No-Bid recommendation
- FastAPI backend
- Streamlit frontend
  
  ---
  
## 🚀 Deployment

- FastAPI endpoint: `/ask`

---

## 🔐 Environment Variables

```env
OPENAI_API_KEY=your_api_key
```
