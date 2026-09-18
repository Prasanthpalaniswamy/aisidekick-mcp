from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PAuditX")


@_attrs_define
class PAuditX:
    """PAuditX Entity

    Attributes:
        subject_area (str | Unset): Denotes the table name of the audit record
        table_primary_keys (str | Unset): Denotes the table primary keys of the audit record
        table_column_name (str | Unset): Denotes the table column name of the audit record.
        old_value (str | Unset): Denotes the previous value of the attribute column of audit record
        new_value (str | Unset): Denotes the new value of the attribute column of audit record
        project_id (int | Unset): Project id of the audit record
        operation (str | Unset): Denotes the operation that was executed on the audit record
        prm_user_name (str | Unset): Denotes the name of the user which created or updated the audit record
        host_name (str | Unset): Denotes the hostname when the audit record was created or updated
        application_name (str | Unset): Denotes the application name of the audit record.
        audit_timestamp (datetime.datetime | Unset): Denotes the timestamp at which the record was created, updated or
            deleted
        project_name (str | Unset): Denotes the project name of the audit record with respect to project id
        project_short_name (str | Unset): Denotes the project short name of the audit record with respect to project id
        activity_code (str | Unset): Denotes the activity name of the audit record with respect to table primary key
            when table name is TASK
        activity_name (str | Unset): Denotes the actiity name of the audit record with respect to table primary key when
            table name is TASK
        actual_name (str | Unset): Denotes the actual name of the user which executed the operation on the audit record
    """

    subject_area: str | Unset = UNSET
    table_primary_keys: str | Unset = UNSET
    table_column_name: str | Unset = UNSET
    old_value: str | Unset = UNSET
    new_value: str | Unset = UNSET
    project_id: int | Unset = UNSET
    operation: str | Unset = UNSET
    prm_user_name: str | Unset = UNSET
    host_name: str | Unset = UNSET
    application_name: str | Unset = UNSET
    audit_timestamp: datetime.datetime | Unset = UNSET
    project_name: str | Unset = UNSET
    project_short_name: str | Unset = UNSET
    activity_code: str | Unset = UNSET
    activity_name: str | Unset = UNSET
    actual_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subject_area = self.subject_area

        table_primary_keys = self.table_primary_keys

        table_column_name = self.table_column_name

        old_value = self.old_value

        new_value = self.new_value

        project_id = self.project_id

        operation = self.operation

        prm_user_name = self.prm_user_name

        host_name = self.host_name

        application_name = self.application_name

        audit_timestamp: str | Unset = UNSET
        if not isinstance(self.audit_timestamp, Unset):
            audit_timestamp = self.audit_timestamp.isoformat()

        project_name = self.project_name

        project_short_name = self.project_short_name

        activity_code = self.activity_code

        activity_name = self.activity_name

        actual_name = self.actual_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subject_area is not UNSET:
            field_dict["SubjectArea"] = subject_area
        if table_primary_keys is not UNSET:
            field_dict["TablePrimaryKeys"] = table_primary_keys
        if table_column_name is not UNSET:
            field_dict["TableColumnName"] = table_column_name
        if old_value is not UNSET:
            field_dict["OldValue"] = old_value
        if new_value is not UNSET:
            field_dict["NewValue"] = new_value
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if operation is not UNSET:
            field_dict["Operation"] = operation
        if prm_user_name is not UNSET:
            field_dict["PrmUserName"] = prm_user_name
        if host_name is not UNSET:
            field_dict["HostName"] = host_name
        if application_name is not UNSET:
            field_dict["ApplicationName"] = application_name
        if audit_timestamp is not UNSET:
            field_dict["AuditTimestamp"] = audit_timestamp
        if project_name is not UNSET:
            field_dict["ProjectName"] = project_name
        if project_short_name is not UNSET:
            field_dict["ProjectShortName"] = project_short_name
        if activity_code is not UNSET:
            field_dict["ActivityCode"] = activity_code
        if activity_name is not UNSET:
            field_dict["ActivityName"] = activity_name
        if actual_name is not UNSET:
            field_dict["ActualName"] = actual_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subject_area = d.pop("SubjectArea", UNSET)

        table_primary_keys = d.pop("TablePrimaryKeys", UNSET)

        table_column_name = d.pop("TableColumnName", UNSET)

        old_value = d.pop("OldValue", UNSET)

        new_value = d.pop("NewValue", UNSET)

        project_id = d.pop("ProjectId", UNSET)

        operation = d.pop("Operation", UNSET)

        prm_user_name = d.pop("PrmUserName", UNSET)

        host_name = d.pop("HostName", UNSET)

        application_name = d.pop("ApplicationName", UNSET)

        _audit_timestamp = d.pop("AuditTimestamp", UNSET)
        audit_timestamp: datetime.datetime | Unset
        if isinstance(_audit_timestamp, Unset):
            audit_timestamp = UNSET
        else:
            audit_timestamp = isoparse(_audit_timestamp)

        project_name = d.pop("ProjectName", UNSET)

        project_short_name = d.pop("ProjectShortName", UNSET)

        activity_code = d.pop("ActivityCode", UNSET)

        activity_name = d.pop("ActivityName", UNSET)

        actual_name = d.pop("ActualName", UNSET)

        p_audit_x = cls(
            subject_area=subject_area,
            table_primary_keys=table_primary_keys,
            table_column_name=table_column_name,
            old_value=old_value,
            new_value=new_value,
            project_id=project_id,
            operation=operation,
            prm_user_name=prm_user_name,
            host_name=host_name,
            application_name=application_name,
            audit_timestamp=audit_timestamp,
            project_name=project_name,
            project_short_name=project_short_name,
            activity_code=activity_code,
            activity_name=activity_name,
            actual_name=actual_name,
        )

        p_audit_x.additional_properties = d
        return p_audit_x

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
