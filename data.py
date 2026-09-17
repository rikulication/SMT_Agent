from fastapi import FastAPI
from sqlalchemy.orm import Session
from dataBase.message import *
from schemas.chat import AgentInput

app = FastAPI()

@app.post("/data")
def getData(response: AgentInput):
    print(response)
    session_id = response.user_messages[0].session_id
    with Session(engine) as session:
        conversation = Conversation(session_id=session_id)
        message = [
            Message(
                session_id=msg.session_id,
                role=msg.role,
                content=msg.content,
                message_time=msg.message_time,
            )
            for msg in response.user_messages
        ]
        order = [
            Order(
                session_id=msg.session_id,
                order_id=msg.orderId,
                order_state=msg.orderState,
                order_time=msg.orderTime,
            )
            for msg in response.order_detail
        ]
        session.add(conversation)
        session.add_all(message)
        session.add_all(order)
        session.commit()
