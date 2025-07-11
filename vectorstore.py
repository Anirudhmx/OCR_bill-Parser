import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Dummy taxonomy
TAXONOMY = ["Coca Cola", "French Fries", "Chicken Biryani", "Masala Dosa"]

model = SentenceTransformer('all-MiniLM-L6-v2')

# Build index from taxonomy
taxonomy_embeddings = model.encode(TAXONOMY, normalize_embeddings=True)
index = faiss.IndexFlatIP(taxonomy_embeddings.shape[1])
index.add(taxonomy_embeddings)

def normalize_item_name(item_name: str) -> str:
    item_embedding = model.encode([item_name], normalize_embeddings=True)
    D, I = index.search(item_embedding, k=1)
    return TAXONOMY[I[0][0]]
