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


query_example="""

    Question: show me head showers that looks like lips
    SQL Query: SELECT name, url from cb_products where category_names LIKE '%head shower%' and (name like '%lips%' or category_label LIKE '%lips%') limit 8;

    Question: show me easy to clean faucets
    SQL Query: SELECT name, url from cb_products where  category_names LIKE '%faucet%' or category_label LIKE '%faucet%' and (tag_names like '%easy-to-clean%' ) limit 8;

    Question: Show me piano products
    SQL Query: SELECT name, url from cb_products where category_label LIKE '%piano%' or category_names LIKE '%piano%' or name LIKE '%piano%' limit 8;

    Question: What tronico you have?
    SQL Query: SELECT name, url from cb_products where category_names LIKE '%tronico%' or category_label LIKE '%tronico%' or name LIKE '%tronico%' limit 8;

    Question: Airdrop products
    SQL Query: SELECT name, url from cb_products where tag_names LIKE '%airdrop%' or name LIKE '%airdrop%' limit 8;

    Question: Show me faucets with LED features
    SQL Query: SELECT name, url from cb_products where name LIKE '%faucet%' or category_names LIKE '%faucet%' or category_label LIKE '%faucet%' or tag_names LIKE '%LED%' limit 8;

    Question: Show me shower systems with sound
    SQL Query: SELECT name, url from cb_products where name LIKE '%Shower Systems%' or category_names LIKE '%Shower Systems%' or category_label LIKE '%Shower Systems%' or tag_names LIKE '%Sound%' limit 8;

    Question: Show me bath tub kits with push button system
    SQL Query: SELECT name, url from cb_products where name LIKE '%Bath Tub Kits%' or category_names LIKE '%Bath Tub Kits%' or category_label LIKE '%Bath Tub Kits%' or tag_names LIKE '%Push Button System%' limit 8;

    Question: Show me head showers with thermostat feature
    SQL Query: SELECT name, url from cb_products where name LIKE '%Head Showers%' or category_names LIKE '%Head Showers%' or category_label LIKE '%Head Showers%' or tag_names LIKE '%Thermostat%' limit 8;

    Question: Show me fresh products with silk feature
    SQL Query: SELECT name, url from cb_products where name LIKE '%Fresh%' or category_names LIKE '%Fresh%' or category_label LIKE '%Fresh%' or tag_names LIKE '%Silk%' limit 8;

    Question: Show me shower arms with pressure control valve
    SQL Query: SELECT name, url from cb_products where name LIKE '%Shower Arms%' or category_names LIKE '%Shower Arms%' or category_label LIKE '%Shower Arms%' or tag_names LIKE '%Pressure Control Valve%' limit 8;

    Question: Show me piano products with click position system
    SQL Query: SELECT name, url from cb_products where name LIKE '%piano%' or category_names LIKE '%piano%' or category_label LIKE '%piano%' or tag_names LIKE '%Click Position System%' limit 8;

    Question: Show me techno products with airdrop feature
    SQL Query: SELECT name, url from cb_products where name LIKE '%Techno%' or category_names LIKE '%Techno%' or category_label LIKE '%Techno%' or tag_names LIKE '%Airdrop%' limit 8;

    Question: Show me infinity faucets
    SQL Query: SELECT name, url from cb_products where name LIKE '%Infinity%' or category_names LIKE '%Faucets%' or category_label LIKE '%Infinity%' limit 8;

    Question: Show me sky shower kits
    SQL Query: SELECT name, url from cb_products where name LIKE '%Sky%' or category_names LIKE '%Shower Kits%' or category_label LIKE '%Sky%' limit 8;

    Question: Show me pure shower hoses
    SQL Query: SELECT name, url from cb_products where name LIKE '%Pure%' or category_names LIKE '%Shower Hoses%' or category_label LIKE '%Pure%' limit 8;

    Question: Show me pearl hand showers
    SQL Query: SELECT name, url from cb_products where name LIKE '%Pearl%' or category_names LIKE '%Hand Showers%' or category_label LIKE '%Pearl%' limit 8;

    Question: Show me viper slide bars
    SQL Query: SELECT name, url from cb_products where name LIKE '%Viper%' or category_names LIKE '%Slide Bars%' or category_label LIKE '%Viper%' limit 8;

    Question: Show me light kitchen spray products
    SQL Query: SELECT name, url from cb_products where name LIKE '%Light%' or category_names LIKE '%Kitchen Spray%' or category_label LIKE '%Light%' limit 8;

    Question: Show me avanti accessories with easy-to-clean feature
    SQL Query: SELECT name, url from cb_products where name LIKE '%Avanti%' or category_names LIKE '%Accessoires%' or category_label LIKE '%Accessoires%' or tag_names LIKE '%easy-to-clean%' limit 8;

    Question: Show me nikles eco faucets with single lever
    SQL Query: SELECT name, url from cb_products where name LIKE '%Nikles ECO%' or category_names LIKE '%Faucets%' or category_label LIKE '%Nikles ECO%' or tag_names LIKE '%Single lever%' limit 8;

    Question: Show me head showers with carbon feature
    SQL Query: SELECT name, url from cb_products where name LIKE '%Head Showers%' or category_names LIKE '%Head Showers%' or category_label LIKE '%Head Showers%' or tag_names LIKE '%Carbon%' limit 8;

    Question: Show me shower kits with sound feature
    SQL Query: SELECT name, url from cb_products where name LIKE '%Shower Kits%' or category_names LIKE '%Shower Kits%' or category_label LIKE '%Shower Kits%' or tag_names LIKE '%Sound%' limit 8;

    Question: Show me tulipa bath tub kits
    SQL Query: SELECT name, url from cb_products where name LIKE '%Tulipa%' or category_names LIKE '%Bath Tub Kits%' or category_label LIKE '%Tulipa%' limit 8;

    Question: Show me fresh shower hoses with thermostat
    SQL Query: SELECT name, url from cb_products where name LIKE '%Fresh%' or category_names LIKE '%Shower Hoses%' or category_label LIKE '%Fresh%' or tag_names LIKE '%Thermostat%' limit 8;

    Question: Show me hand showers with click position system
    SQL Query: SELECT name, url from cb_products where name LIKE '%Hand Showers%' or category_names LIKE '%Hand Showers%' or category_label LIKE '%Hand Showers%' or tag_names LIKE '%Click Position System%' limit 8;

    Question: Show me shower systems with LED feature
    SQL Query: SELECT name, url from cb_products where name LIKE '%Shower Systems%' or category_names LIKE '%Shower Systems%' or category_label LIKE '%Shower Systems%' or tag_names LIKE '%LED%' limit 8;

    Question: Show me architect shower arms
    SQL Query: SELECT name, url from cb_products where name LIKE '%Architect%' or category_names LIKE '%Shower Arms%' or category_label LIKE '%Architect%' limit 8;

    Question: Show me uncategorized accessories
    SQL Query: SELECT name, url from cb_products where name LIKE '%Uncategorized%' or category_names LIKE '%Accessoires%' or category_label LIKE '%Uncategorized%' limit 8;

    Question: Show me kitchen spray products with push button system
    SQL Query: SELECT name, url from cb_products where name LIKE '%Kitchen Spray%' or category_names LIKE '%Kitchen Spray%' or category_label LIKE '%Kitchen Spray%' or tag_names LIKE '%Push Button System%' limit 8;

"""
distinct_values= """
category_names:
Head Showers
Shower Systems
Shower Kits
Bath Tub Kits
Architect
Fresh
Carbon
Hand Showers
Slide Bars
Kitchen Spray
Shower Arms
Accessoires
Shower Hoses
Avanti
Faucets
Uncategorized
Kopfbrausen
Handbrausen
Zubehör
Armaturen
Techno


category_label:
Tronico
Lips
Head Showers
Pure
Luce
Sound
Piano
Infinity
Hand Showers
Pearl
Sky
Light
Uncategorized
Nova
Tulipa
Viper
Handbrausen
Techno
Nikles ECO


tag_names:
Airdrop, Easy-to-clean, Thermostat, Click Position System, LED, Push Button System, Pressure Control Valve, Silk, Sound, Carbon. Single lever
"""
query_maker_template = """
You are a SQL expert. You can only make queries for this schema and question. 

Schema: {schema}
Question: {input}

You will also be given this chat history. Take this chat history into consideration while making queries.

Chat History: {chat_history}

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
- If the Question is asking something like what is the second product, or the first product, it is referencing the chat history, on that case see what was that product in the chat history and generate query for cb_products
- LED means lights
here are some examples: {{query_examples}}

query should search in name or category_names or category_label, features should be searched in tag_names.
here are all distinct vlaues in category_names, category_label, tag_names: {{distinct_values}}

SQL Query:"""



query_maker_prompt = ChatPromptTemplate.from_template(query_maker_template)

query_based_NL_template = """Based on the table schema below, question, sql query, and sql response and chat history, write a natural language response in markdown. DO NOT ever 
mention the table name in the question or response.

Follow these rules while writing the response
- DO NOT mention the sql query. If the sql response is empty, say that information about this thing is not available.
- show names with urls in markdown format. example - [name](url)
- Act like the query is for a shop that produces some products and you are the owner.
- Be consciese and accurate in your response. If you have any image url, you can send it as well.
- If the question is referencing to a past chat history. you are the AImeassage and the input question is the HumanMeassage. SO respond according to that.
- If you have included urls, say at last that click the url to visit the shop

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

