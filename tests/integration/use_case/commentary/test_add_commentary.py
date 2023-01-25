# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa

from pydantic import UUID4

from src.application.use_case.commentary.add.add_commentary import AddCommentaryUseCase
from src.application.use_case.commentary.add.add_commentary_dto import (
    InputAddCommentaryDTO,
)
from src.application.use_case.commentary.find.find_commentary_dto import (
    OutputFindCommentaryDTO,
)
from src.domain.value.tag import Tag
from src.infrastructure.repository.memory.commentary_memory_repository import (
    CommentaryInMemoryRepository,
)


def test_add_new_comment_use_case_using_in_memory_repository(
    new_comment: InputAddCommentaryDTO,
) -> None:
    # Arrange
    customer_id: str = new_comment.customer_id
    repository = CommentaryInMemoryRepository()
    use_case = AddCommentaryUseCase(repository)

    # Act
    use_case.execute(new_comment)
    added_comment: OutputFindCommentaryDTO = list(repository.database.values())[0]

    # Assert
    assert added_comment.content == "The experience was great in general."
    assert added_comment.rating.score == 9
    assert added_comment.tags == [
        Tag(id=0, name="Experience", sentiment=1, subtag=False),
        Tag(id=1, name="Infrastructure", sentiment=1, subtag=False),
    ]
    assert added_comment.customer_id == UUID4(customer_id)
    assert added_comment.instance_slug.name == "lamb"
    assert added_comment.journey_slug.name == "site"
