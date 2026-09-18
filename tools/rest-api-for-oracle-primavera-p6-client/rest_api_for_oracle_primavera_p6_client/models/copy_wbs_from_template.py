from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CopyWBSFromTemplate")


@_attrs_define
class CopyWBSFromTemplate:
    """CopyWBSFromTemplate Entity

    Attributes:
        object_id (int | Unset): The unique identifier of an existing project that will contain the copied WBS
            structure.
        template_wbs_object_id (int | Unset): The unique identifier of the source WBS structure to copy.
        copy_wbs_notes (bool | Unset):
        copy_wbs_milestones (bool | Unset):
        copy_activities (bool | Unset):
        copy_resource_and_role_assignments (bool | Unset):
        copy_relationships (bool | Unset):
        copy_activity_codes (bool | Unset):
        copy_eps_codes_at_project_level (bool | Unset):
        copy_activity_notes (bool | Unset):
        copy_activity_steps (bool | Unset):
        copy_assignment_codes (bool | Unset):
        copy_assignment_secure_codes (bool | Unset):
        copy_activity_secure_codes (bool | Unset):
    """

    object_id: int | Unset = UNSET
    template_wbs_object_id: int | Unset = UNSET
    copy_wbs_notes: bool | Unset = UNSET
    copy_wbs_milestones: bool | Unset = UNSET
    copy_activities: bool | Unset = UNSET
    copy_resource_and_role_assignments: bool | Unset = UNSET
    copy_relationships: bool | Unset = UNSET
    copy_activity_codes: bool | Unset = UNSET
    copy_eps_codes_at_project_level: bool | Unset = UNSET
    copy_activity_notes: bool | Unset = UNSET
    copy_activity_steps: bool | Unset = UNSET
    copy_assignment_codes: bool | Unset = UNSET
    copy_assignment_secure_codes: bool | Unset = UNSET
    copy_activity_secure_codes: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_id = self.object_id

        template_wbs_object_id = self.template_wbs_object_id

        copy_wbs_notes = self.copy_wbs_notes

        copy_wbs_milestones = self.copy_wbs_milestones

        copy_activities = self.copy_activities

        copy_resource_and_role_assignments = self.copy_resource_and_role_assignments

        copy_relationships = self.copy_relationships

        copy_activity_codes = self.copy_activity_codes

        copy_eps_codes_at_project_level = self.copy_eps_codes_at_project_level

        copy_activity_notes = self.copy_activity_notes

        copy_activity_steps = self.copy_activity_steps

        copy_assignment_codes = self.copy_assignment_codes

        copy_assignment_secure_codes = self.copy_assignment_secure_codes

        copy_activity_secure_codes = self.copy_activity_secure_codes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_id is not UNSET:
            field_dict["ObjectId"] = object_id
        if template_wbs_object_id is not UNSET:
            field_dict["TemplateWbsObjectId"] = template_wbs_object_id
        if copy_wbs_notes is not UNSET:
            field_dict["CopyWBSNotes"] = copy_wbs_notes
        if copy_wbs_milestones is not UNSET:
            field_dict["CopyWBSMilestones"] = copy_wbs_milestones
        if copy_activities is not UNSET:
            field_dict["CopyActivities"] = copy_activities
        if copy_resource_and_role_assignments is not UNSET:
            field_dict["CopyResourceAndRoleAssignments"] = copy_resource_and_role_assignments
        if copy_relationships is not UNSET:
            field_dict["CopyRelationships"] = copy_relationships
        if copy_activity_codes is not UNSET:
            field_dict["CopyActivityCodes"] = copy_activity_codes
        if copy_eps_codes_at_project_level is not UNSET:
            field_dict["CopyEPSCodesAtProjectLevel"] = copy_eps_codes_at_project_level
        if copy_activity_notes is not UNSET:
            field_dict["CopyActivityNotes"] = copy_activity_notes
        if copy_activity_steps is not UNSET:
            field_dict["CopyActivitySteps"] = copy_activity_steps
        if copy_assignment_codes is not UNSET:
            field_dict["CopyAssignmentCodes"] = copy_assignment_codes
        if copy_assignment_secure_codes is not UNSET:
            field_dict["CopyAssignmentSecureCodes"] = copy_assignment_secure_codes
        if copy_activity_secure_codes is not UNSET:
            field_dict["CopyActivitySecureCodes"] = copy_activity_secure_codes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_id = d.pop("ObjectId", UNSET)

        template_wbs_object_id = d.pop("TemplateWbsObjectId", UNSET)

        copy_wbs_notes = d.pop("CopyWBSNotes", UNSET)

        copy_wbs_milestones = d.pop("CopyWBSMilestones", UNSET)

        copy_activities = d.pop("CopyActivities", UNSET)

        copy_resource_and_role_assignments = d.pop("CopyResourceAndRoleAssignments", UNSET)

        copy_relationships = d.pop("CopyRelationships", UNSET)

        copy_activity_codes = d.pop("CopyActivityCodes", UNSET)

        copy_eps_codes_at_project_level = d.pop("CopyEPSCodesAtProjectLevel", UNSET)

        copy_activity_notes = d.pop("CopyActivityNotes", UNSET)

        copy_activity_steps = d.pop("CopyActivitySteps", UNSET)

        copy_assignment_codes = d.pop("CopyAssignmentCodes", UNSET)

        copy_assignment_secure_codes = d.pop("CopyAssignmentSecureCodes", UNSET)

        copy_activity_secure_codes = d.pop("CopyActivitySecureCodes", UNSET)

        copy_wbs_from_template = cls(
            object_id=object_id,
            template_wbs_object_id=template_wbs_object_id,
            copy_wbs_notes=copy_wbs_notes,
            copy_wbs_milestones=copy_wbs_milestones,
            copy_activities=copy_activities,
            copy_resource_and_role_assignments=copy_resource_and_role_assignments,
            copy_relationships=copy_relationships,
            copy_activity_codes=copy_activity_codes,
            copy_eps_codes_at_project_level=copy_eps_codes_at_project_level,
            copy_activity_notes=copy_activity_notes,
            copy_activity_steps=copy_activity_steps,
            copy_assignment_codes=copy_assignment_codes,
            copy_assignment_secure_codes=copy_assignment_secure_codes,
            copy_activity_secure_codes=copy_activity_secure_codes,
        )

        copy_wbs_from_template.additional_properties = d
        return copy_wbs_from_template

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
