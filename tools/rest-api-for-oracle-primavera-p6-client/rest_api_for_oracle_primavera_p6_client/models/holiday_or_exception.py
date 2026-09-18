from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.work_time import WorkTime


T = TypeVar("T", bound="HolidayOrException")


@_attrs_define
class HolidayOrException:
    """
    Attributes:
        date (datetime.datetime | Unset):
        work_time (list[WorkTime] | Unset):
    """

    date: datetime.datetime | Unset = UNSET
    work_time: list[WorkTime] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        work_time: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.work_time, Unset):
            work_time = []
            for work_time_item_data in self.work_time:
                work_time_item = work_time_item_data.to_dict()
                work_time.append(work_time_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["Date"] = date
        if work_time is not UNSET:
            field_dict["WorkTime"] = work_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.work_time import WorkTime

        d = dict(src_dict)
        _date = d.pop("Date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        _work_time = d.pop("WorkTime", UNSET)
        work_time: list[WorkTime] | Unset = UNSET
        if _work_time is not UNSET:
            work_time = []
            for work_time_item_data in _work_time:
                work_time_item = WorkTime.from_dict(work_time_item_data)

                work_time.append(work_time_item)

        holiday_or_exception = cls(
            date=date,
            work_time=work_time,
        )

        holiday_or_exception.additional_properties = d
        return holiday_or_exception

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
