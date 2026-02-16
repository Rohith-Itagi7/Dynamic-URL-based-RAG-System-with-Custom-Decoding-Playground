# rag/rag_pipeline.py

from rag.ingestion.web_scraper import WebScraper
from rag.ingestion.text_cleaner import TextCleaner
from rag.ingestion.chunker import Chunker
from rag.embedding.embedder import Embedder
from rag.embedding.vector_store import VectorStore
from rag.retrieval.retriever import Retriever


class RAGPipeline:

    def __init__(self):
        self.embedder = Embedder()

    def run(self, url, query, top_k=3):

        # 1️⃣ Scrape
        raw_text = WebScraper.scrape(url)

        # 2️⃣ Clean
        clean_text = TextCleaner.clean(raw_text)

        # 3️⃣ Chunk (LIMITED)
        chunks = Chunker.chunk(clean_text)

        if not chunks:
            return "No content retrieved from the URL."

        # 4️⃣ Embed (batched)
        embeddings = self.embedder.encode(chunks)

        # 5️⃣ Store
        vector_store = VectorStore()
        vector_store.add(embeddings, chunks)

        # 6️⃣ Retrieve
        retriever = Retriever(self.embedder, vector_store)
        context_chunks = retriever.retrieve(query, top_k)

        return "\n".join(context_chunks)
