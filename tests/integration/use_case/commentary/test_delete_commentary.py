# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa


from src.application.use_case.commentary.delete.delete_commentary import (
    DeleteCommentaryUseCase,
)
from src.application.use_case.commentary.delete.delete_commentary_dto import (
    InputDeleteCommentaryDTO,
)
from src.infrastructure.repository.memory.commentary_memory_repository import (
    CommentaryInMemoryRepository,
)


def test_delete_commentary_use_case_using_in_memory_repository(
    repository_with_comment_in_memory: CommentaryInMemoryRepository,
) -> None:
    # Arrange
    use_case = DeleteCommentaryUseCase(repository_with_comment_in_memory)
    comment_id: str = str(list(repository_with_comment_in_memory.database.keys())[0])
    deleted_comment = InputDeleteCommentaryDTO(id=comment_id)

    # Act
    use_case.execute(deleted_comment)
    database_length: int = len(repository_with_comment_in_memory.database)

    # Assert
    assert database_length == 0
