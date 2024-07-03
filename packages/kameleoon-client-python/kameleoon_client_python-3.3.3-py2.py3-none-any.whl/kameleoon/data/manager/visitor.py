from threading import Lock
from typing import Any, Callable, Optional, Dict, List, Iterator, cast

from logging import Logger
from kameleoon.data.visitor_visits import VisitorVisits
from kameleoon.data.data import Data
from kameleoon.data.browser import Browser
from kameleoon.data.conversion import Conversion
from kameleoon.data.cookie import Cookie
from kameleoon.data.custom_data import CustomData
from kameleoon.data.device import Device
from kameleoon.data.geolocation import Geolocation
from kameleoon.data.kcs_heat import KcsHeat
from kameleoon.data.operating_system import OperatingSystem
from kameleoon.data.page_view import PageView
from kameleoon.data.user_agent import UserAgent
from kameleoon.data.manager.assigned_variation import AssignedVariation
from kameleoon.data.manager.page_view_visit import PageViewVisit
from kameleoon.network.sendable import Sendable


EMPTY_DICT: Dict[Any, Any] = {}
EMPTY_LIST: List[Any] = []


class Visitor:
    def __init__(self) -> None:
        self._lock = Lock()
        self._user_agent: Optional[str] = None
        self._device: Optional[Device] = None
        self._browser: Optional[Browser] = None
        self._geolocation: Optional[Geolocation] = None
        self._operating_system: Optional[OperatingSystem] = None
        self._cookie: Optional[Cookie] = None
        self._custom_data_dict: Optional[Dict[int, CustomData]] = None
        self._page_view_visits: Optional[Dict[str, PageViewVisit]] = None
        self._conversions: Optional[List[Conversion]] = None
        self._variations: Optional[Dict[int, AssignedVariation]] = None
        self._kcs_heat: Optional[KcsHeat] = None
        self._visitor_visits: Optional[VisitorVisits] = None
        self._mapping_identifier: Optional[str] = None
        self.legal_consent = False

    def enumerate_sendable_data(self) -> Iterator[Sendable]:
        if self._device:
            yield self._device
        if self._browser:
            yield self._browser
        if self._geolocation:
            yield self._geolocation
        if self._operating_system:
            yield self._operating_system
        if self._custom_data_dict is not None:
            yield from list(self._custom_data_dict.values())
        if self._page_view_visits is not None:
            yield from (visit.page_view for visit in list(self._page_view_visits.values()))
        if self._conversions is not None:
            yield from list(self._conversions)
        if self._variations is not None:
            yield from list(self._variations.values())

    def count_sendable_data(self) -> int:
        count = 0
        if self._device is not None:
            count += 1
        if self._browser is not None:
            count += 1
        if self._geolocation is not None:
            count += 1
        if self._operating_system is not None:
            count += 1
        if self._custom_data_dict is not None:
            count += len(self._custom_data_dict)
        if self._page_view_visits is not None:
            count += len(self._page_view_visits)
        if self._conversions is not None:
            count += len(self._conversions)
        if self._variations is not None:
            count += len(self._variations)
        return count

    @property
    def user_agent(self) -> Optional[str]:
        return self._user_agent

    @property
    def device(self) -> Optional[Device]:
        return self._device

    @property
    def browser(self) -> Optional[Browser]:
        return self._browser

    @property
    def geolocation(self) -> Optional[Geolocation]:
        return self._geolocation

    @property
    def operating_system(self) -> Optional[OperatingSystem]:
        return self._operating_system

    @property
    def cookie(self) -> Optional[Cookie]:
        return self._cookie

    @property
    def custom_data(self) -> Dict[int, CustomData]:
        return EMPTY_DICT if self._custom_data_dict is None else self._custom_data_dict.copy()

    @property
    def page_view_visits(self) -> Dict[str, PageViewVisit]:
        return EMPTY_DICT if self._page_view_visits is None else self._page_view_visits.copy()

    @property
    def conversions(self) -> List[Conversion]:
        return EMPTY_LIST if self._conversions is None else self._conversions.copy()

    @property
    def variations(self) -> Dict[int, AssignedVariation]:
        return EMPTY_DICT if self._variations is None else self._variations.copy()

    @property
    def kcs_heat(self) -> Optional[KcsHeat]:
        return self._kcs_heat

    @property
    def visitor_visits(self) -> Optional[VisitorVisits]:
        return self._visitor_visits

    def assign_variation(self, variation: AssignedVariation) -> None:
        if self._variations is None:
            with self._lock:
                if self._variations is None:
                    self._variations = {variation.experiment_id: variation}
                    return
        self._variations[variation.experiment_id] = variation

    def add_data(self, *args, overwrite: bool = True, logger: Optional[Logger] = None) -> None:
        with self._lock:
            for data in args:
                data_type = type(data)
                data_adder = DATA_ADDERS.get(data_type)
                if data_adder:
                    data_adder(self.DataAddingContext(self, data, overwrite, logger))
                elif logger:
                    logger.error(f"Data has unsupported type '{data_type}'")

    @property
    def mapping_identifier(self):
        return self._mapping_identifier

    class DataAddingContext:
        def __init__(
            self, visitor: "Visitor", data: Data, overwrite: bool = True, logger: Optional[Logger] = None
        ) -> None:
            self.visitor = visitor
            self.data = data
            self.overwrite = overwrite
            self.logger = logger

    @staticmethod
    def _set_user_agent(c: DataAddingContext) -> None:
        c.visitor._user_agent = cast(UserAgent, c.data).value

    @staticmethod
    def _set_device(c: DataAddingContext) -> None:
        if c.overwrite or c.visitor._device is None:
            c.visitor._device = cast(Device, c.data)

    @staticmethod
    def _add_variation(c: DataAddingContext) -> None:
        variation = cast(AssignedVariation, c.data)
        if c.visitor._variations is None:
            c.visitor._variations = {}
        if c.overwrite or variation.experiment_id not in c.visitor.variations:
            c.visitor._variations[variation.experiment_id] = variation

    @staticmethod
    def _set_browser(c: DataAddingContext) -> None:
        if c.overwrite or c.visitor._browser is None:
            c.visitor._browser = cast(Browser, c.data)

    @staticmethod
    def _set_geolocation(c: DataAddingContext) -> None:
        if c.overwrite or c.visitor._geolocation is None:
            c.visitor._geolocation = cast(Geolocation, c.data)

    @staticmethod
    def _set_operating_system(c: DataAddingContext) -> None:
        if c.overwrite or c.visitor._operating_system is None:
            c.visitor._operating_system = cast(OperatingSystem, c.data)

    @staticmethod
    def _set_cookie(c: DataAddingContext) -> None:
        c.visitor._cookie = cast(Cookie, c.data)

    @staticmethod
    def _add_custom_data(c: DataAddingContext) -> None:
        custom_data = cast(CustomData, c.data)
        if c.visitor._custom_data_dict is None:
            c.visitor._custom_data_dict = {}
        if c.overwrite or custom_data.id not in c.visitor._custom_data_dict:
            c.visitor._custom_data_dict[custom_data.id] = custom_data

    @staticmethod
    def _add_page_view(c: DataAddingContext) -> None:
        page_view = cast(PageView, c.data)
        if len(page_view.url) == 0:
            if c.logger:
                c.logger.error("Passed PageView data is invalid because of empty 'url' field; the data was ignored.")
            return
        if c.visitor._page_view_visits is None:
            c.visitor._page_view_visits = {page_view.url: PageViewVisit(page_view)}
        else:
            if visit := c.visitor._page_view_visits.get(page_view.url):
                visit.overwrite(page_view)
            else:
                c.visitor._page_view_visits[page_view.url] = PageViewVisit(page_view)

    @staticmethod
    def _add_page_view_visit(c: DataAddingContext) -> None:
        page_view_visit = cast(PageViewVisit, c.data)
        if c.visitor._page_view_visits is None:
            c.visitor._page_view_visits = {}
        if visit := c.visitor._page_view_visits.get(page_view_visit.page_view.url):
            visit.merge(page_view_visit)
        else:
            c.visitor._page_view_visits[page_view_visit.page_view.url] = page_view_visit

    @staticmethod
    def _add_conversion(c: DataAddingContext) -> None:
        conversion = cast(Conversion, c.data)
        if c.visitor._conversions is None:
            c.visitor._conversions = [conversion]
        else:
            c.visitor._conversions.append(conversion)

    @staticmethod
    def _set_kcs_heat(c: DataAddingContext) -> None:
        c.visitor._kcs_heat = cast(KcsHeat, c.data)

    @staticmethod
    def _set_visitor_visits(c: DataAddingContext) -> None:
        c.visitor._visitor_visits = cast(VisitorVisits, c.data)


DATA_ADDERS: Dict[type, Callable[[Visitor.DataAddingContext], None]] = {
    UserAgent: Visitor._set_user_agent,
    Device: Visitor._set_device,
    Browser: Visitor._set_browser,
    Geolocation: Visitor._set_geolocation,
    OperatingSystem: Visitor._set_operating_system,
    Cookie: Visitor._set_cookie,
    CustomData: Visitor._add_custom_data,
    PageView: Visitor._add_page_view,
    PageViewVisit: Visitor._add_page_view_visit,
    Conversion: Visitor._add_conversion,
    KcsHeat: Visitor._set_kcs_heat,
    VisitorVisits: Visitor._set_visitor_visits,
    AssignedVariation: Visitor._add_variation,
}
