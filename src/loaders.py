from pathlib import Path
import re
import fitz


def load_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def load_pdf(file_path: str) -> str:
    text_parts = []

    doc = fitz.open(file_path)

    for page in doc:
        text = page.get_text("text")

        if text:
            text_parts.append(text)

    doc.close()

    return "\n".join(text_parts)


def clean_text(text: str) -> str:
    text = text.replace("\x00", " ")
    text = text.replace("\ufeff", " ")

    text = re.sub(r"\r\n?", "\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{2,}", "\n\n", text)

    return text.strip()


def load_document(file_path: str) -> str:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    suffix = path.suffix.lower()

    if suffix == ".pdf":
        text = load_pdf(file_path)

    elif suffix == ".txt":
        text = load_txt(file_path)

    else:
        raise ValueError("Formato não suportado")

    return clean_text(text)