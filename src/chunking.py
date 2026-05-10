from typing import List


def chunk_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 100
) -> List[str]:

    words = text.split()

    chunks = []

    current_chunk = []

    current_length = 0

    for word in words:

        current_chunk.append(word)

        current_length += len(word) + 1

        if current_length >= chunk_size:

            chunk = " ".join(current_chunk)

            chunks.append(chunk)

            overlap_words = current_chunk[-20:]

            current_chunk = overlap_words

            current_length = sum(
                len(w) + 1 for w in current_chunk
            )

    if current_chunk:

        chunks.append(
            " ".join(current_chunk)
        )

    return chunks