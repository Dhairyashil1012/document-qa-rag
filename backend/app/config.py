import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ✅ OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ✅ Upload and FAISS directories
UPLOAD_DIR = "backend/data/uploads"
FAISS_DIR = "backend/data/faiss_index"

# ✅ Chunking parameters
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150

# ✅ Top-K retrieval
TOP_K = 5

# Optional: Mongo URI if needed later
MONGO_URI = os.getenv("MONGO_URI")
