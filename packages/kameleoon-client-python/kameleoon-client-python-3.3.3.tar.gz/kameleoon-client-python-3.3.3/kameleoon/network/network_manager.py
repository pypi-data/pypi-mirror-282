from typing import Type, TypeVar, Optional
from logging import Logger
from kameleoon.network.access_token_source import AccessTokenSource
from kameleoon.network.net_provider import NetProvider
from kameleoon.network.url_provider import UrlProvider
from kameleoon.network.service_initialize_context import ServiceInitializeContext
from kameleoon.network.services.service import Service


S = TypeVar("S", bound=Service)  # pylint: disable=C0103


class NetworkManager:
    @property
    def url_provider(self) -> UrlProvider:
        raise NotImplementedError()

    @property
    def net_provider(self) -> NetProvider:
        raise NotImplementedError()

    @property
    def access_token_source(self) -> AccessTokenSource:
        raise NotImplementedError()

    @property
    def environment(self) -> Optional[str]:
        raise NotImplementedError()

    @property
    def call_timeout(self) -> float:
        raise NotImplementedError()

    @property
    def logger(self) -> Logger:
        raise NotImplementedError()

    def get_service_initialize_context(self) -> ServiceInitializeContext:
        raise NotImplementedError()

    def get_service(self, service_type: Type[S]) -> S:
        raise NotImplementedError()
