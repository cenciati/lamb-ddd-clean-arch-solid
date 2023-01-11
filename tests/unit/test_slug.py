# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa
import pytest
from pydantic.error_wrappers import ValidationError

from src.domain.value_object.slug import Slug


def test_slug_should_raise_an_error_if_it_has_any_whitespaces() -> None:
    # Act
    invalid_slug: str = "la mb"

    # Assert
    with pytest.raises(ValidationError):
        Slug(name=invalid_slug)
