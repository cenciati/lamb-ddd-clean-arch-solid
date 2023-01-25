# pylint: disable=no-name-in-module, no-self-argument
from pydantic import BaseModel, ValidationError, root_validator, validator


class Rating(BaseModel):
    """Value object for rating representation.
    Attributes:
        score (int): Value between 1 and 10 which indicates
            how the user rates their experience with something.
        detractor (bool): Flag indicating whether the user is
            a detractor or a promoter.
    """

    score: int
    detractor: bool = False

    @validator("score", pre=True, always=True)
    def ensure_score_consistency(cls, value: int) -> int:
        if not isinstance(value, int):
            raise ValidationError("Score must be an integer value.")
        if value < 1 or value > 10:
            raise ValidationError("Score must be between 1 and 10.")
        return value

    @root_validator(pre=True)
    def assign_is_detractor_flag_as_a_detractor_or_promotor_based_on_given_score(
        cls, values: dict
    ) -> dict:
        if values["score"] < 7:
            values["detractor"] = True
        return values

    def is_detractor(self) -> bool:
        return self.detractor

    def __repr__(self) -> str:
        return f"""
            <Rating(score={self.score},
            detractor={self.detractor})>,
        """
