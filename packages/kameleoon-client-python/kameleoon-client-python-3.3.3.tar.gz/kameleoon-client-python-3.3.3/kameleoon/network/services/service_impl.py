import asyncio
from typing import Any, Coroutine, Optional
from kameleoon.network.network_manager import NetworkManager
from kameleoon.network.services.service import Service
from kameleoon.network.net_provider import Response, Request


class ServiceImpl(Service):
    __ATTEMP_LIMIT_EXCEEDED_LOG_MESSAGE = "Attempt limit exceeded"

    NUMBER_OF_RECONNECTION_ON_FAILURE = 2

    @property
    def network_manager(self):
        return self.__network_manager

    def __init__(self, network_manager: NetworkManager) -> None:
        super().__init__()
        self.__network_manager = network_manager

    async def _make_call(
        self, request: Request, try_access_token_auth: bool, retry_limit=0, retry_delay=0.0, sync=False
    ) -> Response:
        net_provider = self.__network_manager.net_provider
        access_token_source = self.__network_manager.access_token_source
        attempt = 0
        success = False
        if sync:
            retry_limit = 0
        while not success and (attempt <= retry_limit):
            if (attempt > 0) and (retry_delay > 0.0):
                await self._delay(retry_delay)
            if try_access_token_auth:
                token = await access_token_source.get_token(request.timeout, sync)
                request.authorize(token)
            response = await net_provider.run_request(request)
            if response.error is not None:
                self.__log_failure(request, self.__make_request_error_log_message(response.error))
            elif not response.is_expected_status_code:
                self.__log_failure(request, self.__make_unexpected_code_log_message(response.code))
                if request.access_token and (response.code == 401):
                    self.__log_token_rejection(request.access_token)
                    access_token_source.discard_token(request.access_token)
                    if attempt == retry_limit:
                        try_access_token_auth = False
                        retry_delay = 0.0
                        request.authorize(None)
                        attempt -= 1
            else:
                success = True
            attempt += 1
        if not success:
            self.__log_failure(request, self.__ATTEMP_LIMIT_EXCEEDED_LOG_MESSAGE)
        return response

    @staticmethod
    def _delay(period: float) -> Coroutine[Any, Any, None]:
        return asyncio.sleep(period)

    def __log_failure(self, request: Request, message: str):
        logger = self.network_manager.logger
        logger.error(f"{request.method.value} call '{request.url}' failed: {message}")

    @staticmethod
    def __make_request_error_log_message(err: Exception) -> str:
        return f"Exception occurred during request: {err}"

    @staticmethod
    def __make_unexpected_code_log_message(code: Optional[int]) -> str:
        return f"Received unexpected status code '{code}'"

    def __log_token_rejection(self, access_token: str) -> None:
        self.__network_manager.logger.error(f"Unexpected rejection of access token '{access_token}'")
