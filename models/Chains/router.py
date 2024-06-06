from utils.prompts import router_prompt
from langchain_community.utilities import SQLDatabase
from utils.helper import load_chat_history, dump_chat_history, flush_chat_history
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from models.Chains.sql_chain import run_sql_chain
from models.Chains.doc_chain import run_doc_chain
from langchain_core.messages import HumanMessage, AIMessage

def response(input, uri= 'mysql+mysqlconnector://root:@127.0.0.1:3306/products'):
    mysql_uri = uri
    db = SQLDatabase.from_uri(mysql_uri)    
    def get_schema(_):
        schema = db.get_table_info()
        return schema
    llm = ChatOpenAI(temperature=0.05)
    router = (
        RunnablePassthrough.assign(schema=get_schema)
        | router_prompt
        |llm
        |StrOutputParser()
    )

    chat_history = load_chat_history()
    topic = router.invoke({"input": input,"chat_history":chat_history})

    if 'database' in topic:
        answer = run_sql_chain(input, chat_history)
    else : 
        answer = run_doc_chain(input, chat_history)
    chat_history.extend([HumanMessage(content=input), AIMessage(content=answer)])

    dump_chat_history(chat_history)
    return answer

if __name__ == "__main__":
    flush_chat_history()
    a = response("description of shower heads")
    b = response("max temperature in warranty")

    chat_history = load_chat_history()