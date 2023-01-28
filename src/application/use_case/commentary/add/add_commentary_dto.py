# pylint: disable=no-name-in-module,missing-class-docstring,duplicate-code
from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import UUID4, BaseModel

from src.domain.value.rating import Rating
from src.domain.value.slug import Slug
from src.domain.value.tag import Tag


class InputAddCommentaryDTO(BaseModel):
    content: str
    rating: int
    tags: Optional[List[Dict[str, Any]]] = []
    customer_id: str
    instance_slug: str
    journey_slug: str
    automatic: Optional[bool] = False


class OutputAddCommentaryDTO(BaseModel):
    id: UUID4
    content: str
    rating: Rating
    tags: List[Tag]
    customer_id: UUID4
    instance_slug: Slug
    journey_slug: Slug
    automatic: Optional[bool] = False
    experience_date: datetime
