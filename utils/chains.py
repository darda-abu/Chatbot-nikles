from langchain_community.utilities import SQLDatabase
from utils.prompts import *
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os
from dotenv import load_dotenv
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains import create_retrieval_chain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.chains import RetrievalQA

load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

conversational_memory = ConversationBufferWindowMemory(
        memory_key='chat_history',
        k=5,
        return_messages=True
    )

def run_sql_chain(input):
    mysql_uri = 'mysql+mysqlconnector://root:@127.0.0.1:3306/products'
    db = SQLDatabase.from_uri(mysql_uri)

    def get_schema(_):
        schema = db.get_table_info()
        return schema
    
    llm = ChatOpenAI(model="gpt-3.5-turbo")

    query_chain = (
        RunnablePassthrough.assign(schema=get_schema)
        | query_prompt
        | llm.bind(stop=["\nSQLResult:"])
        | StrOutputParser()
    )
    def run_query(query):
        return db.run(query)
    
    sql_mega_chain = (
        RunnablePassthrough.assign(query=query_chain).assign(
            schema=get_schema,
            response=lambda vars: run_query(vars["query"]),
        )
        | query_to_NL_prompt
        | llm
    )
    return sql_mega_chain.invoke(
        {"question": input},
        config = {
            # "memory": conversational_memory,
            "output_parser" : StrOutputParser(),
        }
    ).content


def run_scrapper_chain(input):
    vectorstore = FAISS.load_local("Data/embedded_knowledge_base",embeddings=OpenAIEmbeddings(), allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})
    llm=ChatOpenAI(model="gpt-3.5-turbo")

    # history_aware_retriever = create_history_aware_retriever(
    #     llm, retriever, contextualize_q_prompt
    # )
    # question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

    # rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
    
    scrapper_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever
    )
    # conversational_rag_chain = RunnablePassthrough(
    #     rag_chain,
    #     # get_session_history,
    #     conversational_memory
    #     input_messages_key="input",
    #     history_messages_key="chat_history",
    #     output_messages_key="answer",
    # )
    return scrapper_chain.invoke(
        {"query": input},
        config={
            # "memory": conversational_memory,
            "output_parser": StrOutputParser(),
        }
    )['result']

if __name__ == "__main__":
    for i in range(5):
        input_text = input("wot?")
        which = input("wich?")
        if which == "sql":
            print(run_sql_chain(input_text))
        else:
            print(run_scrapper_chain(input_text))


