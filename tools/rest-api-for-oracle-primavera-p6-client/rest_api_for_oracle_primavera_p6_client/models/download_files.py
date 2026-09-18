from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DownloadFiles")


@_attrs_define
class DownloadFiles:
    """DownloadFiles Entity

    Attributes:
        job_type (str | Unset): Specifies the job type.
        job_name (list[str] | Unset): Specifies the job name.
        start_date (datetime.datetime | Unset): The start date of the file download.
        end_date (datetime.datetime | Unset): The end date of the file download.
    """

    job_type: str | Unset = UNSET
    job_name: list[str] | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    end_date: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_type = self.job_type

        job_name: list[str] | Unset = UNSET
        if not isinstance(self.job_name, Unset):
            job_name = self.job_name

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_type is not UNSET:
            field_dict["JobType"] = job_type
        if job_name is not UNSET:
            field_dict["JobName"] = job_name
        if start_date is not UNSET:
            field_dict["StartDate"] = start_date
        if end_date is not UNSET:
            field_dict["EndDate"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_type = d.pop("JobType", UNSET)

        job_name = cast(list[str], d.pop("JobName", UNSET))

        _start_date = d.pop("StartDate", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("EndDate", UNSET)
        end_date: datetime.datetime | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        download_files = cls(
            job_type=job_type,
            job_name=job_name,
            start_date=start_date,
            end_date=end_date,
        )

        download_files.additional_properties = d
        return download_files

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
