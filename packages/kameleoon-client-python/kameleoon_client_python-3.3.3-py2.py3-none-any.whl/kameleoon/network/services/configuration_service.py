from typing import Any, Coroutine, Optional
from kameleoon.network.services.service import Service
from kameleoon.network.net_provider import Response


class ConfigurationService(Service):
    def fetch_configuration(
        self, environment: Optional[str] = None, time_stamp: Optional[int] = None, timeout: Optional[float] = None
    ) -> Coroutine[Any, Any, Response]:
        raise NotImplementedError()
