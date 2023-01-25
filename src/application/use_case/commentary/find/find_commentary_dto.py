# pylint: disable=no-name-in-module, missing-class-docstring
from datetime import datetime
from typing import List

from pydantic import UUID4, BaseModel

from src.domain.value.rating import Rating
from src.domain.value.slug import Slug
from src.domain.value.tag import Tag


class InputFindCommentaryByIDDTO(BaseModel):
    id: str


class InputFindCommentaryByInstanceSlugDTO(BaseModel):
    instance_slug: str


class OutputFindCommentaryDTO(BaseModel):
    id: UUID4
    content: str
    rating: Rating
    tags: List[Tag]
    customer_id: UUID4
    instance_slug: Slug
    journey_slug: Slug
    automatic: bool
    experience_date: datetime
