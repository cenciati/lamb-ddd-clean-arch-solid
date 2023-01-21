# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa


from pydantic import UUID4

from src.application.use_case.commentary.delete_commentary import DeleteCommentary
from src.infrastructure.repository.memory.commentary_memory_repository import (
    CommentaryInMemoryRepository,
)


def test_delete_commentary_use_case_using_in_memory_repository(
    repository_with_comment_in_memory: CommentaryInMemoryRepository,
) -> None:
    # Arrange
    use_case = DeleteCommentary(repository_with_comment_in_memory)
    comment_id: UUID4 = list(repository_with_comment_in_memory.database.keys())[0]

    # Act
    use_case.execute(comment_id)
    database_length: int = len(repository_with_comment_in_memory.database)

    # Assert
    assert database_length == 0
