# pylint: disable=no-name-in-module,redefined-builtin

from src.application.use_case.user.update.update_user_dto import InputUpdateUserDTO
from src.domain.repository.user_repository_interface import UserRepositoryInterface


class UpdateUserUseCase:
    """Update a given user."""

    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, input: InputUpdateUserDTO) -> None:
        """Triggers the flow to execute the use case."""
        self.repository.update(input)
