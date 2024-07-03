import asyncio
import time
from logging import Logger
from typing import Optional
from kameleoon.network.services.automation_service import AutomationService


class AccessTokenSource:
    _TOKEN_EXPIRATION_GAP = 60.0  # in seconds
    _TOKEN_OBSOLESCENCE_GAP = 1800.0  # in seconds
    _JWT_ACCESS_TOKEN_FIELD = "access_token"
    _JWT_EXPIRES_IN_FIELD = "expires_in"

    def __init__(self, network_manager, client_id: str, client_secret: str, logger: Optional[Logger] = None) -> None:
        self._network_manager = network_manager
        self._client_id = client_id
        self._client_secret = client_secret
        self._logger = logger
        self._cached_token: Optional[AccessTokenSource.ExpiringToken] = None
        self._fetching = False

    async def get_token(self, timeout: Optional[float] = None, sync=False) -> Optional[str]:
        now = time.time()
        token = self._cached_token
        if (token is None) or token.is_expired(now):
            return await self._call_fetch_token(timeout)
        if not self._fetching and token.is_obsolete(now) and not sync:
            self._run_fetch_token()
        return token.value

    def discard_token(self, token: str) -> None:
        cached_token = self._cached_token
        if cached_token and (cached_token.value == token):
            self._cached_token = None

    async def _call_fetch_token(self, timeout: Optional[float]) -> Optional[str]:
        try:
            self._fetching = True
            return await self._fetch_token(timeout)
        except Exception as e:
            self._log_error(f"Failed to call access token fetching: {e}")
            self._fetching = False
            return None

    def _run_fetch_token(self) -> None:
        try:
            self._fetching = True
            asyncio.create_task(self._fetch_token())
        except Exception as e:
            self._log_error(f"Failed to run access token fetching: {e}")
            self._fetching = False

    async def _fetch_token(self, timeout: Optional[float] = None) -> Optional[str]:
        try:
            service: AutomationService = self._network_manager.get_service(AutomationService)
            response = await service.fetch_access_jwtoken(self._client_id, self._client_secret, timeout)
            if not response.success:
                self._log_error("Failed to fetch access JWT")
                return None
            if not isinstance(response.content, dict):
                self._log_error("Failed to obtain proper access JWT")
                return None
            try:
                jwt = response.content
                token = jwt[self._JWT_ACCESS_TOKEN_FIELD]
                expires_in = jwt[self._JWT_EXPIRES_IN_FIELD]
            except Exception as e:
                self._log_error(f"Failed to parse access JWT: {e}")
                return None
            if not (isinstance(token, str) and token and isinstance(expires_in, int) and expires_in):
                self._log_error("Failed to read access JWT")
                return None
            self._handle_fetched_token(token, expires_in)
            return token
        finally:
            self._fetching = False

    def _handle_fetched_token(self, token: str, expires_in: int) -> None:
        now = time.time()
        exp_time = now + expires_in - self._TOKEN_EXPIRATION_GAP
        if expires_in > self._TOKEN_OBSOLESCENCE_GAP:
            obs_time = now + expires_in - self._TOKEN_OBSOLESCENCE_GAP
        else:
            obs_time = exp_time
            if self._logger:
                if expires_in <= self._TOKEN_EXPIRATION_GAP:
                    issue = "cache the token"
                else:
                    issue = "refresh cached token in background"
                self._logger.warning(f"Access token life time ({expires_in}s) is not long enough to {issue}")
        self._cached_token = self.ExpiringToken(token, exp_time, obs_time)

    def _log_error(self, message: str) -> None:
        if self._logger:
            self._logger.error(message)

    class ExpiringToken:
        def __init__(self, value: str, expiration_time: float, obsolescence_time: float) -> None:
            self.value = value
            self.expiration_time = expiration_time
            self.obsolescence_time = obsolescence_time

        def is_expired(self, now: float) -> bool:
            return now >= self.expiration_time

        def is_obsolete(self, now: float) -> bool:
            return now >= self.obsolescence_time
