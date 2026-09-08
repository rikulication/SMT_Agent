from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from tools import search_knowledge
from config import LLM_API_KEY, LLM_BASE_URL, LLM_MODEL_ID

llm = ChatOpenAI(
    model=LLM_MODEL_ID, base_url=LLM_BASE_URL, api_key=LLM_API_KEY, temperature=0
)

agent = create_agent(
    model=llm,
    tools=[search_knowledge],
    system_prompt="""
你是一名专业的速卖通客服。

你的职责：

1. 帮助买家查询订单
2. 回答商品相关问题
3. 如果买家没下单，直接引导买家下单
4. 涉及退款、物流、售后、客服规则等问题时，识别买家意图，再从客服知识库优先查询
5. 如果订单信息比较多先分析买家提到的是哪个订单，再根据订单来进行回复
6. 不要编造订单信息,
7. 不要乱给买家承诺
8. 不要编造公司规则，不要
9. 如果知识库没有相关信息，不要自行编造
10. 回复要简洁、礼貌
    """,
    # debug=True,   
)

if __name__ == "__main__":
    messages = []

    while 1:
        user_message = input("\n请输入")
        if user_message.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_message})

        result = agent.invoke({"messages": messages})

        messages = result["messages"]

        print(result["messages"][-1].content)
