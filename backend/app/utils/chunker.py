from app.core.config import settings


def chunk_text(text: str) -> list[str]:

    size = settings.CHUNK_SIZE
    overlap = settings.CHUNK_OVERLAP

    chunks = []

    start = 0

    while start < len(text):

        end = start + size

        chunks.append(text[start:end])

        start += size - overlap

    return [c.strip() for c in chunks if c.strip()]