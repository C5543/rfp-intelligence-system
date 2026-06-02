# RFP Intelligence System (RAG) 📄🤖

<p align="center">
  <img src="images/rag_architecture.png" width="800">
</p>

## Table of Contents

- Project Overview
- Objectives
- Architecture
- Data Processing Pipeline
- Retrieval Layer
- Generation Layer
- Evaluation
- Deployment
- Tech Stack
- Repository Structure
- How to Run

```mermaid
flowchart TD

A[Documents] --> B[Chunking]
B --> C[Embeddings]
C --> D[FAISS]
D --> E[Similarity Search]
E --> F[GPT-4o-mini]
F --> G[Answer]
```


| Component | Technology |
|------------|------------|
| Backend | FastAPI |
| LLM | GPT-4o-mini |
| Embeddings | BAAI/bge-small-en-v1.5 |
| Vector DB | FAISS |
| Framework | LangChain |

<p align="center">

Documents
<br>↓<br>
Chunking
<br>↓<br>
Embeddings
<br>↓<br>
FAISS
<br>↓<br>
Similarity Search
<br>↓<br>
GPT-4o-mini
<br>↓<br>
Response

</p>
