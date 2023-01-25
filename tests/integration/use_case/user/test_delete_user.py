# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa

from src.application.use_case.user.delete.delete_user import DeleteUserUseCase
from src.application.use_case.user.delete.delete_user_dto import InputDeleteUserDTO
from src.infrastructure.repository.memory.user_memory_repository import (
    UserInMemoryRepository,
)


def test_delete_user_use_case_using_in_memory_repository(
    repository_with_user_in_memory: UserInMemoryRepository,
) -> None:
    # Arrange
    use_case = DeleteUserUseCase(repository_with_user_in_memory)
    user_id: str = str(list(repository_with_user_in_memory.database.keys())[0])
    deleted_user = InputDeleteUserDTO(id=user_id)

    # Act
    use_case.execute(deleted_user)
    database_length: int = len(repository_with_user_in_memory.database)

    # Assert
    assert database_length == 0
