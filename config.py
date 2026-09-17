from dotenv import load_dotenv
from os import getenv
load_dotenv()

LLM_MODEL_ID = getenv("LLM_MODEL_ID")
LLM_BASE_URL = getenv("LLM_BASE_URL")
LLM_API_KEY = getenv("LLM_API_KEY")

if __name__ == "__main__":
    print(LLM_API_KEY)



# def get_env(name: str) -> str:

#     value = getenv(name)

#     if value is None:
#         raise ValueError(
#             f"环境变量 {name} 未配置"
#         )

#     return value

