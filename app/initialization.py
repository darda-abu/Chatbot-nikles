from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import os
from dotenv import load_dotenv
from langchain import hub
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.messages import HumanMessage, AIMessage
from langchain.chains.history_aware_retriever import create_history_aware_retriever
import pickle
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from utils.prompts import  contextualize_q_prompt, qa_prompt
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


def initiate():
    with open('Data/db.pkl','rb') as f: pkl = pickle.load(f)
    
    vectorstore = FAISS.deserialize_from_bytes(serialized=pkl, embeddings=OpenAIEmbeddings())
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})
    llm=ChatOpenAI(model="gpt-3.5-turbo")

    history_aware_retriever = create_history_aware_retriever(
        llm, retriever, contextualize_q_prompt
    )
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
    store = {}


    def get_session_history(session_id: str) -> BaseChatMessageHistory:
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        return store[session_id]


    conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer",
    )
    
    return conversational_rag_chain


def response(conversational_rag_chain,user_query,ssid):
    return conversational_rag_chain.invoke(
            {"input": user_query},
            config={
                "configurable": {"session_id":f"{ssid}"}
            },
        )['answer']

if __name__ == "__main__":
    print("Welcome to the chatbot. Type 'exit' to quit.")
    print("Type 'clear' to clear the conversation history.")
    chain = initiate()
    ssid = 1
    while True:
        user_query = input("Enter your query: ")
        if user_query == 'exit': break
        if user_query == 'clear':
            print("Conversation history cleared. Type 'exit' to quit.")
            ssid += 1
        print(response(chain,user_query,ssid))
