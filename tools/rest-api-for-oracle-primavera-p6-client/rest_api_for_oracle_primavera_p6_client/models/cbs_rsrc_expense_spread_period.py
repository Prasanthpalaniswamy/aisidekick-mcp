from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CBSRsrcExpenseSpreadPeriod")


@_attrs_define
class CBSRsrcExpenseSpreadPeriod:
    """
    Attributes:
        start_date (str | Unset):
        end_date (str | Unset):
        actual_cost (float | Unset):
        actual_units (float | Unset):
        at_completion_cost (float | Unset):
        at_completion_units (float | Unset):
        planned_cost (float | Unset):
        planned_units (float | Unset):
        remaining_cost (float | Unset):
        remaining_units (float | Unset):
    """

    start_date: str | Unset = UNSET
    end_date: str | Unset = UNSET
    actual_cost: float | Unset = UNSET
    actual_units: float | Unset = UNSET
    at_completion_cost: float | Unset = UNSET
    at_completion_units: float | Unset = UNSET
    planned_cost: float | Unset = UNSET
    planned_units: float | Unset = UNSET
    remaining_cost: float | Unset = UNSET
    remaining_units: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_date = self.start_date

        end_date = self.end_date

        actual_cost = self.actual_cost

        actual_units = self.actual_units

        at_completion_cost = self.at_completion_cost

        at_completion_units = self.at_completion_units

        planned_cost = self.planned_cost

        planned_units = self.planned_units

        remaining_cost = self.remaining_cost

        remaining_units = self.remaining_units

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_date is not UNSET:
            field_dict["StartDate"] = start_date
        if end_date is not UNSET:
            field_dict["EndDate"] = end_date
        if actual_cost is not UNSET:
            field_dict["ActualCost"] = actual_cost
        if actual_units is not UNSET:
            field_dict["ActualUnits"] = actual_units
        if at_completion_cost is not UNSET:
            field_dict["AtCompletionCost"] = at_completion_cost
        if at_completion_units is not UNSET:
            field_dict["AtCompletionUnits"] = at_completion_units
        if planned_cost is not UNSET:
            field_dict["PlannedCost"] = planned_cost
        if planned_units is not UNSET:
            field_dict["PlannedUnits"] = planned_units
        if remaining_cost is not UNSET:
            field_dict["RemainingCost"] = remaining_cost
        if remaining_units is not UNSET:
            field_dict["RemainingUnits"] = remaining_units

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_date = d.pop("StartDate", UNSET)

        end_date = d.pop("EndDate", UNSET)

        actual_cost = d.pop("ActualCost", UNSET)

        actual_units = d.pop("ActualUnits", UNSET)

        at_completion_cost = d.pop("AtCompletionCost", UNSET)

        at_completion_units = d.pop("AtCompletionUnits", UNSET)

        planned_cost = d.pop("PlannedCost", UNSET)

        planned_units = d.pop("PlannedUnits", UNSET)

        remaining_cost = d.pop("RemainingCost", UNSET)

        remaining_units = d.pop("RemainingUnits", UNSET)

        cbs_rsrc_expense_spread_period = cls(
            start_date=start_date,
            end_date=end_date,
            actual_cost=actual_cost,
            actual_units=actual_units,
            at_completion_cost=at_completion_cost,
            at_completion_units=at_completion_units,
            planned_cost=planned_cost,
            planned_units=planned_units,
            remaining_cost=remaining_cost,
            remaining_units=remaining_units,
        )

        cbs_rsrc_expense_spread_period.additional_properties = d
        return cbs_rsrc_expense_spread_period

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
