"""Page view visit"""
import time
from typing import Optional
from kameleoon.data import DataType
from kameleoon.data.data import BaseData
from kameleoon.data.page_view import PageView


class PageViewVisit(BaseData):
    """Page view visit"""
    def __init__(self, page_view: PageView, count=1, last_timestamp: Optional[int] = None) -> None:
        super().__init__()
        self.page_view = page_view
        self.count = count
        self.last_timestamp = last_timestamp or int(time.time() * 1000)

    def overwrite(self, new_page_view: PageView) -> None:
        self.page_view = new_page_view
        self.count += 1

    def merge(self, page_view_visit) -> None:
        self.count += page_view_visit.count
        self.last_timestamp = max(self.last_timestamp, page_view_visit.last_timestamp)

    def increase_page_visits(self) -> None:
        self.count += 1

    @property
    def data_type(self) -> DataType:
        return DataType.PAGE_VIEW_VISIT

    def __eq__(self, other: object) -> bool:
        return isinstance(other, PageViewVisit) and (other.page_view == self.page_view) and (
            other.count == self.count) and (other.last_timestamp == self.last_timestamp)
