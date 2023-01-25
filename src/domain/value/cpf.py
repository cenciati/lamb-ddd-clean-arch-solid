# pylint: disable=no-name-in-module, no-self-argument
from pydantic import BaseModel, ValidationError, validator


class Cpf(BaseModel, frozen=True):
    """Value object for CPF representation.
    Attributes:
        number (str): Valid and unique CPF registration
            number without any ponctuation.
    """

    number: str

    @validator("number", pre=True, always=True)
    def ensure_cpf_consistency(cls, value: str) -> str:
        if not isinstance(value, str):
            raise ValidationError("Cpf must be a string value.")
        if len(value) != 11:
            raise ValidationError("Cpf must have exactly 11 characters.")
        if "." in value or "-" in value:
            raise ValidationError("Cpf must not have any ponctuation.")
        if not cls.validate_cpf(value):
            raise ValidationError("Cpf is not valid.")
        return value

    @classmethod
    def validate_cpf(cls, cpf: str) -> bool:
        """Checks if a CPF is valid."""
        CPF_LENGTH: int = 11
        if cpf in (number * CPF_LENGTH for number in "1234567890"):
            return False
        reverse_cpf: str = cpf[::-1]
        for idx in range(2, 0, -1):
            enumerated_cpf: enumerate[str] = enumerate(reverse_cpf[idx:], start=2)
            valid_digit: int = (
                sum(map(lambda x: int(x[1]) * x[0], enumerated_cpf)) * 10 % 11
            )
            if reverse_cpf[idx - 1 : idx] != str(valid_digit % 10):
                return False
        return True

    def __repr__(self) -> str:
        return f"<Cpf(number={self.number})>"
