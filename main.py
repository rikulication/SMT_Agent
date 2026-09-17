from fastapi import FastAPI
from agent import agent
from schemas.chat import AgentInput,ChatResponse
import json
app = FastAPI()

@app.post("/chat")
def chat(response: AgentInput):
    print(response)
    messages = [
        {
            "role": msg.role,
            "content": msg.content,
            "time":msg.message_time
        }
        for msg in response.user_messages
    ]
    
    order_detail = [
        order.model_dump()
        for order in response.order_detail
    ]
    messages = messages[-20:]
    result = agent.invoke({
        "messages": json.dumps({"user_messages" : messages, "order_detail" : order_detail})
    })
    answer = result["messages"][-1].content
    return {"result":result,"answer":answer}