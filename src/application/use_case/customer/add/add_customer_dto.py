# pylint: disable=no-name-in-module, missing-class-docstring
from pydantic import UUID4, BaseModel, EmailStr

from src.domain.value.cpf import Cpf


class InputAddCustomerDTO(BaseModel):
    full_name: str
    email: EmailStr
    cpf: str


class OutputAddCustomerDTO(BaseModel):
    id: UUID4
    full_name: str
    email: EmailStr
    cpf: Cpf
