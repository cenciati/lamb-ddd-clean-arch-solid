# pylint: disable=no-name-in-module, missing-class-docstring
from typing import Optional

from pydantic import UUID4, BaseModel, EmailStr

from src.domain.value.slug import Slug


class InputUpdateUserDTO(BaseModel):
    id: UUID4
    email: Optional[EmailStr]
    password: Optional[str]
    instance_slug: Optional[Slug]
