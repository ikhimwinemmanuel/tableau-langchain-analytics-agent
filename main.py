import os
from dotenv import load_dotenv

# Import LangSmith tracing (debugging in LangSmith.com)
from langsmith import Client

# Langgraph packages
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_tableau.tools.simple_datasource_qa import initialize_simple_datasource_qa


from utilities.chat import print_stream
from utilities.prompt import AGENT_SYSTEM_PROMPT

# Load environment
load_dotenv()

# Add LangSmith tracing
langsmith_client = Client()

config = {
    "run_name": "Tableau Langchain Main.py"
}

# Initialize the Tableau data source tool
def get_datasource_tool():
    return initialize_simple_datasource_qa(
        domain=os.environ['TABLEAU_DOMAIN'],
        site=os.environ['TABLEAU_SITE'],
        jwt_client_id=os.environ['TABLEAU_JWT_CLIENT_ID'],
        jwt_secret_id=os.environ['TABLEAU_JWT_SECRET_ID'],
        jwt_secret=os.environ['TABLEAU_JWT_SECRET'],
        tableau_api_version=os.environ['TABLEAU_API_VERSION'],
        tableau_user=os.environ['TABLEAU_USER'],
        datasource_luid=os.environ['DATASOURCE_LUID'],
        tooling_llm_model="gpt-4.1-nano",
        model_provider="openai"
    )



# Create the agent
def get_agent():
    llm = ChatOpenAI(model="gpt-4.1", temperature=0)
    datasource_tool = get_datasource_tool()
    tools = [datasource_tool]

    return create_react_agent(
        model=llm,
        tools=tools,
        prompt=AGENT_SYSTEM_PROMPT
    )

    
# Run once Usage
#your_prompt = 'Show sales per customer by region'
#messages = {"messages": [("user", your_prompt)]}
#print_stream(TableauLangChain.stream(messages, config=config, stream_mode="values"))

def ask_tableau_agent(question: str) -> str:
    agent = get_agent()

    messages = {"messages": [("user", question)]}
    result = agent.invoke(messages, config=config)

    return result["messages"][-1].content


# if __name__ == "__main__":
#     response = ask_tableau_agent("Show total Sales by Region")
#     print(response)
