# pylint: disable=unused-private-member
from abc import ABC, abstractmethod
from typing import Any


class DBConnectionHandlerInterface(ABC):
    """Database connection helper interface."""

    @abstractmethod
    def get_engine(self) -> Any:
        """Get database engine."""
        raise NotImplementedError

    @abstractmethod
    def __create_engine(self) -> Any:
        """Create database engine."""
        raise NotImplementedError

    @abstractmethod
    def __enter__(self):
        """Beginning of a database connection context."""
        raise NotImplementedError

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        """End of a database connection context."""
        raise NotImplementedError
