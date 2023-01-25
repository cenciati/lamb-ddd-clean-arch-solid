# pylint: disable=no-name-in-module, no-self-argument, invalid-name
from pydantic import BaseModel, ValidationError, validator


class Tag(BaseModel, frozen=True):
    """Value object for tag representation.
    Attributes:
        id (int): Unique identifier.
        name (str): Text of the topic it represents.
        sentiment (int): Whether the person rated their experience
            positive (1) or negative (0) in this specific topic.
        subtag (bool): Whether it is a tag or subtag.
    """

    id: int
    name: str
    sentiment: int
    subtag: bool

    @validator("name", pre=True, always=True)
    def ensure_name_consistency(cls, value: str) -> str:
        if not isinstance(value, str):
            raise ValidationError("Name must be a string value.")
        if len(value) < 3:
            raise ValidationError("Name must have at least 3 characters.")
        if len(value) > 48:
            raise ValidationError("Name must have at most 24 characters.")
        return value

    @validator("sentiment", pre=True, always=True)
    def ensure_sentiment_consistency(cls, value: int) -> int:
        if not isinstance(value, int):
            raise ValidationError("Sentiment must be an integer value.")
        if value not in (1, 0):
            raise ValidationError("Sentiment must be 1 or 0.")
        return value

    @validator("subtag", pre=True, always=True)
    def ensure_subtag_consistency(cls, value) -> bool:
        if not isinstance(value, bool):
            raise ValidationError("Subtag must be a boolean value.")
        return value

    def is_subtag(self) -> bool:
        return self.subtag

    def __repr__(self) -> str:
        return f"""
            <Tag(id={self.id},
            name={self.name},
            sentiment={self.sentiment},
            subtag={self.subtag}>
        """
