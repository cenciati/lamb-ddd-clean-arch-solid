# # pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# # flake8: noqa
# from src.application.use_case.get_user.get_user import GetUser
# from src.application.use_case.get_user.user_output_dto import UserOutputDTO
# from src.domain.entity.user import User
# from src.domain.value_object.slug import Slug
# from src.infra.repository.memory.user_memory_repository import UserMemoryRepository


# def test_get_user_should_return_user_with_provided_id() -> None:
#     # Arrange
#     user_input = User(
#         email="johndoe@mail.com", password="pass12345", instance_slug=Slug("lamb")
#     )
#     in_memory_repository = UserMemoryRepository()

#     # Act
#     user_output: UserOutputDTO = GetUser(
#         user_input=user_input, repository=in_memory_repository
#     ).execute()

#     # Assert
#     assert user_output == user_input
