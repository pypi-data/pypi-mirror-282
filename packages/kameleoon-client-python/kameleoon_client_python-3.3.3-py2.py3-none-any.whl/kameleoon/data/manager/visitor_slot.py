import time
from threading import Lock
from typing import Optional
from kameleoon.data.manager.visitor import Visitor


class VisitorSlot:
    def __init__(self) -> None:
        self.lock = Lock()
        self.visitor: Optional[Visitor] = None
        self.last_activity_time = 0.0
        self.update_last_activity_time()

    def update_last_activity_time(self) -> None:
        self.last_activity_time = time.time()
