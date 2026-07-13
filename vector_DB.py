import faiss
import numpy as np

class VectorData:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)
        self.document = []

    def add_vector(self, vectors, chunks):
        if vectors is None or len(vectors) == 0:
            print("No vectors data can be found")
            return None

        if chunks is None or len(chunks) == 0:
            print("No chunks data can be found")
            return None

        vectors = np.array(vectors, dtype = np.float32)

        self.index.add(vectors)
        self.document.extend(chunks)

        print("Vectors and chunks store successfully")


    def search_vector(self, query_vector, k=2):
        if query_vector is None:
            print("No query vector can be found")
            return []

        query_vector = np.array(query_vector, dtype = np.float32)
        query_vector = query_vector.reshape(1,-1)
        D,I = self.index.search(query_vector, k)
        res = []
        for idx in I[0]:
            if idx != -1:
                res.append(self.document[idx])

        return res

from chunk import chunk_model
from embedding import create_embedded

def build_vector_store(transcript):
    if transcript is None:
        return None

    chunks = chunk_model(transcript)
    embedding = create_embedded(chunks)

    dimension = embedding.shape[1]

    vector_db = VectorData(dimension)

    vector_db.add_vector(embedding, chunks)

    return vector_db