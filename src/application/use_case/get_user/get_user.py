# from src.application.use_case.get_user.user_output_dto import UserOutputDTO
# from src.domain.entity.user import User


# class GetUser:
#     """Look for a specific user."""

#     def __init__(self, user_input: User, repository: UserRepositoryInterface):
#         self.user_input = user_input
#         self.repository = repository

#     def execute(self) -> UserOutputDTO:
#         return self.repository.get(self.user_input)
