import aiohttp
import asyncio
import threading
from typing import Dict
from kameleoon.network.net_provider import NetProvider, ResponseContentType, Response, Request


class NetProviderImpl(NetProvider):
    __SESSIONS_PURGE_TRIGGER_THRESHOLD = 8
    _H_AUTHORIZATION = "Authorization"

    def __init__(self) -> None:
        self.__sessions: Dict[asyncio.AbstractEventLoop, aiohttp.ClientSession] = {}
        self.__sessions_lock = threading.Lock()

    @property
    async def _session(self) -> aiohttp.ClientSession:
        loop = asyncio.get_running_loop()
        s = self.__sessions.get(loop)
        if s is None:
            with self.__sessions_lock:
                s = self.__sessions.get(loop)
                if s is None:
                    if len(self.__sessions) > self.__SESSIONS_PURGE_TRIGGER_THRESHOLD:
                        await self.__purge_sessions()
                    s = aiohttp.ClientSession()
                    self.__sessions[loop] = s
        return s

    async def __purge_sessions(self) -> None:
        for loop, s in list(self.__sessions.items()):
            if loop.is_closed():
                await s.close()
                del self.__sessions[loop]

    async def close(self) -> None:
        with self.__sessions_lock:
            await asyncio.gather(*(s.close() for s in self.__sessions.values()))

    async def run_request(self, request: Request) -> Response:
        try:
            s = await self._session
            headers = self._collect_headers(request)
            async with await s.request(
                request.method.value, request.url, headers=headers, timeout=request.timeout, data=request.body
            ) as resp:
                response = await self.__form_response(resp, request.response_content_type)
                resp.close()
                return response
        except KeyError as e:
            raise e
        except Exception as err:
            return Response(err, None, None)

    @staticmethod
    def _collect_headers(request: Request) -> Dict[str, str]:
        headers = {}
        if request.headers:
            headers.update(request.headers)
        if request.access_token:
            headers[NetProviderImpl._H_AUTHORIZATION] = f"Bearer {request.access_token}"
        return headers

    @staticmethod
    async def __form_response(resp, response_content_type: ResponseContentType) -> Response:
        try:
            if response_content_type == ResponseContentType.TEXT:
                content = await resp.text()
            elif response_content_type == ResponseContentType.JSON:
                content = await resp.json()
            else:
                content = None
        except aiohttp.ContentTypeError:
            content = None
        return Response(None, resp.status, content)
