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
    from ..models.create_new_project import CreateNewProject


T = TypeVar("T", bound="ImportCreateNewProject")


@_attrs_define
class ImportCreateNewProject:
    """ImportCreateNewProject Entity

    Attributes:
        project_data (File | Unset): File to import
        create_new_project (CreateNewProject | Unset):
    """

    project_data: File | Unset = UNSET
    create_new_project: CreateNewProject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_data: FileTypes | Unset = UNSET
        if not isinstance(self.project_data, Unset):
            project_data = self.project_data.to_tuple()

        create_new_project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.create_new_project, Unset):
            create_new_project = self.create_new_project.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_data is not UNSET:
            field_dict["ProjectData"] = project_data
        if create_new_project is not UNSET:
            field_dict["CreateNewProject"] = create_new_project

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.project_data, Unset):
            files.append(("ProjectData", self.project_data.to_tuple()))

        if not isinstance(self.create_new_project, Unset):
            files.append(
                ("CreateNewProject", (None, json.dumps(self.create_new_project.to_dict()).encode(), "application/json"))
            )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_new_project import CreateNewProject

        d = dict(src_dict)
        _project_data = d.pop("ProjectData", UNSET)
        project_data: File | Unset
        if isinstance(_project_data, Unset):
            project_data = UNSET
        else:
            project_data = File(payload=BytesIO(_project_data))

        _create_new_project = d.pop("CreateNewProject", UNSET)
        create_new_project: CreateNewProject | Unset
        if isinstance(_create_new_project, Unset):
            create_new_project = UNSET
        else:
            create_new_project = CreateNewProject.from_dict(_create_new_project)

        import_create_new_project = cls(
            project_data=project_data,
            create_new_project=create_new_project,
        )

        import_create_new_project.additional_properties = d
        return import_create_new_project

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
