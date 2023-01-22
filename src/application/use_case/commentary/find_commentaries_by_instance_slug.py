# pylint: disable=no-name-in-module
from typing import Optional, Sequence

from src.application.use_case.commentary.dto.commentary_output_dto import (
    CommentaryOutputDTO,
)
from src.domain.repository.commentary_repository_interface import (
    CommentaryRepositoryInterface,
)


class FindCommentariesByInstanceSlug:
    """Look for commentaries by instance slug."""

    def __init__(self, repository: CommentaryRepositoryInterface):
        self.repository = repository

    def execute(
        self, comment_instance_slug: str
    ) -> Optional[Sequence[CommentaryOutputDTO]]:
        """Triggers the flow to execute the use case."""
        return self.repository.find_by_instance(comment_instance_slug)
