from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CopyActivity")


@_attrs_define
class CopyActivity:
    """CopyActivity Entity

    Attributes:
        object_id (int | Unset): The unique identifier of the activity you want to copy.
        target_project_object_id (int | Unset): The unique identifier of the project where you want to copy.
        target_wbs_object_id (int | Unset): The unique identifier of the WBS where you want to copy.
        target_activity_id (str | Unset): The unique identifier of the target activity
        copy_resource_and_role_assignments (bool | Unset): Specifies whether ResourceAndRoleAssignments are to be copied
            into the new project.
        copy_relationships (bool | Unset): Specifies whether Relationships are to be copied into the new project.
        copy_activity_codes (bool | Unset): Specifies whether ActivityCodes are to be copied into the new project.
        copy_activity_notes (bool | Unset): Specifies whether ActivityNotes are to be copied into the new project.
        copy_activity_expenses (bool | Unset): Specifies whether ActivityExpenses are to be copied into the new project.
        copy_activity_steps (bool | Unset): Specifies whether ActivitySteps are to be copied into the new project.
        copy_project_documents (bool | Unset): Specifies whether ProjectDocuments are to be copied into the new project.
        copy_past_period_actuals (bool | Unset): Specifies whether PastPeriodActuals are to be copied into the new
            project.
        copy_assignment_codes (bool | Unset): Specifies whether AssignmentCodes are to be copied into the new project.
        copy_assignment_secure_codes (bool | Unset): Specifies whether AssignmentSecureCodes are to be copied into the
            new project.
        copy_activity_secure_codes (bool | Unset): Specifies whether ActivitySecureCodes are to be copied into the new
            project.
    """

    object_id: int | Unset = UNSET
    target_project_object_id: int | Unset = UNSET
    target_wbs_object_id: int | Unset = UNSET
    target_activity_id: str | Unset = UNSET
    copy_resource_and_role_assignments: bool | Unset = UNSET
    copy_relationships: bool | Unset = UNSET
    copy_activity_codes: bool | Unset = UNSET
    copy_activity_notes: bool | Unset = UNSET
    copy_activity_expenses: bool | Unset = UNSET
    copy_activity_steps: bool | Unset = UNSET
    copy_project_documents: bool | Unset = UNSET
    copy_past_period_actuals: bool | Unset = UNSET
    copy_assignment_codes: bool | Unset = UNSET
    copy_assignment_secure_codes: bool | Unset = UNSET
    copy_activity_secure_codes: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_id = self.object_id

        target_project_object_id = self.target_project_object_id

        target_wbs_object_id = self.target_wbs_object_id

        target_activity_id = self.target_activity_id

        copy_resource_and_role_assignments = self.copy_resource_and_role_assignments

        copy_relationships = self.copy_relationships

        copy_activity_codes = self.copy_activity_codes

        copy_activity_notes = self.copy_activity_notes

        copy_activity_expenses = self.copy_activity_expenses

        copy_activity_steps = self.copy_activity_steps

        copy_project_documents = self.copy_project_documents

        copy_past_period_actuals = self.copy_past_period_actuals

        copy_assignment_codes = self.copy_assignment_codes

        copy_assignment_secure_codes = self.copy_assignment_secure_codes

        copy_activity_secure_codes = self.copy_activity_secure_codes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_id is not UNSET:
            field_dict["ObjectId"] = object_id
        if target_project_object_id is not UNSET:
            field_dict["TargetProjectObjectId"] = target_project_object_id
        if target_wbs_object_id is not UNSET:
            field_dict["TargetWBSObjectId"] = target_wbs_object_id
        if target_activity_id is not UNSET:
            field_dict["TargetActivityId"] = target_activity_id
        if copy_resource_and_role_assignments is not UNSET:
            field_dict["CopyResourceAndRoleAssignments"] = copy_resource_and_role_assignments
        if copy_relationships is not UNSET:
            field_dict["CopyRelationships"] = copy_relationships
        if copy_activity_codes is not UNSET:
            field_dict["CopyActivityCodes"] = copy_activity_codes
        if copy_activity_notes is not UNSET:
            field_dict["CopyActivityNotes"] = copy_activity_notes
        if copy_activity_expenses is not UNSET:
            field_dict["CopyActivityExpenses"] = copy_activity_expenses
        if copy_activity_steps is not UNSET:
            field_dict["CopyActivitySteps"] = copy_activity_steps
        if copy_project_documents is not UNSET:
            field_dict["CopyProjectDocuments"] = copy_project_documents
        if copy_past_period_actuals is not UNSET:
            field_dict["CopyPastPeriodActuals"] = copy_past_period_actuals
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

        target_project_object_id = d.pop("TargetProjectObjectId", UNSET)

        target_wbs_object_id = d.pop("TargetWBSObjectId", UNSET)

        target_activity_id = d.pop("TargetActivityId", UNSET)

        copy_resource_and_role_assignments = d.pop("CopyResourceAndRoleAssignments", UNSET)

        copy_relationships = d.pop("CopyRelationships", UNSET)

        copy_activity_codes = d.pop("CopyActivityCodes", UNSET)

        copy_activity_notes = d.pop("CopyActivityNotes", UNSET)

        copy_activity_expenses = d.pop("CopyActivityExpenses", UNSET)

        copy_activity_steps = d.pop("CopyActivitySteps", UNSET)

        copy_project_documents = d.pop("CopyProjectDocuments", UNSET)

        copy_past_period_actuals = d.pop("CopyPastPeriodActuals", UNSET)

        copy_assignment_codes = d.pop("CopyAssignmentCodes", UNSET)

        copy_assignment_secure_codes = d.pop("CopyAssignmentSecureCodes", UNSET)

        copy_activity_secure_codes = d.pop("CopyActivitySecureCodes", UNSET)

        copy_activity = cls(
            object_id=object_id,
            target_project_object_id=target_project_object_id,
            target_wbs_object_id=target_wbs_object_id,
            target_activity_id=target_activity_id,
            copy_resource_and_role_assignments=copy_resource_and_role_assignments,
            copy_relationships=copy_relationships,
            copy_activity_codes=copy_activity_codes,
            copy_activity_notes=copy_activity_notes,
            copy_activity_expenses=copy_activity_expenses,
            copy_activity_steps=copy_activity_steps,
            copy_project_documents=copy_project_documents,
            copy_past_period_actuals=copy_past_period_actuals,
            copy_assignment_codes=copy_assignment_codes,
            copy_assignment_secure_codes=copy_assignment_secure_codes,
            copy_activity_secure_codes=copy_activity_secure_codes,
        )

        copy_activity.additional_properties = d
        return copy_activity

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
