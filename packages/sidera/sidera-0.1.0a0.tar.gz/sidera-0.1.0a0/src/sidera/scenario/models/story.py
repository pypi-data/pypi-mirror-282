from pydantic import BaseModel, Field

from .scene import Scene


class Story(BaseModel):
    """Story model."""

    name: str = Field(default="", title="Story Name")
    description: str = Field(default="", title="Story Description")
    scenes: list[Scene] = Field(default=[], title="Scenes List")
    destination: str | None = Field(default=None, title="Destination State")
