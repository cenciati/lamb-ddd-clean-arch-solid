# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa


from src.application.use_case.user.find.find_user_by_id import FindUserByIDUseCase
from src.application.use_case.user.find.find_user_dto import (
    InputFindUserByIDDTO,
    OutputFindUserDTO,
)
from src.infrastructure.repository.memory.user_memory_repository import (
    UserInMemoryRepository,
)


def test_find_user_by_id_use_case_using_in_memory_repository(
    repository_with_user_in_memory: UserInMemoryRepository,
) -> None:
    # Arrange
    use_case = FindUserByIDUseCase(repository_with_user_in_memory)
    user_id: str = str(list(repository_with_user_in_memory.database.keys())[0])
    user = InputFindUserByIDDTO(id=user_id)

    # Act
    found_user: OutputFindUserDTO = use_case.execute(user)

    # Assert
    assert found_user.email == "johndoe@mail.com"
    assert found_user.password == "iLoveApples2001"
    assert found_user.instance_slug.name == "lamb"
