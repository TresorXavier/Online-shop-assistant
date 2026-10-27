
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import AIMessage, ToolMessage
from tools import search_product, check_price

load_dotenv()

agent = create_agent(
    model="anthropic:claude-sonnet-4-5",
    tools=[search_product, check_price],
    system_prompt="You are a helpful assistant."
)


def run_agent(question: str):
    response = agent.invoke({"messages": [{"role": "user", "content": question}]})

    actual_output = ""
    tool_results = []

    for message in response["messages"]:


        if isinstance(message, AIMessage) and not message.tool_calls:
            actual_output = message.content

        if isinstance(message, ToolMessage):
            tool_results.append(str(message.content))

    return actual_output, tool_results
