# pylint: disable=no-name-in-module
from typing import Optional

from src.application.use_case.customer.find.find_customer_dto import (
    InputFindCustomerByEmailDTO,
    OutputFindCustomerDTO,
)
from src.domain.repository.customer_repository_interface import (
    CustomerRepositoryInterface,
)


class FindCustomerByEmailUseCase:
    """Look for a specific customer by email."""

    def __init__(self, repository: CustomerRepositoryInterface):
        self.repository = repository

    def execute(
        self, data: InputFindCustomerByEmailDTO
    ) -> Optional[OutputFindCustomerDTO]:
        """Triggers the flow to execute the use case."""
        return self.repository.find_by_email(data)
