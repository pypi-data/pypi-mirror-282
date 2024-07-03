from typing import Any, Coroutine, Optional
from kameleoon.network.services.service_impl import ServiceImpl
from kameleoon.network.services.configuration_service import ConfigurationService
from kameleoon.network.net_provider import ResponseContentType, Response, Request, HttpMethod
from kameleoon.sdk_version import SdkVersion


class ConfigurationServiceImpl(ConfigurationService, ServiceImpl):
    _SDK_TYPE_HEADER = "X-Kameleoon-SDK-Type"
    _SDK_VERSION_HEADER = "X-Kameleoon-SDK-Version"

    def __init__(self, network_manager) -> None:
        ConfigurationService.__init__(self)
        ServiceImpl.__init__(self, network_manager)

    def fetch_configuration(
        self, environment: Optional[str] = None, time_stamp: Optional[int] = None, timeout: Optional[float] = None
    ) -> Coroutine[Any, Any, Response]:
        if timeout is None:
            timeout = self.network_manager.call_timeout
        url: str = self.network_manager.url_provider.make_configuration_url(environment, time_stamp)
        sdk_headers = {
            self._SDK_TYPE_HEADER: SdkVersion.NAME,
            self._SDK_VERSION_HEADER: SdkVersion.VERSION,
        }
        request = Request(
            HttpMethod.GET, url, timeout, headers=sdk_headers,
            response_content_type=ResponseContentType.JSON,
        )
        return self._make_call(request, False, self.NUMBER_OF_RECONNECTION_ON_FAILURE)
