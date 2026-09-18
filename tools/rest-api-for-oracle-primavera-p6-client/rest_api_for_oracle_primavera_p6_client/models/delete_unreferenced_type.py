from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delete_unreferenced_type_import_option import DeleteUnreferencedTypeImportOption
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteUnreferencedType")


@_attrs_define
class DeleteUnreferencedType:
    """
    Attributes:
        import_option (DeleteUnreferencedTypeImportOption | Unset):
        delete_unreferenced (bool | Unset):
    """

    import_option: DeleteUnreferencedTypeImportOption | Unset = UNSET
    delete_unreferenced: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        import_option: str | Unset = UNSET
        if not isinstance(self.import_option, Unset):
            import_option = self.import_option.value

        delete_unreferenced = self.delete_unreferenced

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if import_option is not UNSET:
            field_dict["ImportOption"] = import_option
        if delete_unreferenced is not UNSET:
            field_dict["DeleteUnreferenced"] = delete_unreferenced

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _import_option = d.pop("ImportOption", UNSET)
        import_option: DeleteUnreferencedTypeImportOption | Unset
        if isinstance(_import_option, Unset):
            import_option = UNSET
        else:
            import_option = DeleteUnreferencedTypeImportOption(_import_option)

        delete_unreferenced = d.pop("DeleteUnreferenced", UNSET)

        delete_unreferenced_type = cls(
            import_option=import_option,
            delete_unreferenced=delete_unreferenced,
        )

        delete_unreferenced_type.additional_properties = d
        return delete_unreferenced_type

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
