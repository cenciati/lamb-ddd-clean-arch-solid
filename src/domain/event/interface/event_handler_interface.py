from abc import ABC, abstractmethod

from src.domain.event.interface.event_interface import EventInterface


class EventHandlerInterface(ABC):
    """Interface for domain event handlers."""

    @abstractmethod
    def handle(self, event: EventInterface) -> None:
        """Processes a given event."""
        raise NotImplementedError
