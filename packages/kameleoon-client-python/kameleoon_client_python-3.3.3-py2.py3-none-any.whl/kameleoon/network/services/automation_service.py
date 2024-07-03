from typing import Any, Coroutine, Optional
from kameleoon.network.services.service import Service
from kameleoon.network.net_provider import Response


class AutomationService(Service):
    def fetch_access_jwtoken(
        self, client_id: str, client_secret: str, timeout: Optional[float] = None
    ) -> Coroutine[Any, Any, Response]:
        raise NotImplementedError()
