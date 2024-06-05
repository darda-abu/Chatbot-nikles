from langchain.agents import Tool
from utils.chains import *

product_tool = Tool(
    name = "database",
    func=run_sql_chain,
    description="Use this tool when ansering about any product or object, anything related to products, product description, whenever you think it is necessary to search a database, or when you are not sure",
)
docs_tool = Tool(
    name= "website",
    func=run_scrapper_chain,
    description="Use this tool when ansering about technologies, history, and warranties and news, DO NOT use it if any kind of product related question is asked",
    
)