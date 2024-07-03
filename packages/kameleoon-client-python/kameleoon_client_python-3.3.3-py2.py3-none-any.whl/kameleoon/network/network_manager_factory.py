from logging import Logger
from typing import Optional
from kameleoon.network.access_token_source_factory import AccessTokenSourceFactory
from kameleoon.network.net_provider import NetProvider
from kameleoon.network.network_manager import NetworkManager


class NetworkManagerFactory:
    def create(
        self,
        site_code: str,
        environment: Optional[str],
        call_timeout: float,
        net_provider: NetProvider,
        access_token_source_factory: AccessTokenSourceFactory,
        logger: Logger,
    ) -> NetworkManager:
        raise NotImplementedError()
