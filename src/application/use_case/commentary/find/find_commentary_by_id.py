# pylint: disable=no-name-in-module,redefined-builtin
from typing import Optional

from src.application.use_case.commentary.find.find_commentary_dto import (
    InputFindCommentaryDTO,
    OutputFindCommentaryDTO,
)
from src.domain.repository.commentary_repository_interface import (
    CommentaryRepositoryInterface,
)


class FindCommentaryByIDUseCase:
    """Look for a specific commentary."""

    def __init__(self, repository: CommentaryRepositoryInterface):
        self.repository = repository

    def execute(
        self, input: InputFindCommentaryDTO
    ) -> Optional[OutputFindCommentaryDTO]:
        """Triggers the flow to execute the use case."""
        return self.repository.find(input)
