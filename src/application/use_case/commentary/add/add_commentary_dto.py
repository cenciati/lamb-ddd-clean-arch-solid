# pylint: disable=no-name-in-module, missing-class-docstring
from typing import List, Optional

from pydantic import BaseModel


class InputAddCommentaryDTO(BaseModel):
    content: str
    rating: int
    tags: List[dict]
    customer_id: str
    instance_slug: str
    journey_slug: str
    automatic: Optional[bool] = False
