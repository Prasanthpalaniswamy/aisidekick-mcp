from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CurrentJobResponse")


@_attrs_define
class CurrentJobResponse:
    """CurrentJobResponse Entity

    Attributes:
        job_id (str | Unset):
        job_type (str | Unset):
        job_status (str | Unset):
        submitted_date (str | Unset):
        last_run_date (str | Unset):
        project_object_id (list[str] | Unset):
        eps_object_id (list[str] | Unset):
        worker_host (str | Unset):
    """

    job_id: str | Unset = UNSET
    job_type: str | Unset = UNSET
    job_status: str | Unset = UNSET
    submitted_date: str | Unset = UNSET
    last_run_date: str | Unset = UNSET
    project_object_id: list[str] | Unset = UNSET
    eps_object_id: list[str] | Unset = UNSET
    worker_host: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        job_type = self.job_type

        job_status = self.job_status

        submitted_date = self.submitted_date

        last_run_date = self.last_run_date

        project_object_id: list[str] | Unset = UNSET
        if not isinstance(self.project_object_id, Unset):
            project_object_id = self.project_object_id

        eps_object_id: list[str] | Unset = UNSET
        if not isinstance(self.eps_object_id, Unset):
            eps_object_id = self.eps_object_id

        worker_host = self.worker_host

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["JobId"] = job_id
        if job_type is not UNSET:
            field_dict["JobType"] = job_type
        if job_status is not UNSET:
            field_dict["JobStatus"] = job_status
        if submitted_date is not UNSET:
            field_dict["SubmittedDate"] = submitted_date
        if last_run_date is not UNSET:
            field_dict["LastRunDate"] = last_run_date
        if project_object_id is not UNSET:
            field_dict["ProjectObjectId"] = project_object_id
        if eps_object_id is not UNSET:
            field_dict["EPSObjectId"] = eps_object_id
        if worker_host is not UNSET:
            field_dict["WorkerHost"] = worker_host

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("JobId", UNSET)

        job_type = d.pop("JobType", UNSET)

        job_status = d.pop("JobStatus", UNSET)

        submitted_date = d.pop("SubmittedDate", UNSET)

        last_run_date = d.pop("LastRunDate", UNSET)

        project_object_id = cast(list[str], d.pop("ProjectObjectId", UNSET))

        eps_object_id = cast(list[str], d.pop("EPSObjectId", UNSET))

        worker_host = d.pop("WorkerHost", UNSET)

        current_job_response = cls(
            job_id=job_id,
            job_type=job_type,
            job_status=job_status,
            submitted_date=submitted_date,
            last_run_date=last_run_date,
            project_object_id=project_object_id,
            eps_object_id=eps_object_id,
            worker_host=worker_host,
        )

        current_job_response.additional_properties = d
        return current_job_response

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
