class PromptService:

    def build_prompt(
        self,
        question: str,
        context: str
    ) -> str:

        return f"""
You are an enterprise AI assistant.

RULES:
- Answer ONLY using the provided context
- If context is insufficient, say: "I don't have enough information in the knowledge base"
- Always cite source files when possible

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""