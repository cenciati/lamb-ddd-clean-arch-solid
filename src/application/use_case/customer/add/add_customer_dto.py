# pylint: disable=no-name-in-module, missing-class-docstring
from pydantic import BaseModel, EmailStr

from src.domain.value.cpf import Cpf


class InputAddCustomerDTO(BaseModel):
    full_name: str
    email: EmailStr
    cpf: Cpf
