# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa

from uuid import uuid4

from pydantic import UUID4

from src.application.use_case.commentary.add_commentary import AddCommentary
from src.application.use_case.commentary.dto.add_commentary_dto import AddCommentaryDTO
from src.application.use_case.commentary.dto.commentary_output_dto import (
    CommentaryOutputDTO,
)
from src.domain.value.rating import Rating
from src.domain.value.slug import Slug
from src.domain.value.tag import Tag
from src.infrastructure.repository.memory.commentary_memory_repository import (
    CommentaryInMemoryRepository,
)


def test_add_comment_use_case_using_in_memory_repository() -> None:
    # Arrange
    customer_id: UUID4 = uuid4()
    new_comment = AddCommentaryDTO(
        content="The experience was great in general.",
        rating=Rating(score=9),
        tags=[
            Tag(id=0, name="Experience", sentiment=1, subtag=False),
            Tag(id=1, name="Infrastructure", sentiment=1, subtag=False),
        ],
        customer_id=customer_id,
        instance_slug=Slug(name="lamb"),
        journey_slug=Slug(name="site"),
    )
    repository = CommentaryInMemoryRepository()
    use_case = AddCommentary(repository)

    # Act
    use_case.execute(new_comment)
    added_comment: CommentaryOutputDTO = list(repository.database.values())[0]

    # Assert
    assert added_comment.content == "The experience was great in general."
    assert added_comment.rating == Rating(score=9)
    assert added_comment.tags == [
        Tag(id=0, name="Experience", sentiment=1, subtag=False),
        Tag(id=1, name="Infrastructure", sentiment=1, subtag=False),
    ]
    assert added_comment.customer_id == customer_id
    assert added_comment.instance_slug == Slug(name="lamb")
    assert added_comment.journey_slug == Slug(name="site")
