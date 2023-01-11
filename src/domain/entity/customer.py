# pylint: disable=no-name-in-module, no-self-argument
from uuid import uuid4

from pydantic import UUID4, BaseModel, EmailStr, Field, ValidationError, validator

from src.domain.value_object.cpf import Cpf


class Customer(BaseModel):
    """Customer entity.
    Attributes:
        id (uuid4): Unique identifier.
        full_name (str): Customer full name.
        email (EmaiLStr): Valid and unique e-mail address.
        cpf (Cpf): Valid and unique registration number
            without any kind of ponctuation.
    """

    id: UUID4 = Field(default_factory=uuid4)
    full_name: str
    email: EmailStr
    cpf: Cpf

    @validator("full_name", pre=True, always=True)
    def ensure_full_name_consistency(cls, value) -> str:
        if not isinstance(value, str):
            raise ValidationError("Name must be a string value.")
        if len(value) < 8:
            raise ValidationError("Name must have at least 8 characters.")
        if len(value) > 64:
            raise ValidationError("Name must have at most 64 characters.")
        return value
