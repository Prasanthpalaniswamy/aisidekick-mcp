from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.work_time import WorkTime


T = TypeVar("T", bound="StandardWorkHours")


@_attrs_define
class StandardWorkHours:
    """
    Attributes:
        day_of_week (str | Unset):
        work_time (list[WorkTime] | Unset):
    """

    day_of_week: str | Unset = UNSET
    work_time: list[WorkTime] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day_of_week = self.day_of_week

        work_time: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.work_time, Unset):
            work_time = []
            for work_time_item_data in self.work_time:
                work_time_item = work_time_item_data.to_dict()
                work_time.append(work_time_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if day_of_week is not UNSET:
            field_dict["DayOfWeek"] = day_of_week
        if work_time is not UNSET:
            field_dict["WorkTime"] = work_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.work_time import WorkTime

        d = dict(src_dict)
        day_of_week = d.pop("DayOfWeek", UNSET)

        _work_time = d.pop("WorkTime", UNSET)
        work_time: list[WorkTime] | Unset = UNSET
        if _work_time is not UNSET:
            work_time = []
            for work_time_item_data in _work_time:
                work_time_item = WorkTime.from_dict(work_time_item_data)

                work_time.append(work_time_item)

        standard_work_hours = cls(
            day_of_week=day_of_week,
            work_time=work_time,
        )

        standard_work_hours.additional_properties = d
        return standard_work_hours

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
