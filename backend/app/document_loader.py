from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader
)


from pathlib import Path

def load_document(file_path: str):
    suffix = Path(file_path).suffix.lower()

    if suffix == ".pdf":
        return PyPDFLoader(file_path).load()
    elif suffix == ".docx":
        return Docx2txtLoader(file_path).load()
    elif suffix in [".txt", ".md"]:
        return TextLoader(file_path).load()
    else:
        raise ValueError("Unsupported file format")
