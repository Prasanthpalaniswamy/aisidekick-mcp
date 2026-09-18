from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateResourceRoleResponse")


@_attrs_define
class CreateResourceRoleResponse:
    """CreateResourceRoleResponse Entity

    Attributes:
        resource_object_id (int | Unset): The unique ID of the associated Resource.
        role_object_id (int | Unset):
    """

    resource_object_id: int | Unset = UNSET
    role_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_object_id = self.resource_object_id

        role_object_id = self.role_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_object_id is not UNSET:
            field_dict["ResourceObjectId"] = resource_object_id
        if role_object_id is not UNSET:
            field_dict["RoleObjectId"] = role_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_object_id = d.pop("ResourceObjectId", UNSET)

        role_object_id = d.pop("RoleObjectId", UNSET)

        create_resource_role_response = cls(
            resource_object_id=resource_object_id,
            role_object_id=role_object_id,
        )

        create_resource_role_response.additional_properties = d
        return create_resource_role_response

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
