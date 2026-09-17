from pydantic import BaseModel, Field

class AgentPlan(BaseModel):
    intent: str = Field(
        description="买家的问题意图"
    )
    skill: str = Field(
        description=(
            "需要使用的Skill，只能从 "
            "pre_sales、order、logistics、after_sales、dispute 中选择"
        )
    )
    tools: list[str] = Field(
        default_factory=list,
        description="需要使用的工具"
    )
    knowledge_bases: list[str] = Field(
        default_factory=list,
        description="需要查询的知识库"
    )
    prompt_template: str = Field(
        description=(
            "需要使用的Prompt模板，只能从 "
            "normal_reply、logistics_reply、"
            "after_sales_reply、dispute_reply 中选择"
        )
    )
    need_order: bool = Field(
        description="是否需要订单信息"
    )

