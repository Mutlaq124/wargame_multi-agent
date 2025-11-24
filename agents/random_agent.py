"""
Random agent implementation for testing and baseline comparison.

This agent makes random valid decisions for all its entities.
"""

import random
from typing import Dict, Any, Optional
from env.core.actions import Action
from env.core.types import Team
from env.world import WorldState
from .base_agent import BaseAgent


class RandomAgent(BaseAgent):
    """
    Agent that takes random actions.
    
    Decision process:
    - For each entity, sample uniformly from its allowed actions.
    
    This serves as a baseline for comparing learning agents.
    """
    
    def __init__(
        self, 
        team: Team, 
        name: str = None,
        shoot_probability: float = 0.3,
        move_probability: float = 0.5,
        seed: Optional[int] = None
    ):
        """
        Initialize random agent.
        
        Args:
            team: Team to control
            name: Agent name (default: "RandomAgent")
            shoot_probability: Probability of attempting to shoot when possible
            move_probability: Probability of moving vs waiting
            seed: Random seed for reproducibility (None = random)
        """
        super().__init__(team, name)
        self.shoot_probability = shoot_probability
        self.move_probability = move_probability
        self.rng = random.Random(seed)
    
    def get_actions(
        self,
        state: Dict[str, Any],
        commands: Dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> tuple[Dict[int, Action], Dict[str, Any]]:
        """
        Generate random actions for all entities by sampling allowed actions.
        
        Args:
            state: Current game state
            commands: Optional runtime commands (ignored for random policy)
        
        Returns:
            Tuple of (actions, metadata)
        """
        world: WorldState = state["world"]
        actions = {}
        
        for entity in world.get_team_entities(self.team):
            if not entity.alive:
                continue
            allowed = entity.get_allowed_actions(world)
            if not allowed:
                continue
            actions[entity.id] = self.rng.choice(allowed)
        
        metadata = {
            "policy": "random",
            "commands": commands or {},
            "actions_count": len(actions),
        }
        return actions, metadata
