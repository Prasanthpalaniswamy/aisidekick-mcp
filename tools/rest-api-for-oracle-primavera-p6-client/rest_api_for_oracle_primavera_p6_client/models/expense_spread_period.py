from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExpenseSpreadPeriod")


@_attrs_define
class ExpenseSpreadPeriod:
    """
    Attributes:
        start_date (str | Unset):
        end_date (str | Unset):
        financial_period_object_id (int | Unset):
        actual_cost (float | Unset):
        at_completion_cost (float | Unset):
        planned_cost (float | Unset):
        remaining_cost (float | Unset):
        cumulative_actual_cost (float | Unset):
        cumulative_at_completion_cost (float | Unset):
        cumulative_planned_cost (float | Unset):
        cumulative_remaining_cost (float | Unset):
    """

    start_date: str | Unset = UNSET
    end_date: str | Unset = UNSET
    financial_period_object_id: int | Unset = UNSET
    actual_cost: float | Unset = UNSET
    at_completion_cost: float | Unset = UNSET
    planned_cost: float | Unset = UNSET
    remaining_cost: float | Unset = UNSET
    cumulative_actual_cost: float | Unset = UNSET
    cumulative_at_completion_cost: float | Unset = UNSET
    cumulative_planned_cost: float | Unset = UNSET
    cumulative_remaining_cost: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_date = self.start_date

        end_date = self.end_date

        financial_period_object_id = self.financial_period_object_id

        actual_cost = self.actual_cost

        at_completion_cost = self.at_completion_cost

        planned_cost = self.planned_cost

        remaining_cost = self.remaining_cost

        cumulative_actual_cost = self.cumulative_actual_cost

        cumulative_at_completion_cost = self.cumulative_at_completion_cost

        cumulative_planned_cost = self.cumulative_planned_cost

        cumulative_remaining_cost = self.cumulative_remaining_cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_date is not UNSET:
            field_dict["StartDate"] = start_date
        if end_date is not UNSET:
            field_dict["EndDate"] = end_date
        if financial_period_object_id is not UNSET:
            field_dict["FinancialPeriodObjectId"] = financial_period_object_id
        if actual_cost is not UNSET:
            field_dict["ActualCost"] = actual_cost
        if at_completion_cost is not UNSET:
            field_dict["AtCompletionCost"] = at_completion_cost
        if planned_cost is not UNSET:
            field_dict["PlannedCost"] = planned_cost
        if remaining_cost is not UNSET:
            field_dict["RemainingCost"] = remaining_cost
        if cumulative_actual_cost is not UNSET:
            field_dict["CumulativeActualCost"] = cumulative_actual_cost
        if cumulative_at_completion_cost is not UNSET:
            field_dict["CumulativeAtCompletionCost"] = cumulative_at_completion_cost
        if cumulative_planned_cost is not UNSET:
            field_dict["CumulativePlannedCost"] = cumulative_planned_cost
        if cumulative_remaining_cost is not UNSET:
            field_dict["CumulativeRemainingCost"] = cumulative_remaining_cost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_date = d.pop("StartDate", UNSET)

        end_date = d.pop("EndDate", UNSET)

        financial_period_object_id = d.pop("FinancialPeriodObjectId", UNSET)

        actual_cost = d.pop("ActualCost", UNSET)

        at_completion_cost = d.pop("AtCompletionCost", UNSET)

        planned_cost = d.pop("PlannedCost", UNSET)

        remaining_cost = d.pop("RemainingCost", UNSET)

        cumulative_actual_cost = d.pop("CumulativeActualCost", UNSET)

        cumulative_at_completion_cost = d.pop("CumulativeAtCompletionCost", UNSET)

        cumulative_planned_cost = d.pop("CumulativePlannedCost", UNSET)

        cumulative_remaining_cost = d.pop("CumulativeRemainingCost", UNSET)

        expense_spread_period = cls(
            start_date=start_date,
            end_date=end_date,
            financial_period_object_id=financial_period_object_id,
            actual_cost=actual_cost,
            at_completion_cost=at_completion_cost,
            planned_cost=planned_cost,
            remaining_cost=remaining_cost,
            cumulative_actual_cost=cumulative_actual_cost,
            cumulative_at_completion_cost=cumulative_at_completion_cost,
            cumulative_planned_cost=cumulative_planned_cost,
            cumulative_remaining_cost=cumulative_remaining_cost,
        )

        expense_spread_period.additional_properties = d
        return expense_spread_period

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
