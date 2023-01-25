# pylint: disable=no-name-in-module,invalid-name
from abc import ABC, abstractmethod
from typing import Optional, Sequence

from src.application.use_case.commentary.find.find_commentary_dto import (
    InputFindCommentaryByInstanceSlugDTO,
    OutputFindCommentaryDTO,
)
from src.domain.repository.repository_interface import RepositoryInterface


class CommentaryRepositoryInterface(RepositoryInterface, ABC):
    """Interface for managing commentary aggregates."""

    @abstractmethod
    def find_by_instance_slug(
        self, data: InputFindCommentaryByInstanceSlugDTO
    ) -> Optional[Sequence[OutputFindCommentaryDTO]]:
        """Find commentaries by instance slug."""
        raise NotImplementedError
