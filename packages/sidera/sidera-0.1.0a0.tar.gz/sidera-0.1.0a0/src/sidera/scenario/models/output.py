from pydantic import BaseModel, Field


class Output(BaseModel):
    """Output model."""

    signal: str = Field(..., title="Output Signal")
    value: int | float | str = Field(..., title="Output Value")
