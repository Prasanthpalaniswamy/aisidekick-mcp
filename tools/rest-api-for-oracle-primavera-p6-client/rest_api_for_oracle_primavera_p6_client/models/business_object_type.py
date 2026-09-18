from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.business_object_type_import_option import BusinessObjectTypeImportOption
from ..types import UNSET, Unset

T = TypeVar("T", bound="BusinessObjectType")


@_attrs_define
class BusinessObjectType:
    """BusinessObjectType Entity

    Attributes:
        import_option (BusinessObjectTypeImportOption | Unset):
    """

    import_option: BusinessObjectTypeImportOption | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        import_option: str | Unset = UNSET
        if not isinstance(self.import_option, Unset):
            import_option = self.import_option.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if import_option is not UNSET:
            field_dict["ImportOption"] = import_option

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _import_option = d.pop("ImportOption", UNSET)
        import_option: BusinessObjectTypeImportOption | Unset
        if isinstance(_import_option, Unset):
            import_option = UNSET
        else:
            import_option = BusinessObjectTypeImportOption(_import_option)

        business_object_type = cls(
            import_option=import_option,
        )

        business_object_type.additional_properties = d
        return business_object_type

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
