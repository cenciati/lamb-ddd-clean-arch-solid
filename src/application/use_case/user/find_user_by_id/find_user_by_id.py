# pylint: disable=no-name-in-module
from typing import Optional

from pydantic import UUID4

from src.application.use_case.user.find_user_by_id.user_output_dto import UserOutputDTO
from src.domain.repository.user_repository_interface import UserRepositoryInterface


class FindUserByID:
    """Look for a specific user."""

    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, user_id: UUID4) -> Optional[UserOutputDTO]:
        """Triggers the flow to execute the use case."""
        return self.repository.find(user_id)
