import time
from typing import Optional
from kameleoon.configuration.rule_type import RuleType
from kameleoon.data.data import BaseData, DataType
from kameleoon.network.sendable import DuplicationUnsafeSendableBase
from kameleoon.network.query_builder import QueryBuilder, QueryParam, QueryParams


class AssignedVariation(BaseData, DuplicationUnsafeSendableBase):
    EVENT_TYPE = "experiment"

    def __init__(
        self,
        experiment_id: int,
        variation_id: int,
        rule_type: RuleType = RuleType.UNKNOWN,
        assignment_time: Optional[float] = None,
    ) -> None:
        super().__init__()
        self.__experiment_id = experiment_id
        self.__variation_id = variation_id
        self.__rule_type = rule_type
        self.__assignment_time = assignment_time or time.time()

    @property
    def experiment_id(self) -> int:
        return self.__experiment_id

    @property
    def variation_id(self) -> int:
        return self.__variation_id

    @property
    def rule_type(self) -> RuleType:
        return self.__rule_type

    @property
    def assignment_time(self) -> float:
        return self.__assignment_time

    @property
    def data_type(self) -> DataType:
        return DataType.ASSIGNED_VARIATION

    def _add_query_params(self, qb: QueryBuilder) -> None:
        # fmt: off
        qb.extend(
            QueryParam(QueryParams.EVENT_TYPE, self.EVENT_TYPE),
            QueryParam(QueryParams.EXPERIMENT_ID, str(self.__experiment_id)),
            QueryParam(QueryParams.VARIATION_ID, str(self.__variation_id)),
        )
        # fmt: on

    def is_valid(self, respool_time: Optional[int]) -> bool:
        return (respool_time is None) or (self.assignment_time >= respool_time)
