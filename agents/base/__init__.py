"""Base agent module for all Beatsyndicat agents."""

from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass
class AgentState:
    agent_name: str = "base"
    enabled: bool = True
    config: Dict[str, Any] = field(default_factory=dict)


class BaseAgent:
    """Common base class for all swarm agents."""

    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path
        self.state = AgentState(agent_name=self.__class__.__name__.lower())

    def run_cycle(self) -> Dict[str, Any]:
        return {
            "agent": self.state.agent_name,
            "status": "ok",
            "message": "Agent cycle executed.",
        }

    def start(self) -> None:
        self.run_cycle()

    def stop(self) -> None:
        return None
