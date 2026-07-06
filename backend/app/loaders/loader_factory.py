from pathlib import Path

from app.loaders.text_loader import load_text
from app.loaders.markdown_loader import load_markdown
from app.loaders.pdf_loader import load_pdf


def load_file(file_path: Path) -> str:

    try:

        if file_path.suffix == ".txt":
            return load_text(file_path)

        if file_path.suffix == ".md":
            return load_markdown(file_path)

        if file_path.suffix == ".pdf":
            return load_pdf(file_path)

        return ""

    except Exception as e:

        print(f"[LOAD SKIP] {file_path} -> {e}")

        return ""