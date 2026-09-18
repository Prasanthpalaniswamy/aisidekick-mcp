from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteProjectResourceQuantities")


@_attrs_define
class DeleteProjectResourceQuantities:
    """DeleteProjectResourceQuantities Entity

    Attributes:
        project_resource_object_id (int | Unset):
        week_start_date (datetime.datetime | Unset):
        month_start_date (datetime.datetime | Unset):
    """

    project_resource_object_id: int | Unset = UNSET
    week_start_date: datetime.datetime | Unset = UNSET
    month_start_date: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_resource_object_id = self.project_resource_object_id

        week_start_date: str | Unset = UNSET
        if not isinstance(self.week_start_date, Unset):
            week_start_date = self.week_start_date.isoformat()

        month_start_date: str | Unset = UNSET
        if not isinstance(self.month_start_date, Unset):
            month_start_date = self.month_start_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_resource_object_id is not UNSET:
            field_dict["ProjectResourceObjectId"] = project_resource_object_id
        if week_start_date is not UNSET:
            field_dict["WeekStartDate"] = week_start_date
        if month_start_date is not UNSET:
            field_dict["MonthStartDate"] = month_start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_resource_object_id = d.pop("ProjectResourceObjectId", UNSET)

        _week_start_date = d.pop("WeekStartDate", UNSET)
        week_start_date: datetime.datetime | Unset
        if isinstance(_week_start_date, Unset):
            week_start_date = UNSET
        else:
            week_start_date = isoparse(_week_start_date)

        _month_start_date = d.pop("MonthStartDate", UNSET)
        month_start_date: datetime.datetime | Unset
        if isinstance(_month_start_date, Unset):
            month_start_date = UNSET
        else:
            month_start_date = isoparse(_month_start_date)

        delete_project_resource_quantities = cls(
            project_resource_object_id=project_resource_object_id,
            week_start_date=week_start_date,
            month_start_date=month_start_date,
        )

        delete_project_resource_quantities.additional_properties = d
        return delete_project_resource_quantities

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
