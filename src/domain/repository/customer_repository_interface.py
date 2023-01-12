# pylint: disable=no-name-in-module, invalid-name, redefined-builtin
from abc import ABC, abstractmethod
from typing import Any, Optional, Sequence

from pydantic import EmailStr

from src.domain.repository.repository_interface import RepositoryInterface
from src.domain.value_object.cpf import Cpf


class CustomerRepositoryInterface(RepositoryInterface, ABC):
    """Interface for managing customer aggregates."""

    @abstractmethod
    def find_by_email(self, email: EmailStr) -> Optional[Sequence[Any]]:
        """Find customer by email."""
        raise NotImplementedError

    @abstractmethod
    def find_by_cpf(self, cpf: Cpf) -> Optional[Sequence[Any]]:
        """Find customer by cpf."""
        raise NotImplementedError
