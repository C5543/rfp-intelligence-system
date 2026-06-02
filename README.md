

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

<br><br><br>

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

<br><br><br>

---

## 🔍 Retrieval Layer

- Top-K Similarity Search (k=4)
- Semantic Retrieval
- Context Extraction

<br><br><br>

---

## 🤖 Generation Layer

### LLM
- GPT-4o-mini

### Prompt Rules
- Use ONLY retrieved context  
- No hallucinations  
- Structured answers  
- Say "I don't know" if missing info  
<br><br><br>

---

## 📊 Evaluation

- Retrieval Success  
- Answer Relevance  
- Grounded Responses  

---

## 🚀 Deployment

- FastAPI endpoint: `/ask`

---

## 🔐 Environment Variables

```env
OPENAI_API_KEY=your_api_key
```
