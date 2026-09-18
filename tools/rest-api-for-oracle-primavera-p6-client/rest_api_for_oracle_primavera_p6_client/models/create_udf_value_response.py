from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateUDFValueResponse")


@_attrs_define
class CreateUDFValueResponse:
    """CreateUDFValueResponse Entity

    Attributes:
        udf_type_object_id (int | Unset): The unique ID of the associated UDF type.
        foreign_object_id (int | Unset): The unique ID of the business object to which the UDF is
            assigned:ProjectObjectId, ActivityObjectId, ResourceObjectId, etc.
    """

    udf_type_object_id: int | Unset = UNSET
    foreign_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        udf_type_object_id = self.udf_type_object_id

        foreign_object_id = self.foreign_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if udf_type_object_id is not UNSET:
            field_dict["UDFTypeObjectId"] = udf_type_object_id
        if foreign_object_id is not UNSET:
            field_dict["ForeignObjectId"] = foreign_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        udf_type_object_id = d.pop("UDFTypeObjectId", UNSET)

        foreign_object_id = d.pop("ForeignObjectId", UNSET)

        create_udf_value_response = cls(
            udf_type_object_id=udf_type_object_id,
            foreign_object_id=foreign_object_id,
        )

        create_udf_value_response.additional_properties = d
        return create_udf_value_response

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
