from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GlobalReplace")


@_attrs_define
class GlobalReplace:
    """GlobalReplace Entity

    Attributes:
        all_projects (bool | Unset): The option used to set all of projects to which a user has access.
        global_replace_data (str | Unset): The Global Replace template.
        global_replace_name (str | Unset): The Global Replace template name.
        greplace_object_id (int | Unset): The unique id of the Global Replace template.
        project_id_name (str | Unset): Project ids and names that are separated by commas.
        project_ids (str | Unset): TProject ids that are separated by commas.
        replace_field_name_one (str | Unset): First field name the user has selected to replace.
        search_criteria (str | Unset): The criteria that is used to search and load business objects.
        subject_area_type (str | Unset): The name of the object to be updated.
        user_object_id (int | Unset): The unique id of the associated user.
    """

    all_projects: bool | Unset = UNSET
    global_replace_data: str | Unset = UNSET
    global_replace_name: str | Unset = UNSET
    greplace_object_id: int | Unset = UNSET
    project_id_name: str | Unset = UNSET
    project_ids: str | Unset = UNSET
    replace_field_name_one: str | Unset = UNSET
    search_criteria: str | Unset = UNSET
    subject_area_type: str | Unset = UNSET
    user_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_projects = self.all_projects

        global_replace_data = self.global_replace_data

        global_replace_name = self.global_replace_name

        greplace_object_id = self.greplace_object_id

        project_id_name = self.project_id_name

        project_ids = self.project_ids

        replace_field_name_one = self.replace_field_name_one

        search_criteria = self.search_criteria

        subject_area_type = self.subject_area_type

        user_object_id = self.user_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_projects is not UNSET:
            field_dict["AllProjects"] = all_projects
        if global_replace_data is not UNSET:
            field_dict["GlobalReplaceData"] = global_replace_data
        if global_replace_name is not UNSET:
            field_dict["GlobalReplaceName"] = global_replace_name
        if greplace_object_id is not UNSET:
            field_dict["GreplaceObjectId"] = greplace_object_id
        if project_id_name is not UNSET:
            field_dict["ProjectIdName"] = project_id_name
        if project_ids is not UNSET:
            field_dict["ProjectIds"] = project_ids
        if replace_field_name_one is not UNSET:
            field_dict["ReplaceFieldNameOne"] = replace_field_name_one
        if search_criteria is not UNSET:
            field_dict["SearchCriteria"] = search_criteria
        if subject_area_type is not UNSET:
            field_dict["SubjectAreaType"] = subject_area_type
        if user_object_id is not UNSET:
            field_dict["UserObjectId"] = user_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        all_projects = d.pop("AllProjects", UNSET)

        global_replace_data = d.pop("GlobalReplaceData", UNSET)

        global_replace_name = d.pop("GlobalReplaceName", UNSET)

        greplace_object_id = d.pop("GreplaceObjectId", UNSET)

        project_id_name = d.pop("ProjectIdName", UNSET)

        project_ids = d.pop("ProjectIds", UNSET)

        replace_field_name_one = d.pop("ReplaceFieldNameOne", UNSET)

        search_criteria = d.pop("SearchCriteria", UNSET)

        subject_area_type = d.pop("SubjectAreaType", UNSET)

        user_object_id = d.pop("UserObjectId", UNSET)

        global_replace = cls(
            all_projects=all_projects,
            global_replace_data=global_replace_data,
            global_replace_name=global_replace_name,
            greplace_object_id=greplace_object_id,
            project_id_name=project_id_name,
            project_ids=project_ids,
            replace_field_name_one=replace_field_name_one,
            search_criteria=search_criteria,
            subject_area_type=subject_area_type,
            user_object_id=user_object_id,
        )

        global_replace.additional_properties = d
        return global_replace

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
