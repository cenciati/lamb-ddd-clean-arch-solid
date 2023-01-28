# pylint: disable=missing-class-docstring


class UserNotFoundError(Exception):
    message = "Could not find specified user."

    def __str__(self):
        return UserNotFoundError.message


class UsersNotFoundError(Exception):
    message = "Could not find any user."

    def __str__(self):
        return UsersNotFoundError.message


class UserDuplicateEmailError(Exception):
    message = "User with specified email already exists."

    def __str__(self):
        return UserDuplicateEmailError.message
