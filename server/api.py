# server/api.py
from fastapi import FastAPI
from server.schemas import GenerateRequest
from rag.rag_pipeline import RAGPipeline
from generation.generation_engine import GenerationEngine

app = FastAPI()

rag = RAGPipeline()
generator = GenerationEngine()

@app.post("/generate")
def generate(request: GenerateRequest):

    context = rag.run(request.url, request.query, top_k=request.top_k)

    params = request.dict()

    answer = generator.generate(context, request.query, params)

    return {"answer": answer}
