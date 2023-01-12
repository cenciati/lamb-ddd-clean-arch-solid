# pylint: disable=no-name-in-module, no-self-argument, unused-private-member
from datetime import datetime
from typing import Any, Optional
from uuid import uuid4

from pydantic import (
    UUID4,
    BaseModel,
    EmailStr,
    Field,
    PrivateAttr,
    ValidationError,
    validator,
)

from src.domain.value_object.slug import Slug


class User(BaseModel):
    """User entity.
    Attributes:
        id (int): Unique identifier.
        email (EmailStr): Valid an unique email.
        instance_slug (Slug): Instance that has been given access in.
        created_at (datetime): Date when it was created.
        updated_at (datetime): Date when it was last updated.
    """

    id: UUID4 = Field(default_factory=uuid4)
    email: EmailStr
    password: str
    instance_slug: Slug
    __created_at: datetime = PrivateAttr(default_factory=datetime.utcnow)
    __updated_at: datetime = PrivateAttr(default_factory=datetime.utcnow)

    @validator("password", pre=True, always=True)
    def ensure_password_consistency(cls, value) -> str:
        if not isinstance(value, str):
            raise ValidationError("Password must be a string value.")
        if len(value) < 8:
            raise ValidationError("Password must have at least 8 characters.")
        if len(value) > 32:
            raise ValidationError("Password must have at most 32 characters.")
        return value

    @property
    def created_at(self) -> datetime:
        return self.__created_at

    @property
    def updated_at(self) -> datetime:
        return self.__updated_at

    def update(
        self,
        new_email: Optional[EmailStr],
        new_password: Optional[str],
        new_instance_slug: Optional[Slug],
    ) -> None:
        if new_email:
            self.email = new_email
        if new_password:
            self.password = new_password
        if new_instance_slug:
            self.instance_slug = new_instance_slug
