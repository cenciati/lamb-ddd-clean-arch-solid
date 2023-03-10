# pylint: disable=line-too-long, protected-access, no-name-in-module, duplicate-code
# flake8: noqa


from typing import Sequence

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
from src.domain.value.tag import Tag
from src.infrastructure.repository.memory.commentary_memory_repository import (
    CommentaryInMemoryRepository,
)


def test_add_new_comment_in_memory(new_comment: InputAddCommentaryDTO) -> None:
    # Arrange
    comment_repository = CommentaryInMemoryRepository()

    # Act
    added_new_comment: OutputAddCommentaryDTO = comment_repository.add(new_comment)

    # Assert
    assert len(comment_repository.database) == 1
    assert added_new_comment.content == "The experience was great in general."
    assert added_new_comment.rating.score == 9
    assert added_new_comment.tags == [
        Tag(id=0, name="Experience", sentiment=1, subtag=False),
        Tag(id=1, name="Infrastructure", sentiment=1, subtag=False),
    ]
    assert added_new_comment.customer_id == UUID4(new_comment.customer_id)
    assert added_new_comment.instance_slug.name == "lamb"
    assert added_new_comment.journey_slug.name == "site"


def test_find_comment_in_memory(
    repository_with_comment_in_memory: CommentaryInMemoryRepository,
) -> None:
    # Arrange
    comment_id: str = str(list(repository_with_comment_in_memory.database.keys())[0])
    comment = InputFindCommentaryByIDDTO(id=comment_id)

    # Act
    found_comment: OutputFindCommentaryDTO = repository_with_comment_in_memory.find(
        comment
    )

    # Assert
    assert len(repository_with_comment_in_memory.database) == 1
    assert found_comment.content == "The experience was great in general."
    assert found_comment.rating.score == 9
    assert found_comment.tags == [
        Tag(id=0, name="Experience", sentiment=1, subtag=False),
        Tag(id=1, name="Infrastructure", sentiment=1, subtag=False),
    ]
    assert found_comment.instance_slug.name == "lamb"
    assert found_comment.journey_slug.name == "site"


def test_find_user_by_instance_slug_in_memory(
    repository_with_comments_in_memory: CommentaryInMemoryRepository,
) -> None:
    # Arrange
    comment = InputFindCommentaryByInstanceSlugDTO(instance_slug="lamb")

    # Act
    found_comments: OutputFindCommentaryDTO = (
        repository_with_comments_in_memory.find_by_instance_slug(comment)
    )

    # Assert
    assert len(found_comments) == 3
    assert found_comments[0].instance_slug.name == "lamb"
    assert found_comments[1].instance_slug.name == "lamb"
    assert found_comments[2].instance_slug.name == "lamb"


def test_find_all_comments_in_memory(
    repository_with_comments_in_memory: CommentaryInMemoryRepository,
) -> None:
    # Act
    all_comments: Sequence[
        InputAddCommentaryDTO
    ] = repository_with_comments_in_memory.find_all()
    comments_amount_length: int = len(repository_with_comments_in_memory.database)

    # Assert
    assert comments_amount_length == 3

    assert all_comments[0].content == "The experience was great in general."
    assert all_comments[0].rating.score == 9
    assert all_comments[0].tags == [
        Tag(id=0, name="Experience", sentiment=1, subtag=False),
        Tag(id=1, name="Infrastructure", sentiment=1, subtag=False),
    ]
    assert all_comments[0].instance_slug.name == "lamb"
    assert all_comments[0].journey_slug.name == "site"

    assert all_comments[1].content == "It doesn't work properly."
    assert all_comments[1].rating.score == 2
    assert all_comments[1].tags == [
        Tag(id=0, name="Experience", sentiment=0, subtag=False),
    ]
    assert all_comments[1].instance_slug.name == "lamb"
    assert all_comments[1].journey_slug.name == "app"

    assert all_comments[2].content == "Support took a while to reply."
    assert all_comments[2].rating.score == 5
    assert all_comments[2].tags == [
        Tag(id=0, name="Experience", sentiment=1, subtag=False),
        Tag(id=2, name="Support", sentiment=0, subtag=False),
        Tag(id=3, name="Support - Agility", sentiment=0, subtag=True),
    ]
    assert all_comments[2].instance_slug.name == "lamb"
    assert all_comments[2].journey_slug.name == "site"


def test_delete_comment_in_memory(
    repository_with_comment_in_memory: CommentaryInMemoryRepository,
) -> None:
    # Act
    comment_id: str = str(list(repository_with_comment_in_memory.database.keys())[0])
    deleted_comment = InputDeleteCommentaryDTO(id=comment_id)
    repository_with_comment_in_memory.delete(deleted_comment)

    # Assert
    assert len(repository_with_comment_in_memory.database) == 0
