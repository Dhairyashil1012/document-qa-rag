# 📄 Document Q&A Assistant (RAG)

## Overview

This project is a **web-based AI assistant** that allows users to upload documents (PDF, DOCX, TXT, Markdown) and ask questions that are answered **strictly based on the document content**. It uses **Retrieval-Augmented Generation (RAG)** to combine **vector-based retrieval** and **LLM-powered question answering**, ensuring answers are grounded in the uploaded documents with clear citations.

This project was implemented as part of an **AI Intern Assignment** to demonstrate **document-based Q&A using modern AI techniques**.

---

## Features

1. **Document Upload & Indexing**
   - Supports multiple file formats: PDF, DOCX, TXT, Markdown.
   - Extracts text from uploaded documents.
   - Splits documents into **chunks (800 tokens with 150-token overlap)** for better context retrieval.
   - Generates **embeddings** for each chunk using **OpenAI embeddings**.
   - Stores embeddings in a **local FAISS vector store** (no MongoDB required).
   - Displays upload and indexing status.

2. **Question Answering**
   - Simple chat interface using **Streamlit frontend**.
   - Retrieves **top-k relevant chunks** (default k=5) from FAISS.
   - Uses **GPT-4o-mini** to answer questions **strictly based on retrieved context**.
   - Provides **citations** for each answer, showing document name and page.
   - Safe fallback: `"I couldn’t find this information in the uploaded document."` if the answer is not found.

3. **Additional Functionalities**
   - Clear chat option in frontend.
   - Reset knowledge base option to delete FAISS index and re-upload documents.
   - Designed with **production-ready folder structure** for backend and frontend separation.
   - Error handling in both backend and frontend.
   - Easily extendable to **other vector stores** (Pinecone, Weaviate, Qdrant).

---

## Project Structure

document-qa-rag/
│
├── backend/
│ │
│ ├── app/
| |
│ │ ├── main.py # FastAPI backend
│ │
│ │ ├── config.py # Configurations (.env)
│ │
│ │ ├── rag_pipeline.py # RAG pipeline (retrieval + LLM)
│ │
│ │ ├── vector_store.py # FAISS vector store handling
│ │
│ │ ├── document_loader.py # Load PDF, DOCX, TXT, MD
│ │
│ │ └── schemas.py # Pydantic request/response schemas
│ │
│ ├── data/
│ │
│ │ ├── uploads/ # Uploaded documents
│ │
│ │ └── faiss_index/ # FAISS vector database
│ │
│ └── requirements.txt # Backend dependencies
│
├── frontend/
│ │
│ └── streamlit_app.py # Streamlit frontend
│ 
│
└── README.md




---

## Technologies Used

- **Backend**
  - FastAPI: Lightweight backend API.
  - FAISS: Local vector store for embeddings.
  - LangChain: Document loaders, vector store utilities.
  - OpenAI GPT-4o-mini: Language model for generating answers.
- **Frontend**
  - Streamlit: Simple, interactive UI for file upload and chat.
- **Other**
  - PyPDF, docx2txt: Extract text from PDFs and DOCX.
  - python-dotenv: Load API keys securely from `.env`.

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <YOUR_REPO_URL>
cd document-qa-rag/backend




Why This Implementation?

Uses RAG pipeline → ensures answers are grounded in the documents, avoiding hallucinations.

FAISS local vector store → no external database required.

Multi-format support → PDF, DOCX, TXT, Markdown.

Clear architecture → backend/frontend separation, production-ready.

Error handling & fallbacks → robust for real-world use.

Citation tracing → recruiters see references for each answer.

This demonstrates practical AI engineering skills, including document parsing, embedding generation, vector search, LLM prompting, and frontend integration.
