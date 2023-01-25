# pylint: disable=no-name-in-module
from typing import Optional

from src.application.use_case.customer.find.find_customer_dto import (
    InputFindCustomerByCpfDTO,
    OutputFindCustomerDTO,
)
from src.domain.repository.customer_repository_interface import (
    CustomerRepositoryInterface,
)


class FindCustomerByCpfUseCase:
    """Look for a specific customer by cpf."""

    def __init__(self, repository: CustomerRepositoryInterface):
        self.repository = repository

    def execute(
        self, data: InputFindCustomerByCpfDTO
    ) -> Optional[OutputFindCustomerDTO]:
        """Triggers the flow to execute the use case."""
        return self.repository.find_by_cpf(data)
