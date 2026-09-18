from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportDOECPPProject")


@_attrs_define
class ExportDOECPPProject:
    """ExportDOECPPProject Entity

    Attributes:
        project_object_id (list[int] | Unset):
        baseline_object_id (list[int] | Unset):
        template_id (str | Unset):
    """

    project_object_id: list[int] | Unset = UNSET
    baseline_object_id: list[int] | Unset = UNSET
    template_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_object_id: list[int] | Unset = UNSET
        if not isinstance(self.project_object_id, Unset):
            project_object_id = self.project_object_id

        baseline_object_id: list[int] | Unset = UNSET
        if not isinstance(self.baseline_object_id, Unset):
            baseline_object_id = self.baseline_object_id

        template_id = self.template_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_object_id is not UNSET:
            field_dict["ProjectObjectId"] = project_object_id
        if baseline_object_id is not UNSET:
            field_dict["BaselineObjectId"] = baseline_object_id
        if template_id is not UNSET:
            field_dict["TemplateId"] = template_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_object_id = cast(list[int], d.pop("ProjectObjectId", UNSET))

        baseline_object_id = cast(list[int], d.pop("BaselineObjectId", UNSET))

        template_id = d.pop("TemplateId", UNSET)

        export_doecpp_project = cls(
            project_object_id=project_object_id,
            baseline_object_id=baseline_object_id,
            template_id=template_id,
        )

        export_doecpp_project.additional_properties = d
        return export_doecpp_project

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
