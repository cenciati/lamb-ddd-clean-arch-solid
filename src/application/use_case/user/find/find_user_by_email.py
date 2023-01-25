# pylint: disable=no-name-in-module
from typing import Optional

from src.application.use_case.user.find.find_user_dto import (
    InputFindUserByEmailDTO,
    OutputFindUserDTO,
)
from src.domain.repository.user_repository_interface import UserRepositoryInterface


class FindUserByEmailUseCase:
    """Look for a specific user by email."""

    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, data: InputFindUserByEmailDTO) -> Optional[OutputFindUserDTO]:
        """Triggers the flow to execute the use case."""
        return self.repository.find_by_email(data)
