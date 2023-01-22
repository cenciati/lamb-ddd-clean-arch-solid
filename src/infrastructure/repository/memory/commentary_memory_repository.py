# pylint: disable=no-name-in-module,redefined-builtin, duplicate-code
from typing import Optional, Sequence

from pydantic import UUID4

from src.application.use_case.commentary.dto.add_commentary_dto import AddCommentaryDTO
from src.application.use_case.commentary.dto.commentary_output_dto import (
    CommentaryOutputDTO,
)
from src.domain.entity.commentary import Commentary
from src.domain.repository.commentary_repository_interface import (
    CommentaryRepositoryInterface,
)


class CommentaryInMemoryRepository(CommentaryRepositoryInterface):
    """In memory commentary repository."""

    def __init__(self) -> None:
        self.database = {}

    def add(self, entity: AddCommentaryDTO) -> None:
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

    def find(self, id: UUID4) -> Optional[CommentaryOutputDTO]:
        """Find commentary by unique identifier."""
        try:
            return self.database.get(id)
        except Exception as exc:
            raise Exception from exc

    def find_by_instance(
        self, instance_slug: str
    ) -> Optional[Sequence[CommentaryOutputDTO]]:
        """Find commentaries by instance."""
        try:
            return [
                comment
                for _, comment in self.database.items()
                if comment.instance_slug.name == instance_slug
            ]
        except Exception as exc:
            raise Exception from exc

    def find_all(self) -> Optional[Sequence[CommentaryOutputDTO]]:
        """Find all commentaries from memory."""
        try:
            return list(self.database.values())
        except Exception as exc:
            raise Exception from exc

    def delete(self, id: UUID4) -> None:
        """Delete commentary by ID."""
        try:
            self.database.pop(id)
        except Exception as exc:
            raise Exception from exc
