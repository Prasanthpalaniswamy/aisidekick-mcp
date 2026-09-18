from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SummarizedSpreadPeriod")


@_attrs_define
class SummarizedSpreadPeriod:
    """
    Attributes:
        start_date (str | Unset):
        end_date (str | Unset):
        actual_cost (float | Unset):
        actual_expense_cost (float | Unset):
        actual_labor_cost (float | Unset):
        actual_labor_units (float | Unset):
        actual_material_cost (float | Unset):
        actual_nonlabor_cost (float | Unset):
        actual_nonlabor_units (float | Unset):
        actual_total_cost (float | Unset):
        at_completion_expense_cost (float | Unset):
        at_completion_labor_cost (float | Unset):
        at_completion_labor_units (float | Unset):
        at_completion_material_cost (float | Unset):
        at_completion_nonlabor_cost (float | Unset):
        at_completion_nonlabor_units (float | Unset):
        at_completion_total_cost (float | Unset):
        baseline_planned_expense_cost (float | Unset):
        baseline_planned_labor_cost (float | Unset):
        baseline_planned_labor_units (float | Unset):
        baseline_planned_material_cost (float | Unset):
        baseline_planned_nonlabor_cost (float | Unset):
        baseline_planned_nonlabor_units (float | Unset):
        baseline_planned_total_cost (float | Unset):
        earned_value_cost (float | Unset):
        earned_value_labor_units (float | Unset):
        estimate_at_completion_cost (float | Unset):
        estimate_at_completion_labor_units (float | Unset):
        estimate_to_complete_cost (float | Unset):
        estimate_to_complete_labor_units (float | Unset):
        period_actual_cost (float | Unset):
        period_actual_expense_cost (float | Unset):
        period_actual_labor_cost (float | Unset):
        period_actual_labor_units (float | Unset):
        period_actual_material_cost (float | Unset):
        period_actual_non_labor_cost (float | Unset):
        period_actual_non_labor_units (float | Unset):
        period_at_completion_expense_cost (float | Unset):
        period_at_completion_labor_cost (float | Unset):
        period_at_completion_labor_units (float | Unset):
        period_at_completion_material_cost (float | Unset):
        period_at_completion_non_labor_cost (float | Unset):
        period_at_completion_non_labor_units (float | Unset):
        period_at_completion_total_cost (float | Unset):
        period_earned_value_cost (float | Unset):
        period_earned_value_labor_units (float | Unset):
        period_estimate_at_completion_cost (float | Unset):
        period_estimate_at_completion_labor_units (float | Unset):
        period_planned_value_cost (float | Unset):
        period_planned_value_labor_units (float | Unset):
        planned_expense_cost (float | Unset):
        planned_labor_cost (float | Unset):
        planned_labor_units (float | Unset):
        planned_material_cost (float | Unset):
        planned_nonlabor_cost (float | Unset):
        planned_nonlabor_units (float | Unset):
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
        remaining_late_nonlabor_cost (float | Unset):
        remaining_late_nonlabor_units (float | Unset):
        remaining_late_total_cost (float | Unset):
        remaining_material_cost (float | Unset):
        remaining_nonlabor_cost (float | Unset):
        remaining_nonlabor_units (float | Unset):
        remaining_total_cost (float | Unset):
        cumulative_actual_cost (float | Unset):
        cumulative_actual_expense_cost (float | Unset):
        cumulative_actual_labor_cost (float | Unset):
        cumulative_actual_labor_units (float | Unset):
        cumulative_actual_material_cost (float | Unset):
        cumulative_actual_nonlabor_cost (float | Unset):
        cumulative_actual_nonlabor_units (float | Unset):
        cumulative_actual_total_cost (float | Unset):
        cumulative_at_completion_expense_cost (float | Unset):
        cumulative_at_completion_labor_cost (float | Unset):
        cumulative_at_completion_labor_units (float | Unset):
        cumulative_at_completion_material_cost (float | Unset):
        cumulative_at_completion_nonlabor_cost (float | Unset):
        cumulative_at_completion_nonlabor_units (float | Unset):
        cumulative_at_completion_total_cost (float | Unset):
        cumulative_baseline_planned_expense_cost (float | Unset):
        cumulative_baseline_planned_labor_cost (float | Unset):
        cumulative_baseline_planned_labor_units (float | Unset):
        cumulative_baseline_planned_material_cost (float | Unset):
        cumulative_baseline_planned_nonlabor_cost (float | Unset):
        cumulative_baseline_planned_nonlabor_units (float | Unset):
        cumulative_baseline_planned_total_cost (float | Unset):
        cumulative_earned_value_cost (float | Unset):
        cumulative_earned_value_labor_units (float | Unset):
        cumulative_estimate_at_completion_cost (float | Unset):
        cumulative_estimate_at_completion_labor_units (float | Unset):
        cumulative_estimate_to_complete_cost (float | Unset):
        cumulative_estimate_to_complete_labor_units (float | Unset):
        cumulative_limit (float | Unset):
        cumulative_planned_expense_cost (float | Unset):
        cumulative_planned_labor_cost (float | Unset):
        cumulative_planned_labor_units (float | Unset):
        cumulative_planned_material_cost (float | Unset):
        cumulative_planned_nonlabor_cost (float | Unset):
        cumulative_planned_nonlabor_units (float | Unset):
        cumulative_planned_total_cost (float | Unset):
        cumulative_planned_value_cost (float | Unset):
        cumulative_planned_value_labor_units (float | Unset):
        cumulative_period_actual_cost (float | Unset):
        cumulative_period_actual_expense_cost (float | Unset):
        cumulative_period_actual_labor_cost (float | Unset):
        cumulative_period_actual_labor_units (float | Unset):
        cumulative_period_actual_material_cost (float | Unset):
        cumulative_period_actual_non_labor_cost (float | Unset):
        cumulative_period_actual_non_labor_units (float | Unset):
        cumulative_period_at_completion_expense_cost (float | Unset):
        cumulative_period_at_completion_labor_cost (float | Unset):
        cumulative_period_at_completion_labor_units (float | Unset):
        cumulative_period_at_completion_material_cost (float | Unset):
        cumulative_period_at_completion_non_labor_cost (float | Unset):
        cumulative_period_at_completion_non_labor_units (float | Unset):
        cumulative_period_at_completion_total_cost (float | Unset):
        cumulative_period_earned_value_cost (float | Unset):
        cumulative_period_earned_value_labor_units (float | Unset):
        cumulative_period_estimate_at_completion_cost (float | Unset):
        cumulative_period_estimate_at_completion_labor_units (float | Unset):
        cumulative_period_planned_value_cost (float | Unset):
        cumulative_period_planned_value_labor_units (float | Unset):
        cumulative_remaining_expense_cost (float | Unset):
        cumulative_remaining_labor_cost (float | Unset):
        cumulative_remaining_labor_units (float | Unset):
        cumulative_remaining_late_expense_cost (float | Unset):
        cumulative_remaining_late_labor_cost (float | Unset):
        cumulative_remaining_late_labor_units (float | Unset):
        cumulative_remaining_late_material_cost (float | Unset):
        cumulative_remaining_late_nonlabor_cost (float | Unset):
        cumulative_remaining_late_nonlabor_units (float | Unset):
        cumulative_remaining_late_total_cost (float | Unset):
        cumulative_remaining_material_cost (float | Unset):
        cumulative_remaining_nonlabor_cost (float | Unset):
        cumulative_remaining_nonlabor_units (float | Unset):
        cumulative_remaining_total_cost (float | Unset):
    """

    start_date: str | Unset = UNSET
    end_date: str | Unset = UNSET
    actual_cost: float | Unset = UNSET
    actual_expense_cost: float | Unset = UNSET
    actual_labor_cost: float | Unset = UNSET
    actual_labor_units: float | Unset = UNSET
    actual_material_cost: float | Unset = UNSET
    actual_nonlabor_cost: float | Unset = UNSET
    actual_nonlabor_units: float | Unset = UNSET
    actual_total_cost: float | Unset = UNSET
    at_completion_expense_cost: float | Unset = UNSET
    at_completion_labor_cost: float | Unset = UNSET
    at_completion_labor_units: float | Unset = UNSET
    at_completion_material_cost: float | Unset = UNSET
    at_completion_nonlabor_cost: float | Unset = UNSET
    at_completion_nonlabor_units: float | Unset = UNSET
    at_completion_total_cost: float | Unset = UNSET
    baseline_planned_expense_cost: float | Unset = UNSET
    baseline_planned_labor_cost: float | Unset = UNSET
    baseline_planned_labor_units: float | Unset = UNSET
    baseline_planned_material_cost: float | Unset = UNSET
    baseline_planned_nonlabor_cost: float | Unset = UNSET
    baseline_planned_nonlabor_units: float | Unset = UNSET
    baseline_planned_total_cost: float | Unset = UNSET
    earned_value_cost: float | Unset = UNSET
    earned_value_labor_units: float | Unset = UNSET
    estimate_at_completion_cost: float | Unset = UNSET
    estimate_at_completion_labor_units: float | Unset = UNSET
    estimate_to_complete_cost: float | Unset = UNSET
    estimate_to_complete_labor_units: float | Unset = UNSET
    period_actual_cost: float | Unset = UNSET
    period_actual_expense_cost: float | Unset = UNSET
    period_actual_labor_cost: float | Unset = UNSET
    period_actual_labor_units: float | Unset = UNSET
    period_actual_material_cost: float | Unset = UNSET
    period_actual_non_labor_cost: float | Unset = UNSET
    period_actual_non_labor_units: float | Unset = UNSET
    period_at_completion_expense_cost: float | Unset = UNSET
    period_at_completion_labor_cost: float | Unset = UNSET
    period_at_completion_labor_units: float | Unset = UNSET
    period_at_completion_material_cost: float | Unset = UNSET
    period_at_completion_non_labor_cost: float | Unset = UNSET
    period_at_completion_non_labor_units: float | Unset = UNSET
    period_at_completion_total_cost: float | Unset = UNSET
    period_earned_value_cost: float | Unset = UNSET
    period_earned_value_labor_units: float | Unset = UNSET
    period_estimate_at_completion_cost: float | Unset = UNSET
    period_estimate_at_completion_labor_units: float | Unset = UNSET
    period_planned_value_cost: float | Unset = UNSET
    period_planned_value_labor_units: float | Unset = UNSET
    planned_expense_cost: float | Unset = UNSET
    planned_labor_cost: float | Unset = UNSET
    planned_labor_units: float | Unset = UNSET
    planned_material_cost: float | Unset = UNSET
    planned_nonlabor_cost: float | Unset = UNSET
    planned_nonlabor_units: float | Unset = UNSET
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
    remaining_late_nonlabor_cost: float | Unset = UNSET
    remaining_late_nonlabor_units: float | Unset = UNSET
    remaining_late_total_cost: float | Unset = UNSET
    remaining_material_cost: float | Unset = UNSET
    remaining_nonlabor_cost: float | Unset = UNSET
    remaining_nonlabor_units: float | Unset = UNSET
    remaining_total_cost: float | Unset = UNSET
    cumulative_actual_cost: float | Unset = UNSET
    cumulative_actual_expense_cost: float | Unset = UNSET
    cumulative_actual_labor_cost: float | Unset = UNSET
    cumulative_actual_labor_units: float | Unset = UNSET
    cumulative_actual_material_cost: float | Unset = UNSET
    cumulative_actual_nonlabor_cost: float | Unset = UNSET
    cumulative_actual_nonlabor_units: float | Unset = UNSET
    cumulative_actual_total_cost: float | Unset = UNSET
    cumulative_at_completion_expense_cost: float | Unset = UNSET
    cumulative_at_completion_labor_cost: float | Unset = UNSET
    cumulative_at_completion_labor_units: float | Unset = UNSET
    cumulative_at_completion_material_cost: float | Unset = UNSET
    cumulative_at_completion_nonlabor_cost: float | Unset = UNSET
    cumulative_at_completion_nonlabor_units: float | Unset = UNSET
    cumulative_at_completion_total_cost: float | Unset = UNSET
    cumulative_baseline_planned_expense_cost: float | Unset = UNSET
    cumulative_baseline_planned_labor_cost: float | Unset = UNSET
    cumulative_baseline_planned_labor_units: float | Unset = UNSET
    cumulative_baseline_planned_material_cost: float | Unset = UNSET
    cumulative_baseline_planned_nonlabor_cost: float | Unset = UNSET
    cumulative_baseline_planned_nonlabor_units: float | Unset = UNSET
    cumulative_baseline_planned_total_cost: float | Unset = UNSET
    cumulative_earned_value_cost: float | Unset = UNSET
    cumulative_earned_value_labor_units: float | Unset = UNSET
    cumulative_estimate_at_completion_cost: float | Unset = UNSET
    cumulative_estimate_at_completion_labor_units: float | Unset = UNSET
    cumulative_estimate_to_complete_cost: float | Unset = UNSET
    cumulative_estimate_to_complete_labor_units: float | Unset = UNSET
    cumulative_limit: float | Unset = UNSET
    cumulative_planned_expense_cost: float | Unset = UNSET
    cumulative_planned_labor_cost: float | Unset = UNSET
    cumulative_planned_labor_units: float | Unset = UNSET
    cumulative_planned_material_cost: float | Unset = UNSET
    cumulative_planned_nonlabor_cost: float | Unset = UNSET
    cumulative_planned_nonlabor_units: float | Unset = UNSET
    cumulative_planned_total_cost: float | Unset = UNSET
    cumulative_planned_value_cost: float | Unset = UNSET
    cumulative_planned_value_labor_units: float | Unset = UNSET
    cumulative_period_actual_cost: float | Unset = UNSET
    cumulative_period_actual_expense_cost: float | Unset = UNSET
    cumulative_period_actual_labor_cost: float | Unset = UNSET
    cumulative_period_actual_labor_units: float | Unset = UNSET
    cumulative_period_actual_material_cost: float | Unset = UNSET
    cumulative_period_actual_non_labor_cost: float | Unset = UNSET
    cumulative_period_actual_non_labor_units: float | Unset = UNSET
    cumulative_period_at_completion_expense_cost: float | Unset = UNSET
    cumulative_period_at_completion_labor_cost: float | Unset = UNSET
    cumulative_period_at_completion_labor_units: float | Unset = UNSET
    cumulative_period_at_completion_material_cost: float | Unset = UNSET
    cumulative_period_at_completion_non_labor_cost: float | Unset = UNSET
    cumulative_period_at_completion_non_labor_units: float | Unset = UNSET
    cumulative_period_at_completion_total_cost: float | Unset = UNSET
    cumulative_period_earned_value_cost: float | Unset = UNSET
    cumulative_period_earned_value_labor_units: float | Unset = UNSET
    cumulative_period_estimate_at_completion_cost: float | Unset = UNSET
    cumulative_period_estimate_at_completion_labor_units: float | Unset = UNSET
    cumulative_period_planned_value_cost: float | Unset = UNSET
    cumulative_period_planned_value_labor_units: float | Unset = UNSET
    cumulative_remaining_expense_cost: float | Unset = UNSET
    cumulative_remaining_labor_cost: float | Unset = UNSET
    cumulative_remaining_labor_units: float | Unset = UNSET
    cumulative_remaining_late_expense_cost: float | Unset = UNSET
    cumulative_remaining_late_labor_cost: float | Unset = UNSET
    cumulative_remaining_late_labor_units: float | Unset = UNSET
    cumulative_remaining_late_material_cost: float | Unset = UNSET
    cumulative_remaining_late_nonlabor_cost: float | Unset = UNSET
    cumulative_remaining_late_nonlabor_units: float | Unset = UNSET
    cumulative_remaining_late_total_cost: float | Unset = UNSET
    cumulative_remaining_material_cost: float | Unset = UNSET
    cumulative_remaining_nonlabor_cost: float | Unset = UNSET
    cumulative_remaining_nonlabor_units: float | Unset = UNSET
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

        actual_nonlabor_cost = self.actual_nonlabor_cost

        actual_nonlabor_units = self.actual_nonlabor_units

        actual_total_cost = self.actual_total_cost

        at_completion_expense_cost = self.at_completion_expense_cost

        at_completion_labor_cost = self.at_completion_labor_cost

        at_completion_labor_units = self.at_completion_labor_units

        at_completion_material_cost = self.at_completion_material_cost

        at_completion_nonlabor_cost = self.at_completion_nonlabor_cost

        at_completion_nonlabor_units = self.at_completion_nonlabor_units

        at_completion_total_cost = self.at_completion_total_cost

        baseline_planned_expense_cost = self.baseline_planned_expense_cost

        baseline_planned_labor_cost = self.baseline_planned_labor_cost

        baseline_planned_labor_units = self.baseline_planned_labor_units

        baseline_planned_material_cost = self.baseline_planned_material_cost

        baseline_planned_nonlabor_cost = self.baseline_planned_nonlabor_cost

        baseline_planned_nonlabor_units = self.baseline_planned_nonlabor_units

        baseline_planned_total_cost = self.baseline_planned_total_cost

        earned_value_cost = self.earned_value_cost

        earned_value_labor_units = self.earned_value_labor_units

        estimate_at_completion_cost = self.estimate_at_completion_cost

        estimate_at_completion_labor_units = self.estimate_at_completion_labor_units

        estimate_to_complete_cost = self.estimate_to_complete_cost

        estimate_to_complete_labor_units = self.estimate_to_complete_labor_units

        period_actual_cost = self.period_actual_cost

        period_actual_expense_cost = self.period_actual_expense_cost

        period_actual_labor_cost = self.period_actual_labor_cost

        period_actual_labor_units = self.period_actual_labor_units

        period_actual_material_cost = self.period_actual_material_cost

        period_actual_non_labor_cost = self.period_actual_non_labor_cost

        period_actual_non_labor_units = self.period_actual_non_labor_units

        period_at_completion_expense_cost = self.period_at_completion_expense_cost

        period_at_completion_labor_cost = self.period_at_completion_labor_cost

        period_at_completion_labor_units = self.period_at_completion_labor_units

        period_at_completion_material_cost = self.period_at_completion_material_cost

        period_at_completion_non_labor_cost = self.period_at_completion_non_labor_cost

        period_at_completion_non_labor_units = self.period_at_completion_non_labor_units

        period_at_completion_total_cost = self.period_at_completion_total_cost

        period_earned_value_cost = self.period_earned_value_cost

        period_earned_value_labor_units = self.period_earned_value_labor_units

        period_estimate_at_completion_cost = self.period_estimate_at_completion_cost

        period_estimate_at_completion_labor_units = self.period_estimate_at_completion_labor_units

        period_planned_value_cost = self.period_planned_value_cost

        period_planned_value_labor_units = self.period_planned_value_labor_units

        planned_expense_cost = self.planned_expense_cost

        planned_labor_cost = self.planned_labor_cost

        planned_labor_units = self.planned_labor_units

        planned_material_cost = self.planned_material_cost

        planned_nonlabor_cost = self.planned_nonlabor_cost

        planned_nonlabor_units = self.planned_nonlabor_units

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

        remaining_late_nonlabor_cost = self.remaining_late_nonlabor_cost

        remaining_late_nonlabor_units = self.remaining_late_nonlabor_units

        remaining_late_total_cost = self.remaining_late_total_cost

        remaining_material_cost = self.remaining_material_cost

        remaining_nonlabor_cost = self.remaining_nonlabor_cost

        remaining_nonlabor_units = self.remaining_nonlabor_units

        remaining_total_cost = self.remaining_total_cost

        cumulative_actual_cost = self.cumulative_actual_cost

        cumulative_actual_expense_cost = self.cumulative_actual_expense_cost

        cumulative_actual_labor_cost = self.cumulative_actual_labor_cost

        cumulative_actual_labor_units = self.cumulative_actual_labor_units

        cumulative_actual_material_cost = self.cumulative_actual_material_cost

        cumulative_actual_nonlabor_cost = self.cumulative_actual_nonlabor_cost

        cumulative_actual_nonlabor_units = self.cumulative_actual_nonlabor_units

        cumulative_actual_total_cost = self.cumulative_actual_total_cost

        cumulative_at_completion_expense_cost = self.cumulative_at_completion_expense_cost

        cumulative_at_completion_labor_cost = self.cumulative_at_completion_labor_cost

        cumulative_at_completion_labor_units = self.cumulative_at_completion_labor_units

        cumulative_at_completion_material_cost = self.cumulative_at_completion_material_cost

        cumulative_at_completion_nonlabor_cost = self.cumulative_at_completion_nonlabor_cost

        cumulative_at_completion_nonlabor_units = self.cumulative_at_completion_nonlabor_units

        cumulative_at_completion_total_cost = self.cumulative_at_completion_total_cost

        cumulative_baseline_planned_expense_cost = self.cumulative_baseline_planned_expense_cost

        cumulative_baseline_planned_labor_cost = self.cumulative_baseline_planned_labor_cost

        cumulative_baseline_planned_labor_units = self.cumulative_baseline_planned_labor_units

        cumulative_baseline_planned_material_cost = self.cumulative_baseline_planned_material_cost

        cumulative_baseline_planned_nonlabor_cost = self.cumulative_baseline_planned_nonlabor_cost

        cumulative_baseline_planned_nonlabor_units = self.cumulative_baseline_planned_nonlabor_units

        cumulative_baseline_planned_total_cost = self.cumulative_baseline_planned_total_cost

        cumulative_earned_value_cost = self.cumulative_earned_value_cost

        cumulative_earned_value_labor_units = self.cumulative_earned_value_labor_units

        cumulative_estimate_at_completion_cost = self.cumulative_estimate_at_completion_cost

        cumulative_estimate_at_completion_labor_units = self.cumulative_estimate_at_completion_labor_units

        cumulative_estimate_to_complete_cost = self.cumulative_estimate_to_complete_cost

        cumulative_estimate_to_complete_labor_units = self.cumulative_estimate_to_complete_labor_units

        cumulative_limit = self.cumulative_limit

        cumulative_planned_expense_cost = self.cumulative_planned_expense_cost

        cumulative_planned_labor_cost = self.cumulative_planned_labor_cost

        cumulative_planned_labor_units = self.cumulative_planned_labor_units

        cumulative_planned_material_cost = self.cumulative_planned_material_cost

        cumulative_planned_nonlabor_cost = self.cumulative_planned_nonlabor_cost

        cumulative_planned_nonlabor_units = self.cumulative_planned_nonlabor_units

        cumulative_planned_total_cost = self.cumulative_planned_total_cost

        cumulative_planned_value_cost = self.cumulative_planned_value_cost

        cumulative_planned_value_labor_units = self.cumulative_planned_value_labor_units

        cumulative_period_actual_cost = self.cumulative_period_actual_cost

        cumulative_period_actual_expense_cost = self.cumulative_period_actual_expense_cost

        cumulative_period_actual_labor_cost = self.cumulative_period_actual_labor_cost

        cumulative_period_actual_labor_units = self.cumulative_period_actual_labor_units

        cumulative_period_actual_material_cost = self.cumulative_period_actual_material_cost

        cumulative_period_actual_non_labor_cost = self.cumulative_period_actual_non_labor_cost

        cumulative_period_actual_non_labor_units = self.cumulative_period_actual_non_labor_units

        cumulative_period_at_completion_expense_cost = self.cumulative_period_at_completion_expense_cost

        cumulative_period_at_completion_labor_cost = self.cumulative_period_at_completion_labor_cost

        cumulative_period_at_completion_labor_units = self.cumulative_period_at_completion_labor_units

        cumulative_period_at_completion_material_cost = self.cumulative_period_at_completion_material_cost

        cumulative_period_at_completion_non_labor_cost = self.cumulative_period_at_completion_non_labor_cost

        cumulative_period_at_completion_non_labor_units = self.cumulative_period_at_completion_non_labor_units

        cumulative_period_at_completion_total_cost = self.cumulative_period_at_completion_total_cost

        cumulative_period_earned_value_cost = self.cumulative_period_earned_value_cost

        cumulative_period_earned_value_labor_units = self.cumulative_period_earned_value_labor_units

        cumulative_period_estimate_at_completion_cost = self.cumulative_period_estimate_at_completion_cost

        cumulative_period_estimate_at_completion_labor_units = self.cumulative_period_estimate_at_completion_labor_units

        cumulative_period_planned_value_cost = self.cumulative_period_planned_value_cost

        cumulative_period_planned_value_labor_units = self.cumulative_period_planned_value_labor_units

        cumulative_remaining_expense_cost = self.cumulative_remaining_expense_cost

        cumulative_remaining_labor_cost = self.cumulative_remaining_labor_cost

        cumulative_remaining_labor_units = self.cumulative_remaining_labor_units

        cumulative_remaining_late_expense_cost = self.cumulative_remaining_late_expense_cost

        cumulative_remaining_late_labor_cost = self.cumulative_remaining_late_labor_cost

        cumulative_remaining_late_labor_units = self.cumulative_remaining_late_labor_units

        cumulative_remaining_late_material_cost = self.cumulative_remaining_late_material_cost

        cumulative_remaining_late_nonlabor_cost = self.cumulative_remaining_late_nonlabor_cost

        cumulative_remaining_late_nonlabor_units = self.cumulative_remaining_late_nonlabor_units

        cumulative_remaining_late_total_cost = self.cumulative_remaining_late_total_cost

        cumulative_remaining_material_cost = self.cumulative_remaining_material_cost

        cumulative_remaining_nonlabor_cost = self.cumulative_remaining_nonlabor_cost

        cumulative_remaining_nonlabor_units = self.cumulative_remaining_nonlabor_units

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
        if actual_nonlabor_cost is not UNSET:
            field_dict["ActualNonlaborCost"] = actual_nonlabor_cost
        if actual_nonlabor_units is not UNSET:
            field_dict["ActualNonlaborUnits"] = actual_nonlabor_units
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
        if at_completion_nonlabor_cost is not UNSET:
            field_dict["AtCompletionNonlaborCost"] = at_completion_nonlabor_cost
        if at_completion_nonlabor_units is not UNSET:
            field_dict["AtCompletionNonlaborUnits"] = at_completion_nonlabor_units
        if at_completion_total_cost is not UNSET:
            field_dict["AtCompletionTotalCost"] = at_completion_total_cost
        if baseline_planned_expense_cost is not UNSET:
            field_dict["BaselinePlannedExpenseCost"] = baseline_planned_expense_cost
        if baseline_planned_labor_cost is not UNSET:
            field_dict["BaselinePlannedLaborCost"] = baseline_planned_labor_cost
        if baseline_planned_labor_units is not UNSET:
            field_dict["BaselinePlannedLaborUnits"] = baseline_planned_labor_units
        if baseline_planned_material_cost is not UNSET:
            field_dict["BaselinePlannedMaterialCost"] = baseline_planned_material_cost
        if baseline_planned_nonlabor_cost is not UNSET:
            field_dict["BaselinePlannedNonlaborCost"] = baseline_planned_nonlabor_cost
        if baseline_planned_nonlabor_units is not UNSET:
            field_dict["BaselinePlannedNonlaborUnits"] = baseline_planned_nonlabor_units
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
        if period_actual_cost is not UNSET:
            field_dict["PeriodActualCost"] = period_actual_cost
        if period_actual_expense_cost is not UNSET:
            field_dict["PeriodActualExpenseCost"] = period_actual_expense_cost
        if period_actual_labor_cost is not UNSET:
            field_dict["PeriodActualLaborCost"] = period_actual_labor_cost
        if period_actual_labor_units is not UNSET:
            field_dict["PeriodActualLaborUnits"] = period_actual_labor_units
        if period_actual_material_cost is not UNSET:
            field_dict["PeriodActualMaterialCost"] = period_actual_material_cost
        if period_actual_non_labor_cost is not UNSET:
            field_dict["PeriodActualNonLaborCost"] = period_actual_non_labor_cost
        if period_actual_non_labor_units is not UNSET:
            field_dict["PeriodActualNonLaborUnits"] = period_actual_non_labor_units
        if period_at_completion_expense_cost is not UNSET:
            field_dict["PeriodAtCompletionExpenseCost"] = period_at_completion_expense_cost
        if period_at_completion_labor_cost is not UNSET:
            field_dict["PeriodAtCompletionLaborCost"] = period_at_completion_labor_cost
        if period_at_completion_labor_units is not UNSET:
            field_dict["PeriodAtCompletionLaborUnits"] = period_at_completion_labor_units
        if period_at_completion_material_cost is not UNSET:
            field_dict["PeriodAtCompletionMaterialCost"] = period_at_completion_material_cost
        if period_at_completion_non_labor_cost is not UNSET:
            field_dict["PeriodAtCompletionNonLaborCost"] = period_at_completion_non_labor_cost
        if period_at_completion_non_labor_units is not UNSET:
            field_dict["PeriodAtCompletionNonLaborUnits"] = period_at_completion_non_labor_units
        if period_at_completion_total_cost is not UNSET:
            field_dict["PeriodAtCompletionTotalCost"] = period_at_completion_total_cost
        if period_earned_value_cost is not UNSET:
            field_dict["PeriodEarnedValueCost"] = period_earned_value_cost
        if period_earned_value_labor_units is not UNSET:
            field_dict["PeriodEarnedValueLaborUnits"] = period_earned_value_labor_units
        if period_estimate_at_completion_cost is not UNSET:
            field_dict["PeriodEstimateAtCompletionCost"] = period_estimate_at_completion_cost
        if period_estimate_at_completion_labor_units is not UNSET:
            field_dict["PeriodEstimateAtCompletionLaborUnits"] = period_estimate_at_completion_labor_units
        if period_planned_value_cost is not UNSET:
            field_dict["PeriodPlannedValueCost"] = period_planned_value_cost
        if period_planned_value_labor_units is not UNSET:
            field_dict["PeriodPlannedValueLaborUnits"] = period_planned_value_labor_units
        if planned_expense_cost is not UNSET:
            field_dict["PlannedExpenseCost"] = planned_expense_cost
        if planned_labor_cost is not UNSET:
            field_dict["PlannedLaborCost"] = planned_labor_cost
        if planned_labor_units is not UNSET:
            field_dict["PlannedLaborUnits"] = planned_labor_units
        if planned_material_cost is not UNSET:
            field_dict["PlannedMaterialCost"] = planned_material_cost
        if planned_nonlabor_cost is not UNSET:
            field_dict["PlannedNonlaborCost"] = planned_nonlabor_cost
        if planned_nonlabor_units is not UNSET:
            field_dict["PlannedNonlaborUnits"] = planned_nonlabor_units
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
        if remaining_late_nonlabor_cost is not UNSET:
            field_dict["RemainingLateNonlaborCost"] = remaining_late_nonlabor_cost
        if remaining_late_nonlabor_units is not UNSET:
            field_dict["RemainingLateNonlaborUnits"] = remaining_late_nonlabor_units
        if remaining_late_total_cost is not UNSET:
            field_dict["RemainingLateTotalCost"] = remaining_late_total_cost
        if remaining_material_cost is not UNSET:
            field_dict["RemainingMaterialCost"] = remaining_material_cost
        if remaining_nonlabor_cost is not UNSET:
            field_dict["RemainingNonlaborCost"] = remaining_nonlabor_cost
        if remaining_nonlabor_units is not UNSET:
            field_dict["RemainingNonlaborUnits"] = remaining_nonlabor_units
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
        if cumulative_actual_nonlabor_cost is not UNSET:
            field_dict["CumulativeActualNonlaborCost"] = cumulative_actual_nonlabor_cost
        if cumulative_actual_nonlabor_units is not UNSET:
            field_dict["CumulativeActualNonlaborUnits"] = cumulative_actual_nonlabor_units
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
        if cumulative_at_completion_nonlabor_cost is not UNSET:
            field_dict["CumulativeAtCompletionNonlaborCost"] = cumulative_at_completion_nonlabor_cost
        if cumulative_at_completion_nonlabor_units is not UNSET:
            field_dict["CumulativeAtCompletionNonlaborUnits"] = cumulative_at_completion_nonlabor_units
        if cumulative_at_completion_total_cost is not UNSET:
            field_dict["CumulativeAtCompletionTotalCost"] = cumulative_at_completion_total_cost
        if cumulative_baseline_planned_expense_cost is not UNSET:
            field_dict["CumulativeBaselinePlannedExpenseCost"] = cumulative_baseline_planned_expense_cost
        if cumulative_baseline_planned_labor_cost is not UNSET:
            field_dict["CumulativeBaselinePlannedLaborCost"] = cumulative_baseline_planned_labor_cost
        if cumulative_baseline_planned_labor_units is not UNSET:
            field_dict["CumulativeBaselinePlannedLaborUnits"] = cumulative_baseline_planned_labor_units
        if cumulative_baseline_planned_material_cost is not UNSET:
            field_dict["CumulativeBaselinePlannedMaterialCost"] = cumulative_baseline_planned_material_cost
        if cumulative_baseline_planned_nonlabor_cost is not UNSET:
            field_dict["CumulativeBaselinePlannedNonlaborCost"] = cumulative_baseline_planned_nonlabor_cost
        if cumulative_baseline_planned_nonlabor_units is not UNSET:
            field_dict["CumulativeBaselinePlannedNonlaborUnits"] = cumulative_baseline_planned_nonlabor_units
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
        if cumulative_limit is not UNSET:
            field_dict["CumulativeLimit"] = cumulative_limit
        if cumulative_planned_expense_cost is not UNSET:
            field_dict["CumulativePlannedExpenseCost"] = cumulative_planned_expense_cost
        if cumulative_planned_labor_cost is not UNSET:
            field_dict["CumulativePlannedLaborCost"] = cumulative_planned_labor_cost
        if cumulative_planned_labor_units is not UNSET:
            field_dict["CumulativePlannedLaborUnits"] = cumulative_planned_labor_units
        if cumulative_planned_material_cost is not UNSET:
            field_dict["CumulativePlannedMaterialCost"] = cumulative_planned_material_cost
        if cumulative_planned_nonlabor_cost is not UNSET:
            field_dict["CumulativePlannedNonlaborCost"] = cumulative_planned_nonlabor_cost
        if cumulative_planned_nonlabor_units is not UNSET:
            field_dict["CumulativePlannedNonlaborUnits"] = cumulative_planned_nonlabor_units
        if cumulative_planned_total_cost is not UNSET:
            field_dict["CumulativePlannedTotalCost"] = cumulative_planned_total_cost
        if cumulative_planned_value_cost is not UNSET:
            field_dict["CumulativePlannedValueCost"] = cumulative_planned_value_cost
        if cumulative_planned_value_labor_units is not UNSET:
            field_dict["CumulativePlannedValueLaborUnits"] = cumulative_planned_value_labor_units
        if cumulative_period_actual_cost is not UNSET:
            field_dict["CumulativePeriodActualCost"] = cumulative_period_actual_cost
        if cumulative_period_actual_expense_cost is not UNSET:
            field_dict["CumulativePeriodActualExpenseCost"] = cumulative_period_actual_expense_cost
        if cumulative_period_actual_labor_cost is not UNSET:
            field_dict["CumulativePeriodActualLaborCost"] = cumulative_period_actual_labor_cost
        if cumulative_period_actual_labor_units is not UNSET:
            field_dict["CumulativePeriodActualLaborUnits"] = cumulative_period_actual_labor_units
        if cumulative_period_actual_material_cost is not UNSET:
            field_dict["CumulativePeriodActualMaterialCost"] = cumulative_period_actual_material_cost
        if cumulative_period_actual_non_labor_cost is not UNSET:
            field_dict["CumulativePeriodActualNonLaborCost"] = cumulative_period_actual_non_labor_cost
        if cumulative_period_actual_non_labor_units is not UNSET:
            field_dict["CumulativePeriodActualNonLaborUnits"] = cumulative_period_actual_non_labor_units
        if cumulative_period_at_completion_expense_cost is not UNSET:
            field_dict["CumulativePeriodAtCompletionExpenseCost"] = cumulative_period_at_completion_expense_cost
        if cumulative_period_at_completion_labor_cost is not UNSET:
            field_dict["CumulativePeriodAtCompletionLaborCost"] = cumulative_period_at_completion_labor_cost
        if cumulative_period_at_completion_labor_units is not UNSET:
            field_dict["CumulativePeriodAtCompletionLaborUnits"] = cumulative_period_at_completion_labor_units
        if cumulative_period_at_completion_material_cost is not UNSET:
            field_dict["CumulativePeriodAtCompletionMaterialCost"] = cumulative_period_at_completion_material_cost
        if cumulative_period_at_completion_non_labor_cost is not UNSET:
            field_dict["CumulativePeriodAtCompletionNonLaborCost"] = cumulative_period_at_completion_non_labor_cost
        if cumulative_period_at_completion_non_labor_units is not UNSET:
            field_dict["CumulativePeriodAtCompletionNonLaborUnits"] = cumulative_period_at_completion_non_labor_units
        if cumulative_period_at_completion_total_cost is not UNSET:
            field_dict["CumulativePeriodAtCompletionTotalCost"] = cumulative_period_at_completion_total_cost
        if cumulative_period_earned_value_cost is not UNSET:
            field_dict["CumulativePeriodEarnedValueCost"] = cumulative_period_earned_value_cost
        if cumulative_period_earned_value_labor_units is not UNSET:
            field_dict["CumulativePeriodEarnedValueLaborUnits"] = cumulative_period_earned_value_labor_units
        if cumulative_period_estimate_at_completion_cost is not UNSET:
            field_dict["CumulativePeriodEstimateAtCompletionCost"] = cumulative_period_estimate_at_completion_cost
        if cumulative_period_estimate_at_completion_labor_units is not UNSET:
            field_dict["CumulativePeriodEstimateAtCompletionLaborUnits"] = (
                cumulative_period_estimate_at_completion_labor_units
            )
        if cumulative_period_planned_value_cost is not UNSET:
            field_dict["CumulativePeriodPlannedValueCost"] = cumulative_period_planned_value_cost
        if cumulative_period_planned_value_labor_units is not UNSET:
            field_dict["CumulativePeriodPlannedValueLaborUnits"] = cumulative_period_planned_value_labor_units
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
        if cumulative_remaining_late_nonlabor_cost is not UNSET:
            field_dict["CumulativeRemainingLateNonlaborCost"] = cumulative_remaining_late_nonlabor_cost
        if cumulative_remaining_late_nonlabor_units is not UNSET:
            field_dict["CumulativeRemainingLateNonlaborUnits"] = cumulative_remaining_late_nonlabor_units
        if cumulative_remaining_late_total_cost is not UNSET:
            field_dict["CumulativeRemainingLateTotalCost"] = cumulative_remaining_late_total_cost
        if cumulative_remaining_material_cost is not UNSET:
            field_dict["CumulativeRemainingMaterialCost"] = cumulative_remaining_material_cost
        if cumulative_remaining_nonlabor_cost is not UNSET:
            field_dict["CumulativeRemainingNonlaborCost"] = cumulative_remaining_nonlabor_cost
        if cumulative_remaining_nonlabor_units is not UNSET:
            field_dict["CumulativeRemainingNonlaborUnits"] = cumulative_remaining_nonlabor_units
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

        actual_nonlabor_cost = d.pop("ActualNonlaborCost", UNSET)

        actual_nonlabor_units = d.pop("ActualNonlaborUnits", UNSET)

        actual_total_cost = d.pop("ActualTotalCost", UNSET)

        at_completion_expense_cost = d.pop("AtCompletionExpenseCost", UNSET)

        at_completion_labor_cost = d.pop("AtCompletionLaborCost", UNSET)

        at_completion_labor_units = d.pop("AtCompletionLaborUnits", UNSET)

        at_completion_material_cost = d.pop("AtCompletionMaterialCost", UNSET)

        at_completion_nonlabor_cost = d.pop("AtCompletionNonlaborCost", UNSET)

        at_completion_nonlabor_units = d.pop("AtCompletionNonlaborUnits", UNSET)

        at_completion_total_cost = d.pop("AtCompletionTotalCost", UNSET)

        baseline_planned_expense_cost = d.pop("BaselinePlannedExpenseCost", UNSET)

        baseline_planned_labor_cost = d.pop("BaselinePlannedLaborCost", UNSET)

        baseline_planned_labor_units = d.pop("BaselinePlannedLaborUnits", UNSET)

        baseline_planned_material_cost = d.pop("BaselinePlannedMaterialCost", UNSET)

        baseline_planned_nonlabor_cost = d.pop("BaselinePlannedNonlaborCost", UNSET)

        baseline_planned_nonlabor_units = d.pop("BaselinePlannedNonlaborUnits", UNSET)

        baseline_planned_total_cost = d.pop("BaselinePlannedTotalCost", UNSET)

        earned_value_cost = d.pop("EarnedValueCost", UNSET)

        earned_value_labor_units = d.pop("EarnedValueLaborUnits", UNSET)

        estimate_at_completion_cost = d.pop("EstimateAtCompletionCost", UNSET)

        estimate_at_completion_labor_units = d.pop("EstimateAtCompletionLaborUnits", UNSET)

        estimate_to_complete_cost = d.pop("EstimateToCompleteCost", UNSET)

        estimate_to_complete_labor_units = d.pop("EstimateToCompleteLaborUnits", UNSET)

        period_actual_cost = d.pop("PeriodActualCost", UNSET)

        period_actual_expense_cost = d.pop("PeriodActualExpenseCost", UNSET)

        period_actual_labor_cost = d.pop("PeriodActualLaborCost", UNSET)

        period_actual_labor_units = d.pop("PeriodActualLaborUnits", UNSET)

        period_actual_material_cost = d.pop("PeriodActualMaterialCost", UNSET)

        period_actual_non_labor_cost = d.pop("PeriodActualNonLaborCost", UNSET)

        period_actual_non_labor_units = d.pop("PeriodActualNonLaborUnits", UNSET)

        period_at_completion_expense_cost = d.pop("PeriodAtCompletionExpenseCost", UNSET)

        period_at_completion_labor_cost = d.pop("PeriodAtCompletionLaborCost", UNSET)

        period_at_completion_labor_units = d.pop("PeriodAtCompletionLaborUnits", UNSET)

        period_at_completion_material_cost = d.pop("PeriodAtCompletionMaterialCost", UNSET)

        period_at_completion_non_labor_cost = d.pop("PeriodAtCompletionNonLaborCost", UNSET)

        period_at_completion_non_labor_units = d.pop("PeriodAtCompletionNonLaborUnits", UNSET)

        period_at_completion_total_cost = d.pop("PeriodAtCompletionTotalCost", UNSET)

        period_earned_value_cost = d.pop("PeriodEarnedValueCost", UNSET)

        period_earned_value_labor_units = d.pop("PeriodEarnedValueLaborUnits", UNSET)

        period_estimate_at_completion_cost = d.pop("PeriodEstimateAtCompletionCost", UNSET)

        period_estimate_at_completion_labor_units = d.pop("PeriodEstimateAtCompletionLaborUnits", UNSET)

        period_planned_value_cost = d.pop("PeriodPlannedValueCost", UNSET)

        period_planned_value_labor_units = d.pop("PeriodPlannedValueLaborUnits", UNSET)

        planned_expense_cost = d.pop("PlannedExpenseCost", UNSET)

        planned_labor_cost = d.pop("PlannedLaborCost", UNSET)

        planned_labor_units = d.pop("PlannedLaborUnits", UNSET)

        planned_material_cost = d.pop("PlannedMaterialCost", UNSET)

        planned_nonlabor_cost = d.pop("PlannedNonlaborCost", UNSET)

        planned_nonlabor_units = d.pop("PlannedNonlaborUnits", UNSET)

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

        remaining_late_nonlabor_cost = d.pop("RemainingLateNonlaborCost", UNSET)

        remaining_late_nonlabor_units = d.pop("RemainingLateNonlaborUnits", UNSET)

        remaining_late_total_cost = d.pop("RemainingLateTotalCost", UNSET)

        remaining_material_cost = d.pop("RemainingMaterialCost", UNSET)

        remaining_nonlabor_cost = d.pop("RemainingNonlaborCost", UNSET)

        remaining_nonlabor_units = d.pop("RemainingNonlaborUnits", UNSET)

        remaining_total_cost = d.pop("RemainingTotalCost", UNSET)

        cumulative_actual_cost = d.pop("CumulativeActualCost", UNSET)

        cumulative_actual_expense_cost = d.pop("CumulativeActualExpenseCost", UNSET)

        cumulative_actual_labor_cost = d.pop("CumulativeActualLaborCost", UNSET)

        cumulative_actual_labor_units = d.pop("CumulativeActualLaborUnits", UNSET)

        cumulative_actual_material_cost = d.pop("CumulativeActualMaterialCost", UNSET)

        cumulative_actual_nonlabor_cost = d.pop("CumulativeActualNonlaborCost", UNSET)

        cumulative_actual_nonlabor_units = d.pop("CumulativeActualNonlaborUnits", UNSET)

        cumulative_actual_total_cost = d.pop("CumulativeActualTotalCost", UNSET)

        cumulative_at_completion_expense_cost = d.pop("CumulativeAtCompletionExpenseCost", UNSET)

        cumulative_at_completion_labor_cost = d.pop("CumulativeAtCompletionLaborCost", UNSET)

        cumulative_at_completion_labor_units = d.pop("CumulativeAtCompletionLaborUnits", UNSET)

        cumulative_at_completion_material_cost = d.pop("CumulativeAtCompletionMaterialCost", UNSET)

        cumulative_at_completion_nonlabor_cost = d.pop("CumulativeAtCompletionNonlaborCost", UNSET)

        cumulative_at_completion_nonlabor_units = d.pop("CumulativeAtCompletionNonlaborUnits", UNSET)

        cumulative_at_completion_total_cost = d.pop("CumulativeAtCompletionTotalCost", UNSET)

        cumulative_baseline_planned_expense_cost = d.pop("CumulativeBaselinePlannedExpenseCost", UNSET)

        cumulative_baseline_planned_labor_cost = d.pop("CumulativeBaselinePlannedLaborCost", UNSET)

        cumulative_baseline_planned_labor_units = d.pop("CumulativeBaselinePlannedLaborUnits", UNSET)

        cumulative_baseline_planned_material_cost = d.pop("CumulativeBaselinePlannedMaterialCost", UNSET)

        cumulative_baseline_planned_nonlabor_cost = d.pop("CumulativeBaselinePlannedNonlaborCost", UNSET)

        cumulative_baseline_planned_nonlabor_units = d.pop("CumulativeBaselinePlannedNonlaborUnits", UNSET)

        cumulative_baseline_planned_total_cost = d.pop("CumulativeBaselinePlannedTotalCost", UNSET)

        cumulative_earned_value_cost = d.pop("CumulativeEarnedValueCost", UNSET)

        cumulative_earned_value_labor_units = d.pop("CumulativeEarnedValueLaborUnits", UNSET)

        cumulative_estimate_at_completion_cost = d.pop("CumulativeEstimateAtCompletionCost", UNSET)

        cumulative_estimate_at_completion_labor_units = d.pop("CumulativeEstimateAtCompletionLaborUnits", UNSET)

        cumulative_estimate_to_complete_cost = d.pop("CumulativeEstimateToCompleteCost", UNSET)

        cumulative_estimate_to_complete_labor_units = d.pop("CumulativeEstimateToCompleteLaborUnits", UNSET)

        cumulative_limit = d.pop("CumulativeLimit", UNSET)

        cumulative_planned_expense_cost = d.pop("CumulativePlannedExpenseCost", UNSET)

        cumulative_planned_labor_cost = d.pop("CumulativePlannedLaborCost", UNSET)

        cumulative_planned_labor_units = d.pop("CumulativePlannedLaborUnits", UNSET)

        cumulative_planned_material_cost = d.pop("CumulativePlannedMaterialCost", UNSET)

        cumulative_planned_nonlabor_cost = d.pop("CumulativePlannedNonlaborCost", UNSET)

        cumulative_planned_nonlabor_units = d.pop("CumulativePlannedNonlaborUnits", UNSET)

        cumulative_planned_total_cost = d.pop("CumulativePlannedTotalCost", UNSET)

        cumulative_planned_value_cost = d.pop("CumulativePlannedValueCost", UNSET)

        cumulative_planned_value_labor_units = d.pop("CumulativePlannedValueLaborUnits", UNSET)

        cumulative_period_actual_cost = d.pop("CumulativePeriodActualCost", UNSET)

        cumulative_period_actual_expense_cost = d.pop("CumulativePeriodActualExpenseCost", UNSET)

        cumulative_period_actual_labor_cost = d.pop("CumulativePeriodActualLaborCost", UNSET)

        cumulative_period_actual_labor_units = d.pop("CumulativePeriodActualLaborUnits", UNSET)

        cumulative_period_actual_material_cost = d.pop("CumulativePeriodActualMaterialCost", UNSET)

        cumulative_period_actual_non_labor_cost = d.pop("CumulativePeriodActualNonLaborCost", UNSET)

        cumulative_period_actual_non_labor_units = d.pop("CumulativePeriodActualNonLaborUnits", UNSET)

        cumulative_period_at_completion_expense_cost = d.pop("CumulativePeriodAtCompletionExpenseCost", UNSET)

        cumulative_period_at_completion_labor_cost = d.pop("CumulativePeriodAtCompletionLaborCost", UNSET)

        cumulative_period_at_completion_labor_units = d.pop("CumulativePeriodAtCompletionLaborUnits", UNSET)

        cumulative_period_at_completion_material_cost = d.pop("CumulativePeriodAtCompletionMaterialCost", UNSET)

        cumulative_period_at_completion_non_labor_cost = d.pop("CumulativePeriodAtCompletionNonLaborCost", UNSET)

        cumulative_period_at_completion_non_labor_units = d.pop("CumulativePeriodAtCompletionNonLaborUnits", UNSET)

        cumulative_period_at_completion_total_cost = d.pop("CumulativePeriodAtCompletionTotalCost", UNSET)

        cumulative_period_earned_value_cost = d.pop("CumulativePeriodEarnedValueCost", UNSET)

        cumulative_period_earned_value_labor_units = d.pop("CumulativePeriodEarnedValueLaborUnits", UNSET)

        cumulative_period_estimate_at_completion_cost = d.pop("CumulativePeriodEstimateAtCompletionCost", UNSET)

        cumulative_period_estimate_at_completion_labor_units = d.pop(
            "CumulativePeriodEstimateAtCompletionLaborUnits", UNSET
        )

        cumulative_period_planned_value_cost = d.pop("CumulativePeriodPlannedValueCost", UNSET)

        cumulative_period_planned_value_labor_units = d.pop("CumulativePeriodPlannedValueLaborUnits", UNSET)

        cumulative_remaining_expense_cost = d.pop("CumulativeRemainingExpenseCost", UNSET)

        cumulative_remaining_labor_cost = d.pop("CumulativeRemainingLaborCost", UNSET)

        cumulative_remaining_labor_units = d.pop("CumulativeRemainingLaborUnits", UNSET)

        cumulative_remaining_late_expense_cost = d.pop("CumulativeRemainingLateExpenseCost", UNSET)

        cumulative_remaining_late_labor_cost = d.pop("CumulativeRemainingLateLaborCost", UNSET)

        cumulative_remaining_late_labor_units = d.pop("CumulativeRemainingLateLaborUnits", UNSET)

        cumulative_remaining_late_material_cost = d.pop("CumulativeRemainingLateMaterialCost", UNSET)

        cumulative_remaining_late_nonlabor_cost = d.pop("CumulativeRemainingLateNonlaborCost", UNSET)

        cumulative_remaining_late_nonlabor_units = d.pop("CumulativeRemainingLateNonlaborUnits", UNSET)

        cumulative_remaining_late_total_cost = d.pop("CumulativeRemainingLateTotalCost", UNSET)

        cumulative_remaining_material_cost = d.pop("CumulativeRemainingMaterialCost", UNSET)

        cumulative_remaining_nonlabor_cost = d.pop("CumulativeRemainingNonlaborCost", UNSET)

        cumulative_remaining_nonlabor_units = d.pop("CumulativeRemainingNonlaborUnits", UNSET)

        cumulative_remaining_total_cost = d.pop("CumulativeRemainingTotalCost", UNSET)

        summarized_spread_period = cls(
            start_date=start_date,
            end_date=end_date,
            actual_cost=actual_cost,
            actual_expense_cost=actual_expense_cost,
            actual_labor_cost=actual_labor_cost,
            actual_labor_units=actual_labor_units,
            actual_material_cost=actual_material_cost,
            actual_nonlabor_cost=actual_nonlabor_cost,
            actual_nonlabor_units=actual_nonlabor_units,
            actual_total_cost=actual_total_cost,
            at_completion_expense_cost=at_completion_expense_cost,
            at_completion_labor_cost=at_completion_labor_cost,
            at_completion_labor_units=at_completion_labor_units,
            at_completion_material_cost=at_completion_material_cost,
            at_completion_nonlabor_cost=at_completion_nonlabor_cost,
            at_completion_nonlabor_units=at_completion_nonlabor_units,
            at_completion_total_cost=at_completion_total_cost,
            baseline_planned_expense_cost=baseline_planned_expense_cost,
            baseline_planned_labor_cost=baseline_planned_labor_cost,
            baseline_planned_labor_units=baseline_planned_labor_units,
            baseline_planned_material_cost=baseline_planned_material_cost,
            baseline_planned_nonlabor_cost=baseline_planned_nonlabor_cost,
            baseline_planned_nonlabor_units=baseline_planned_nonlabor_units,
            baseline_planned_total_cost=baseline_planned_total_cost,
            earned_value_cost=earned_value_cost,
            earned_value_labor_units=earned_value_labor_units,
            estimate_at_completion_cost=estimate_at_completion_cost,
            estimate_at_completion_labor_units=estimate_at_completion_labor_units,
            estimate_to_complete_cost=estimate_to_complete_cost,
            estimate_to_complete_labor_units=estimate_to_complete_labor_units,
            period_actual_cost=period_actual_cost,
            period_actual_expense_cost=period_actual_expense_cost,
            period_actual_labor_cost=period_actual_labor_cost,
            period_actual_labor_units=period_actual_labor_units,
            period_actual_material_cost=period_actual_material_cost,
            period_actual_non_labor_cost=period_actual_non_labor_cost,
            period_actual_non_labor_units=period_actual_non_labor_units,
            period_at_completion_expense_cost=period_at_completion_expense_cost,
            period_at_completion_labor_cost=period_at_completion_labor_cost,
            period_at_completion_labor_units=period_at_completion_labor_units,
            period_at_completion_material_cost=period_at_completion_material_cost,
            period_at_completion_non_labor_cost=period_at_completion_non_labor_cost,
            period_at_completion_non_labor_units=period_at_completion_non_labor_units,
            period_at_completion_total_cost=period_at_completion_total_cost,
            period_earned_value_cost=period_earned_value_cost,
            period_earned_value_labor_units=period_earned_value_labor_units,
            period_estimate_at_completion_cost=period_estimate_at_completion_cost,
            period_estimate_at_completion_labor_units=period_estimate_at_completion_labor_units,
            period_planned_value_cost=period_planned_value_cost,
            period_planned_value_labor_units=period_planned_value_labor_units,
            planned_expense_cost=planned_expense_cost,
            planned_labor_cost=planned_labor_cost,
            planned_labor_units=planned_labor_units,
            planned_material_cost=planned_material_cost,
            planned_nonlabor_cost=planned_nonlabor_cost,
            planned_nonlabor_units=planned_nonlabor_units,
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
            remaining_late_nonlabor_cost=remaining_late_nonlabor_cost,
            remaining_late_nonlabor_units=remaining_late_nonlabor_units,
            remaining_late_total_cost=remaining_late_total_cost,
            remaining_material_cost=remaining_material_cost,
            remaining_nonlabor_cost=remaining_nonlabor_cost,
            remaining_nonlabor_units=remaining_nonlabor_units,
            remaining_total_cost=remaining_total_cost,
            cumulative_actual_cost=cumulative_actual_cost,
            cumulative_actual_expense_cost=cumulative_actual_expense_cost,
            cumulative_actual_labor_cost=cumulative_actual_labor_cost,
            cumulative_actual_labor_units=cumulative_actual_labor_units,
            cumulative_actual_material_cost=cumulative_actual_material_cost,
            cumulative_actual_nonlabor_cost=cumulative_actual_nonlabor_cost,
            cumulative_actual_nonlabor_units=cumulative_actual_nonlabor_units,
            cumulative_actual_total_cost=cumulative_actual_total_cost,
            cumulative_at_completion_expense_cost=cumulative_at_completion_expense_cost,
            cumulative_at_completion_labor_cost=cumulative_at_completion_labor_cost,
            cumulative_at_completion_labor_units=cumulative_at_completion_labor_units,
            cumulative_at_completion_material_cost=cumulative_at_completion_material_cost,
            cumulative_at_completion_nonlabor_cost=cumulative_at_completion_nonlabor_cost,
            cumulative_at_completion_nonlabor_units=cumulative_at_completion_nonlabor_units,
            cumulative_at_completion_total_cost=cumulative_at_completion_total_cost,
            cumulative_baseline_planned_expense_cost=cumulative_baseline_planned_expense_cost,
            cumulative_baseline_planned_labor_cost=cumulative_baseline_planned_labor_cost,
            cumulative_baseline_planned_labor_units=cumulative_baseline_planned_labor_units,
            cumulative_baseline_planned_material_cost=cumulative_baseline_planned_material_cost,
            cumulative_baseline_planned_nonlabor_cost=cumulative_baseline_planned_nonlabor_cost,
            cumulative_baseline_planned_nonlabor_units=cumulative_baseline_planned_nonlabor_units,
            cumulative_baseline_planned_total_cost=cumulative_baseline_planned_total_cost,
            cumulative_earned_value_cost=cumulative_earned_value_cost,
            cumulative_earned_value_labor_units=cumulative_earned_value_labor_units,
            cumulative_estimate_at_completion_cost=cumulative_estimate_at_completion_cost,
            cumulative_estimate_at_completion_labor_units=cumulative_estimate_at_completion_labor_units,
            cumulative_estimate_to_complete_cost=cumulative_estimate_to_complete_cost,
            cumulative_estimate_to_complete_labor_units=cumulative_estimate_to_complete_labor_units,
            cumulative_limit=cumulative_limit,
            cumulative_planned_expense_cost=cumulative_planned_expense_cost,
            cumulative_planned_labor_cost=cumulative_planned_labor_cost,
            cumulative_planned_labor_units=cumulative_planned_labor_units,
            cumulative_planned_material_cost=cumulative_planned_material_cost,
            cumulative_planned_nonlabor_cost=cumulative_planned_nonlabor_cost,
            cumulative_planned_nonlabor_units=cumulative_planned_nonlabor_units,
            cumulative_planned_total_cost=cumulative_planned_total_cost,
            cumulative_planned_value_cost=cumulative_planned_value_cost,
            cumulative_planned_value_labor_units=cumulative_planned_value_labor_units,
            cumulative_period_actual_cost=cumulative_period_actual_cost,
            cumulative_period_actual_expense_cost=cumulative_period_actual_expense_cost,
            cumulative_period_actual_labor_cost=cumulative_period_actual_labor_cost,
            cumulative_period_actual_labor_units=cumulative_period_actual_labor_units,
            cumulative_period_actual_material_cost=cumulative_period_actual_material_cost,
            cumulative_period_actual_non_labor_cost=cumulative_period_actual_non_labor_cost,
            cumulative_period_actual_non_labor_units=cumulative_period_actual_non_labor_units,
            cumulative_period_at_completion_expense_cost=cumulative_period_at_completion_expense_cost,
            cumulative_period_at_completion_labor_cost=cumulative_period_at_completion_labor_cost,
            cumulative_period_at_completion_labor_units=cumulative_period_at_completion_labor_units,
            cumulative_period_at_completion_material_cost=cumulative_period_at_completion_material_cost,
            cumulative_period_at_completion_non_labor_cost=cumulative_period_at_completion_non_labor_cost,
            cumulative_period_at_completion_non_labor_units=cumulative_period_at_completion_non_labor_units,
            cumulative_period_at_completion_total_cost=cumulative_period_at_completion_total_cost,
            cumulative_period_earned_value_cost=cumulative_period_earned_value_cost,
            cumulative_period_earned_value_labor_units=cumulative_period_earned_value_labor_units,
            cumulative_period_estimate_at_completion_cost=cumulative_period_estimate_at_completion_cost,
            cumulative_period_estimate_at_completion_labor_units=cumulative_period_estimate_at_completion_labor_units,
            cumulative_period_planned_value_cost=cumulative_period_planned_value_cost,
            cumulative_period_planned_value_labor_units=cumulative_period_planned_value_labor_units,
            cumulative_remaining_expense_cost=cumulative_remaining_expense_cost,
            cumulative_remaining_labor_cost=cumulative_remaining_labor_cost,
            cumulative_remaining_labor_units=cumulative_remaining_labor_units,
            cumulative_remaining_late_expense_cost=cumulative_remaining_late_expense_cost,
            cumulative_remaining_late_labor_cost=cumulative_remaining_late_labor_cost,
            cumulative_remaining_late_labor_units=cumulative_remaining_late_labor_units,
            cumulative_remaining_late_material_cost=cumulative_remaining_late_material_cost,
            cumulative_remaining_late_nonlabor_cost=cumulative_remaining_late_nonlabor_cost,
            cumulative_remaining_late_nonlabor_units=cumulative_remaining_late_nonlabor_units,
            cumulative_remaining_late_total_cost=cumulative_remaining_late_total_cost,
            cumulative_remaining_material_cost=cumulative_remaining_material_cost,
            cumulative_remaining_nonlabor_cost=cumulative_remaining_nonlabor_cost,
            cumulative_remaining_nonlabor_units=cumulative_remaining_nonlabor_units,
            cumulative_remaining_total_cost=cumulative_remaining_total_cost,
        )

        summarized_spread_period.additional_properties = d
        return summarized_spread_period

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
