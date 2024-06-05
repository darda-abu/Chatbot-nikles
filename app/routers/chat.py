from fastapi import APIRouter
from app.initialization import initiate, response
from models.models import ChatRequest, ChatResponse
from utils.agents import conv_agent
router = APIRouter()
# conversational_rag_chain = initiate()
agent = conv_agent
@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # ssid = 1
# 
    answer = agent.invoke(request.user_query)
    print(answer)
    # answer = response(conversational_rag_chain, request.user_query, ssid)
    return ChatResponse(answer=answer['output'])

