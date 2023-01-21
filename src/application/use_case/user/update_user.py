# pylint: disable=no-name-in-module

from pydantic import UUID4

from src.application.use_case.user.dto.update_user_dto import UpdateUserDTO
from src.domain.repository.user_repository_interface import UserRepositoryInterface


class UpdateUser:
    """Update a given user."""

    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, user_id: UUID4, updated_user: UpdateUserDTO) -> None:
        """Triggers the flow to execute the use case."""
        self.repository.update(user_id, updated_user)
