from pathlib import Path

from app.clients.embedding_client import EmbeddingClient
from app.clients.chroma_client import ChromaClient
from app.core.config import settings
from app.services.llm_service import LLMService


class RAGService:

    def __init__(self):

        self.embedding_model = EmbeddingClient.get_model()

        self.client = ChromaClient.get_client()

        self.collection = self.client.get_or_create_collection(
            name=settings.CHROMA_COLLECTION
        )

        self.llm = LLMService()

    def ask(self, question: str) -> str:

        embedding = self.embedding_model.encode(question).tolist()

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=settings.TOP_K_RESULTS
        )

        documents = results["documents"][0]
        metadata = results["metadatas"][0]

        context = ""

        sources = []

        for doc, meta in zip(documents, metadata):

            filename = Path(meta["source"]).name

            context += (
                f"\nSOURCE: {filename}\n"
                f"{doc}\n"
            )

            if filename not in sources:
                sources.append(filename)

        prompt = f"""
You are an Enterprise AI Assistant.

Use ONLY the supplied context to answer the user's question.

If the context does not contain enough information, reply exactly:

"I couldn't find that information in the uploaded documents."

Do not use outside knowledge.

Do not make assumptions.

Always answer professionally.

Context:
{context}

Question:
{question}
"""

        answer = self.llm.generate(prompt)

        if sources:
            answer += "\n\nReferenced Documents:\n"

            for source in sources:
                answer += f"• {source}\n"

        return answer