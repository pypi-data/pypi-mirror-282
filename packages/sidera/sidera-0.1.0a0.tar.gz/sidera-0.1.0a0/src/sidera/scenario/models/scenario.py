from pathlib import Path
from pydantic import BaseModel, Field, model_validator

from .signal import Signal
from .state import State


class Scenario(BaseModel):
    """Scenario model."""

    # Hint information
    _file: Path | None = None
    _dir: Path | None = None

    name: str = Field(default="", title="Scenario Name")
    description: str = Field(default="", title="Scenario Description")

    signals: list[Signal] | None = Field(default=None, title="Signal data list")
    states: list[State] | None = Field(default=None, title="State data list")

    @model_validator(mode="after")
    def set_name(self):
        """Set name if no name."""
        if not self.name:
            self.name = "(unnamed)"
        return self
