# pylint: disable=no-name-in-module, no-self-argument, unused-private-member
from datetime import datetime
from typing import Optional
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

from src.domain.value.slug import Slug


class User(BaseModel):
    """It represents an user entity.
    Attributes:
        id (UUID4): Unique identifier.
        email (EmailStr): Valid and unique email.
        password (str): User password.
        instance_slug (Slug): Instance where it has access.
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
    def _ensure_password_consistency(cls, value: str) -> str:
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

    @updated_at.setter
    def updated_at(self, value) -> None:
        self.__updated_at = value

    def update(
        self,
        new_email: Optional[EmailStr],
        new_password: Optional[str],
        new_instance_slug: Optional[str],
    ) -> None:
        if new_email:
            self.email = new_email
        if new_password:
            self.password = new_password
        if new_instance_slug:
            self.instance_slug = Slug(name=new_instance_slug)
        was_there_any_update: bool = new_email or new_password or new_instance_slug
        if was_there_any_update:
            self.__updated_at = datetime.utcnow()

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.id == other.id
        return False

    def __repr__(self) -> str:
        return f"""
            <User(id={self.id},
            email={self.email},
            password={self.password},
            instance_slug={self.instance_slug})>
        """
