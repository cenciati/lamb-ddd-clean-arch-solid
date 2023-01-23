# pylint: disable=no-name-in-module,redefined-builtin
from typing import Optional

from src.application.use_case.customer.find.find_customer_dto import (
    InputFindCustomerDTO,
    OutputFindCustomerDTO,
)
from src.domain.repository.customer_repository_interface import (
    CustomerRepositoryInterface,
)


class FindCustomerByIDUseCase:
    """Look for a specific customer."""

    def __init__(self, repository: CustomerRepositoryInterface):
        self.repository = repository

    def execute(self, input: InputFindCustomerDTO) -> Optional[OutputFindCustomerDTO]:
        """Triggers the flow to execute the use case."""
        return self.repository.find(input)
