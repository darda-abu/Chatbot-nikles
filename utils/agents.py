from langchain.agents import initialize_agent
from utils.tools import *
from dotenv import load_dotenv
from utils.prompts import agent_prompt

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
llm = ChatOpenAI(model="gpt-3.5-turbo")

tools = [product_tool, docs_tool]
conv_agent = initialize_agent(
    agent="chat-conversational-react-description",
    tools=tools,
    llm=llm,
    verbose=False,
    max_iterations=3,
    early_stopping_method='generate',
    memory=conversational_memory,
    agent_kwargs={
        'prefix': agent_prompt
    }
)
# few shot promting in router, tempera
for i in range(5):
    x = input("wot?")
    y = conv_agent.invoke(x)
    print(y)
    print(y['output'])