from enum import Enum
from typing import Any, Coroutine, Dict, Optional


class ResponseContentType(Enum):
    NONE = 0
    TEXT = 1
    JSON = 2


class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"


class Response:
    def __init__(self, error: Optional[Exception], code: Optional[int], content: Optional[Any]):
        self.error = error
        self.code = code
        self.content = content

    @property
    def success(self) -> bool:
        return (self.error is None) and self.is_expected_status_code

    @property
    def is_expected_status_code(self) -> bool:
        return (self.code is not None) and ((self.code // 100 == 2) or (self.code == 403))


class Request:
    def __init__(
        self, method: HttpMethod, url: str, timeout: float,
        headers: Optional[Dict[str, str]] = None, body: Optional[str] = None,
        response_content_type=ResponseContentType.NONE,
    ) -> None:
        self.method = method
        self.url = url
        self.timeout = timeout
        self.headers = headers
        self.body = body
        self.response_content_type = response_content_type
        self.access_token: Optional[str] = None

    def authorize(self, access_token: Optional[str]) -> None:
        self.access_token = access_token


class NetProvider:
    def close(self) -> Coroutine[Any, Any, None]:
        raise NotImplementedError()

    def run_request(self, request: Request) -> Coroutine[Any, Any, Response]:
        raise NotImplementedError()
