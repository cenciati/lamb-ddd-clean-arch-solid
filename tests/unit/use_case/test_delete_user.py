# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa
from pydantic import UUID4

from src.application.use_case.user.delete_user import DeleteUser
from src.infrastructure.repository.memory.user_memory_repository import (
    UserInMemoryRepository,
)


def test_delete_user_use_case_using_in_memory_repository(
    repository_with_user_in_memory: UserInMemoryRepository,
) -> None:
    # Arrange
    use_case = DeleteUser(repository_with_user_in_memory)
    user_id: UUID4 = list(repository_with_user_in_memory.database.keys())[0]

    # Act
    use_case.execute(user_id)
    database_length: int = len(repository_with_user_in_memory.database)

    # Assert
    assert database_length == 0
