# pylint: disable=no-name-in-module, missing-class-docstring
from pydantic import BaseModel, EmailStr


class InputAddUserDTO(BaseModel):
    email: EmailStr
    password: str
    instance_slug: str
