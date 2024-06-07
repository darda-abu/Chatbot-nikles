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

query_maker_template = """Based on the table schema and some chat history below, write a SQL query that would answer the user's question
follow these rules while making the query

- Only produce SELECT queries.
- Never produce a query that will delete something from the database.
- Always limit the output limit to 8
- If any relevant query cannot be made, make a query that will not generate any data but can be run the database without any error.

{schema}
{chat_history}
Question: {input}
SQL Query:"""

query_maker_prompt = ChatPromptTemplate.from_template(query_maker_template)

query_based_NL_template = """Based on the table schema below, question, sql query, and sql response and chat history, write a natural language response. DO NOT ever 
mention the table name in the question or response. DO NOT mention the sql query. Act like the query is for a shop that produces some products and you are the owner.
Be consciese and accurate in your response.

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