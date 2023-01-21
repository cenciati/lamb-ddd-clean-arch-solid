# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa
import pytest
from pydantic.error_wrappers import ValidationError

from src.domain.entity.customer import Customer


def test_customer_name_should_raise_an_error_if_its_size_is_longer_than_60() -> None:
    # Arrange
    invalid_name: str = "Test" * 16

    # Assert
    with pytest.raises(ValidationError):
        Customer(full_name=invalid_name, email="johndoe@mail.com", cpf="01234567890")


def test_customer_email_should_raise_an_error_if_it_receives_an_invalid_email() -> None:
    # Arrange
    invalid_emails: list = [
        "abc@.com",
        "@mail.com",
        "abc@mail",
        "asidsaiasd",
        123,
        "abcmail.com",
        "@.com",
        ".com",
    ]

    # Act
    with pytest.raises(ValidationError):
        for email in invalid_emails:
            Customer(full_name="John Doe", email=email, cpf="01234567890")
