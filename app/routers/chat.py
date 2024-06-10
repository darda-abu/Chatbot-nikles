from fastapi import APIRouter
from models.models import ChatRequest, ChatResponse
from models.Chains.router import response

router = APIRouter()
from utils.helper import flush_chat_history

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    ssid = 1
    answer = response(request.user_query)
    print(answer)
    return ChatResponse(answer=answer)

@router.post("/clear")
async def clear_chat_history():
    flush_chat_history()
    return {"message": "Chat history cleared."}