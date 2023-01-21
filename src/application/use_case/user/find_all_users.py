# pylint: disable=no-name-in-module
from typing import Optional, Sequence

from src.application.use_case.user.dto.user_output_dto import UserOutputDTO
from src.domain.repository.user_repository_interface import UserRepositoryInterface


class FindAllUsers:
    """Find all users."""

    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self) -> Optional[Sequence[UserOutputDTO]]:
        """Triggers the flow to execute the use case."""
        return self.repository.find_all()
