"""
Random agent implementation for testing and baseline comparison.

This agent makes random valid decisions for all its entities.
"""

import random
from typing import Dict, Any, Optional, TYPE_CHECKING
from env.core.actions import Action
from env.core.types import Team
from env.world import WorldState
from ..base_agent import BaseAgent
from ..team_intel import TeamIntel
from ..registry import register_agent
from .prompt_formatter import PromptFormatter, PromptConfig

if TYPE_CHECKING:
    from env.environment import StepInfo


@register_agent("llm_basic")
class LLMAgent(BaseAgent):
    """
    """

    def __init__(
            self,
            team: Team,
            name: str = None,
            seed: Optional[int] = None,
            **_: Any,
    ):
        """
        Initialize random agent.

        Args:
            team: Team to control
            name: Agent name (default: "RandomAgent")
            seed: Random seed for reproducibility (None = random)
        """
        super().__init__(team, name)
        self.rng = random.Random(seed)
        self.prompt_formatter = PromptFormatter()
        self.prompt_config = PromptConfig()

    def get_actions(
            self,
            state: Dict[str, Any],
            step_info: Optional["StepInfo"] = None,
            **kwargs: Any,
    ) -> tuple[Dict[int, Action], Dict[str, Any]]:
        """
        Generate random actions for all entities by sampling allowed actions.

        Args:
            state: Current game state
            step_info: Optional previous step resolution info (unused)

        Returns:
            Tuple of (actions, metadata)
        """
        world: WorldState = state["world"]
        intel: TeamIntel = TeamIntel.build(world, self.team)
        actions: Dict[int, Action] = {}
        allowed_actions: Dict[int, list[Action]] = {}

        for entity in intel.friendlies:
            if not entity.alive:
                continue
            allowed = entity.get_allowed_actions(world)
            if not allowed:
                continue
            allowed_actions[entity.id] = allowed
            actions[entity.id] = self.rng.choice(allowed)

        prompt_text, prompt_payload = self.prompt_formatter.build_prompt(
            intel=intel,
            allowed_actions=allowed_actions,
            config=self.prompt_config,
        )

        metadata = {
            "allowed_actions": allowed_actions,
            "llm_prompt": prompt_text,
            "llm_prompt_payload": prompt_payload,
        }
        return actions, metadata
