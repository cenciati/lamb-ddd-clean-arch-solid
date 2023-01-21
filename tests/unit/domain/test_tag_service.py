# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa
from src.domain.entity.commentary import Commentary
from src.domain.service.commentary_tag_service import CommentaryTagService


def test_commentary_tag_services_should_be_equal_zero_if_there_are_no_tags(
    comment: Commentary,
) -> None:
    # Arrange
    commentary_tag_service = CommentaryTagService()

    # Act
    assert commentary_tag_service.calculate_likes(comment) == 0
    assert commentary_tag_service.calculate_dislikes(comment) == 0
    assert commentary_tag_service.calculate_tags_quantity(comment) == 0
    assert commentary_tag_service.calculate_subtags_quantity(comment) == 0


def test_calculate_likes_should_return_quantity_of_likes_present_in_a_comment(
    comment_with_tags: Commentary,
) -> None:
    # Arrange
    commentary_tag_service = CommentaryTagService()

    # Act
    likes_quantity: int = commentary_tag_service.calculate_likes(comment_with_tags)

    # Assert
    assert likes_quantity == 3


def test_calculate_dislikes_should_return_quantity_of_dislikes_present_in_a_comment(
    comment_with_tags: Commentary,
) -> None:
    # Arrange
    commentary_tag_service = CommentaryTagService()

    # Act
    dislikes_quantity: int = commentary_tag_service.calculate_dislikes(
        comment_with_tags
    )

    # Assert
    assert dislikes_quantity == 1


def test_calculate_tags_quantity_should_return_quantity_of_tags_present_in_a_comment(
    comment_with_tags: Commentary,
) -> None:
    # Arrange
    commentary_tag_service = CommentaryTagService()

    # Act
    tags_quantity: int = commentary_tag_service.calculate_tags_quantity(
        comment_with_tags
    )

    # Assert
    assert tags_quantity == 3


def test_calculate_subtags_quantity_should_return_quantity_of_subtags_present_in_a_comment(
    comment_with_tags: Commentary,
) -> None:
    # Arrange
    commentary_tag_service = CommentaryTagService()

    # Act
    subtags_quantity: int = commentary_tag_service.calculate_subtags_quantity(
        comment_with_tags
    )

    # Assert
    assert subtags_quantity == 1
