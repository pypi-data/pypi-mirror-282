from typing import Any, Coroutine, Iterable, Optional
from kameleoon.network.services.service_impl import ServiceImpl
from kameleoon.network.services.data_service import DataService
from kameleoon.network.net_provider import ResponseContentType, Response, Request, HttpMethod
from kameleoon.network.query_encodable import QueryEncodable
from kameleoon.types.remote_visitor_data_filter import RemoteVisitorDataFilter


class DataServiceImpl(DataService, ServiceImpl):
    _TRACKING_CALL_RETRY_DELAY = 5.0  # in seconds

    def __init__(self, network_manager) -> None:
        DataService.__init__(self)
        ServiceImpl.__init__(self, network_manager)

    def send_tracking_data(
        self,
        visitor_code: str,
        lines: Iterable[QueryEncodable],
        user_agent: Optional[str],
        is_unique_identifier: bool,
        timeout: Optional[float] = None,
        sync=False,
    ) -> Coroutine[Any, Any, Response]:
        if timeout is None:
            timeout = self.network_manager.call_timeout
        url: str = self.network_manager.url_provider.make_tracking_url(visitor_code, is_unique_identifier)
        body = "\n".join(line.encode_query() for line in lines)
        headers = {"User-Agent": user_agent} if user_agent else None
        request = Request(HttpMethod.POST, url, timeout, headers=headers, body=body)
        return self._make_call(
            request, True, self.NUMBER_OF_RECONNECTION_ON_FAILURE, self._TRACKING_CALL_RETRY_DELAY, sync
        )

    def get_remote_data(self, key: str, timeout: Optional[float] = None, sync=False) -> Coroutine[Any, Any, Response]:
        if timeout is None:
            timeout = self.network_manager.call_timeout
        url: str = self.network_manager.url_provider.make_api_data_get_request_url(key)
        request = Request(HttpMethod.GET, url, timeout, response_content_type=ResponseContentType.JSON)
        return self._make_call(request, True, sync=sync)

    def get_remote_visitor_data(
        self,
        visitor_code: str,
        data_filter: RemoteVisitorDataFilter,
        is_unique_identifier: bool,
        timeout: Optional[float] = None,
        sync=False,
    ) -> Coroutine[Any, Any, Response]:
        if timeout is None:
            timeout = self.network_manager.call_timeout
        url: str = self.network_manager.url_provider.make_visitor_data_get_url(
            visitor_code, data_filter, is_unique_identifier
        )
        request = Request(HttpMethod.GET, url, timeout, response_content_type=ResponseContentType.JSON)
        return self._make_call(request, True, sync=sync)
