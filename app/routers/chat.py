from fastapi import APIRouter
from app.initialization import initiate, response
from models.models import ChatRequest, ChatResponse

router = APIRouter()
conversational_rag_chain = initiate()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    ssid = 1
    answer = response(conversational_rag_chain, request.user_query, ssid)
    return ChatResponse(answer=answer)


