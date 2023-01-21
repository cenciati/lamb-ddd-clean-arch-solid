# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa


from pydantic import EmailStr

from src.application.use_case.user.dto.user_output_dto import UserOutputDTO
from src.application.use_case.user.find_user_by_email import FindUserByEmail
from src.infrastructure.repository.memory.user_memory_repository import (
    UserInMemoryRepository,
)


def test_find_user_by_email_use_case_using_in_memory_repository(
    repository_with_user_in_memory: UserInMemoryRepository,
) -> None:
    # Arrange
    use_case = FindUserByEmail(repository_with_user_in_memory)
    email: EmailStr = list(repository_with_user_in_memory.database.values())[0].email

    # Act
    found_user: UserOutputDTO = use_case.execute(email)

    # Assert
    assert found_user.email == email
    assert found_user.password == "iLoveApples2001"
    assert found_user.instance_slug.name == "lamb"
