from logging import Logger
from typing import Optional
from kameleoon.network.access_token_source import AccessTokenSource


class AccessTokenSourceFactory:
    def __init__(self, client_id: str, client_secret: str) -> None:
        self._client_id = client_id
        self._client_secret = client_secret

    def create(self, network_manager, logger: Optional[Logger] = None) -> AccessTokenSource:
        return AccessTokenSource(network_manager, self._client_id, self._client_secret, logger)
