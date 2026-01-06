import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"

st.title("📄 Document Q&A Assistant")

uploaded_file = st.file_uploader(
    "Upload a document",
    type=["pdf", "docx", "txt", "md"]
)

if uploaded_file:
    res = requests.post(
        f"{BACKEND_URL}/upload",
        files={"file": uploaded_file}
    )
    st.success("Document uploaded and indexed")

question = st.chat_input("Ask a question based on the document")


if question:
    res = requests.post(
        f"{BACKEND_URL}/chat",
        json={"query": question}
    ).json()

    # Use get() to avoid KeyError
    st.markdown(res.get("answer", "No answer returned."))
    st.subheader("Sources")
    for c in res.get("citations", []):
        st.write(f"- {c}")


if st.button("Reset Knowledge Base"):
    requests.post(f"{BACKEND_URL}/reset")
    st.success("Knowledge base cleared")
