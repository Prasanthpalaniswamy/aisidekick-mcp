from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssignProjectAsBaselineResponse")


@_attrs_define
class AssignProjectAsBaselineResponse:
    """AssignProjectAsBaselineResponse Entity

    Attributes:
        baseline_project_object_id (int | Unset):
    """

    baseline_project_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        baseline_project_object_id = self.baseline_project_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if baseline_project_object_id is not UNSET:
            field_dict["BaselineProjectObjectId"] = baseline_project_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        baseline_project_object_id = d.pop("BaselineProjectObjectId", UNSET)

        assign_project_as_baseline_response = cls(
            baseline_project_object_id=baseline_project_object_id,
        )

        assign_project_as_baseline_response.additional_properties = d
        return assign_project_as_baseline_response

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
