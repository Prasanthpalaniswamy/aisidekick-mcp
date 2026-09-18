from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteWithReplacementTO")


@_attrs_define
class DeleteWithReplacementTO:
    """
    Attributes:
        object_id (str):
        replacement_object_id (int | Unset):
    """

    object_id: str
    replacement_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_id = self.object_id

        replacement_object_id = self.replacement_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ObjectId": object_id,
            }
        )
        if replacement_object_id is not UNSET:
            field_dict["ReplacementObjectId"] = replacement_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_id = d.pop("ObjectId")

        replacement_object_id = d.pop("ReplacementObjectId", UNSET)

        delete_with_replacement_to = cls(
            object_id=object_id,
            replacement_object_id=replacement_object_id,
        )

        delete_with_replacement_to.additional_properties = d
        return delete_with_replacement_to

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
