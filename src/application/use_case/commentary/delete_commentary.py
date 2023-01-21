# pylint: disable=no-name-in-module

from pydantic import UUID4

from src.domain.repository.commentary_repository_interface import (
    CommentaryRepositoryInterface,
)


class DeleteCommentary:
    """Delete a commentary by id."""

    def __init__(self, repository: CommentaryRepositoryInterface):
        self.repository = repository

    def execute(self, comment_id: UUID4) -> None:
        """Triggers the flow to execute the use case."""
        self.repository.delete(comment_id)
