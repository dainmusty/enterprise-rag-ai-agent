from app.clients.ollama_client import get_ollama


class LLMService:

    def __init__(self):

        self.client = get_ollama()

    def generate(
        self,
        prompt: str
    ) -> str:

        return self.client.generate(prompt)