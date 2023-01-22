# pylint: disable=no-name-in-module,redefined-builtin

from src.application.use_case.commentary.delete.delete_commentary_dto import (
    InputDeleteCommentaryDTO,
)
from src.domain.repository.commentary_repository_interface import (
    CommentaryRepositoryInterface,
)


class DeleteCommentaryUseCase:
    """Delete a commentary by id."""

    def __init__(self, repository: CommentaryRepositoryInterface):
        self.repository = repository

    def execute(self, input: InputDeleteCommentaryDTO) -> None:
        """Triggers the flow to execute the use case."""
        self.repository.delete(input)
