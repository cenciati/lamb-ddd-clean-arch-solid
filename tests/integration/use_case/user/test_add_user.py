# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa
from src.application.use_case.user.add.add_user import AddUserUseCase
from src.application.use_case.user.add.add_user_dto import (
    InputAddUserDTO,
    OutputAddUserDTO,
)
from src.infrastructure.repository.memory.user_memory_repository import (
    UserInMemoryRepository,
)


def test_add_user_use_case_using_in_memory_repository() -> None:
    # Arrange
    new_user = InputAddUserDTO(
        email="larryg@mail.com",
        password="Dunno3222",
        instance_slug="lamb",
    )
    repository = UserInMemoryRepository()
    use_case = AddUserUseCase(repository)

    # Act
    added_user: OutputAddUserDTO = use_case.execute(new_user)

    # Assert
    assert added_user.email == "larryg@mail.com"
    assert added_user.password == "Dunno3222"
    assert added_user.instance_slug.name == "lamb"
