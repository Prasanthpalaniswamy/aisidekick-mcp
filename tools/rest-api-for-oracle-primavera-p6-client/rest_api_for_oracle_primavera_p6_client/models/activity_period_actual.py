from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityPeriodActual")


@_attrs_define
class ActivityPeriodActual:
    """ActivityPeriodActual Entity

    Attributes:
        activity_object_id (int): The unique ID of the associated activity.
        financial_period_object_id (int): The unique ID of the associated financial period.
        actual_expense_cost (float | Unset): The actual expense cost on this activity during a financial period.
        actual_labor_cost (float | Unset): The actual labor cost on this activity during a financial period.
        actual_labor_units (float | Unset): The actual labor units on this activity during a financial period.
        actual_material_cost (float | Unset): The actual material cost on this activity during a financial period.
        actual_non_labor_cost (float | Unset): The actual nonlabor cost on this activity during a financial period.
        actual_non_labor_units (float | Unset): The actual nonlabor units on this activity during a financial period.
        create_date (datetime.datetime | Unset): The date this activity period actual was created.
        create_user (str | Unset): The name of the user that created this activity period actual.
        earned_value_cost (float | Unset): The earned value cost on this activity during a financial period.
        earned_value_labor_units (float | Unset): The earned value labor units on this activity during a financial
            period.
        is_baseline (bool | Unset): The boolean value indicating if this business object is related to a Project or
            Baseline
        is_template (bool | Unset): The boolean value indicating if this business object is related to a template
            Project.
        last_update_date (datetime.datetime | Unset): The date this activity period actual was last updated.
        last_update_user (str | Unset): The name of the user that last updated this activity period actual.
        planned_value_cost (float | Unset): The planned value cost on this activity during a financial period.
        planned_value_labor_units (float | Unset): The planned value labor units on this activity during a financial
            period.
        project_object_id (int | Unset): The unique ID of the associated project.
        wbs_object_id (int | Unset): The unique ID of the WBS for the activity.
    """

    activity_object_id: int
    financial_period_object_id: int
    actual_expense_cost: float | Unset = UNSET
    actual_labor_cost: float | Unset = UNSET
    actual_labor_units: float | Unset = UNSET
    actual_material_cost: float | Unset = UNSET
    actual_non_labor_cost: float | Unset = UNSET
    actual_non_labor_units: float | Unset = UNSET
    create_date: datetime.datetime | Unset = UNSET
    create_user: str | Unset = UNSET
    earned_value_cost: float | Unset = UNSET
    earned_value_labor_units: float | Unset = UNSET
    is_baseline: bool | Unset = UNSET
    is_template: bool | Unset = UNSET
    last_update_date: datetime.datetime | Unset = UNSET
    last_update_user: str | Unset = UNSET
    planned_value_cost: float | Unset = UNSET
    planned_value_labor_units: float | Unset = UNSET
    project_object_id: int | Unset = UNSET
    wbs_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_object_id = self.activity_object_id

        financial_period_object_id = self.financial_period_object_id

        actual_expense_cost = self.actual_expense_cost

        actual_labor_cost = self.actual_labor_cost

        actual_labor_units = self.actual_labor_units

        actual_material_cost = self.actual_material_cost

        actual_non_labor_cost = self.actual_non_labor_cost

        actual_non_labor_units = self.actual_non_labor_units

        create_date: str | Unset = UNSET
        if not isinstance(self.create_date, Unset):
            create_date = self.create_date.isoformat()

        create_user = self.create_user

        earned_value_cost = self.earned_value_cost

        earned_value_labor_units = self.earned_value_labor_units

        is_baseline = self.is_baseline

        is_template = self.is_template

        last_update_date: str | Unset = UNSET
        if not isinstance(self.last_update_date, Unset):
            last_update_date = self.last_update_date.isoformat()

        last_update_user = self.last_update_user

        planned_value_cost = self.planned_value_cost

        planned_value_labor_units = self.planned_value_labor_units

        project_object_id = self.project_object_id

        wbs_object_id = self.wbs_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ActivityObjectId": activity_object_id,
                "FinancialPeriodObjectId": financial_period_object_id,
            }
        )
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
        if create_date is not UNSET:
            field_dict["CreateDate"] = create_date
        if create_user is not UNSET:
            field_dict["CreateUser"] = create_user
        if earned_value_cost is not UNSET:
            field_dict["EarnedValueCost"] = earned_value_cost
        if earned_value_labor_units is not UNSET:
            field_dict["EarnedValueLaborUnits"] = earned_value_labor_units
        if is_baseline is not UNSET:
            field_dict["IsBaseline"] = is_baseline
        if is_template is not UNSET:
            field_dict["IsTemplate"] = is_template
        if last_update_date is not UNSET:
            field_dict["LastUpdateDate"] = last_update_date
        if last_update_user is not UNSET:
            field_dict["LastUpdateUser"] = last_update_user
        if planned_value_cost is not UNSET:
            field_dict["PlannedValueCost"] = planned_value_cost
        if planned_value_labor_units is not UNSET:
            field_dict["PlannedValueLaborUnits"] = planned_value_labor_units
        if project_object_id is not UNSET:
            field_dict["ProjectObjectId"] = project_object_id
        if wbs_object_id is not UNSET:
            field_dict["WBSObjectId"] = wbs_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        activity_object_id = d.pop("ActivityObjectId")

        financial_period_object_id = d.pop("FinancialPeriodObjectId")

        actual_expense_cost = d.pop("ActualExpenseCost", UNSET)

        actual_labor_cost = d.pop("ActualLaborCost", UNSET)

        actual_labor_units = d.pop("ActualLaborUnits", UNSET)

        actual_material_cost = d.pop("ActualMaterialCost", UNSET)

        actual_non_labor_cost = d.pop("ActualNonLaborCost", UNSET)

        actual_non_labor_units = d.pop("ActualNonLaborUnits", UNSET)

        _create_date = d.pop("CreateDate", UNSET)
        create_date: datetime.datetime | Unset
        if isinstance(_create_date, Unset):
            create_date = UNSET
        else:
            create_date = isoparse(_create_date)

        create_user = d.pop("CreateUser", UNSET)

        earned_value_cost = d.pop("EarnedValueCost", UNSET)

        earned_value_labor_units = d.pop("EarnedValueLaborUnits", UNSET)

        is_baseline = d.pop("IsBaseline", UNSET)

        is_template = d.pop("IsTemplate", UNSET)

        _last_update_date = d.pop("LastUpdateDate", UNSET)
        last_update_date: datetime.datetime | Unset
        if isinstance(_last_update_date, Unset):
            last_update_date = UNSET
        else:
            last_update_date = isoparse(_last_update_date)

        last_update_user = d.pop("LastUpdateUser", UNSET)

        planned_value_cost = d.pop("PlannedValueCost", UNSET)

        planned_value_labor_units = d.pop("PlannedValueLaborUnits", UNSET)

        project_object_id = d.pop("ProjectObjectId", UNSET)

        wbs_object_id = d.pop("WBSObjectId", UNSET)

        activity_period_actual = cls(
            activity_object_id=activity_object_id,
            financial_period_object_id=financial_period_object_id,
            actual_expense_cost=actual_expense_cost,
            actual_labor_cost=actual_labor_cost,
            actual_labor_units=actual_labor_units,
            actual_material_cost=actual_material_cost,
            actual_non_labor_cost=actual_non_labor_cost,
            actual_non_labor_units=actual_non_labor_units,
            create_date=create_date,
            create_user=create_user,
            earned_value_cost=earned_value_cost,
            earned_value_labor_units=earned_value_labor_units,
            is_baseline=is_baseline,
            is_template=is_template,
            last_update_date=last_update_date,
            last_update_user=last_update_user,
            planned_value_cost=planned_value_cost,
            planned_value_labor_units=planned_value_labor_units,
            project_object_id=project_object_id,
            wbs_object_id=wbs_object_id,
        )

        activity_period_actual.additional_properties = d
        return activity_period_actual

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
