from pydantic import BaseModel, ConfigDict, FilePath, Field

from .constants import DEFAULT_CONFIG_FILE


class ConfigModel(BaseModel):
    """Base class for the configuration models."""

    model_config = ConfigDict(validate_assignment=True, extra="ignore")

    def update(self, **new_data):
        for field, value in new_data.items():
            if hasattr(self, field):
                setattr(self, field, value)


class ArgsModel(ConfigModel):
    """Arguments model."""

    config: FilePath | None = Field(
        default=None,
        description=f"Path of the configuration file that replaces the default '{DEFAULT_CONFIG_FILE}'.",
    )
    scenario: FilePath | None = Field(
        default=None, description="Path of the scenario file to load."
    )


class CoreConfigModel(ConfigModel):
    """Config class for the application."""

    pass
