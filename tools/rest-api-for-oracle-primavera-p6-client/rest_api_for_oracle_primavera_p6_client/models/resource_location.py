from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceLocation")


@_attrs_define
class ResourceLocation:
    """ResourceLocation Entity

    Attributes:
        create_date (datetime.datetime | Unset): The date this resource location was created.
        create_user (str | Unset): The name of the user that created this resource location.
        latitude (float | Unset): The latitude of the resource location.
        longitude (float | Unset): The longitude of the resource location.
        last_update_date (datetime.datetime | Unset): The date this resource location was last updated.
        last_update_user (str | Unset): The name of the user that last updated this resource location.
        object_id (int | Unset): The unique ID of the resource location.
        resource_object_id (int | Unset): The unique ID of the associated resource.
    """

    create_date: datetime.datetime | Unset = UNSET
    create_user: str | Unset = UNSET
    latitude: float | Unset = UNSET
    longitude: float | Unset = UNSET
    last_update_date: datetime.datetime | Unset = UNSET
    last_update_user: str | Unset = UNSET
    object_id: int | Unset = UNSET
    resource_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_date: str | Unset = UNSET
        if not isinstance(self.create_date, Unset):
            create_date = self.create_date.isoformat()

        create_user = self.create_user

        latitude = self.latitude

        longitude = self.longitude

        last_update_date: str | Unset = UNSET
        if not isinstance(self.last_update_date, Unset):
            last_update_date = self.last_update_date.isoformat()

        last_update_user = self.last_update_user

        object_id = self.object_id

        resource_object_id = self.resource_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_date is not UNSET:
            field_dict["CreateDate"] = create_date
        if create_user is not UNSET:
            field_dict["CreateUser"] = create_user
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if last_update_date is not UNSET:
            field_dict["LastUpdateDate"] = last_update_date
        if last_update_user is not UNSET:
            field_dict["LastUpdateUser"] = last_update_user
        if object_id is not UNSET:
            field_dict["ObjectId"] = object_id
        if resource_object_id is not UNSET:
            field_dict["ResourceObjectId"] = resource_object_id

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

        latitude = d.pop("Latitude", UNSET)

        longitude = d.pop("Longitude", UNSET)

        _last_update_date = d.pop("LastUpdateDate", UNSET)
        last_update_date: datetime.datetime | Unset
        if isinstance(_last_update_date, Unset):
            last_update_date = UNSET
        else:
            last_update_date = isoparse(_last_update_date)

        last_update_user = d.pop("LastUpdateUser", UNSET)

        object_id = d.pop("ObjectId", UNSET)

        resource_object_id = d.pop("ResourceObjectId", UNSET)

        resource_location = cls(
            create_date=create_date,
            create_user=create_user,
            latitude=latitude,
            longitude=longitude,
            last_update_date=last_update_date,
            last_update_user=last_update_user,
            object_id=object_id,
            resource_object_id=resource_object_id,
        )

        resource_location.additional_properties = d
        return resource_location

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
