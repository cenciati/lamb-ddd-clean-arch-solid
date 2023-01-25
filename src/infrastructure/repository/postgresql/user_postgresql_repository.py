# pylint: disable=no-name-in-module,duplicate-code
from typing import Optional, Sequence

from src.application.interface.db_connection_handler_interface import (
    DBConnectionHandlerInterface,
)
from src.application.use_case.user.add.add_user_dto import InputAddUserDTO
from src.application.use_case.user.delete.delete_user_dto import InputDeleteUserDTO
from src.application.use_case.user.find.find_user_dto import (
    InputFindUserByEmailDTO,
    InputFindUserByIDDTO,
    OutputFindUserDTO,
)
from src.application.use_case.user.update.update_user_dto import InputUpdateUserDTO
from src.domain.entity.user import User
from src.domain.repository.user_repository_interface import UserRepositoryInterface
from src.infrastructure.database.sqlalchemy.model.user_model import UserModel


class UserPostgreSQLRepository(UserRepositoryInterface):
    """In memory user repository."""

    def __init__(self, db_handler: DBConnectionHandlerInterface):
        self.db_handler = db_handler

    def add(self, entity: InputAddUserDTO) -> None:
        """Insert data into the database.
        Args:
            entity (InputAddUserDTO): Target user to be
                added into the database.
        """
        with self.db_handler as db_connection:
            try:
                new_user = User(
                    email=entity.email,
                    password=entity.password,
                    instance_slug=entity.instance_slug,
                )
                new_user_db_format = UserModel(new_user.dict())
                db_connection.session.add(new_user_db_format)
                db_connection.session.commit()
            except Exception as exc:
                db_connection.session.rollback()
                raise Exception from exc
            finally:
                db_connection.session.close()

    def find(self, data: InputFindUserByIDDTO) -> Optional[OutputFindUserDTO]:
        """Find user by ID.
        Args:
            data (InputFindUserByIDDTO): Object containing user ID.
        Returns:
            Object containing found user information if it exists.
        """
        with self.db_handler as db_connection:
            try:
                found_user = (
                    db_connection.session.query(UserModel).filter_by(id=data.id).one()
                )
                return OutputFindUserDTO(
                    id=found_user.id,
                    email=found_user.email,
                    password=found_user.password,
                    instance_slug=found_user.instance_slug,
                    created_at=found_user.created_at,
                    updated_at=found_user.updated_at,
                )
            except Exception as exc:
                db_connection.session.rollback()
                raise Exception from exc
            finally:
                db_connection.session.close()

    def find_by_email(
        self, data: InputFindUserByEmailDTO
    ) -> Optional[OutputFindUserDTO]:
        """Find user by email.
        Args:
            data (InputFindUserByEmailDTO): Object containing user email.
        Returns:
            Object containing found user information if it exists.
        """
        with self.db_handler as db_connection:
            try:
                found_user = (
                    db_connection.session.query(UserModel)
                    .filter_by(id=data.email)
                    .one()
                )
                return OutputFindUserDTO(
                    id=found_user.id,
                    email=found_user.email,
                    password=found_user.password,
                    instance_slug=found_user.instance_slug,
                    created_at=found_user.created_at,
                    updated_at=found_user.updated_at,
                )
            except Exception as exc:
                db_connection.session.rollback()
                raise Exception from exc
            finally:
                db_connection.session.close()

    def find_all(self) -> Optional[Sequence[OutputFindUserDTO]]:
        """Find all added users.
        Returns:
            List of objects containing registred users information if they exist.
        """
        with self.db_handler as db_connection:
            try:
                found_users = db_connection.session.query(UserModel).all()
                return [
                    OutputFindUserDTO(
                        id=user.id,
                        email=user.email,
                        password=user.password,
                        instance_slug=user.instance_slug,
                        created_at=user.created_at,
                        updated_at=user.updated_at,
                    )
                    for user in found_users
                ]
            except Exception as exc:
                db_connection.session.rollback()
                raise Exception from exc
            finally:
                db_connection.session.close()

    def update(self, data: InputUpdateUserDTO) -> None:
        """Update user information by ID.
        Args:
            data (InputUpdateUserDTO): Object containing user ID and
                the information(s) to be updated.
        """
        with self.db_handler as db_connection:
            try:
                db_connection.session.query(UserModel).filter_by(id=data.id).update(
                    data.dict()
                )
            except Exception as exc:
                db_connection.session.rollback()
                raise Exception from exc
            finally:
                db_connection.session.close()

    def delete(self, data: InputDeleteUserDTO) -> None:
        """Delete user by ID.
        Args:
            data (InputDeleteUserDTO): Object containing user ID.
        """
        with self.db_handler as db_connection:
            try:
                db_connection.session.query(UserModel).filter_by(id=data.id).delete()
            except Exception as exc:
                db_connection.session.rollback()
                raise Exception from exc
            finally:
                db_connection.session.close()
