# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa


from typing import Sequence

from pydantic import UUID4

from src.application.use_case.user.add.add_user_dto import InputAddUserDTO
from src.application.use_case.user.delete.delete_user_dto import InputDeleteUserDTO
from src.application.use_case.user.find.find_user_dto import (
    InputFindUserDTO,
    OutputFindUserDTO,
)
from src.application.use_case.user.update.update_user_dto import InputUpdateUserDTO
from src.domain.value.slug import Slug
from src.infrastructure.repository.memory.user_memory_repository import (
    UserInMemoryRepository,
)


def test_add_new_user_in_memory() -> None:
    # Arrange
    new_user = InputAddUserDTO(
        email="johndoe@mail.com",
        password="iloveapples",
        instance_slug=Slug(name="lamb"),
    )

    # Act
    user_repository = UserInMemoryRepository()
    user_repository.add(new_user)
    database: list = list(user_repository.database.values())

    # Assert
    assert len(user_repository.database) == 1
    assert database[0].email == "johndoe@mail.com"
    assert database[0].password == "iloveapples"
    assert database[0].instance_slug.name == "lamb"


def test_find_user_in_memory(
    repository_with_user_in_memory: UserInMemoryRepository,
) -> None:
    # Arrange
    created_user_id: UUID4 = list(repository_with_user_in_memory.database.keys())[0]
    user = InputFindUserDTO(id=created_user_id)

    # Act
    found_user: OutputFindUserDTO = repository_with_user_in_memory.find(user)

    # Assert
    assert len(repository_with_user_in_memory.database) == 1
    assert found_user.email == "johndoe@mail.com"
    assert found_user.password == "iLoveApples2001"
    assert found_user.instance_slug.name == "lamb"


def test_find_user_by_email_in_memory(
    repository_with_user_in_memory: UserInMemoryRepository,
) -> None:
    # Arrange
    user = InputFindUserDTO(email="johndoe@mail.com")

    # Act
    found_user: OutputFindUserDTO = repository_with_user_in_memory.find_by_email(user)

    # Assert
    assert len(repository_with_user_in_memory.database) == 1
    assert found_user.email == "johndoe@mail.com"
    assert found_user.password == "iLoveApples2001"
    assert found_user.instance_slug.name == "lamb"


def test_find_all_users_in_memory(
    repository_with_users_in_memory: UserInMemoryRepository,
) -> None:
    # Act
    all_users: Sequence[OutputFindUserDTO] = repository_with_users_in_memory.find_all()
    users_amount_length: int = len(repository_with_users_in_memory.database)

    # Assert
    assert users_amount_length == 3

    assert all_users[0].email == "larrygaham@mail.com"
    assert all_users[0].password == "Dunno3222"
    assert all_users[0].instance_slug.name == "lamb-1"

    assert all_users[1].email == "vanessamiwb@mail.com"
    assert all_users[1].password == "wEIrDpass003woRd"
    assert all_users[1].instance_slug.name == "lamb-2"

    assert all_users[2].email == "michaelrmanson@mail.com"
    assert all_users[2].password == "allRIGHT2000Pass"
    assert all_users[2].instance_slug.name == "lamb-3"


def test_update_user_email_in_memory(
    repository_with_user_in_memory: UserInMemoryRepository,
) -> None:
    # Arrange
    user_id: UUID4 = list(repository_with_user_in_memory.database.keys())[0]
    updated_user = InputUpdateUserDTO(id=user_id, email="johndoe2@mail.com")

    # Act
    repository_with_user_in_memory.update(updated_user)
    database: list = list(repository_with_user_in_memory.database.values())

    # Assert
    assert len(repository_with_user_in_memory.database) == 1
    assert database[0].email == "johndoe2@mail.com"


def test_update_user_password_in_memory(
    repository_with_user_in_memory: UserInMemoryRepository,
) -> None:
    # Arrange
    user_id: UUID4 = list(repository_with_user_in_memory.database.keys())[0]
    updated_user = InputUpdateUserDTO(id=user_id, password="sausage755")

    # Act
    repository_with_user_in_memory.update(updated_user)
    database: list = list(repository_with_user_in_memory.database.values())

    # Assert
    assert len(repository_with_user_in_memory.database) == 1
    assert database[0].password == "sausage755"


def test_update_user_instance_slug_in_memory(
    repository_with_user_in_memory: UserInMemoryRepository,
) -> None:
    # Arrange
    user_id: UUID4 = list(repository_with_user_in_memory.database.keys())[0]
    updated_user = InputUpdateUserDTO(id=user_id, instance_slug=Slug(name="lamb4"))

    # Act
    repository_with_user_in_memory.update(updated_user)
    database: list = list(repository_with_user_in_memory.database.values())

    # Assert
    assert len(repository_with_user_in_memory.database) == 1
    assert database[0].instance_slug.name == "lamb4"


def test_update_entire_user_info_in_memory(
    repository_with_user_in_memory: UserInMemoryRepository,
) -> None:
    # Arrange
    user_id: UUID4 = list(repository_with_user_in_memory.database.keys())[0]
    updated_user = InputUpdateUserDTO(
        id=user_id,
        email="johndoe2@mail.com",
        password="idontknow2006",
        instance_slug=Slug(name="lamb55"),
    )

    # Act
    repository_with_user_in_memory.update(updated_user)
    database: list = list(repository_with_user_in_memory.database.values())

    # Assert
    assert len(repository_with_user_in_memory.database) == 1
    assert database[0].email == "johndoe2@mail.com"
    assert database[0].password == "idontknow2006"
    assert database[0].instance_slug.name == "lamb55"


def test_delete_user_in_memory(
    repository_with_user_in_memory: UserInMemoryRepository,
) -> None:
    # Act
    user_id: UUID4 = list(repository_with_user_in_memory.database.keys())[0]
    deleted_user = InputDeleteUserDTO(id=user_id)
    repository_with_user_in_memory.delete(deleted_user)

    # Assert
    assert len(repository_with_user_in_memory.database) == 0
