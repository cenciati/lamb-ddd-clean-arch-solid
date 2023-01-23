# pylint: disable=no-name-in-module, missing-class-docstring
from pydantic import UUID4, BaseModel


class InputDeleteCustomerDTO(BaseModel):
    id: UUID4
