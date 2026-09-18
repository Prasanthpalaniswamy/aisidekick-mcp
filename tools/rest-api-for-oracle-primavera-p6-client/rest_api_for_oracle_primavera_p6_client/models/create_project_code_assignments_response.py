from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateProjectCodeAssignmentsResponse")


@_attrs_define
class CreateProjectCodeAssignmentsResponse:
    """CreateProjectCodeAssignmentsResponse Entity

    Attributes:
        project_object_id (int | Unset): The unique ID of the project to which the project code is assigned.
        project_code_type_object_id (int | Unset): The unique ID of the parent project code type.
    """

    project_object_id: int | Unset = UNSET
    project_code_type_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_object_id = self.project_object_id

        project_code_type_object_id = self.project_code_type_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_object_id is not UNSET:
            field_dict["ProjectObjectId"] = project_object_id
        if project_code_type_object_id is not UNSET:
            field_dict["ProjectCodeTypeObjectId"] = project_code_type_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_object_id = d.pop("ProjectObjectId", UNSET)

        project_code_type_object_id = d.pop("ProjectCodeTypeObjectId", UNSET)

        create_project_code_assignments_response = cls(
            project_object_id=project_object_id,
            project_code_type_object_id=project_code_type_object_id,
        )

        create_project_code_assignments_response.additional_properties = d
        return create_project_code_assignments_response

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
