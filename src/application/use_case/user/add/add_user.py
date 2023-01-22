# pylint: disable=no-name-in-module,redefined-builtin

from src.application.use_case.user.add.add_user_dto import InputAddUserDTO
from src.domain.repository.user_repository_interface import UserRepositoryInterface


class AddUserUseCase:
    """Add a given user."""

    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, input: InputAddUserDTO) -> None:
        """Triggers the flow to execute the use case."""
        self.repository.add(input)
