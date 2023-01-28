# pylint: disable=no-name-in-module,duplicate-code
from typing import Optional, Sequence

from pydantic import UUID4

from src.application.use_case.customer.add.add_customer_dto import (
    InputAddCustomerDTO,
    OutputAddCustomerDTO,
)
from src.application.use_case.customer.find.find_customer_dto import (
    InputFindCustomerByCpfDTO,
    InputFindCustomerByEmailDTO,
    InputFindCustomerByIDDTO,
    OutputFindCustomerDTO,
)
from src.application.use_case.user.delete.delete_user_dto import InputDeleteUserDTO
from src.domain.entity.customer import Customer
from src.domain.error.customer_exception import (
    CustomerDuplicateEmailError,
    CustomerNotFoundError,
    CustomersNotFoundError,
)
from src.domain.repository.customer_repository_interface import (
    CustomerRepositoryInterface,
)
from src.domain.value.cpf import Cpf


class CustomerInMemoryRepository(CustomerRepositoryInterface):
    """In memory customer repository."""

    def __init__(self) -> None:
        self.database = {}

    def add(self, entity: InputAddCustomerDTO) -> OutputAddCustomerDTO:
        """Add customer into memory."""
        try:
            new_customer = Customer(
                full_name=entity.full_name,
                email=entity.email,
                cpf=Cpf(number=entity.cpf),
            )
            self.database[new_customer.id] = new_customer
            return new_customer
        except Exception as exc:
            raise CustomerDuplicateEmailError from exc

    def find(self, data: InputFindCustomerByIDDTO) -> Optional[OutputFindCustomerDTO]:
        """Find customer by unique identifier."""
        try:
            return self.database.get(UUID4(data.id))
        except Exception as exc:
            raise CustomerNotFoundError from exc

    def find_by_email(
        self, data: InputFindCustomerByEmailDTO
    ) -> Optional[OutputFindCustomerDTO]:
        """Find customer by email."""
        try:
            return [
                user for _, user in self.database.items() if user.email == data.email
            ][0]
        except Exception as exc:
            raise CustomerNotFoundError from exc

    def find_by_cpf(
        self, data: InputFindCustomerByCpfDTO
    ) -> Optional[OutputFindCustomerDTO]:
        """Find customer by cpf."""
        try:
            return [
                user for _, user in self.database.items() if user.cpf.number == data.cpf
            ][0]
        except Exception as exc:
            raise CustomerNotFoundError from exc

    def find_all(self) -> Optional[Sequence[OutputFindCustomerDTO]]:
        """Find all customers from memory."""
        data: Sequence[OutputFindCustomerDTO] | None = list(self.database.values())
        if not data:
            raise CustomersNotFoundError
        return data

    def delete(self, data: InputDeleteUserDTO) -> None:
        """Delete customer by unique identifier."""
        try:
            self.database.pop(UUID4(data.id))
        except Exception as exc:
            raise CustomerNotFoundError from exc
