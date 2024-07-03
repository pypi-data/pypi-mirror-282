"ThreadingClientReadiness"
from threading import Lock


class ThreadingClientReadiness:
    def __init__(self) -> None:
        self._is_initializing = False
        self._success = False
        self._condition = Lock()
        self.reset()

    @property
    def is_initializing(self) -> bool:
        return self._is_initializing

    @property
    def success(self) -> bool:
        return self._success

    def reset(self) -> None:
        self._success = False
        if not self._is_initializing:
            self._is_initializing = True
            self._condition.acquire()

    def set(self, success: bool) -> None:
        self._success = success
        if self._is_initializing:
            self._condition.release()
            self._is_initializing = False

    def wait(self) -> bool:
        if self._is_initializing:
            with self._condition:
                pass
        return self._success
