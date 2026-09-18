from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceAssignmentCodeAssignment")


@_attrs_define
class ResourceAssignmentCodeAssignment:
    """ResourceAssignmentCodeAssignment Entity

    Attributes:
        create_date (datetime.datetime | Unset): The date this code assignment was created.
        create_user (str | Unset): The name of the user that created this code assignment.
        last_update_date (datetime.datetime | Unset): The date this code assignment was last updated.
        last_update_user (str | Unset): The name of the user that last updated this code assignment.
        project_object_id (int | Unset): The unique identifier of the project that is associated with the
            ResourceAssignmentCodeAssignment object.
        resource_assignment_code_description (str | Unset): The description of the associated code.
        resource_assignment_code_object_id (int | Unset): The unique ID of the associated code.
        resource_assignment_code_type_name (str | Unset): The name of the parent code type.
        resource_assignment_code_type_object_id (int | Unset): The unique ID of the parent code type.
        resource_assignment_code_value (str | Unset): The value of the associated code.
        resource_assignment_object_id (int | Unset): The object ID of the associated resource or role assignment.
    """

    create_date: datetime.datetime | Unset = UNSET
    create_user: str | Unset = UNSET
    last_update_date: datetime.datetime | Unset = UNSET
    last_update_user: str | Unset = UNSET
    project_object_id: int | Unset = UNSET
    resource_assignment_code_description: str | Unset = UNSET
    resource_assignment_code_object_id: int | Unset = UNSET
    resource_assignment_code_type_name: str | Unset = UNSET
    resource_assignment_code_type_object_id: int | Unset = UNSET
    resource_assignment_code_value: str | Unset = UNSET
    resource_assignment_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_date: str | Unset = UNSET
        if not isinstance(self.create_date, Unset):
            create_date = self.create_date.isoformat()

        create_user = self.create_user

        last_update_date: str | Unset = UNSET
        if not isinstance(self.last_update_date, Unset):
            last_update_date = self.last_update_date.isoformat()

        last_update_user = self.last_update_user

        project_object_id = self.project_object_id

        resource_assignment_code_description = self.resource_assignment_code_description

        resource_assignment_code_object_id = self.resource_assignment_code_object_id

        resource_assignment_code_type_name = self.resource_assignment_code_type_name

        resource_assignment_code_type_object_id = self.resource_assignment_code_type_object_id

        resource_assignment_code_value = self.resource_assignment_code_value

        resource_assignment_object_id = self.resource_assignment_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_date is not UNSET:
            field_dict["CreateDate"] = create_date
        if create_user is not UNSET:
            field_dict["CreateUser"] = create_user
        if last_update_date is not UNSET:
            field_dict["LastUpdateDate"] = last_update_date
        if last_update_user is not UNSET:
            field_dict["LastUpdateUser"] = last_update_user
        if project_object_id is not UNSET:
            field_dict["ProjectObjectId"] = project_object_id
        if resource_assignment_code_description is not UNSET:
            field_dict["ResourceAssignmentCodeDescription"] = resource_assignment_code_description
        if resource_assignment_code_object_id is not UNSET:
            field_dict["ResourceAssignmentCodeObjectId"] = resource_assignment_code_object_id
        if resource_assignment_code_type_name is not UNSET:
            field_dict["ResourceAssignmentCodeTypeName"] = resource_assignment_code_type_name
        if resource_assignment_code_type_object_id is not UNSET:
            field_dict["ResourceAssignmentCodeTypeObjectId"] = resource_assignment_code_type_object_id
        if resource_assignment_code_value is not UNSET:
            field_dict["ResourceAssignmentCodeValue"] = resource_assignment_code_value
        if resource_assignment_object_id is not UNSET:
            field_dict["ResourceAssignmentObjectId"] = resource_assignment_object_id

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

        _last_update_date = d.pop("LastUpdateDate", UNSET)
        last_update_date: datetime.datetime | Unset
        if isinstance(_last_update_date, Unset):
            last_update_date = UNSET
        else:
            last_update_date = isoparse(_last_update_date)

        last_update_user = d.pop("LastUpdateUser", UNSET)

        project_object_id = d.pop("ProjectObjectId", UNSET)

        resource_assignment_code_description = d.pop("ResourceAssignmentCodeDescription", UNSET)

        resource_assignment_code_object_id = d.pop("ResourceAssignmentCodeObjectId", UNSET)

        resource_assignment_code_type_name = d.pop("ResourceAssignmentCodeTypeName", UNSET)

        resource_assignment_code_type_object_id = d.pop("ResourceAssignmentCodeTypeObjectId", UNSET)

        resource_assignment_code_value = d.pop("ResourceAssignmentCodeValue", UNSET)

        resource_assignment_object_id = d.pop("ResourceAssignmentObjectId", UNSET)

        resource_assignment_code_assignment = cls(
            create_date=create_date,
            create_user=create_user,
            last_update_date=last_update_date,
            last_update_user=last_update_user,
            project_object_id=project_object_id,
            resource_assignment_code_description=resource_assignment_code_description,
            resource_assignment_code_object_id=resource_assignment_code_object_id,
            resource_assignment_code_type_name=resource_assignment_code_type_name,
            resource_assignment_code_type_object_id=resource_assignment_code_type_object_id,
            resource_assignment_code_value=resource_assignment_code_value,
            resource_assignment_object_id=resource_assignment_object_id,
        )

        resource_assignment_code_assignment.additional_properties = d
        return resource_assignment_code_assignment

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
