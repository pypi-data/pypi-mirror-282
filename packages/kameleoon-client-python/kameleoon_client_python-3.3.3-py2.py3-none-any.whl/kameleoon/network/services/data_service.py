from typing import Any, Coroutine, Iterable, Optional
from kameleoon.network.services.service import Service
from kameleoon.network.query_encodable import QueryEncodable
from kameleoon.network.net_provider import Response
from kameleoon.types.remote_visitor_data_filter import RemoteVisitorDataFilter


class DataService(Service):
    def send_tracking_data(
        self,
        visitor_code: str,
        lines: Iterable[QueryEncodable],
        user_agent: Optional[str],
        is_unique_identifier: bool,
        timeout: Optional[float] = None,
        sync=False,
    ) -> Coroutine[Any, Any, Response]:
        raise NotImplementedError()

    def get_remote_data(self, key: str, timeout: Optional[float] = None, sync=False) -> Coroutine[Any, Any, Response]:
        raise NotImplementedError()

    def get_remote_visitor_data(
        self,
        visitor_code: str,
        data_filter: RemoteVisitorDataFilter,
        is_unique_identifier: bool,
        timeout: Optional[float] = None,
        sync=False,
    ) -> Coroutine[Any, Any, Response]:
        raise NotImplementedError()
