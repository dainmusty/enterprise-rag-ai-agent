from sentence_transformers import SentenceTransformer

from app.core.config import settings


class EmbeddingClient:

    _model = None

    @classmethod
    def get_model(cls):

        if cls._model is None:

            print("Loading embedding model...")

            cls._model = SentenceTransformer(
                settings.EMBEDDING_MODEL
            )

        return cls._model