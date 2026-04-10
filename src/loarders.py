from pathlib import Path
import re
import fitz  # PyMuPDF


def load_txt(file_path: str) -> str:
    path = Path(file_path)
    with path.open("r", encoding="utf-8") as f:
        return f.read()


def load_pdf(file_path: str) -> str:
    text_parts = []
    doc = fitz.open(file_path)

    for page in doc:
        page_text = page.get_text("text")
        if page_text:
            text_parts.append(page_text)

    doc.close()
    return "\n".join(text_parts)


def clean_text(text: str) -> str:
    if not text:
        return ""

    # remove caracteres nulos e alguns inválidos comuns
    text = text.replace("\x00", " ")
    text = text.replace("\ufeff", " ")

    # normaliza espaços e quebras de linha
    text = re.sub(r"\r\n?", "\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{2,}", "\n\n", text)

    # remove espaços nas bordas
    text = text.strip()

    return text


def load_document(file_path: str) -> str:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    suffix = path.suffix.lower()

    if suffix == ".txt":
        raw_text = load_txt(file_path)
    elif suffix == ".pdf":
        raw_text = load_pdf(file_path)
    else:
        raise ValueError("Formato não suportado. Use apenas PDF ou TXT.")

    return clean_text(raw_text)