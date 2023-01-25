# pylint: disable=no-name-in-module

from src.application.use_case.customer.add.add_customer_dto import (
    InputAddCustomerDTO,
    OutputAddCustomerDTO,
)
from src.domain.repository.customer_repository_interface import (
    CustomerRepositoryInterface,
)


class AddCustomerUseCase:
    """Add a customer user."""

    def __init__(self, repository: CustomerRepositoryInterface):
        self.repository = repository

    def execute(self, data: InputAddCustomerDTO) -> OutputAddCustomerDTO:
        """Triggers the flow to execute the use case."""
        return self.repository.add(data)
