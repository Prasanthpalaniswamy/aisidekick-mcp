from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.import_project_import_option import ImportProjectImportOption
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportProject")


@_attrs_define
class ImportProject:
    """ImportProject Entity

    Attributes:
        project_object_id (int | Unset): Specifies the Project Id to be imported.
        import_option (ImportProjectImportOption | Unset): Specify Create New to import a project that already exists as
            a new project; specify Update Existing to import a project to update an existing project.
        eps_object_id (int | Unset): If the ImportOption is Update Existing, then specifies the Project ID; if the
            ImportOption is Create New, then specifies the EPS ID.
    """

    project_object_id: int | Unset = UNSET
    import_option: ImportProjectImportOption | Unset = UNSET
    eps_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_object_id = self.project_object_id

        import_option: str | Unset = UNSET
        if not isinstance(self.import_option, Unset):
            import_option = self.import_option.value

        eps_object_id = self.eps_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_object_id is not UNSET:
            field_dict["ProjectObjectId"] = project_object_id
        if import_option is not UNSET:
            field_dict["ImportOption"] = import_option
        if eps_object_id is not UNSET:
            field_dict["EPSObjectId"] = eps_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_object_id = d.pop("ProjectObjectId", UNSET)

        _import_option = d.pop("ImportOption", UNSET)
        import_option: ImportProjectImportOption | Unset
        if isinstance(_import_option, Unset):
            import_option = UNSET
        else:
            import_option = ImportProjectImportOption(_import_option)

        eps_object_id = d.pop("EPSObjectId", UNSET)

        import_project = cls(
            project_object_id=project_object_id,
            import_option=import_option,
            eps_object_id=eps_object_id,
        )

        import_project.additional_properties = d
        return import_project

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
