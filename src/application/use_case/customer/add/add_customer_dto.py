# pylint: disable=no-name-in-module, missing-class-docstring
from pydantic import BaseModel, EmailStr


class InputAddCustomerDTO(BaseModel):
    full_name: str
    email: EmailStr
    cpf: str
