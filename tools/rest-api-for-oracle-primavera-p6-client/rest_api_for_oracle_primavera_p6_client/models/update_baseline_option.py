from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBaselineOption")


@_attrs_define
class UpdateBaselineOption:
    """UpdateBaselineOption Entity

    Attributes:
        object_id (int): The unique ID of the associated user.
        activities_filter (str | Unset): The option used to update activity IDs of the selected filter when updating the
            baseline.
        activities_filter_logic (str | Unset): The option used to update activity filter logic when updating the
            baseline.
        activity_code_assignments (bool | Unset): The option used to update activity code assignments when updating the
            baseline.
        activity_filter_id (str | Unset): The option used to update activity filter id when updating the baseline.
        activity_filter_name (str | Unset): The option used to update activity filter name when updating the baseline.
        activity_information (bool | Unset): The option used to update activity information for existing resource and
            role assignments when updating the baseline.
        activity_notebooks (bool | Unset): The option used to update activity information for existing resource and role
            assignments when updating the baseline.
        activity_rsrc_assignment_codes (bool | Unset):
        activity_rsrc_assignment_udfs (bool | Unset): The option used to update activity resource assignment UDFs when
            updating the baseline.
        activity_udfs (bool | Unset): The option used to update activity UDFs when updating the baseline
        actual_units_cost_wo_rsrc_assignmnt (bool | Unset): The option used to update activity actual units and cost
            without resource assignments when updating the baseline.
        add_new_activities_data (bool | Unset): The option used to add new activities with data when updating the
            baseline.
        add_new_rsrc_role (bool | Unset): The option used to add new resource and role assignments when updating the
            baseline.
        all_activities (bool | Unset): The option used to include all activities when updating the baseline.
        batch_mode_enabled (bool | Unset): The option used to enable the batch update mode when updating the baseline.
        budget_units_cost (bool | Unset): The option used to update budget units and cost for existing resource and role
            assignments when updating the baseline.
        budget_units_cost_wo_rsrc_assignmnt (bool | Unset): The option used to update activity budget units and cost
            without resource assignment when updating the baseline.
        constraints (bool | Unset): The option used to update activity constraints when updating the baseline
        dates_duration_datadates (bool | Unset): The option used to update activity dates, duration, and data dates when
            updating the baseline
        delete_non_existing_activities (bool | Unset): The option used to delete non existing activities when updating
            the baseline.
        expense_udfs (bool | Unset): the option used to update activity expense UDFs when updating the baseline.
        expenses (bool | Unset): The option used to update activity expenses when updating the baseline.
        filtered_activities (bool | Unset): The option used to include activities in the selected folder when updating
            the baseline.
        general_activiti_info (bool | Unset): The option used to update general activity info when updating the
            baseline.
        ignore_last_update_date (bool | Unset): The option used to ignore LastUpdateDate when updating the baseline.
        issue_ud_fs (bool | Unset): The option used to update the Issue UDFs when updating the baseline.
        new_activity_information (bool | Unset):
        new_budget_units_cost (bool | Unset):
        project_details (bool | Unset): The option used to update the project details when updating the baseline.
        project_risks_issues_and_thresholds (bool | Unset): The option used to update the Project Risks Issues and
            Thresholds when updating the baseline.
        project_ud_fs (bool | Unset): The option used to update the project UDFs when updating the baseline.
        relationships (bool | Unset): The option used to update activity relationships when updating the baseline.
        risk_assignments (bool | Unset): The option used to update risk assignments when updating the baseline.
        risk_ud_fs (bool | Unset): The option used to update the Risks UDFs when updating the baseline.
        steps (bool | Unset): The option used to update activity steps when updating the baseline.
        steps_udf (bool | Unset): The option used to update activity steps UDFs when updating the baseline.
        update_exist_rsrc_role_assignment (bool | Unset): The option used to update existing resource and role
            assignments when updating the baseline.
        update_existing_activities (bool | Unset): The option used to update existing activities when updating the
            baseline.
        user_name (str | Unset): The user's login name.
        wp_document_ud_fs (bool | Unset): The option used to update the WPDocument UDFs when updating the baseline.
        wbs_assignments (bool | Unset): The option used to update WBS assignments when updating the baseline.
        wbs_ud_fs (bool | Unset): The option used to update the WBS UDFs when updating the baseline.
        work_products_and_documents (bool | Unset): The option used to update the work products and documents when
            updating the baseline.
    """

    object_id: int
    activities_filter: str | Unset = UNSET
    activities_filter_logic: str | Unset = UNSET
    activity_code_assignments: bool | Unset = UNSET
    activity_filter_id: str | Unset = UNSET
    activity_filter_name: str | Unset = UNSET
    activity_information: bool | Unset = UNSET
    activity_notebooks: bool | Unset = UNSET
    activity_rsrc_assignment_codes: bool | Unset = UNSET
    activity_rsrc_assignment_udfs: bool | Unset = UNSET
    activity_udfs: bool | Unset = UNSET
    actual_units_cost_wo_rsrc_assignmnt: bool | Unset = UNSET
    add_new_activities_data: bool | Unset = UNSET
    add_new_rsrc_role: bool | Unset = UNSET
    all_activities: bool | Unset = UNSET
    batch_mode_enabled: bool | Unset = UNSET
    budget_units_cost: bool | Unset = UNSET
    budget_units_cost_wo_rsrc_assignmnt: bool | Unset = UNSET
    constraints: bool | Unset = UNSET
    dates_duration_datadates: bool | Unset = UNSET
    delete_non_existing_activities: bool | Unset = UNSET
    expense_udfs: bool | Unset = UNSET
    expenses: bool | Unset = UNSET
    filtered_activities: bool | Unset = UNSET
    general_activiti_info: bool | Unset = UNSET
    ignore_last_update_date: bool | Unset = UNSET
    issue_ud_fs: bool | Unset = UNSET
    new_activity_information: bool | Unset = UNSET
    new_budget_units_cost: bool | Unset = UNSET
    project_details: bool | Unset = UNSET
    project_risks_issues_and_thresholds: bool | Unset = UNSET
    project_ud_fs: bool | Unset = UNSET
    relationships: bool | Unset = UNSET
    risk_assignments: bool | Unset = UNSET
    risk_ud_fs: bool | Unset = UNSET
    steps: bool | Unset = UNSET
    steps_udf: bool | Unset = UNSET
    update_exist_rsrc_role_assignment: bool | Unset = UNSET
    update_existing_activities: bool | Unset = UNSET
    user_name: str | Unset = UNSET
    wp_document_ud_fs: bool | Unset = UNSET
    wbs_assignments: bool | Unset = UNSET
    wbs_ud_fs: bool | Unset = UNSET
    work_products_and_documents: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_id = self.object_id

        activities_filter = self.activities_filter

        activities_filter_logic = self.activities_filter_logic

        activity_code_assignments = self.activity_code_assignments

        activity_filter_id = self.activity_filter_id

        activity_filter_name = self.activity_filter_name

        activity_information = self.activity_information

        activity_notebooks = self.activity_notebooks

        activity_rsrc_assignment_codes = self.activity_rsrc_assignment_codes

        activity_rsrc_assignment_udfs = self.activity_rsrc_assignment_udfs

        activity_udfs = self.activity_udfs

        actual_units_cost_wo_rsrc_assignmnt = self.actual_units_cost_wo_rsrc_assignmnt

        add_new_activities_data = self.add_new_activities_data

        add_new_rsrc_role = self.add_new_rsrc_role

        all_activities = self.all_activities

        batch_mode_enabled = self.batch_mode_enabled

        budget_units_cost = self.budget_units_cost

        budget_units_cost_wo_rsrc_assignmnt = self.budget_units_cost_wo_rsrc_assignmnt

        constraints = self.constraints

        dates_duration_datadates = self.dates_duration_datadates

        delete_non_existing_activities = self.delete_non_existing_activities

        expense_udfs = self.expense_udfs

        expenses = self.expenses

        filtered_activities = self.filtered_activities

        general_activiti_info = self.general_activiti_info

        ignore_last_update_date = self.ignore_last_update_date

        issue_ud_fs = self.issue_ud_fs

        new_activity_information = self.new_activity_information

        new_budget_units_cost = self.new_budget_units_cost

        project_details = self.project_details

        project_risks_issues_and_thresholds = self.project_risks_issues_and_thresholds

        project_ud_fs = self.project_ud_fs

        relationships = self.relationships

        risk_assignments = self.risk_assignments

        risk_ud_fs = self.risk_ud_fs

        steps = self.steps

        steps_udf = self.steps_udf

        update_exist_rsrc_role_assignment = self.update_exist_rsrc_role_assignment

        update_existing_activities = self.update_existing_activities

        user_name = self.user_name

        wp_document_ud_fs = self.wp_document_ud_fs

        wbs_assignments = self.wbs_assignments

        wbs_ud_fs = self.wbs_ud_fs

        work_products_and_documents = self.work_products_and_documents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ObjectId": object_id,
            }
        )
        if activities_filter is not UNSET:
            field_dict["ActivitiesFilter"] = activities_filter
        if activities_filter_logic is not UNSET:
            field_dict["ActivitiesFilterLogic"] = activities_filter_logic
        if activity_code_assignments is not UNSET:
            field_dict["ActivityCodeAssignments"] = activity_code_assignments
        if activity_filter_id is not UNSET:
            field_dict["ActivityFilterId"] = activity_filter_id
        if activity_filter_name is not UNSET:
            field_dict["ActivityFilterName"] = activity_filter_name
        if activity_information is not UNSET:
            field_dict["ActivityInformation"] = activity_information
        if activity_notebooks is not UNSET:
            field_dict["ActivityNotebooks"] = activity_notebooks
        if activity_rsrc_assignment_codes is not UNSET:
            field_dict["ActivityRsrcAssignmentCodes"] = activity_rsrc_assignment_codes
        if activity_rsrc_assignment_udfs is not UNSET:
            field_dict["ActivityRsrcAssignmentUdfs"] = activity_rsrc_assignment_udfs
        if activity_udfs is not UNSET:
            field_dict["ActivityUdfs"] = activity_udfs
        if actual_units_cost_wo_rsrc_assignmnt is not UNSET:
            field_dict["ActualUnitsCostWoRsrcAssignmnt"] = actual_units_cost_wo_rsrc_assignmnt
        if add_new_activities_data is not UNSET:
            field_dict["AddNewActivitiesData"] = add_new_activities_data
        if add_new_rsrc_role is not UNSET:
            field_dict["AddNewRsrcRole"] = add_new_rsrc_role
        if all_activities is not UNSET:
            field_dict["AllActivities"] = all_activities
        if batch_mode_enabled is not UNSET:
            field_dict["BatchModeEnabled"] = batch_mode_enabled
        if budget_units_cost is not UNSET:
            field_dict["BudgetUnitsCost"] = budget_units_cost
        if budget_units_cost_wo_rsrc_assignmnt is not UNSET:
            field_dict["BudgetUnitsCostWoRsrcAssignmnt"] = budget_units_cost_wo_rsrc_assignmnt
        if constraints is not UNSET:
            field_dict["Constraints"] = constraints
        if dates_duration_datadates is not UNSET:
            field_dict["DatesDurationDatadates"] = dates_duration_datadates
        if delete_non_existing_activities is not UNSET:
            field_dict["DeleteNonExistingActivities"] = delete_non_existing_activities
        if expense_udfs is not UNSET:
            field_dict["ExpenseUdfs"] = expense_udfs
        if expenses is not UNSET:
            field_dict["Expenses"] = expenses
        if filtered_activities is not UNSET:
            field_dict["FilteredActivities"] = filtered_activities
        if general_activiti_info is not UNSET:
            field_dict["GeneralActivitiInfo"] = general_activiti_info
        if ignore_last_update_date is not UNSET:
            field_dict["IgnoreLastUpdateDate"] = ignore_last_update_date
        if issue_ud_fs is not UNSET:
            field_dict["IssueUDFs"] = issue_ud_fs
        if new_activity_information is not UNSET:
            field_dict["NewActivityInformation"] = new_activity_information
        if new_budget_units_cost is not UNSET:
            field_dict["NewBudgetUnitsCost"] = new_budget_units_cost
        if project_details is not UNSET:
            field_dict["ProjectDetails"] = project_details
        if project_risks_issues_and_thresholds is not UNSET:
            field_dict["ProjectRisksIssuesAndThresholds"] = project_risks_issues_and_thresholds
        if project_ud_fs is not UNSET:
            field_dict["ProjectUDFs"] = project_ud_fs
        if relationships is not UNSET:
            field_dict["Relationships"] = relationships
        if risk_assignments is not UNSET:
            field_dict["RiskAssignments"] = risk_assignments
        if risk_ud_fs is not UNSET:
            field_dict["RiskUDFs"] = risk_ud_fs
        if steps is not UNSET:
            field_dict["Steps"] = steps
        if steps_udf is not UNSET:
            field_dict["StepsUdf"] = steps_udf
        if update_exist_rsrc_role_assignment is not UNSET:
            field_dict["UpdateExistRsrcRoleAssignment"] = update_exist_rsrc_role_assignment
        if update_existing_activities is not UNSET:
            field_dict["UpdateExistingActivities"] = update_existing_activities
        if user_name is not UNSET:
            field_dict["UserName"] = user_name
        if wp_document_ud_fs is not UNSET:
            field_dict["WPDocumentUDFs"] = wp_document_ud_fs
        if wbs_assignments is not UNSET:
            field_dict["WbsAssignments"] = wbs_assignments
        if wbs_ud_fs is not UNSET:
            field_dict["WbsUDFs"] = wbs_ud_fs
        if work_products_and_documents is not UNSET:
            field_dict["WorkProductsAndDocuments"] = work_products_and_documents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_id = d.pop("ObjectId")

        activities_filter = d.pop("ActivitiesFilter", UNSET)

        activities_filter_logic = d.pop("ActivitiesFilterLogic", UNSET)

        activity_code_assignments = d.pop("ActivityCodeAssignments", UNSET)

        activity_filter_id = d.pop("ActivityFilterId", UNSET)

        activity_filter_name = d.pop("ActivityFilterName", UNSET)

        activity_information = d.pop("ActivityInformation", UNSET)

        activity_notebooks = d.pop("ActivityNotebooks", UNSET)

        activity_rsrc_assignment_codes = d.pop("ActivityRsrcAssignmentCodes", UNSET)

        activity_rsrc_assignment_udfs = d.pop("ActivityRsrcAssignmentUdfs", UNSET)

        activity_udfs = d.pop("ActivityUdfs", UNSET)

        actual_units_cost_wo_rsrc_assignmnt = d.pop("ActualUnitsCostWoRsrcAssignmnt", UNSET)

        add_new_activities_data = d.pop("AddNewActivitiesData", UNSET)

        add_new_rsrc_role = d.pop("AddNewRsrcRole", UNSET)

        all_activities = d.pop("AllActivities", UNSET)

        batch_mode_enabled = d.pop("BatchModeEnabled", UNSET)

        budget_units_cost = d.pop("BudgetUnitsCost", UNSET)

        budget_units_cost_wo_rsrc_assignmnt = d.pop("BudgetUnitsCostWoRsrcAssignmnt", UNSET)

        constraints = d.pop("Constraints", UNSET)

        dates_duration_datadates = d.pop("DatesDurationDatadates", UNSET)

        delete_non_existing_activities = d.pop("DeleteNonExistingActivities", UNSET)

        expense_udfs = d.pop("ExpenseUdfs", UNSET)

        expenses = d.pop("Expenses", UNSET)

        filtered_activities = d.pop("FilteredActivities", UNSET)

        general_activiti_info = d.pop("GeneralActivitiInfo", UNSET)

        ignore_last_update_date = d.pop("IgnoreLastUpdateDate", UNSET)

        issue_ud_fs = d.pop("IssueUDFs", UNSET)

        new_activity_information = d.pop("NewActivityInformation", UNSET)

        new_budget_units_cost = d.pop("NewBudgetUnitsCost", UNSET)

        project_details = d.pop("ProjectDetails", UNSET)

        project_risks_issues_and_thresholds = d.pop("ProjectRisksIssuesAndThresholds", UNSET)

        project_ud_fs = d.pop("ProjectUDFs", UNSET)

        relationships = d.pop("Relationships", UNSET)

        risk_assignments = d.pop("RiskAssignments", UNSET)

        risk_ud_fs = d.pop("RiskUDFs", UNSET)

        steps = d.pop("Steps", UNSET)

        steps_udf = d.pop("StepsUdf", UNSET)

        update_exist_rsrc_role_assignment = d.pop("UpdateExistRsrcRoleAssignment", UNSET)

        update_existing_activities = d.pop("UpdateExistingActivities", UNSET)

        user_name = d.pop("UserName", UNSET)

        wp_document_ud_fs = d.pop("WPDocumentUDFs", UNSET)

        wbs_assignments = d.pop("WbsAssignments", UNSET)

        wbs_ud_fs = d.pop("WbsUDFs", UNSET)

        work_products_and_documents = d.pop("WorkProductsAndDocuments", UNSET)

        update_baseline_option = cls(
            object_id=object_id,
            activities_filter=activities_filter,
            activities_filter_logic=activities_filter_logic,
            activity_code_assignments=activity_code_assignments,
            activity_filter_id=activity_filter_id,
            activity_filter_name=activity_filter_name,
            activity_information=activity_information,
            activity_notebooks=activity_notebooks,
            activity_rsrc_assignment_codes=activity_rsrc_assignment_codes,
            activity_rsrc_assignment_udfs=activity_rsrc_assignment_udfs,
            activity_udfs=activity_udfs,
            actual_units_cost_wo_rsrc_assignmnt=actual_units_cost_wo_rsrc_assignmnt,
            add_new_activities_data=add_new_activities_data,
            add_new_rsrc_role=add_new_rsrc_role,
            all_activities=all_activities,
            batch_mode_enabled=batch_mode_enabled,
            budget_units_cost=budget_units_cost,
            budget_units_cost_wo_rsrc_assignmnt=budget_units_cost_wo_rsrc_assignmnt,
            constraints=constraints,
            dates_duration_datadates=dates_duration_datadates,
            delete_non_existing_activities=delete_non_existing_activities,
            expense_udfs=expense_udfs,
            expenses=expenses,
            filtered_activities=filtered_activities,
            general_activiti_info=general_activiti_info,
            ignore_last_update_date=ignore_last_update_date,
            issue_ud_fs=issue_ud_fs,
            new_activity_information=new_activity_information,
            new_budget_units_cost=new_budget_units_cost,
            project_details=project_details,
            project_risks_issues_and_thresholds=project_risks_issues_and_thresholds,
            project_ud_fs=project_ud_fs,
            relationships=relationships,
            risk_assignments=risk_assignments,
            risk_ud_fs=risk_ud_fs,
            steps=steps,
            steps_udf=steps_udf,
            update_exist_rsrc_role_assignment=update_exist_rsrc_role_assignment,
            update_existing_activities=update_existing_activities,
            user_name=user_name,
            wp_document_ud_fs=wp_document_ud_fs,
            wbs_assignments=wbs_assignments,
            wbs_ud_fs=wbs_ud_fs,
            work_products_and_documents=work_products_and_documents,
        )

        update_baseline_option.additional_properties = d
        return update_baseline_option

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
