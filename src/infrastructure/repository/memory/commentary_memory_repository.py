# pylint: disable=no-name-in-module,duplicate-code
from typing import List, Optional, Sequence

from pydantic import UUID4

from src.application.use_case.commentary.add.add_commentary_dto import (
    InputAddCommentaryDTO,
    OutputAddCommentaryDTO,
)
from src.application.use_case.commentary.delete.delete_commentary_dto import (
    InputDeleteCommentaryDTO,
)
from src.application.use_case.commentary.find.find_commentary_dto import (
    InputFindCommentaryByIDDTO,
    InputFindCommentaryByInstanceSlugDTO,
    OutputFindCommentaryDTO,
)
from src.domain.entity.commentary import Commentary
from src.domain.repository.commentary_repository_interface import (
    CommentaryRepositoryInterface,
)
from src.domain.value.rating import Rating
from src.domain.value.slug import Slug
from src.domain.value.tag import Tag


class CommentaryInMemoryRepository(CommentaryRepositoryInterface):
    """In memory commentary repository."""

    def __init__(self) -> None:
        self.database = {}

    def add(self, entity: InputAddCommentaryDTO) -> OutputAddCommentaryDTO:
        """Add commentary into memory."""
        try:
            if entity.tags:
                tags: List[Tag] = [
                    Tag(
                        id=tag["id"],
                        name=tag["name"],
                        sentiment=tag["sentiment"],
                        subtag=tag["subtag"],
                    )
                    for tag in entity.tags
                ]
            new_comment = Commentary(
                content=entity.content,
                rating=Rating(score=entity.rating),
                tags=tags,
                customer_id=UUID4(entity.customer_id),
                instance_slug=Slug(name=entity.instance_slug),
                journey_slug=Slug(name=entity.journey_slug),
                automatic=entity.automatic,
            )
            self.database[new_comment.id] = new_comment
            return new_comment
        except Exception as exc:
            raise Exception from exc

    def find(
        self, data: InputFindCommentaryByIDDTO
    ) -> Optional[OutputFindCommentaryDTO]:
        """Find commentary by unique identifier."""
        try:
            return self.database.get(UUID4(data.id))
        except Exception as exc:
            raise Exception from exc

    def find_by_instance_slug(
        self, data: InputFindCommentaryByInstanceSlugDTO
    ) -> Optional[Sequence[OutputFindCommentaryDTO]]:
        """Find commentaries by instance."""
        try:
            return [
                comment
                for _, comment in self.database.items()
                if comment.instance_slug.name == data.instance_slug
            ]
        except Exception as exc:
            raise Exception from exc

    def find_all(self) -> Optional[Sequence[OutputFindCommentaryDTO]]:
        """Find all commentaries from memory."""
        try:
            return list(self.database.values())
        except Exception as exc:
            raise Exception from exc

    def delete(self, data: InputDeleteCommentaryDTO) -> None:
        """Delete commentary by ID."""
        try:
            self.database.pop(UUID4(data.id))
        except Exception as exc:
            raise Exception from exc
