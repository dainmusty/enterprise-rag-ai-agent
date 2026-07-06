from fastapi import APIRouter, Depends

from app.models.chat_models import ChatRequest, ChatResponse
from app.services.chat_service import ChatService
from app.core.dependencies import get_chat_service

router = APIRouter(
    prefix="/api/v2/chat",
    tags=["Chat"]
)


@router.post("/", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    chat_service: ChatService = Depends(get_chat_service)
):

    answer = chat_service.chat(
        session_id=request.session_id,
        message=request.message
    )

    return ChatResponse(
        response=answer
    )