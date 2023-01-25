# pylint: disable=no-name-in-module, missing-class-docstring
from pydantic import BaseModel


class InputDeleteCustomerDTO(BaseModel):
    id: str
