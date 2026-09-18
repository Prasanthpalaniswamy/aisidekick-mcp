from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPrimaryBaselineProjectResponse")


@_attrs_define
class GetPrimaryBaselineProjectResponse:
    """GetPrimaryBaselineProjectResponse Entity

    Attributes:
        primary_baseline_object_id (int | Unset):
    """

    primary_baseline_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        primary_baseline_object_id = self.primary_baseline_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if primary_baseline_object_id is not UNSET:
            field_dict["PrimaryBaselineObjectId"] = primary_baseline_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        primary_baseline_object_id = d.pop("PrimaryBaselineObjectId", UNSET)

        get_primary_baseline_project_response = cls(
            primary_baseline_object_id=primary_baseline_object_id,
        )

        get_primary_baseline_project_response.additional_properties = d
        return get_primary_baseline_project_response

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
