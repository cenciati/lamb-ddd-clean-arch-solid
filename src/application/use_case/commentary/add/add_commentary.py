# pylint: disable=no-name-in-module,redefined-builtin

from src.application.use_case.commentary.add.add_commentary_dto import (
    InputAddCommentaryDTO,
)
from src.domain.repository.commentary_repository_interface import (
    CommentaryRepositoryInterface,
)


class AddCommentaryUseCase:
    """Add a given commentary."""

    def __init__(self, repository: CommentaryRepositoryInterface):
        self.repository = repository

    def execute(self, input: InputAddCommentaryDTO) -> None:
        """Triggers the flow to execute the use case."""
        self.repository.add(input)
