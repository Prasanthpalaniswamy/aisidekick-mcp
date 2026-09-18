from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.role_limit_field_item import RoleLimitFieldItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="RoleLimit")


@_attrs_define
class RoleLimit:
    """RoleLimit Entity

    Attributes:
        include (bool | Unset): Boolean flag that indicates whether the associated object is to be exported. The default
            value of the Include element is true. To exclude a business object from the XML export file, specify false in
            the Include element for that business object.
        field (list[RoleLimitFieldItem] | Unset): List of Fields for RoleLimit Business Object
    """

    include: bool | Unset = UNSET
    field: list[RoleLimitFieldItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        include = self.include

        field: list[str] | Unset = UNSET
        if not isinstance(self.field, Unset):
            field = []
            for field_item_data in self.field:
                field_item = field_item_data.value
                field.append(field_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include is not UNSET:
            field_dict["Include"] = include
        if field is not UNSET:
            field_dict["Field"] = field

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        include = d.pop("Include", UNSET)

        _field = d.pop("Field", UNSET)
        field: list[RoleLimitFieldItem] | Unset = UNSET
        if _field is not UNSET:
            field = []
            for field_item_data in _field:
                field_item = RoleLimitFieldItem(field_item_data)

                field.append(field_item)

        role_limit = cls(
            include=include,
            field=field,
        )

        role_limit.additional_properties = d
        return role_limit

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
