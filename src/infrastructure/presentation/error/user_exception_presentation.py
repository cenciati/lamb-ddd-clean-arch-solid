# pylint: disable=missing-class-docstring
from pydantic import BaseModel, Field

from src.domain.error.user_exception import (
    UserDuplicateEmailError,
    UserNotFoundError,
    UsersNotFoundError,
)


class ErrorMessageUserNotFound(BaseModel):
    detail: str = Field(example=UserNotFoundError.message)


class ErrorMessageUsersNotFound(BaseModel):
    detail: str = Field(example=UsersNotFoundError.message)


class ErrorMessageUserDuplicateEmail(BaseModel):
    detail: str = Field(example=UserDuplicateEmailError.message)
