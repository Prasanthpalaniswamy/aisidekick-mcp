from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_spread_period import ActivitySpreadPeriod


T = TypeVar("T", bound="ReadWBSSpreadResponse")


@_attrs_define
class ReadWBSSpreadResponse:
    """ReadWBSSpreadResponse Entity

    Attributes:
        activity_id (str | Unset):
        activity_object_id (int | Unset):
        start_date (str | Unset):
        end_date (str | Unset):
        period_type (str | Unset):
        period (list[ActivitySpreadPeriod] | Unset):
    """

    activity_id: str | Unset = UNSET
    activity_object_id: int | Unset = UNSET
    start_date: str | Unset = UNSET
    end_date: str | Unset = UNSET
    period_type: str | Unset = UNSET
    period: list[ActivitySpreadPeriod] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_id = self.activity_id

        activity_object_id = self.activity_object_id

        start_date = self.start_date

        end_date = self.end_date

        period_type = self.period_type

        period: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.period, Unset):
            period = []
            for period_item_data in self.period:
                period_item = period_item_data.to_dict()
                period.append(period_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity_id is not UNSET:
            field_dict["ActivityId"] = activity_id
        if activity_object_id is not UNSET:
            field_dict["ActivityObjectId"] = activity_object_id
        if start_date is not UNSET:
            field_dict["StartDate"] = start_date
        if end_date is not UNSET:
            field_dict["EndDate"] = end_date
        if period_type is not UNSET:
            field_dict["PeriodType"] = period_type
        if period is not UNSET:
            field_dict["Period"] = period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_spread_period import ActivitySpreadPeriod

        d = dict(src_dict)
        activity_id = d.pop("ActivityId", UNSET)

        activity_object_id = d.pop("ActivityObjectId", UNSET)

        start_date = d.pop("StartDate", UNSET)

        end_date = d.pop("EndDate", UNSET)

        period_type = d.pop("PeriodType", UNSET)

        _period = d.pop("Period", UNSET)
        period: list[ActivitySpreadPeriod] | Unset = UNSET
        if _period is not UNSET:
            period = []
            for period_item_data in _period:
                period_item = ActivitySpreadPeriod.from_dict(period_item_data)

                period.append(period_item)

        read_wbs_spread_response = cls(
            activity_id=activity_id,
            activity_object_id=activity_object_id,
            start_date=start_date,
            end_date=end_date,
            period_type=period_type,
            period=period,
        )

        read_wbs_spread_response.additional_properties = d
        return read_wbs_spread_response

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
