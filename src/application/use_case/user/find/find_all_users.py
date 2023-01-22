# pylint: disable=no-name-in-module
from typing import Optional, Sequence

from src.application.use_case.user.find.find_user_dto import OutputFindUserDTO
from src.domain.repository.user_repository_interface import UserRepositoryInterface


class FindAllUsersUseCase:
    """Find all users."""

    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self) -> Optional[Sequence[OutputFindUserDTO]]:
        """Triggers the flow to execute the use case."""
        return self.repository.find_all()
