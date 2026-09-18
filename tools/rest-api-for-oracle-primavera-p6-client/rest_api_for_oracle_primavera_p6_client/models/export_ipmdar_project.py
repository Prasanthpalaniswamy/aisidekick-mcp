from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportIpmdarProject")


@_attrs_define
class ExportIpmdarProject:
    """ExportIpmdarProject Entity

    Attributes:
        template_id (str | Unset):
        project_id (str | Unset):
    """

    template_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_id = self.template_id

        project_id = self.project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template_id is not UNSET:
            field_dict["TemplateId"] = template_id
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        template_id = d.pop("TemplateId", UNSET)

        project_id = d.pop("ProjectId", UNSET)

        export_ipmdar_project = cls(
            template_id=template_id,
            project_id=project_id,
        )

        export_ipmdar_project.additional_properties = d
        return export_ipmdar_project

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
