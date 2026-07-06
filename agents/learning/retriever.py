import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from pathlib import Path

# -----------------------------
# Load embedding model
# -----------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"

# -----------------------------
# Load FAISS index
# -----------------------------
index = faiss.read_index(str(DATA_DIR / "faiss.index"))

# -----------------------------
# Load original documents
# -----------------------------
with open(DATA_DIR / "documents.pkl", "rb") as f:
    documents = pickle.load(f)


def retrieve_resources(query, top_k=3):
    """
    Retrieve the most relevant learning resources.

    Parameters
    ----------
    query : str
        Example:
        "Docker AWS Leadership"

    top_k : int
        Number of documents to retrieve

    Returns
    -------
    list
        Top matching documents
    """

    query_embedding = model.encode(query)

    query_embedding = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:
        if idx != -1:
            results.append(documents[idx])

    return results