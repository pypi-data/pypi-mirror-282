from kameleoon.network.sendable import DuplicationUnsafeSendableBase
from kameleoon.network.query_builder import QueryBuilder, QueryParam, QueryParams


class ActivityEvent(DuplicationUnsafeSendableBase):
    EVENT_TYPE = "activity"

    def __init__(self) -> None:
        super().__init__()

    def _add_query_params(self, qb: QueryBuilder) -> None:
        qb.append(QueryParam(QueryParams.EVENT_TYPE, self.EVENT_TYPE))
