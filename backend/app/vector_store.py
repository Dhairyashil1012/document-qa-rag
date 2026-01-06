import os
from langchain_text_splitters.character import RecursiveCharacterTextSplitter

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from app.config import CHUNK_SIZE, CHUNK_OVERLAP, FAISS_DIR

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

def create_or_update_faiss(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    chunks = splitter.split_documents(docs)

    if os.path.exists(FAISS_DIR):
        db = FAISS.load_local(FAISS_DIR, embeddings, allow_dangerous_deserialization=True)
        db.add_documents(chunks)
    else:
        db = FAISS.from_documents(chunks, embeddings)
    
    db.save_local(FAISS_DIR)
