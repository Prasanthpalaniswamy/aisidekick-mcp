from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivitySpreadPeriod")


@_attrs_define
class ActivitySpreadPeriod:
    """
    Attributes:
        start_date (str | Unset):
        end_date (str | Unset):
        actual_cost (float | Unset):
        actual_expense_cost (float | Unset):
        actual_labor_cost (float | Unset):
        actual_labor_units (float | Unset):
        actual_material_cost (float | Unset):
        actual_non_labor_cost (float | Unset):
        actual_non_labor_units (float | Unset):
        actual_total_cost (float | Unset):
        at_completion_expense_cost (float | Unset):
        at_completion_labor_cost (float | Unset):
        at_completion_labor_units (float | Unset):
        at_completion_material_cost (float | Unset):
        at_completion_non_labor_cost (float | Unset):
        at_completion_non_labor_units (float | Unset):
        at_completion_total_cost (float | Unset):
        baseline_1_actual_expense_cost (float | Unset):
        baseline_1_actual_labor_cost (float | Unset):
        baseline_1_actual_labor_units (float | Unset):
        baseline_1_actual_material_cost (float | Unset):
        baseline_1_actual_non_labor_cost (float | Unset):
        baseline_1_actual_non_labor_units (float | Unset):
        baseline_1_actual_total_cost (float | Unset):
        baseline_1_planned_expense_cost (float | Unset):
        baseline_1_planned_labor_cost (float | Unset):
        baseline_1_planned_labor_units (float | Unset):
        baseline_1_planned_material_cost (float | Unset):
        baseline_1_planned_non_labor_cost (float | Unset):
        baseline_1_planned_non_labor_units (float | Unset):
        baseline_1_planned_total_cost (float | Unset):
        baseline_actual_expense_cost (float | Unset):
        baseline_actual_labor_cost (float | Unset):
        baseline_actual_labor_units (float | Unset):
        baseline_actual_material_cost (float | Unset):
        baseline_actual_non_labor_cost (float | Unset):
        baseline_actual_non_labor_units (float | Unset):
        baseline_actual_total_cost (float | Unset):
        baseline_planned_expense_cost (float | Unset):
        baseline_planned_labor_cost (float | Unset):
        baseline_planned_labor_units (float | Unset):
        baseline_planned_material_cost (float | Unset):
        baseline_planned_non_labor_cost (float | Unset):
        baseline_planned_non_labor_units (float | Unset):
        baseline_planned_total_cost (float | Unset):
        earned_value_cost (float | Unset):
        earned_value_labor_units (float | Unset):
        estimate_at_completion_cost (float | Unset):
        estimate_at_completion_labor_units (float | Unset):
        estimate_to_complete_cost (float | Unset):
        estimate_to_complete_labor_units (float | Unset):
        planned_expense_cost (float | Unset):
        planned_labor_cost (float | Unset):
        planned_labor_units (float | Unset):
        planned_material_cost (float | Unset):
        planned_non_labor_cost (float | Unset):
        planned_non_labor_units (float | Unset):
        planned_total_cost (float | Unset):
        planned_value_cost (float | Unset):
        planned_value_labor_units (float | Unset):
        remaining_expense_cost (float | Unset):
        remaining_labor_cost (float | Unset):
        remaining_labor_units (float | Unset):
        remaining_late_expense_cost (float | Unset):
        remaining_late_labor_cost (float | Unset):
        remaining_late_labor_units (float | Unset):
        remaining_late_material_cost (float | Unset):
        remaining_late_non_labor_cost (float | Unset):
        remaining_late_non_labor_units (float | Unset):
        remaining_late_total_cost (float | Unset):
        remaining_material_cost (float | Unset):
        remaining_non_labor_cost (float | Unset):
        remaining_non_labor_units (float | Unset):
        remaining_total_cost (float | Unset):
        cumulative_actual_cost (float | Unset):
        cumulative_actual_expense_cost (float | Unset):
        cumulative_actual_labor_cost (float | Unset):
        cumulative_actual_labor_units (float | Unset):
        cumulative_actual_material_cost (float | Unset):
        cumulative_actual_non_labor_cost (float | Unset):
        cumulative_actual_non_labor_units (float | Unset):
        cumulative_actual_total_cost (float | Unset):
        cumulative_at_completion_expense_cost (float | Unset):
        cumulative_at_completion_labor_cost (float | Unset):
        cumulative_at_completion_labor_units (float | Unset):
        cumulative_at_completion_material_cost (float | Unset):
        cumulative_at_completion_non_labor_cost (float | Unset):
        cumulative_at_completion_non_labor_units (float | Unset):
        cumulative_at_completion_total_cost (float | Unset):
        cumulative_baseline_1_actual_expense_cost (float | Unset):
        cumulative_baseline_1_actual_labor_cost (float | Unset):
        cumulative_baseline_1_actual_labor_units (float | Unset):
        cumulative_baseline_1_actual_material_cost (float | Unset):
        cumulative_baseline_1_actual_non_labor_cost (float | Unset):
        cumulative_baseline_1_actual_non_labor_units (float | Unset):
        cumulative_baseline_1_actual_total_cost (float | Unset):
        cumulative_baseline_1_planned_expense_cost (float | Unset):
        cumulative_baseline_1_planned_labor_cost (float | Unset):
        cumulative_baseline_1_planned_labor_units (float | Unset):
        cumulative_baseline_1_planned_material_cost (float | Unset):
        cumulative_baseline_1_planned_non_labor_cost (float | Unset):
        cumulative_baseline_1_planned_non_labor_units (float | Unset):
        cumulative_baseline_1_planned_total_cost (float | Unset):
        cumulative_baseline_actual_expense_cost (float | Unset):
        cumulative_baseline_actual_labor_cost (float | Unset):
        cumulative_baseline_actual_labor_units (float | Unset):
        cumulative_baseline_actual_material_cost (float | Unset):
        cumulative_baseline_actual_non_labor_cost (float | Unset):
        cumulative_baseline_actual_non_labor_units (float | Unset):
        cumulative_baseline_actual_total_cost (float | Unset):
        cumulative_baseline_planned_expense_cost (float | Unset):
        cumulative_baseline_planned_labor_cost (float | Unset):
        cumulative_baseline_planned_labor_units (float | Unset):
        cumulative_baseline_planned_material_cost (float | Unset):
        cumulative_baseline_planned_non_labor_cost (float | Unset):
        cumulative_baseline_planned_non_labor_units (float | Unset):
        cumulative_baseline_planned_total_cost (float | Unset):
        cumulative_earned_value_cost (float | Unset):
        cumulative_earned_value_labor_units (float | Unset):
        cumulative_estimate_at_completion_cost (float | Unset):
        cumulative_estimate_at_completion_labor_units (float | Unset):
        cumulative_estimate_to_complete_cost (float | Unset):
        cumulative_estimate_to_complete_labor_units (float | Unset):
        cumulative_planned_expense_cost (float | Unset):
        cumulative_planned_labor_cost (float | Unset):
        cumulative_planned_labor_units (float | Unset):
        cumulative_planned_material_cost (float | Unset):
        cumulative_planned_non_labor_cost (float | Unset):
        cumulative_planned_non_labor_units (float | Unset):
        cumulative_planned_total_cost (float | Unset):
        cumulative_planned_value_cost (float | Unset):
        cumulative_planned_value_labor_units (float | Unset):
        cumulative_remaining_expense_cost (float | Unset):
        cumulative_remaining_labor_cost (float | Unset):
        cumulative_remaining_labor_units (float | Unset):
        cumulative_remaining_late_expense_cost (float | Unset):
        cumulative_remaining_late_labor_cost (float | Unset):
        cumulative_remaining_late_labor_units (float | Unset):
        cumulative_remaining_late_material_cost (float | Unset):
        cumulative_remaining_late_non_labor_cost (float | Unset):
        cumulative_remaining_late_non_labor_units (float | Unset):
        cumulative_remaining_late_total_cost (float | Unset):
        cumulative_remaining_material_cost (float | Unset):
        cumulative_remaining_non_labor_cost (float | Unset):
        cumulative_remaining_non_labor_units (float | Unset):
        cumulative_remaining_total_cost (float | Unset):
    """

    start_date: str | Unset = UNSET
    end_date: str | Unset = UNSET
    actual_cost: float | Unset = UNSET
    actual_expense_cost: float | Unset = UNSET
    actual_labor_cost: float | Unset = UNSET
    actual_labor_units: float | Unset = UNSET
    actual_material_cost: float | Unset = UNSET
    actual_non_labor_cost: float | Unset = UNSET
    actual_non_labor_units: float | Unset = UNSET
    actual_total_cost: float | Unset = UNSET
    at_completion_expense_cost: float | Unset = UNSET
    at_completion_labor_cost: float | Unset = UNSET
    at_completion_labor_units: float | Unset = UNSET
    at_completion_material_cost: float | Unset = UNSET
    at_completion_non_labor_cost: float | Unset = UNSET
    at_completion_non_labor_units: float | Unset = UNSET
    at_completion_total_cost: float | Unset = UNSET
    baseline_1_actual_expense_cost: float | Unset = UNSET
    baseline_1_actual_labor_cost: float | Unset = UNSET
    baseline_1_actual_labor_units: float | Unset = UNSET
    baseline_1_actual_material_cost: float | Unset = UNSET
    baseline_1_actual_non_labor_cost: float | Unset = UNSET
    baseline_1_actual_non_labor_units: float | Unset = UNSET
    baseline_1_actual_total_cost: float | Unset = UNSET
    baseline_1_planned_expense_cost: float | Unset = UNSET
    baseline_1_planned_labor_cost: float | Unset = UNSET
    baseline_1_planned_labor_units: float | Unset = UNSET
    baseline_1_planned_material_cost: float | Unset = UNSET
    baseline_1_planned_non_labor_cost: float | Unset = UNSET
    baseline_1_planned_non_labor_units: float | Unset = UNSET
    baseline_1_planned_total_cost: float | Unset = UNSET
    baseline_actual_expense_cost: float | Unset = UNSET
    baseline_actual_labor_cost: float | Unset = UNSET
    baseline_actual_labor_units: float | Unset = UNSET
    baseline_actual_material_cost: float | Unset = UNSET
    baseline_actual_non_labor_cost: float | Unset = UNSET
    baseline_actual_non_labor_units: float | Unset = UNSET
    baseline_actual_total_cost: float | Unset = UNSET
    baseline_planned_expense_cost: float | Unset = UNSET
    baseline_planned_labor_cost: float | Unset = UNSET
    baseline_planned_labor_units: float | Unset = UNSET
    baseline_planned_material_cost: float | Unset = UNSET
    baseline_planned_non_labor_cost: float | Unset = UNSET
    baseline_planned_non_labor_units: float | Unset = UNSET
    baseline_planned_total_cost: float | Unset = UNSET
    earned_value_cost: float | Unset = UNSET
    earned_value_labor_units: float | Unset = UNSET
    estimate_at_completion_cost: float | Unset = UNSET
    estimate_at_completion_labor_units: float | Unset = UNSET
    estimate_to_complete_cost: float | Unset = UNSET
    estimate_to_complete_labor_units: float | Unset = UNSET
    planned_expense_cost: float | Unset = UNSET
    planned_labor_cost: float | Unset = UNSET
    planned_labor_units: float | Unset = UNSET
    planned_material_cost: float | Unset = UNSET
    planned_non_labor_cost: float | Unset = UNSET
    planned_non_labor_units: float | Unset = UNSET
    planned_total_cost: float | Unset = UNSET
    planned_value_cost: float | Unset = UNSET
    planned_value_labor_units: float | Unset = UNSET
    remaining_expense_cost: float | Unset = UNSET
    remaining_labor_cost: float | Unset = UNSET
    remaining_labor_units: float | Unset = UNSET
    remaining_late_expense_cost: float | Unset = UNSET
    remaining_late_labor_cost: float | Unset = UNSET
    remaining_late_labor_units: float | Unset = UNSET
    remaining_late_material_cost: float | Unset = UNSET
    remaining_late_non_labor_cost: float | Unset = UNSET
    remaining_late_non_labor_units: float | Unset = UNSET
    remaining_late_total_cost: float | Unset = UNSET
    remaining_material_cost: float | Unset = UNSET
    remaining_non_labor_cost: float | Unset = UNSET
    remaining_non_labor_units: float | Unset = UNSET
    remaining_total_cost: float | Unset = UNSET
    cumulative_actual_cost: float | Unset = UNSET
    cumulative_actual_expense_cost: float | Unset = UNSET
    cumulative_actual_labor_cost: float | Unset = UNSET
    cumulative_actual_labor_units: float | Unset = UNSET
    cumulative_actual_material_cost: float | Unset = UNSET
    cumulative_actual_non_labor_cost: float | Unset = UNSET
    cumulative_actual_non_labor_units: float | Unset = UNSET
    cumulative_actual_total_cost: float | Unset = UNSET
    cumulative_at_completion_expense_cost: float | Unset = UNSET
    cumulative_at_completion_labor_cost: float | Unset = UNSET
    cumulative_at_completion_labor_units: float | Unset = UNSET
    cumulative_at_completion_material_cost: float | Unset = UNSET
    cumulative_at_completion_non_labor_cost: float | Unset = UNSET
    cumulative_at_completion_non_labor_units: float | Unset = UNSET
    cumulative_at_completion_total_cost: float | Unset = UNSET
    cumulative_baseline_1_actual_expense_cost: float | Unset = UNSET
    cumulative_baseline_1_actual_labor_cost: float | Unset = UNSET
    cumulative_baseline_1_actual_labor_units: float | Unset = UNSET
    cumulative_baseline_1_actual_material_cost: float | Unset = UNSET
    cumulative_baseline_1_actual_non_labor_cost: float | Unset = UNSET
    cumulative_baseline_1_actual_non_labor_units: float | Unset = UNSET
    cumulative_baseline_1_actual_total_cost: float | Unset = UNSET
    cumulative_baseline_1_planned_expense_cost: float | Unset = UNSET
    cumulative_baseline_1_planned_labor_cost: float | Unset = UNSET
    cumulative_baseline_1_planned_labor_units: float | Unset = UNSET
    cumulative_baseline_1_planned_material_cost: float | Unset = UNSET
    cumulative_baseline_1_planned_non_labor_cost: float | Unset = UNSET
    cumulative_baseline_1_planned_non_labor_units: float | Unset = UNSET
    cumulative_baseline_1_planned_total_cost: float | Unset = UNSET
    cumulative_baseline_actual_expense_cost: float | Unset = UNSET
    cumulative_baseline_actual_labor_cost: float | Unset = UNSET
    cumulative_baseline_actual_labor_units: float | Unset = UNSET
    cumulative_baseline_actual_material_cost: float | Unset = UNSET
    cumulative_baseline_actual_non_labor_cost: float | Unset = UNSET
    cumulative_baseline_actual_non_labor_units: float | Unset = UNSET
    cumulative_baseline_actual_total_cost: float | Unset = UNSET
    cumulative_baseline_planned_expense_cost: float | Unset = UNSET
    cumulative_baseline_planned_labor_cost: float | Unset = UNSET
    cumulative_baseline_planned_labor_units: float | Unset = UNSET
    cumulative_baseline_planned_material_cost: float | Unset = UNSET
    cumulative_baseline_planned_non_labor_cost: float | Unset = UNSET
    cumulative_baseline_planned_non_labor_units: float | Unset = UNSET
    cumulative_baseline_planned_total_cost: float | Unset = UNSET
    cumulative_earned_value_cost: float | Unset = UNSET
    cumulative_earned_value_labor_units: float | Unset = UNSET
    cumulative_estimate_at_completion_cost: float | Unset = UNSET
    cumulative_estimate_at_completion_labor_units: float | Unset = UNSET
    cumulative_estimate_to_complete_cost: float | Unset = UNSET
    cumulative_estimate_to_complete_labor_units: float | Unset = UNSET
    cumulative_planned_expense_cost: float | Unset = UNSET
    cumulative_planned_labor_cost: float | Unset = UNSET
    cumulative_planned_labor_units: float | Unset = UNSET
    cumulative_planned_material_cost: float | Unset = UNSET
    cumulative_planned_non_labor_cost: float | Unset = UNSET
    cumulative_planned_non_labor_units: float | Unset = UNSET
    cumulative_planned_total_cost: float | Unset = UNSET
    cumulative_planned_value_cost: float | Unset = UNSET
    cumulative_planned_value_labor_units: float | Unset = UNSET
    cumulative_remaining_expense_cost: float | Unset = UNSET
    cumulative_remaining_labor_cost: float | Unset = UNSET
    cumulative_remaining_labor_units: float | Unset = UNSET
    cumulative_remaining_late_expense_cost: float | Unset = UNSET
    cumulative_remaining_late_labor_cost: float | Unset = UNSET
    cumulative_remaining_late_labor_units: float | Unset = UNSET
    cumulative_remaining_late_material_cost: float | Unset = UNSET
    cumulative_remaining_late_non_labor_cost: float | Unset = UNSET
    cumulative_remaining_late_non_labor_units: float | Unset = UNSET
    cumulative_remaining_late_total_cost: float | Unset = UNSET
    cumulative_remaining_material_cost: float | Unset = UNSET
    cumulative_remaining_non_labor_cost: float | Unset = UNSET
    cumulative_remaining_non_labor_units: float | Unset = UNSET
    cumulative_remaining_total_cost: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_date = self.start_date

        end_date = self.end_date

        actual_cost = self.actual_cost

        actual_expense_cost = self.actual_expense_cost

        actual_labor_cost = self.actual_labor_cost

        actual_labor_units = self.actual_labor_units

        actual_material_cost = self.actual_material_cost

        actual_non_labor_cost = self.actual_non_labor_cost

        actual_non_labor_units = self.actual_non_labor_units

        actual_total_cost = self.actual_total_cost

        at_completion_expense_cost = self.at_completion_expense_cost

        at_completion_labor_cost = self.at_completion_labor_cost

        at_completion_labor_units = self.at_completion_labor_units

        at_completion_material_cost = self.at_completion_material_cost

        at_completion_non_labor_cost = self.at_completion_non_labor_cost

        at_completion_non_labor_units = self.at_completion_non_labor_units

        at_completion_total_cost = self.at_completion_total_cost

        baseline_1_actual_expense_cost = self.baseline_1_actual_expense_cost

        baseline_1_actual_labor_cost = self.baseline_1_actual_labor_cost

        baseline_1_actual_labor_units = self.baseline_1_actual_labor_units

        baseline_1_actual_material_cost = self.baseline_1_actual_material_cost

        baseline_1_actual_non_labor_cost = self.baseline_1_actual_non_labor_cost

        baseline_1_actual_non_labor_units = self.baseline_1_actual_non_labor_units

        baseline_1_actual_total_cost = self.baseline_1_actual_total_cost

        baseline_1_planned_expense_cost = self.baseline_1_planned_expense_cost

        baseline_1_planned_labor_cost = self.baseline_1_planned_labor_cost

        baseline_1_planned_labor_units = self.baseline_1_planned_labor_units

        baseline_1_planned_material_cost = self.baseline_1_planned_material_cost

        baseline_1_planned_non_labor_cost = self.baseline_1_planned_non_labor_cost

        baseline_1_planned_non_labor_units = self.baseline_1_planned_non_labor_units

        baseline_1_planned_total_cost = self.baseline_1_planned_total_cost

        baseline_actual_expense_cost = self.baseline_actual_expense_cost

        baseline_actual_labor_cost = self.baseline_actual_labor_cost

        baseline_actual_labor_units = self.baseline_actual_labor_units

        baseline_actual_material_cost = self.baseline_actual_material_cost

        baseline_actual_non_labor_cost = self.baseline_actual_non_labor_cost

        baseline_actual_non_labor_units = self.baseline_actual_non_labor_units

        baseline_actual_total_cost = self.baseline_actual_total_cost

        baseline_planned_expense_cost = self.baseline_planned_expense_cost

        baseline_planned_labor_cost = self.baseline_planned_labor_cost

        baseline_planned_labor_units = self.baseline_planned_labor_units

        baseline_planned_material_cost = self.baseline_planned_material_cost

        baseline_planned_non_labor_cost = self.baseline_planned_non_labor_cost

        baseline_planned_non_labor_units = self.baseline_planned_non_labor_units

        baseline_planned_total_cost = self.baseline_planned_total_cost

        earned_value_cost = self.earned_value_cost

        earned_value_labor_units = self.earned_value_labor_units

        estimate_at_completion_cost = self.estimate_at_completion_cost

        estimate_at_completion_labor_units = self.estimate_at_completion_labor_units

        estimate_to_complete_cost = self.estimate_to_complete_cost

        estimate_to_complete_labor_units = self.estimate_to_complete_labor_units

        planned_expense_cost = self.planned_expense_cost

        planned_labor_cost = self.planned_labor_cost

        planned_labor_units = self.planned_labor_units

        planned_material_cost = self.planned_material_cost

        planned_non_labor_cost = self.planned_non_labor_cost

        planned_non_labor_units = self.planned_non_labor_units

        planned_total_cost = self.planned_total_cost

        planned_value_cost = self.planned_value_cost

        planned_value_labor_units = self.planned_value_labor_units

        remaining_expense_cost = self.remaining_expense_cost

        remaining_labor_cost = self.remaining_labor_cost

        remaining_labor_units = self.remaining_labor_units

        remaining_late_expense_cost = self.remaining_late_expense_cost

        remaining_late_labor_cost = self.remaining_late_labor_cost

        remaining_late_labor_units = self.remaining_late_labor_units

        remaining_late_material_cost = self.remaining_late_material_cost

        remaining_late_non_labor_cost = self.remaining_late_non_labor_cost

        remaining_late_non_labor_units = self.remaining_late_non_labor_units

        remaining_late_total_cost = self.remaining_late_total_cost

        remaining_material_cost = self.remaining_material_cost

        remaining_non_labor_cost = self.remaining_non_labor_cost

        remaining_non_labor_units = self.remaining_non_labor_units

        remaining_total_cost = self.remaining_total_cost

        cumulative_actual_cost = self.cumulative_actual_cost

        cumulative_actual_expense_cost = self.cumulative_actual_expense_cost

        cumulative_actual_labor_cost = self.cumulative_actual_labor_cost

        cumulative_actual_labor_units = self.cumulative_actual_labor_units

        cumulative_actual_material_cost = self.cumulative_actual_material_cost

        cumulative_actual_non_labor_cost = self.cumulative_actual_non_labor_cost

        cumulative_actual_non_labor_units = self.cumulative_actual_non_labor_units

        cumulative_actual_total_cost = self.cumulative_actual_total_cost

        cumulative_at_completion_expense_cost = self.cumulative_at_completion_expense_cost

        cumulative_at_completion_labor_cost = self.cumulative_at_completion_labor_cost

        cumulative_at_completion_labor_units = self.cumulative_at_completion_labor_units

        cumulative_at_completion_material_cost = self.cumulative_at_completion_material_cost

        cumulative_at_completion_non_labor_cost = self.cumulative_at_completion_non_labor_cost

        cumulative_at_completion_non_labor_units = self.cumulative_at_completion_non_labor_units

        cumulative_at_completion_total_cost = self.cumulative_at_completion_total_cost

        cumulative_baseline_1_actual_expense_cost = self.cumulative_baseline_1_actual_expense_cost

        cumulative_baseline_1_actual_labor_cost = self.cumulative_baseline_1_actual_labor_cost

        cumulative_baseline_1_actual_labor_units = self.cumulative_baseline_1_actual_labor_units

        cumulative_baseline_1_actual_material_cost = self.cumulative_baseline_1_actual_material_cost

        cumulative_baseline_1_actual_non_labor_cost = self.cumulative_baseline_1_actual_non_labor_cost

        cumulative_baseline_1_actual_non_labor_units = self.cumulative_baseline_1_actual_non_labor_units

        cumulative_baseline_1_actual_total_cost = self.cumulative_baseline_1_actual_total_cost

        cumulative_baseline_1_planned_expense_cost = self.cumulative_baseline_1_planned_expense_cost

        cumulative_baseline_1_planned_labor_cost = self.cumulative_baseline_1_planned_labor_cost

        cumulative_baseline_1_planned_labor_units = self.cumulative_baseline_1_planned_labor_units

        cumulative_baseline_1_planned_material_cost = self.cumulative_baseline_1_planned_material_cost

        cumulative_baseline_1_planned_non_labor_cost = self.cumulative_baseline_1_planned_non_labor_cost

        cumulative_baseline_1_planned_non_labor_units = self.cumulative_baseline_1_planned_non_labor_units

        cumulative_baseline_1_planned_total_cost = self.cumulative_baseline_1_planned_total_cost

        cumulative_baseline_actual_expense_cost = self.cumulative_baseline_actual_expense_cost

        cumulative_baseline_actual_labor_cost = self.cumulative_baseline_actual_labor_cost

        cumulative_baseline_actual_labor_units = self.cumulative_baseline_actual_labor_units

        cumulative_baseline_actual_material_cost = self.cumulative_baseline_actual_material_cost

        cumulative_baseline_actual_non_labor_cost = self.cumulative_baseline_actual_non_labor_cost

        cumulative_baseline_actual_non_labor_units = self.cumulative_baseline_actual_non_labor_units

        cumulative_baseline_actual_total_cost = self.cumulative_baseline_actual_total_cost

        cumulative_baseline_planned_expense_cost = self.cumulative_baseline_planned_expense_cost

        cumulative_baseline_planned_labor_cost = self.cumulative_baseline_planned_labor_cost

        cumulative_baseline_planned_labor_units = self.cumulative_baseline_planned_labor_units

        cumulative_baseline_planned_material_cost = self.cumulative_baseline_planned_material_cost

        cumulative_baseline_planned_non_labor_cost = self.cumulative_baseline_planned_non_labor_cost

        cumulative_baseline_planned_non_labor_units = self.cumulative_baseline_planned_non_labor_units

        cumulative_baseline_planned_total_cost = self.cumulative_baseline_planned_total_cost

        cumulative_earned_value_cost = self.cumulative_earned_value_cost

        cumulative_earned_value_labor_units = self.cumulative_earned_value_labor_units

        cumulative_estimate_at_completion_cost = self.cumulative_estimate_at_completion_cost

        cumulative_estimate_at_completion_labor_units = self.cumulative_estimate_at_completion_labor_units

        cumulative_estimate_to_complete_cost = self.cumulative_estimate_to_complete_cost

        cumulative_estimate_to_complete_labor_units = self.cumulative_estimate_to_complete_labor_units

        cumulative_planned_expense_cost = self.cumulative_planned_expense_cost

        cumulative_planned_labor_cost = self.cumulative_planned_labor_cost

        cumulative_planned_labor_units = self.cumulative_planned_labor_units

        cumulative_planned_material_cost = self.cumulative_planned_material_cost

        cumulative_planned_non_labor_cost = self.cumulative_planned_non_labor_cost

        cumulative_planned_non_labor_units = self.cumulative_planned_non_labor_units

        cumulative_planned_total_cost = self.cumulative_planned_total_cost

        cumulative_planned_value_cost = self.cumulative_planned_value_cost

        cumulative_planned_value_labor_units = self.cumulative_planned_value_labor_units

        cumulative_remaining_expense_cost = self.cumulative_remaining_expense_cost

        cumulative_remaining_labor_cost = self.cumulative_remaining_labor_cost

        cumulative_remaining_labor_units = self.cumulative_remaining_labor_units

        cumulative_remaining_late_expense_cost = self.cumulative_remaining_late_expense_cost

        cumulative_remaining_late_labor_cost = self.cumulative_remaining_late_labor_cost

        cumulative_remaining_late_labor_units = self.cumulative_remaining_late_labor_units

        cumulative_remaining_late_material_cost = self.cumulative_remaining_late_material_cost

        cumulative_remaining_late_non_labor_cost = self.cumulative_remaining_late_non_labor_cost

        cumulative_remaining_late_non_labor_units = self.cumulative_remaining_late_non_labor_units

        cumulative_remaining_late_total_cost = self.cumulative_remaining_late_total_cost

        cumulative_remaining_material_cost = self.cumulative_remaining_material_cost

        cumulative_remaining_non_labor_cost = self.cumulative_remaining_non_labor_cost

        cumulative_remaining_non_labor_units = self.cumulative_remaining_non_labor_units

        cumulative_remaining_total_cost = self.cumulative_remaining_total_cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_date is not UNSET:
            field_dict["StartDate"] = start_date
        if end_date is not UNSET:
            field_dict["EndDate"] = end_date
        if actual_cost is not UNSET:
            field_dict["ActualCost"] = actual_cost
        if actual_expense_cost is not UNSET:
            field_dict["ActualExpenseCost"] = actual_expense_cost
        if actual_labor_cost is not UNSET:
            field_dict["ActualLaborCost"] = actual_labor_cost
        if actual_labor_units is not UNSET:
            field_dict["ActualLaborUnits"] = actual_labor_units
        if actual_material_cost is not UNSET:
            field_dict["ActualMaterialCost"] = actual_material_cost
        if actual_non_labor_cost is not UNSET:
            field_dict["ActualNonLaborCost"] = actual_non_labor_cost
        if actual_non_labor_units is not UNSET:
            field_dict["ActualNonLaborUnits"] = actual_non_labor_units
        if actual_total_cost is not UNSET:
            field_dict["ActualTotalCost"] = actual_total_cost
        if at_completion_expense_cost is not UNSET:
            field_dict["AtCompletionExpenseCost"] = at_completion_expense_cost
        if at_completion_labor_cost is not UNSET:
            field_dict["AtCompletionLaborCost"] = at_completion_labor_cost
        if at_completion_labor_units is not UNSET:
            field_dict["AtCompletionLaborUnits"] = at_completion_labor_units
        if at_completion_material_cost is not UNSET:
            field_dict["AtCompletionMaterialCost"] = at_completion_material_cost
        if at_completion_non_labor_cost is not UNSET:
            field_dict["AtCompletionNonLaborCost"] = at_completion_non_labor_cost
        if at_completion_non_labor_units is not UNSET:
            field_dict["AtCompletionNonLaborUnits"] = at_completion_non_labor_units
        if at_completion_total_cost is not UNSET:
            field_dict["AtCompletionTotalCost"] = at_completion_total_cost
        if baseline_1_actual_expense_cost is not UNSET:
            field_dict["Baseline1ActualExpenseCost"] = baseline_1_actual_expense_cost
        if baseline_1_actual_labor_cost is not UNSET:
            field_dict["Baseline1ActualLaborCost"] = baseline_1_actual_labor_cost
        if baseline_1_actual_labor_units is not UNSET:
            field_dict["Baseline1ActualLaborUnits"] = baseline_1_actual_labor_units
        if baseline_1_actual_material_cost is not UNSET:
            field_dict["Baseline1ActualMaterialCost"] = baseline_1_actual_material_cost
        if baseline_1_actual_non_labor_cost is not UNSET:
            field_dict["Baseline1ActualNonLaborCost"] = baseline_1_actual_non_labor_cost
        if baseline_1_actual_non_labor_units is not UNSET:
            field_dict["Baseline1ActualNonLaborUnits"] = baseline_1_actual_non_labor_units
        if baseline_1_actual_total_cost is not UNSET:
            field_dict["Baseline1ActualTotalCost"] = baseline_1_actual_total_cost
        if baseline_1_planned_expense_cost is not UNSET:
            field_dict["Baseline1PlannedExpenseCost"] = baseline_1_planned_expense_cost
        if baseline_1_planned_labor_cost is not UNSET:
            field_dict["Baseline1PlannedLaborCost"] = baseline_1_planned_labor_cost
        if baseline_1_planned_labor_units is not UNSET:
            field_dict["Baseline1PlannedLaborUnits"] = baseline_1_planned_labor_units
        if baseline_1_planned_material_cost is not UNSET:
            field_dict["Baseline1PlannedMaterialCost"] = baseline_1_planned_material_cost
        if baseline_1_planned_non_labor_cost is not UNSET:
            field_dict["Baseline1PlannedNonLaborCost"] = baseline_1_planned_non_labor_cost
        if baseline_1_planned_non_labor_units is not UNSET:
            field_dict["Baseline1PlannedNonLaborUnits"] = baseline_1_planned_non_labor_units
        if baseline_1_planned_total_cost is not UNSET:
            field_dict["Baseline1PlannedTotalCost"] = baseline_1_planned_total_cost
        if baseline_actual_expense_cost is not UNSET:
            field_dict["BaselineActualExpenseCost"] = baseline_actual_expense_cost
        if baseline_actual_labor_cost is not UNSET:
            field_dict["BaselineActualLaborCost"] = baseline_actual_labor_cost
        if baseline_actual_labor_units is not UNSET:
            field_dict["BaselineActualLaborUnits"] = baseline_actual_labor_units
        if baseline_actual_material_cost is not UNSET:
            field_dict["BaselineActualMaterialCost"] = baseline_actual_material_cost
        if baseline_actual_non_labor_cost is not UNSET:
            field_dict["BaselineActualNonLaborCost"] = baseline_actual_non_labor_cost
        if baseline_actual_non_labor_units is not UNSET:
            field_dict["BaselineActualNonLaborUnits"] = baseline_actual_non_labor_units
        if baseline_actual_total_cost is not UNSET:
            field_dict["BaselineActualTotalCost"] = baseline_actual_total_cost
        if baseline_planned_expense_cost is not UNSET:
            field_dict["BaselinePlannedExpenseCost"] = baseline_planned_expense_cost
        if baseline_planned_labor_cost is not UNSET:
            field_dict["BaselinePlannedLaborCost"] = baseline_planned_labor_cost
        if baseline_planned_labor_units is not UNSET:
            field_dict["BaselinePlannedLaborUnits"] = baseline_planned_labor_units
        if baseline_planned_material_cost is not UNSET:
            field_dict["BaselinePlannedMaterialCost"] = baseline_planned_material_cost
        if baseline_planned_non_labor_cost is not UNSET:
            field_dict["BaselinePlannedNonLaborCost"] = baseline_planned_non_labor_cost
        if baseline_planned_non_labor_units is not UNSET:
            field_dict["BaselinePlannedNonLaborUnits"] = baseline_planned_non_labor_units
        if baseline_planned_total_cost is not UNSET:
            field_dict["BaselinePlannedTotalCost"] = baseline_planned_total_cost
        if earned_value_cost is not UNSET:
            field_dict["EarnedValueCost"] = earned_value_cost
        if earned_value_labor_units is not UNSET:
            field_dict["EarnedValueLaborUnits"] = earned_value_labor_units
        if estimate_at_completion_cost is not UNSET:
            field_dict["EstimateAtCompletionCost"] = estimate_at_completion_cost
        if estimate_at_completion_labor_units is not UNSET:
            field_dict["EstimateAtCompletionLaborUnits"] = estimate_at_completion_labor_units
        if estimate_to_complete_cost is not UNSET:
            field_dict["EstimateToCompleteCost"] = estimate_to_complete_cost
        if estimate_to_complete_labor_units is not UNSET:
            field_dict["EstimateToCompleteLaborUnits"] = estimate_to_complete_labor_units
        if planned_expense_cost is not UNSET:
            field_dict["PlannedExpenseCost"] = planned_expense_cost
        if planned_labor_cost is not UNSET:
            field_dict["PlannedLaborCost"] = planned_labor_cost
        if planned_labor_units is not UNSET:
            field_dict["PlannedLaborUnits"] = planned_labor_units
        if planned_material_cost is not UNSET:
            field_dict["PlannedMaterialCost"] = planned_material_cost
        if planned_non_labor_cost is not UNSET:
            field_dict["PlannedNonLaborCost"] = planned_non_labor_cost
        if planned_non_labor_units is not UNSET:
            field_dict["PlannedNonLaborUnits"] = planned_non_labor_units
        if planned_total_cost is not UNSET:
            field_dict["PlannedTotalCost"] = planned_total_cost
        if planned_value_cost is not UNSET:
            field_dict["PlannedValueCost"] = planned_value_cost
        if planned_value_labor_units is not UNSET:
            field_dict["PlannedValueLaborUnits"] = planned_value_labor_units
        if remaining_expense_cost is not UNSET:
            field_dict["RemainingExpenseCost"] = remaining_expense_cost
        if remaining_labor_cost is not UNSET:
            field_dict["RemainingLaborCost"] = remaining_labor_cost
        if remaining_labor_units is not UNSET:
            field_dict["RemainingLaborUnits"] = remaining_labor_units
        if remaining_late_expense_cost is not UNSET:
            field_dict["RemainingLateExpenseCost"] = remaining_late_expense_cost
        if remaining_late_labor_cost is not UNSET:
            field_dict["RemainingLateLaborCost"] = remaining_late_labor_cost
        if remaining_late_labor_units is not UNSET:
            field_dict["RemainingLateLaborUnits"] = remaining_late_labor_units
        if remaining_late_material_cost is not UNSET:
            field_dict["RemainingLateMaterialCost"] = remaining_late_material_cost
        if remaining_late_non_labor_cost is not UNSET:
            field_dict["RemainingLateNonLaborCost"] = remaining_late_non_labor_cost
        if remaining_late_non_labor_units is not UNSET:
            field_dict["RemainingLateNonLaborUnits"] = remaining_late_non_labor_units
        if remaining_late_total_cost is not UNSET:
            field_dict["RemainingLateTotalCost"] = remaining_late_total_cost
        if remaining_material_cost is not UNSET:
            field_dict["RemainingMaterialCost"] = remaining_material_cost
        if remaining_non_labor_cost is not UNSET:
            field_dict["RemainingNonLaborCost"] = remaining_non_labor_cost
        if remaining_non_labor_units is not UNSET:
            field_dict["RemainingNonLaborUnits"] = remaining_non_labor_units
        if remaining_total_cost is not UNSET:
            field_dict["RemainingTotalCost"] = remaining_total_cost
        if cumulative_actual_cost is not UNSET:
            field_dict["CumulativeActualCost"] = cumulative_actual_cost
        if cumulative_actual_expense_cost is not UNSET:
            field_dict["CumulativeActualExpenseCost"] = cumulative_actual_expense_cost
        if cumulative_actual_labor_cost is not UNSET:
            field_dict["CumulativeActualLaborCost"] = cumulative_actual_labor_cost
        if cumulative_actual_labor_units is not UNSET:
            field_dict["CumulativeActualLaborUnits"] = cumulative_actual_labor_units
        if cumulative_actual_material_cost is not UNSET:
            field_dict["CumulativeActualMaterialCost"] = cumulative_actual_material_cost
        if cumulative_actual_non_labor_cost is not UNSET:
            field_dict["CumulativeActualNonLaborCost"] = cumulative_actual_non_labor_cost
        if cumulative_actual_non_labor_units is not UNSET:
            field_dict["CumulativeActualNonLaborUnits"] = cumulative_actual_non_labor_units
        if cumulative_actual_total_cost is not UNSET:
            field_dict["CumulativeActualTotalCost"] = cumulative_actual_total_cost
        if cumulative_at_completion_expense_cost is not UNSET:
            field_dict["CumulativeAtCompletionExpenseCost"] = cumulative_at_completion_expense_cost
        if cumulative_at_completion_labor_cost is not UNSET:
            field_dict["CumulativeAtCompletionLaborCost"] = cumulative_at_completion_labor_cost
        if cumulative_at_completion_labor_units is not UNSET:
            field_dict["CumulativeAtCompletionLaborUnits"] = cumulative_at_completion_labor_units
        if cumulative_at_completion_material_cost is not UNSET:
            field_dict["CumulativeAtCompletionMaterialCost"] = cumulative_at_completion_material_cost
        if cumulative_at_completion_non_labor_cost is not UNSET:
            field_dict["CumulativeAtCompletionNonLaborCost"] = cumulative_at_completion_non_labor_cost
        if cumulative_at_completion_non_labor_units is not UNSET:
            field_dict["CumulativeAtCompletionNonLaborUnits"] = cumulative_at_completion_non_labor_units
        if cumulative_at_completion_total_cost is not UNSET:
            field_dict["CumulativeAtCompletionTotalCost"] = cumulative_at_completion_total_cost
        if cumulative_baseline_1_actual_expense_cost is not UNSET:
            field_dict["CumulativeBaseline1ActualExpenseCost"] = cumulative_baseline_1_actual_expense_cost
        if cumulative_baseline_1_actual_labor_cost is not UNSET:
            field_dict["CumulativeBaseline1ActualLaborCost"] = cumulative_baseline_1_actual_labor_cost
        if cumulative_baseline_1_actual_labor_units is not UNSET:
            field_dict["CumulativeBaseline1ActualLaborUnits"] = cumulative_baseline_1_actual_labor_units
        if cumulative_baseline_1_actual_material_cost is not UNSET:
            field_dict["CumulativeBaseline1ActualMaterialCost"] = cumulative_baseline_1_actual_material_cost
        if cumulative_baseline_1_actual_non_labor_cost is not UNSET:
            field_dict["CumulativeBaseline1ActualNonLaborCost"] = cumulative_baseline_1_actual_non_labor_cost
        if cumulative_baseline_1_actual_non_labor_units is not UNSET:
            field_dict["CumulativeBaseline1ActualNonLaborUnits"] = cumulative_baseline_1_actual_non_labor_units
        if cumulative_baseline_1_actual_total_cost is not UNSET:
            field_dict["CumulativeBaseline1ActualTotalCost"] = cumulative_baseline_1_actual_total_cost
        if cumulative_baseline_1_planned_expense_cost is not UNSET:
            field_dict["CumulativeBaseline1PlannedExpenseCost"] = cumulative_baseline_1_planned_expense_cost
        if cumulative_baseline_1_planned_labor_cost is not UNSET:
            field_dict["CumulativeBaseline1PlannedLaborCost"] = cumulative_baseline_1_planned_labor_cost
        if cumulative_baseline_1_planned_labor_units is not UNSET:
            field_dict["CumulativeBaseline1PlannedLaborUnits"] = cumulative_baseline_1_planned_labor_units
        if cumulative_baseline_1_planned_material_cost is not UNSET:
            field_dict["CumulativeBaseline1PlannedMaterialCost"] = cumulative_baseline_1_planned_material_cost
        if cumulative_baseline_1_planned_non_labor_cost is not UNSET:
            field_dict["CumulativeBaseline1PlannedNonLaborCost"] = cumulative_baseline_1_planned_non_labor_cost
        if cumulative_baseline_1_planned_non_labor_units is not UNSET:
            field_dict["CumulativeBaseline1PlannedNonLaborUnits"] = cumulative_baseline_1_planned_non_labor_units
        if cumulative_baseline_1_planned_total_cost is not UNSET:
            field_dict["CumulativeBaseline1PlannedTotalCost"] = cumulative_baseline_1_planned_total_cost
        if cumulative_baseline_actual_expense_cost is not UNSET:
            field_dict["CumulativeBaselineActualExpenseCost"] = cumulative_baseline_actual_expense_cost
        if cumulative_baseline_actual_labor_cost is not UNSET:
            field_dict["CumulativeBaselineActualLaborCost"] = cumulative_baseline_actual_labor_cost
        if cumulative_baseline_actual_labor_units is not UNSET:
            field_dict["CumulativeBaselineActualLaborUnits"] = cumulative_baseline_actual_labor_units
        if cumulative_baseline_actual_material_cost is not UNSET:
            field_dict["CumulativeBaselineActualMaterialCost"] = cumulative_baseline_actual_material_cost
        if cumulative_baseline_actual_non_labor_cost is not UNSET:
            field_dict["CumulativeBaselineActualNonLaborCost"] = cumulative_baseline_actual_non_labor_cost
        if cumulative_baseline_actual_non_labor_units is not UNSET:
            field_dict["CumulativeBaselineActualNonLaborUnits"] = cumulative_baseline_actual_non_labor_units
        if cumulative_baseline_actual_total_cost is not UNSET:
            field_dict["CumulativeBaselineActualTotalCost"] = cumulative_baseline_actual_total_cost
        if cumulative_baseline_planned_expense_cost is not UNSET:
            field_dict["CumulativeBaselinePlannedExpenseCost"] = cumulative_baseline_planned_expense_cost
        if cumulative_baseline_planned_labor_cost is not UNSET:
            field_dict["CumulativeBaselinePlannedLaborCost"] = cumulative_baseline_planned_labor_cost
        if cumulative_baseline_planned_labor_units is not UNSET:
            field_dict["CumulativeBaselinePlannedLaborUnits"] = cumulative_baseline_planned_labor_units
        if cumulative_baseline_planned_material_cost is not UNSET:
            field_dict["CumulativeBaselinePlannedMaterialCost"] = cumulative_baseline_planned_material_cost
        if cumulative_baseline_planned_non_labor_cost is not UNSET:
            field_dict["CumulativeBaselinePlannedNonLaborCost"] = cumulative_baseline_planned_non_labor_cost
        if cumulative_baseline_planned_non_labor_units is not UNSET:
            field_dict["CumulativeBaselinePlannedNonLaborUnits"] = cumulative_baseline_planned_non_labor_units
        if cumulative_baseline_planned_total_cost is not UNSET:
            field_dict["CumulativeBaselinePlannedTotalCost"] = cumulative_baseline_planned_total_cost
        if cumulative_earned_value_cost is not UNSET:
            field_dict["CumulativeEarnedValueCost"] = cumulative_earned_value_cost
        if cumulative_earned_value_labor_units is not UNSET:
            field_dict["CumulativeEarnedValueLaborUnits"] = cumulative_earned_value_labor_units
        if cumulative_estimate_at_completion_cost is not UNSET:
            field_dict["CumulativeEstimateAtCompletionCost"] = cumulative_estimate_at_completion_cost
        if cumulative_estimate_at_completion_labor_units is not UNSET:
            field_dict["CumulativeEstimateAtCompletionLaborUnits"] = cumulative_estimate_at_completion_labor_units
        if cumulative_estimate_to_complete_cost is not UNSET:
            field_dict["CumulativeEstimateToCompleteCost"] = cumulative_estimate_to_complete_cost
        if cumulative_estimate_to_complete_labor_units is not UNSET:
            field_dict["CumulativeEstimateToCompleteLaborUnits"] = cumulative_estimate_to_complete_labor_units
        if cumulative_planned_expense_cost is not UNSET:
            field_dict["CumulativePlannedExpenseCost"] = cumulative_planned_expense_cost
        if cumulative_planned_labor_cost is not UNSET:
            field_dict["CumulativePlannedLaborCost"] = cumulative_planned_labor_cost
        if cumulative_planned_labor_units is not UNSET:
            field_dict["CumulativePlannedLaborUnits"] = cumulative_planned_labor_units
        if cumulative_planned_material_cost is not UNSET:
            field_dict["CumulativePlannedMaterialCost"] = cumulative_planned_material_cost
        if cumulative_planned_non_labor_cost is not UNSET:
            field_dict["CumulativePlannedNonLaborCost"] = cumulative_planned_non_labor_cost
        if cumulative_planned_non_labor_units is not UNSET:
            field_dict["CumulativePlannedNonLaborUnits"] = cumulative_planned_non_labor_units
        if cumulative_planned_total_cost is not UNSET:
            field_dict["CumulativePlannedTotalCost"] = cumulative_planned_total_cost
        if cumulative_planned_value_cost is not UNSET:
            field_dict["CumulativePlannedValueCost"] = cumulative_planned_value_cost
        if cumulative_planned_value_labor_units is not UNSET:
            field_dict["CumulativePlannedValueLaborUnits"] = cumulative_planned_value_labor_units
        if cumulative_remaining_expense_cost is not UNSET:
            field_dict["CumulativeRemainingExpenseCost"] = cumulative_remaining_expense_cost
        if cumulative_remaining_labor_cost is not UNSET:
            field_dict["CumulativeRemainingLaborCost"] = cumulative_remaining_labor_cost
        if cumulative_remaining_labor_units is not UNSET:
            field_dict["CumulativeRemainingLaborUnits"] = cumulative_remaining_labor_units
        if cumulative_remaining_late_expense_cost is not UNSET:
            field_dict["CumulativeRemainingLateExpenseCost"] = cumulative_remaining_late_expense_cost
        if cumulative_remaining_late_labor_cost is not UNSET:
            field_dict["CumulativeRemainingLateLaborCost"] = cumulative_remaining_late_labor_cost
        if cumulative_remaining_late_labor_units is not UNSET:
            field_dict["CumulativeRemainingLateLaborUnits"] = cumulative_remaining_late_labor_units
        if cumulative_remaining_late_material_cost is not UNSET:
            field_dict["CumulativeRemainingLateMaterialCost"] = cumulative_remaining_late_material_cost
        if cumulative_remaining_late_non_labor_cost is not UNSET:
            field_dict["CumulativeRemainingLateNonLaborCost"] = cumulative_remaining_late_non_labor_cost
        if cumulative_remaining_late_non_labor_units is not UNSET:
            field_dict["CumulativeRemainingLateNonLaborUnits"] = cumulative_remaining_late_non_labor_units
        if cumulative_remaining_late_total_cost is not UNSET:
            field_dict["CumulativeRemainingLateTotalCost"] = cumulative_remaining_late_total_cost
        if cumulative_remaining_material_cost is not UNSET:
            field_dict["CumulativeRemainingMaterialCost"] = cumulative_remaining_material_cost
        if cumulative_remaining_non_labor_cost is not UNSET:
            field_dict["CumulativeRemainingNonLaborCost"] = cumulative_remaining_non_labor_cost
        if cumulative_remaining_non_labor_units is not UNSET:
            field_dict["CumulativeRemainingNonLaborUnits"] = cumulative_remaining_non_labor_units
        if cumulative_remaining_total_cost is not UNSET:
            field_dict["CumulativeRemainingTotalCost"] = cumulative_remaining_total_cost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_date = d.pop("StartDate", UNSET)

        end_date = d.pop("EndDate", UNSET)

        actual_cost = d.pop("ActualCost", UNSET)

        actual_expense_cost = d.pop("ActualExpenseCost", UNSET)

        actual_labor_cost = d.pop("ActualLaborCost", UNSET)

        actual_labor_units = d.pop("ActualLaborUnits", UNSET)

        actual_material_cost = d.pop("ActualMaterialCost", UNSET)

        actual_non_labor_cost = d.pop("ActualNonLaborCost", UNSET)

        actual_non_labor_units = d.pop("ActualNonLaborUnits", UNSET)

        actual_total_cost = d.pop("ActualTotalCost", UNSET)

        at_completion_expense_cost = d.pop("AtCompletionExpenseCost", UNSET)

        at_completion_labor_cost = d.pop("AtCompletionLaborCost", UNSET)

        at_completion_labor_units = d.pop("AtCompletionLaborUnits", UNSET)

        at_completion_material_cost = d.pop("AtCompletionMaterialCost", UNSET)

        at_completion_non_labor_cost = d.pop("AtCompletionNonLaborCost", UNSET)

        at_completion_non_labor_units = d.pop("AtCompletionNonLaborUnits", UNSET)

        at_completion_total_cost = d.pop("AtCompletionTotalCost", UNSET)

        baseline_1_actual_expense_cost = d.pop("Baseline1ActualExpenseCost", UNSET)

        baseline_1_actual_labor_cost = d.pop("Baseline1ActualLaborCost", UNSET)

        baseline_1_actual_labor_units = d.pop("Baseline1ActualLaborUnits", UNSET)

        baseline_1_actual_material_cost = d.pop("Baseline1ActualMaterialCost", UNSET)

        baseline_1_actual_non_labor_cost = d.pop("Baseline1ActualNonLaborCost", UNSET)

        baseline_1_actual_non_labor_units = d.pop("Baseline1ActualNonLaborUnits", UNSET)

        baseline_1_actual_total_cost = d.pop("Baseline1ActualTotalCost", UNSET)

        baseline_1_planned_expense_cost = d.pop("Baseline1PlannedExpenseCost", UNSET)

        baseline_1_planned_labor_cost = d.pop("Baseline1PlannedLaborCost", UNSET)

        baseline_1_planned_labor_units = d.pop("Baseline1PlannedLaborUnits", UNSET)

        baseline_1_planned_material_cost = d.pop("Baseline1PlannedMaterialCost", UNSET)

        baseline_1_planned_non_labor_cost = d.pop("Baseline1PlannedNonLaborCost", UNSET)

        baseline_1_planned_non_labor_units = d.pop("Baseline1PlannedNonLaborUnits", UNSET)

        baseline_1_planned_total_cost = d.pop("Baseline1PlannedTotalCost", UNSET)

        baseline_actual_expense_cost = d.pop("BaselineActualExpenseCost", UNSET)

        baseline_actual_labor_cost = d.pop("BaselineActualLaborCost", UNSET)

        baseline_actual_labor_units = d.pop("BaselineActualLaborUnits", UNSET)

        baseline_actual_material_cost = d.pop("BaselineActualMaterialCost", UNSET)

        baseline_actual_non_labor_cost = d.pop("BaselineActualNonLaborCost", UNSET)

        baseline_actual_non_labor_units = d.pop("BaselineActualNonLaborUnits", UNSET)

        baseline_actual_total_cost = d.pop("BaselineActualTotalCost", UNSET)

        baseline_planned_expense_cost = d.pop("BaselinePlannedExpenseCost", UNSET)

        baseline_planned_labor_cost = d.pop("BaselinePlannedLaborCost", UNSET)

        baseline_planned_labor_units = d.pop("BaselinePlannedLaborUnits", UNSET)

        baseline_planned_material_cost = d.pop("BaselinePlannedMaterialCost", UNSET)

        baseline_planned_non_labor_cost = d.pop("BaselinePlannedNonLaborCost", UNSET)

        baseline_planned_non_labor_units = d.pop("BaselinePlannedNonLaborUnits", UNSET)

        baseline_planned_total_cost = d.pop("BaselinePlannedTotalCost", UNSET)

        earned_value_cost = d.pop("EarnedValueCost", UNSET)

        earned_value_labor_units = d.pop("EarnedValueLaborUnits", UNSET)

        estimate_at_completion_cost = d.pop("EstimateAtCompletionCost", UNSET)

        estimate_at_completion_labor_units = d.pop("EstimateAtCompletionLaborUnits", UNSET)

        estimate_to_complete_cost = d.pop("EstimateToCompleteCost", UNSET)

        estimate_to_complete_labor_units = d.pop("EstimateToCompleteLaborUnits", UNSET)

        planned_expense_cost = d.pop("PlannedExpenseCost", UNSET)

        planned_labor_cost = d.pop("PlannedLaborCost", UNSET)

        planned_labor_units = d.pop("PlannedLaborUnits", UNSET)

        planned_material_cost = d.pop("PlannedMaterialCost", UNSET)

        planned_non_labor_cost = d.pop("PlannedNonLaborCost", UNSET)

        planned_non_labor_units = d.pop("PlannedNonLaborUnits", UNSET)

        planned_total_cost = d.pop("PlannedTotalCost", UNSET)

        planned_value_cost = d.pop("PlannedValueCost", UNSET)

        planned_value_labor_units = d.pop("PlannedValueLaborUnits", UNSET)

        remaining_expense_cost = d.pop("RemainingExpenseCost", UNSET)

        remaining_labor_cost = d.pop("RemainingLaborCost", UNSET)

        remaining_labor_units = d.pop("RemainingLaborUnits", UNSET)

        remaining_late_expense_cost = d.pop("RemainingLateExpenseCost", UNSET)

        remaining_late_labor_cost = d.pop("RemainingLateLaborCost", UNSET)

        remaining_late_labor_units = d.pop("RemainingLateLaborUnits", UNSET)

        remaining_late_material_cost = d.pop("RemainingLateMaterialCost", UNSET)

        remaining_late_non_labor_cost = d.pop("RemainingLateNonLaborCost", UNSET)

        remaining_late_non_labor_units = d.pop("RemainingLateNonLaborUnits", UNSET)

        remaining_late_total_cost = d.pop("RemainingLateTotalCost", UNSET)

        remaining_material_cost = d.pop("RemainingMaterialCost", UNSET)

        remaining_non_labor_cost = d.pop("RemainingNonLaborCost", UNSET)

        remaining_non_labor_units = d.pop("RemainingNonLaborUnits", UNSET)

        remaining_total_cost = d.pop("RemainingTotalCost", UNSET)

        cumulative_actual_cost = d.pop("CumulativeActualCost", UNSET)

        cumulative_actual_expense_cost = d.pop("CumulativeActualExpenseCost", UNSET)

        cumulative_actual_labor_cost = d.pop("CumulativeActualLaborCost", UNSET)

        cumulative_actual_labor_units = d.pop("CumulativeActualLaborUnits", UNSET)

        cumulative_actual_material_cost = d.pop("CumulativeActualMaterialCost", UNSET)

        cumulative_actual_non_labor_cost = d.pop("CumulativeActualNonLaborCost", UNSET)

        cumulative_actual_non_labor_units = d.pop("CumulativeActualNonLaborUnits", UNSET)

        cumulative_actual_total_cost = d.pop("CumulativeActualTotalCost", UNSET)

        cumulative_at_completion_expense_cost = d.pop("CumulativeAtCompletionExpenseCost", UNSET)

        cumulative_at_completion_labor_cost = d.pop("CumulativeAtCompletionLaborCost", UNSET)

        cumulative_at_completion_labor_units = d.pop("CumulativeAtCompletionLaborUnits", UNSET)

        cumulative_at_completion_material_cost = d.pop("CumulativeAtCompletionMaterialCost", UNSET)

        cumulative_at_completion_non_labor_cost = d.pop("CumulativeAtCompletionNonLaborCost", UNSET)

        cumulative_at_completion_non_labor_units = d.pop("CumulativeAtCompletionNonLaborUnits", UNSET)

        cumulative_at_completion_total_cost = d.pop("CumulativeAtCompletionTotalCost", UNSET)

        cumulative_baseline_1_actual_expense_cost = d.pop("CumulativeBaseline1ActualExpenseCost", UNSET)

        cumulative_baseline_1_actual_labor_cost = d.pop("CumulativeBaseline1ActualLaborCost", UNSET)

        cumulative_baseline_1_actual_labor_units = d.pop("CumulativeBaseline1ActualLaborUnits", UNSET)

        cumulative_baseline_1_actual_material_cost = d.pop("CumulativeBaseline1ActualMaterialCost", UNSET)

        cumulative_baseline_1_actual_non_labor_cost = d.pop("CumulativeBaseline1ActualNonLaborCost", UNSET)

        cumulative_baseline_1_actual_non_labor_units = d.pop("CumulativeBaseline1ActualNonLaborUnits", UNSET)

        cumulative_baseline_1_actual_total_cost = d.pop("CumulativeBaseline1ActualTotalCost", UNSET)

        cumulative_baseline_1_planned_expense_cost = d.pop("CumulativeBaseline1PlannedExpenseCost", UNSET)

        cumulative_baseline_1_planned_labor_cost = d.pop("CumulativeBaseline1PlannedLaborCost", UNSET)

        cumulative_baseline_1_planned_labor_units = d.pop("CumulativeBaseline1PlannedLaborUnits", UNSET)

        cumulative_baseline_1_planned_material_cost = d.pop("CumulativeBaseline1PlannedMaterialCost", UNSET)

        cumulative_baseline_1_planned_non_labor_cost = d.pop("CumulativeBaseline1PlannedNonLaborCost", UNSET)

        cumulative_baseline_1_planned_non_labor_units = d.pop("CumulativeBaseline1PlannedNonLaborUnits", UNSET)

        cumulative_baseline_1_planned_total_cost = d.pop("CumulativeBaseline1PlannedTotalCost", UNSET)

        cumulative_baseline_actual_expense_cost = d.pop("CumulativeBaselineActualExpenseCost", UNSET)

        cumulative_baseline_actual_labor_cost = d.pop("CumulativeBaselineActualLaborCost", UNSET)

        cumulative_baseline_actual_labor_units = d.pop("CumulativeBaselineActualLaborUnits", UNSET)

        cumulative_baseline_actual_material_cost = d.pop("CumulativeBaselineActualMaterialCost", UNSET)

        cumulative_baseline_actual_non_labor_cost = d.pop("CumulativeBaselineActualNonLaborCost", UNSET)

        cumulative_baseline_actual_non_labor_units = d.pop("CumulativeBaselineActualNonLaborUnits", UNSET)

        cumulative_baseline_actual_total_cost = d.pop("CumulativeBaselineActualTotalCost", UNSET)

        cumulative_baseline_planned_expense_cost = d.pop("CumulativeBaselinePlannedExpenseCost", UNSET)

        cumulative_baseline_planned_labor_cost = d.pop("CumulativeBaselinePlannedLaborCost", UNSET)

        cumulative_baseline_planned_labor_units = d.pop("CumulativeBaselinePlannedLaborUnits", UNSET)

        cumulative_baseline_planned_material_cost = d.pop("CumulativeBaselinePlannedMaterialCost", UNSET)

        cumulative_baseline_planned_non_labor_cost = d.pop("CumulativeBaselinePlannedNonLaborCost", UNSET)

        cumulative_baseline_planned_non_labor_units = d.pop("CumulativeBaselinePlannedNonLaborUnits", UNSET)

        cumulative_baseline_planned_total_cost = d.pop("CumulativeBaselinePlannedTotalCost", UNSET)

        cumulative_earned_value_cost = d.pop("CumulativeEarnedValueCost", UNSET)

        cumulative_earned_value_labor_units = d.pop("CumulativeEarnedValueLaborUnits", UNSET)

        cumulative_estimate_at_completion_cost = d.pop("CumulativeEstimateAtCompletionCost", UNSET)

        cumulative_estimate_at_completion_labor_units = d.pop("CumulativeEstimateAtCompletionLaborUnits", UNSET)

        cumulative_estimate_to_complete_cost = d.pop("CumulativeEstimateToCompleteCost", UNSET)

        cumulative_estimate_to_complete_labor_units = d.pop("CumulativeEstimateToCompleteLaborUnits", UNSET)

        cumulative_planned_expense_cost = d.pop("CumulativePlannedExpenseCost", UNSET)

        cumulative_planned_labor_cost = d.pop("CumulativePlannedLaborCost", UNSET)

        cumulative_planned_labor_units = d.pop("CumulativePlannedLaborUnits", UNSET)

        cumulative_planned_material_cost = d.pop("CumulativePlannedMaterialCost", UNSET)

        cumulative_planned_non_labor_cost = d.pop("CumulativePlannedNonLaborCost", UNSET)

        cumulative_planned_non_labor_units = d.pop("CumulativePlannedNonLaborUnits", UNSET)

        cumulative_planned_total_cost = d.pop("CumulativePlannedTotalCost", UNSET)

        cumulative_planned_value_cost = d.pop("CumulativePlannedValueCost", UNSET)

        cumulative_planned_value_labor_units = d.pop("CumulativePlannedValueLaborUnits", UNSET)

        cumulative_remaining_expense_cost = d.pop("CumulativeRemainingExpenseCost", UNSET)

        cumulative_remaining_labor_cost = d.pop("CumulativeRemainingLaborCost", UNSET)

        cumulative_remaining_labor_units = d.pop("CumulativeRemainingLaborUnits", UNSET)

        cumulative_remaining_late_expense_cost = d.pop("CumulativeRemainingLateExpenseCost", UNSET)

        cumulative_remaining_late_labor_cost = d.pop("CumulativeRemainingLateLaborCost", UNSET)

        cumulative_remaining_late_labor_units = d.pop("CumulativeRemainingLateLaborUnits", UNSET)

        cumulative_remaining_late_material_cost = d.pop("CumulativeRemainingLateMaterialCost", UNSET)

        cumulative_remaining_late_non_labor_cost = d.pop("CumulativeRemainingLateNonLaborCost", UNSET)

        cumulative_remaining_late_non_labor_units = d.pop("CumulativeRemainingLateNonLaborUnits", UNSET)

        cumulative_remaining_late_total_cost = d.pop("CumulativeRemainingLateTotalCost", UNSET)

        cumulative_remaining_material_cost = d.pop("CumulativeRemainingMaterialCost", UNSET)

        cumulative_remaining_non_labor_cost = d.pop("CumulativeRemainingNonLaborCost", UNSET)

        cumulative_remaining_non_labor_units = d.pop("CumulativeRemainingNonLaborUnits", UNSET)

        cumulative_remaining_total_cost = d.pop("CumulativeRemainingTotalCost", UNSET)

        activity_spread_period = cls(
            start_date=start_date,
            end_date=end_date,
            actual_cost=actual_cost,
            actual_expense_cost=actual_expense_cost,
            actual_labor_cost=actual_labor_cost,
            actual_labor_units=actual_labor_units,
            actual_material_cost=actual_material_cost,
            actual_non_labor_cost=actual_non_labor_cost,
            actual_non_labor_units=actual_non_labor_units,
            actual_total_cost=actual_total_cost,
            at_completion_expense_cost=at_completion_expense_cost,
            at_completion_labor_cost=at_completion_labor_cost,
            at_completion_labor_units=at_completion_labor_units,
            at_completion_material_cost=at_completion_material_cost,
            at_completion_non_labor_cost=at_completion_non_labor_cost,
            at_completion_non_labor_units=at_completion_non_labor_units,
            at_completion_total_cost=at_completion_total_cost,
            baseline_1_actual_expense_cost=baseline_1_actual_expense_cost,
            baseline_1_actual_labor_cost=baseline_1_actual_labor_cost,
            baseline_1_actual_labor_units=baseline_1_actual_labor_units,
            baseline_1_actual_material_cost=baseline_1_actual_material_cost,
            baseline_1_actual_non_labor_cost=baseline_1_actual_non_labor_cost,
            baseline_1_actual_non_labor_units=baseline_1_actual_non_labor_units,
            baseline_1_actual_total_cost=baseline_1_actual_total_cost,
            baseline_1_planned_expense_cost=baseline_1_planned_expense_cost,
            baseline_1_planned_labor_cost=baseline_1_planned_labor_cost,
            baseline_1_planned_labor_units=baseline_1_planned_labor_units,
            baseline_1_planned_material_cost=baseline_1_planned_material_cost,
            baseline_1_planned_non_labor_cost=baseline_1_planned_non_labor_cost,
            baseline_1_planned_non_labor_units=baseline_1_planned_non_labor_units,
            baseline_1_planned_total_cost=baseline_1_planned_total_cost,
            baseline_actual_expense_cost=baseline_actual_expense_cost,
            baseline_actual_labor_cost=baseline_actual_labor_cost,
            baseline_actual_labor_units=baseline_actual_labor_units,
            baseline_actual_material_cost=baseline_actual_material_cost,
            baseline_actual_non_labor_cost=baseline_actual_non_labor_cost,
            baseline_actual_non_labor_units=baseline_actual_non_labor_units,
            baseline_actual_total_cost=baseline_actual_total_cost,
            baseline_planned_expense_cost=baseline_planned_expense_cost,
            baseline_planned_labor_cost=baseline_planned_labor_cost,
            baseline_planned_labor_units=baseline_planned_labor_units,
            baseline_planned_material_cost=baseline_planned_material_cost,
            baseline_planned_non_labor_cost=baseline_planned_non_labor_cost,
            baseline_planned_non_labor_units=baseline_planned_non_labor_units,
            baseline_planned_total_cost=baseline_planned_total_cost,
            earned_value_cost=earned_value_cost,
            earned_value_labor_units=earned_value_labor_units,
            estimate_at_completion_cost=estimate_at_completion_cost,
            estimate_at_completion_labor_units=estimate_at_completion_labor_units,
            estimate_to_complete_cost=estimate_to_complete_cost,
            estimate_to_complete_labor_units=estimate_to_complete_labor_units,
            planned_expense_cost=planned_expense_cost,
            planned_labor_cost=planned_labor_cost,
            planned_labor_units=planned_labor_units,
            planned_material_cost=planned_material_cost,
            planned_non_labor_cost=planned_non_labor_cost,
            planned_non_labor_units=planned_non_labor_units,
            planned_total_cost=planned_total_cost,
            planned_value_cost=planned_value_cost,
            planned_value_labor_units=planned_value_labor_units,
            remaining_expense_cost=remaining_expense_cost,
            remaining_labor_cost=remaining_labor_cost,
            remaining_labor_units=remaining_labor_units,
            remaining_late_expense_cost=remaining_late_expense_cost,
            remaining_late_labor_cost=remaining_late_labor_cost,
            remaining_late_labor_units=remaining_late_labor_units,
            remaining_late_material_cost=remaining_late_material_cost,
            remaining_late_non_labor_cost=remaining_late_non_labor_cost,
            remaining_late_non_labor_units=remaining_late_non_labor_units,
            remaining_late_total_cost=remaining_late_total_cost,
            remaining_material_cost=remaining_material_cost,
            remaining_non_labor_cost=remaining_non_labor_cost,
            remaining_non_labor_units=remaining_non_labor_units,
            remaining_total_cost=remaining_total_cost,
            cumulative_actual_cost=cumulative_actual_cost,
            cumulative_actual_expense_cost=cumulative_actual_expense_cost,
            cumulative_actual_labor_cost=cumulative_actual_labor_cost,
            cumulative_actual_labor_units=cumulative_actual_labor_units,
            cumulative_actual_material_cost=cumulative_actual_material_cost,
            cumulative_actual_non_labor_cost=cumulative_actual_non_labor_cost,
            cumulative_actual_non_labor_units=cumulative_actual_non_labor_units,
            cumulative_actual_total_cost=cumulative_actual_total_cost,
            cumulative_at_completion_expense_cost=cumulative_at_completion_expense_cost,
            cumulative_at_completion_labor_cost=cumulative_at_completion_labor_cost,
            cumulative_at_completion_labor_units=cumulative_at_completion_labor_units,
            cumulative_at_completion_material_cost=cumulative_at_completion_material_cost,
            cumulative_at_completion_non_labor_cost=cumulative_at_completion_non_labor_cost,
            cumulative_at_completion_non_labor_units=cumulative_at_completion_non_labor_units,
            cumulative_at_completion_total_cost=cumulative_at_completion_total_cost,
            cumulative_baseline_1_actual_expense_cost=cumulative_baseline_1_actual_expense_cost,
            cumulative_baseline_1_actual_labor_cost=cumulative_baseline_1_actual_labor_cost,
            cumulative_baseline_1_actual_labor_units=cumulative_baseline_1_actual_labor_units,
            cumulative_baseline_1_actual_material_cost=cumulative_baseline_1_actual_material_cost,
            cumulative_baseline_1_actual_non_labor_cost=cumulative_baseline_1_actual_non_labor_cost,
            cumulative_baseline_1_actual_non_labor_units=cumulative_baseline_1_actual_non_labor_units,
            cumulative_baseline_1_actual_total_cost=cumulative_baseline_1_actual_total_cost,
            cumulative_baseline_1_planned_expense_cost=cumulative_baseline_1_planned_expense_cost,
            cumulative_baseline_1_planned_labor_cost=cumulative_baseline_1_planned_labor_cost,
            cumulative_baseline_1_planned_labor_units=cumulative_baseline_1_planned_labor_units,
            cumulative_baseline_1_planned_material_cost=cumulative_baseline_1_planned_material_cost,
            cumulative_baseline_1_planned_non_labor_cost=cumulative_baseline_1_planned_non_labor_cost,
            cumulative_baseline_1_planned_non_labor_units=cumulative_baseline_1_planned_non_labor_units,
            cumulative_baseline_1_planned_total_cost=cumulative_baseline_1_planned_total_cost,
            cumulative_baseline_actual_expense_cost=cumulative_baseline_actual_expense_cost,
            cumulative_baseline_actual_labor_cost=cumulative_baseline_actual_labor_cost,
            cumulative_baseline_actual_labor_units=cumulative_baseline_actual_labor_units,
            cumulative_baseline_actual_material_cost=cumulative_baseline_actual_material_cost,
            cumulative_baseline_actual_non_labor_cost=cumulative_baseline_actual_non_labor_cost,
            cumulative_baseline_actual_non_labor_units=cumulative_baseline_actual_non_labor_units,
            cumulative_baseline_actual_total_cost=cumulative_baseline_actual_total_cost,
            cumulative_baseline_planned_expense_cost=cumulative_baseline_planned_expense_cost,
            cumulative_baseline_planned_labor_cost=cumulative_baseline_planned_labor_cost,
            cumulative_baseline_planned_labor_units=cumulative_baseline_planned_labor_units,
            cumulative_baseline_planned_material_cost=cumulative_baseline_planned_material_cost,
            cumulative_baseline_planned_non_labor_cost=cumulative_baseline_planned_non_labor_cost,
            cumulative_baseline_planned_non_labor_units=cumulative_baseline_planned_non_labor_units,
            cumulative_baseline_planned_total_cost=cumulative_baseline_planned_total_cost,
            cumulative_earned_value_cost=cumulative_earned_value_cost,
            cumulative_earned_value_labor_units=cumulative_earned_value_labor_units,
            cumulative_estimate_at_completion_cost=cumulative_estimate_at_completion_cost,
            cumulative_estimate_at_completion_labor_units=cumulative_estimate_at_completion_labor_units,
            cumulative_estimate_to_complete_cost=cumulative_estimate_to_complete_cost,
            cumulative_estimate_to_complete_labor_units=cumulative_estimate_to_complete_labor_units,
            cumulative_planned_expense_cost=cumulative_planned_expense_cost,
            cumulative_planned_labor_cost=cumulative_planned_labor_cost,
            cumulative_planned_labor_units=cumulative_planned_labor_units,
            cumulative_planned_material_cost=cumulative_planned_material_cost,
            cumulative_planned_non_labor_cost=cumulative_planned_non_labor_cost,
            cumulative_planned_non_labor_units=cumulative_planned_non_labor_units,
            cumulative_planned_total_cost=cumulative_planned_total_cost,
            cumulative_planned_value_cost=cumulative_planned_value_cost,
            cumulative_planned_value_labor_units=cumulative_planned_value_labor_units,
            cumulative_remaining_expense_cost=cumulative_remaining_expense_cost,
            cumulative_remaining_labor_cost=cumulative_remaining_labor_cost,
            cumulative_remaining_labor_units=cumulative_remaining_labor_units,
            cumulative_remaining_late_expense_cost=cumulative_remaining_late_expense_cost,
            cumulative_remaining_late_labor_cost=cumulative_remaining_late_labor_cost,
            cumulative_remaining_late_labor_units=cumulative_remaining_late_labor_units,
            cumulative_remaining_late_material_cost=cumulative_remaining_late_material_cost,
            cumulative_remaining_late_non_labor_cost=cumulative_remaining_late_non_labor_cost,
            cumulative_remaining_late_non_labor_units=cumulative_remaining_late_non_labor_units,
            cumulative_remaining_late_total_cost=cumulative_remaining_late_total_cost,
            cumulative_remaining_material_cost=cumulative_remaining_material_cost,
            cumulative_remaining_non_labor_cost=cumulative_remaining_non_labor_cost,
            cumulative_remaining_non_labor_units=cumulative_remaining_non_labor_units,
            cumulative_remaining_total_cost=cumulative_remaining_total_cost,
        )

        activity_spread_period.additional_properties = d
        return activity_spread_period

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
