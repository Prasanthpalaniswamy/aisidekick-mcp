from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cbs_rsrc_expense_spread_period import CBSRsrcExpenseSpreadPeriod


T = TypeVar("T", bound="CBSExpenseSpread")


@_attrs_define
class CBSExpenseSpread:
    """
    Attributes:
        cbsobject_id (int | Unset):
        baseline_project_object_id (int | Unset):
        project_object_id (int | Unset):
        project_id (str | Unset):
        project_name (str | Unset):
        original_project_object_id (int | Unset):
        cbs_object_id (int | Unset):
        expense_category_object_id (int | Unset):
        expense_category_name (str | Unset):
        baseline_type (str | Unset):
        data_date (datetime.datetime | Unset):
        summary_actual_cost (float | Unset):
        summary_actual_units (float | Unset):
        summary_at_completion_cost (float | Unset):
        summary_at_completion_units (float | Unset):
        summary_planned_cost (float | Unset):
        summary_planned_units (float | Unset):
        summary_remaining_cost (float | Unset):
        summary_remaining_units (float | Unset):
        start_date (datetime.datetime | Unset):
        end_date (datetime.datetime | Unset):
        period_type (str | Unset):
        period (list[CBSRsrcExpenseSpreadPeriod] | Unset):
    """

    cbsobject_id: int | Unset = UNSET
    baseline_project_object_id: int | Unset = UNSET
    project_object_id: int | Unset = UNSET
    project_id: str | Unset = UNSET
    project_name: str | Unset = UNSET
    original_project_object_id: int | Unset = UNSET
    cbs_object_id: int | Unset = UNSET
    expense_category_object_id: int | Unset = UNSET
    expense_category_name: str | Unset = UNSET
    baseline_type: str | Unset = UNSET
    data_date: datetime.datetime | Unset = UNSET
    summary_actual_cost: float | Unset = UNSET
    summary_actual_units: float | Unset = UNSET
    summary_at_completion_cost: float | Unset = UNSET
    summary_at_completion_units: float | Unset = UNSET
    summary_planned_cost: float | Unset = UNSET
    summary_planned_units: float | Unset = UNSET
    summary_remaining_cost: float | Unset = UNSET
    summary_remaining_units: float | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    end_date: datetime.datetime | Unset = UNSET
    period_type: str | Unset = UNSET
    period: list[CBSRsrcExpenseSpreadPeriod] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cbsobject_id = self.cbsobject_id

        baseline_project_object_id = self.baseline_project_object_id

        project_object_id = self.project_object_id

        project_id = self.project_id

        project_name = self.project_name

        original_project_object_id = self.original_project_object_id

        cbs_object_id = self.cbs_object_id

        expense_category_object_id = self.expense_category_object_id

        expense_category_name = self.expense_category_name

        baseline_type = self.baseline_type

        data_date: str | Unset = UNSET
        if not isinstance(self.data_date, Unset):
            data_date = self.data_date.isoformat()

        summary_actual_cost = self.summary_actual_cost

        summary_actual_units = self.summary_actual_units

        summary_at_completion_cost = self.summary_at_completion_cost

        summary_at_completion_units = self.summary_at_completion_units

        summary_planned_cost = self.summary_planned_cost

        summary_planned_units = self.summary_planned_units

        summary_remaining_cost = self.summary_remaining_cost

        summary_remaining_units = self.summary_remaining_units

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

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
        if cbsobject_id is not UNSET:
            field_dict["cbsobjectId"] = cbsobject_id
        if baseline_project_object_id is not UNSET:
            field_dict["BaselineProjectObjectId"] = baseline_project_object_id
        if project_object_id is not UNSET:
            field_dict["ProjectObjectId"] = project_object_id
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if project_name is not UNSET:
            field_dict["ProjectName"] = project_name
        if original_project_object_id is not UNSET:
            field_dict["OriginalProjectObjectId"] = original_project_object_id
        if cbs_object_id is not UNSET:
            field_dict["CBSObjectId"] = cbs_object_id
        if expense_category_object_id is not UNSET:
            field_dict["ExpenseCategoryObjectId"] = expense_category_object_id
        if expense_category_name is not UNSET:
            field_dict["ExpenseCategoryName"] = expense_category_name
        if baseline_type is not UNSET:
            field_dict["BaselineType"] = baseline_type
        if data_date is not UNSET:
            field_dict["DataDate"] = data_date
        if summary_actual_cost is not UNSET:
            field_dict["SummaryActualCost"] = summary_actual_cost
        if summary_actual_units is not UNSET:
            field_dict["SummaryActualUnits"] = summary_actual_units
        if summary_at_completion_cost is not UNSET:
            field_dict["SummaryAtCompletionCost"] = summary_at_completion_cost
        if summary_at_completion_units is not UNSET:
            field_dict["SummaryAtCompletionUnits"] = summary_at_completion_units
        if summary_planned_cost is not UNSET:
            field_dict["SummaryPlannedCost"] = summary_planned_cost
        if summary_planned_units is not UNSET:
            field_dict["SummaryPlannedUnits"] = summary_planned_units
        if summary_remaining_cost is not UNSET:
            field_dict["SummaryRemainingCost"] = summary_remaining_cost
        if summary_remaining_units is not UNSET:
            field_dict["SummaryRemainingUnits"] = summary_remaining_units
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
        from ..models.cbs_rsrc_expense_spread_period import CBSRsrcExpenseSpreadPeriod

        d = dict(src_dict)
        cbsobject_id = d.pop("cbsobjectId", UNSET)

        baseline_project_object_id = d.pop("BaselineProjectObjectId", UNSET)

        project_object_id = d.pop("ProjectObjectId", UNSET)

        project_id = d.pop("ProjectId", UNSET)

        project_name = d.pop("ProjectName", UNSET)

        original_project_object_id = d.pop("OriginalProjectObjectId", UNSET)

        cbs_object_id = d.pop("CBSObjectId", UNSET)

        expense_category_object_id = d.pop("ExpenseCategoryObjectId", UNSET)

        expense_category_name = d.pop("ExpenseCategoryName", UNSET)

        baseline_type = d.pop("BaselineType", UNSET)

        _data_date = d.pop("DataDate", UNSET)
        data_date: datetime.datetime | Unset
        if isinstance(_data_date, Unset):
            data_date = UNSET
        else:
            data_date = isoparse(_data_date)

        summary_actual_cost = d.pop("SummaryActualCost", UNSET)

        summary_actual_units = d.pop("SummaryActualUnits", UNSET)

        summary_at_completion_cost = d.pop("SummaryAtCompletionCost", UNSET)

        summary_at_completion_units = d.pop("SummaryAtCompletionUnits", UNSET)

        summary_planned_cost = d.pop("SummaryPlannedCost", UNSET)

        summary_planned_units = d.pop("SummaryPlannedUnits", UNSET)

        summary_remaining_cost = d.pop("SummaryRemainingCost", UNSET)

        summary_remaining_units = d.pop("SummaryRemainingUnits", UNSET)

        _start_date = d.pop("StartDate", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("EndDate", UNSET)
        end_date: datetime.datetime | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        period_type = d.pop("PeriodType", UNSET)

        _period = d.pop("Period", UNSET)
        period: list[CBSRsrcExpenseSpreadPeriod] | Unset = UNSET
        if _period is not UNSET:
            period = []
            for period_item_data in _period:
                period_item = CBSRsrcExpenseSpreadPeriod.from_dict(period_item_data)

                period.append(period_item)

        cbs_expense_spread = cls(
            cbsobject_id=cbsobject_id,
            baseline_project_object_id=baseline_project_object_id,
            project_object_id=project_object_id,
            project_id=project_id,
            project_name=project_name,
            original_project_object_id=original_project_object_id,
            cbs_object_id=cbs_object_id,
            expense_category_object_id=expense_category_object_id,
            expense_category_name=expense_category_name,
            baseline_type=baseline_type,
            data_date=data_date,
            summary_actual_cost=summary_actual_cost,
            summary_actual_units=summary_actual_units,
            summary_at_completion_cost=summary_at_completion_cost,
            summary_at_completion_units=summary_at_completion_units,
            summary_planned_cost=summary_planned_cost,
            summary_planned_units=summary_planned_units,
            summary_remaining_cost=summary_remaining_cost,
            summary_remaining_units=summary_remaining_units,
            start_date=start_date,
            end_date=end_date,
            period_type=period_type,
            period=period,
        )

        cbs_expense_spread.additional_properties = d
        return cbs_expense_spread

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
