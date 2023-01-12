# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa


from pydantic import UUID4
from src.application.use_case.user.find_user_by_id.add_user_dto import AddUserDTO
from src.application.use_case.user.find_user_by_id.find_user_by_id import FindUserByID
from src.application.use_case.user.find_user_by_id.user_output_dto import UserOutputDTO
from src.domain.value_object.slug import Slug
from src.infrastructure.repository.memory.user_memory_repository import (
    UserInMemoryRepository,
)


def test_find_user_by_id_use_case_using_in_memory_repository() -> None:
    # Arrange
    new_user = AddUserDTO(
        email="johndoe@mail.com",
        password="iloveapples",
        instance_slug=Slug(name="lamb"),
    )
    repository = UserInMemoryRepository()
    repository.add(new_user)
    user_id: UUID4 = list(repository.database.keys())[0]
    use_case = FindUserByID(repository)

    # Act
    found_user: UserOutputDTO = use_case.execute(user_id)

    # Assert
    assert found_user.email == "johndoe@mail.com"
    assert found_user.password == "iloveapples"
    assert found_user.instance_slug.name == "lamb"
