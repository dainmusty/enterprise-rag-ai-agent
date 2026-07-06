import requests

from app.core.config import settings


class OllamaClient:

    def generate(
        self,
        prompt: str
    ) -> str:

        response = requests.post(

            f"{settings.OLLAMA_BASE_URL}/api/generate",

            json={

                "model": settings.LLM_MODEL,

                "prompt": prompt,

                "stream": False,

                "options": {
                    "temperature": settings.LLM_TEMPERATURE
                }

            },

            timeout=300

        )

        response.raise_for_status()

        return response.json()["response"]


_client = OllamaClient()


def get_ollama():

    return _client