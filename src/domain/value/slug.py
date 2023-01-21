# pylint: disable=no-name-in-module, no-self-argument, invalid-name
from pydantic import BaseModel, ValidationError, validator


class Slug(BaseModel):
    """Slug value object.
    Attributes:
        name (str): A valid and unique name for the slug.
    """

    name: str

    @validator("name", pre=True, always=True)
    def ensure_slug_consistency(cls, value) -> str:
        if not isinstance(value, str):
            raise ValidationError("Slug must be a string value.")
        if len(value) < 3:
            raise ValidationError("Slug must have at least 3 characters.")
        if len(value) > 24:
            raise ValidationError("Slug must have at most 24 characters.")
        if " " in value:
            raise ValidationError("Slug must not have any whitespace.")
        return value.lower()
