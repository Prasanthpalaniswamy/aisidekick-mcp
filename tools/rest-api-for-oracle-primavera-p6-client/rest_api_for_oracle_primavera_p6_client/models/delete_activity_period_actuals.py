from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteActivityPeriodActuals")


@_attrs_define
class DeleteActivityPeriodActuals:
    """DeleteActivityPeriodActuals Entity

    Attributes:
        financial_period_object_id (int | Unset):
        activity_object_id (int | Unset):
    """

    financial_period_object_id: int | Unset = UNSET
    activity_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        financial_period_object_id = self.financial_period_object_id

        activity_object_id = self.activity_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if financial_period_object_id is not UNSET:
            field_dict["FinancialPeriodObjectId"] = financial_period_object_id
        if activity_object_id is not UNSET:
            field_dict["ActivityObjectId"] = activity_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        financial_period_object_id = d.pop("FinancialPeriodObjectId", UNSET)

        activity_object_id = d.pop("ActivityObjectId", UNSET)

        delete_activity_period_actuals = cls(
            financial_period_object_id=financial_period_object_id,
            activity_object_id=activity_object_id,
        )

        delete_activity_period_actuals.additional_properties = d
        return delete_activity_period_actuals

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
