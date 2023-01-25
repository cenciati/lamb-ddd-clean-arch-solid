# pylint: disable=no-name-in-module

from src.application.use_case.user.add.add_user_dto import (
    InputAddUserDTO,
    OutputAddUserDTO,
)
from src.domain.repository.user_repository_interface import UserRepositoryInterface


class AddUserUseCase:
    """Add a given user."""

    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, data: InputAddUserDTO) -> OutputAddUserDTO:
        """Triggers the flow to execute the use case."""
        return self.repository.add(data)
