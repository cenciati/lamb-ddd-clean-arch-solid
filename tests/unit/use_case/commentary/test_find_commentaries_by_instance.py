# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa


from typing import Sequence

from src.application.use_case.commentary.dto.commentary_output_dto import (
    CommentaryOutputDTO,
)
from src.application.use_case.commentary.find_commentary_by_instance_slug import (
    FindCommentariesByInstanceSlug,
)
from src.infrastructure.repository.memory.commentary_memory_repository import (
    CommentaryInMemoryRepository,
)


def test_find_comments_by_instance_slug_use_case_using_in_memory_repository(
    repository_with_comments_in_memory: CommentaryInMemoryRepository,
) -> None:
    # Arrange
    use_case = FindCommentariesByInstanceSlug(repository_with_comments_in_memory)

    # Act
    found_comments: Sequence[CommentaryOutputDTO] = use_case.execute("lamb")

    # Assert
    assert len(found_comments) == 3
    assert found_comments[0].instance_slug.name == "lamb"
    assert found_comments[1].instance_slug.name == "lamb"
    assert found_comments[2].instance_slug.name == "lamb"
