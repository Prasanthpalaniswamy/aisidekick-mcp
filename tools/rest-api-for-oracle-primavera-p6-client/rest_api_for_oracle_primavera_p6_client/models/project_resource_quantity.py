from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectResourceQuantity")


@_attrs_define
class ProjectResourceQuantity:
    """ProjectResourceQuantity Entity

    Attributes:
        financial_period_1_quantity (float): The value that represents the resource allocation hours for the first
            financial period for this project resource quantity. If the week contains days from two different months, two
            ProjectResourceQuantity business objects will exist. The first business object's Quantity field represents the
            hours of the first week fragment (WeekStartDate and MonthStartDate have the same month value). The second
            business object's Quantity field represents the second week fragment (WeekStartDate and MonthStartDate have
            different month values).
        financial_period_2_quantity (float): The value that represents the resource allocation hours for the second
            financial period for this project resource quantity. If the week contains days from two different months, two
            ProjectResourceQuantity business objects will exist. The first business object's Quantity field represents the
            hours of the first week fragment (WeekStartDate and MonthStartDate have the same month value). The second
            business object's Quantity field represents the second week fragment (WeekStartDate and MonthStartDate have
            different month values).
        project_resource_object_id (int): The unique ID of the associated project resource.
        quantity (float): The value that represents the resource allocation hours per week for this project resource
            quantity. If the week contains days from two different months, two ProjectResourceQuantity business objects will
            exist. The first business object's Quantity field represents the hours of the first week fragment (WeekStartDate
            and MonthStartDate have the same month value). The second business object's Quantity field represents the second
            week fragment (WeekStartDate and MonthStartDate have different month values).
        week_start_date (datetime.datetime): The date value that represents the first day of the week.
        committed_flag (bool | Unset): The Boolean value that determines whether a resource is committed, and so, the
            resource assignment is stable and unlikely to change. When calculating availability, Primavera considers only
            assignments that are marked as committed.
        create_date (datetime.datetime | Unset): The date this project resource quantity was created.
        create_user (str | Unset): The name of the user that created this project resource quantity.
        financial_period_1_object_id (int | Unset): The unique ID of the associated first financial period for this
            project resource quantity.
        financial_period_2_object_id (int | Unset): The unique ID of the associated second financial period for this
            project resource quantity.
        financial_period_tmpl_id (int | Unset):
        is_baseline (bool | Unset): The boolean value indicating if this business object is related to a Project or
            Baseline
        is_template (bool | Unset): The boolean value indicating if this business object is related to a template
            Project.
        last_update_date (datetime.datetime | Unset): The date this project resource quantity was last updated.
        last_update_user (str | Unset): The name of the user that last updated this project resource quantity.
        month_start_date (datetime.datetime | Unset): The date value that represents the first day of the month. If the
            week contains days from two different months, two objects will exist. The first ProjectResourceQuantity object's
            MonthStartDate is the first day of the month for the first week fragment. The second ProjectResourceQuantity
            object's MonthStartDate is the first day of the month for the second week fragment.
        project_object_id (int | Unset): The unique ID of the associated project.
        resource_object_id (int | Unset): The unique ID of the associated resource.
        role_object_id (int | Unset): The unique ID of the associated role.
        wbs_object_id (int | Unset): The unique ID of the associated WBS.
    """

    financial_period_1_quantity: float
    financial_period_2_quantity: float
    project_resource_object_id: int
    quantity: float
    week_start_date: datetime.datetime
    committed_flag: bool | Unset = UNSET
    create_date: datetime.datetime | Unset = UNSET
    create_user: str | Unset = UNSET
    financial_period_1_object_id: int | Unset = UNSET
    financial_period_2_object_id: int | Unset = UNSET
    financial_period_tmpl_id: int | Unset = UNSET
    is_baseline: bool | Unset = UNSET
    is_template: bool | Unset = UNSET
    last_update_date: datetime.datetime | Unset = UNSET
    last_update_user: str | Unset = UNSET
    month_start_date: datetime.datetime | Unset = UNSET
    project_object_id: int | Unset = UNSET
    resource_object_id: int | Unset = UNSET
    role_object_id: int | Unset = UNSET
    wbs_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        financial_period_1_quantity = self.financial_period_1_quantity

        financial_period_2_quantity = self.financial_period_2_quantity

        project_resource_object_id = self.project_resource_object_id

        quantity = self.quantity

        week_start_date = self.week_start_date.isoformat()

        committed_flag = self.committed_flag

        create_date: str | Unset = UNSET
        if not isinstance(self.create_date, Unset):
            create_date = self.create_date.isoformat()

        create_user = self.create_user

        financial_period_1_object_id = self.financial_period_1_object_id

        financial_period_2_object_id = self.financial_period_2_object_id

        financial_period_tmpl_id = self.financial_period_tmpl_id

        is_baseline = self.is_baseline

        is_template = self.is_template

        last_update_date: str | Unset = UNSET
        if not isinstance(self.last_update_date, Unset):
            last_update_date = self.last_update_date.isoformat()

        last_update_user = self.last_update_user

        month_start_date: str | Unset = UNSET
        if not isinstance(self.month_start_date, Unset):
            month_start_date = self.month_start_date.isoformat()

        project_object_id = self.project_object_id

        resource_object_id = self.resource_object_id

        role_object_id = self.role_object_id

        wbs_object_id = self.wbs_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "FinancialPeriod1Quantity": financial_period_1_quantity,
                "FinancialPeriod2Quantity": financial_period_2_quantity,
                "ProjectResourceObjectId": project_resource_object_id,
                "Quantity": quantity,
                "WeekStartDate": week_start_date,
            }
        )
        if committed_flag is not UNSET:
            field_dict["CommittedFlag"] = committed_flag
        if create_date is not UNSET:
            field_dict["CreateDate"] = create_date
        if create_user is not UNSET:
            field_dict["CreateUser"] = create_user
        if financial_period_1_object_id is not UNSET:
            field_dict["FinancialPeriod1ObjectId"] = financial_period_1_object_id
        if financial_period_2_object_id is not UNSET:
            field_dict["FinancialPeriod2ObjectId"] = financial_period_2_object_id
        if financial_period_tmpl_id is not UNSET:
            field_dict["FinancialPeriodTmplId"] = financial_period_tmpl_id
        if is_baseline is not UNSET:
            field_dict["IsBaseline"] = is_baseline
        if is_template is not UNSET:
            field_dict["IsTemplate"] = is_template
        if last_update_date is not UNSET:
            field_dict["LastUpdateDate"] = last_update_date
        if last_update_user is not UNSET:
            field_dict["LastUpdateUser"] = last_update_user
        if month_start_date is not UNSET:
            field_dict["MonthStartDate"] = month_start_date
        if project_object_id is not UNSET:
            field_dict["ProjectObjectId"] = project_object_id
        if resource_object_id is not UNSET:
            field_dict["ResourceObjectId"] = resource_object_id
        if role_object_id is not UNSET:
            field_dict["RoleObjectId"] = role_object_id
        if wbs_object_id is not UNSET:
            field_dict["WBSObjectId"] = wbs_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        financial_period_1_quantity = d.pop("FinancialPeriod1Quantity")

        financial_period_2_quantity = d.pop("FinancialPeriod2Quantity")

        project_resource_object_id = d.pop("ProjectResourceObjectId")

        quantity = d.pop("Quantity")

        week_start_date = isoparse(d.pop("WeekStartDate"))

        committed_flag = d.pop("CommittedFlag", UNSET)

        _create_date = d.pop("CreateDate", UNSET)
        create_date: datetime.datetime | Unset
        if isinstance(_create_date, Unset):
            create_date = UNSET
        else:
            create_date = isoparse(_create_date)

        create_user = d.pop("CreateUser", UNSET)

        financial_period_1_object_id = d.pop("FinancialPeriod1ObjectId", UNSET)

        financial_period_2_object_id = d.pop("FinancialPeriod2ObjectId", UNSET)

        financial_period_tmpl_id = d.pop("FinancialPeriodTmplId", UNSET)

        is_baseline = d.pop("IsBaseline", UNSET)

        is_template = d.pop("IsTemplate", UNSET)

        _last_update_date = d.pop("LastUpdateDate", UNSET)
        last_update_date: datetime.datetime | Unset
        if isinstance(_last_update_date, Unset):
            last_update_date = UNSET
        else:
            last_update_date = isoparse(_last_update_date)

        last_update_user = d.pop("LastUpdateUser", UNSET)

        _month_start_date = d.pop("MonthStartDate", UNSET)
        month_start_date: datetime.datetime | Unset
        if isinstance(_month_start_date, Unset):
            month_start_date = UNSET
        else:
            month_start_date = isoparse(_month_start_date)

        project_object_id = d.pop("ProjectObjectId", UNSET)

        resource_object_id = d.pop("ResourceObjectId", UNSET)

        role_object_id = d.pop("RoleObjectId", UNSET)

        wbs_object_id = d.pop("WBSObjectId", UNSET)

        project_resource_quantity = cls(
            financial_period_1_quantity=financial_period_1_quantity,
            financial_period_2_quantity=financial_period_2_quantity,
            project_resource_object_id=project_resource_object_id,
            quantity=quantity,
            week_start_date=week_start_date,
            committed_flag=committed_flag,
            create_date=create_date,
            create_user=create_user,
            financial_period_1_object_id=financial_period_1_object_id,
            financial_period_2_object_id=financial_period_2_object_id,
            financial_period_tmpl_id=financial_period_tmpl_id,
            is_baseline=is_baseline,
            is_template=is_template,
            last_update_date=last_update_date,
            last_update_user=last_update_user,
            month_start_date=month_start_date,
            project_object_id=project_object_id,
            resource_object_id=resource_object_id,
            role_object_id=role_object_id,
            wbs_object_id=wbs_object_id,
        )

        project_resource_quantity.additional_properties = d
        return project_resource_quantity

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
