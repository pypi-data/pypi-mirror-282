from typing import Optional, Any, List

from kameleoon.data.data import BaseData
from kameleoon.data import Data
from kameleoon.network.net_provider import Response
from logging import Logger

from kameleoon.network.services.data_service import DataService
from kameleoon.data.manager.visitor_manager import VisitorManager
from kameleoon.network.network_manager import NetworkManager
from kameleoon.managers.remote_data.remote_visitor_data import RemoteVisitorData
from kameleoon.types.remote_visitor_data_filter import RemoteVisitorDataFilter


class RemoteDataManager:

    def __init__(
        self, network_manager: NetworkManager, visitor_manager: VisitorManager, logger: Optional[Logger] = None
    ) -> None:
        self._network_manager = network_manager
        self._visitor_manager = visitor_manager
        self._logger = logger

    async def get_data(self, key: str, timeout: Optional[float] = None, sync_mode=False) -> Optional[Any]:
        service: DataService = self._network_manager.get_service(DataService)
        response = await service.get_remote_data(key, timeout, sync_mode)
        return response.content

    async def get_visitor_data(
        self,
        visitor_code: str,
        add_data: bool = True,
        data_filter: Optional[RemoteVisitorDataFilter] = None,
        is_unique_identifier: bool = False,
        sync_mode=False,
        timeout: Optional[float] = None,
    ) -> List[Data]:
        # TODO: Uncomment with the next major update
        # validate_visitor_code(visitor_code)
        if data_filter is None:
            data_filter = RemoteVisitorDataFilter()
        service: DataService = self._network_manager.get_service(DataService)
        response = await service.get_remote_visitor_data(visitor_code, data_filter, is_unique_identifier, timeout,
                                                         sync_mode)
        return self.__handle_remote_visitor_data_response(response, visitor_code, add_data)

    def __handle_remote_visitor_data_response(
        self, response: Response, visitor_code: str, add_data: bool
    ) -> List[Data]:
        if response.content is None:
            return []
        data_to_add, data_to_return = self.__parse_remote_visitor_data(response.content)
        if add_data and data_to_add:
            visitor = self._visitor_manager.get_or_create_visitor(visitor_code)
            visitor.add_data(*data_to_add, overwrite=False, logger=self._logger)
        return data_to_return

    def __parse_remote_visitor_data(self, raw: Any) -> tuple[List[BaseData], List[Data]]:
        try:
            remote_visitor_data = RemoteVisitorData(raw)
            remote_visitor_data.mark_data_as_sent(self._visitor_manager.custom_data_info)
            return remote_visitor_data.collect_data_to_add(), remote_visitor_data.collect_data_to_return()
        except Exception as ex:  # pylint: disable=W0703
            if self._logger:
                self._logger.error(f"Parsing of visitor data failed: {ex}")
            return [], []
