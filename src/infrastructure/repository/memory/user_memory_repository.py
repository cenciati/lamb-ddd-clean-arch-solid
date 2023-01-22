# pylint: disable=no-name-in-module,redefined-builtin, duplicate-code
from typing import Optional, Sequence

from src.application.use_case.user.add.add_user_dto import InputAddUserDTO
from src.application.use_case.user.delete.delete_user_dto import InputDeleteUserDTO
from src.application.use_case.user.find.find_user_dto import (
    InputFindUserDTO,
    OutputFindUserDTO,
)
from src.application.use_case.user.update.update_user_dto import InputUpdateUserDTO
from src.domain.entity.user import User
from src.domain.repository.user_repository_interface import UserRepositoryInterface


class UserInMemoryRepository(UserRepositoryInterface):
    """In memory user repository."""

    def __init__(self) -> None:
        self.database = {}

    def add(self, entity: InputAddUserDTO) -> None:
        """Add user into memory."""
        try:
            new_user = User(
                email=entity.email,
                password=entity.password,
                instance_slug=entity.instance_slug,
            )
            self.database[new_user.id] = new_user
        except Exception as exc:
            raise Exception from exc

    def find(self, input: InputFindUserDTO) -> Optional[OutputFindUserDTO]:
        """Find user by unique identifier."""
        try:
            return self.database.get(input.id)
        except Exception as exc:
            raise Exception from exc

    def find_by_email(self, input: InputFindUserDTO) -> Optional[OutputFindUserDTO]:
        """Find user by email."""
        try:
            return [
                user for _, user in self.database.items() if user.email == input.email
            ][0]
        except Exception as exc:
            raise Exception from exc

    def find_all(self) -> Optional[Sequence[OutputFindUserDTO]]:
        """Find all users from memory."""
        try:
            return list(self.database.values())
        except Exception as exc:
            raise Exception from exc

    def update(self, input: InputUpdateUserDTO) -> None:
        """Update user information by unique identifier."""
        try:
            self.database.get(input.id).update(
                input.email,
                input.password,
                input.instance_slug,
            )
        except Exception as exc:
            raise Exception from exc

    def delete(self, input: InputDeleteUserDTO) -> None:
        """Delete user by unique identifier."""
        try:
            self.database.pop(input.id)
        except Exception as exc:
            raise Exception from exc
