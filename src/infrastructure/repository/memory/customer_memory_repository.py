# pylint: disable=no-name-in-module,redefined-builtin, duplicate-code
from typing import Optional, Sequence

from src.application.use_case.customer.add.add_customer_dto import InputAddCustomerDTO
from src.application.use_case.customer.find.find_customer_dto import (
    InputFindCustomerDTO,
    OutputFindCustomerDTO,
)
from src.application.use_case.user.delete.delete_user_dto import InputDeleteUserDTO
from src.domain.entity.customer import Customer
from src.domain.repository.customer_repository_interface import (
    CustomerRepositoryInterface,
)


class CustomerInMemoryRepository(CustomerRepositoryInterface):
    """In memory customer repository."""

    def __init__(self) -> None:
        self.database = {}

    def add(self, entity: InputAddCustomerDTO) -> None:
        """Add customer into memory."""
        try:
            new_customer = Customer(
                full_name=entity.full_name,
                email=entity.email,
                cpf=entity.cpf,
            )
            self.database[new_customer.id] = new_customer
        except Exception as exc:
            raise Exception from exc

    def find(self, input: InputFindCustomerDTO) -> Optional[OutputFindCustomerDTO]:
        """Find customer by unique identifier."""
        try:
            return self.database.get(input.id)
        except Exception as exc:
            raise Exception from exc

    def find_by_email(
        self, input: InputFindCustomerDTO
    ) -> Optional[OutputFindCustomerDTO]:
        """Find customer by email."""
        try:
            return [
                user for _, user in self.database.items() if user.email == input.email
            ][0]
        except Exception as exc:
            raise Exception from exc

    def find_by_cpf(
        self, input: InputFindCustomerDTO
    ) -> Optional[OutputFindCustomerDTO]:
        """Find customer by cpf."""
        try:
            return [user for _, user in self.database.items() if user.cpf == input.cpf][
                0
            ]
        except Exception as exc:
            raise Exception from exc

    def find_all(self) -> Optional[Sequence[OutputFindCustomerDTO]]:
        """Find all customers from memory."""
        try:
            return list(self.database.values())
        except Exception as exc:
            raise Exception from exc

    def delete(self, input: InputDeleteUserDTO) -> None:
        """Delete customer by unique identifier."""
        try:
            self.database.pop(input.id)
        except Exception as exc:
            raise Exception from exc
