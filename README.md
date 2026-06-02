RFP Intelligence System (RAG) 📄🤖

A Retrieval-Augmented Generation (RAG) system built with FastAPI, FAISS, Hugging Face Embeddings, and OpenAI GPT-4o-mini to assist consulting organizations in responding to Request for Proposals (RFPs).

📌 Project Overview

This project aims to build an intelligent RFP assistant capable of retrieving relevant information from company documents and generating grounded responses for proposal writing.

The system combines semantic search with Large Language Models (LLMs) to help proposal writers, consultants, and business development teams quickly find relevant content and draft accurate responses.

🎯 Objectives
Build a document ingestion pipeline
Create a searchable knowledge base
Implement semantic retrieval using vector embeddings
Generate grounded responses using RAG
Evaluate retrieval and generation quality
Deploy the solution as an API service
🏗️ Project Architecture

Internal Documents

↓

Document Parsing

↓

Chunking

↓

Embeddings (BAAI/bge-small-en-v1.5)

↓

FAISS Vector Database

↓

Similarity Search

↓

GPT-4o-mini

↓

Grounded RFP Response

🔹 Data Processing Pipeline
Step 1: Document Ingestion

Supported document formats:

PDF
DOCX
XLSX

The system extracts and normalizes text from company knowledge sources including:

Past RFP responses
Case studies
Company capability statements
Technical documentation
Training materials
Client proposals
Step 2: Chunking

Documents are split into semantic chunks using:

RecursiveCharacterTextSplitter
Chunk Size = 500
Chunk Overlap = 100
Step 3: Embeddings

Embedding Model:

BAAI/bge-small-en-v1.5
Step 4: Vector Database

Vector Store:

FAISS

Used for semantic similarity search and retrieval.

🔍 Retrieval Layer

Implemented retrieval features:

Top-K Similarity Search
Semantic Retrieval
Context Extraction

Current configuration:

k = 4

Retrieved chunks are provided to the LLM as grounding context.

🧠 Generation Layer

LLM:

GPT-4o-mini

Prompt Rules:

Use only retrieved context
Provide concise responses
Avoid hallucination
Generate structured answers
📊 Evaluation

Evaluation pipeline implemented using:

evaluation.py

Sample Evaluation Questions:

What is this RFP about?
What services are mentioned?
What is the business problem?
Who is the client?

Evaluation Output:

evaluation_results.json

Metrics currently inspected:

Retrieval Quality
Context Coverage
Answer Relevance
🚀 Deployment

The system is deployed as a FastAPI application.

API Endpoint:

POST /ask

Example Request:

{
  "query": "What is this RFP about?"
}

Example Response:

{
  "answer": "The RFP is about establishing scanning and digitization services..."
}

Interactive API Documentation:

http://127.0.0.1:8000/docs
🛠️ Tech Stack
Layer	Technology
Backend	FastAPI
LLM	GPT-4o-mini
Embeddings	BAAI/bge-small-en-v1.5
Vector Database	FAISS
Framework	LangChain
Evaluation	Custom Evaluation Pipeline
Language	Python
📦 Repository Structure
rfp_intelligence_system/
│
├── ingestion.py
├── rag_chain.py
├── evaluation.py
├── prompt.py
├── llm.py
├── main.py
│
├── faiss_index/
│
├── evaluation_results.json
│
├── requirements.txt
└── README.md
🚀 How to Run Locally
Clone Repository
git clone <repository-url>
cd rfp_intelligence_system
Install Dependencies
pip install -r requirements.txt
Set OpenAI API Key
OPENAI_API_KEY=your_api_key
Build Vector Database
python ingestion.py
Start API
uvicorn main:app --reload
Run Evaluation
python evaluation.py
🎓 Learning Outcomes

This project demonstrates:

Retrieval-Augmented Generation (RAG)
Document Processing Pipelines
Vector Databases
Semantic Search
Prompt Engineering
LLM Integration
Evaluation Frameworks
API Deployment
