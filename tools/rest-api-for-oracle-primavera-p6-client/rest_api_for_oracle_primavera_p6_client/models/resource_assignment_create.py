from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceAssignmentCreate")


@_attrs_define
class ResourceAssignmentCreate:
    """ResourceAssignmentCreate Entity

    Attributes:
        activity_object_id (int): The unique ID of the activity to which the associated assignment is assigned.
        resource_object_id (int): The unique identifier of the associated resource.
        actual_finish_date (datetime.datetime | Unset): The date the resource actually finished working on the activity.
        actual_start_date (datetime.datetime | Unset): The date the resource actually started working on the activity.
        actual_units (float | Unset): The actual units worked by the resource on this activity.
        assignment_is_read (str | Unset): To determine whether or not the newly created assignment from P6 Team Member
            Web is viewed by the manager in the Control Status Update.
        change_set_object_id (int | Unset): The unique ID of the associated Changeset.
        date (datetime.datetime | Unset): The date of the transaction.
        project_object_id (int | Unset): The unique identifier of the project that is associated with the
            ResourceAssignmentCreate object.
        remaining_duration (float | Unset): The remaining finish date for the resource working on the activity.
        remaining_finish_date (datetime.datetime | Unset): The remaining finish date for the resource working on the
            activity.
        remaining_units (float | Unset): The remaining units of work to be performed by this resource on this activity.
        request_user_object_id (int | Unset): The unique ID of the user modifying the task, assignment or step.
        resource_assignment_create_object_id (int | Unset): The unique identifier of the ResourceAssignment that is
            associated to the ResourceAssignmentCreate.
        resource_assignment_object_id (int | Unset): The unique identifier of the ResourceAssignment that is associated
            with ResourceAssignmentCreate object.
        status (str | Unset): The status of the resource assignment. [not sure about the filter orderable or read only]
    """

    activity_object_id: int
    resource_object_id: int
    actual_finish_date: datetime.datetime | Unset = UNSET
    actual_start_date: datetime.datetime | Unset = UNSET
    actual_units: float | Unset = UNSET
    assignment_is_read: str | Unset = UNSET
    change_set_object_id: int | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    project_object_id: int | Unset = UNSET
    remaining_duration: float | Unset = UNSET
    remaining_finish_date: datetime.datetime | Unset = UNSET
    remaining_units: float | Unset = UNSET
    request_user_object_id: int | Unset = UNSET
    resource_assignment_create_object_id: int | Unset = UNSET
    resource_assignment_object_id: int | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_object_id = self.activity_object_id

        resource_object_id = self.resource_object_id

        actual_finish_date: str | Unset = UNSET
        if not isinstance(self.actual_finish_date, Unset):
            actual_finish_date = self.actual_finish_date.isoformat()

        actual_start_date: str | Unset = UNSET
        if not isinstance(self.actual_start_date, Unset):
            actual_start_date = self.actual_start_date.isoformat()

        actual_units = self.actual_units

        assignment_is_read = self.assignment_is_read

        change_set_object_id = self.change_set_object_id

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        project_object_id = self.project_object_id

        remaining_duration = self.remaining_duration

        remaining_finish_date: str | Unset = UNSET
        if not isinstance(self.remaining_finish_date, Unset):
            remaining_finish_date = self.remaining_finish_date.isoformat()

        remaining_units = self.remaining_units

        request_user_object_id = self.request_user_object_id

        resource_assignment_create_object_id = self.resource_assignment_create_object_id

        resource_assignment_object_id = self.resource_assignment_object_id

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ActivityObjectId": activity_object_id,
                "ResourceObjectId": resource_object_id,
            }
        )
        if actual_finish_date is not UNSET:
            field_dict["ActualFinishDate"] = actual_finish_date
        if actual_start_date is not UNSET:
            field_dict["ActualStartDate"] = actual_start_date
        if actual_units is not UNSET:
            field_dict["ActualUnits"] = actual_units
        if assignment_is_read is not UNSET:
            field_dict["AssignmentIsRead"] = assignment_is_read
        if change_set_object_id is not UNSET:
            field_dict["ChangeSetObjectId"] = change_set_object_id
        if date is not UNSET:
            field_dict["Date"] = date
        if project_object_id is not UNSET:
            field_dict["ProjectObjectId"] = project_object_id
        if remaining_duration is not UNSET:
            field_dict["RemainingDuration"] = remaining_duration
        if remaining_finish_date is not UNSET:
            field_dict["RemainingFinishDate"] = remaining_finish_date
        if remaining_units is not UNSET:
            field_dict["RemainingUnits"] = remaining_units
        if request_user_object_id is not UNSET:
            field_dict["RequestUserObjectId"] = request_user_object_id
        if resource_assignment_create_object_id is not UNSET:
            field_dict["ResourceAssignmentCreateObjectId"] = resource_assignment_create_object_id
        if resource_assignment_object_id is not UNSET:
            field_dict["ResourceAssignmentObjectId"] = resource_assignment_object_id
        if status is not UNSET:
            field_dict["Status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        activity_object_id = d.pop("ActivityObjectId")

        resource_object_id = d.pop("ResourceObjectId")

        _actual_finish_date = d.pop("ActualFinishDate", UNSET)
        actual_finish_date: datetime.datetime | Unset
        if isinstance(_actual_finish_date, Unset):
            actual_finish_date = UNSET
        else:
            actual_finish_date = isoparse(_actual_finish_date)

        _actual_start_date = d.pop("ActualStartDate", UNSET)
        actual_start_date: datetime.datetime | Unset
        if isinstance(_actual_start_date, Unset):
            actual_start_date = UNSET
        else:
            actual_start_date = isoparse(_actual_start_date)

        actual_units = d.pop("ActualUnits", UNSET)

        assignment_is_read = d.pop("AssignmentIsRead", UNSET)

        change_set_object_id = d.pop("ChangeSetObjectId", UNSET)

        _date = d.pop("Date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        project_object_id = d.pop("ProjectObjectId", UNSET)

        remaining_duration = d.pop("RemainingDuration", UNSET)

        _remaining_finish_date = d.pop("RemainingFinishDate", UNSET)
        remaining_finish_date: datetime.datetime | Unset
        if isinstance(_remaining_finish_date, Unset):
            remaining_finish_date = UNSET
        else:
            remaining_finish_date = isoparse(_remaining_finish_date)

        remaining_units = d.pop("RemainingUnits", UNSET)

        request_user_object_id = d.pop("RequestUserObjectId", UNSET)

        resource_assignment_create_object_id = d.pop("ResourceAssignmentCreateObjectId", UNSET)

        resource_assignment_object_id = d.pop("ResourceAssignmentObjectId", UNSET)

        status = d.pop("Status", UNSET)

        resource_assignment_create = cls(
            activity_object_id=activity_object_id,
            resource_object_id=resource_object_id,
            actual_finish_date=actual_finish_date,
            actual_start_date=actual_start_date,
            actual_units=actual_units,
            assignment_is_read=assignment_is_read,
            change_set_object_id=change_set_object_id,
            date=date,
            project_object_id=project_object_id,
            remaining_duration=remaining_duration,
            remaining_finish_date=remaining_finish_date,
            remaining_units=remaining_units,
            request_user_object_id=request_user_object_id,
            resource_assignment_create_object_id=resource_assignment_create_object_id,
            resource_assignment_object_id=resource_assignment_object_id,
            status=status,
        )

        resource_assignment_create.additional_properties = d
        return resource_assignment_create

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
