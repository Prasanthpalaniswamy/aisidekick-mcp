from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CopyProject")


@_attrs_define
class CopyProject:
    """CopyProject Entity

    Attributes:
        object_id (int | Unset): The unique identifier of the project you want to copy.
        copy_risks (bool | Unset): Specifies whether risks are to be copied into the new project.
        copy_issues_thresholds (bool | Unset): Specifies whether issues and thresholds are to be copied into the new
            project.
        copy_reports (bool | Unset): Specifies whether reports are to be copied into the new project.
        copy_project_documents (bool | Unset): Specifies whether project documents are to be copied into the new
            project.
        copy_funding_sources (bool | Unset): Specifies whether project funding sources are to be copied into the new
            project.
        copy_summary_data (bool | Unset): Specifies whether summary data is copied into the new project. Summary Data is
            created by calling the SummarizeProject Operation of the Job service.
        copy_project_notes (bool | Unset): Specifies whether project notes are to be copied into the new project.
        copy_wbs_milestones (bool | Unset): Specifies whether WBS milestones are to be copied into the new project.
        copy_activities (bool | Unset): Specifies whether activities are to be copied into the new project.
        copy_activity_risks (bool | Unset): Specifies whether activity risk are to be copied into the new project.
        copy_high_level_resource_planning (bool | Unset): Specifies whether high level resource planning is to be copied
            into the new project.
        copy_resource_and_role_assignments (bool | Unset): Specifies whether resources and role assignments are to be
            copied into the new project.
        copy_assignment_codes (bool | Unset): Specifies whether assignment codes are to be copied into the new project.
        copy_assignment_secure_codes (bool | Unset): Specifies whether secure assignment codes are to be copied into the
            new project.
        copy_relationships (bool | Unset): Specifies whether relationships are to be copied into the new project.
        copy_only_between_copied_activities (bool | Unset): Setting the CopyOnlyBetweenCopiedActivities to true limits
            the copied relationships to those that are within the project (i.e. relationships between projects are not
            copied). This field only has an effect if the CopyRelationships field is set to true.
        copy_activity_expenses (bool | Unset): Specifies whether activity expenses are to be copied into the new
            project.
        copy_activity_codes (bool | Unset): Specifies whether activity codes are to be copied into the new project.
        copy_activity_secure_codes (bool | Unset): Specifies whether secure activity codes are to be copied into the new
            project.
        copy_activity_notes (bool | Unset): Specifies whether activity notes are to be copied into the new project.
        copy_activity_steps (bool | Unset): Specifies whether activity steps are to be copied into the new project.
        copy_past_period_actuals (bool | Unset): Specifies whether past period actuals are to be copied into the new
            project.
        copy_project_codes (bool | Unset): Specifies whether project codes are to be copied into the new project.
        copy_project_secure_codes (bool | Unset): Specifies secure project codes are to be copied into the new project.
        eps_object_id (int | Unset): The unique identifier of the destination EPS that you want the new project to be
            copied into.
    """

    object_id: int | Unset = UNSET
    copy_risks: bool | Unset = UNSET
    copy_issues_thresholds: bool | Unset = UNSET
    copy_reports: bool | Unset = UNSET
    copy_project_documents: bool | Unset = UNSET
    copy_funding_sources: bool | Unset = UNSET
    copy_summary_data: bool | Unset = UNSET
    copy_project_notes: bool | Unset = UNSET
    copy_wbs_milestones: bool | Unset = UNSET
    copy_activities: bool | Unset = UNSET
    copy_activity_risks: bool | Unset = UNSET
    copy_high_level_resource_planning: bool | Unset = UNSET
    copy_resource_and_role_assignments: bool | Unset = UNSET
    copy_assignment_codes: bool | Unset = UNSET
    copy_assignment_secure_codes: bool | Unset = UNSET
    copy_relationships: bool | Unset = UNSET
    copy_only_between_copied_activities: bool | Unset = UNSET
    copy_activity_expenses: bool | Unset = UNSET
    copy_activity_codes: bool | Unset = UNSET
    copy_activity_secure_codes: bool | Unset = UNSET
    copy_activity_notes: bool | Unset = UNSET
    copy_activity_steps: bool | Unset = UNSET
    copy_past_period_actuals: bool | Unset = UNSET
    copy_project_codes: bool | Unset = UNSET
    copy_project_secure_codes: bool | Unset = UNSET
    eps_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_id = self.object_id

        copy_risks = self.copy_risks

        copy_issues_thresholds = self.copy_issues_thresholds

        copy_reports = self.copy_reports

        copy_project_documents = self.copy_project_documents

        copy_funding_sources = self.copy_funding_sources

        copy_summary_data = self.copy_summary_data

        copy_project_notes = self.copy_project_notes

        copy_wbs_milestones = self.copy_wbs_milestones

        copy_activities = self.copy_activities

        copy_activity_risks = self.copy_activity_risks

        copy_high_level_resource_planning = self.copy_high_level_resource_planning

        copy_resource_and_role_assignments = self.copy_resource_and_role_assignments

        copy_assignment_codes = self.copy_assignment_codes

        copy_assignment_secure_codes = self.copy_assignment_secure_codes

        copy_relationships = self.copy_relationships

        copy_only_between_copied_activities = self.copy_only_between_copied_activities

        copy_activity_expenses = self.copy_activity_expenses

        copy_activity_codes = self.copy_activity_codes

        copy_activity_secure_codes = self.copy_activity_secure_codes

        copy_activity_notes = self.copy_activity_notes

        copy_activity_steps = self.copy_activity_steps

        copy_past_period_actuals = self.copy_past_period_actuals

        copy_project_codes = self.copy_project_codes

        copy_project_secure_codes = self.copy_project_secure_codes

        eps_object_id = self.eps_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if copy_wbs_milestones is not UNSET:
            field_dict["CopyWBSMilestones"] = copy_wbs_milestones
        if copy_activities is not UNSET:
            field_dict["CopyActivities"] = copy_activities
        if copy_activity_risks is not UNSET:
            field_dict["CopyActivityRisks"] = copy_activity_risks
        if copy_high_level_resource_planning is not UNSET:
            field_dict["CopyHighLevelResourcePlanning"] = copy_high_level_resource_planning
        if copy_resource_and_role_assignments is not UNSET:
            field_dict["CopyResourceAndRoleAssignments"] = copy_resource_and_role_assignments
        if copy_assignment_codes is not UNSET:
            field_dict["CopyAssignmentCodes"] = copy_assignment_codes
        if copy_assignment_secure_codes is not UNSET:
            field_dict["CopyAssignmentSecureCodes"] = copy_assignment_secure_codes
        if copy_relationships is not UNSET:
            field_dict["CopyRelationships"] = copy_relationships
        if copy_only_between_copied_activities is not UNSET:
            field_dict["CopyOnlyBetweenCopiedActivities"] = copy_only_between_copied_activities
        if copy_activity_expenses is not UNSET:
            field_dict["CopyActivityExpenses"] = copy_activity_expenses
        if copy_activity_codes is not UNSET:
            field_dict["CopyActivityCodes"] = copy_activity_codes
        if copy_activity_secure_codes is not UNSET:
            field_dict["CopyActivitySecureCodes"] = copy_activity_secure_codes
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
        if eps_object_id is not UNSET:
            field_dict["EPSObjectId"] = eps_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_id = d.pop("ObjectId", UNSET)

        copy_risks = d.pop("CopyRisks", UNSET)

        copy_issues_thresholds = d.pop("CopyIssuesThresholds", UNSET)

        copy_reports = d.pop("CopyReports", UNSET)

        copy_project_documents = d.pop("CopyProjectDocuments", UNSET)

        copy_funding_sources = d.pop("CopyFundingSources", UNSET)

        copy_summary_data = d.pop("CopySummaryData", UNSET)

        copy_project_notes = d.pop("CopyProjectNotes", UNSET)

        copy_wbs_milestones = d.pop("CopyWBSMilestones", UNSET)

        copy_activities = d.pop("CopyActivities", UNSET)

        copy_activity_risks = d.pop("CopyActivityRisks", UNSET)

        copy_high_level_resource_planning = d.pop("CopyHighLevelResourcePlanning", UNSET)

        copy_resource_and_role_assignments = d.pop("CopyResourceAndRoleAssignments", UNSET)

        copy_assignment_codes = d.pop("CopyAssignmentCodes", UNSET)

        copy_assignment_secure_codes = d.pop("CopyAssignmentSecureCodes", UNSET)

        copy_relationships = d.pop("CopyRelationships", UNSET)

        copy_only_between_copied_activities = d.pop("CopyOnlyBetweenCopiedActivities", UNSET)

        copy_activity_expenses = d.pop("CopyActivityExpenses", UNSET)

        copy_activity_codes = d.pop("CopyActivityCodes", UNSET)

        copy_activity_secure_codes = d.pop("CopyActivitySecureCodes", UNSET)

        copy_activity_notes = d.pop("CopyActivityNotes", UNSET)

        copy_activity_steps = d.pop("CopyActivitySteps", UNSET)

        copy_past_period_actuals = d.pop("CopyPastPeriodActuals", UNSET)

        copy_project_codes = d.pop("CopyProjectCodes", UNSET)

        copy_project_secure_codes = d.pop("CopyProjectSecureCodes", UNSET)

        eps_object_id = d.pop("EPSObjectId", UNSET)

        copy_project = cls(
            object_id=object_id,
            copy_risks=copy_risks,
            copy_issues_thresholds=copy_issues_thresholds,
            copy_reports=copy_reports,
            copy_project_documents=copy_project_documents,
            copy_funding_sources=copy_funding_sources,
            copy_summary_data=copy_summary_data,
            copy_project_notes=copy_project_notes,
            copy_wbs_milestones=copy_wbs_milestones,
            copy_activities=copy_activities,
            copy_activity_risks=copy_activity_risks,
            copy_high_level_resource_planning=copy_high_level_resource_planning,
            copy_resource_and_role_assignments=copy_resource_and_role_assignments,
            copy_assignment_codes=copy_assignment_codes,
            copy_assignment_secure_codes=copy_assignment_secure_codes,
            copy_relationships=copy_relationships,
            copy_only_between_copied_activities=copy_only_between_copied_activities,
            copy_activity_expenses=copy_activity_expenses,
            copy_activity_codes=copy_activity_codes,
            copy_activity_secure_codes=copy_activity_secure_codes,
            copy_activity_notes=copy_activity_notes,
            copy_activity_steps=copy_activity_steps,
            copy_past_period_actuals=copy_past_period_actuals,
            copy_project_codes=copy_project_codes,
            copy_project_secure_codes=copy_project_secure_codes,
            eps_object_id=eps_object_id,
        )

        copy_project.additional_properties = d
        return copy_project

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
