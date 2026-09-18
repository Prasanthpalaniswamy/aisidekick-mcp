from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetDetailedWorkHours")


@_attrs_define
class SetDetailedWorkHours:
    """SetDetailedWorkHours Entity

    Attributes:
        calendar_object_id (int | Unset): The unique identifier for the calendar object.
        date (datetime.datetime | Unset): Date on which detailed work hours will be set.
        detailed_work_hours (str | Unset): The detailed work hours to set for the specified date.
    """

    calendar_object_id: int | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    detailed_work_hours: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        calendar_object_id = self.calendar_object_id

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        detailed_work_hours = self.detailed_work_hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if calendar_object_id is not UNSET:
            field_dict["CalendarObjectId"] = calendar_object_id
        if date is not UNSET:
            field_dict["Date"] = date
        if detailed_work_hours is not UNSET:
            field_dict["DetailedWorkHours"] = detailed_work_hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        calendar_object_id = d.pop("CalendarObjectId", UNSET)

        _date = d.pop("Date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        detailed_work_hours = d.pop("DetailedWorkHours", UNSET)

        set_detailed_work_hours = cls(
            calendar_object_id=calendar_object_id,
            date=date,
            detailed_work_hours=detailed_work_hours,
        )

        set_detailed_work_hours.additional_properties = d
        return set_detailed_work_hours

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
