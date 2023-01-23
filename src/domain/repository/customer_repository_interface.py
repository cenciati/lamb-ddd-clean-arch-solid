# pylint: disable=no-name-in-module, invalid-name, redefined-builtin
from abc import ABC, abstractmethod
from typing import Optional

from src.application.use_case.customer.find.find_customer_dto import (
    InputFindCustomerDTO,
    OutputFindCustomerDTO,
)
from src.domain.repository.repository_interface import RepositoryInterface


class CustomerRepositoryInterface(RepositoryInterface, ABC):
    """Interface for managing customer aggregates."""

    @abstractmethod
    def find_by_email(
        self, input: InputFindCustomerDTO
    ) -> Optional[OutputFindCustomerDTO]:
        """Find customer by email."""
        raise NotImplementedError

    @abstractmethod
    def find_by_cpf(
        self, input: InputFindCustomerDTO
    ) -> Optional[OutputFindCustomerDTO]:
        """Find customer by cpf."""
        raise NotImplementedError
