from langchain_core.tools import tool

@tool
def get_order_status(order_id: str):
    """根据订单号查询订单状态。"""

    return {"order_id": order_id, "status": "shipped", "tracking_number": "LP123456789"}
