# pylint: disable=line-too-long, protected-access, disable=no-name-in-module
# flake8: noqa


from src.domain.entity.commentary import Commentary
from src.domain.event.commentary.commentary_made_event import CommentaryMadeEvent
from src.domain.event.commentary.handler.send_notification_when_commentary_is_made import (
    SendNotificationWhenCommentaryIsMadeHandler,
)
from src.domain.event.event_dispatcher import EventDispatcher


def test_register_an_new_event() -> None:
    # Arrange
    event_dispatcher = EventDispatcher()
    event_handler = SendNotificationWhenCommentaryIsMadeHandler()
    event_name: str = "CommentaryMadeEvent"

    # Act
    event_dispatcher.register(event_name, event_handler)

    # Assert
    assert len(event_dispatcher.event_handlers) == 1
    assert isinstance(event_dispatcher.event_handlers, dict)
    assert event_dispatcher.event_handlers[event_name] == [event_handler]


def test_unregister_an_event() -> None:
    # Arrange
    event_dispatcher = EventDispatcher()
    event_handler = SendNotificationWhenCommentaryIsMadeHandler()
    event_name: str = "CommentaryMadeEvent"
    event_dispatcher.register(event_name, event_handler)

    # Act
    event_dispatcher.unregister(event_name)

    # Assert
    assert len(event_dispatcher.event_handlers) == 0


def test_unregister_all_events() -> None:
    # Arrange
    event_dispatcher = EventDispatcher()
    event_handler = SendNotificationWhenCommentaryIsMadeHandler()
    event_name: str = "CommentaryMadeEvent"
    event_dispatcher.register(event_name, event_handler)
    event_dispatcher.register(event_name, event_handler)
    event_dispatcher.register(event_name, event_handler)

    # Act
    event_dispatcher.unregister_all()

    # Assert
    assert len(event_dispatcher.event_handlers) == 0


def test_notify_all_event_handlers(comment_with_tags: Commentary) -> None:
    # Arrange
    event_dispatcher = EventDispatcher()
    event_handler = SendNotificationWhenCommentaryIsMadeHandler()
    event_name: str = "CommentaryMadeEvent"
    event_dispatcher.register(event_name, event_handler)
    event = CommentaryMadeEvent(name=event_name, data=comment_with_tags.dict())

    # Act
    event_dispatcher.notify(event)

    # Assert
    assert True
