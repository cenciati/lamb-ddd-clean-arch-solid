# pylint: disable=no-name-in-module,invalid-name
from abc import ABC, abstractmethod
from typing import Optional

from src.application.use_case.customer.find.find_customer_dto import (
    InputFindCustomerByEmailDTO,
    OutputFindCustomerDTO,
)
from src.domain.repository.repository_interface import RepositoryInterface


class CustomerRepositoryInterface(RepositoryInterface, ABC):
    """Interface for managing customer aggregates."""

    @abstractmethod
    def find_by_email(
        self, data: InputFindCustomerByEmailDTO
    ) -> Optional[OutputFindCustomerDTO]:
        """Find customer by email."""
        raise NotImplementedError

    @abstractmethod
    def find_by_cpf(
        self, data: InputFindCustomerByEmailDTO
    ) -> Optional[OutputFindCustomerDTO]:
        """Find customer by cpf."""
        raise NotImplementedError
