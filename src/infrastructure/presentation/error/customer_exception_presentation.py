# pylint: disable=missing-class-docstring
from pydantic import BaseModel, Field

from src.domain.error.customer_exception import (
    CustomerDuplicateCpfError,
    CustomerDuplicateEmailError,
    CustomerNotFoundError,
    CustomersNotFoundError,
)


class ErrorMessageCustomerNotFound(BaseModel):
    detail: str = Field(example=CustomerNotFoundError.message)


class ErrorMessageCustomersNotFound(BaseModel):
    detail: str = Field(example=CustomersNotFoundError.message)


class ErrorMessageCustomerDuplicateEmail(BaseModel):
    detail: str = Field(example=CustomerDuplicateEmailError.message)


class ErrorMessageCustomerDuplicateCpf(Exception):
    detail: str = Field(example=CustomerDuplicateCpfError.message)
