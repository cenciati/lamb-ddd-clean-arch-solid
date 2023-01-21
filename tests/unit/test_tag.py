# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa
import pytest
from pydantic.error_wrappers import ValidationError

from src.domain.value.tag import Tag


def test_tag_name_should_raise_an_error_if_it_shorter_than_3_characters() -> None:
    # Arrange
    short_tag_name: str = "a" * 2

    # Assert
    with pytest.raises(ValidationError):
        Tag(id=1, name=short_tag_name, sentiment=1, subtag=False)


def test_tag_name_should_raise_an_error_if_it_longer_than_48_characters() -> None:
    # Arrange
    long_tag_name: str = "a" * 49

    # Assert
    with pytest.raises(ValidationError):
        Tag(id=1, name=long_tag_name, sentiment=1, subtag=False)


def test_tag_sentiment_should_raise_an_error_if_it_is_not_1_or_0() -> None:
    # Assert
    with pytest.raises(ValidationError):
        Tag(id=1, name="Delivery", sentiment=3, subtag=True)


def test_tag_subtag_should_raise_an_error_if_it_is_not_a_boolean() -> None:
    # Assert
    with pytest.raises(ValidationError):
        Tag(id=1, name="Delivery - Agility", sentiment=1, subtag="True")


def test_tag_is_subtag_should_return_subtag_current_state() -> None:
    # Arrange
    tag = Tag(id=1, name="Delivery", sentiment=1, subtag=False)

    # Assert
    assert tag.is_subtag() is False
