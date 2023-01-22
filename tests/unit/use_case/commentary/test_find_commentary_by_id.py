# pylint: disable=line-too-long, protected-access, no-name-in-module, duplicate-code
# flake8: noqa


from pydantic import UUID4

from src.application.use_case.commentary.dto.commentary_output_dto import (
    CommentaryOutputDTO,
)
from src.application.use_case.commentary.find_commentary_by_id import FindCommentaryByID
from src.domain.value.rating import Rating
from src.domain.value.tag import Tag
from src.infrastructure.repository.memory.commentary_memory_repository import (
    CommentaryInMemoryRepository,
)


def test_find_comment_by_id_use_case_using_in_memory_repository(
    repository_with_comment_in_memory: CommentaryInMemoryRepository,
) -> None:
    # Arrange
    use_case = FindCommentaryByID(repository_with_comment_in_memory)
    comment_id: UUID4 = list(repository_with_comment_in_memory.database.keys())[0]

    # Act
    found_comment: CommentaryOutputDTO = use_case.execute(comment_id)

    # Assert
    assert found_comment.content == "The experience was great in general."
    assert found_comment.rating == Rating(score=9)
    assert found_comment.tags == [
        Tag(id=0, name="Experience", sentiment=1, subtag=False),
        Tag(id=1, name="Infrastructure", sentiment=1, subtag=False),
    ]
    assert found_comment.instance_slug.name == "lamb"
    assert found_comment.journey_slug.name == "site"
