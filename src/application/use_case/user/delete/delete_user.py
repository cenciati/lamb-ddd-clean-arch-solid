# pylint: disable=no-name-in-module,redefined-builtin

from src.application.use_case.user.delete.delete_user_dto import InputDeleteUserDTO
from src.domain.repository.user_repository_interface import UserRepositoryInterface


class DeleteUserUseCase:
    """Delete an user by id."""

    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, input: InputDeleteUserDTO) -> None:
        """Triggers the flow to execute the use case."""
        self.repository.delete(input)
