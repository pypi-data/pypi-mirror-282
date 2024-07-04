from pydantic import BaseModel, Field

from .value import Value


class Signal(BaseModel):
    name: str = Field(..., description="Signal name", min_length=1)
    description: str = Field(default="", description="Signal description")
    values: list[Value] = Field(..., description="Signal values list", min_length=1)
