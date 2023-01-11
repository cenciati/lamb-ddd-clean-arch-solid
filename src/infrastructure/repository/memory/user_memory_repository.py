# from typing import List

# from src.application.use_case.get_user.user_output_dto import UserOutputDTO
# from src.application.use_case.get_user.user_update_dto import UserUpdateDTO
# from src.domain.entity.user import User


# class UserMemoryRepository(UserRepositoryInterface):
#     """In memory user repository."""

#     def __init__(self) -> None:
#         self.database: List[User] = []

#     def add(self, user_input: User) -> UserOutputDTO:
#         """Add a new user into memory."""
#         self.database.append(user_input)
#         return user_input

#     def get(self, user_input: User) -> UserOutputDTO:
#         """Get a user by their internal id or e-mail."""
#         idx: int = self.database.index(user_input)
#         return self.database[idx]

#     def update(self, user_input: UserUpdateDTO) -> UserOutputDTO:
#         """Update a user information by their internal id or e-mail."""
#         for record in self.database:
#             if record.id == user_input.id:
#                 idx: int = self.database.index(record)
#                 updated_user: User = record
#                 self.database[idx] = user_input
#         return updated_user

#     def delete(self, user_input: User) -> UserOutputDTO:
#         """Delete a user by their internal id or e-mail."""
#         idx: int = self.database.index(user_input)
#         deleted_user: UserOutputDTO = self.database[idx]
#         self.database.remove(user_input)
#         return deleted_user
