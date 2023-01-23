# pylint: disable=no-name-in-module,redefined-builtin

from src.application.use_case.customer.delete.delete_customer_dto import (
    InputDeleteCustomerDTO,
)
from src.domain.repository.customer_repository_interface import (
    CustomerRepositoryInterface,
)


class DeleteCustomerUseCase:
    """Delete a customer by id."""

    def __init__(self, repository: CustomerRepositoryInterface):
        self.repository = repository

    def execute(self, input: InputDeleteCustomerDTO) -> None:
        """Triggers the flow to execute the use case."""
        self.repository.delete(input)
