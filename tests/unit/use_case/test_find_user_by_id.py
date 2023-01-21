# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa


from pydantic import UUID4

from src.application.use_case.user.dto.user_output_dto import UserOutputDTO
from src.application.use_case.user.find_user_by_id import FindUserByID
from src.infrastructure.repository.memory.user_memory_repository import (
    UserInMemoryRepository,
)


def test_find_user_by_id_use_case_using_in_memory_repository(
    repository_with_user_in_memory: UserInMemoryRepository,
) -> None:
    # Arrange
    use_case = FindUserByID(repository_with_user_in_memory)
    user_id: UUID4 = list(repository_with_user_in_memory.database.keys())[0]

    # Act
    found_user: UserOutputDTO = use_case.execute(user_id)

    # Assert
    assert found_user.email == "johndoe@mail.com"
    assert found_user.password == "iLoveApples2001"
    assert found_user.instance_slug.name == "lamb"
