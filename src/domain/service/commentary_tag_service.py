from src.domain.entity.commentary import Commentary


class CommentaryTagService:
    """Service for extracting more information about
    tags classified by a customer in a commentary."""

    @classmethod
    def calculate_likes(cls, comment: Commentary) -> int:
        """Calculate how many tags with a positive sentiment (1) exist.
        Args:
            comment (Commentary): Target comment to extract this information.
        Return:
            An integer value representing the quantity of likes present
                in the comment.
        """
        return [tag.sentiment for tag in comment.tags].count(1)

    @classmethod
    def calculate_dislikes(cls, comment: Commentary) -> int:
        """Calculate how many tags with a negative sentiment (0) exist.
        Args:
            comment (Commentary): Target comment to extract this information.
        Return:
            An integer value representing the quantity of dislikes present
                in the comment.
        """

        return [tag.sentiment for tag in comment.tags].count(0)

    @classmethod
    def calculate_tags_quantity(cls, comment: Commentary) -> int:
        """Calculate how many tags there are in a comment.
        Args:
            comment (Commentary): Target comment to extract this information.
        Return:
            An integer value representing the quantity of tags present
                in the comment.
        """
        return [1 for tag in comment.tags if not tag.subtag].count(1)

    @classmethod
    def calculate_subtags_quantity(cls, comment: Commentary) -> int:
        """Calculate how many subtags there are in a comment.
        Args:
            comment (Commentary): Target comment to extract this information.
        Return:
            An integer value representing the quantity of subtags present
                in the comment.
        """
        return [1 for tag in comment.tags if tag.subtag].count(1)
