"""Variable"""
from typing import Any, Optional


class Variable:
    """Variable"""

    def __init__(self, key: str, type: str, value: Optional[Any]):
        self.__key = key
        self.__type = type
        self.__value = value

    @property
    def key(self) -> str:
        """Return key"""
        return self.__key

    @property
    def type(self) -> str:
        """Return type"""
        return self.__type

    @property
    def value(self) -> Optional[Any]:
        """Return value"""
        return self.__value
