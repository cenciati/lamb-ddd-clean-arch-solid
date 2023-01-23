# pylint: disable=no-name-in-module,redefined-builtin

from src.application.use_case.customer.add.add_customer_dto import InputAddCustomerDTO
from src.domain.repository.customer_repository_interface import (
    CustomerRepositoryInterface,
)


class AddCustomerUseCase:
    """Add a customer user."""

    def __init__(self, repository: CustomerRepositoryInterface):
        self.repository = repository

    def execute(self, input: InputAddCustomerDTO) -> None:
        """Triggers the flow to execute the use case."""
        self.repository.add(input)
