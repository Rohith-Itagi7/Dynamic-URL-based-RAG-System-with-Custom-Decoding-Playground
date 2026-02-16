# server/schemas.py
from pydantic import BaseModel

class GenerateRequest(BaseModel):
    url: str
    query: str
    strategy: str
    temperature: float
    top_k: int
    top_p: float
    repetition_penalty: float
    max_tokens: int
    num_beams: int
