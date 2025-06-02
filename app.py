from langchain.agents import initialize_agent, Tool, AgentType
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI()

tools = [
    Tool(name="Calculator", func=lambda x: eval(x), description="Useful for math"),
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

response = agent.run("What is 45 * 67?")
print(response)
