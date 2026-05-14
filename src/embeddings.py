from sentence_transformers import SentenceTransformer
import torch

# Detecta se GPU está disponível e usa automaticamente
device = "cuda" if torch.cuda.is_available() else "cpu"

model = SentenceTransformer(
    "all-MiniLM-L6-v2",
    device=device
)


def generate_embedding(text: str):

    embedding = model.encode(text, convert_to_tensor=False)

    return embedding.tolist()