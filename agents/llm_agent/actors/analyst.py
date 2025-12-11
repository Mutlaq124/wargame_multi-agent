from typing import List, Literal, Optional

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


class Position(BaseModel):
    x: int = Field(description="X coordinate on the grid.")
    y: int = Field(description="Y coordinate on the grid.")


class Action(BaseModel):
    """
    Flat action schema for simpler LLM outputs. Type is an enum; other fields are conditional by type.
    """

    type: Literal["MOVE", "SHOOT", "TOGGLE", "WAIT"] = Field(
        description="Action keyword. Allowed: MOVE | SHOOT | TOGGLE | WAIT.",
        examples=["MOVE", "SHOOT", "TOGGLE", "WAIT"],
    )
    direction: Optional[Literal["UP", "DOWN", "LEFT", "RIGHT"]] = Field(
        default=None,
        description="MOVE only: direction to move one cell.",
        examples=["UP", "DOWN", "LEFT", "RIGHT"],
    )
    destination: Optional[Position] = Field(
        default=None,
        description="MOVE only: destination after moving (x,y).",
    )
    target: Optional[int] = Field(
        default=None,
        description="SHOOT only: enemy unit id to target.",
    )
    on: Optional[bool] = Field(
        default=None,
        description="TOGGLE only: true to activate SAM radar/weapon system, false to go dark/stealth (SAM units only).",
    )

class ActionAnalysis(BaseModel):
    action: Action = Field(description="Specific action being considered for the unit.")
    implication: str = Field(description="Expected tactical effect or tradeoff of this action.")

class UnitInsight(BaseModel):
    unit_id: int = Field(description="Identifier for the unit in the current game_state.")
    role: str = Field(description="Role or mission context of the unit.")
    key_considerations: List[str] = Field(
        description="Bullet points on threats, resources, positioning, or timing relevant to this unit."
    )
    action_analysis: List[ActionAnalysis] = Field(
        description="Action options for the unit with their implications. Include all feasible options, even 'WAIT'."
    )

class GameAnalysis(BaseModel):
    unit_insights: List[UnitInsight] = Field(
        description="Unit-level analysis items. Start with the most threatened or impactful units."
    )
    spatial_status: str = Field(
        description="Short narrative of formation posture, positioning relative to enemies, and maneuver space."
    )
    critical_alerts: List[str] = Field(
        description="Ordered list of urgent risks that demand commander attention, prefixed with severity."
    )
    opportunities: List[str] = Field(
        description="Offensive or positional openings the team can exploit, prefixed with severity."
    )
    constraints: List[str] = Field(
        description="Key limitations such as ammo, detection gaps, terrain edges, or coordination risks."
    )
    situation_summary: str = Field(
        description="Overall tactical snapshot combining threats, openings, and intent for the next turn."
    )

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

### OUTPUT FORMAT
Return JSON that matches the GameAnalysis schema:
- unit_insights: ordered list of UnitInsight objects with key considerations and action analyses per unit.
- critical_alerts: most urgent issues first, each prefixed with severity (e.g., HIGH/MEDIUM/LOW).
- opportunities: actionable openings, prefixed with severity.
- constraints: limiting factors or coordination risks that affect options.
- spatial_status: brief posture and positioning narrative.
- situation_summary: concise commander-ready summary tying alerts and intent together.
- Actions must use this flat schema:
  - type: MOVE | SHOOT | TOGGLE | WAIT (enum)
  - MOVE fields: direction in [UP, DOWN, LEFT, RIGHT], optional destination {x,y}
  - SHOOT fields: target is enemy unit id
  - TOGGLE fields: on=true/false, only for SAM units (activates/deactivates radar/weapon system)
  - WAIT fields: no additional fields
  - Examples: {"type":"MOVE","direction":"UP","destination":{"x":10,"y":8}} | {"type":"SHOOT","target":3} | {"type":"TOGGLE","on":false} | {"type":"WAIT"}

### GAME STATE 
{ctx.deps.game_state}

### RECENT STEPS
{ctx.deps.step_info_list}
"""
