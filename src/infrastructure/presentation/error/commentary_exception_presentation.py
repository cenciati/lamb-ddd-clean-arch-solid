# pylint: disable=missing-class-docstring

from pydantic import BaseModel, Field

from src.domain.error.commentary_exception import (
    CommentariesNotFoundError,
    CommentaryNotFoundError,
)


class ErrorMessageCommentaryNotFound(BaseModel):
    detail: str = Field(example=CommentaryNotFoundError.message)


class ErrorMessageCommentariesNotFound(BaseModel):
    detail: str = Field(example=CommentariesNotFoundError.message)
