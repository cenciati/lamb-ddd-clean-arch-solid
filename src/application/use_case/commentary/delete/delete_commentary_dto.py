# pylint: disable=no-name-in-module, missing-class-docstring

from pydantic import BaseModel


class InputDeleteCommentaryDTO(BaseModel):
    id: str
