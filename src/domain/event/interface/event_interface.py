from abc import ABC
from datetime import datetime
from typing import Any


class EventInterface(ABC):
    """Interface for creating domain events."""

    name: str
    data: Any
    occurred_time: datetime
