from app.clients.embedding_client import EmbeddingClient
from app.clients.chroma_client import ChromaClient


class AppState:

    embedding_model = None

    chroma_client = None


def startup():

    print("\nStarting Enterprise AI Agent...")

    if AppState.embedding_model is None:

        print("Loading embedding model...")

        AppState.embedding_model = EmbeddingClient.get_model()

    if AppState.chroma_client is None:

        print("Connecting to ChromaDB...")

        AppState.chroma_client = ChromaClient.get_client()

    print("Startup complete.\n")