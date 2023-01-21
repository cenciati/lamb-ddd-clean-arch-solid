# pylint: disable=no-name-in-module, invalid-name, redefined-builtin
from abc import ABC, abstractmethod
from typing import Any, Optional

from pydantic import UUID4, EmailStr

from src.application.use_case.user.dto.update_user_dto import UpdateUserDTO
from src.domain.repository.repository_interface import RepositoryInterface


class UserRepositoryInterface(RepositoryInterface, ABC):
    """Interface for managing user aggregates."""

    @abstractmethod
    def find_by_email(self, email: EmailStr) -> Optional[Any]:
        """Find user by email."""
        raise NotImplementedError

    @abstractmethod
    def update(self, id: UUID4, updated_user: UpdateUserDTO) -> None:
        """Update user by ID."""
        raise NotImplementedError
