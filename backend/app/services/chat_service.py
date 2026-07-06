from app.services.rag_service import RAGService
from app.services.memory_service import MemoryService
from app.services.summarizer_service import SummarizerService


class ChatService:

    def __init__(self):

        self.rag = RAGService()
        self.memory = MemoryService()
        self.summarizer = SummarizerService()

    def chat(self, session_id: str, message: str) -> str:

        self.memory.save(session_id, "user", message)

        history = self.memory.history(session_id)

        # Build short-term context
        recent_context = "\n".join(
            [f"{m.role}: {m.content}" for m in history]
        )

        # Create compact prompt
        prompt = f"""
You are an enterprise AI assistant.

Conversation context:
{recent_context}

User question:
{message}
"""

        response = self.rag.ask(prompt)

        self.memory.save(session_id, "assistant", response)

        # Optional summarization trigger (lightweight rule)
        if len(history) > 8:

            summary = self.summarizer.summarize(history)

            self.memory.clear(session_id)
            self.memory.save(session_id, "system", summary)

        return response