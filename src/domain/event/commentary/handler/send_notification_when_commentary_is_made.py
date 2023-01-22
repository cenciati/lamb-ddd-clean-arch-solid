from src.domain.event.interface.event_handler_interface import EventHandlerInterface
from src.domain.event.interface.event_interface import EventInterface


class SendNotificationWhenCommentaryIsMadeHandler(EventHandlerInterface):
    """Send a notification when a commentary is made handler."""

    def handle(self, event: EventInterface) -> None:
        """Processs the event."""
        # to-do: Send notification feature
        print(event.data)
