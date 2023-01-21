# pylint: disable=no-name-in-module

from pydantic import UUID4

from src.domain.repository.user_repository_interface import UserRepositoryInterface


class DeleteUser:
    """Delete an user by id."""

    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, user_id: UUID4) -> None:
        """Triggers the flow to execute the use case."""
        self.repository.delete(user_id)
