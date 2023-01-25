# pylint: disable=no-name-in-module,missing-class-docstring,duplicate-code
from datetime import datetime

from pydantic import UUID4, BaseModel, EmailStr

from src.domain.value.slug import Slug


class InputAddUserDTO(BaseModel):
    email: EmailStr
    password: str
    instance_slug: str


class OutputAddUserDTO(BaseModel):
    id: UUID4
    email: EmailStr
    password: str
    instance_slug: Slug
    created_at: datetime
    updated_at: datetime
