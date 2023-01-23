# pylint: disable=no-name-in-module, missing-class-docstring
from typing import Optional

from pydantic import UUID4, BaseModel, EmailStr

from src.domain.value.cpf import Cpf


class InputFindCustomerDTO(BaseModel):
    id: Optional[UUID4]
    email: Optional[EmailStr]
    cpf: Optional[Cpf]


class OutputFindCustomerDTO(BaseModel):
    id: UUID4
    full_name: str
    email: EmailStr
    cpf: Cpf
