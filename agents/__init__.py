"""
Agent interface and implementations for the Grid Combat Environment.

This module provides:
- BaseAgent: Abstract interface for all agents
- RandomAgent: Simple random action agent for testing/default scenarios
- HumanAgent: Human-controlled agent for UI interaction
- LLMAgentV2: Main hierarchical multi-agent AI (agentic_agent)
"""

from .base_agent import BaseAgent
from .factory import create_agent_from_spec

from .registry import register_agent, resolve_agent_class
from .spec import AgentSpec
from .random_agent import RandomAgent
from .agentic_agent.llm_agent_v2 import LLMAgentV2
from .human_agent import HumanAgent
from .team_intel import TeamIntel, VisibleEnemy

__all__ = [
    "BaseAgent",
    "AgentSpec",
    "create_agent_from_spec",
    "register_agent",
    "resolve_agent_class",
    "RandomAgent",
    "LLMAgentV2",
    "HumanAgent",
    "TeamIntel",
    "VisibleEnemy",
]

