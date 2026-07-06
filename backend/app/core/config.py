import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    # Application

    APP_NAME = os.getenv(
        "APP_NAME",
        "Enterprise AI Agent"
    )

    APP_VERSION = os.getenv(
        "APP_VERSION",
        "1.0.0"
    )

    # Ollama

    OLLAMA_BASE_URL = os.getenv(
        "OLLAMA_BASE_URL"
    )

    LLM_MODEL = os.getenv(
        "LLM_MODEL"
    )

    LLM_TEMPERATURE = float(
        os.getenv(
            "LLM_TEMPERATURE",
            0.2
        )
    )

    # Embeddings

    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL"
    )

    # Chroma

    CHROMA_COLLECTION = os.getenv(
        "CHROMA_COLLECTION"
    )

    # Retrieval

    TOP_K_RESULTS = int(
        os.getenv(
            "TOP_K_RESULTS",
            3
        )
    )

    # Chunking

    CHUNK_SIZE = int(
        os.getenv(
            "CHUNK_SIZE",
            500
        )
    )

    CHUNK_OVERLAP = int(
        os.getenv(
            "CHUNK_OVERLAP",
            50
        )
    )


settings = Settings()