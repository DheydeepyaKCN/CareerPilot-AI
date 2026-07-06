import json
import pickle
import faiss
import numpy as np
from pathlib import Path
import json

from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load knowledge base
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"

with open(DATA_DIR / "learning_resources.json", "r", encoding="utf-8") as f:
    data = json.load(f)

documents = []
embeddings = []

for item in data:

    text = f"""
Skill: {item['skill']}

Category: {item['category']}

Difficulty: {item['difficulty']}

Duration: {item['duration']}

Resources:
"""

    for resource in item["resources"]:
        text += f"""
{resource['title']}
{resource['provider']}
{resource['url']}
"""

    documents.append(item)

    embedding = model.encode(text)

    embeddings.append(embedding)

embeddings = np.array(embeddings).astype("float32")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

faiss.write_index(index, str(DATA_DIR / "faiss.index"))

with open(DATA_DIR / "documents.pkl", "wb") as f:
    pickle.dump(documents, f)

print("Vector Database Created Successfully!")