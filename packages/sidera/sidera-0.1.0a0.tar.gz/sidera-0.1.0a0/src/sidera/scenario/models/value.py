from typing import Any

from pydantic import BaseModel, Field, field_validator, model_validator

from ..signal_func import DEFAULT_FUNC_NAME, func_keys


class Value(BaseModel):
    """Value model of signal."""

    name: str = Field(default="", title="Value Display Name")
    description: str = Field(default="", title="Value Description")
    function: str = Field(default="", title="Signal function name")
    params: list[Any] = Field(default=[], title="Signal function fixed parameters")
    value: float | int | None = Field(
        default=None,
        title="Static signal value",
    )

    @field_validator("function", mode="after")
    @classmethod
    def check_function(cls, value):
        assert (
            value is None or value in func_keys()
        ), f"'{value}' is not defined as function name."
        return value

    @model_validator(mode="after")
    def set_func_params(self):
        """Set function parameters from value."""
        if self.function == "":
            assert self.value is not None, "'function' or 'value' is required."
            self.function = DEFAULT_FUNC_NAME
            self.params = [self.value]
        else:
            assert self.value is None, "'function' and 'value' are exclusive."

        return self

    @model_validator(mode="after")
    def set_name(self):
        """Set value name from value or function."""
        if self.name == "":
            if self.value is not None:
                self.name = str(self.value)
            else:
                self.name = self.function
                if self.params:
                    self.name += f"({', '.join(map(str, self.params))})"
        return self
