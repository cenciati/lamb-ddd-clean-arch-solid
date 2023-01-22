# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa
from pydantic import UUID4

from src.application.use_case.user.find.find_user_dto import OutputFindUserDTO
from src.application.use_case.user.update.update_user import UpdateUserUseCase
from src.application.use_case.user.update.update_user_dto import InputUpdateUserDTO
from src.domain.value.slug import Slug
from src.infrastructure.repository.memory.user_memory_repository import (
    UserInMemoryRepository,
)


def test_update_user_use_case_using_in_memory_repository(
    repository_with_user_in_memory: UserInMemoryRepository,
) -> None:
    # Arrange
    use_case = UpdateUserUseCase(repository_with_user_in_memory)
    user_id: UUID4 = list(repository_with_user_in_memory.database.keys())[0]
    updated_user = InputUpdateUserDTO(
        id=user_id,
        email="newemail@mail.com",
        password="new_password",
        instance_slug=Slug(name="new-slug"),
    )

    # Act
    use_case.execute(updated_user)
    current_user: OutputFindUserDTO = list(
        repository_with_user_in_memory.database.values()
    )[0]

    # Assert
    assert current_user.email == updated_user.email
    assert current_user.password == updated_user.password
    assert current_user.instance_slug.name == updated_user.instance_slug.name
