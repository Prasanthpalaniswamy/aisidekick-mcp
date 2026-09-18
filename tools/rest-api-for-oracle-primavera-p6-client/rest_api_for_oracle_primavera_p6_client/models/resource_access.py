from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceAccess")


@_attrs_define
class ResourceAccess:
    """ResourceAccess Entity

    Attributes:
        create_date (datetime.datetime | Unset): The date this resource security was created.
        create_user (str | Unset): The name of the user that created this resource security.
        last_update_date (datetime.datetime | Unset): The date this resource security was last updated.
        last_update_user (str | Unset): The name of the user that last updated this resource security.
        resource_id (str | Unset): The short code that uniquely identifies the resource.
        resource_name (str | Unset): The name of the resource.
        resource_object_id (int | Unset): The unique ID of the associated resource.
        sequence_number (int | Unset):
        user_name (str | Unset): The user's login name.
        user_object_id (int | Unset): The unique ID of the associated user.
    """

    create_date: datetime.datetime | Unset = UNSET
    create_user: str | Unset = UNSET
    last_update_date: datetime.datetime | Unset = UNSET
    last_update_user: str | Unset = UNSET
    resource_id: str | Unset = UNSET
    resource_name: str | Unset = UNSET
    resource_object_id: int | Unset = UNSET
    sequence_number: int | Unset = UNSET
    user_name: str | Unset = UNSET
    user_object_id: int | Unset = UNSET
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

        resource_id = self.resource_id

        resource_name = self.resource_name

        resource_object_id = self.resource_object_id

        sequence_number = self.sequence_number

        user_name = self.user_name

        user_object_id = self.user_object_id

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
        if resource_id is not UNSET:
            field_dict["ResourceId"] = resource_id
        if resource_name is not UNSET:
            field_dict["ResourceName"] = resource_name
        if resource_object_id is not UNSET:
            field_dict["ResourceObjectId"] = resource_object_id
        if sequence_number is not UNSET:
            field_dict["SequenceNumber"] = sequence_number
        if user_name is not UNSET:
            field_dict["UserName"] = user_name
        if user_object_id is not UNSET:
            field_dict["UserObjectId"] = user_object_id

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

        resource_id = d.pop("ResourceId", UNSET)

        resource_name = d.pop("ResourceName", UNSET)

        resource_object_id = d.pop("ResourceObjectId", UNSET)

        sequence_number = d.pop("SequenceNumber", UNSET)

        user_name = d.pop("UserName", UNSET)

        user_object_id = d.pop("UserObjectId", UNSET)

        resource_access = cls(
            create_date=create_date,
            create_user=create_user,
            last_update_date=last_update_date,
            last_update_user=last_update_user,
            resource_id=resource_id,
            resource_name=resource_name,
            resource_object_id=resource_object_id,
            sequence_number=sequence_number,
            user_name=user_name,
            user_object_id=user_object_id,
        )

        resource_access.additional_properties = d
        return resource_access

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
