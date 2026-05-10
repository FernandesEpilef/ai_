from src.vector_store import search_chunks
from src.llm_api import ask_llm


def answer_question(question, top_k=2):

    retrieved_chunks = search_chunks(
        question,
        top_k
    )

    context = "\n\n".join(retrieved_chunks)

    response = ask_llm(
        context,
        question
    )

    return response, retrieved_chunks