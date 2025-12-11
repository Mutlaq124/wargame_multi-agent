from pydantic_ai import Agent, RunContext
from pydantic import BaseModel, Field

from agents.llm_agent.actors.game_deps import GameDeps
from agents.llm_agent.prompts.tactics import TACTICAL_GUIDE


ANALYST_TASK = (
    "Provide a concise battlefield analysis for the commander. Cover: "
    "1) threats to AWACS or exposed units and safe repositioning ideas, "
    "2) high-value targets and feasible strikes this turn, "
    "3) radar/visibility gaps plus missing contacts with last-seen details, "
    "4) recommended team intent for the next turn. Keep it under 120 words."
)


class GameAnalysis(BaseModel):
    analysis: str = Field(description="Your game analysis/suggestions will be given to the field commander directly.")


analyst_agent = Agent(
    "openai:gpt-5-mini",
    deps_type=GameDeps,
    output_type=GameAnalysis,
    instructions="You are an AI game analyst for your team in a grid-based air combat simulation."
)

@analyst_agent.instructions
def full_prompt(ctx: RunContext[GameDeps]) -> str:

    return f"""
### TASK
{ANALYST_TASK}

### TACTICAL GUIDE (REFERENCE ONLY)
{TACTICAL_GUIDE}

### GAME STATE 
{ctx.deps.game_state}

### RECENT STEPS
{ctx.deps.step_info_list}
"""
