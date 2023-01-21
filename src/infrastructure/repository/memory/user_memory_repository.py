# pylint: disable=no-name-in-module,redefined-builtin
from typing import Optional, Sequence

from pydantic import UUID4, EmailStr

from src.application.use_case.user.dto.add_user_dto import AddUserDTO
from src.application.use_case.user.dto.update_user_dto import UpdateUserDTO
from src.application.use_case.user.dto.user_output_dto import UserOutputDTO
from src.domain.entity.user import User
from src.domain.repository.user_repository_interface import UserRepositoryInterface


class UserInMemoryRepository(UserRepositoryInterface):
    """In memory user repository."""

    def __init__(self) -> None:
        self.database = {}

    def add(self, entity: AddUserDTO) -> None:
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

    def find(self, id: UUID4) -> Optional[UserOutputDTO]:
        """Find user by unique identifier."""
        try:
            return self.database.get(id)
        except Exception as exc:
            raise Exception from exc

    def find_by_email(self, email: EmailStr) -> Optional[UserOutputDTO]:
        """Find user by email."""
        try:
            return [user for _, user in self.database.items() if user.email == email][0]
        except Exception as exc:
            raise Exception from exc

    def find_all(self) -> Optional[Sequence[UserOutputDTO]]:
        """Find all users from memory."""
        try:
            return list(self.database.values())
        except Exception as exc:
            raise Exception from exc

    def update(self, id: UUID4, updated_entity: UpdateUserDTO) -> None:
        """Update user information by unique identifier."""
        try:
            self.database.get(id).update(
                updated_entity.email,
                updated_entity.password,
                updated_entity.instance_slug,
            )
        except Exception as exc:
            raise Exception from exc

    def delete(self, id: UUID4) -> None:
        """Delete user by unique identifier."""
        try:
            self.database.pop(id)
        except Exception as exc:
            raise Exception from exc
