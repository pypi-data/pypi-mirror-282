from typing import Optional
import kameleoon.helpers.nonce as nonce
from kameleoon.network.query_encodable import QueryEncodable
from kameleoon.network.query_builder import QueryBuilder, QueryParam, QueryParams


class Sendable(QueryEncodable):
    def __init__(self) -> None:
        super().__init__()
        self._nonce: Optional[str] = None
        self._sent = False

    @property
    def nonce(self) -> str:
        raise NotImplementedError

    @property
    def sent(self) -> bool:
        return self._sent

    def mark_as_sent(self) -> None:
        self._sent = True
        self._nonce = None

    def encode_query(self) -> str:
        qb = QueryBuilder(QueryParam(QueryParams.NONCE, self.nonce))
        self._add_query_params(qb)
        return str(qb)

    def _add_query_params(self, qb: QueryBuilder) -> None:
        pass


class DuplicationSafeSendableBase(Sendable):
    def __init__(self) -> None:
        super().__init__()
        self._nonce = nonce.get_nonce()

    @property
    def nonce(self) -> str:
        return self._nonce or ""


class DuplicationUnsafeSendableBase(Sendable):
    @property
    def nonce(self) -> str:
        if (self._nonce is None) and not self._sent:
            self._nonce = nonce.get_nonce()
        return self._nonce or ""
