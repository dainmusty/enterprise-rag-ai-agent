from functools import lru_cache

from app.services.chat_service import ChatService
from app.services.rag_service import RAGService
from app.services.retrieval_service import RetrievalService
from app.services.llm_service import LLMService


@lru_cache
def get_llm_service() -> LLMService:
    return LLMService()


@lru_cache
def get_retrieval_service() -> RetrievalService:
    return RetrievalService()


@lru_cache
def get_rag_service() -> RAGService:
    return RAGService()


@lru_cache
def get_chat_service() -> ChatService:
    return ChatService()