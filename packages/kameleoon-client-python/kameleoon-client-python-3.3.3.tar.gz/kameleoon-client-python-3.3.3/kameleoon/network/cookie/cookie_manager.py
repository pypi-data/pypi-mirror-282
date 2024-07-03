import datetime
from http.cookies import SimpleCookie, Morsel
from typing import Dict, Optional, Union
from kameleoon.helpers.visitor_code import generate_visitor_code, validate_visitor_code


COOKIE_KEY_JS = "_js_"
VISITOR_CODE_COOKIE = "kameleoonVisitorCode"
COOKIE_TTL = datetime.timedelta(days=380)
MAX_AGE = str(int(COOKIE_TTL.total_seconds()))


class CookieManager:
    _ENCODER: SimpleCookie[str] = SimpleCookie()

    def __init__(self, top_level_domain: str) -> None:
        self.__top_level_domain = top_level_domain
        self.consent_required = False

    def get_or_add(
        self,
        cookies_readonly: Optional[Dict[str, str]] = None,
        cookies: Optional[Dict[str, Morsel[str]]] = None,
        default_visitor_code: Optional[str] = None,
    ) -> str:
        visitor_code = self._get_visitor_code_from_cookies(cookies_readonly or cookies or {})
        if visitor_code is not None:
            validate_visitor_code(visitor_code)
            return visitor_code

        if default_visitor_code is None:
            visitor_code = generate_visitor_code()
            if not self.consent_required and cookies is not None:
                self._add(visitor_code, cookies)
            return visitor_code

        validate_visitor_code(default_visitor_code)
        visitor_code = default_visitor_code
        if cookies is not None:
            self._add(visitor_code, cookies)
        return visitor_code

    def update(self, visitor_code: str, consent: bool, cookies: Dict[str, Morsel[str]]) -> None:
        if consent:
            self._add(visitor_code, cookies)
        else:
            self._remove(cookies)

    def _add(self, visitor_code: str, cookies: Dict[str, Morsel[str]]) -> None:
        m: Morsel[str] = Morsel()
        m.set(VISITOR_CODE_COOKIE, *self._ENCODER.value_encode(visitor_code))
        m["domain"] = self.__top_level_domain
        m["path"] = "/"
        expires = datetime.datetime.utcnow() + COOKIE_TTL
        m["expires"] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
        m["max-age"] = MAX_AGE
        cookies[VISITOR_CODE_COOKIE] = m

    def _remove(self, cookies: Dict[str, Morsel[str]]) -> None:
        if self.consent_required:
            if m := cookies.get(VISITOR_CODE_COOKIE):
                m["domain"] = self.__top_level_domain
                m["path"] = "/"
                m["max-age"] = "0"

    @staticmethod
    def _get_visitor_code_from_cookies(cookies: Union[Dict[str, str], Dict[str, Morsel[str]]]) -> Optional[str]:
        visitor_code_cookie = cookies.get(VISITOR_CODE_COOKIE)
        if visitor_code_cookie:
            # SimpleCookie or request.COOKIES could be passed to the method, we should determine what exactly
            visitor_code = visitor_code_cookie if isinstance(visitor_code_cookie, str) else visitor_code_cookie.value
            if visitor_code.startswith(COOKIE_KEY_JS):
                visitor_code = visitor_code[len(COOKIE_KEY_JS) :]
            return visitor_code if visitor_code else None
        return None
