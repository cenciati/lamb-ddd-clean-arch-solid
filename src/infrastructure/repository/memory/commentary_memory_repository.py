# pylint: disable=no-name-in-module,redefined-builtin, duplicate-code
from typing import Optional, Sequence

from src.application.use_case.commentary.add.add_commentary_dto import (
    InputAddCommentaryDTO,
)
from src.application.use_case.commentary.delete.delete_commentary_dto import (
    InputDeleteCommentaryDTO,
)
from src.application.use_case.commentary.find.find_commentary_dto import (
    InputFindCommentaryDTO,
    OutputFindCommentaryDTO,
)
from src.domain.entity.commentary import Commentary
from src.domain.repository.commentary_repository_interface import (
    CommentaryRepositoryInterface,
)


class CommentaryInMemoryRepository(CommentaryRepositoryInterface):
    """In memory commentary repository."""

    def __init__(self) -> None:
        self.database = {}

    def add(self, entity: InputAddCommentaryDTO) -> None:
        """Add commentary into memory."""
        try:
            new_comment = Commentary(
                content=entity.content,
                rating=entity.rating,
                tags=entity.tags,
                customer_id=entity.customer_id,
                instance_slug=entity.instance_slug,
                journey_slug=entity.journey_slug,
                automatic=entity.automatic,
            )
            self.database[new_comment.id] = new_comment
        except Exception as exc:
            raise Exception from exc

    def find(self, input: InputFindCommentaryDTO) -> Optional[OutputFindCommentaryDTO]:
        """Find commentary by unique identifier."""
        try:
            return self.database.get(input.id)
        except Exception as exc:
            raise Exception from exc

    def find_by_instance_slug(
        self, input: InputFindCommentaryDTO
    ) -> Optional[Sequence[OutputFindCommentaryDTO]]:
        """Find commentaries by instance."""
        try:
            return [
                comment
                for _, comment in self.database.items()
                if comment.instance_slug.name == input.instance_slug.name
            ]
        except Exception as exc:
            raise Exception from exc

    def find_all(self) -> Optional[Sequence[OutputFindCommentaryDTO]]:
        """Find all commentaries from memory."""
        try:
            return list(self.database.values())
        except Exception as exc:
            raise Exception from exc

    def delete(self, input: InputDeleteCommentaryDTO) -> None:
        """Delete commentary by ID."""
        try:
            self.database.pop(input.id)
        except Exception as exc:
            raise Exception from exc
