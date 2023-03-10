# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa


from typing import Sequence

from src.application.use_case.commentary.find.find_all_commentaries import (
    FindAllCommentariesUseCase,
)
from src.application.use_case.commentary.find.find_commentary_dto import (
    OutputFindCommentaryDTO,
)
from src.infrastructure.repository.memory.commentary_memory_repository import (
    CommentaryInMemoryRepository,
)


def test_find_all_comments_use_case_using_in_memory_repository(
    repository_with_comments_in_memory: CommentaryInMemoryRepository,
) -> None:
    # Arrange
    use_case = FindAllCommentariesUseCase(repository_with_comments_in_memory)

    # Act
    all_comments_found: Sequence[OutputFindCommentaryDTO] = use_case.execute()
    comments_amount_length: int = len(all_comments_found)

    # Assert
    assert comments_amount_length == 3
