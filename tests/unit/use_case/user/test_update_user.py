# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa
from pydantic import UUID4

from src.application.use_case.user.dto.update_user_dto import UpdateUserDTO
from src.application.use_case.user.dto.user_output_dto import UserOutputDTO
from src.application.use_case.user.update_user import UpdateUser
from src.domain.value.slug import Slug
from src.infrastructure.repository.memory.user_memory_repository import (
    UserInMemoryRepository,
)


def test_update_user_use_case_using_in_memory_repository(
    repository_with_user_in_memory: UserInMemoryRepository,
) -> None:
    # Arrange
    use_case = UpdateUser(repository_with_user_in_memory)
    user_id: UUID4 = list(repository_with_user_in_memory.database.keys())[0]
    updated_user = UpdateUserDTO(
        email="newemail@mail.com",
        password="new_password",
        instance_slug=Slug(name="new-slug"),
    )

    # Act
    use_case.execute(user_id, updated_user)
    current_user: UserOutputDTO = list(
        repository_with_user_in_memory.database.values()
    )[0]

    # Assert
    assert current_user.email == updated_user.email
    assert current_user.password == updated_user.password
    assert current_user.instance_slug.name == updated_user.instance_slug.name
