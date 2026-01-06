from fastapi import FastAPI, UploadFile, File
from app.schemas import ChatRequest, ChatResponse, UploadResponse, ResetResponse
from app.document_loader import load_document
from app.vector_store import create_or_update_faiss
from app.rag_pipeline import answer_question
from app.config import UPLOAD_DIR
import os
import shutil

app = FastAPI(title="Document Q&A Assistant")

# Ensure upload directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a document and index it into FAISS.
    Supports PDF, DOCX, TXT, MD.
    """
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as f:
            f.write(await file.read())

        # Load and index document
        docs = load_document(file_path)
        create_or_update_faiss(docs)

        return {"status": "success", "message": f"Document '{file.filename}' uploaded and indexed."}

    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Ask a question and get a grounded answer with citations.
    """
    res = answer_question(request.query)
    return res

@app.post("/reset", response_model=ResetResponse)
async def reset_knowledge_base():
    """
    Reset the FAISS knowledge base (delete all indexed documents).
    """
    try:
        shutil.rmtree("backend/data/faiss_index", ignore_errors=True)
        return {"status": "success"}
    except Exception as e:
        return {"status": f"error: {str(e)}"}
