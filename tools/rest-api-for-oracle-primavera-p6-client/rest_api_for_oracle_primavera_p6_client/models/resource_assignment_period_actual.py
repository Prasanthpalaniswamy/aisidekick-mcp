from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceAssignmentPeriodActual")


@_attrs_define
class ResourceAssignmentPeriodActual:
    """ResourceAssignmentPeriodActual Entity

    Attributes:
        actual_cost (float): The actual cost on this resource assignment during a financial period.
        actual_units (float): The actual units on this resource assignment during a financial period.
        financial_period_object_id (int): The unique ID of the associated financial period.
        resource_assignment_object_id (int): The unique ID of the associated resource assignment.
        activity_object_id (int | Unset): The unique ID of the associated activity.
        create_date (datetime.datetime | Unset): The date this resource assignment period actual was created.
        create_user (str | Unset): The name of the user that created this resource assignment period actual.
        is_baseline (bool | Unset): The boolean value indicating if this business object is related to a Project or
            Baseline
        is_template (bool | Unset): The boolean value indicating if this business object is related to a template
            Project.
        last_update_date (datetime.datetime | Unset): The date this resource assignment period actual was last updated.
        last_update_user (str | Unset): The name of the user that last updated this resource assignment period actual.
        project_object_id (int | Unset): The unique ID of the associated project.
        resource_type (str | Unset): The resource type: "Labor", "Nonlabor", or "Material".
        wbs_object_id (int | Unset): The unique ID of the WBS for the associated activity.
    """

    actual_cost: float
    actual_units: float
    financial_period_object_id: int
    resource_assignment_object_id: int
    activity_object_id: int | Unset = UNSET
    create_date: datetime.datetime | Unset = UNSET
    create_user: str | Unset = UNSET
    is_baseline: bool | Unset = UNSET
    is_template: bool | Unset = UNSET
    last_update_date: datetime.datetime | Unset = UNSET
    last_update_user: str | Unset = UNSET
    project_object_id: int | Unset = UNSET
    resource_type: str | Unset = UNSET
    wbs_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actual_cost = self.actual_cost

        actual_units = self.actual_units

        financial_period_object_id = self.financial_period_object_id

        resource_assignment_object_id = self.resource_assignment_object_id

        activity_object_id = self.activity_object_id

        create_date: str | Unset = UNSET
        if not isinstance(self.create_date, Unset):
            create_date = self.create_date.isoformat()

        create_user = self.create_user

        is_baseline = self.is_baseline

        is_template = self.is_template

        last_update_date: str | Unset = UNSET
        if not isinstance(self.last_update_date, Unset):
            last_update_date = self.last_update_date.isoformat()

        last_update_user = self.last_update_user

        project_object_id = self.project_object_id

        resource_type = self.resource_type

        wbs_object_id = self.wbs_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ActualCost": actual_cost,
                "ActualUnits": actual_units,
                "FinancialPeriodObjectId": financial_period_object_id,
                "ResourceAssignmentObjectId": resource_assignment_object_id,
            }
        )
        if activity_object_id is not UNSET:
            field_dict["ActivityObjectId"] = activity_object_id
        if create_date is not UNSET:
            field_dict["CreateDate"] = create_date
        if create_user is not UNSET:
            field_dict["CreateUser"] = create_user
        if is_baseline is not UNSET:
            field_dict["IsBaseline"] = is_baseline
        if is_template is not UNSET:
            field_dict["IsTemplate"] = is_template
        if last_update_date is not UNSET:
            field_dict["LastUpdateDate"] = last_update_date
        if last_update_user is not UNSET:
            field_dict["LastUpdateUser"] = last_update_user
        if project_object_id is not UNSET:
            field_dict["ProjectObjectId"] = project_object_id
        if resource_type is not UNSET:
            field_dict["ResourceType"] = resource_type
        if wbs_object_id is not UNSET:
            field_dict["WBSObjectId"] = wbs_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        actual_cost = d.pop("ActualCost")

        actual_units = d.pop("ActualUnits")

        financial_period_object_id = d.pop("FinancialPeriodObjectId")

        resource_assignment_object_id = d.pop("ResourceAssignmentObjectId")

        activity_object_id = d.pop("ActivityObjectId", UNSET)

        _create_date = d.pop("CreateDate", UNSET)
        create_date: datetime.datetime | Unset
        if isinstance(_create_date, Unset):
            create_date = UNSET
        else:
            create_date = isoparse(_create_date)

        create_user = d.pop("CreateUser", UNSET)

        is_baseline = d.pop("IsBaseline", UNSET)

        is_template = d.pop("IsTemplate", UNSET)

        _last_update_date = d.pop("LastUpdateDate", UNSET)
        last_update_date: datetime.datetime | Unset
        if isinstance(_last_update_date, Unset):
            last_update_date = UNSET
        else:
            last_update_date = isoparse(_last_update_date)

        last_update_user = d.pop("LastUpdateUser", UNSET)

        project_object_id = d.pop("ProjectObjectId", UNSET)

        resource_type = d.pop("ResourceType", UNSET)

        wbs_object_id = d.pop("WBSObjectId", UNSET)

        resource_assignment_period_actual = cls(
            actual_cost=actual_cost,
            actual_units=actual_units,
            financial_period_object_id=financial_period_object_id,
            resource_assignment_object_id=resource_assignment_object_id,
            activity_object_id=activity_object_id,
            create_date=create_date,
            create_user=create_user,
            is_baseline=is_baseline,
            is_template=is_template,
            last_update_date=last_update_date,
            last_update_user=last_update_user,
            project_object_id=project_object_id,
            resource_type=resource_type,
            wbs_object_id=wbs_object_id,
        )

        resource_assignment_period_actual.additional_properties = d
        return resource_assignment_period_actual

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
