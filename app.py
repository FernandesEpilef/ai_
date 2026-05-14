from pathlib import Path

from src.loaders import load_document
from src.chunking import chunk_text

from src.vector_store import add_chunks
from src.rag_pipeline import answer_question


def main():

    data_path = Path("./data")

    all_chunks = []

    print("Carregando documentos...")

    for file_path in data_path.iterdir():

        if file_path.suffix.lower() in [".pdf", ".txt"]:

            print(f"\nProcessando: {file_path.name}")

            text = load_document(str(file_path))

            chunks = chunk_text(
                text,
                chunk_size=400,
                overlap=80
            )

            all_chunks.extend(chunks)

            print(f"{len(chunks)} chunks gerados")

    print("\nIndexando chunks...")

    add_chunks(all_chunks)

    print(f"\nTotal de chunks indexados: {len(all_chunks)}")

    while True:

        question = input("\nDigite sua pergunta: ")

        if question.lower() == "sair":
            break

        answer, retrieved_chunks = answer_question(
            question,
            top_k=4
        )

        print("\nRESPOSTA:")
        print(answer)

        # DEBUG OPCIONAL
        print("\nCHUNKS RECUPERADOS:")
        #
        for i, chunk in enumerate(retrieved_chunks, start=1):
             print(f"\n[CHUNK {i}]")
             print(chunk[:800])


if __name__ == "__main__":
    main()