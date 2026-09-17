from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SKILL_DIR = BASE_DIR / "skills"

AVAILABLE_SKILLS = {
    "pre_sales",
    "order",
    "logistics",
    "after_sales",
    "dispute",
}

def load_skill(skill_name: str) -> str:

    if skill_name not in AVAILABLE_SKILLS:
        raise ValueError(
            f"不支持的Skill: {skill_name}"
        )

    skill_path = SKILL_DIR / skill_name / "skill.md"

    if not skill_path.exists():
        raise FileNotFoundError(
            f"Skill文件不存在: {skill_path}"
        )

    return skill_path.read_text(
        encoding="utf-8"
    )
