"""Base agent module for all Beatsyndicat agents."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Optional

import yaml


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
        self.config: Dict[str, Any] = {}
        self._load_config()

    def _load_config(self) -> None:
        if not self.config_path:
            return

        path = Path(self.config_path)
        if not path.exists():
            return

        try:
            with path.open("r", encoding="utf-8") as handle:
                loaded = yaml.safe_load(handle) or {}
        except Exception:
            loaded = {}

        self.config = loaded if isinstance(loaded, dict) else {}
        self.state.config = self.config
        self.state.enabled = bool(self.config.get("project", {}).get("enabled", True))
        self.state.agent_name = self.config.get("project", {}).get("name", self.state.agent_name)

    def run_cycle(self) -> Dict[str, Any]:
        stack_summary = {
            "project": self.config.get("project", {}).get("name", "beatsyndicat"),
            "version": self.config.get("project", {}).get("version", "10.0.0"),
            "release": self.config.get("project", {}).get("release", "Genesis"),
            "stacks": self.config.get("project", {}).get("active_stacks", ["platform", "plugin", "ai", "database", "knowledge"]),
        }
        return {
            "agent": self.state.agent_name,
            "status": "ok",
            "message": "Agent cycle executed.",
            "config": stack_summary,
        }

    def start(self) -> Dict[str, Any]:
        return self.run_cycle()

    def stop(self) -> None:
        return None
