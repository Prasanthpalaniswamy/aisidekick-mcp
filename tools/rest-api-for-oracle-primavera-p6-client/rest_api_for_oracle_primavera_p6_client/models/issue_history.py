from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueHistory")


@_attrs_define
class IssueHistory:
    """IssueHistory Entity

    Attributes:
        create_date (datetime.datetime | Unset): The date this issue history was created.
        create_user (str | Unset): The name of the user that created this issue history.
        is_baseline (bool | Unset): The boolean value indicating if this business object is related to a Project or
            Baseline
        is_template (bool | Unset): The boolean value indicating if this business object is related to a template
            Project.
        last_update_date (datetime.datetime | Unset): The date this issue history was last updated.
        last_update_user (str | Unset): The name of the user that last updated this issue history.
        notes (str | Unset): The notes associated with the issue history.
        project_issue_object_id (int | Unset): The unique ID of the associated project issue for this issue history.
        project_object_id (int | Unset): The unique ID of the associated project for this issue history.
    """

    create_date: datetime.datetime | Unset = UNSET
    create_user: str | Unset = UNSET
    is_baseline: bool | Unset = UNSET
    is_template: bool | Unset = UNSET
    last_update_date: datetime.datetime | Unset = UNSET
    last_update_user: str | Unset = UNSET
    notes: str | Unset = UNSET
    project_issue_object_id: int | Unset = UNSET
    project_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        notes = self.notes

        project_issue_object_id = self.project_issue_object_id

        project_object_id = self.project_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if notes is not UNSET:
            field_dict["Notes"] = notes
        if project_issue_object_id is not UNSET:
            field_dict["ProjectIssueObjectId"] = project_issue_object_id
        if project_object_id is not UNSET:
            field_dict["ProjectObjectId"] = project_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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

        notes = d.pop("Notes", UNSET)

        project_issue_object_id = d.pop("ProjectIssueObjectId", UNSET)

        project_object_id = d.pop("ProjectObjectId", UNSET)

        issue_history = cls(
            create_date=create_date,
            create_user=create_user,
            is_baseline=is_baseline,
            is_template=is_template,
            last_update_date=last_update_date,
            last_update_user=last_update_user,
            notes=notes,
            project_issue_object_id=project_issue_object_id,
            project_object_id=project_object_id,
        )

        issue_history.additional_properties = d
        return issue_history

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
