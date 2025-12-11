from dataclasses import dataclass, field
from typing import Optional, Any

from env import StepInfo


@dataclass
class GameDeps:
    current_turn_number: int = 0

    multi_phase_strategy: Optional[str] = None
    current_phase_strategy: Optional[str] = None

    entity_roles: Optional[dict[int, str]] = None

    callback_conditions: Optional[str] = None

    game_state: dict[int, Any] = field(default_factory=dict)
    step_info_list: list[StepInfo] = field(default_factory=list)


COMBAT_GAME_DEPS = GameDeps()
