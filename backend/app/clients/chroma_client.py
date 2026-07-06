from pathlib import Path

import chromadb


class ChromaClient:

    _client = None

    @classmethod
    def get_client(cls):

        if cls._client is None:

            print("Connecting to ChromaDB...")

            project_root = Path(__file__).resolve().parents[2]

            chroma_path = project_root / "chroma_db"

            cls._client = chromadb.PersistentClient(
                path=str(chroma_path)
            )

        return cls._client