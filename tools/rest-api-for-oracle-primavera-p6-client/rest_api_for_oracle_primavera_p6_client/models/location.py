from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Location")


@_attrs_define
class Location:
    """Location Entity

    Attributes:
        latitude (float): The latitude of the address.
        longitude (float): The longitude of the address.
        name (str): The name of the location.
        address_line_1 (str | Unset): The first line of the address with street number and street name.
        address_line_2 (str | Unset): The second line of the address with street number and street name.
        city (str | Unset): The city name of the address.
        country (str | Unset): The country of the address.
        country_code (str | Unset): The country code of the address.
        create_date (datetime.datetime | Unset): The creation date of the Location.
        create_user (str | Unset): The name of the user that created this location.
        last_update_date (datetime.datetime | Unset): The date this location was last updated.
        last_update_user (str | Unset): The name of the user that last updated this location.
        municipality (str | Unset): The municipality name of the address.
        object_id (int | Unset): The unique ID of the location.
        postal_code (str | Unset): The postal code of the address.
        state (str | Unset): The state name of the address.
        state_code (str | Unset): The state abbreviation of the address.
    """

    latitude: float
    longitude: float
    name: str
    address_line_1: str | Unset = UNSET
    address_line_2: str | Unset = UNSET
    city: str | Unset = UNSET
    country: str | Unset = UNSET
    country_code: str | Unset = UNSET
    create_date: datetime.datetime | Unset = UNSET
    create_user: str | Unset = UNSET
    last_update_date: datetime.datetime | Unset = UNSET
    last_update_user: str | Unset = UNSET
    municipality: str | Unset = UNSET
    object_id: int | Unset = UNSET
    postal_code: str | Unset = UNSET
    state: str | Unset = UNSET
    state_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latitude = self.latitude

        longitude = self.longitude

        name = self.name

        address_line_1 = self.address_line_1

        address_line_2 = self.address_line_2

        city = self.city

        country = self.country

        country_code = self.country_code

        create_date: str | Unset = UNSET
        if not isinstance(self.create_date, Unset):
            create_date = self.create_date.isoformat()

        create_user = self.create_user

        last_update_date: str | Unset = UNSET
        if not isinstance(self.last_update_date, Unset):
            last_update_date = self.last_update_date.isoformat()

        last_update_user = self.last_update_user

        municipality = self.municipality

        object_id = self.object_id

        postal_code = self.postal_code

        state = self.state

        state_code = self.state_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Latitude": latitude,
                "Longitude": longitude,
                "Name": name,
            }
        )
        if address_line_1 is not UNSET:
            field_dict["AddressLine1"] = address_line_1
        if address_line_2 is not UNSET:
            field_dict["AddressLine2"] = address_line_2
        if city is not UNSET:
            field_dict["City"] = city
        if country is not UNSET:
            field_dict["Country"] = country
        if country_code is not UNSET:
            field_dict["CountryCode"] = country_code
        if create_date is not UNSET:
            field_dict["CreateDate"] = create_date
        if create_user is not UNSET:
            field_dict["CreateUser"] = create_user
        if last_update_date is not UNSET:
            field_dict["LastUpdateDate"] = last_update_date
        if last_update_user is not UNSET:
            field_dict["LastUpdateUser"] = last_update_user
        if municipality is not UNSET:
            field_dict["Municipality"] = municipality
        if object_id is not UNSET:
            field_dict["ObjectId"] = object_id
        if postal_code is not UNSET:
            field_dict["PostalCode"] = postal_code
        if state is not UNSET:
            field_dict["State"] = state
        if state_code is not UNSET:
            field_dict["StateCode"] = state_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latitude = d.pop("Latitude")

        longitude = d.pop("Longitude")

        name = d.pop("Name")

        address_line_1 = d.pop("AddressLine1", UNSET)

        address_line_2 = d.pop("AddressLine2", UNSET)

        city = d.pop("City", UNSET)

        country = d.pop("Country", UNSET)

        country_code = d.pop("CountryCode", UNSET)

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

        municipality = d.pop("Municipality", UNSET)

        object_id = d.pop("ObjectId", UNSET)

        postal_code = d.pop("PostalCode", UNSET)

        state = d.pop("State", UNSET)

        state_code = d.pop("StateCode", UNSET)

        location = cls(
            latitude=latitude,
            longitude=longitude,
            name=name,
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            city=city,
            country=country,
            country_code=country_code,
            create_date=create_date,
            create_user=create_user,
            last_update_date=last_update_date,
            last_update_user=last_update_user,
            municipality=municipality,
            object_id=object_id,
            postal_code=postal_code,
            state=state,
            state_code=state_code,
        )

        location.additional_properties = d
        return location

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
