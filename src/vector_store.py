import faiss
import numpy as np

from src.embeddings import generate_embedding

documents = []

dimension = 384

index = faiss.IndexFlatL2(dimension)


def add_chunks(chunks):

    global documents

    vectors = []

    for chunk in chunks:

        embedding = generate_embedding(chunk)

        vectors.append(embedding)

        documents.append(chunk)

    vectors = np.array(vectors).astype("float32")

    index.add(vectors)


def search_chunks(query, top_k=3):

    query_embedding = generate_embedding(query)

    query_vector = np.array(
        [query_embedding]
    ).astype("float32")

    distances, indices = index.search(
        query_vector,
        top_k
    )

    results = []

    for idx in indices[0]:

        results.append(documents[idx])

    return results