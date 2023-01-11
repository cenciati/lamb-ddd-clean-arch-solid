# pylint: disable=no-name-in-module, invalid-name, redefined-builtin
from abc import ABC, abstractmethod
from typing import Any, Sequence

from pydantic import EmailStr

from src.domain.repository.repository_interface import RepositoryInterface


class UserRepositoryInterface(RepositoryInterface, ABC):
    """Interface for managing user aggregates."""

    @abstractmethod
    def find_by_email(self, email: EmailStr) -> Sequence[Any]:
        """Find user by email."""
        raise NotImplementedError
