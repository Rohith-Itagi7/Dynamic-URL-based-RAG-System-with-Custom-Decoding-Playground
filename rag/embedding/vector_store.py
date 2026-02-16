# rag/embedding/vector_store.py

import torch

class VectorStore:

    def __init__(self):
        self.embeddings = None
        self.texts = []

    def add(self, embeddings, texts):
        self.embeddings = embeddings
        self.texts = texts

    def search(self, query_embedding, top_k=3):

        if self.embeddings is None or len(self.texts) == 0:
            return []

        scores = torch.matmul(query_embedding, self.embeddings.T)

        # 🔥 FIX: Clamp top_k
        actual_k = min(top_k, len(self.texts))

        top_indices = torch.topk(scores, k=actual_k).indices[0]

        return [self.texts[i] for i in top_indices]
