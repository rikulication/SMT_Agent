from langchain_core.tools import tool
import datetime
@tool
def get_today():
    """ 获取当天的日期 """
    return datetime.datetime.now().strftime("%Y-%m-%d")
