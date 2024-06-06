from fastapi import APIRouter
from app.initialization import initiate, response
from models.models import ChatRequest, ChatResponse
# from utils.agents import conv_agent
from models.Chains.router import response

router = APIRouter()
# conversational_rag_chain = initiate()
# agent = conv_agent
from utils.helper import flush_chat_history
# flush_chat_history(ssid=1)

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    ssid = 1
    answer = response(request.user_query)
    # answer = agent.invoke(request.user_query)
    print(answer)
    # answer = response(conversational_rag_chain, request.user_query, ssid)
    return ChatResponse(answer=answer)

@router.post("/clear")
async def clear_chat_history():
    # chat_history.clear()
    flush_chat_history()
    return {"message": "Chat history cleared."}