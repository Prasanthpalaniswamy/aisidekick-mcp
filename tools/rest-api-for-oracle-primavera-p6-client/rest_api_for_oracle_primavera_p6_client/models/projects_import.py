from __future__ import annotations

import json
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

if TYPE_CHECKING:
    from ..models.import_projects import ImportProjects


T = TypeVar("T", bound="ProjectsImport")


@_attrs_define
class ProjectsImport:
    """ProjectsImport Entity

    Attributes:
        project_data (File | Unset): File to import
        import_projects (ImportProjects | Unset):
    """

    project_data: File | Unset = UNSET
    import_projects: ImportProjects | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_data: FileTypes | Unset = UNSET
        if not isinstance(self.project_data, Unset):
            project_data = self.project_data.to_tuple()

        import_projects: dict[str, Any] | Unset = UNSET
        if not isinstance(self.import_projects, Unset):
            import_projects = self.import_projects.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_data is not UNSET:
            field_dict["ProjectData"] = project_data
        if import_projects is not UNSET:
            field_dict["ImportProjects"] = import_projects

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.project_data, Unset):
            files.append(("ProjectData", self.project_data.to_tuple()))

        if not isinstance(self.import_projects, Unset):
            files.append(
                ("ImportProjects", (None, json.dumps(self.import_projects.to_dict()).encode(), "application/json"))
            )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_projects import ImportProjects

        d = dict(src_dict)
        _project_data = d.pop("ProjectData", UNSET)
        project_data: File | Unset
        if isinstance(_project_data, Unset):
            project_data = UNSET
        else:
            project_data = File(payload=BytesIO(_project_data))

        _import_projects = d.pop("ImportProjects", UNSET)
        import_projects: ImportProjects | Unset
        if isinstance(_import_projects, Unset):
            import_projects = UNSET
        else:
            import_projects = ImportProjects.from_dict(_import_projects)

        projects_import = cls(
            project_data=project_data,
            import_projects=import_projects,
        )

        projects_import.additional_properties = d
        return projects_import

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
