from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.standard_work_hours import StandardWorkHours


T = TypeVar("T", bound="StandardWorkWeek")


@_attrs_define
class StandardWorkWeek:
    """
    Attributes:
        standard_work_hours (list[StandardWorkHours] | Unset):
    """

    standard_work_hours: list[StandardWorkHours] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        standard_work_hours: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.standard_work_hours, Unset):
            standard_work_hours = []
            for standard_work_hours_item_data in self.standard_work_hours:
                standard_work_hours_item = standard_work_hours_item_data.to_dict()
                standard_work_hours.append(standard_work_hours_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if standard_work_hours is not UNSET:
            field_dict["StandardWorkHours"] = standard_work_hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.standard_work_hours import StandardWorkHours

        d = dict(src_dict)
        _standard_work_hours = d.pop("StandardWorkHours", UNSET)
        standard_work_hours: list[StandardWorkHours] | Unset = UNSET
        if _standard_work_hours is not UNSET:
            standard_work_hours = []
            for standard_work_hours_item_data in _standard_work_hours:
                standard_work_hours_item = StandardWorkHours.from_dict(standard_work_hours_item_data)

                standard_work_hours.append(standard_work_hours_item)

        standard_work_week = cls(
            standard_work_hours=standard_work_hours,
        )

        standard_work_week.additional_properties = d
        return standard_work_week

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
