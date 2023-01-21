# pylint: disable=no-name-in-module

from src.application.use_case.user.dto.add_user_dto import AddUserDTO
from src.domain.repository.user_repository_interface import UserRepositoryInterface


class AddUser:
    """Add a given user."""

    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, new_user: AddUserDTO) -> None:
        """Triggers the flow to execute the use case."""
        self.repository.add(new_user)
