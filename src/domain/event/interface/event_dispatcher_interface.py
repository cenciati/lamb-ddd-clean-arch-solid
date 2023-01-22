from abc import ABC, abstractmethod

from src.domain.event.interface.event_handler_interface import EventHandlerInterface
from src.domain.event.interface.event_interface import EventInterface


class EventDispatcherInterface(ABC):
    """Interface for domain event dispatchers."""

    @abstractmethod
    def notify(self, event: EventInterface) -> None:
        """Notifies about a given event."""
        raise NotImplementedError

    @abstractmethod
    def register(self, event_name: str, event_handler: EventHandlerInterface) -> None:
        """Registries new events."""
        raise NotImplementedError

    @abstractmethod
    def unregister(self, event_name: str) -> None:
        """Unregistries a specific event."""
        raise NotImplementedError

    @abstractmethod
    def unregister_all(self) -> None:
        """Unregistries all events."""
        raise NotImplementedError
