# pylint: disable=no-name-in-module,invalid-name
from abc import ABC, abstractmethod
from typing import Optional

from src.application.use_case.user.find.find_user_dto import (
    InputFindUserByEmailDTO,
    OutputFindUserDTO,
)
from src.application.use_case.user.update.update_user_dto import InputUpdateUserDTO
from src.domain.repository.repository_interface import RepositoryInterface


class UserRepositoryInterface(RepositoryInterface, ABC):
    """Interface for managing user aggregates."""

    @abstractmethod
    def find_by_email(
        self, data: InputFindUserByEmailDTO
    ) -> Optional[OutputFindUserDTO]:
        """Find user by email."""
        raise NotImplementedError

    @abstractmethod
    def update(self, data: InputUpdateUserDTO) -> None:
        """Update user by ID."""
        raise NotImplementedError
