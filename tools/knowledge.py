from langchain_core.tools import tool
from knowledge.vectorstore import Vectorstore


collection_name = "customer_service"
vectorstore = Vectorstore(collection_name)
retriever = vectorstore.load_vectorstore().as_retriever(search_kwargs={"k": 3})


@tool
def search_knowledge(query: str):
    """搜索客服知识库，获取退款、物流、售后、商品规则等信息。"""
    docs = retriever.invoke(query)
    return [{"content": doc.page_content, "metadata": doc.metadata} for doc in docs]
