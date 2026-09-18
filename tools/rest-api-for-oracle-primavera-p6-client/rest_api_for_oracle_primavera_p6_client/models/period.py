from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Period")


@_attrs_define
class Period:
    """
    Attributes:
        start_date (datetime.datetime | Unset): The start of the time period that you are interested in.
        planned_units (float | Unset): The planned units of work for the resource assignment on the activity. This field
            is named BudgetedUnits in Primavera's Engineering & Construction and Maintenance & Turnaround solutions.
        remaining_units (float | Unset): The remaining units of work to be performed by this resource on this activity.
            Before the activity is started, the remaining units are the same as the planned units. After the activity is
            completed, the remaining units are zero.
    """

    start_date: datetime.datetime | Unset = UNSET
    planned_units: float | Unset = UNSET
    remaining_units: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        planned_units = self.planned_units

        remaining_units = self.remaining_units

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_date is not UNSET:
            field_dict["StartDate"] = start_date
        if planned_units is not UNSET:
            field_dict["PlannedUnits"] = planned_units
        if remaining_units is not UNSET:
            field_dict["RemainingUnits"] = remaining_units

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _start_date = d.pop("StartDate", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        planned_units = d.pop("PlannedUnits", UNSET)

        remaining_units = d.pop("RemainingUnits", UNSET)

        period = cls(
            start_date=start_date,
            planned_units=planned_units,
            remaining_units=remaining_units,
        )

        period.additional_properties = d
        return period

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
