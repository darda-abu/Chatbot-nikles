from langchain_community.utilities import SQLDatabase
from utils.prompts import  query_maker_prompt, query_based_NL_prompt
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from utils.helper import load_chat_history, dump_chat_history
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

def run_sql_chain(input,chat_history, uri= 'mysql+mysqlconnector://root:@127.0.0.1:3306/products'):
    mysql_uri = uri
    db = SQLDatabase.from_uri(mysql_uri)

    # db = Database(uri)
    
    llm = ChatOpenAI(temperature=0.05)

    def get_schema(_):
        schema = db.get_table_info()
        return schema
    
    sql_chain = (
        RunnablePassthrough.assign(schema=get_schema)
        | query_maker_prompt
        | llm.bind(stop=["\nSQLResult:"])
        | StrOutputParser()
    )

    def run_query(query):
        return db.run(query)
    
    sql_chain = (
        RunnablePassthrough.assign(query=sql_chain).assign(
            schema=get_schema,
            response=lambda vars: run_query(vars["query"]),
        )
        | query_based_NL_prompt
        | llm
    )
    return sql_chain.invoke({"input": input, "chat_history": chat_history}).content

