# pylint: disable=no-name-in-module
from typing import Optional, Sequence

from src.application.use_case.commentary.dto.commentary_output_dto import (
    CommentaryOutputDTO,
)
from src.domain.repository.commentary_repository_interface import (
    CommentaryRepositoryInterface,
)


class FindAllCommentaries:
    """Find all commentaries."""

    def __init__(self, repository: CommentaryRepositoryInterface):
        self.repository = repository

    def execute(self) -> Optional[Sequence[CommentaryOutputDTO]]:
        """Triggers the flow to execute the use case."""
        return self.repository.find_all()
