from fastapi import APIRouter
from app.initialization import initiate
from models.models import ChatRequest, ChatResponse

router = APIRouter()
conversational_rag_chain = initiate()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # answer = conversational_rag_chain.invoke(
    #     {"input": request.user_query},
    #     config={"configurable": {"session_id": request.session_id}},
    # )['answer']
    return ChatResponse(answer=f"yes {request.user_query}")


