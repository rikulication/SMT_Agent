from pydantic import BaseModel, Field

class Message(BaseModel):
    role: str
    content: str
    message_time: str = Field(alias="time")


class Order(BaseModel):
    orderId: str | None = None
    orderState: str | None = None
    orderTime: str | None = None


class AgentInput(BaseModel):
    user_messages: list[Message] | None = None
    order_detail: list[Order] | None = None


# class ChatRequest(BaseModel):
#     dialogue : AgentInput
class ChatResponse(BaseModel):
    answer: str
