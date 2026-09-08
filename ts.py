import config
from langchain_openai import *

llm = ChatOpenAI(
    model=config.LLM_MODEL_ID, base_url=config.LLM_BASE_URL, api_key=config.LLM_API_KEY, temperature=0
)