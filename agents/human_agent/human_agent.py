"""Human agent that accepts actions from the UI."""

from typing import Dict, Any, Optional, TYPE_CHECKING

from agents.base_agent import BaseAgent
from agents.registry import register_agent
from env.core.actions import Action
from env.core.types import Team

if TYPE_CHECKING:
    from env.environment import StepInfo


@register_agent("human")
class HumanAgent(BaseAgent):
    """
    Human-controlled agent that receives actions from the UI.
    
    This agent returns WAIT actions by default, but the runner/API
    can inject actual actions via the injections mechanism.
    
    The agent signals that it's awaiting human input in its metadata,
    allowing the UI to know when to show action selection.
    """
    
    def __init__(self, team: Team, name: str = None):
        super().__init__(team, name or "Human Player")
        self._pending_actions: Dict[int, Action] = {}
    
    def set_actions(self, actions: Dict[int, Action]) -> None:
        """
        Set the actions to be used in the next get_actions call.
        
        This is called by the runner when human provides input via UI.
        """
        self._pending_actions = actions
    
    def get_actions(
        self,
        state: Dict[str, Any],
        step_info: Optional["StepInfo"] = None,
        **kwargs: Any,
    ) -> tuple[Dict[int, Action], Dict[str, Any]]:
        """
        Get actions for human-controlled entities.
        
        If actions were provided via set_actions() or injections, use those.
        Otherwise, return WAIT for all entities and signal awaiting input.
        
        Args:
            state: Current game state
            step_info: Previous step info (optional)
            **kwargs: May contain 'actions' dict from UI injection
            
        Returns:
            Tuple of (actions dict, metadata dict)
        """
        world = state["world"]
        my_entities = world.get_team_entities(self.team)
        alive_entities = [e for e in my_entities if e.alive]
        
        # Check for injected actions from UI
        raw_injected = kwargs.get("actions", {})
        
        # CRITICAL: JSON keys are always strings, but entity IDs are ints.
        # Normalize all keys to int for proper lookup.
        injected_actions: Dict[int, Any] = {}
        for k, v in raw_injected.items():
            try:
                injected_actions[int(k)] = v
            except (ValueError, TypeError):
                pass
        
        # Use injected actions if provided, otherwise use pending or default to WAIT
        actions: Dict[int, Action] = {}
        for entity in alive_entities:
            entity_id = entity.id
            
            # Priority: injected > pending > WAIT
            if entity_id in injected_actions:
                action_data = injected_actions[entity_id]
                if isinstance(action_data, Action):
                    actions[entity_id] = action_data
                elif isinstance(action_data, dict):
                    actions[entity_id] = Action.from_dict(action_data)
                else:
                    actions[entity_id] = Action.wait()
            elif entity_id in self._pending_actions:
                actions[entity_id] = self._pending_actions[entity_id]
            else:
                # Default to WAIT if no action specified
                actions[entity_id] = Action.wait()
        
        # Clear pending actions after use
        self._pending_actions.clear()
        
        metadata = {
            "agent_type": "human",
            "team": self.team.name,
            "entities_controlled": len(alive_entities),
            "actions_received": len(injected_actions),
            "actions_applied": {eid: str(a) for eid, a in actions.items()},
        }
        
        return actions, metadata
