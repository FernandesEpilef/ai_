from pathlib import Path

from src.loaders import load_document
from src.chunking import chunk_text

from src.vector_store import add_chunks, load_persisted_store
from src.rag_pipeline import answer_question

# Parâmetros de experimento: altere aqui para testar diferentes configurações.
# Não é necessário editar src/chunking.py quando mudar CHUNK_SIZE ou OVERLAP aqui.
CHUNK_SIZE = 300
OVERLAP = 80
TOP_K = 4


def main():

    data_path = Path("./data")

    print("Carregando documentos...")

    index_loaded = load_persisted_store()

    if index_loaded:
        print("Índice vetorial existente carregado.")
    else:
        all_chunks = []

        for file_path in data_path.iterdir():

            if file_path.suffix.lower() in [".pdf", ".txt"]:

                print(f"\nProcessando: {file_path.name}")

                text = load_document(str(file_path))

                chunks = chunk_text(
                    text,
                    chunk_size=CHUNK_SIZE,
                    overlap=OVERLAP
                )

                all_chunks.extend(chunks)

                print(f"{len(chunks)} chunks gerados")

        print("\nIndexando chunks...")

        add_chunks(all_chunks)

        print(f"Total de chunks indexados: {len(all_chunks)}")

    history = []

    print("\nDigite 'limpar histórico' para iniciar novo chat.")
    print("Digite 'sair' para encerrar.\n")

    while True:

        question = input("Digite sua pergunta: ").strip()

        if question.lower() in ["sair", "exit"]:
            break

        if question.lower() in ["limpar histórico", "novo chat", "reset"]:
            history.clear()
            print("Histórico limpo. O próximo diálogo será tratado como novo chat.\n")
            continue

        if not question:
            print("Pergunta vazia. Digite uma pergunta ou 'sair'.\n")
            continue

        answer, retrieved_chunks = answer_question(
            question,
            top_k=TOP_K,
            history=history,
        )

        print("\nRESPOSTA:")
        print(answer)

        print("\nCHUNKS RECUPERADOS:")
        for i, chunk in enumerate(retrieved_chunks, start=1):
            print(f"\n[CHUNK {i}]")
            print(chunk[:800])

        history.append({"question": question, "answer": answer})


if __name__ == "__main__":
    main()