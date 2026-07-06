from pathlib import Path
from pypdf import PdfReader


def load_pdf(file_path: Path) -> str:

    try:

        reader = PdfReader(str(file_path))

        text = ""

        for page in reader.pages:

            text += page.extract_text() or ""

        return text

    except Exception as e:

        print(f"[PDF SKIP] {file_path} -> {e}")

        return ""