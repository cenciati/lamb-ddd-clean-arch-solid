# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa
import pytest
from pydantic.error_wrappers import ValidationError

from src.domain.value.cpf import Cpf


def test_cpf_should_raise_an_error_if_its_size_is_greater_than_11() -> None:
    # Arrange
    cpf_greater_than_11: str = "012345678901"

    # Assert
    with pytest.raises(ValidationError):
        Cpf(number=cpf_greater_than_11)


def test_cpf_should_raise_an_error_if_its_size_is_lower_than_11() -> None:
    # Arrange
    cpf_lower_than_11: str = "0123456789"

    # Assert
    with pytest.raises(ValidationError):
        Cpf(number=cpf_lower_than_11)
