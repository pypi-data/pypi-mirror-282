"""Implement model for blueprint summary."""
from pathlib import Path
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, field_validator


class BlueprintSummary(BaseModel):
    """Detailed summary of a Covalent blueprint."""

    name: str
    type: str
    inputs: Dict[str, Any]
    executors: Dict[str, Any]
    environments: List[Dict[str, Any]]
    volumes: List[str]
    source_file: Optional[str] = None
    source: Optional[str] = None

    model_config = ConfigDict(extra="forbid")

    @field_validator("executors")
    @classmethod
    def _clean_up_executors(cls, value):
        remove_fields = ["settings", "validate_environment", "volume_id"]
        for target, executor_dict in value.items():
            value[target] = {
                k: v for k, v in executor_dict.items()
                if k not in remove_fields
            }
        return value

    @field_validator("name")
    @classmethod
    def _clean_up_name(cls, value):
        return value.lstrip("_")

    @field_validator("environments")
    @classmethod
    def _clean_up_environments(cls, value):
        remove_fields = ["timeout", "wait"]
        new_envs = []
        for env in value:
            env = {
                k: v for k, v in env.items()
                if k not in remove_fields
            }
            new_envs.append(env)
        return new_envs

    def get_source(self):
        """Read the source script from the source file."""
        if not self.source_file.is_file():
            raise FileNotFoundError(f"File not found: {self.source_file}")

        # Read source script.
        self.source = self.source_file.read_text()
