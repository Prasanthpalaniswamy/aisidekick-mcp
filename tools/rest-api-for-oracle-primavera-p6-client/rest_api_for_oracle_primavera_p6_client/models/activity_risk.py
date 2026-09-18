from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityRisk")


@_attrs_define
class ActivityRisk:
    """ActivityRisk Entity

    Attributes:
        activity_object_id (int): The unique ID of the activity to which the risk is assigned.
        risk_object_id (int): The unique ID of the associated risk.
        activity_id (str | Unset): The id of an activity impacted by the Risk.
        activity_name (str | Unset): The name of an activity impacted by the Risk. The activity name does not have to be
            unique.
        create_date (datetime.datetime | Unset): The date this activity was created.
        create_user (str | Unset): The name of the user that created this activity risk.
        is_baseline (bool | Unset): The boolean value indicating if this business object is related to a Project or
            Baseline
        is_template (bool | Unset): The boolean value indicating if this business object is related to a template
            Project.
        last_update_date (datetime.datetime | Unset): The date this activity was last updated.
        last_update_user (str | Unset): The name of the user that last updated this activity risk.
        project_id (str | Unset): The short code of the associated project.
        project_name (str | Unset): The name of the associated project.
        project_object_id (int | Unset): The unique ID of the associated project.
        risk_id (str | Unset): The ID of the Risk. Must be unique within a project.
        risk_name (str | Unset): The name of the Risk. Does not need to be unique.
    """

    activity_object_id: int
    risk_object_id: int
    activity_id: str | Unset = UNSET
    activity_name: str | Unset = UNSET
    create_date: datetime.datetime | Unset = UNSET
    create_user: str | Unset = UNSET
    is_baseline: bool | Unset = UNSET
    is_template: bool | Unset = UNSET
    last_update_date: datetime.datetime | Unset = UNSET
    last_update_user: str | Unset = UNSET
    project_id: str | Unset = UNSET
    project_name: str | Unset = UNSET
    project_object_id: int | Unset = UNSET
    risk_id: str | Unset = UNSET
    risk_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_object_id = self.activity_object_id

        risk_object_id = self.risk_object_id

        activity_id = self.activity_id

        activity_name = self.activity_name

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

        project_id = self.project_id

        project_name = self.project_name

        project_object_id = self.project_object_id

        risk_id = self.risk_id

        risk_name = self.risk_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ActivityObjectId": activity_object_id,
                "RiskObjectId": risk_object_id,
            }
        )
        if activity_id is not UNSET:
            field_dict["ActivityId"] = activity_id
        if activity_name is not UNSET:
            field_dict["ActivityName"] = activity_name
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
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if project_name is not UNSET:
            field_dict["ProjectName"] = project_name
        if project_object_id is not UNSET:
            field_dict["ProjectObjectId"] = project_object_id
        if risk_id is not UNSET:
            field_dict["RiskId"] = risk_id
        if risk_name is not UNSET:
            field_dict["RiskName"] = risk_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        activity_object_id = d.pop("ActivityObjectId")

        risk_object_id = d.pop("RiskObjectId")

        activity_id = d.pop("ActivityId", UNSET)

        activity_name = d.pop("ActivityName", UNSET)

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

        project_id = d.pop("ProjectId", UNSET)

        project_name = d.pop("ProjectName", UNSET)

        project_object_id = d.pop("ProjectObjectId", UNSET)

        risk_id = d.pop("RiskId", UNSET)

        risk_name = d.pop("RiskName", UNSET)

        activity_risk = cls(
            activity_object_id=activity_object_id,
            risk_object_id=risk_object_id,
            activity_id=activity_id,
            activity_name=activity_name,
            create_date=create_date,
            create_user=create_user,
            is_baseline=is_baseline,
            is_template=is_template,
            last_update_date=last_update_date,
            last_update_user=last_update_user,
            project_id=project_id,
            project_name=project_name,
            project_object_id=project_object_id,
            risk_id=risk_id,
            risk_name=risk_name,
        )

        activity_risk.additional_properties = d
        return activity_risk

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
