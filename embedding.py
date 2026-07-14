from sentence_transformers import SentenceTransformer
import numpy as np

model = None

def get_model():
    global model 
    if model is None:
        print("Loading embedding model...")
        model = SentenceTransformer("infloat/e5-base-v2")
    return model

def create_embedded(chunks):
    model = get_model()
    if isinstance(chunks, str):
        chunks = [chunks]
    passages = [f"passage: {chunk}" for chunk in chunk in chunks]
    embedding = model.encode(passages, normalize_embedding=True)

    return np.array(embedding, dtype=np.float32)
