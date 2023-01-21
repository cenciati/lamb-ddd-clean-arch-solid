# pylint: disable=no-name-in-module
from typing import Optional

from pydantic import EmailStr

from src.application.use_case.user.dto.user_output_dto import UserOutputDTO
from src.domain.repository.user_repository_interface import UserRepositoryInterface


class FindUserByEmail:
    """Look for a specific user by email."""

    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, user_email: EmailStr) -> Optional[UserOutputDTO]:
        """Triggers the flow to execute the use case."""
        return self.repository.find_by_email(user_email)
