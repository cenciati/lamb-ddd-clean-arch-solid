from datetime import datetime
from typing import Any, Optional

from src.domain.event.interface.event_interface import EventInterface


class CommentaryMadeEvent(EventInterface):
    """Event indicating when a commentary is made."""

    def __init__(
        self, name: str, data: Any, occurred_date: Optional[datetime] = datetime.now()
    ) -> None:
        self.name = name
        self.data = data
        self.occurred_date = occurred_date
