from typing import Any, Dict, List, Sequence

from src.application.use_case.user.add.add_user_dto import OutputAddUserDTO
from src.application.use_case.user.find.find_user_dto import OutputFindUserDTO


class UserPresenter:
    """Presentation layer for user entities."""

    @classmethod
    def to_json(
        cls,
        data: OutputAddUserDTO
        | OutputFindUserDTO
        | Sequence[OutputAddUserDTO]
        | Sequence[OutputFindUserDTO],
    ) -> List[Dict[str, Any]]:
        """Transform a data transfer object into a
            presentable json response for HTTP.
        Args:
            data (OutputFindUserDTO): Input data to be
                converted to JSON format.
        Returns:
            Presentable dictionary for HTTP responses.
        """
        if isinstance(data, list):
            return [user.dict() for user in data]
        return [data.dict()]
