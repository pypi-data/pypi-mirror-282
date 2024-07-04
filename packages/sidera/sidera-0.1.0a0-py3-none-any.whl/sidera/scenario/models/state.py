from pydantic import BaseModel, Field

from .story import Story
from .input import Input
from .output import Output


class State(BaseModel):
    """State model."""

    name: str = Field(..., title="State Name")
    description: str = Field(default="", title="State Description")
    input: list[Input] = Field(default=[], title="Input Signals")
    output: list[Output] = Field(default=[], title="Output Signals")
    stories: list[Story] = Field(default=[], title="Transition Stories")
