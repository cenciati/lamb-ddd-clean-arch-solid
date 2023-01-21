# pylint: disable=no-name-in-module
from typing import Optional

from pydantic import UUID4

from src.application.use_case.commentary.dto.commentary_output_dto import (
    CommentaryOutputDTO,
)
from src.domain.repository.commentary_repository_interface import (
    CommentaryRepositoryInterface,
)


class FindCommentaryByID:
    """Look for a specific commentary."""

    def __init__(self, repository: CommentaryRepositoryInterface):
        self.repository = repository

    def execute(self, commentary_id: UUID4) -> Optional[CommentaryOutputDTO]:
        """Triggers the flow to execute the use case."""
        return self.repository.find(commentary_id)
