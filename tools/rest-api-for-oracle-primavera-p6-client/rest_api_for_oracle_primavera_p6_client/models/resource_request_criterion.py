from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceRequestCriterion")


@_attrs_define
class ResourceRequestCriterion:
    """
    Attributes:
        criterion_type (str | Unset):
        proficiency (str | Unset):
        value_object_id (int | Unset):
    """

    criterion_type: str | Unset = UNSET
    proficiency: str | Unset = UNSET
    value_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        criterion_type = self.criterion_type

        proficiency = self.proficiency

        value_object_id = self.value_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if criterion_type is not UNSET:
            field_dict["CriterionType"] = criterion_type
        if proficiency is not UNSET:
            field_dict["Proficiency"] = proficiency
        if value_object_id is not UNSET:
            field_dict["ValueObjectId"] = value_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        criterion_type = d.pop("CriterionType", UNSET)

        proficiency = d.pop("Proficiency", UNSET)

        value_object_id = d.pop("ValueObjectId", UNSET)

        resource_request_criterion = cls(
            criterion_type=criterion_type,
            proficiency=proficiency,
            value_object_id=value_object_id,
        )

        resource_request_criterion.additional_properties = d
        return resource_request_criterion

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
