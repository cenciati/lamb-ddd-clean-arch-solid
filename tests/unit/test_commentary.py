# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa
from datetime import datetime
from uuid import UUID

import pytest
from pydantic.error_wrappers import ValidationError

from src.domain.entity.commentary import Commentary
from src.domain.value_object.rating import Rating
from src.domain.value_object.slug import Slug


def test_id_should_be_a_valid_uuid4(comment: Commentary) -> None:
    # Act
    comment_id: str = str(comment.id)

    # Assert
    assert UUID(comment_id)


def test_experience_date_should_be_a_valid_datetime(comment: Commentary) -> None:
    # Act
    comment_experience_date: datetime = comment.experience_date

    # Assert
    assert isinstance(comment_experience_date, datetime)


def test_content_should_raise_an_error_if_it_is_longer_than_2000() -> None:
    # Arrange
    invalid_content: str = "Test" * 501

    # Assert
    with pytest.raises(ValidationError):
        Commentary(
            content=invalid_content,
            rating=Rating(score=9),
            customer_id="ef29ffc3-9ef3-40f5-842d-8403c5eccde1",
            instance_slug=Slug(name="lamb"),
            journey_slug=Slug(name="generic"),
        )


def test_tags_should_raise_an_error_if_it_is_not_a_list_or_none() -> None:
    # Arrange
    invalid_tags: dict = {}

    # Assert
    with pytest.raises(ValidationError):
        Commentary(
            content="Test",
            rating=Rating(score=9),
            tags=invalid_tags,
            customer_id="ef29ffc3-9ef3-40f5-842d-8403c5eccde1",
            instance_slug=Slug(name="lamb"),
            journey_slug=Slug(name="generic"),
        )


def test_automatic_should_raise_an_error_if_it_is_not_a_boolean() -> None:
    # Arrange
    invalid_automatic: str = "No"

    # Assert
    with pytest.raises(ValidationError):
        Commentary(
            content="Test",
            rating=Rating(score=9),
            customer_id="ef29ffc3-9ef3-40f5-842d-8403c5eccde1",
            instance_slug=Slug(name="lamb"),
            journey_slug=Slug(name="generic"),
            automatic=invalid_automatic,
        )


def test_if_is_automatic_set_attribute_works(
    comment: Commentary,
) -> None:
    # Arrange
    comment.set_automatic()

    # Assert
    assert comment.automatic is True
