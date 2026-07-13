from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embedded(chunks):
    if isinstance(chunks, str):
        chunks = [chunks]
    passages = [f"passage: {chunk} " for chunk in chunks]
    embedding = model.encode(passages, normalize_embeddings=True)

    return np.array(embedding, dtype=np.float32) 