# pylint: disable=no-name-in-module, missing-class-docstring
from datetime import datetime
from typing import Optional

from pydantic import UUID4, BaseModel, EmailStr

from src.domain.value.slug import Slug


class InputFindUserDTO(BaseModel):
    id: Optional[UUID4]
    email: Optional[EmailStr]


class OutputFindUserDTO(BaseModel):
    id: UUID4
    email: EmailStr
    password: str
    instance_slug: Slug
    created_at: datetime
    updated_at: datetime
