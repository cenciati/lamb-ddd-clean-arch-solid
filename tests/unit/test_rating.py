# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa
import pytest
from pydantic.error_wrappers import ValidationError

from src.domain.value_object.rating import Rating


def test_rating_score_should_raise_a_validation_error_if_it_is_lower_than_1() -> None:
    # Assert
    with pytest.raises(ValidationError):
        Rating(score=0)


def test_rating_score_should_raise_a_validation_error_if_it_is_greater_than_10() -> None:
    # Assert
    with pytest.raises(ValidationError):
        Rating(score=11)


def test_is_detractor_should_be_true_if_rating_score_is_lower_than_7() -> None:
    # Assert
    assert Rating(score=6).is_detractor() is True
    assert Rating(score=5).is_detractor() is True
    assert Rating(score=4).is_detractor() is True
    assert Rating(score=3).is_detractor() is True
    assert Rating(score=2).is_detractor() is True
    assert Rating(score=1).is_detractor() is True


def test_is_detractor_should_be_false_if_rating_score_is_equal_or_greater_than_7() -> None:
    # Assert
    assert Rating(score=7).is_detractor() is False
    assert Rating(score=8).is_detractor() is False
    assert Rating(score=9).is_detractor() is False
    assert Rating(score=10).is_detractor() is False
