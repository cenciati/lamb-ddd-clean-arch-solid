# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa
from src.application.use_case.user.add_user import AddUser
from src.application.use_case.user.dto.add_user_dto import AddUserDTO
from src.application.use_case.user.dto.user_output_dto import UserOutputDTO
from src.domain.value.slug import Slug
from src.infrastructure.repository.memory.user_memory_repository import (
    UserInMemoryRepository,
)


def test_add_user_use_case_using_in_memory_repository() -> None:
    # Arrange
    new_user = AddUserDTO(
        email="larryg@mail.com",
        password="Dunno3222",
        instance_slug=Slug(name="lamb"),
    )
    repository = UserInMemoryRepository()
    use_case = AddUser(repository)

    # Act
    use_case.execute(new_user)
    added_user: UserOutputDTO = list(repository.database.values())[0]

    # Assert
    assert added_user.email == "larryg@mail.com"
    assert added_user.password == "Dunno3222"
    assert added_user.instance_slug.name == "lamb"
