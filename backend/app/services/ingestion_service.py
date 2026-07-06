from pathlib import Path

from app.clients.embedding_client import EmbeddingClient
from app.clients.chroma_client import ChromaClient
from app.core.config import settings

from app.loaders.loader_factory import load_file
from app.utils.chunker import chunk_text
from app.utils.hash import generate_hash


class IngestionService:

    def __init__(self):

        self.model = EmbeddingClient.get_model()

        self.client = ChromaClient.get_client()

        self.collection = self.client.get_or_create_collection(
            name=settings.CHROMA_COLLECTION
        )

        self.data_path = Path(__file__).resolve().parents[3] / "data"

    def ingest_file(self, file_path: Path):

        print(f"\nIndexing {file_path.name}")

        text = load_file(file_path)

        if not text or len(text.strip()) < 10:

            print("Skipped (empty file)")

            return 0

        chunks = chunk_text(text)

        embeddings = self.model.encode(chunks).tolist()

        indexed = 0

        for i, chunk in enumerate(chunks):

            doc_id = generate_hash(
                f"{file_path.name}-{i}-{chunk[:50]}"
            )

            self.collection.upsert(

                ids=[doc_id],

                documents=[chunk],

                embeddings=[embeddings[i]],

                metadatas=[{

                    "source": file_path.name,

                    "filename": file_path.name,

                    "extension": file_path.suffix,

                    "chunk": i

                }]
            )

            indexed += 1

        print(f"Indexed {indexed} chunks")

        try:
            file_path.unlink()
            print(f"Removed temporary file: {file_path.name}")
        except Exception as e:
            print(f"Could not remove temporary file: {e}")

        return indexed

    def ingest_all(self):

        total = 0

        for file_path in self.data_path.rglob("*"):

            if file_path.suffix.lower() in {

                ".txt",

                ".md",

                ".pdf"

            }:

                total += self.ingest_file(file_path)

        print(f"\nTotal indexed chunks: {total}")