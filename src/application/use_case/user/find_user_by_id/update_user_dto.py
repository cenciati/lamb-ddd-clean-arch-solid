# pylint: disable=no-name-in-module, missing-class-docstring
from typing import Optional

from pydantic import BaseModel, EmailStr

from src.domain.value_object.slug import Slug


class UpdateUserDTO(BaseModel):
    email: Optional[EmailStr]
    password: Optional[str]
    instance_slug: Optional[Slug]
