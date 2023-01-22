# pylint: disable=no-name-in-module,redefined-builtin
from typing import Optional

from src.application.use_case.user.find.find_user_dto import (
    InputFindUserDTO,
    OutputFindUserDTO,
)
from src.domain.repository.user_repository_interface import UserRepositoryInterface


class FindUserByIDUseCase:
    """Look for a specific user."""

    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, input: InputFindUserDTO) -> Optional[OutputFindUserDTO]:
        """Triggers the flow to execute the use case."""
        return self.repository.find(input)
