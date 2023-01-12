# pylint: disable=no-name-in-module, missing-class-docstring
from pydantic import BaseModel, EmailStr

from src.domain.value_object.slug import Slug


class AddUserDTO(BaseModel):
    email: EmailStr
    password: str
    instance_slug: Slug
