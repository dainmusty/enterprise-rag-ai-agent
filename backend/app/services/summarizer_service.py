from app.services.llm_service import LLMService


class SummarizerService:

    def __init__(self):

        self.llm = LLMService()

    def summarize(self, messages):

        if not messages:
            return ""

        text = "\n".join(
            [f"{m.role}: {m.content}" for m in messages]
        )

        prompt = f"""
Summarize the following conversation into a compact memory.

Keep:
- user facts
- preferences
- key context

Conversation:
{text}

Summary:
"""

        return self.llm.generate(prompt)