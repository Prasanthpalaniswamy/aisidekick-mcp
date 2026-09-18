from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Timesheet")


@_attrs_define
class Timesheet:
    """Timesheet Entity

    Attributes:
        resource_object_id (int): The unique ID of the associated resource.
        timesheet_period_object_id (int): The unique ID of the timesheet period.
        create_date (datetime.datetime | Unset): The date this timesheet was created.
        create_user (str | Unset): The name of the user that created this timesheet.
        is_daily (bool | Unset): The flag that identifies whether timesheet users enter hours daily or by entire
            timesheet reporting period.
        last_received_date (datetime.datetime | Unset): The last date on which the timesheet was submitted by the
            resource.
        last_update_date (datetime.datetime | Unset): The date this timesheet was last updated.
        last_update_user (str | Unset): The name of the user that last updated this timesheet.
        notes (str | Unset): The notes associated with the timesheet.
        resource_id (str | Unset): The short code that uniquely identifies the resource.
        resource_name (str | Unset): The name of the resource.
        status (str | Unset): The current status of the timesheet: 'Submitted', 'Approved', 'Resource Manager Approved',
            'Project Manager Approved', 'Active', or 'Rejected'.
        status_date (datetime.datetime | Unset): The date on which the status of the timesheet was last changed.
    """

    resource_object_id: int
    timesheet_period_object_id: int
    create_date: datetime.datetime | Unset = UNSET
    create_user: str | Unset = UNSET
    is_daily: bool | Unset = UNSET
    last_received_date: datetime.datetime | Unset = UNSET
    last_update_date: datetime.datetime | Unset = UNSET
    last_update_user: str | Unset = UNSET
    notes: str | Unset = UNSET
    resource_id: str | Unset = UNSET
    resource_name: str | Unset = UNSET
    status: str | Unset = UNSET
    status_date: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_object_id = self.resource_object_id

        timesheet_period_object_id = self.timesheet_period_object_id

        create_date: str | Unset = UNSET
        if not isinstance(self.create_date, Unset):
            create_date = self.create_date.isoformat()

        create_user = self.create_user

        is_daily = self.is_daily

        last_received_date: str | Unset = UNSET
        if not isinstance(self.last_received_date, Unset):
            last_received_date = self.last_received_date.isoformat()

        last_update_date: str | Unset = UNSET
        if not isinstance(self.last_update_date, Unset):
            last_update_date = self.last_update_date.isoformat()

        last_update_user = self.last_update_user

        notes = self.notes

        resource_id = self.resource_id

        resource_name = self.resource_name

        status = self.status

        status_date: str | Unset = UNSET
        if not isinstance(self.status_date, Unset):
            status_date = self.status_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ResourceObjectId": resource_object_id,
                "TimesheetPeriodObjectId": timesheet_period_object_id,
            }
        )
        if create_date is not UNSET:
            field_dict["CreateDate"] = create_date
        if create_user is not UNSET:
            field_dict["CreateUser"] = create_user
        if is_daily is not UNSET:
            field_dict["IsDaily"] = is_daily
        if last_received_date is not UNSET:
            field_dict["LastReceivedDate"] = last_received_date
        if last_update_date is not UNSET:
            field_dict["LastUpdateDate"] = last_update_date
        if last_update_user is not UNSET:
            field_dict["LastUpdateUser"] = last_update_user
        if notes is not UNSET:
            field_dict["Notes"] = notes
        if resource_id is not UNSET:
            field_dict["ResourceId"] = resource_id
        if resource_name is not UNSET:
            field_dict["ResourceName"] = resource_name
        if status is not UNSET:
            field_dict["Status"] = status
        if status_date is not UNSET:
            field_dict["StatusDate"] = status_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_object_id = d.pop("ResourceObjectId")

        timesheet_period_object_id = d.pop("TimesheetPeriodObjectId")

        _create_date = d.pop("CreateDate", UNSET)
        create_date: datetime.datetime | Unset
        if isinstance(_create_date, Unset):
            create_date = UNSET
        else:
            create_date = isoparse(_create_date)

        create_user = d.pop("CreateUser", UNSET)

        is_daily = d.pop("IsDaily", UNSET)

        _last_received_date = d.pop("LastReceivedDate", UNSET)
        last_received_date: datetime.datetime | Unset
        if isinstance(_last_received_date, Unset):
            last_received_date = UNSET
        else:
            last_received_date = isoparse(_last_received_date)

        _last_update_date = d.pop("LastUpdateDate", UNSET)
        last_update_date: datetime.datetime | Unset
        if isinstance(_last_update_date, Unset):
            last_update_date = UNSET
        else:
            last_update_date = isoparse(_last_update_date)

        last_update_user = d.pop("LastUpdateUser", UNSET)

        notes = d.pop("Notes", UNSET)

        resource_id = d.pop("ResourceId", UNSET)

        resource_name = d.pop("ResourceName", UNSET)

        status = d.pop("Status", UNSET)

        _status_date = d.pop("StatusDate", UNSET)
        status_date: datetime.datetime | Unset
        if isinstance(_status_date, Unset):
            status_date = UNSET
        else:
            status_date = isoparse(_status_date)

        timesheet = cls(
            resource_object_id=resource_object_id,
            timesheet_period_object_id=timesheet_period_object_id,
            create_date=create_date,
            create_user=create_user,
            is_daily=is_daily,
            last_received_date=last_received_date,
            last_update_date=last_update_date,
            last_update_user=last_update_user,
            notes=notes,
            resource_id=resource_id,
            resource_name=resource_name,
            status=status,
            status_date=status_date,
        )

        timesheet.additional_properties = d
        return timesheet

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
