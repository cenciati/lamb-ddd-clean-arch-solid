# pylint: disable=no-name-in-module, invalid-name, redefined-builtin
from abc import ABC, abstractmethod
from typing import Any, Sequence

from src.domain.repository.repository_interface import RepositoryInterface


class CommentaryRepositoryInterface(RepositoryInterface, ABC):
    """Interface for managing commentary aggregates."""

    @abstractmethod
    def find_by_instance(self, instance_slug: str) -> Sequence[Any]:
        """Find commentaries by instance slug associated.."""
        raise NotImplementedError
