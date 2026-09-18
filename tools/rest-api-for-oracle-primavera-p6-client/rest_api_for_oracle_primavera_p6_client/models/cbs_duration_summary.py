from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CBSDurationSummary")


@_attrs_define
class CBSDurationSummary:
    """CBSDurationSummary Entity

    Attributes:
        cbs_object_id (int): The internal CBS ID of the project. This ID cannot be used to load the CBS object directly.
        project_id (str): The short code of the associated project.
        original_project_object_id (int | Unset): The unique ID of the project from which the project baseline was
            created, if the current project is a project baseline
        project_name (str | Unset): The name of the associated project.
        project_object_id (int | Unset): The unique ID of the associated project.
        summary_actual_duration (float | Unset): The actual duration.
        summary_actual_finish_date (datetime.datetime | Unset): The latest actual finish date of all activities in the
            CBS.
        summary_actual_start_date (datetime.datetime | Unset): The earliest actual start date of all activities in the
            CBS.
        summary_percent_complete (float | Unset): The measure that indicates how much of the CBS baseline duration has
            been completed so far. Computed based on where the current data date falls between the activity's baseline start
            and finish dates. If the data date is earlier than the baseline start, the schedule % complete is 0. If the data
            date is later than the baseline finish, the schedule % complete is 100. The schedule % complete indicates how
            much of the CBS duration should be currently completed, relative to the selected baseline.
        summary_planned_duration (float | Unset): The total working days between planned start and finish dates in the
            CBS.
        summary_planned_finish_date (datetime.datetime | Unset): The latest planned finish date of all activities in the
            CBS.
        summary_planned_start_date (datetime.datetime | Unset): The earliest planned start date of all activities in the
            CBS.
        summary_remaining_duration (float | Unset): The total working time from the CBS remaining start date to the
            remaining finish date.
        summary_remaining_finish_date (datetime.datetime | Unset): The date the resource is scheduled to finish the
            remaining work for the activity.
        summary_remaining_start_date (datetime.datetime | Unset): The earliest remaining start of all activities
            assigned to the CBS.
    """

    cbs_object_id: int
    project_id: str
    original_project_object_id: int | Unset = UNSET
    project_name: str | Unset = UNSET
    project_object_id: int | Unset = UNSET
    summary_actual_duration: float | Unset = UNSET
    summary_actual_finish_date: datetime.datetime | Unset = UNSET
    summary_actual_start_date: datetime.datetime | Unset = UNSET
    summary_percent_complete: float | Unset = UNSET
    summary_planned_duration: float | Unset = UNSET
    summary_planned_finish_date: datetime.datetime | Unset = UNSET
    summary_planned_start_date: datetime.datetime | Unset = UNSET
    summary_remaining_duration: float | Unset = UNSET
    summary_remaining_finish_date: datetime.datetime | Unset = UNSET
    summary_remaining_start_date: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cbs_object_id = self.cbs_object_id

        project_id = self.project_id

        original_project_object_id = self.original_project_object_id

        project_name = self.project_name

        project_object_id = self.project_object_id

        summary_actual_duration = self.summary_actual_duration

        summary_actual_finish_date: str | Unset = UNSET
        if not isinstance(self.summary_actual_finish_date, Unset):
            summary_actual_finish_date = self.summary_actual_finish_date.isoformat()

        summary_actual_start_date: str | Unset = UNSET
        if not isinstance(self.summary_actual_start_date, Unset):
            summary_actual_start_date = self.summary_actual_start_date.isoformat()

        summary_percent_complete = self.summary_percent_complete

        summary_planned_duration = self.summary_planned_duration

        summary_planned_finish_date: str | Unset = UNSET
        if not isinstance(self.summary_planned_finish_date, Unset):
            summary_planned_finish_date = self.summary_planned_finish_date.isoformat()

        summary_planned_start_date: str | Unset = UNSET
        if not isinstance(self.summary_planned_start_date, Unset):
            summary_planned_start_date = self.summary_planned_start_date.isoformat()

        summary_remaining_duration = self.summary_remaining_duration

        summary_remaining_finish_date: str | Unset = UNSET
        if not isinstance(self.summary_remaining_finish_date, Unset):
            summary_remaining_finish_date = self.summary_remaining_finish_date.isoformat()

        summary_remaining_start_date: str | Unset = UNSET
        if not isinstance(self.summary_remaining_start_date, Unset):
            summary_remaining_start_date = self.summary_remaining_start_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CBSObjectId": cbs_object_id,
                "ProjectId": project_id,
            }
        )
        if original_project_object_id is not UNSET:
            field_dict["OriginalProjectObjectId"] = original_project_object_id
        if project_name is not UNSET:
            field_dict["ProjectName"] = project_name
        if project_object_id is not UNSET:
            field_dict["ProjectObjectId"] = project_object_id
        if summary_actual_duration is not UNSET:
            field_dict["SummaryActualDuration"] = summary_actual_duration
        if summary_actual_finish_date is not UNSET:
            field_dict["SummaryActualFinishDate"] = summary_actual_finish_date
        if summary_actual_start_date is not UNSET:
            field_dict["SummaryActualStartDate"] = summary_actual_start_date
        if summary_percent_complete is not UNSET:
            field_dict["SummaryPercentComplete"] = summary_percent_complete
        if summary_planned_duration is not UNSET:
            field_dict["SummaryPlannedDuration"] = summary_planned_duration
        if summary_planned_finish_date is not UNSET:
            field_dict["SummaryPlannedFinishDate"] = summary_planned_finish_date
        if summary_planned_start_date is not UNSET:
            field_dict["SummaryPlannedStartDate"] = summary_planned_start_date
        if summary_remaining_duration is not UNSET:
            field_dict["SummaryRemainingDuration"] = summary_remaining_duration
        if summary_remaining_finish_date is not UNSET:
            field_dict["SummaryRemainingFinishDate"] = summary_remaining_finish_date
        if summary_remaining_start_date is not UNSET:
            field_dict["SummaryRemainingStartDate"] = summary_remaining_start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cbs_object_id = d.pop("CBSObjectId")

        project_id = d.pop("ProjectId")

        original_project_object_id = d.pop("OriginalProjectObjectId", UNSET)

        project_name = d.pop("ProjectName", UNSET)

        project_object_id = d.pop("ProjectObjectId", UNSET)

        summary_actual_duration = d.pop("SummaryActualDuration", UNSET)

        _summary_actual_finish_date = d.pop("SummaryActualFinishDate", UNSET)
        summary_actual_finish_date: datetime.datetime | Unset
        if isinstance(_summary_actual_finish_date, Unset):
            summary_actual_finish_date = UNSET
        else:
            summary_actual_finish_date = isoparse(_summary_actual_finish_date)

        _summary_actual_start_date = d.pop("SummaryActualStartDate", UNSET)
        summary_actual_start_date: datetime.datetime | Unset
        if isinstance(_summary_actual_start_date, Unset):
            summary_actual_start_date = UNSET
        else:
            summary_actual_start_date = isoparse(_summary_actual_start_date)

        summary_percent_complete = d.pop("SummaryPercentComplete", UNSET)

        summary_planned_duration = d.pop("SummaryPlannedDuration", UNSET)

        _summary_planned_finish_date = d.pop("SummaryPlannedFinishDate", UNSET)
        summary_planned_finish_date: datetime.datetime | Unset
        if isinstance(_summary_planned_finish_date, Unset):
            summary_planned_finish_date = UNSET
        else:
            summary_planned_finish_date = isoparse(_summary_planned_finish_date)

        _summary_planned_start_date = d.pop("SummaryPlannedStartDate", UNSET)
        summary_planned_start_date: datetime.datetime | Unset
        if isinstance(_summary_planned_start_date, Unset):
            summary_planned_start_date = UNSET
        else:
            summary_planned_start_date = isoparse(_summary_planned_start_date)

        summary_remaining_duration = d.pop("SummaryRemainingDuration", UNSET)

        _summary_remaining_finish_date = d.pop("SummaryRemainingFinishDate", UNSET)
        summary_remaining_finish_date: datetime.datetime | Unset
        if isinstance(_summary_remaining_finish_date, Unset):
            summary_remaining_finish_date = UNSET
        else:
            summary_remaining_finish_date = isoparse(_summary_remaining_finish_date)

        _summary_remaining_start_date = d.pop("SummaryRemainingStartDate", UNSET)
        summary_remaining_start_date: datetime.datetime | Unset
        if isinstance(_summary_remaining_start_date, Unset):
            summary_remaining_start_date = UNSET
        else:
            summary_remaining_start_date = isoparse(_summary_remaining_start_date)

        cbs_duration_summary = cls(
            cbs_object_id=cbs_object_id,
            project_id=project_id,
            original_project_object_id=original_project_object_id,
            project_name=project_name,
            project_object_id=project_object_id,
            summary_actual_duration=summary_actual_duration,
            summary_actual_finish_date=summary_actual_finish_date,
            summary_actual_start_date=summary_actual_start_date,
            summary_percent_complete=summary_percent_complete,
            summary_planned_duration=summary_planned_duration,
            summary_planned_finish_date=summary_planned_finish_date,
            summary_planned_start_date=summary_planned_start_date,
            summary_remaining_duration=summary_remaining_duration,
            summary_remaining_finish_date=summary_remaining_finish_date,
            summary_remaining_start_date=summary_remaining_start_date,
        )

        cbs_duration_summary.additional_properties = d
        return cbs_duration_summary

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
