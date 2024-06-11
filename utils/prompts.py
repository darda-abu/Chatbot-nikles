from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

contextualize_q_system_prompt = """Given a chat history and the latest user question \
which might reference context in the chat history, formulate a standalone question \
which can be understood without the chat history. Do NOT answer the question, \
just reformulate it if needed and otherwise return it as is."""
contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

qa_system_prompt = """You are an assistant for question-answering tasks. \
Use the following pieces of retrieved context to answer the question. \
If you don't know the answer, just say that you don't know. \
Use three sentences maximum and keep the answer concise.\

{context}"""
qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", qa_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)



query_maker_template = """You are an sql expert. Based on the table schema, question and some context below, write a SQL query that would answer the user's question


Schema: {schema}


Follow these rules while making the query

- The only valid table for query is cb_products. DO NOT make queries for other tables.
- If any SELECT query cannot be made for cb_products table, make a query that will NOT generate any data but can be run into the database without any error.
- If any relevant query cannot be made for cb_products table, make a query that will not generate any data but can be run into the database without any error.
- Only produce valid queries according to the schema.
- Only produce SELECT queries.
- Never produce a query that will delete something from the database.
- Always limit the output limit to 8
- Never generate queries that will show product ID.
- Try to send url of the product when asked about products.
- Send image_url only if specifically asked for images, on other scenarios, send url.




Question: {input}
SQL Query:"""

# query_maker_template = """Based on the table schema and input, write a SQL query that would answer the user's question



# Follow these rules while making the query

# - Only produce valid queries according to the schema.
# - Only produce SELECT queries.
# - Never produce a query that will delete something from the database.
# - Always limit the output limit to 8
# - If any relevant query cannot be made, make a query that will not generate any data but can be run into the database without any error.
# - If any SELECT query cannot be made, make a query that will NOT generate any data but can be run into the database without any error.
# - Never generate queries that will show product ID.
# - Try to send url of the product when asked about products.
# - Send image_url only if specifically asked for images, on other scenarios, send url.

# {schema}
# Question: {input}
# SQL Query:"""

query_maker_prompt = ChatPromptTemplate.from_template(query_maker_template)

query_based_NL_template = """Based on the table schema below, question, sql query, and sql response and chat history, write a natural language response in markdown. DO NOT ever 
mention the table name in the question or response.

Follow these rules while writing the response
- DO NOT mention the sql query. If the sql response is empty, say that information about this thing is not available.
- show names with urls in markdown format. example - [name](url)
- Act like the query is for a shop that produces some products and you are the owner.
- Be consciese and accurate in your response. If you have any image url, you can send it as well.
- If the question is referencing to a past chat history. Do not use the sql response. answer according to the question

{schema}

{chat_history}

Question: {input}
SQL Query: {query}
SQL Response: {response}"""
query_based_NL_prompt = ChatPromptTemplate.from_template(query_based_NL_template)

router_prompt_template = """Given the user question and chat history below, classify it as either being about `database`,or `pdf`. do not respond with more than one word.
you are given the schema of the only table in the database as well. Decide if the user question can be answered by looking at the database, if not classify as `pdf`.

remember these rules

- DO NOT respond with more than one word.
- if the input is about warranties, then classify it as `pdf`
- if the input is about products, then classify it as `database`
- if the input is about details of product types, then classify it as `pdf`
- if the input is about details of products, then classify it as `database`

Here is the schema
{schema}

<question>
{input}
</question>
{chat_history}
Classification:"""

router_prompt = ChatPromptTemplate.from_template(router_prompt_template)

