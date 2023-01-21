# pylint: disable=no-name-in-module, missing-class-docstring
from pydantic import BaseModel, EmailStr

from src.domain.value.slug import Slug


class AddUserDTO(BaseModel):
    email: EmailStr
    password: str
    instance_slug: Slug
