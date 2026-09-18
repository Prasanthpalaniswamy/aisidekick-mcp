"""Contains all the data models used in inputs/outputs"""

from .activity import Activity
from .activity_code import ActivityCode
from .activity_code_assignment import ActivityCodeAssignment
from .activity_code_export import ActivityCodeExport
from .activity_code_export_field_item import ActivityCodeExportFieldItem
from .activity_code_type import ActivityCodeType
from .activity_comment import ActivityComment
from .activity_expense import ActivityExpense
from .activity_expense_field_item import ActivityExpenseFieldItem
from .activity_filter import ActivityFilter
from .activity_note import ActivityNote
from .activity_note_field_item import ActivityNoteFieldItem
from .activity_owner import ActivityOwner
from .activity_period_actual import ActivityPeriodActual
from .activity_risk import ActivityRisk
from .activity_spread_period import ActivitySpreadPeriod
from .activity_step import ActivityStep
from .activity_step_template import ActivityStepTemplate
from .activity_step_template_item import ActivityStepTemplateItem
from .add_projects_response import AddProjectsResponse
from .add_resources_response import AddResourcesResponse
from .add_roles_response import AddRolesResponse
from .add_shift_period_response import AddShiftPeriodResponse
from .apply_actuals import ApplyActuals
from .assign_project_as_baseline_response import AssignProjectAsBaselineResponse
from .async_asap_import_project import AsyncASAPImportProject
from .baseline_project import BaselineProject
from .baseline_type import BaselineType
from .business_object_options import BusinessObjectOptions
from .business_object_type import BusinessObjectType
from .business_object_type_import_option import BusinessObjectTypeImportOption
from .calculate_project_score_response import CalculateProjectScoreResponse
from .calendar import Calendar
from .cancel_job import CancelJob
from .cbs import CBS
from .cbs_duration_summary import CBSDurationSummary
from .cbs_expense_spread import CBSExpenseSpread
from .cbs_resource_spread import CBSResourceSpread
from .cbs_rsrc_expense_spread_period import CBSRsrcExpenseSpreadPeriod
from .checkin_document_body import CheckinDocumentBody
from .copy_activity import CopyActivity
from .copy_activity_response import CopyActivityResponse
from .copy_project import CopyProject
from .copy_project_as_baseline_response import CopyProjectAsBaselineResponse
from .copy_project_response import CopyProjectResponse
from .copy_wbs_from_template import CopyWBSFromTemplate
from .copy_wbs_from_template_response import CopyWBSFromTemplateResponse
from .cost_account import CostAccount
from .create_activity_code_assignments_response import CreateActivityCodeAssignmentsResponse
from .create_activity_risk_response import CreateActivityRiskResponse
from .create_copy_as_template import CreateCopyAsTemplate
from .create_copy_as_template_response import CreateCopyAsTemplateResponse
from .create_new_project import CreateNewProject
from .create_new_project_default_global_import_option import CreateNewProjectDefaultGlobalImportOption
from .create_new_project_default_project_specific_import_option import (
    CreateNewProjectDefaultProjectSpecificImportOption,
)
from .create_new_project_file_type import CreateNewProjectFileType
from .create_new_project_log_level import CreateNewProjectLogLevel
from .create_new_project_response import CreateNewProjectResponse
from .create_project_code_assignments_response import CreateProjectCodeAssignmentsResponse
from .create_project_from_template import CreateProjectFromTemplate
from .create_project_from_template_response import CreateProjectFromTemplateResponse
from .create_project_resource_quantity_response import CreateProjectResourceQuantityResponse
from .create_resource_access_response import CreateResourceAccessResponse
from .create_resource_assignment_code_assignments_response import CreateResourceAssignmentCodeAssignmentsResponse
from .create_resource_assignment_period_actuals_response import CreateResourceAssignmentPeriodActualsResponse
from .create_resource_assignment_update_response import CreateResourceAssignmentUpdateResponse
from .create_resource_code_assignments_response import CreateResourceCodeAssignmentsResponse
from .create_resource_role_response import CreateResourceRoleResponse
from .create_risk_impact_response import CreateRiskImpactResponse
from .create_risk_matrix_threshold_response import CreateRiskMatrixThresholdResponse
from .create_risk_response_action_impact_response import CreateRiskResponseActionImpactResponse
from .create_role_code_assignments_response import CreateRoleCodeAssignmentsResponse
from .create_timesheets_response import CreateTimesheetsResponse
from .create_udf_value_response import CreateUDFValueResponse
from .create_user_obs_response import CreateUserOBSResponse
from .currency import Currency
from .current_job_response import CurrentJobResponse
from .delete_activity_code_assignments import DeleteActivityCodeAssignments
from .delete_activity_period_actuals import DeleteActivityPeriodActuals
from .delete_activity_risks import DeleteActivityRisks
from .delete_project_code_assignments import DeleteProjectCodeAssignments
from .delete_project_resource_quantities import DeleteProjectResourceQuantities
from .delete_resource_access import DeleteResourceAccess
from .delete_resource_assignment_code_assignments import DeleteResourceAssignmentCodeAssignments
from .delete_resource_assignment_period_actuals import DeleteResourceAssignmentPeriodActuals
from .delete_resource_assignment_updates import DeleteResourceAssignmentUpdates
from .delete_resource_code_assignments import DeleteResourceCodeAssignments
from .delete_resource_roles import DeleteResourceRoles
from .delete_risk_impacts import DeleteRiskImpacts
from .delete_risk_matrix_thresholds import DeleteRiskMatrixThresholds
from .delete_risk_response_action_impacts import DeleteRiskResponseActionImpacts
from .delete_role_code_assignments import DeleteRoleCodeAssignments
from .delete_timesheets import DeleteTimesheets
from .delete_udf_values import DeleteUDFValues
from .delete_unreferenced_type import DeleteUnreferencedType
from .delete_unreferenced_type_import_option import DeleteUnreferencedTypeImportOption
from .delete_user_obs import DeleteUserOBS
from .delete_with_replacement_to import DeleteWithReplacementTO
from .document import Document
from .document_category import DocumentCategory
from .document_resource_response import DocumentResourceResponse
from .document_status_code import DocumentStatusCode
from .document_status_code_field_item import DocumentStatusCodeFieldItem
from .download_files import DownloadFiles
from .download_files_response import DownloadFilesResponse
from .eps import EPS
from .eps_budget_change_log import EPSBudgetChangeLog
from .eps_field_item import EPSFieldItem
from .eps_funding import EPSFunding
from .eps_note import EPSNote
from .eps_spending_plan import EPSSpendingPlan
from .expense_category import ExpenseCategory
from .expense_category_field_item import ExpenseCategoryFieldItem
from .expense_spread_period import ExpenseSpreadPeriod
from .export_doecpp_project import ExportDOECPPProject
from .export_ipmdar_project import ExportIpmdarProject
from .export_xer_project import ExportXERProject
from .export_xer_project_file_type_type import ExportXERProjectFileTypeType
from .financial_period import FinancialPeriod
from .form_data_content_disposition import FormDataContentDisposition
from .form_data_content_disposition_parameters import FormDataContentDispositionParameters
from .funding_source import FundingSource
from .funding_source_field_item import FundingSourceFieldItem
from .get_primary_baseline_project_response import GetPrimaryBaselineProjectResponse
from .get_project_object_ids_response import GetProjectObjectIdsResponse
from .get_resource_object_ids_response import GetResourceObjectIdsResponse
from .get_role_object_ids_response import GetRoleObjectIdsResponse
from .global_business_object_options import GlobalBusinessObjectOptions
from .global_preferences import GlobalPreferences
from .global_profile import GlobalProfile
from .global_replace import GlobalReplace
from .has_privilege_response import HasPrivilegeResponse
from .holiday_or_exception import HolidayOrException
from .holiday_or_exceptions import HolidayOrExceptions
from .import_create_new_project import ImportCreateNewProject
from .import_options_template import ImportOptionsTemplate
from .import_project import ImportProject
from .import_project_async_asap import ImportProjectAsyncASAP
from .import_project_async_asap_currencies_import_in_option import ImportProjectAsyncASAPCurrenciesImportInOption
from .import_project_async_asap_file_type import ImportProjectAsyncASAPFileType
from .import_project_async_asap_log_level import ImportProjectAsyncASAPLogLevel
from .import_project_async_asap_response import ImportProjectAsyncASAPResponse
from .import_project_import_option import ImportProjectImportOption
from .import_projects import ImportProjects
from .import_projects_currencies_import_in_option import ImportProjectsCurrenciesImportInOption
from .import_projects_default_global_import_option import ImportProjectsDefaultGlobalImportOption
from .import_projects_default_project_specific_import_option import ImportProjectsDefaultProjectSpecificImportOption
from .import_projects_file_type import ImportProjectsFileType
from .import_projects_log_level import ImportProjectsLogLevel
from .import_projects_response import ImportProjectsResponse
from .import_update_existing_project import ImportUpdateExistingProject
from .issue_history import IssueHistory
from .job_service import JobService
from .job_service_response import JobServiceResponse
from .lean_task import LeanTask
from .level import Level
from .load_activities_response import LoadActivitiesResponse
from .load_projects_response import LoadProjectsResponse
from .load_user_filtered_activities_response import LoadUserFilteredActivitiesResponse
from .load_user_filtered_milestone_activities_response import LoadUserFilteredMilestoneActivitiesResponse
from .location import Location
from .member_project import MemberProject
from .member_resource import MemberResource
from .member_role import MemberRole
from .msp_template import MSPTemplate
from .notebook_topic import NotebookTopic
from .obs import OBS
from .overhead_code import OverheadCode
from .p_audit_x import PAuditX
from .period import Period
from .privilege import Privilege
from .project import Project
from .project_budget_change_log import ProjectBudgetChangeLog
from .project_code import ProjectCode
from .project_code_assignment import ProjectCodeAssignment
from .project_code_field_item import ProjectCodeFieldItem
from .project_code_type import ProjectCodeType
from .project_code_type_field_item import ProjectCodeTypeFieldItem
from .project_deployment import ProjectDeployment
from .project_document import ProjectDocument
from .project_document_field_item import ProjectDocumentFieldItem
from .project_funding import ProjectFunding
from .project_funding_field_item import ProjectFundingFieldItem
from .project_issue import ProjectIssue
from .project_issue_field_item import ProjectIssueFieldItem
from .project_note import ProjectNote
from .project_note_field_item import ProjectNoteFieldItem
from .project_portfolio import ProjectPortfolio
from .project_profile import ProjectProfile
from .project_resource import ProjectResource
from .project_resource_category import ProjectResourceCategory
from .project_resource_quantity import ProjectResourceQuantity
from .project_specific_business_object_options import ProjectSpecificBusinessObjectOptions
from .project_spending_plan import ProjectSpendingPlan
from .project_threshold import ProjectThreshold
from .projects_import import ProjectsImport
from .publish import Publish
from .read_cbs_expense_spread_response import ReadCBSExpenseSpreadResponse
from .read_cbs_resource_spread_response import ReadCBSResourceSpreadResponse
from .read_eps_spread_response import ReadEPSSpreadResponse
from .read_job_log import ReadJobLog
from .read_job_log_response import ReadJobLogResponse
from .read_project_resource_spread_response import ReadProjectResourceSpreadResponse
from .read_project_role_spread_response import ReadProjectRoleSpreadResponse
from .read_project_spread_response import ReadProjectSpreadResponse
from .read_resource_assignment_spread_response import ReadResourceAssignmentSpreadResponse
from .read_wbs_expense_spread_response import ReadWBSExpenseSpreadResponse
from .read_wbs_resource_spread_response import ReadWBSResourceSpreadResponse
from .read_wbs_role_spread_response import ReadWBSRoleSpreadResponse
from .read_wbs_spread_response import ReadWBSSpreadResponse
from .recalculate_assignment_costs import RecalculateAssignmentCosts
from .relationship import Relationship
from .remove_all_shift_periods_response import RemoveAllShiftPeriodsResponse
from .remove_projects_response import RemoveProjectsResponse
from .remove_resources_response import RemoveResourcesResponse
from .remove_roles_response import RemoveRolesResponse
from .remove_shift_period_response import RemoveShiftPeriodResponse
from .resource import Resource
from .resource_access import ResourceAccess
from .resource_assignment import ResourceAssignment
from .resource_assignment_code import ResourceAssignmentCode
from .resource_assignment_code_assignment import ResourceAssignmentCodeAssignment
from .resource_assignment_code_type import ResourceAssignmentCodeType
from .resource_assignment_create import ResourceAssignmentCreate
from .resource_assignment_field_item import ResourceAssignmentFieldItem
from .resource_assignment_period_actual import ResourceAssignmentPeriodActual
from .resource_assignment_spread import ResourceAssignmentSpread
from .resource_assignment_spread_period import ResourceAssignmentSpreadPeriod
from .resource_assignment_update import ResourceAssignmentUpdate
from .resource_code import ResourceCode
from .resource_code_assignment import ResourceCodeAssignment
from .resource_code_field_item import ResourceCodeFieldItem
from .resource_code_type import ResourceCodeType
from .resource_curve import ResourceCurve
from .resource_hour import ResourceHour
from .resource_location import ResourceLocation
from .resource_rate import ResourceRate
from .resource_rate_field_item import ResourceRateFieldItem
from .resource_request import ResourceRequest
from .resource_request_criterion import ResourceRequestCriterion
from .resource_requests import ResourceRequests
from .resource_role import ResourceRole
from .resource_role_field_item import ResourceRoleFieldItem
from .resource_role_spread_period import ResourceRoleSpreadPeriod
from .resource_team import ResourceTeam
from .risk import Risk
from .risk_category import RiskCategory
from .risk_impact import RiskImpact
from .risk_impact_field_item import RiskImpactFieldItem
from .risk_matrix import RiskMatrix
from .risk_matrix_field_item import RiskMatrixFieldItem
from .risk_matrix_score import RiskMatrixScore
from .risk_matrix_score_field_item import RiskMatrixScoreFieldItem
from .risk_matrix_threshold import RiskMatrixThreshold
from .risk_matrix_threshold_field_item import RiskMatrixThresholdFieldItem
from .risk_response_action import RiskResponseAction
from .risk_response_action_field_item import RiskResponseActionFieldItem
from .risk_response_action_impact import RiskResponseActionImpact
from .risk_response_plan import RiskResponsePlan
from .risk_threshold import RiskThreshold
from .risk_threshold_level import RiskThresholdLevel
from .role import Role
from .role_code import RoleCode
from .role_code_assignment import RoleCodeAssignment
from .role_code_type import RoleCodeType
from .role_code_type_field_item import RoleCodeTypeFieldItem
from .role_field_item import RoleFieldItem
from .role_limit import RoleLimit
from .role_limit_field_item import RoleLimitFieldItem
from .role_rate import RoleRate
from .role_rate_field_item import RoleRateFieldItem
from .role_team import RoleTeam
from .schedule import Schedule
from .schedule_check import ScheduleCheck
from .schedule_check_option import ScheduleCheckOption
from .schedule_options import ScheduleOptions
from .send_to_unifier import SendToUnifier
from .set_detailed_work_hours import SetDetailedWorkHours
from .set_primary_baseline_project_response import SetPrimaryBaselineProjectResponse
from .set_standard_detailed_work_hours import SetStandardDetailedWorkHours
from .set_user_password_response import SetUserPasswordResponse
from .shift import Shift
from .shift_field_item import ShiftFieldItem
from .shift_period import ShiftPeriod
from .standard_work_hours import StandardWorkHours
from .standard_work_week import StandardWorkWeek
from .store_period_performance import StorePeriodPerformance
from .summarize_cbs import SummarizeCBS
from .summarize_eps import SummarizeEPS
from .summarize_project import SummarizeProject
from .summarized_spread_period import SummarizedSpreadPeriod
from .threshold_parameter import ThresholdParameter
from .threshold_parameter_field_item import ThresholdParameterFieldItem
from .timesheet import Timesheet
from .timesheet_audit import TimesheetAudit
from .timesheet_delegate import TimesheetDelegate
from .timesheet_period import TimesheetPeriod
from .udf_code import UDFCode
from .udf_type import UDFType
from .udf_value import UDFValue
from .unit_of_measure import UnitOfMeasure
from .update_baseline import UpdateBaseline
from .update_baseline_option import UpdateBaselineOption
from .update_currency import UpdateCurrency
from .update_existing_project import UpdateExistingProject
from .update_existing_project_default_global_import_option import UpdateExistingProjectDefaultGlobalImportOption
from .update_existing_project_default_project_specific_import_option import (
    UpdateExistingProjectDefaultProjectSpecificImportOption,
)
from .update_existing_project_file_type import UpdateExistingProjectFileType
from .update_existing_project_log_level import UpdateExistingProjectLogLevel
from .update_existing_project_response import UpdateExistingProjectResponse
from .update_resource_assignment_spread import UpdateResourceAssignmentSpread
from .upload_document_body import UploadDocumentBody
from .user import User
from .user_field_title import UserFieldTitle
from .user_interface_view import UserInterfaceView
from .user_license import UserLicense
from .user_obs import UserOBS
from .values import Values
from .wbs import WBS
from .wbs_category import WBSCategory
from .wbs_category_field_item import WBSCategoryFieldItem
from .wbs_field_item import WBSFieldItem
from .wbs_milestone import WBSMilestone
from .wbs_reviewers import WbsReviewers
from .work_time import WorkTime

