# pylint: disable=missing-class-docstring


class CommentaryNotFoundError(Exception):
    message = "Could not find specified commentary."

    def __str__(self):
        return CommentaryNotFoundError.message


class CommentariesNotFoundError(Exception):
    message = "Could not find any commentary."

    def __str__(self):
        return CommentariesNotFoundError.message
