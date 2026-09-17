from planner import make_plan
from skill import load_skill
from executor import executor, load_prompt

from tools import search_knowledge

def handle_customer(
    user_message: str,
    order_detail: list[dict] | None = None,
):
    order_detail = order_detail or []
    # ==================================================
    # 第一次调用
    # Planner
    # ==================================================
    plan = make_plan(
        user_message=user_message,
        order_detail=order_detail,
    )
    print("========== Planner ==========")
    print(plan.model_dump_json(indent=2))

    # ==================================================
    # 根据 Planner 结果加载 Skill
    # ==================================================

    skill = load_skill(plan.skill)

    # ==================================================
    # 加载 Prompt Template
    # ==================================================

    prompt_template = load_prompt(plan.prompt_template)

    # ==================================================
    # 根据 Planner 结果查询知识库
    # ==================================================

    knowledge = ""
    if "search_knowledge" in plan.tools:
        knowledge_results = []
        for kb in plan.knowledge_bases:
            result = search_knowledge.invoke(
                {
                    "query": user_message,
                    "knowledge_base": kb,
                }
            )
            knowledge_results.append(f"""
===== {kb} =====
{result}
""")

        knowledge = "\n".join(knowledge_results)

    # ==================================================
    # 第二次调用
    # Executor
    # ==================================================

    executor_input = f"""
【买家消息】
{user_message}
【Planner处理计划】
{plan.model_dump_json(indent=2)}
【当前Skill】
{skill}
【订单信息】
{order_detail}
【知识库内容】
{knowledge}
【Prompt模板】
{prompt_template}
请根据以上信息生成最终客服回复。
"""
    result = executor.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": executor_input,
                }
            ]
        }
    )

    # ==================================================
    # 获取最终消息
    # ==================================================

    return result["messages"][-1].content
