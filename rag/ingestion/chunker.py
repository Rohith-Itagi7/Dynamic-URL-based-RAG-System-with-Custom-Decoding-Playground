# rag/ingestion/chunker.py

class Chunker:

    @staticmethod
    def chunk(text: str, chunk_size=400, overlap=50, max_chunks=30):
        chunks = []
        start = 0

        while start < len(text) and len(chunks) < max_chunks:
            end = start + chunk_size
            chunks.append(text[start:end])
            start += chunk_size - overlap

        return chunks
