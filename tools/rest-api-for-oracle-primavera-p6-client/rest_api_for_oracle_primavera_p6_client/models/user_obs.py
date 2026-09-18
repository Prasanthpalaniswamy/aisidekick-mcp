from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserOBS")


@_attrs_define
class UserOBS:
    """UserOBS Entity

    Attributes:
        create_date (datetime.datetime | Unset): The date this association was created.
        create_user (str | Unset): The name of the user that created this association.
        last_update_date (datetime.datetime | Unset): The date this association was last updated.
        last_update_user (str | Unset): The name of the user that last updated this association.
        profile_name (str | Unset): The name of security profile.
        project_profile_object_id (int | Unset): The unique ID of the project profile with which the user is granted
            access to the project and OBS. See the ProjectProfile class for a constant defining the fixed profile of Project
            Superuser.
        user_name (str | Unset): The user's login name.
        user_object_id (int | Unset): The unique ID of the user who is assigned to the project OBS.
        obs_name (str | Unset): The name of the person/role in the organization, sometimes referred to as the
            "responsible manager".
        obs_object_id (int | Unset): The unique ID of the OBS to which the user is granted access.
    """

    create_date: datetime.datetime | Unset = UNSET
    create_user: str | Unset = UNSET
    last_update_date: datetime.datetime | Unset = UNSET
    last_update_user: str | Unset = UNSET
    profile_name: str | Unset = UNSET
    project_profile_object_id: int | Unset = UNSET
    user_name: str | Unset = UNSET
    user_object_id: int | Unset = UNSET
    obs_name: str | Unset = UNSET
    obs_object_id: int | Unset = UNSET
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

        profile_name = self.profile_name

        project_profile_object_id = self.project_profile_object_id

        user_name = self.user_name

        user_object_id = self.user_object_id

        obs_name = self.obs_name

        obs_object_id = self.obs_object_id

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
        if profile_name is not UNSET:
            field_dict["ProfileName"] = profile_name
        if project_profile_object_id is not UNSET:
            field_dict["ProjectProfileObjectId"] = project_profile_object_id
        if user_name is not UNSET:
            field_dict["UserName"] = user_name
        if user_object_id is not UNSET:
            field_dict["UserObjectId"] = user_object_id
        if obs_name is not UNSET:
            field_dict["OBSName"] = obs_name
        if obs_object_id is not UNSET:
            field_dict["OBSObjectId"] = obs_object_id

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

        profile_name = d.pop("ProfileName", UNSET)

        project_profile_object_id = d.pop("ProjectProfileObjectId", UNSET)

        user_name = d.pop("UserName", UNSET)

        user_object_id = d.pop("UserObjectId", UNSET)

        obs_name = d.pop("OBSName", UNSET)

        obs_object_id = d.pop("OBSObjectId", UNSET)

        user_obs = cls(
            create_date=create_date,
            create_user=create_user,
            last_update_date=last_update_date,
            last_update_user=last_update_user,
            profile_name=profile_name,
            project_profile_object_id=project_profile_object_id,
            user_name=user_name,
            user_object_id=user_object_id,
            obs_name=obs_name,
            obs_object_id=obs_object_id,
        )

        user_obs.additional_properties = d
        return user_obs

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
