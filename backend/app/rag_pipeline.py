import os
from app.config import FAISS_DIR, TOP_K, OPENAI_API_KEY
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

# Initialize embeddings and LLM once
embeddings = OpenAIEmbeddings(model="text-embedding-3-large", openai_api_key=OPENAI_API_KEY)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, openai_api_key=OPENAI_API_KEY)

# System prompt for strict grounded answers
SYSTEM_PROMPT = """
You are a document-based question answering assistant.
Rules:
- Answer ONLY using the provided context.
- If the answer is not found, say:
  "I couldn’t find this information in the uploaded document."
- Always cite the source (document name and page).

Context:
{context}

Question:
{question}
"""

def answer_question(question: str):
    """
    Retrieve top-k chunks from FAISS and generate a strict answer from LLM.
    Returns a dict with 'answer' and 'citations'.
    """

    # Check if FAISS index exists
    if not os.path.exists(FAISS_DIR):
        return {"answer": "No documents indexed.", "citations": []}

    # Load FAISS vector store
    db = FAISS.load_local(FAISS_DIR, embeddings, allow_dangerous_deserialization=True)

    # Top-k similarity search
    docs = db.similarity_search(question, k=TOP_K)

    if not docs:
        return {"answer": "I couldn’t find this information in the uploaded document.", "citations": []}

    # Build context and citation list
    context_text = ""
    citations = []
    for d in docs:
        page_content = d.page_content
        metadata = d.metadata
        source = metadata.get("source", "Unknown Document")
        page = metadata.get("page", "N/A")
        context_text += f"{page_content}\n\n"
        citations.append(f"{source}, page {page}")

    # Format prompt
    prompt = SYSTEM_PROMPT.format(context=context_text, question=question)

    # Generate answer
    try:
        response = llm.invoke(prompt).content
    except Exception as e:
        response = f"Error generating answer: {str(e)}"

    # Return properly formatted dict
    return {"answer": response, "citations": list(set(citations))}
