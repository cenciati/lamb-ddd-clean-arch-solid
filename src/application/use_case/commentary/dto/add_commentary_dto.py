# pylint: disable=no-name-in-module, missing-class-docstring
from typing import List, Optional

from pydantic import UUID4, BaseModel

from src.domain.value.rating import Rating
from src.domain.value.slug import Slug
from src.domain.value.tag import Tag


class AddCommentaryDTO(BaseModel):
    content: str
    rating: Rating
    tags: List[Tag] | None
    customer_id: UUID4
    instance_slug: Slug
    journey_slug: Slug
    automatic: Optional[bool] = False
