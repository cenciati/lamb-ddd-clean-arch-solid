# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa


from typing import Sequence

from pydantic import UUID4

from src.application.use_case.user.dto.add_user_dto import AddUserDTO
from src.application.use_case.user.dto.update_user_dto import UpdateUserDTO
from src.application.use_case.user.dto.user_output_dto import UserOutputDTO
from src.domain.value.slug import Slug
from src.infrastructure.repository.memory.user_memory_repository import (
    UserInMemoryRepository,
)


def test_add_new_user_in_memory() -> None:
    # Arrange
    new_user = AddUserDTO(
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

    # Act
    found_user: UserOutputDTO = repository_with_user_in_memory.find(created_user_id)

    # Assert
    assert len(repository_with_user_in_memory.database) == 1
    assert found_user.email == "johndoe@mail.com"
    assert found_user.password == "iLoveApples2001"
    assert found_user.instance_slug.name == "lamb"


def test_find_user_by_email_in_memory(
    repository_with_user_in_memory: UserInMemoryRepository,
) -> None:
    # Act
    found_user: UserOutputDTO = repository_with_user_in_memory.find_by_email(
        "johndoe@mail.com"
    )

    # Assert
    assert len(repository_with_user_in_memory.database) == 1
    assert found_user.email == "johndoe@mail.com"
    assert found_user.password == "iLoveApples2001"
    assert found_user.instance_slug.name == "lamb"


def test_find_all_users_in_memory() -> None:
    # Arrange
    new_user_1 = AddUserDTO(
        email="johndoe@mail.com",
        password="iloveapples",
        instance_slug=Slug(name="lamb1"),
    )
    new_user_2 = AddUserDTO(
        email="claireb@mail.com",
        password="films2008",
        instance_slug=Slug(name="lamb2"),
    )
    new_user_3 = AddUserDTO(
        email="mikeadams@mail.com",
        password="keyboardiscool99999999",
        instance_slug=Slug(name="lamb3"),
    )
    user_repository = UserInMemoryRepository()
    user_repository.add(new_user_1)
    user_repository.add(new_user_2)
    user_repository.add(new_user_3)

    # Act
    all_users: Sequence[UserOutputDTO] = user_repository.find_all()
    users_amount_length: int = len(user_repository.database)

    # Assert
    assert users_amount_length == 3
    assert all_users[0].email == "johndoe@mail.com"
    assert all_users[0].password == "iloveapples"
    assert all_users[0].instance_slug.name == "lamb1"

    assert all_users[1].email == "claireb@mail.com"
    assert all_users[1].password == "films2008"
    assert all_users[1].instance_slug.name == "lamb2"

    assert all_users[2].email == "mikeadams@mail.com"
    assert all_users[2].password == "keyboardiscool99999999"
    assert all_users[2].instance_slug.name == "lamb3"


def test_update_user_email_in_memory(
    repository_with_user_in_memory: UserInMemoryRepository,
) -> None:
    # Arrange
    user_id: UUID4 = list(repository_with_user_in_memory.database.keys())[0]
    updated_user = UpdateUserDTO(email="johndoe2@mail.com")

    # Act
    repository_with_user_in_memory.update(user_id, updated_user)
    database: list = list(repository_with_user_in_memory.database.values())

    # Assert
    assert len(repository_with_user_in_memory.database) == 1
    assert database[0].email == "johndoe2@mail.com"


def test_update_user_password_in_memory(
    repository_with_user_in_memory: UserInMemoryRepository,
) -> None:
    # Arrange
    user_id: UUID4 = list(repository_with_user_in_memory.database.keys())[0]
    updated_user = UpdateUserDTO(password="sausage755")

    # Act
    repository_with_user_in_memory.update(user_id, updated_user)
    database: list = list(repository_with_user_in_memory.database.values())

    # Assert
    assert len(repository_with_user_in_memory.database) == 1
    assert database[0].password == "sausage755"


def test_update_user_instance_slug_in_memory(
    repository_with_user_in_memory: UserInMemoryRepository,
) -> None:
    # Arrange
    user_id: UUID4 = list(repository_with_user_in_memory.database.keys())[0]
    updated_user = UpdateUserDTO(instance_slug=Slug(name="lamb4"))

    # Act
    repository_with_user_in_memory.update(user_id, updated_user)
    database: list = list(repository_with_user_in_memory.database.values())

    # Assert
    assert len(repository_with_user_in_memory.database) == 1
    assert database[0].instance_slug.name == "lamb4"


def test_update_entire_user_info_in_memory(
    repository_with_user_in_memory: UserInMemoryRepository,
) -> None:
    # Arrange
    user_id: UUID4 = list(repository_with_user_in_memory.database.keys())[0]
    updated_user = UpdateUserDTO(
        email="johndoe2@mail.com",
        password="idontknow2006",
        instance_slug=Slug(name="lamb55"),
    )

    # Act
    repository_with_user_in_memory.update(user_id, updated_user)
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
    repository_with_user_in_memory.delete(user_id)

    # Assert
    assert len(repository_with_user_in_memory.database) == 0
