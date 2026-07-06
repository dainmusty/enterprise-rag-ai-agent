from app.clients.chroma_client import ChromaClient

from app.core.config import settings


class ChromaRepository:

    def __init__(self):

        client = ChromaClient.get_client()

        self.collection = client.get_collection(
            settings.CHROMA_COLLECTION
        )

    def search(
        self,
        embedding,
        top_k
    ):

        return self.collection.query(

            query_embeddings=[embedding],

            n_results=top_k

        )

    def insert(

        self,

        doc_id,

        text,

        embedding,

        metadata

    ):

        self.collection.add(

            ids=[doc_id],

            documents=[text],

            embeddings=[embedding],

            metadatas=[metadata]

        )