# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa


from pydantic import EmailStr

from src.application.use_case.user.find.find_user_by_email import FindUserByEmailUseCase
from src.application.use_case.user.find.find_user_dto import (
    InputFindUserByEmailDTO,
    OutputFindUserDTO,
)
from src.infrastructure.repository.memory.user_memory_repository import (
    UserInMemoryRepository,
)


def test_find_user_by_email_use_case_using_in_memory_repository(
    repository_with_user_in_memory: UserInMemoryRepository,
) -> None:
    # Arrange
    use_case = FindUserByEmailUseCase(repository_with_user_in_memory)
    email: EmailStr = list(repository_with_user_in_memory.database.values())[0].email
    user = InputFindUserByEmailDTO(email=email)

    # Act
    found_user: OutputFindUserDTO = use_case.execute(user)

    # Assert
    assert found_user.email == email
    assert found_user.password == "iLoveApples2001"
    assert found_user.instance_slug.name == "lamb"
