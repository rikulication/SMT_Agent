from langchain_openai import ChatOpenAI
from config import *
from langchain.agents import create_agent
from tools import get_today
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

llm = ChatOpenAI(
    model=LLM_MODEL_ID, base_url=LLM_BASE_URL, api_key=LLM_API_KEY, temperature=0
)

messages = []

agent = create_agent(
    model=llm,
    tools=[get_today],
    system_prompt="""
    你是一个万能助手
    """,
    
)

while True:
    question = input("\n请输入问题:")
    if question.lower() == "exit":
        break
    messages.append(HumanMessage(content=question))
    result = agent.invoke({"messages": messages})

    print(f"上下文列表:\n{messages}\n")
    print(result["messages"][-1].content)
    messages = result["messages"]
