from app.clients.embedding_client import EmbeddingClient
from app.clients.chroma_client import ChromaClient
from app.core.config import settings


class RetrievalService:

    def __init__(self):

        self.model = EmbeddingClient.get_model()

        self.client = ChromaClient.get_client()

        self.collection = self.client.get_or_create_collection(
            name=settings.CHROMA_COLLECTION
        )

    def search(self, question: str):

        embedding = self.model.encode([question]).tolist()[0]

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=settings.TOP_K_RESULTS,
            include=["documents", "metadatas"]
        )

        output = []

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]

        for document, metadata in zip(documents, metadatas):

            output.append(
                {
                    "document": document,
                    "source": metadata.get("source", "Unknown"),
                    "chunk": metadata.get("chunk", 0),
                }
            )

        return output