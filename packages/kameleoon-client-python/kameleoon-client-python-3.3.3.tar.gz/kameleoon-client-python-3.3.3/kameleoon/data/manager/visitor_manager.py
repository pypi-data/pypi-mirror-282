import collections
import time
from typing import Dict, Iterator, Optional
from logging import Logger
from kameleoon.data import CustomData
from kameleoon.configuration.custom_data_info import CustomDataInfo
from kameleoon.data.manager.visitor import Visitor
from kameleoon.data.manager.visitor_slot import VisitorSlot
from kameleoon.helpers.scheduler import Scheduler


class VisitorManager:

    def __init__(self, expiration_period: float, scheduler: Scheduler) -> None:
        self.__expiration_period = expiration_period
        self._slots: Dict[str, VisitorSlot] = collections.defaultdict(VisitorSlot)
        self.custom_data_info: Optional[CustomDataInfo] = None
        scheduler.schedule_job("VisitorManager.purge", expiration_period, self.__purge)

    def __iter__(self) -> Iterator[str]:
        yield from list(self._slots)

    def __len__(self) -> int:
        return len(self._slots)

    def get_visitor(self, visitor_code: str) -> Optional[Visitor]:
        if (slot := self.__try_acquire_slot(visitor_code)) is None:
            return None
        try:
            if slot.visitor is not None:
                slot.update_last_activity_time()
            return slot.visitor
        finally:
            slot.lock.release()

    def get_or_create_visitor(self, visitor_code: str) -> Visitor:
        slot = self.__acquire_slot(visitor_code)
        try:
            if slot.visitor is None:
                slot.visitor = Visitor()
            else:
                slot.update_last_activity_time()
            return slot.visitor
        finally:
            slot.lock.release()

    def add_data(self, visitor_code: str, *args, logger: Optional[Logger] = None):
        visitor = self.get_or_create_visitor(visitor_code)
        for custom_data in args:
            if not isinstance(custom_data, CustomData):
                continue
            # We shouldn't send custom data with local only type
            if self.custom_data_info and self.custom_data_info.is_local_only(custom_data.id):
                custom_data.mark_as_sent()
            # If mappingIdentifier is passed, we should link anonymous visitor with real unique userId.
            # After authorization, customer must be able to continue work with userId, but hash for variation
            # should be calculated based on anonymous visitor code, that's why set MappingIdentifier to visitor.
            if (
                self.custom_data_info is not None
                and self.custom_data_info.is_mapping_identifier(custom_data.id)
                and len(custom_data.values) > 0
                and len(custom_data.values[0]) > 0
            ):
                custom_data.is_mapping_identifier = True
                visitor._mapping_identifier = visitor_code
                target_visitor_code = custom_data.values[0]
                if visitor_code != target_visitor_code:
                    slot = self.__acquire_slot(target_visitor_code)
                    try:
                        slot.visitor = visitor
                    finally:
                        slot.lock.release()
        visitor.add_data(*args, logger=logger)
        return visitor

    def __purge(self) -> None:
        expired_time = time.time() - self.__expiration_period
        for visitor_code in list(self._slots):
            if slot := self.__try_acquire_slot_once(visitor_code):
                try:
                    if (slot.visitor is None) or (slot.last_activity_time < expired_time):
                        self._slots.pop(visitor_code, None)
                finally:
                    slot.lock.release()

    def __acquire_slot(self, visitor_code: str) -> VisitorSlot:
        while True:
            slot = self._slots[visitor_code]
            slot.lock.acquire()
            if slot == self._slots.get(visitor_code):
                return slot
            slot.lock.release()

    def __try_acquire_slot(self, visitor_code: str) -> Optional[VisitorSlot]:
        while True:
            slot = self._slots.get(visitor_code)
            if slot is None:
                return None
            slot.lock.acquire()
            if slot == self._slots.get(visitor_code):
                return slot
            slot.lock.release()

    def __try_acquire_slot_once(self, visitor_code: str) -> Optional[VisitorSlot]:
        slot = self._slots.get(visitor_code)
        if slot is None:
            return None
        slot.lock.acquire()
        if slot == self._slots.get(visitor_code):
            return slot
        slot.lock.release()
        return None
