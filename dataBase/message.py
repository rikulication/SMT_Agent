from sqlalchemy import create_engine, String, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

# 数据库连接
engine = create_engine("sqlite:///dataBase/customer_service.db")


# ORM 基类
class Base(DeclarativeBase):
    pass


class Conversation(Base):
    __tablename__ = "conversation"

    session_id: Mapped[str] = mapped_column(String(50), primary_key=True)


class Message(Base):
    __tablename__ = "message"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    session_id: Mapped[str] = mapped_column(ForeignKey("conversation.session_id"))
    role: Mapped[str] = mapped_column(String(10))
    content: Mapped[str] = mapped_column(Text)
    message_time: Mapped[str] = mapped_column(String(20))


class Order(Base):
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    session_id: Mapped[str] = mapped_column(ForeignKey("conversation.session_id"))
    order_id: Mapped[str] = mapped_column(String(20))
    order_state: Mapped[str] = mapped_column(String(20))
    order_time: Mapped[str] = mapped_column(String(20))


if __name__ == "__main__":
    Base.metadata.create_all(engine)
