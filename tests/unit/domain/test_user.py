# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa
import pytest
from pydantic.error_wrappers import ValidationError

from src.domain.entity.user import User
from src.domain.value.slug import Slug


def test_user_password_should_raise_an_error_if_it_is_shorter_than_8_chars() -> None:
    # assert
    with pytest.raises(ValidationError):
        User(
            email="johndoe@mail.com",
            password="a" * 7,
            instance_slug=Slug(name="lamb"),
        )


def test_user_password_should_raise_an_error_if_it_is_longer_than_32_chars() -> None:
    # Assert
    with pytest.raises(ValidationError):
        User(
            email="johndoe@mail.com",
            password="a" * 33,
            instance_slug=Slug(name="lamb"),
        )
