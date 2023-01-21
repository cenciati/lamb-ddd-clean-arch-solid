# pylint: disable=no-name-in-module, no-self-argument
from pydantic import BaseModel, ValidationError, validator


class Cpf(BaseModel):
    """Cpf value object.
    Attributes:
        number (str): A valid and unique CPF registration
            number without any ponctuation.
    """

    number: str

    @validator("number", pre=True, always=True)
    def ensure_cpf_consistency(cls, value) -> str:
        if not isinstance(value, str):
            raise ValidationError("Cpf must be a string value.")
        if len(value) != 11:
            raise ValidationError("Cpf must have exactly 11 characters.")
        return value
