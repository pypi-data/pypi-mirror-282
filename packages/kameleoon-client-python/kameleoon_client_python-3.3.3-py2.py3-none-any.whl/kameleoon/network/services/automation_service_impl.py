from typing import Any, Coroutine, Optional
from kameleoon.network.services.service_impl import ServiceImpl
from kameleoon.network.services.automation_service import AutomationService
from kameleoon.network.net_provider import ResponseContentType, Response, Request, HttpMethod
from kameleoon.network.query_builder import QueryBuilder, QueryParam, QueryParams


class AutomationServiceImpl(AutomationService, ServiceImpl):
    _ACCESS_TOKEN_GRANT_TYPE = "client_credentials"
    _H_CONTENT_TYPE_NAME = "Content-Type"
    _H_CONTENT_TYPE_VALUE = "application/x-www-form-urlencoded"

    def __init__(self, network_manager) -> None:
        AutomationService.__init__(self)
        ServiceImpl.__init__(self, network_manager)

    def fetch_access_jwtoken(
        self, client_id: str, client_secret: str, timeout: Optional[float] = None
    ) -> Coroutine[Any, Any, Response]:
        if timeout is None:
            timeout = self.network_manager.call_timeout
        url: str = self.network_manager.url_provider.make_access_token_url()
        body = QueryBuilder(
            QueryParam(QueryParams.GRANT_TYPE, self._ACCESS_TOKEN_GRANT_TYPE),
            QueryParam(QueryParams.CLIENT_ID, client_id),
            QueryParam(QueryParams.CLIENT_SECRET, client_secret),
        )
        headers = {self._H_CONTENT_TYPE_NAME: self._H_CONTENT_TYPE_VALUE}
        request = Request(
            HttpMethod.POST, url, timeout, headers=headers, body=str(body),
            response_content_type=ResponseContentType.JSON,
        )
        return self._make_call(request, False)
