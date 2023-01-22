# pylint: disable=no-name-in-module, invalid-name, redefined-builtin
from abc import ABC, abstractmethod
from typing import Optional

from src.application.use_case.user.find.find_user_dto import (
    InputFindUserDTO,
    OutputFindUserDTO,
)
from src.application.use_case.user.update.update_user_dto import InputUpdateUserDTO
from src.domain.repository.repository_interface import RepositoryInterface


class UserRepositoryInterface(RepositoryInterface, ABC):
    """Interface for managing user aggregates."""

    @abstractmethod
    def find_by_email(self, input: InputFindUserDTO) -> Optional[OutputFindUserDTO]:
        """Find user by email."""
        raise NotImplementedError

    @abstractmethod
    def update(self, input: InputUpdateUserDTO) -> None:
        """Update user by ID."""
        raise NotImplementedError
