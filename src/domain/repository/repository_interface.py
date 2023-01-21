# pylint: disable=no-name-in-module, invalid-name, redefined-builtin
from abc import ABC, abstractmethod
from typing import Any, Optional, Sequence


class RepositoryInterface(ABC):
    """Interface for managing aggregates."""

    @abstractmethod
    def add(self, entity: Any) -> None:
        """Add something into somewhere."""
        raise NotImplementedError

    @abstractmethod
    def find(self, id: Any) -> Optional[Any]:
        """Find something by unique identifier."""
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> Optional[Sequence[Any]]:
        """Find everything of something."""
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: Any) -> None:
        """Delete something by unique identifier."""
        raise NotImplementedError
