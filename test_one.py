from src.loarders import load_document
from src.chunking import chunk_text


def main():
    file_path = r".\data\13+-+[OK2]+#878+-+discurso+odio.pdf"  #pode ser mudado

    text = load_document(file_path)
    chunks = chunk_text(text, chunk_size=800, overlap=100)

    print("=" * 60)
    print("TAMANHO DO TEXTO EXTRAÍDO:")
    print(len(text))

    print("\n" + "=" * 60)
    print("QUANTIDADE DE CHUNKS:")
    print(len(chunks))

    print("\n" + "=" * 60)
    print("PRIMEIROS 2 CHUNKS:\n")

    for i, chunk in enumerate(chunks[:2], start=1):
        print(f"[CHUNK {i}]")
        print(chunk[:1000])  # limita impressão
        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    main()