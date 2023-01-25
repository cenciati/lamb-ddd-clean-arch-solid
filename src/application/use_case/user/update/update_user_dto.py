# pylint: disable=no-name-in-module, missing-class-docstring
from typing import Optional

from pydantic import BaseModel, EmailStr


class InputUpdateUserDTO(BaseModel):
    id: str
    email: Optional[EmailStr]
    password: Optional[str]
    instance_slug: Optional[str]
