# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa


from typing import Sequence

from src.application.use_case.user.dto.user_output_dto import UserOutputDTO
from src.application.use_case.user.find_all_users import FindAllUsers
from src.infrastructure.repository.memory.user_memory_repository import (
    UserInMemoryRepository,
)


def test_find_all_users_use_case_using_in_memory_repository(
    repository_with_users_in_memory: UserInMemoryRepository,
) -> None:
    # Arrange
    use_case = FindAllUsers(repository_with_users_in_memory)

    # Act
    all_users_found: Sequence[UserOutputDTO] = use_case.execute()
    users_amount_length: int = len(all_users_found)

    # Assert
    assert users_amount_length == 3

    assert all_users_found[0].email == "larrygaham@mail.com"
    assert all_users_found[0].password == "Dunno3222"
    assert all_users_found[0].instance_slug.name == "lamb-1"

    assert all_users_found[1].email == "vanessamiwb@mail.com"
    assert all_users_found[1].password == "wEIrDpass003woRd"
    assert all_users_found[1].instance_slug.name == "lamb-2"

    assert all_users_found[2].email == "michaelrmanson@mail.com"
    assert all_users_found[2].password == "allRIGHT2000Pass"
    assert all_users_found[2].instance_slug.name == "lamb-3"
