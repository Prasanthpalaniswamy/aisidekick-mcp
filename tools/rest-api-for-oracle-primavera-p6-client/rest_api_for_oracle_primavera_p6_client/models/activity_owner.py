from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityOwner")


@_attrs_define
class ActivityOwner:
    """ActivityOwner Entity

    Attributes:
        activity_object_id (int): The unique ID of the associated activity.
        user_object_id (int): The unique ID of the associated user.
        create_date (datetime.datetime | Unset): The date this activity owner was created.
        create_user (str | Unset): The name of the user that created this activity owner.
        is_activity_flagged (bool | Unset): The flag that indicates whether the owner of the activity has flagged the
            activity as important.
        is_baseline (bool | Unset): The boolean value indicating if this business object is related to a Project or
            Baseline.
        is_template (bool | Unset): The boolean value indicating if this business object is related to a template
            Project.
        last_update_date (datetime.datetime | Unset): The date this activity owner was last updated.
        last_update_user (str | Unset): The name of the user that last updated this activity owner.
        project_flag (str | Unset): Indicates if this WBS node is a Project/EPS node.
        project_object_id (int | Unset): The unique ID of the associated project.
        project_project_flag (str | Unset): Indicates if this Project/EPS node is a Project or EPS.
        status_code (str | Unset): The project status, either 'Planned', 'Active', 'Inactive', 'What-If', 'Requested',
            or 'Template'.
    """

    activity_object_id: int
    user_object_id: int
    create_date: datetime.datetime | Unset = UNSET
    create_user: str | Unset = UNSET
    is_activity_flagged: bool | Unset = UNSET
    is_baseline: bool | Unset = UNSET
    is_template: bool | Unset = UNSET
    last_update_date: datetime.datetime | Unset = UNSET
    last_update_user: str | Unset = UNSET
    project_flag: str | Unset = UNSET
    project_object_id: int | Unset = UNSET
    project_project_flag: str | Unset = UNSET
    status_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_object_id = self.activity_object_id

        user_object_id = self.user_object_id

        create_date: str | Unset = UNSET
        if not isinstance(self.create_date, Unset):
            create_date = self.create_date.isoformat()

        create_user = self.create_user

        is_activity_flagged = self.is_activity_flagged

        is_baseline = self.is_baseline

        is_template = self.is_template

        last_update_date: str | Unset = UNSET
        if not isinstance(self.last_update_date, Unset):
            last_update_date = self.last_update_date.isoformat()

        last_update_user = self.last_update_user

        project_flag = self.project_flag

        project_object_id = self.project_object_id

        project_project_flag = self.project_project_flag

        status_code = self.status_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ActivityObjectId": activity_object_id,
                "UserObjectId": user_object_id,
            }
        )
        if create_date is not UNSET:
            field_dict["CreateDate"] = create_date
        if create_user is not UNSET:
            field_dict["CreateUser"] = create_user
        if is_activity_flagged is not UNSET:
            field_dict["IsActivityFlagged"] = is_activity_flagged
        if is_baseline is not UNSET:
            field_dict["IsBaseline"] = is_baseline
        if is_template is not UNSET:
            field_dict["IsTemplate"] = is_template
        if last_update_date is not UNSET:
            field_dict["LastUpdateDate"] = last_update_date
        if last_update_user is not UNSET:
            field_dict["LastUpdateUser"] = last_update_user
        if project_flag is not UNSET:
            field_dict["ProjectFlag"] = project_flag
        if project_object_id is not UNSET:
            field_dict["ProjectObjectId"] = project_object_id
        if project_project_flag is not UNSET:
            field_dict["ProjectProjectFlag"] = project_project_flag
        if status_code is not UNSET:
            field_dict["StatusCode"] = status_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        activity_object_id = d.pop("ActivityObjectId")

        user_object_id = d.pop("UserObjectId")

        _create_date = d.pop("CreateDate", UNSET)
        create_date: datetime.datetime | Unset
        if isinstance(_create_date, Unset):
            create_date = UNSET
        else:
            create_date = isoparse(_create_date)

        create_user = d.pop("CreateUser", UNSET)

        is_activity_flagged = d.pop("IsActivityFlagged", UNSET)

        is_baseline = d.pop("IsBaseline", UNSET)

        is_template = d.pop("IsTemplate", UNSET)

        _last_update_date = d.pop("LastUpdateDate", UNSET)
        last_update_date: datetime.datetime | Unset
        if isinstance(_last_update_date, Unset):
            last_update_date = UNSET
        else:
            last_update_date = isoparse(_last_update_date)

        last_update_user = d.pop("LastUpdateUser", UNSET)

        project_flag = d.pop("ProjectFlag", UNSET)

        project_object_id = d.pop("ProjectObjectId", UNSET)

        project_project_flag = d.pop("ProjectProjectFlag", UNSET)

        status_code = d.pop("StatusCode", UNSET)

        activity_owner = cls(
            activity_object_id=activity_object_id,
            user_object_id=user_object_id,
            create_date=create_date,
            create_user=create_user,
            is_activity_flagged=is_activity_flagged,
            is_baseline=is_baseline,
            is_template=is_template,
            last_update_date=last_update_date,
            last_update_user=last_update_user,
            project_flag=project_flag,
            project_object_id=project_object_id,
            project_project_flag=project_project_flag,
            status_code=status_code,
        )

        activity_owner.additional_properties = d
        return activity_owner

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