__all__ = (
    "Activity",
    "ActivityCode",
    "ActivityCodeAssignment",
    "ActivityCodeExport",
    "ActivityCodeExportFieldItem",
    "ActivityCodeType",
    "ActivityComment",
    "ActivityExpense",
    "ActivityExpenseFieldItem",
    "ActivityFilter",
    "ActivityNote",
    "ActivityNoteFieldItem",
    "ActivityOwner",
    "ActivityPeriodActual",
    "ActivityRisk",
    "ActivitySpreadPeriod",
    "ActivityStep",
    "ActivityStepTemplate",
    "ActivityStepTemplateItem",
    "AddProjectsResponse",
    "AddResourcesResponse",
    "AddRolesResponse",
    "AddShiftPeriodResponse",
    "ApplyActuals",
    "AssignProjectAsBaselineResponse",
    "AsyncASAPImportProject",
    "BaselineProject",
    "BaselineType",
    "BusinessObjectOptions",
    "BusinessObjectType",
    "BusinessObjectTypeImportOption",
    "CalculateProjectScoreResponse",
    "Calendar",
    "CancelJob",
    "CBS",
    "CBSDurationSummary",
    "CBSExpenseSpread",
    "CBSResourceSpread",
    "CBSRsrcExpenseSpreadPeriod",
    "CheckinDocumentBody",
    "CopyActivity",
    "CopyActivityResponse",
    "CopyProject",
    "CopyProjectAsBaselineResponse",
    "CopyProjectResponse",
    "CopyWBSFromTemplate",
    "CopyWBSFromTemplateResponse",
    "CostAccount",
    "CreateActivityCodeAssignmentsResponse",
    "CreateActivityRiskResponse",
    "CreateCopyAsTemplate",
    "CreateCopyAsTemplateResponse",
    "CreateNewProject",
    "CreateNewProjectDefaultGlobalImportOption",
    "CreateNewProjectDefaultProjectSpecificImportOption",
    "CreateNewProjectFileType",
    "CreateNewProjectLogLevel",
    "CreateNewProjectResponse",
    "CreateProjectCodeAssignmentsResponse",
    "CreateProjectFromTemplate",
    "CreateProjectFromTemplateResponse",
    "CreateProjectResourceQuantityResponse",
    "CreateResourceAccessResponse",
    "CreateResourceAssignmentCodeAssignmentsResponse",
    "CreateResourceAssignmentPeriodActualsResponse",
    "CreateResourceAssignmentUpdateResponse",
    "CreateResourceCodeAssignmentsResponse",
    "CreateResourceRoleResponse",
    "CreateRiskImpactResponse",
    "CreateRiskMatrixThresholdResponse",
    "CreateRiskResponseActionImpactResponse",
    "CreateRoleCodeAssignmentsResponse",
    "CreateTimesheetsResponse",
    "CreateUDFValueResponse",
    "CreateUserOBSResponse",
    "Currency",
    "CurrentJobResponse",
    "DeleteActivityCodeAssignments",
    "DeleteActivityPeriodActuals",
    "DeleteActivityRisks",
    "DeleteProjectCodeAssignments",
    "DeleteProjectResourceQuantities",
    "DeleteResourceAccess",
    "DeleteResourceAssignmentCodeAssignments",
    "DeleteResourceAssignmentPeriodActuals",
    "DeleteResourceAssignmentUpdates",
    "DeleteResourceCodeAssignments",
    "DeleteResourceRoles",
    "DeleteRiskImpacts",
    "DeleteRiskMatrixThresholds",
    "DeleteRiskResponseActionImpacts",
    "DeleteRoleCodeAssignments",
    "DeleteTimesheets",
    "DeleteUDFValues",
    "DeleteUnreferencedType",
    "DeleteUnreferencedTypeImportOption",
    "DeleteUserOBS",
    "DeleteWithReplacementTO",
    "Document",
    "DocumentCategory",
    "DocumentResourceResponse",
    "DocumentStatusCode",
    "DocumentStatusCodeFieldItem",
    "DownloadFiles",
    "DownloadFilesResponse",
    "EPS",
    "EPSBudgetChangeLog",
    "EPSFieldItem",
    "EPSFunding",
    "EPSNote",
    "EPSSpendingPlan",
    "ExpenseCategory",
    "ExpenseCategoryFieldItem",
    "ExpenseSpreadPeriod",
    "ExportDOECPPProject",
    "ExportIpmdarProject",
    "ExportXERProject",
    "ExportXERProjectFileTypeType",
    "FinancialPeriod",
    "FormDataContentDisposition",
    "FormDataContentDispositionParameters",
    "FundingSource",
    "FundingSourceFieldItem",
    "GetPrimaryBaselineProjectResponse",
    "GetProjectObjectIdsResponse",
    "GetResourceObjectIdsResponse",
    "GetRoleObjectIdsResponse",
    "GlobalBusinessObjectOptions",
    "GlobalPreferences",
    "GlobalProfile",
    "GlobalReplace",
    "HasPrivilegeResponse",
    "HolidayOrException",
    "HolidayOrExceptions",
    "ImportCreateNewProject",
    "ImportOptionsTemplate",
    "ImportProject",
    "ImportProjectAsyncASAP",
    "ImportProjectAsyncASAPCurrenciesImportInOption",
    "ImportProjectAsyncASAPFileType",
    "ImportProjectAsyncASAPLogLevel",
    "ImportProjectAsyncASAPResponse",
    "ImportProjectImportOption",
    "ImportProjects",
    "ImportProjectsCurrenciesImportInOption",
    "ImportProjectsDefaultGlobalImportOption",
    "ImportProjectsDefaultProjectSpecificImportOption",
    "ImportProjectsFileType",
    "ImportProjectsLogLevel",
    "ImportProjectsResponse",
    "ImportUpdateExistingProject",
    "IssueHistory",
    "JobService",
    "JobServiceResponse",
    "LeanTask",
    "Level",
    "LoadActivitiesResponse",
    "LoadProjectsResponse",
    "LoadUserFilteredActivitiesResponse",
    "LoadUserFilteredMilestoneActivitiesResponse",
    "Location",
    "MemberProject",
    "MemberResource",
    "MemberRole",
    "MSPTemplate",
    "NotebookTopic",
    "OBS",
    "OverheadCode",
    "PAuditX",
    "Period",
    "Privilege",
    "Project",
    "ProjectBudgetChangeLog",
    "ProjectCode",
    "ProjectCodeAssignment",
    "ProjectCodeFieldItem",
    "ProjectCodeType",
    "ProjectCodeTypeFieldItem",
    "ProjectDeployment",
    "ProjectDocument",
    "ProjectDocumentFieldItem",
    "ProjectFunding",
    "ProjectFundingFieldItem",
    "ProjectIssue",
    "ProjectIssueFieldItem",
    "ProjectNote",
    "ProjectNoteFieldItem",
    "ProjectPortfolio",
    "ProjectProfile",
    "ProjectResource",
    "ProjectResourceCategory",
    "ProjectResourceQuantity",
    "ProjectsImport",
    "ProjectSpecificBusinessObjectOptions",
    "ProjectSpendingPlan",
    "ProjectThreshold",
    "Publish",
    "ReadCBSExpenseSpreadResponse",
    "ReadCBSResourceSpreadResponse",
    "ReadEPSSpreadResponse",
    "ReadJobLog",
    "ReadJobLogResponse",
    "ReadProjectResourceSpreadResponse",
    "ReadProjectRoleSpreadResponse",
    "ReadProjectSpreadResponse",
    "ReadResourceAssignmentSpreadResponse",
    "ReadWBSExpenseSpreadResponse",
    "ReadWBSResourceSpreadResponse",
    "ReadWBSRoleSpreadResponse",
    "ReadWBSSpreadResponse",
    "RecalculateAssignmentCosts",
    "Relationship",
    "RemoveAllShiftPeriodsResponse",
    "RemoveProjectsResponse",
    "RemoveResourcesResponse",
    "RemoveRolesResponse",
    "RemoveShiftPeriodResponse",
    "Resource",
    "ResourceAccess",
    "ResourceAssignment",
    "ResourceAssignmentCode",
    "ResourceAssignmentCodeAssignment",
    "ResourceAssignmentCodeType",
    "ResourceAssignmentCreate",
    "ResourceAssignmentFieldItem",
    "ResourceAssignmentPeriodActual",
    "ResourceAssignmentSpread",
    "ResourceAssignmentSpreadPeriod",
    "ResourceAssignmentUpdate",
    "ResourceCode",
    "ResourceCodeAssignment",
    "ResourceCodeFieldItem",
    "ResourceCodeType",
    "ResourceCurve",
    "ResourceHour",
    "ResourceLocation",
    "ResourceRate",
    "ResourceRateFieldItem",
    "ResourceRequest",
    "ResourceRequestCriterion",
    "ResourceRequests",
    "ResourceRole",
    "ResourceRoleFieldItem",
    "ResourceRoleSpreadPeriod",
    "ResourceTeam",
    "Risk",
    "RiskCategory",
    "RiskImpact",
    "RiskImpactFieldItem",
    "RiskMatrix",
    "RiskMatrixFieldItem",
    "RiskMatrixScore",
    "RiskMatrixScoreFieldItem",
    "RiskMatrixThreshold",
    "RiskMatrixThresholdFieldItem",
    "RiskResponseAction",
    "RiskResponseActionFieldItem",
    "RiskResponseActionImpact",
    "RiskResponsePlan",
    "RiskThreshold",
    "RiskThresholdLevel",
    "Role",
    "RoleCode",
    "RoleCodeAssignment",
    "RoleCodeType",
    "RoleCodeTypeFieldItem",
    "RoleFieldItem",
    "RoleLimit",
    "RoleLimitFieldItem",
    "RoleRate",
    "RoleRateFieldItem",
    "RoleTeam",
    "Schedule",
    "ScheduleCheck",
    "ScheduleCheckOption",
    "ScheduleOptions",
    "SendToUnifier",
    "SetDetailedWorkHours",
    "SetPrimaryBaselineProjectResponse",
    "SetStandardDetailedWorkHours",
    "SetUserPasswordResponse",
    "Shift",
    "ShiftFieldItem",
    "ShiftPeriod",
    "StandardWorkHours",
    "StandardWorkWeek",
    "StorePeriodPerformance",
    "SummarizeCBS",
    "SummarizedSpreadPeriod",
    "SummarizeEPS",
    "SummarizeProject",
    "ThresholdParameter",
    "ThresholdParameterFieldItem",
    "Timesheet",
    "TimesheetAudit",
    "TimesheetDelegate",
    "TimesheetPeriod",
    "UDFCode",
    "UDFType",
    "UDFValue",
    "UnitOfMeasure",
    "UpdateBaseline",
    "UpdateBaselineOption",
    "UpdateCurrency",
    "UpdateExistingProject",
    "UpdateExistingProjectDefaultGlobalImportOption",
    "UpdateExistingProjectDefaultProjectSpecificImportOption",
    "UpdateExistingProjectFileType",
    "UpdateExistingProjectLogLevel",
    "UpdateExistingProjectResponse",
    "UpdateResourceAssignmentSpread",
    "UploadDocumentBody",
    "User",
    "UserFieldTitle",
    "UserInterfaceView",
    "UserLicense",
    "UserOBS",
    "Values",
    "WBS",
    "WBSCategory",
    "WBSCategoryFieldItem",
    "WBSFieldItem",
    "WBSMilestone",
    "WbsReviewers",
    "WorkTime",
)
