from typing import Literal
from pydantic import BaseModel, Field

WaitTime = Literal["any"] | float


class Scene(BaseModel):
    """Scene model."""

    name: str = Field(default="", title="Scene Name")
    description: str = Field(default="", title="Scene Description")
    wait_time: WaitTime = Field(default="any", title="Scene wait time")
    signal: str = Field(..., title="Changed signal name")
    value: int | float | str = Field(..., title="Changed signal value")
