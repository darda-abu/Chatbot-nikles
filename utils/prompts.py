from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)

contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)

qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)


query_prompt_template = (
    """
    You are an MySQL expert. Based on the table schema below, write a SQL query that would answer the user's question:
    {schema}

    Question: {question}
    SQL Query:
    """
)

query_prompt = ChatPromptTemplate.from_template(query_prompt_template)

query_to_NL_prompt_template = (
    """Based on the table schema below, question, sql query, and sql response, write a natural language response. DO NOT ever 
    mention the table name in the question or response. DO NOT mention the sql query. Act like the query is for a shop that produces some products and you are the owner.
    Be consciese and accurate in your response.
    {schema}

    Question: {question}
    SQL Query: {query}
    SQL Response: {response}"""
)

query_to_NL_prompt = prompt_response = ChatPromptTemplate.from_template(query_to_NL_prompt_template)

agent_prompt = "Assistant is an agent that will use two tools. And if the question is not from these tools it will say that it is sorry. It will not generate answers that the tools cannot generate. It does not have a knowledgebase itself. Anything it doesn't know, it will say sorry."


# sql_promt = (
#     """
#     You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.
# Unless the user specifies in the question a specific number of examples to obtain, query for at most 5 results using the LIMIT clause as per MySQL. You can order the results to return the most informative data in the database.
# Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
# Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
# Pay attention to use CURDATE() function to get the current date, if the question involves "today".

# Use the following format:

# Question: Question here
# SQLQuery: SQL Query to run
# SQLResult: Result of the SQLQuery
# Answer: Final answer here

# Only use the following tables:

# CREATE TABLE cb_products (
# 	code VARCHAR(255) NOT NULL, 
# 	name TEXT, 
# 	description TEXT, 
# 	url VARCHAR(255), 
# 	image_url TEXT, 
# 	category_names TEXT, 
# 	category_label TEXT, 
# 	tag_names TEXT, 
# 	PRIMARY KEY (`ID`)
# )DEFAULT CHARSET=utf8mb4 ENGINE=InnoDB COLLATE utf8mb4_general_ci

# /*
# 3 rows from cb_products table:
# ID	code	name	description	url	image_url	category_names	category_label	tag_names
# 9237	B4705N	SHOWER HEAD TRONICO 250	• Contemporary organic • Ø 250 mm – L-M 415 • Intelligent water distribution resulting in minimal wa	https://www.nikles.com/product/shower-head-tronico-250	https://www.nikles.com/wp-content/uploads/2020/05/B4705N1-scaled.jpg	Head Showers	Tronico	Airdrop, Easy-to-clean
# 9251	BLS.001.07N	LIPS CASCADE SHOWER HEAD - MATTE BLACK	• Outstanding contemporary • Dimensions: 215 x 82.5 • Cascade spray with intelligent water • Materia	https://www.nikles.com/product/lips-cascade-shower-head-black	https://www.nikles.com/wp-content/uploads/2022/03/BLS.001.07N.jpg	Head Showers	Lips	Cascade Shower
# 	LIPS CASCADE SHOWER HEAD - RED	• Outstanding contemporary • Dimensions: 215 x 82.5 • Cascade spray with intelligent water • Materia	https://www.nikles.com/product/lips-cascade-shower-head-red	https://www.nikles.com/wp-content/uploads/2022/03/BLS.001.RRN_.jpg	Head Showers	Lips	Cascade Shower
# */

# Question: {input}
# """
# )
