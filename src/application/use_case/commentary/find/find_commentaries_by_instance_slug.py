# pylint: disable=no-name-in-module
from typing import Optional, Sequence

from src.application.use_case.commentary.find.find_commentary_dto import (
    InputFindCommentaryByInstanceSlugDTO,
    OutputFindCommentaryDTO,
)
from src.domain.repository.commentary_repository_interface import (
    CommentaryRepositoryInterface,
)


class FindCommentariesByInstanceSlugUseCase:
    """Look for commentaries by instance slug."""

    def __init__(self, repository: CommentaryRepositoryInterface):
        self.repository = repository

    def execute(
        self, data: InputFindCommentaryByInstanceSlugDTO
    ) -> Optional[Sequence[OutputFindCommentaryDTO]]:
        """Triggers the flow to execute the use case."""
        return self.repository.find_by_instance_slug(data)
