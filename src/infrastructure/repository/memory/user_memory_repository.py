# pylint: disable=no-name-in-module,duplicate-code
from typing import Optional, Sequence

from pydantic import UUID4

from src.application.use_case.user.add.add_user_dto import (
    InputAddUserDTO,
    OutputAddUserDTO,
)
from src.application.use_case.user.delete.delete_user_dto import InputDeleteUserDTO
from src.application.use_case.user.find.find_user_dto import (
    InputFindUserByEmailDTO,
    InputFindUserByIDDTO,
    OutputFindUserDTO,
)
from src.application.use_case.user.update.update_user_dto import InputUpdateUserDTO
from src.domain.entity.user import User
from src.domain.repository.user_repository_interface import UserRepositoryInterface
from src.domain.value.slug import Slug


class UserInMemoryRepository(UserRepositoryInterface):
    """In memory user repository."""

    def __init__(self) -> None:
        self.database = {}

    def add(self, entity: InputAddUserDTO) -> OutputAddUserDTO:
        """Add user into memory."""
        try:
            new_user = User(
                email=entity.email,
                password=entity.password,
                instance_slug=Slug(name=entity.instance_slug),
            )
            self.database[new_user.id] = new_user
            return new_user
        except Exception as exc:
            raise Exception from exc

    def find(self, data: InputFindUserByIDDTO) -> Optional[OutputFindUserDTO]:
        """Find user by unique identifier."""
        try:
            return self.database.get(UUID4(data.id))
        except Exception as exc:
            raise Exception from exc

    def find_by_email(
        self, data: InputFindUserByEmailDTO
    ) -> Optional[OutputFindUserDTO]:
        """Find user by email."""
        try:
            return [
                user for _, user in self.database.items() if user.email == data.email
            ][0]
        except Exception as exc:
            raise Exception from exc

    def find_all(self) -> Optional[Sequence[OutputFindUserDTO]]:
        """Find all users from memory."""
        try:
            return list(self.database.values())
        except Exception as exc:
            raise Exception from exc

    def update(self, data: InputUpdateUserDTO) -> None:
        """Update user information by unique identifier."""
        try:
            self.database.get(UUID4(data.id)).update(
                data.email, data.password, data.instance_slug
            )
        except Exception as exc:
            raise Exception from exc

    def delete(self, data: InputDeleteUserDTO) -> None:
        """Delete user by unique identifier."""
        try:
            self.database.pop(UUID4(data.id))
        except Exception as exc:
            raise Exception from exc
