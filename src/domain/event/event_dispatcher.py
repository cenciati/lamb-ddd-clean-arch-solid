from typing import Dict

from src.domain.event.interface.event_dispatcher_interface import (
    EventDispatcherInterface,
)
from src.domain.event.interface.event_handler_interface import EventHandlerInterface
from src.domain.event.interface.event_interface import EventInterface


class EventDispatcher(EventDispatcherInterface):
    """Manages the registration and distribution of events."""

    def __init__(self) -> None:
        self.__event_handlers = {}

    @property
    def event_handlers(self) -> Dict[str, EventHandlerInterface]:
        return self.__event_handlers

    def notify(self, event: EventInterface) -> None:
        """Notifies about a given event."""
        event_name: str = event.name
        if self.event_handlers.get(event_name):
            for event_handler in self.event_handlers.get(event_name):
                event_handler.handle(event)

    def register(self, event_name: str, event_handler: EventHandlerInterface) -> None:
        """Registries new events."""
        if not self.event_handlers.get(event_name):
            self.event_handlers[event_name] = []
        self.event_handlers[event_name].append(event_handler)

    def unregister(self, event_name: str) -> None:
        """Unregistries a specific event."""
        if self.event_handlers.get(event_name):
            self.event_handlers.pop(event_name)

    def unregister_all(self) -> None:
        """Unregistries all events."""
        self.event_handlers.clear()
