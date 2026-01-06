from pydantic import BaseModel
from typing import List, Optional

# ✅ Request schema for chat
class ChatRequest(BaseModel):
    query: str

# ✅ Response schema for chat
class ChatResponse(BaseModel):
    answer: str
    citations: List[str]

# ✅ Response schema for upload
class UploadResponse(BaseModel):
    status: str
    message: Optional[str] = None

# ✅ Response schema for reset
class ResetResponse(BaseModel):
    status: str
