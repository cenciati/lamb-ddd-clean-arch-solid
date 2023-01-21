# pylint: disable=no-name-in-module

from src.application.use_case.commentary.dto.add_commentary_dto import AddCommentaryDTO
from src.domain.repository.commentary_repository_interface import (
    CommentaryRepositoryInterface,
)


class AddCommentary:
    """Add a given commentary."""

    def __init__(self, repository: CommentaryRepositoryInterface):
        self.repository = repository

    def execute(self, new_commentary: AddCommentaryDTO) -> None:
        """Triggers the flow to execute the use case."""
        self.repository.add(new_commentary)
