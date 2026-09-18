from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCopyAsTemplate")


@_attrs_define
class CreateCopyAsTemplate:
    """CreateCopyAsTemplate Entity

    Attributes:
        eps_object_id (int): The unique ID of the EPS where the new project will reside.
        object_id (int | Unset): The unique ID of the project that you are using as the basis for the new template.
        copy_risks (bool | Unset): The flag that indicates whether Risks should be copied.
        copy_issues_thresholds (bool | Unset): The flag that indicates whether Issues Thresholds should be copied.
        copy_reports (bool | Unset): The flag that indicates whether Reports should be copied.
        copy_project_documents (bool | Unset): The flag that indicates whether ProjectDocuments should be copied.
        copy_funding_sources (bool | Unset): The flag that indicates whether FundingSources should be copied.
        copy_summary_data (bool | Unset): The flag that indicates whether SummaryData should be copied.
        copy_project_notes (bool | Unset): The flag that indicates whether ProjectNotes should be copied.
        copy_actual_to_planned_values (bool | Unset): The flag that indicates whether ActualToPlannedValues should be
            copied.
        copy_wbs_milestones (bool | Unset): The flag that indicates whether WBSMilestones should be copied.
        copy_activities (bool | Unset): The flag that indicates whether Activities should be copied.
        copy_high_level_resource_planning (bool | Unset): The flag that indicates whether HighLevelResourcePlanning
            should be copied.
        copy_resource_and_role_assignments (bool | Unset): The flag that indicates whether ResourceAndRoleAssignments
            should be copied.
        copy_relationships (bool | Unset): The flag that indicates whether Relationships should be copied.
        copy_only_between_copied_activities (bool | Unset): The flag that indicates whether OnlyBetweenCopiedActivities
            should be copied.
        copy_activity_expenses (bool | Unset): The flag that indicates whether ActivityExpenses should be copied.
        copy_activity_codes (bool | Unset): The flag that indicates whether ActivityCodes should be copied.
        copy_activity_notes (bool | Unset): The flag that indicates whether ActivityNotes should be copied.
        copy_activity_steps (bool | Unset): The flag that indicates whether ActivitySteps should be copied.
        copy_past_period_actuals (bool | Unset): The flag that indicates whether PastPeriodActuals should be copied.
        copy_project_codes (bool | Unset): The flag that indicates whether Project Codes should be copied.
        copy_project_secure_codes (bool | Unset): The flag that indicates whether Secure Project Codes should be copied.
        copy_assignment_codes (bool | Unset): The flag that indicates whether Assignment Codes should be copied.
        copy_assignment_secure_codes (bool | Unset): The flag that indicates whether Secure Assignment Codes should be
            copied.
        copy_activity_secure_codes (bool | Unset): The flag that indicates whether Secure Activity Codes should be
            copied.
    """

    eps_object_id: int
    object_id: int | Unset = UNSET
    copy_risks: bool | Unset = UNSET
    copy_issues_thresholds: bool | Unset = UNSET
    copy_reports: bool | Unset = UNSET
    copy_project_documents: bool | Unset = UNSET
    copy_funding_sources: bool | Unset = UNSET
    copy_summary_data: bool | Unset = UNSET
    copy_project_notes: bool | Unset = UNSET
    copy_actual_to_planned_values: bool | Unset = UNSET
    copy_wbs_milestones: bool | Unset = UNSET
    copy_activities: bool | Unset = UNSET
    copy_high_level_resource_planning: bool | Unset = UNSET
    copy_resource_and_role_assignments: bool | Unset = UNSET
    copy_relationships: bool | Unset = UNSET
    copy_only_between_copied_activities: bool | Unset = UNSET
    copy_activity_expenses: bool | Unset = UNSET
    copy_activity_codes: bool | Unset = UNSET
    copy_activity_notes: bool | Unset = UNSET
    copy_activity_steps: bool | Unset = UNSET
    copy_past_period_actuals: bool | Unset = UNSET
    copy_project_codes: bool | Unset = UNSET
    copy_project_secure_codes: bool | Unset = UNSET
    copy_assignment_codes: bool | Unset = UNSET
    copy_assignment_secure_codes: bool | Unset = UNSET
    copy_activity_secure_codes: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        eps_object_id = self.eps_object_id

        object_id = self.object_id

        copy_risks = self.copy_risks

        copy_issues_thresholds = self.copy_issues_thresholds

        copy_reports = self.copy_reports

        copy_project_documents = self.copy_project_documents

        copy_funding_sources = self.copy_funding_sources

        copy_summary_data = self.copy_summary_data

        copy_project_notes = self.copy_project_notes

        copy_actual_to_planned_values = self.copy_actual_to_planned_values

        copy_wbs_milestones = self.copy_wbs_milestones

        copy_activities = self.copy_activities

        copy_high_level_resource_planning = self.copy_high_level_resource_planning

        copy_resource_and_role_assignments = self.copy_resource_and_role_assignments

        copy_relationships = self.copy_relationships

        copy_only_between_copied_activities = self.copy_only_between_copied_activities

        copy_activity_expenses = self.copy_activity_expenses

        copy_activity_codes = self.copy_activity_codes

        copy_activity_notes = self.copy_activity_notes

        copy_activity_steps = self.copy_activity_steps

        copy_past_period_actuals = self.copy_past_period_actuals

        copy_project_codes = self.copy_project_codes

        copy_project_secure_codes = self.copy_project_secure_codes

        copy_assignment_codes = self.copy_assignment_codes

        copy_assignment_secure_codes = self.copy_assignment_secure_codes

        copy_activity_secure_codes = self.copy_activity_secure_codes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "EPSObjectId": eps_object_id,
            }
        )
        if object_id is not UNSET:
            field_dict["ObjectId"] = object_id
        if copy_risks is not UNSET:
            field_dict["CopyRisks"] = copy_risks
        if copy_issues_thresholds is not UNSET:
            field_dict["CopyIssuesThresholds"] = copy_issues_thresholds
        if copy_reports is not UNSET:
            field_dict["CopyReports"] = copy_reports
        if copy_project_documents is not UNSET:
            field_dict["CopyProjectDocuments"] = copy_project_documents
        if copy_funding_sources is not UNSET:
            field_dict["CopyFundingSources"] = copy_funding_sources
        if copy_summary_data is not UNSET:
            field_dict["CopySummaryData"] = copy_summary_data
        if copy_project_notes is not UNSET:
            field_dict["CopyProjectNotes"] = copy_project_notes
        if copy_actual_to_planned_values is not UNSET:
            field_dict["CopyActualToPlannedValues"] = copy_actual_to_planned_values
        if copy_wbs_milestones is not UNSET:
            field_dict["CopyWBSMilestones"] = copy_wbs_milestones
        if copy_activities is not UNSET:
            field_dict["CopyActivities"] = copy_activities
        if copy_high_level_resource_planning is not UNSET:
            field_dict["CopyHighLevelResourcePlanning"] = copy_high_level_resource_planning
        if copy_resource_and_role_assignments is not UNSET:
            field_dict["CopyResourceAndRoleAssignments"] = copy_resource_and_role_assignments
        if copy_relationships is not UNSET:
            field_dict["CopyRelationships"] = copy_relationships
        if copy_only_between_copied_activities is not UNSET:
            field_dict["CopyOnlyBetweenCopiedActivities"] = copy_only_between_copied_activities
        if copy_activity_expenses is not UNSET:
            field_dict["CopyActivityExpenses"] = copy_activity_expenses
        if copy_activity_codes is not UNSET:
            field_dict["CopyActivityCodes"] = copy_activity_codes
        if copy_activity_notes is not UNSET:
            field_dict["CopyActivityNotes"] = copy_activity_notes
        if copy_activity_steps is not UNSET:
            field_dict["CopyActivitySteps"] = copy_activity_steps
        if copy_past_period_actuals is not UNSET:
            field_dict["CopyPastPeriodActuals"] = copy_past_period_actuals
        if copy_project_codes is not UNSET:
            field_dict["CopyProjectCodes"] = copy_project_codes
        if copy_project_secure_codes is not UNSET:
            field_dict["CopyProjectSecureCodes"] = copy_project_secure_codes
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
        eps_object_id = d.pop("EPSObjectId")

        object_id = d.pop("ObjectId", UNSET)

        copy_risks = d.pop("CopyRisks", UNSET)

        copy_issues_thresholds = d.pop("CopyIssuesThresholds", UNSET)

        copy_reports = d.pop("CopyReports", UNSET)

        copy_project_documents = d.pop("CopyProjectDocuments", UNSET)

        copy_funding_sources = d.pop("CopyFundingSources", UNSET)

        copy_summary_data = d.pop("CopySummaryData", UNSET)

        copy_project_notes = d.pop("CopyProjectNotes", UNSET)

        copy_actual_to_planned_values = d.pop("CopyActualToPlannedValues", UNSET)

        copy_wbs_milestones = d.pop("CopyWBSMilestones", UNSET)

        copy_activities = d.pop("CopyActivities", UNSET)

        copy_high_level_resource_planning = d.pop("CopyHighLevelResourcePlanning", UNSET)

        copy_resource_and_role_assignments = d.pop("CopyResourceAndRoleAssignments", UNSET)

        copy_relationships = d.pop("CopyRelationships", UNSET)

        copy_only_between_copied_activities = d.pop("CopyOnlyBetweenCopiedActivities", UNSET)

        copy_activity_expenses = d.pop("CopyActivityExpenses", UNSET)

        copy_activity_codes = d.pop("CopyActivityCodes", UNSET)

        copy_activity_notes = d.pop("CopyActivityNotes", UNSET)

        copy_activity_steps = d.pop("CopyActivitySteps", UNSET)

        copy_past_period_actuals = d.pop("CopyPastPeriodActuals", UNSET)

        copy_project_codes = d.pop("CopyProjectCodes", UNSET)

        copy_project_secure_codes = d.pop("CopyProjectSecureCodes", UNSET)

        copy_assignment_codes = d.pop("CopyAssignmentCodes", UNSET)

        copy_assignment_secure_codes = d.pop("CopyAssignmentSecureCodes", UNSET)

        copy_activity_secure_codes = d.pop("CopyActivitySecureCodes", UNSET)

        create_copy_as_template = cls(
            eps_object_id=eps_object_id,
            object_id=object_id,
            copy_risks=copy_risks,
            copy_issues_thresholds=copy_issues_thresholds,
            copy_reports=copy_reports,
            copy_project_documents=copy_project_documents,
            copy_funding_sources=copy_funding_sources,
            copy_summary_data=copy_summary_data,
            copy_project_notes=copy_project_notes,
            copy_actual_to_planned_values=copy_actual_to_planned_values,
            copy_wbs_milestones=copy_wbs_milestones,
            copy_activities=copy_activities,
            copy_high_level_resource_planning=copy_high_level_resource_planning,
            copy_resource_and_role_assignments=copy_resource_and_role_assignments,
            copy_relationships=copy_relationships,
            copy_only_between_copied_activities=copy_only_between_copied_activities,
            copy_activity_expenses=copy_activity_expenses,
            copy_activity_codes=copy_activity_codes,
            copy_activity_notes=copy_activity_notes,
            copy_activity_steps=copy_activity_steps,
            copy_past_period_actuals=copy_past_period_actuals,
            copy_project_codes=copy_project_codes,
            copy_project_secure_codes=copy_project_secure_codes,
            copy_assignment_codes=copy_assignment_codes,
            copy_assignment_secure_codes=copy_assignment_secure_codes,
            copy_activity_secure_codes=copy_activity_secure_codes,
        )

        create_copy_as_template.additional_properties = d
        return create_copy_as_template

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
