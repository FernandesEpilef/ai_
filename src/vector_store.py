import faiss
import json
import numpy as np
from pathlib import Path

from src.embeddings import generate_embedding

dimension = 384
index = faiss.IndexFlatL2(dimension)
documents = []

index_file = Path("./data/vector_index.faiss")
docs_file = Path("./data/documents.json")


def load_persisted_store():

    global documents, index

    if not index_file.exists() or not docs_file.exists():
        return False

    with docs_file.open("r", encoding="utf-8") as f:
        documents = json.load(f)

    index = faiss.read_index(str(index_file))
    return True


def save_persisted_store():

    docs_file.parent.mkdir(parents=True, exist_ok=True)

    with docs_file.open("w", encoding="utf-8") as f:
        json.dump(documents, f, ensure_ascii=False, indent=2)

    faiss.write_index(index, str(index_file))


def add_chunks(chunks):

    global documents

    new_vectors = []

    for chunk in chunks:
        if chunk in documents:
            continue

        embedding = generate_embedding(chunk)
        new_vectors.append(embedding)
        documents.append(chunk)

    if not new_vectors:
        return

    vectors = np.array(new_vectors).astype("float32")
    index.add(vectors)

    save_persisted_store()


def search_chunks(query, top_k=3):

    if len(documents) == 0 or index.ntotal == 0:
        return []

    query_embedding = generate_embedding(query)
    query_vector = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_vector, top_k)

    results = []
    for idx in indices[0]:
        if idx < len(documents):
            results.append(documents[idx])

    return results