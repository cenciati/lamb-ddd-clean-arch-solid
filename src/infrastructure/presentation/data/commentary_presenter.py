from typing import Any, Dict, List, Sequence

from src.application.use_case.commentary.add.add_commentary_dto import (
    OutputAddCommentaryDTO,
)
from src.application.use_case.commentary.find.find_commentary_dto import (
    OutputFindCommentaryDTO,
)


class CommentaryPresenter:
    """Presentation layer for commentary entities."""

    @classmethod
    def to_json(
        cls,
        data: OutputAddCommentaryDTO
        | OutputFindCommentaryDTO
        | Sequence[OutputAddCommentaryDTO]
        | Sequence[OutputFindCommentaryDTO],
    ) -> List[Dict[str, Any]]:
        """Transform a data transfer object into a
            presentable json response for HTTP.
        Args:
            data (OutputFindCommentaryDTO): Input data to be
                converted to JSON format.
        Returns:
            Presentable dictionary for HTTP responses.
        """
        if isinstance(data, list):
            return [commentary.dict() for commentary in data]
        return [data.dict()]
