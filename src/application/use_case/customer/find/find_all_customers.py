# pylint: disable=no-name-in-module
from typing import Optional, Sequence

from src.application.use_case.customer.find.find_customer_dto import (
    OutputFindCustomerDTO,
)
from src.domain.repository.customer_repository_interface import (
    CustomerRepositoryInterface,
)


class FindAllCustomersUseCase:
    """Find all customers."""

    def __init__(self, repository: CustomerRepositoryInterface):
        self.repository = repository

    def execute(self) -> Optional[Sequence[OutputFindCustomerDTO]]:
        """Triggers the flow to execute the use case."""
        return self.repository.find_all()
