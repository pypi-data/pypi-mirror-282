from pydantic import BaseModel, Field


class Input(BaseModel):
    """Input model."""

    signal: str = Field(..., title="Input Signal")
    value: int | float | str = Field(..., title="Input Value")
