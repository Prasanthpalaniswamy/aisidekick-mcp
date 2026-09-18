from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LeanTask")


@_attrs_define
class LeanTask:
    """LeanTask Entity

    Attributes:
        activity_id (str | Unset): The short ID that uniquely identifies the activity to which the lean task is
            assigned.
        activity_name (str | Unset): The name of the activity to which the lean task is assigned.
        activity_object_id (int | Unset): The unique ID of the activity to which the lean task is assigned.
        company (str | Unset): The company associated with the lean task in Oracle Primavera Cloud.
        completed_date (datetime.datetime | Unset): The date the lean task was completed.
        create_date (datetime.datetime | Unset): The date the lean task was created.
        create_user (str | Unset): The name of the user that created this lean task.
        due_date (datetime.datetime | Unset): The date the lean task is due.
        duration (float | Unset): Number of days required for task to complete.
        flag (bool | Unset): The indication of whether the lean task is considered high importance.
        is_baseline (bool | Unset): Determines whether the object is associated with a baseline (true) or a project
            (false).
        is_overdue (bool | Unset): Shows whether the due date for the lean task is earlier than the current date.
        is_template (bool | Unset): Determines whether the object is associated with a template project in Oracle
            Primavera Cloud.
        is_use_only_work_days (bool | Unset): Determines whether the object is set to use only working days in Oracle
            Primavera Cloud.
        last_update_date (datetime.datetime | Unset): The date the lean task was last updated.
        last_update_user (str | Unset): The name of the user that last updated this lean task.
        lean_task_id (str | Unset): The short ID that uniquely identifies the lean task.
        name (str | Unset): The name of the lean task in Oracle Primavera Cloud.
        object_id (int | Unset): The primary key of the lean task in the P6 EPPM database.
        project_id (str | Unset): The short ID that uniquely identifies the project to which the lean task is assigned.
        project_object_id (int | Unset): The unique ID of the project to which the lean task is assigned.
        proposed_due_date (datetime.datetime | Unset): The proposed due date of the lean task in Oracle Primavera Cloud.
        sequence_number (int | Unset): Denotes the creation order of lean tasks relative to each other.
        start_date (datetime.datetime | Unset): The date the lean task was started or is due to start.
        status (str | Unset): The status of the lean task in Oracle Primavera Cloud.
        status_completion (str | Unset): The completion status of the lean task in Oracle Primavera Cloud.
        status_dates (str | Unset): A comparison of the dates of the lean task and the activity to which it is assigned.
        task_type (str | Unset): The type of the lean task in Oracle Primavera Cloud.
        wbs_object_id (int | Unset): The unique ID of the WBS to which the lean task is assigned.
    """

    activity_id: str | Unset = UNSET
    activity_name: str | Unset = UNSET
    activity_object_id: int | Unset = UNSET
    company: str | Unset = UNSET
    completed_date: datetime.datetime | Unset = UNSET
    create_date: datetime.datetime | Unset = UNSET
    create_user: str | Unset = UNSET
    due_date: datetime.datetime | Unset = UNSET
    duration: float | Unset = UNSET
    flag: bool | Unset = UNSET
    is_baseline: bool | Unset = UNSET
    is_overdue: bool | Unset = UNSET
    is_template: bool | Unset = UNSET
    is_use_only_work_days: bool | Unset = UNSET
    last_update_date: datetime.datetime | Unset = UNSET
    last_update_user: str | Unset = UNSET
    lean_task_id: str | Unset = UNSET
    name: str | Unset = UNSET
    object_id: int | Unset = UNSET
    project_id: str | Unset = UNSET
    project_object_id: int | Unset = UNSET
    proposed_due_date: datetime.datetime | Unset = UNSET
    sequence_number: int | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    status: str | Unset = UNSET
    status_completion: str | Unset = UNSET
    status_dates: str | Unset = UNSET
    task_type: str | Unset = UNSET
    wbs_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_id = self.activity_id

        activity_name = self.activity_name

        activity_object_id = self.activity_object_id

        company = self.company

        completed_date: str | Unset = UNSET
        if not isinstance(self.completed_date, Unset):
            completed_date = self.completed_date.isoformat()

        create_date: str | Unset = UNSET
        if not isinstance(self.create_date, Unset):
            create_date = self.create_date.isoformat()

        create_user = self.create_user

        due_date: str | Unset = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        duration = self.duration

        flag = self.flag

        is_baseline = self.is_baseline

        is_overdue = self.is_overdue

        is_template = self.is_template

        is_use_only_work_days = self.is_use_only_work_days

        last_update_date: str | Unset = UNSET
        if not isinstance(self.last_update_date, Unset):
            last_update_date = self.last_update_date.isoformat()

        last_update_user = self.last_update_user

        lean_task_id = self.lean_task_id

        name = self.name

        object_id = self.object_id

        project_id = self.project_id

        project_object_id = self.project_object_id

        proposed_due_date: str | Unset = UNSET
        if not isinstance(self.proposed_due_date, Unset):
            proposed_due_date = self.proposed_due_date.isoformat()

        sequence_number = self.sequence_number

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        status = self.status

        status_completion = self.status_completion

        status_dates = self.status_dates

        task_type = self.task_type

        wbs_object_id = self.wbs_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity_id is not UNSET:
            field_dict["ActivityId"] = activity_id
        if activity_name is not UNSET:
            field_dict["ActivityName"] = activity_name
        if activity_object_id is not UNSET:
            field_dict["ActivityObjectId"] = activity_object_id
        if company is not UNSET:
            field_dict["Company"] = company
        if completed_date is not UNSET:
            field_dict["CompletedDate"] = completed_date
        if create_date is not UNSET:
            field_dict["CreateDate"] = create_date
        if create_user is not UNSET:
            field_dict["CreateUser"] = create_user
        if due_date is not UNSET:
            field_dict["DueDate"] = due_date
        if duration is not UNSET:
            field_dict["Duration"] = duration
        if flag is not UNSET:
            field_dict["Flag"] = flag
        if is_baseline is not UNSET:
            field_dict["IsBaseline"] = is_baseline
        if is_overdue is not UNSET:
            field_dict["IsOverdue"] = is_overdue
        if is_template is not UNSET:
            field_dict["IsTemplate"] = is_template
        if is_use_only_work_days is not UNSET:
            field_dict["IsUseOnlyWorkDays"] = is_use_only_work_days
        if last_update_date is not UNSET:
            field_dict["LastUpdateDate"] = last_update_date
        if last_update_user is not UNSET:
            field_dict["LastUpdateUser"] = last_update_user
        if lean_task_id is not UNSET:
            field_dict["LeanTaskId"] = lean_task_id
        if name is not UNSET:
            field_dict["Name"] = name
        if object_id is not UNSET:
            field_dict["ObjectId"] = object_id
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if project_object_id is not UNSET:
            field_dict["ProjectObjectId"] = project_object_id
        if proposed_due_date is not UNSET:
            field_dict["ProposedDueDate"] = proposed_due_date
        if sequence_number is not UNSET:
            field_dict["SequenceNumber"] = sequence_number
        if start_date is not UNSET:
            field_dict["StartDate"] = start_date
        if status is not UNSET:
            field_dict["Status"] = status
        if status_completion is not UNSET:
            field_dict["StatusCompletion"] = status_completion
        if status_dates is not UNSET:
            field_dict["StatusDates"] = status_dates
        if task_type is not UNSET:
            field_dict["TaskType"] = task_type
        if wbs_object_id is not UNSET:
            field_dict["WBSObjectId"] = wbs_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        activity_id = d.pop("ActivityId", UNSET)

        activity_name = d.pop("ActivityName", UNSET)

        activity_object_id = d.pop("ActivityObjectId", UNSET)

        company = d.pop("Company", UNSET)

        _completed_date = d.pop("CompletedDate", UNSET)
        completed_date: datetime.datetime | Unset
        if isinstance(_completed_date, Unset):
            completed_date = UNSET
        else:
            completed_date = isoparse(_completed_date)

        _create_date = d.pop("CreateDate", UNSET)
        create_date: datetime.datetime | Unset
        if isinstance(_create_date, Unset):
            create_date = UNSET
        else:
            create_date = isoparse(_create_date)

        create_user = d.pop("CreateUser", UNSET)

        _due_date = d.pop("DueDate", UNSET)
        due_date: datetime.datetime | Unset
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        duration = d.pop("Duration", UNSET)

        flag = d.pop("Flag", UNSET)

        is_baseline = d.pop("IsBaseline", UNSET)

        is_overdue = d.pop("IsOverdue", UNSET)

        is_template = d.pop("IsTemplate", UNSET)

        is_use_only_work_days = d.pop("IsUseOnlyWorkDays", UNSET)

        _last_update_date = d.pop("LastUpdateDate", UNSET)
        last_update_date: datetime.datetime | Unset
        if isinstance(_last_update_date, Unset):
            last_update_date = UNSET
        else:
            last_update_date = isoparse(_last_update_date)

        last_update_user = d.pop("LastUpdateUser", UNSET)

        lean_task_id = d.pop("LeanTaskId", UNSET)

        name = d.pop("Name", UNSET)

        object_id = d.pop("ObjectId", UNSET)

        project_id = d.pop("ProjectId", UNSET)

        project_object_id = d.pop("ProjectObjectId", UNSET)

        _proposed_due_date = d.pop("ProposedDueDate", UNSET)
        proposed_due_date: datetime.datetime | Unset
        if isinstance(_proposed_due_date, Unset):
            proposed_due_date = UNSET
        else:
            proposed_due_date = isoparse(_proposed_due_date)

        sequence_number = d.pop("SequenceNumber", UNSET)

        _start_date = d.pop("StartDate", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        status = d.pop("Status", UNSET)

        status_completion = d.pop("StatusCompletion", UNSET)

        status_dates = d.pop("StatusDates", UNSET)

        task_type = d.pop("TaskType", UNSET)

        wbs_object_id = d.pop("WBSObjectId", UNSET)

        lean_task = cls(
            activity_id=activity_id,
            activity_name=activity_name,
            activity_object_id=activity_object_id,
            company=company,
            completed_date=completed_date,
            create_date=create_date,
            create_user=create_user,
            due_date=due_date,
            duration=duration,
            flag=flag,
            is_baseline=is_baseline,
            is_overdue=is_overdue,
            is_template=is_template,
            is_use_only_work_days=is_use_only_work_days,
            last_update_date=last_update_date,
            last_update_user=last_update_user,
            lean_task_id=lean_task_id,
            name=name,
            object_id=object_id,
            project_id=project_id,
            project_object_id=project_object_id,
            proposed_due_date=proposed_due_date,
            sequence_number=sequence_number,
            start_date=start_date,
            status=status,
            status_completion=status_completion,
            status_dates=status_dates,
            task_type=task_type,
            wbs_object_id=wbs_object_id,
        )

        lean_task.additional_properties = d
        return lean_task

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
