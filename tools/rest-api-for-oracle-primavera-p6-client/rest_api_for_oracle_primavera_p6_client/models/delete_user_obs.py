from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteUserOBS")


@_attrs_define
class DeleteUserOBS:
    """DeleteUserOBS Entity

    Attributes:
        obsobject_id (int | Unset):
        user_object_id (int | Unset):
        obs_object_id (int | Unset):
    """

    obsobject_id: int | Unset = UNSET
    user_object_id: int | Unset = UNSET
    obs_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        obsobject_id = self.obsobject_id

        user_object_id = self.user_object_id

        obs_object_id = self.obs_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if obsobject_id is not UNSET:
            field_dict["obsobjectId"] = obsobject_id
        if user_object_id is not UNSET:
            field_dict["UserObjectId"] = user_object_id
        if obs_object_id is not UNSET:
            field_dict["OBSObjectId"] = obs_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        obsobject_id = d.pop("obsobjectId", UNSET)

        user_object_id = d.pop("UserObjectId", UNSET)

        obs_object_id = d.pop("OBSObjectId", UNSET)

        delete_user_obs = cls(
            obsobject_id=obsobject_id,
            user_object_id=user_object_id,
            obs_object_id=obs_object_id,
        )

        delete_user_obs.additional_properties = d
        return delete_user_obs

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
