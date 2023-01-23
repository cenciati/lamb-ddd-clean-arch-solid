# pylint: disable=no-name-in-module,redefined-builtin
from typing import Optional

from src.application.use_case.customer.find.find_customer_dto import (
    InputFindCustomerDTO,
    OutputFindCustomerDTO,
)
from src.domain.repository.customer_repository_interface import (
    CustomerRepositoryInterface,
)


class FindCustomerByEmailUseCase:
    """Look for a specific customer by email."""

    def __init__(self, repository: CustomerRepositoryInterface):
        self.repository = repository

    def execute(self, input: InputFindCustomerDTO) -> Optional[OutputFindCustomerDTO]:
        """Triggers the flow to execute the use case."""
        return self.repository.find_by_email(input)
