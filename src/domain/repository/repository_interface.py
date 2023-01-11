# pylint: disable=no-name-in-module, invalid-name, redefined-builtin
from abc import ABC, abstractmethod
from typing import Any, Sequence


class RepositoryInterface(ABC):
    """Interface for managing aggregates."""

    @abstractmethod
    def add(self, aggregate_input: Any) -> None:
        """Add something into somewhere."""
        raise NotImplementedError

    @abstractmethod
    def find(self, id: Any) -> Any:
        """Find something by its unique identifier."""
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> Sequence[Any]:
        """Find everything of something by its unique identifier."""
        raise NotImplementedError

    @abstractmethod
    def update(self, id: Any, updated_aggregate_input: Any) -> None:
        """Update information of something by its unique identifier."""
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: Any) -> None:
        """Delete something by its unique identifier."""
        raise NotImplementedError
