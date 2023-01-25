# pylint: disable=no-name-in-module,no-self-argument,invalid-name,duplicate-code
from datetime import datetime
from typing import List
from uuid import uuid4

from pydantic import UUID4, BaseModel, Field, PrivateAttr, ValidationError, validator

from src.domain.value.rating import Rating
from src.domain.value.slug import Slug
from src.domain.value.tag import Tag


class Commentary(BaseModel):
    """It represents a commentary entity.
    Attributes:
        id (UUID4): Unique identifier.
        content (str): Commentary text by itself. Written thoughts
            about what someone experienced in somewhere.
        rating (Rating): Score and is_detractor flag indicating in
            a measurable way how much someone enjoyed the experience
            and whether they are a detractor or promoter respectively.
        tags (List[Tag]): Set of tag(s) containing information about the
            topics liked and disliked by someone. It may also be an empty list.
        customer_id (UUID4): Unique identifier from the customer who rated it.
        instance_slug (Slug): Identifier of what company instance was rated.
        journey_slug (Slug): Identifier of which specific part of the customer
            journey was rated.
        automatic (bool): Whether the tags were classified manually or
            by an artificial intelligence.
        experience_date (datetime): Date when the experience occured.
    """

    id: UUID4 = Field(default_factory=uuid4)
    content: str
    rating: Rating
    tags: List[Tag] = []
    customer_id: UUID4
    instance_slug: Slug
    journey_slug: Slug
    automatic: bool = False
    __experience_date: datetime = PrivateAttr(default_factory=datetime.utcnow)

    @property
    def experience_date(self) -> datetime:
        return self.__experience_date

    @validator("content", pre=True, always=True)
    def ensure_content_consistency(cls, value: str) -> str:
        if not isinstance(value, str):
            raise ValidationError("Content must be a string value.")
        if len(value) > 2000:
            raise ValidationError("Content must not be longer than 2000 characters.")
        return value

    @validator("automatic", pre=True, always=True)
    def ensure_automatic_consistency(cls, value: bool) -> bool:
        if not isinstance(value, bool):
            raise ValidationError("Automatic must be a True or False value.")
        return value

    def set_automatic(self) -> None:
        """Sets automatic classified flag as True."""
        self.automatic = True

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Commentary):
            return self.id == other.id
        return False

    def __repr__(self) -> str:
        return f"""
            <Commentary(id={self.id},
            content={self.content},
            rating={self.rating},
            tags={self.tags},
            customer_id={self.customer_id},
            instance_slug={self.instance_slug},
            journey_slug={self.journey_slug},
            automatic={self.automatic})>
        """
