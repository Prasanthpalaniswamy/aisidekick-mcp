from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceRoleSpreadPeriod")


@_attrs_define
class ResourceRoleSpreadPeriod:
    """
    Attributes:
        start_date (str | Unset):
        end_date (str | Unset):
        financial_period_object_id (int | Unset):
        actual_cost (float | Unset):
        actual_overtime_cost (float | Unset):
        actual_overtime_units (float | Unset):
        actual_regular_cost (float | Unset):
        actual_regular_units (float | Unset):
        actual_units (float | Unset):
        at_completion_cost (float | Unset):
        at_completion_units (float | Unset):
        limit (float | Unset):
        period_actual_cost (float | Unset):
        period_actual_units (float | Unset):
        period_at_completion_cost (float | Unset):
        period_at_completion_units (float | Unset):
        planned_cost (float | Unset):
        planned_units (float | Unset):
        remaining_cost (float | Unset):
        remaining_late_cost (float | Unset):
        remaining_late_units (float | Unset):
        remaining_units (float | Unset):
        staffed_actual_cost (float | Unset):
        staffed_actual_overtime_cost (float | Unset):
        staffed_actual_overtime_units (float | Unset):
        staffed_actual_regular_cost (float | Unset):
        staffed_actual_regular_units (float | Unset):
        staffed_actual_units (float | Unset):
        staffed_at_completion_cost (float | Unset):
        staffed_at_completion_units (float | Unset):
        staffed_planned_cost (float | Unset):
        staffed_planned_units (float | Unset):
        staffed_remaining_cost (float | Unset):
        staffed_remaining_late_cost (float | Unset):
        staffed_remaining_late_units (float | Unset):
        staffed_remaining_units (float | Unset):
        unstaffed_actual_cost (float | Unset):
        unstaffed_actual_overtime_cost (float | Unset):
        unstaffed_actual_overtime_units (float | Unset):
        unstaffed_actual_regular_cost (float | Unset):
        unstaffed_actual_regular_units (float | Unset):
        unstaffed_actual_units (float | Unset):
        unstaffed_at_completion_cost (float | Unset):
        unstaffed_at_completion_units (float | Unset):
        unstaffed_planned_cost (float | Unset):
        unstaffed_planned_units (float | Unset):
        unstaffed_remaining_cost (float | Unset):
        unstaffed_remaining_late_cost (float | Unset):
        unstaffed_remaining_late_units (float | Unset):
        unstaffed_remaining_units (float | Unset):
        cumulative_actual_cost (float | Unset):
        cumulative_actual_overtime_cost (float | Unset):
        cumulative_actual_overtime_units (float | Unset):
        cumulative_actual_regular_cost (float | Unset):
        cumulative_actual_regular_units (float | Unset):
        cumulative_actual_units (float | Unset):
        cumulative_at_completion_cost (float | Unset):
        cumulative_at_completion_units (float | Unset):
        cumulative_limit (float | Unset):
        cumulative_period_actual_cost (float | Unset):
        cumulative_period_actual_units (float | Unset):
        cumulative_period_at_completion_cost (float | Unset):
        cumulative_period_at_completion_units (float | Unset):
        cumulative_planned_cost (float | Unset):
        cumulative_planned_units (float | Unset):
        cumulative_remaining_cost (float | Unset):
        cumulative_remaining_late_cost (float | Unset):
        cumulative_remaining_late_units (float | Unset):
        cumulative_remaining_units (float | Unset):
        cumulative_staffed_actual_cost (float | Unset):
        cumulative_staffed_actual_overtime_cost (float | Unset):
        cumulative_staffed_actual_overtime_units (float | Unset):
        cumulative_staffed_actual_regular_cost (float | Unset):
        cumulative_staffed_actual_regular_units (float | Unset):
        cumulative_staffed_actual_units (float | Unset):
        cumulative_staffed_at_completion_cost (float | Unset):
        cumulative_staffed_at_completion_units (float | Unset):
        cumulative_staffed_planned_cost (float | Unset):
        cumulative_staffed_planned_units (float | Unset):
        cumulative_staffed_remaining_cost (float | Unset):
        cumulative_staffed_remaining_late_cost (float | Unset):
        cumulative_staffed_remaining_late_units (float | Unset):
        cumulative_staffed_remaining_units (float | Unset):
        cumulative_unstaffed_actual_cost (float | Unset):
        cumulative_unstaffed_actual_overtime_cost (float | Unset):
        cumulative_unstaffed_actual_overtime_units (float | Unset):
        cumulative_unstaffed_actual_regular_cost (float | Unset):
        cumulative_unstaffed_actual_regular_units (float | Unset):
        cumulative_unstaffed_actual_units (float | Unset):
        cumulative_unstaffed_at_completion_cost (float | Unset):
        cumulative_unstaffed_at_completion_units (float | Unset):
        cumulative_unstaffed_planned_cost (float | Unset):
        cumulative_unstaffed_planned_units (float | Unset):
        cumulative_unstaffed_remaining_cost (float | Unset):
        cumulative_unstaffed_remaining_late_cost (float | Unset):
        cumulative_unstaffed_remaining_late_units (float | Unset):
        cumulative_unstaffed_remaining_units (float | Unset):
    """

    start_date: str | Unset = UNSET
    end_date: str | Unset = UNSET
    financial_period_object_id: int | Unset = UNSET
    actual_cost: float | Unset = UNSET
    actual_overtime_cost: float | Unset = UNSET
    actual_overtime_units: float | Unset = UNSET
    actual_regular_cost: float | Unset = UNSET
    actual_regular_units: float | Unset = UNSET
    actual_units: float | Unset = UNSET
    at_completion_cost: float | Unset = UNSET
    at_completion_units: float | Unset = UNSET
    limit: float | Unset = UNSET
    period_actual_cost: float | Unset = UNSET
    period_actual_units: float | Unset = UNSET
    period_at_completion_cost: float | Unset = UNSET
    period_at_completion_units: float | Unset = UNSET
    planned_cost: float | Unset = UNSET
    planned_units: float | Unset = UNSET
    remaining_cost: float | Unset = UNSET
    remaining_late_cost: float | Unset = UNSET
    remaining_late_units: float | Unset = UNSET
    remaining_units: float | Unset = UNSET
    staffed_actual_cost: float | Unset = UNSET
    staffed_actual_overtime_cost: float | Unset = UNSET
    staffed_actual_overtime_units: float | Unset = UNSET
    staffed_actual_regular_cost: float | Unset = UNSET
    staffed_actual_regular_units: float | Unset = UNSET
    staffed_actual_units: float | Unset = UNSET
    staffed_at_completion_cost: float | Unset = UNSET
    staffed_at_completion_units: float | Unset = UNSET
    staffed_planned_cost: float | Unset = UNSET
    staffed_planned_units: float | Unset = UNSET
    staffed_remaining_cost: float | Unset = UNSET
    staffed_remaining_late_cost: float | Unset = UNSET
    staffed_remaining_late_units: float | Unset = UNSET
    staffed_remaining_units: float | Unset = UNSET
    unstaffed_actual_cost: float | Unset = UNSET
    unstaffed_actual_overtime_cost: float | Unset = UNSET
    unstaffed_actual_overtime_units: float | Unset = UNSET
    unstaffed_actual_regular_cost: float | Unset = UNSET
    unstaffed_actual_regular_units: float | Unset = UNSET
    unstaffed_actual_units: float | Unset = UNSET
    unstaffed_at_completion_cost: float | Unset = UNSET
    unstaffed_at_completion_units: float | Unset = UNSET
    unstaffed_planned_cost: float | Unset = UNSET
    unstaffed_planned_units: float | Unset = UNSET
    unstaffed_remaining_cost: float | Unset = UNSET
    unstaffed_remaining_late_cost: float | Unset = UNSET
    unstaffed_remaining_late_units: float | Unset = UNSET
    unstaffed_remaining_units: float | Unset = UNSET
    cumulative_actual_cost: float | Unset = UNSET
    cumulative_actual_overtime_cost: float | Unset = UNSET
    cumulative_actual_overtime_units: float | Unset = UNSET
    cumulative_actual_regular_cost: float | Unset = UNSET
    cumulative_actual_regular_units: float | Unset = UNSET
    cumulative_actual_units: float | Unset = UNSET
    cumulative_at_completion_cost: float | Unset = UNSET
    cumulative_at_completion_units: float | Unset = UNSET
    cumulative_limit: float | Unset = UNSET
    cumulative_period_actual_cost: float | Unset = UNSET
    cumulative_period_actual_units: float | Unset = UNSET
    cumulative_period_at_completion_cost: float | Unset = UNSET
    cumulative_period_at_completion_units: float | Unset = UNSET
    cumulative_planned_cost: float | Unset = UNSET
    cumulative_planned_units: float | Unset = UNSET
    cumulative_remaining_cost: float | Unset = UNSET
    cumulative_remaining_late_cost: float | Unset = UNSET
    cumulative_remaining_late_units: float | Unset = UNSET
    cumulative_remaining_units: float | Unset = UNSET
    cumulative_staffed_actual_cost: float | Unset = UNSET
    cumulative_staffed_actual_overtime_cost: float | Unset = UNSET
    cumulative_staffed_actual_overtime_units: float | Unset = UNSET
    cumulative_staffed_actual_regular_cost: float | Unset = UNSET
    cumulative_staffed_actual_regular_units: float | Unset = UNSET
    cumulative_staffed_actual_units: float | Unset = UNSET
    cumulative_staffed_at_completion_cost: float | Unset = UNSET
    cumulative_staffed_at_completion_units: float | Unset = UNSET
    cumulative_staffed_planned_cost: float | Unset = UNSET
    cumulative_staffed_planned_units: float | Unset = UNSET
    cumulative_staffed_remaining_cost: float | Unset = UNSET
    cumulative_staffed_remaining_late_cost: float | Unset = UNSET
    cumulative_staffed_remaining_late_units: float | Unset = UNSET
    cumulative_staffed_remaining_units: float | Unset = UNSET
    cumulative_unstaffed_actual_cost: float | Unset = UNSET
    cumulative_unstaffed_actual_overtime_cost: float | Unset = UNSET
    cumulative_unstaffed_actual_overtime_units: float | Unset = UNSET
    cumulative_unstaffed_actual_regular_cost: float | Unset = UNSET
    cumulative_unstaffed_actual_regular_units: float | Unset = UNSET
    cumulative_unstaffed_actual_units: float | Unset = UNSET
    cumulative_unstaffed_at_completion_cost: float | Unset = UNSET
    cumulative_unstaffed_at_completion_units: float | Unset = UNSET
    cumulative_unstaffed_planned_cost: float | Unset = UNSET
    cumulative_unstaffed_planned_units: float | Unset = UNSET
    cumulative_unstaffed_remaining_cost: float | Unset = UNSET
    cumulative_unstaffed_remaining_late_cost: float | Unset = UNSET
    cumulative_unstaffed_remaining_late_units: float | Unset = UNSET
    cumulative_unstaffed_remaining_units: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_date = self.start_date

        end_date = self.end_date

        financial_period_object_id = self.financial_period_object_id

        actual_cost = self.actual_cost

        actual_overtime_cost = self.actual_overtime_cost

        actual_overtime_units = self.actual_overtime_units

        actual_regular_cost = self.actual_regular_cost

        actual_regular_units = self.actual_regular_units

        actual_units = self.actual_units

        at_completion_cost = self.at_completion_cost

        at_completion_units = self.at_completion_units

        limit = self.limit

        period_actual_cost = self.period_actual_cost

        period_actual_units = self.period_actual_units

        period_at_completion_cost = self.period_at_completion_cost

        period_at_completion_units = self.period_at_completion_units

        planned_cost = self.planned_cost

        planned_units = self.planned_units

        remaining_cost = self.remaining_cost

        remaining_late_cost = self.remaining_late_cost

        remaining_late_units = self.remaining_late_units

        remaining_units = self.remaining_units

        staffed_actual_cost = self.staffed_actual_cost

        staffed_actual_overtime_cost = self.staffed_actual_overtime_cost

        staffed_actual_overtime_units = self.staffed_actual_overtime_units

        staffed_actual_regular_cost = self.staffed_actual_regular_cost

        staffed_actual_regular_units = self.staffed_actual_regular_units

        staffed_actual_units = self.staffed_actual_units

        staffed_at_completion_cost = self.staffed_at_completion_cost

        staffed_at_completion_units = self.staffed_at_completion_units

        staffed_planned_cost = self.staffed_planned_cost

        staffed_planned_units = self.staffed_planned_units

        staffed_remaining_cost = self.staffed_remaining_cost

        staffed_remaining_late_cost = self.staffed_remaining_late_cost

        staffed_remaining_late_units = self.staffed_remaining_late_units

        staffed_remaining_units = self.staffed_remaining_units

        unstaffed_actual_cost = self.unstaffed_actual_cost

        unstaffed_actual_overtime_cost = self.unstaffed_actual_overtime_cost

        unstaffed_actual_overtime_units = self.unstaffed_actual_overtime_units

        unstaffed_actual_regular_cost = self.unstaffed_actual_regular_cost

        unstaffed_actual_regular_units = self.unstaffed_actual_regular_units

        unstaffed_actual_units = self.unstaffed_actual_units

        unstaffed_at_completion_cost = self.unstaffed_at_completion_cost

        unstaffed_at_completion_units = self.unstaffed_at_completion_units

        unstaffed_planned_cost = self.unstaffed_planned_cost

        unstaffed_planned_units = self.unstaffed_planned_units

        unstaffed_remaining_cost = self.unstaffed_remaining_cost

        unstaffed_remaining_late_cost = self.unstaffed_remaining_late_cost

        unstaffed_remaining_late_units = self.unstaffed_remaining_late_units

        unstaffed_remaining_units = self.unstaffed_remaining_units

        cumulative_actual_cost = self.cumulative_actual_cost

        cumulative_actual_overtime_cost = self.cumulative_actual_overtime_cost

        cumulative_actual_overtime_units = self.cumulative_actual_overtime_units

        cumulative_actual_regular_cost = self.cumulative_actual_regular_cost

        cumulative_actual_regular_units = self.cumulative_actual_regular_units

        cumulative_actual_units = self.cumulative_actual_units

        cumulative_at_completion_cost = self.cumulative_at_completion_cost

        cumulative_at_completion_units = self.cumulative_at_completion_units

        cumulative_limit = self.cumulative_limit

        cumulative_period_actual_cost = self.cumulative_period_actual_cost

        cumulative_period_actual_units = self.cumulative_period_actual_units

        cumulative_period_at_completion_cost = self.cumulative_period_at_completion_cost

        cumulative_period_at_completion_units = self.cumulative_period_at_completion_units

        cumulative_planned_cost = self.cumulative_planned_cost

        cumulative_planned_units = self.cumulative_planned_units

        cumulative_remaining_cost = self.cumulative_remaining_cost

        cumulative_remaining_late_cost = self.cumulative_remaining_late_cost

        cumulative_remaining_late_units = self.cumulative_remaining_late_units

        cumulative_remaining_units = self.cumulative_remaining_units

        cumulative_staffed_actual_cost = self.cumulative_staffed_actual_cost

        cumulative_staffed_actual_overtime_cost = self.cumulative_staffed_actual_overtime_cost

        cumulative_staffed_actual_overtime_units = self.cumulative_staffed_actual_overtime_units

        cumulative_staffed_actual_regular_cost = self.cumulative_staffed_actual_regular_cost

        cumulative_staffed_actual_regular_units = self.cumulative_staffed_actual_regular_units

        cumulative_staffed_actual_units = self.cumulative_staffed_actual_units

        cumulative_staffed_at_completion_cost = self.cumulative_staffed_at_completion_cost

        cumulative_staffed_at_completion_units = self.cumulative_staffed_at_completion_units

        cumulative_staffed_planned_cost = self.cumulative_staffed_planned_cost

        cumulative_staffed_planned_units = self.cumulative_staffed_planned_units

        cumulative_staffed_remaining_cost = self.cumulative_staffed_remaining_cost

        cumulative_staffed_remaining_late_cost = self.cumulative_staffed_remaining_late_cost

        cumulative_staffed_remaining_late_units = self.cumulative_staffed_remaining_late_units

        cumulative_staffed_remaining_units = self.cumulative_staffed_remaining_units

        cumulative_unstaffed_actual_cost = self.cumulative_unstaffed_actual_cost

        cumulative_unstaffed_actual_overtime_cost = self.cumulative_unstaffed_actual_overtime_cost

        cumulative_unstaffed_actual_overtime_units = self.cumulative_unstaffed_actual_overtime_units

        cumulative_unstaffed_actual_regular_cost = self.cumulative_unstaffed_actual_regular_cost

        cumulative_unstaffed_actual_regular_units = self.cumulative_unstaffed_actual_regular_units

        cumulative_unstaffed_actual_units = self.cumulative_unstaffed_actual_units

        cumulative_unstaffed_at_completion_cost = self.cumulative_unstaffed_at_completion_cost

        cumulative_unstaffed_at_completion_units = self.cumulative_unstaffed_at_completion_units

        cumulative_unstaffed_planned_cost = self.cumulative_unstaffed_planned_cost

        cumulative_unstaffed_planned_units = self.cumulative_unstaffed_planned_units

        cumulative_unstaffed_remaining_cost = self.cumulative_unstaffed_remaining_cost

        cumulative_unstaffed_remaining_late_cost = self.cumulative_unstaffed_remaining_late_cost

        cumulative_unstaffed_remaining_late_units = self.cumulative_unstaffed_remaining_late_units

        cumulative_unstaffed_remaining_units = self.cumulative_unstaffed_remaining_units

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
        if actual_overtime_cost is not UNSET:
            field_dict["ActualOvertimeCost"] = actual_overtime_cost
        if actual_overtime_units is not UNSET:
            field_dict["ActualOvertimeUnits"] = actual_overtime_units
        if actual_regular_cost is not UNSET:
            field_dict["ActualRegularCost"] = actual_regular_cost
        if actual_regular_units is not UNSET:
            field_dict["ActualRegularUnits"] = actual_regular_units
        if actual_units is not UNSET:
            field_dict["ActualUnits"] = actual_units
        if at_completion_cost is not UNSET:
            field_dict["AtCompletionCost"] = at_completion_cost
        if at_completion_units is not UNSET:
            field_dict["AtCompletionUnits"] = at_completion_units
        if limit is not UNSET:
            field_dict["Limit"] = limit
        if period_actual_cost is not UNSET:
            field_dict["PeriodActualCost"] = period_actual_cost
        if period_actual_units is not UNSET:
            field_dict["PeriodActualUnits"] = period_actual_units
        if period_at_completion_cost is not UNSET:
            field_dict["PeriodAtCompletionCost"] = period_at_completion_cost
        if period_at_completion_units is not UNSET:
            field_dict["PeriodAtCompletionUnits"] = period_at_completion_units
        if planned_cost is not UNSET:
            field_dict["PlannedCost"] = planned_cost
        if planned_units is not UNSET:
            field_dict["PlannedUnits"] = planned_units
        if remaining_cost is not UNSET:
            field_dict["RemainingCost"] = remaining_cost
        if remaining_late_cost is not UNSET:
            field_dict["RemainingLateCost"] = remaining_late_cost
        if remaining_late_units is not UNSET:
            field_dict["RemainingLateUnits"] = remaining_late_units
        if remaining_units is not UNSET:
            field_dict["RemainingUnits"] = remaining_units
        if staffed_actual_cost is not UNSET:
            field_dict["StaffedActualCost"] = staffed_actual_cost
        if staffed_actual_overtime_cost is not UNSET:
            field_dict["StaffedActualOvertimeCost"] = staffed_actual_overtime_cost
        if staffed_actual_overtime_units is not UNSET:
            field_dict["StaffedActualOvertimeUnits"] = staffed_actual_overtime_units
        if staffed_actual_regular_cost is not UNSET:
            field_dict["StaffedActualRegularCost"] = staffed_actual_regular_cost
        if staffed_actual_regular_units is not UNSET:
            field_dict["StaffedActualRegularUnits"] = staffed_actual_regular_units
        if staffed_actual_units is not UNSET:
            field_dict["StaffedActualUnits"] = staffed_actual_units
        if staffed_at_completion_cost is not UNSET:
            field_dict["StaffedAtCompletionCost"] = staffed_at_completion_cost
        if staffed_at_completion_units is not UNSET:
            field_dict["StaffedAtCompletionUnits"] = staffed_at_completion_units
        if staffed_planned_cost is not UNSET:
            field_dict["StaffedPlannedCost"] = staffed_planned_cost
        if staffed_planned_units is not UNSET:
            field_dict["StaffedPlannedUnits"] = staffed_planned_units
        if staffed_remaining_cost is not UNSET:
            field_dict["StaffedRemainingCost"] = staffed_remaining_cost
        if staffed_remaining_late_cost is not UNSET:
            field_dict["StaffedRemainingLateCost"] = staffed_remaining_late_cost
        if staffed_remaining_late_units is not UNSET:
            field_dict["StaffedRemainingLateUnits"] = staffed_remaining_late_units
        if staffed_remaining_units is not UNSET:
            field_dict["StaffedRemainingUnits"] = staffed_remaining_units
        if unstaffed_actual_cost is not UNSET:
            field_dict["UnstaffedActualCost"] = unstaffed_actual_cost
        if unstaffed_actual_overtime_cost is not UNSET:
            field_dict["UnstaffedActualOvertimeCost"] = unstaffed_actual_overtime_cost
        if unstaffed_actual_overtime_units is not UNSET:
            field_dict["UnstaffedActualOvertimeUnits"] = unstaffed_actual_overtime_units
        if unstaffed_actual_regular_cost is not UNSET:
            field_dict["UnstaffedActualRegularCost"] = unstaffed_actual_regular_cost
        if unstaffed_actual_regular_units is not UNSET:
            field_dict["UnstaffedActualRegularUnits"] = unstaffed_actual_regular_units
        if unstaffed_actual_units is not UNSET:
            field_dict["UnstaffedActualUnits"] = unstaffed_actual_units
        if unstaffed_at_completion_cost is not UNSET:
            field_dict["UnstaffedAtCompletionCost"] = unstaffed_at_completion_cost
        if unstaffed_at_completion_units is not UNSET:
            field_dict["UnstaffedAtCompletionUnits"] = unstaffed_at_completion_units
        if unstaffed_planned_cost is not UNSET:
            field_dict["UnstaffedPlannedCost"] = unstaffed_planned_cost
        if unstaffed_planned_units is not UNSET:
            field_dict["UnstaffedPlannedUnits"] = unstaffed_planned_units
        if unstaffed_remaining_cost is not UNSET:
            field_dict["UnstaffedRemainingCost"] = unstaffed_remaining_cost
        if unstaffed_remaining_late_cost is not UNSET:
            field_dict["UnstaffedRemainingLateCost"] = unstaffed_remaining_late_cost
        if unstaffed_remaining_late_units is not UNSET:
            field_dict["UnstaffedRemainingLateUnits"] = unstaffed_remaining_late_units
        if unstaffed_remaining_units is not UNSET:
            field_dict["UnstaffedRemainingUnits"] = unstaffed_remaining_units
        if cumulative_actual_cost is not UNSET:
            field_dict["CumulativeActualCost"] = cumulative_actual_cost
        if cumulative_actual_overtime_cost is not UNSET:
            field_dict["CumulativeActualOvertimeCost"] = cumulative_actual_overtime_cost
        if cumulative_actual_overtime_units is not UNSET:
            field_dict["CumulativeActualOvertimeUnits"] = cumulative_actual_overtime_units
        if cumulative_actual_regular_cost is not UNSET:
            field_dict["CumulativeActualRegularCost"] = cumulative_actual_regular_cost
        if cumulative_actual_regular_units is not UNSET:
            field_dict["CumulativeActualRegularUnits"] = cumulative_actual_regular_units
        if cumulative_actual_units is not UNSET:
            field_dict["CumulativeActualUnits"] = cumulative_actual_units
        if cumulative_at_completion_cost is not UNSET:
            field_dict["CumulativeAtCompletionCost"] = cumulative_at_completion_cost
        if cumulative_at_completion_units is not UNSET:
            field_dict["CumulativeAtCompletionUnits"] = cumulative_at_completion_units
        if cumulative_limit is not UNSET:
            field_dict["CumulativeLimit"] = cumulative_limit
        if cumulative_period_actual_cost is not UNSET:
            field_dict["CumulativePeriodActualCost"] = cumulative_period_actual_cost
        if cumulative_period_actual_units is not UNSET:
            field_dict["CumulativePeriodActualUnits"] = cumulative_period_actual_units
        if cumulative_period_at_completion_cost is not UNSET:
            field_dict["CumulativePeriodAtCompletionCost"] = cumulative_period_at_completion_cost
        if cumulative_period_at_completion_units is not UNSET:
            field_dict["CumulativePeriodAtCompletionUnits"] = cumulative_period_at_completion_units
        if cumulative_planned_cost is not UNSET:
            field_dict["CumulativePlannedCost"] = cumulative_planned_cost
        if cumulative_planned_units is not UNSET:
            field_dict["CumulativePlannedUnits"] = cumulative_planned_units
        if cumulative_remaining_cost is not UNSET:
            field_dict["CumulativeRemainingCost"] = cumulative_remaining_cost
        if cumulative_remaining_late_cost is not UNSET:
            field_dict["CumulativeRemainingLateCost"] = cumulative_remaining_late_cost
        if cumulative_remaining_late_units is not UNSET:
            field_dict["CumulativeRemainingLateUnits"] = cumulative_remaining_late_units
        if cumulative_remaining_units is not UNSET:
            field_dict["CumulativeRemainingUnits"] = cumulative_remaining_units
        if cumulative_staffed_actual_cost is not UNSET:
            field_dict["CumulativeStaffedActualCost"] = cumulative_staffed_actual_cost
        if cumulative_staffed_actual_overtime_cost is not UNSET:
            field_dict["CumulativeStaffedActualOvertimeCost"] = cumulative_staffed_actual_overtime_cost
        if cumulative_staffed_actual_overtime_units is not UNSET:
            field_dict["CumulativeStaffedActualOvertimeUnits"] = cumulative_staffed_actual_overtime_units
        if cumulative_staffed_actual_regular_cost is not UNSET:
            field_dict["CumulativeStaffedActualRegularCost"] = cumulative_staffed_actual_regular_cost
        if cumulative_staffed_actual_regular_units is not UNSET:
            field_dict["CumulativeStaffedActualRegularUnits"] = cumulative_staffed_actual_regular_units
        if cumulative_staffed_actual_units is not UNSET:
            field_dict["CumulativeStaffedActualUnits"] = cumulative_staffed_actual_units
        if cumulative_staffed_at_completion_cost is not UNSET:
            field_dict["CumulativeStaffedAtCompletionCost"] = cumulative_staffed_at_completion_cost
        if cumulative_staffed_at_completion_units is not UNSET:
            field_dict["CumulativeStaffedAtCompletionUnits"] = cumulative_staffed_at_completion_units
        if cumulative_staffed_planned_cost is not UNSET:
            field_dict["CumulativeStaffedPlannedCost"] = cumulative_staffed_planned_cost
        if cumulative_staffed_planned_units is not UNSET:
            field_dict["CumulativeStaffedPlannedUnits"] = cumulative_staffed_planned_units
        if cumulative_staffed_remaining_cost is not UNSET:
            field_dict["CumulativeStaffedRemainingCost"] = cumulative_staffed_remaining_cost
        if cumulative_staffed_remaining_late_cost is not UNSET:
            field_dict["CumulativeStaffedRemainingLateCost"] = cumulative_staffed_remaining_late_cost
        if cumulative_staffed_remaining_late_units is not UNSET:
            field_dict["CumulativeStaffedRemainingLateUnits"] = cumulative_staffed_remaining_late_units
        if cumulative_staffed_remaining_units is not UNSET:
            field_dict["CumulativeStaffedRemainingUnits"] = cumulative_staffed_remaining_units
        if cumulative_unstaffed_actual_cost is not UNSET:
            field_dict["CumulativeUnstaffedActualCost"] = cumulative_unstaffed_actual_cost
        if cumulative_unstaffed_actual_overtime_cost is not UNSET:
            field_dict["CumulativeUnstaffedActualOvertimeCost"] = cumulative_unstaffed_actual_overtime_cost
        if cumulative_unstaffed_actual_overtime_units is not UNSET:
            field_dict["CumulativeUnstaffedActualOvertimeUnits"] = cumulative_unstaffed_actual_overtime_units
        if cumulative_unstaffed_actual_regular_cost is not UNSET:
            field_dict["CumulativeUnstaffedActualRegularCost"] = cumulative_unstaffed_actual_regular_cost
        if cumulative_unstaffed_actual_regular_units is not UNSET:
            field_dict["CumulativeUnstaffedActualRegularUnits"] = cumulative_unstaffed_actual_regular_units
        if cumulative_unstaffed_actual_units is not UNSET:
            field_dict["CumulativeUnstaffedActualUnits"] = cumulative_unstaffed_actual_units
        if cumulative_unstaffed_at_completion_cost is not UNSET:
            field_dict["CumulativeUnstaffedAtCompletionCost"] = cumulative_unstaffed_at_completion_cost
        if cumulative_unstaffed_at_completion_units is not UNSET:
            field_dict["CumulativeUnstaffedAtCompletionUnits"] = cumulative_unstaffed_at_completion_units
        if cumulative_unstaffed_planned_cost is not UNSET:
            field_dict["CumulativeUnstaffedPlannedCost"] = cumulative_unstaffed_planned_cost
        if cumulative_unstaffed_planned_units is not UNSET:
            field_dict["CumulativeUnstaffedPlannedUnits"] = cumulative_unstaffed_planned_units
        if cumulative_unstaffed_remaining_cost is not UNSET:
            field_dict["CumulativeUnstaffedRemainingCost"] = cumulative_unstaffed_remaining_cost
        if cumulative_unstaffed_remaining_late_cost is not UNSET:
            field_dict["CumulativeUnstaffedRemainingLateCost"] = cumulative_unstaffed_remaining_late_cost
        if cumulative_unstaffed_remaining_late_units is not UNSET:
            field_dict["CumulativeUnstaffedRemainingLateUnits"] = cumulative_unstaffed_remaining_late_units
        if cumulative_unstaffed_remaining_units is not UNSET:
            field_dict["CumulativeUnstaffedRemainingUnits"] = cumulative_unstaffed_remaining_units

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_date = d.pop("StartDate", UNSET)

        end_date = d.pop("EndDate", UNSET)

        financial_period_object_id = d.pop("FinancialPeriodObjectId", UNSET)

        actual_cost = d.pop("ActualCost", UNSET)

        actual_overtime_cost = d.pop("ActualOvertimeCost", UNSET)

        actual_overtime_units = d.pop("ActualOvertimeUnits", UNSET)

        actual_regular_cost = d.pop("ActualRegularCost", UNSET)

        actual_regular_units = d.pop("ActualRegularUnits", UNSET)

        actual_units = d.pop("ActualUnits", UNSET)

        at_completion_cost = d.pop("AtCompletionCost", UNSET)

        at_completion_units = d.pop("AtCompletionUnits", UNSET)

        limit = d.pop("Limit", UNSET)

        period_actual_cost = d.pop("PeriodActualCost", UNSET)

        period_actual_units = d.pop("PeriodActualUnits", UNSET)

        period_at_completion_cost = d.pop("PeriodAtCompletionCost", UNSET)

        period_at_completion_units = d.pop("PeriodAtCompletionUnits", UNSET)

        planned_cost = d.pop("PlannedCost", UNSET)

        planned_units = d.pop("PlannedUnits", UNSET)

        remaining_cost = d.pop("RemainingCost", UNSET)

        remaining_late_cost = d.pop("RemainingLateCost", UNSET)

        remaining_late_units = d.pop("RemainingLateUnits", UNSET)

        remaining_units = d.pop("RemainingUnits", UNSET)

        staffed_actual_cost = d.pop("StaffedActualCost", UNSET)

        staffed_actual_overtime_cost = d.pop("StaffedActualOvertimeCost", UNSET)

        staffed_actual_overtime_units = d.pop("StaffedActualOvertimeUnits", UNSET)

        staffed_actual_regular_cost = d.pop("StaffedActualRegularCost", UNSET)

        staffed_actual_regular_units = d.pop("StaffedActualRegularUnits", UNSET)

        staffed_actual_units = d.pop("StaffedActualUnits", UNSET)

        staffed_at_completion_cost = d.pop("StaffedAtCompletionCost", UNSET)

        staffed_at_completion_units = d.pop("StaffedAtCompletionUnits", UNSET)

        staffed_planned_cost = d.pop("StaffedPlannedCost", UNSET)

        staffed_planned_units = d.pop("StaffedPlannedUnits", UNSET)

        staffed_remaining_cost = d.pop("StaffedRemainingCost", UNSET)

        staffed_remaining_late_cost = d.pop("StaffedRemainingLateCost", UNSET)

        staffed_remaining_late_units = d.pop("StaffedRemainingLateUnits", UNSET)

        staffed_remaining_units = d.pop("StaffedRemainingUnits", UNSET)

        unstaffed_actual_cost = d.pop("UnstaffedActualCost", UNSET)

        unstaffed_actual_overtime_cost = d.pop("UnstaffedActualOvertimeCost", UNSET)

        unstaffed_actual_overtime_units = d.pop("UnstaffedActualOvertimeUnits", UNSET)

        unstaffed_actual_regular_cost = d.pop("UnstaffedActualRegularCost", UNSET)

        unstaffed_actual_regular_units = d.pop("UnstaffedActualRegularUnits", UNSET)

        unstaffed_actual_units = d.pop("UnstaffedActualUnits", UNSET)

        unstaffed_at_completion_cost = d.pop("UnstaffedAtCompletionCost", UNSET)

        unstaffed_at_completion_units = d.pop("UnstaffedAtCompletionUnits", UNSET)

        unstaffed_planned_cost = d.pop("UnstaffedPlannedCost", UNSET)

        unstaffed_planned_units = d.pop("UnstaffedPlannedUnits", UNSET)

        unstaffed_remaining_cost = d.pop("UnstaffedRemainingCost", UNSET)

        unstaffed_remaining_late_cost = d.pop("UnstaffedRemainingLateCost", UNSET)

        unstaffed_remaining_late_units = d.pop("UnstaffedRemainingLateUnits", UNSET)

        unstaffed_remaining_units = d.pop("UnstaffedRemainingUnits", UNSET)

        cumulative_actual_cost = d.pop("CumulativeActualCost", UNSET)

        cumulative_actual_overtime_cost = d.pop("CumulativeActualOvertimeCost", UNSET)

        cumulative_actual_overtime_units = d.pop("CumulativeActualOvertimeUnits", UNSET)

        cumulative_actual_regular_cost = d.pop("CumulativeActualRegularCost", UNSET)

        cumulative_actual_regular_units = d.pop("CumulativeActualRegularUnits", UNSET)

        cumulative_actual_units = d.pop("CumulativeActualUnits", UNSET)

        cumulative_at_completion_cost = d.pop("CumulativeAtCompletionCost", UNSET)

        cumulative_at_completion_units = d.pop("CumulativeAtCompletionUnits", UNSET)

        cumulative_limit = d.pop("CumulativeLimit", UNSET)

        cumulative_period_actual_cost = d.pop("CumulativePeriodActualCost", UNSET)

        cumulative_period_actual_units = d.pop("CumulativePeriodActualUnits", UNSET)

        cumulative_period_at_completion_cost = d.pop("CumulativePeriodAtCompletionCost", UNSET)

        cumulative_period_at_completion_units = d.pop("CumulativePeriodAtCompletionUnits", UNSET)

        cumulative_planned_cost = d.pop("CumulativePlannedCost", UNSET)

        cumulative_planned_units = d.pop("CumulativePlannedUnits", UNSET)

        cumulative_remaining_cost = d.pop("CumulativeRemainingCost", UNSET)

        cumulative_remaining_late_cost = d.pop("CumulativeRemainingLateCost", UNSET)

        cumulative_remaining_late_units = d.pop("CumulativeRemainingLateUnits", UNSET)

        cumulative_remaining_units = d.pop("CumulativeRemainingUnits", UNSET)

        cumulative_staffed_actual_cost = d.pop("CumulativeStaffedActualCost", UNSET)

        cumulative_staffed_actual_overtime_cost = d.pop("CumulativeStaffedActualOvertimeCost", UNSET)

        cumulative_staffed_actual_overtime_units = d.pop("CumulativeStaffedActualOvertimeUnits", UNSET)

        cumulative_staffed_actual_regular_cost = d.pop("CumulativeStaffedActualRegularCost", UNSET)

        cumulative_staffed_actual_regular_units = d.pop("CumulativeStaffedActualRegularUnits", UNSET)

        cumulative_staffed_actual_units = d.pop("CumulativeStaffedActualUnits", UNSET)

        cumulative_staffed_at_completion_cost = d.pop("CumulativeStaffedAtCompletionCost", UNSET)

        cumulative_staffed_at_completion_units = d.pop("CumulativeStaffedAtCompletionUnits", UNSET)

        cumulative_staffed_planned_cost = d.pop("CumulativeStaffedPlannedCost", UNSET)

        cumulative_staffed_planned_units = d.pop("CumulativeStaffedPlannedUnits", UNSET)

        cumulative_staffed_remaining_cost = d.pop("CumulativeStaffedRemainingCost", UNSET)

        cumulative_staffed_remaining_late_cost = d.pop("CumulativeStaffedRemainingLateCost", UNSET)

        cumulative_staffed_remaining_late_units = d.pop("CumulativeStaffedRemainingLateUnits", UNSET)

        cumulative_staffed_remaining_units = d.pop("CumulativeStaffedRemainingUnits", UNSET)

        cumulative_unstaffed_actual_cost = d.pop("CumulativeUnstaffedActualCost", UNSET)

        cumulative_unstaffed_actual_overtime_cost = d.pop("CumulativeUnstaffedActualOvertimeCost", UNSET)

        cumulative_unstaffed_actual_overtime_units = d.pop("CumulativeUnstaffedActualOvertimeUnits", UNSET)

        cumulative_unstaffed_actual_regular_cost = d.pop("CumulativeUnstaffedActualRegularCost", UNSET)

        cumulative_unstaffed_actual_regular_units = d.pop("CumulativeUnstaffedActualRegularUnits", UNSET)

        cumulative_unstaffed_actual_units = d.pop("CumulativeUnstaffedActualUnits", UNSET)

        cumulative_unstaffed_at_completion_cost = d.pop("CumulativeUnstaffedAtCompletionCost", UNSET)

        cumulative_unstaffed_at_completion_units = d.pop("CumulativeUnstaffedAtCompletionUnits", UNSET)

        cumulative_unstaffed_planned_cost = d.pop("CumulativeUnstaffedPlannedCost", UNSET)

        cumulative_unstaffed_planned_units = d.pop("CumulativeUnstaffedPlannedUnits", UNSET)

        cumulative_unstaffed_remaining_cost = d.pop("CumulativeUnstaffedRemainingCost", UNSET)

        cumulative_unstaffed_remaining_late_cost = d.pop("CumulativeUnstaffedRemainingLateCost", UNSET)

        cumulative_unstaffed_remaining_late_units = d.pop("CumulativeUnstaffedRemainingLateUnits", UNSET)

        cumulative_unstaffed_remaining_units = d.pop("CumulativeUnstaffedRemainingUnits", UNSET)

        resource_role_spread_period = cls(
            start_date=start_date,
            end_date=end_date,
            financial_period_object_id=financial_period_object_id,
            actual_cost=actual_cost,
            actual_overtime_cost=actual_overtime_cost,
            actual_overtime_units=actual_overtime_units,
            actual_regular_cost=actual_regular_cost,
            actual_regular_units=actual_regular_units,
            actual_units=actual_units,
            at_completion_cost=at_completion_cost,
            at_completion_units=at_completion_units,
            limit=limit,
            period_actual_cost=period_actual_cost,
            period_actual_units=period_actual_units,
            period_at_completion_cost=period_at_completion_cost,
            period_at_completion_units=period_at_completion_units,
            planned_cost=planned_cost,
            planned_units=planned_units,
            remaining_cost=remaining_cost,
            remaining_late_cost=remaining_late_cost,
            remaining_late_units=remaining_late_units,
            remaining_units=remaining_units,
            staffed_actual_cost=staffed_actual_cost,
            staffed_actual_overtime_cost=staffed_actual_overtime_cost,
            staffed_actual_overtime_units=staffed_actual_overtime_units,
            staffed_actual_regular_cost=staffed_actual_regular_cost,
            staffed_actual_regular_units=staffed_actual_regular_units,
            staffed_actual_units=staffed_actual_units,
            staffed_at_completion_cost=staffed_at_completion_cost,
            staffed_at_completion_units=staffed_at_completion_units,
            staffed_planned_cost=staffed_planned_cost,
            staffed_planned_units=staffed_planned_units,
            staffed_remaining_cost=staffed_remaining_cost,
            staffed_remaining_late_cost=staffed_remaining_late_cost,
            staffed_remaining_late_units=staffed_remaining_late_units,
            staffed_remaining_units=staffed_remaining_units,
            unstaffed_actual_cost=unstaffed_actual_cost,
            unstaffed_actual_overtime_cost=unstaffed_actual_overtime_cost,
            unstaffed_actual_overtime_units=unstaffed_actual_overtime_units,
            unstaffed_actual_regular_cost=unstaffed_actual_regular_cost,
            unstaffed_actual_regular_units=unstaffed_actual_regular_units,
            unstaffed_actual_units=unstaffed_actual_units,
            unstaffed_at_completion_cost=unstaffed_at_completion_cost,
            unstaffed_at_completion_units=unstaffed_at_completion_units,
            unstaffed_planned_cost=unstaffed_planned_cost,
            unstaffed_planned_units=unstaffed_planned_units,
            unstaffed_remaining_cost=unstaffed_remaining_cost,
            unstaffed_remaining_late_cost=unstaffed_remaining_late_cost,
            unstaffed_remaining_late_units=unstaffed_remaining_late_units,
            unstaffed_remaining_units=unstaffed_remaining_units,
            cumulative_actual_cost=cumulative_actual_cost,
            cumulative_actual_overtime_cost=cumulative_actual_overtime_cost,
            cumulative_actual_overtime_units=cumulative_actual_overtime_units,
            cumulative_actual_regular_cost=cumulative_actual_regular_cost,
            cumulative_actual_regular_units=cumulative_actual_regular_units,
            cumulative_actual_units=cumulative_actual_units,
            cumulative_at_completion_cost=cumulative_at_completion_cost,
            cumulative_at_completion_units=cumulative_at_completion_units,
            cumulative_limit=cumulative_limit,
            cumulative_period_actual_cost=cumulative_period_actual_cost,
            cumulative_period_actual_units=cumulative_period_actual_units,
            cumulative_period_at_completion_cost=cumulative_period_at_completion_cost,
            cumulative_period_at_completion_units=cumulative_period_at_completion_units,
            cumulative_planned_cost=cumulative_planned_cost,
            cumulative_planned_units=cumulative_planned_units,
            cumulative_remaining_cost=cumulative_remaining_cost,
            cumulative_remaining_late_cost=cumulative_remaining_late_cost,
            cumulative_remaining_late_units=cumulative_remaining_late_units,
            cumulative_remaining_units=cumulative_remaining_units,
            cumulative_staffed_actual_cost=cumulative_staffed_actual_cost,
            cumulative_staffed_actual_overtime_cost=cumulative_staffed_actual_overtime_cost,
            cumulative_staffed_actual_overtime_units=cumulative_staffed_actual_overtime_units,
            cumulative_staffed_actual_regular_cost=cumulative_staffed_actual_regular_cost,
            cumulative_staffed_actual_regular_units=cumulative_staffed_actual_regular_units,
            cumulative_staffed_actual_units=cumulative_staffed_actual_units,
            cumulative_staffed_at_completion_cost=cumulative_staffed_at_completion_cost,
            cumulative_staffed_at_completion_units=cumulative_staffed_at_completion_units,
            cumulative_staffed_planned_cost=cumulative_staffed_planned_cost,
            cumulative_staffed_planned_units=cumulative_staffed_planned_units,
            cumulative_staffed_remaining_cost=cumulative_staffed_remaining_cost,
            cumulative_staffed_remaining_late_cost=cumulative_staffed_remaining_late_cost,
            cumulative_staffed_remaining_late_units=cumulative_staffed_remaining_late_units,
            cumulative_staffed_remaining_units=cumulative_staffed_remaining_units,
            cumulative_unstaffed_actual_cost=cumulative_unstaffed_actual_cost,
            cumulative_unstaffed_actual_overtime_cost=cumulative_unstaffed_actual_overtime_cost,
            cumulative_unstaffed_actual_overtime_units=cumulative_unstaffed_actual_overtime_units,
            cumulative_unstaffed_actual_regular_cost=cumulative_unstaffed_actual_regular_cost,
            cumulative_unstaffed_actual_regular_units=cumulative_unstaffed_actual_regular_units,
            cumulative_unstaffed_actual_units=cumulative_unstaffed_actual_units,
            cumulative_unstaffed_at_completion_cost=cumulative_unstaffed_at_completion_cost,
            cumulative_unstaffed_at_completion_units=cumulative_unstaffed_at_completion_units,
            cumulative_unstaffed_planned_cost=cumulative_unstaffed_planned_cost,
            cumulative_unstaffed_planned_units=cumulative_unstaffed_planned_units,
            cumulative_unstaffed_remaining_cost=cumulative_unstaffed_remaining_cost,
            cumulative_unstaffed_remaining_late_cost=cumulative_unstaffed_remaining_late_cost,
            cumulative_unstaffed_remaining_late_units=cumulative_unstaffed_remaining_late_units,
            cumulative_unstaffed_remaining_units=cumulative_unstaffed_remaining_units,
        )

        resource_role_spread_period.additional_properties = d
        return resource_role_spread_period

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
