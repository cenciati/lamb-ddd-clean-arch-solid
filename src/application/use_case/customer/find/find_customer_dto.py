# pylint: disable=no-name-in-module, missing-class-docstring
from pydantic import BaseModel, EmailStr

from src.domain.value.cpf import Cpf


class InputFindCustomerByIDDTO(BaseModel):
    id: str


class InputFindCustomerByEmailDTO(BaseModel):
    email: EmailStr


class InputFindCustomerByCpfDTO(BaseModel):
    cpf: str


class OutputFindCustomerDTO(BaseModel):
    id: str
    full_name: str
    email: EmailStr
    cpf: Cpf
