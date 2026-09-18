from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateActivityCodeAssignmentsResponse")


@_attrs_define
class CreateActivityCodeAssignmentsResponse:
    """CreateActivityCodeAssignmentsResponse Entity

    Attributes:
        activity_code_type_object_id (int | Unset): The unique ID of the parent activity code type.
        activity_object_id (int | Unset): The unique ID of the activity to which the activity code is assigned.
    """

    activity_code_type_object_id: int | Unset = UNSET
    activity_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_code_type_object_id = self.activity_code_type_object_id

        activity_object_id = self.activity_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity_code_type_object_id is not UNSET:
            field_dict["ActivityCodeTypeObjectId"] = activity_code_type_object_id
        if activity_object_id is not UNSET:
            field_dict["ActivityObjectId"] = activity_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        activity_code_type_object_id = d.pop("ActivityCodeTypeObjectId", UNSET)

        activity_object_id = d.pop("ActivityObjectId", UNSET)

        create_activity_code_assignments_response = cls(
            activity_code_type_object_id=activity_code_type_object_id,
            activity_object_id=activity_object_id,
        )

        create_activity_code_assignments_response.additional_properties = d
        return create_activity_code_assignments_response

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
