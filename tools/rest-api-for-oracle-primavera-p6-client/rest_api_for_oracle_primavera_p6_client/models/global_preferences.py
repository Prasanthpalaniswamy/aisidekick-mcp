from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GlobalPreferences")


@_attrs_define
class GlobalPreferences:
    """GlobalPreferences Entity

    Attributes:
        allow_approved_ts_rejection (bool | Unset):
        always_launch_online_help (bool | Unset): The flag indicating that Online Help should be launched whenever a
            user accesses help.
        base_currency_object_id (int | Unset): The unique ID of the currency.
        contract_management_url (str | Unset): This is the URL of the Contract Management application.
        create_date (datetime.datetime | Unset): The date this global preferences was created.
        create_user (str | Unset): The name of the user that created this global preferences.
        custom_label_1 (str | Unset): The custom (user-defined) text that will be inserted into any report containing
            the Custom Label 1 global variable text cell, when printed.
        custom_label_2 (str | Unset): The custom (user-defined) text that will be inserted into any report containing
            the Custom Label 2 global variable text cell, when printed.
        custom_label_3 (str | Unset): The custom (user-defined) text that will be inserted into any report containing
            the Custom Label 3 global variable text cell, when printed.
        day_abbreviation (str | Unset): The abbreviation character for time periods of days. This abbreviation is used
            for displaying time units and durations in the user's selected display formats.
        default_duration (float | Unset): The planned duration assigned to new activities by default.
        default_timesheet_approval_manager (int | Unset): The unique ID of the resource manager assigned to approve
            timesheets for new resources by default.
        eppm_consent_message (str | Unset):
        eppm_enable_consent (str | Unset):
        ev_estimate_to_complete_factor (float | Unset): The user-defined performance factor, PF, for computing earned-
            value estimate-to-complete. ETC is computed as PF * ( BAC - earned value). This value is assigned to new
            projects by default. It can be modified for each project WBS element.
        ev_estimate_to_complete_technique (str | Unset): The technique for computing earned-value estimate-to-complete.
            This setting is assigned to new projects by default. It can be modified for each project WBS element.
        ev_performance_pct_complete_custom_pct (float | Unset): The user-defined percent complete for computing earned
            value for activities within the WBS. A value of, say, 25 means that 25% of the planned amount is earned when the
            activity is started and the remainder is earned when the activity is completed. This value is assigned to new
            projects by default. It can be modified for each project WBS element.
        ev_performance_pct_complete_technique (str | Unset): The technique used for computing earned-value percent
            complete. This setting is assigned to new projects by default. It can be modified for each project WBS element.
        earned_value_calculation (str | Unset): The flag indicating which values to use when calculating earned value
            when using a primary baseline. Valid values are 'At Completion Values with Current Dates', 'Planned Values with
            Planned Dates', and 'Planned Values with Current Dates'.
        email_notify_ts_rejection (bool | Unset):
        enable_password_policy (bool | Unset): The flag that indicates whether the password policy is enforced.
        enable_ts_audit (bool | Unset): The flag indicating whether to track timesheet submission, approval, and
            rejection. When you set this option, the application saves each user who reviews a timesheet, and when the
            timesheet was reviewed. This information can be viewed by loading TimesheetAudit business objects.
        enable_web_services_ip_check (bool | Unset):
        enable_whats_new_dialog (bool | Unset):
        exception_site_list (str | Unset):
        footer_label_1 (str | Unset): The first footer for reports. The Project Management application allows up to
            three different footer text strings that can be optionally placed at the bottom of all reports using the report
            writer.
        footer_label_2 (str | Unset): The second footer for reports. The Project Management application allows up to
            three different footer text strings that can be optionally placed at the bottom of all reports using the report
            writer.
        footer_label_3 (str | Unset): The third footer for reports. The Project Management application allows up to
            three different footer text strings that can be optionally placed at the bottom of all reports using the report
            writer.
        gateway_api_url (str | Unset): The Primavera Gateway URL that will allow you to integrate other products with P6
            and P6 Professional.
        gateway_export_erp_sync_name (str | Unset): The synchronization for exporting to ERP.
        gateway_export_unifier_sync_name (str | Unset): The synchronization for exporting to Primavera Unifier.
        gateway_import_erp_sync_name (str | Unset): The synchronization for importing to ERP.
        gateway_import_unifier_sync_name (str | Unset): The synchronization for importing to Primavera Unifier.
        gateway_p6_deployment_name (str | Unset): The name for the P6 deployment to be integrated with Primavera
            Gateway.
        gateway_password (str | Unset): The password for integration.
        gateway_unifier_enabled (bool | Unset): This is the flag to enable Unifier through Gateway.
        gateway_username (str | Unset): The username for integration.
        header_label_1 (str | Unset): The first header for reports. The Project Management application allows up to
            three different header text strings that can be optionally placed at the top of all reports using the report
            writer.
        header_label_2 (str | Unset): The second header for reports. The Project Management application allows up to
            three different header text strings that can be optionally placed at the top of all reports using the report
            writer.
        header_label_3 (str | Unset): The third header for reports. The Project Management application allows up to
            three different header text strings that can be optionally placed at the top of all reports using the report
            writer.
        hour_abbreviation (str | Unset): The abbreviation character for time periods of hours. This abbreviation is used
            for displaying time units and durations in the user's selected display formats.
        hours_per_day (float | Unset): The number of work hours per day. This conversion factor is used for displaying
            time units and durations in the user's selected display formats.
        hours_per_month (float | Unset): The number of work hours per month. This conversion factor is used for
            displaying time units and durations in the user's selected display formats.
        hours_per_week (float | Unset): The number of work hours per week. This conversion factor is used for displaying
            time units and durations in the user's selected display formats.
        hours_per_year (float | Unset): The number of work hours per year. This conversion factor is used for displaying
            time units and durations in the user's selected display formats.
        ip_site_list (str | Unset):
        last_update_date (datetime.datetime | Unset): The date this global preferences was last updated.
        last_update_user (str | Unset): The name of the user that last updated this global preferences.
        log_hours_after_actual_finish (bool | Unset): The flag that indicates whether timesheet application users are
            allowed to log timesheet hours on activities for dates after the activities' actual finish dates.
        log_hours_before_actual_start (bool | Unset): The flag that indicates whether timesheet application users are
            allowed to log timesheet hours on activities for dates prior to the activities' actual start dates.
        log_hours_completed_activities (bool | Unset): The flag that indicates whether timesheet application users are
            allowed to log timesheet hours on activities that are already marked as completed.
        log_hours_in_future (bool | Unset): The flag that indicates whether the user can log hours in the future.
        log_hours_not_started_activities (bool | Unset): The flag that indicates whether timesheet application users are
            allowed to log timesheet hours on activities that are still marked as Not started.
        max_activity_code_tree_levels (int | Unset): The maximum number of levels that can be created in activity code
            hierarchies in the Project Management application. The API ignores this setting when creating activity codes.
        max_activity_codes_per_project (int | Unset): The maximum number of project-level activity user codes that can
            be created per project.
        max_activity_id_length (int | Unset): The maximum number of characters allowed for activity IDs.
        max_assignment_code_tree_level_cnt (int | Unset):
        max_baselines_per_project (int | Unset): The maximum number of baselines that can be created per project.
        max_cost_account_length (int | Unset): The maximum number of characters allowed for cost account IDs (at each
            level in the cost account tree).
        max_cost_account_tree_levels (int | Unset): The maximum number of levels that can be created in the cost account
            hierarchy in the Project Management application. The API ignores this setting when creating cost accounts.
        max_fp_calendar_count (int | Unset):
        max_obs_tree_levels (int | Unset): The maximum number of levels that can be created in OBS hierarchies in the
            Project Management application. The API ignores this setting when creating OBS objects.
        max_project_code_tree_levels (int | Unset): The maximum number of levels in the project category hierarchy in
            the Project Management application. The API ignores this setting when creating project codes.
        max_project_id_length (int | Unset): The maximum number characters allowed for project IDs.
        max_resource_code_tree_levels (int | Unset): The maximum number of levels in the resource code hierarchy in the
            Project Management application. The API ignores this setting when creating resource codes.
        max_resource_id_length (int | Unset): The maximum number of characters allowed for resource IDs (at each level
            in the resource tree).
        max_resource_tree_levels (int | Unset): The maximum number of levels that can be created in the resource
            hierarchy.
        max_role_code_tree_level_cnt (int | Unset):
        max_role_id_length (int | Unset): The maximum number characters allowed for role IDs.
        max_role_tree_levels (int | Unset): The maximum number of levels in the role hierarchy in the Project Management
            application. The API ignores this setting when creating roles.
        max_timesheet_resource_hours (float | Unset): The maximum hours a resource can enter per day for all of their
            assigned activities.
        max_wbs_code_length (int | Unset): The maximum number of characters allowed for WBS codes (at each level in the
            WBS tree).
        max_wbs_tree_levels (int | Unset): The maximum number of levels that can be created in WBS hierarchies.
        maximum_baselines_copied_with_project (int | Unset): The number of baseline projects that can be copied with a
            project.
        minute_abbreviation (str | Unset): The abbreviation character for time periods of minutes. This abbreviation is
            used for displaying time units and durations in the user's selected display formats.
        month_abbreviation (str | Unset): The abbreviation character for time periods of months. This abbreviation is
            used for displaying time units and durations in the user's selected display formats.
        number_of_accessible_future_timesheets (int | Unset): The number of future timesheets that timesheet application
            users are allowed to access.
        number_of_accessible_past_timesheets (int | Unset):
        private_ip_allow_list (str | Unset):
        report_enable_lazy_load (bool | Unset):
        resources_can_assign_themselves_to_activities (bool | Unset): The flag that indicates whether timesheet
            application users are allowed to assign themselves to activities in this project.
        resources_can_assign_themselves_to_activities_outside_their_obs_access (bool | Unset):
        start_day_of_week (int | Unset): The starting day of the week as displayed in all calendars.
        summarize_by_calendar (bool | Unset): The flag indicating whether to summarize by calendar .
        summarize_by_financial_periods (bool | Unset): The flag indicating whether to summarize the EPS, project or WBS
            by financial periods.
        summary_resource_spread_interval (str | Unset): The interval in which resource and role level spreads are
            summarized and stored. Valid values are 'Month' and 'Week'. This setting is used by the Summarizer job service.
        summary_wbs_spread_interval (str | Unset): The interval in which WBS level spreads are summarized and stored.
            Valid values are 'Month' and 'Week'. This setting is used by the Summarizer job service.
        team_member_consent_message (str | Unset):
        team_member_enable_consent (str | Unset):
        time_window_completed_activities (int | Unset): The time window (days) to access completed activities in the
            timesheet application, assigned to new resources by default.
        time_window_not_started_activities (int | Unset): The time window (days) to access not started activities in the
            timesheet application, assigned to new resources by default.
        timesheet_approval_level (int | Unset): The number of approval levels required for timesheets (0, 1, or 2)
            before timesheets hours are applied to activities as actuals.
        timesheet_decimal_digits (int | Unset): The number of decimal digits for recording hours in timesheets.
        timesheet_interval (bool | Unset): The flag that indicates whether timesheet application users enter timesheet
            hours daily or by entire timesheet reporting period.
        timesheet_period_ends_on_day (str | Unset): The end day of time sheet period used in time sheet application.
            Valid values are: 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday' and 'Saturday'.
        timesheet_period_type (str | Unset): The time period used in time sheet application. Valid values are: 'Every
            Week', 'Every Two Weeks', 'Every Four Weeks' and 'Every Month'.
        unifier_auth_code (str | Unset):
        unifier_company_short_name (str | Unset):
        unifier_integration_password (str | Unset):
        unifier_integration_user_name (str | Unset):
        unifier_web_service_url (str | Unset):
        use_calendar_time_periods_flag (bool | Unset): The flag that indicates whether the system uses the hours per
            time period defined in the calendar.If this flag is true, the system uses the hours per time period settings
            that are defined in the calendar.If this flag is false, the system uses the hours per time period from the
            global preferences.
        use_max_timesheet_resource_hours (bool | Unset): The flag indicating whether to restrict the number of hours a
            user can enter to the limit specified in MaxTimesheetResourceHours.
        use_project_manager_approval (str | Unset): The flag that indicates the approval sequence, if any, required for
            level 2 timesheet approvals. For example, project managers must approve before resource manager do, or vice
            versa.
        use_timesheets (bool | Unset): The flag that indicates whether new resources use timesheets by default.
        version_for_whats_new (str | Unset):
        wbs_category_label (str | Unset): The dynamic label used for the WBS category. Project Planner allows the system
            administrator to dynamically label the WBS category.
        wbs_code_separator (str | Unset): The character used for separating code fields for the cost account tree. This
            is also the WBS code separator for new projects by default.
        week_abbreviation (str | Unset): The abbreviation character for time periods of weeks. This abbreviation is used
            for displaying time units and durations in the user's selected display formats.
        year_abbreviation (str | Unset): The abbreviation character for time periods of years. This abbreviation is used
            for displaying time units and durations in the user's selected display formats.
    """

    allow_approved_ts_rejection: bool | Unset = UNSET
    always_launch_online_help: bool | Unset = UNSET
    base_currency_object_id: int | Unset = UNSET
    contract_management_url: str | Unset = UNSET
    create_date: datetime.datetime | Unset = UNSET
    create_user: str | Unset = UNSET
    custom_label_1: str | Unset = UNSET
    custom_label_2: str | Unset = UNSET
    custom_label_3: str | Unset = UNSET
    day_abbreviation: str | Unset = UNSET
    default_duration: float | Unset = UNSET
    default_timesheet_approval_manager: int | Unset = UNSET
    eppm_consent_message: str | Unset = UNSET
    eppm_enable_consent: str | Unset = UNSET
    ev_estimate_to_complete_factor: float | Unset = UNSET
    ev_estimate_to_complete_technique: str | Unset = UNSET
    ev_performance_pct_complete_custom_pct: float | Unset = UNSET
    ev_performance_pct_complete_technique: str | Unset = UNSET
    earned_value_calculation: str | Unset = UNSET
    email_notify_ts_rejection: bool | Unset = UNSET
    enable_password_policy: bool | Unset = UNSET
    enable_ts_audit: bool | Unset = UNSET
    enable_web_services_ip_check: bool | Unset = UNSET
    enable_whats_new_dialog: bool | Unset = UNSET
    exception_site_list: str | Unset = UNSET
    footer_label_1: str | Unset = UNSET
    footer_label_2: str | Unset = UNSET
    footer_label_3: str | Unset = UNSET
    gateway_api_url: str | Unset = UNSET
    gateway_export_erp_sync_name: str | Unset = UNSET
    gateway_export_unifier_sync_name: str | Unset = UNSET
    gateway_import_erp_sync_name: str | Unset = UNSET
    gateway_import_unifier_sync_name: str | Unset = UNSET
    gateway_p6_deployment_name: str | Unset = UNSET
    gateway_password: str | Unset = UNSET
    gateway_unifier_enabled: bool | Unset = UNSET
    gateway_username: str | Unset = UNSET
    header_label_1: str | Unset = UNSET
    header_label_2: str | Unset = UNSET
    header_label_3: str | Unset = UNSET
    hour_abbreviation: str | Unset = UNSET
    hours_per_day: float | Unset = UNSET
    hours_per_month: float | Unset = UNSET
    hours_per_week: float | Unset = UNSET
    hours_per_year: float | Unset = UNSET
    ip_site_list: str | Unset = UNSET
    last_update_date: datetime.datetime | Unset = UNSET
    last_update_user: str | Unset = UNSET
    log_hours_after_actual_finish: bool | Unset = UNSET
    log_hours_before_actual_start: bool | Unset = UNSET
    log_hours_completed_activities: bool | Unset = UNSET
    log_hours_in_future: bool | Unset = UNSET
    log_hours_not_started_activities: bool | Unset = UNSET
    max_activity_code_tree_levels: int | Unset = UNSET
    max_activity_codes_per_project: int | Unset = UNSET
    max_activity_id_length: int | Unset = UNSET
    max_assignment_code_tree_level_cnt: int | Unset = UNSET
    max_baselines_per_project: int | Unset = UNSET
    max_cost_account_length: int | Unset = UNSET
    max_cost_account_tree_levels: int | Unset = UNSET
    max_fp_calendar_count: int | Unset = UNSET
    max_obs_tree_levels: int | Unset = UNSET
    max_project_code_tree_levels: int | Unset = UNSET
    max_project_id_length: int | Unset = UNSET
    max_resource_code_tree_levels: int | Unset = UNSET
    max_resource_id_length: int | Unset = UNSET
    max_resource_tree_levels: int | Unset = UNSET
    max_role_code_tree_level_cnt: int | Unset = UNSET
    max_role_id_length: int | Unset = UNSET
    max_role_tree_levels: int | Unset = UNSET
    max_timesheet_resource_hours: float | Unset = UNSET
    max_wbs_code_length: int | Unset = UNSET
    max_wbs_tree_levels: int | Unset = UNSET
    maximum_baselines_copied_with_project: int | Unset = UNSET
    minute_abbreviation: str | Unset = UNSET
    month_abbreviation: str | Unset = UNSET
    number_of_accessible_future_timesheets: int | Unset = UNSET
    number_of_accessible_past_timesheets: int | Unset = UNSET
    private_ip_allow_list: str | Unset = UNSET
    report_enable_lazy_load: bool | Unset = UNSET
    resources_can_assign_themselves_to_activities: bool | Unset = UNSET
    resources_can_assign_themselves_to_activities_outside_their_obs_access: bool | Unset = UNSET
    start_day_of_week: int | Unset = UNSET
    summarize_by_calendar: bool | Unset = UNSET
    summarize_by_financial_periods: bool | Unset = UNSET
    summary_resource_spread_interval: str | Unset = UNSET
    summary_wbs_spread_interval: str | Unset = UNSET
    team_member_consent_message: str | Unset = UNSET
    team_member_enable_consent: str | Unset = UNSET
    time_window_completed_activities: int | Unset = UNSET
    time_window_not_started_activities: int | Unset = UNSET
    timesheet_approval_level: int | Unset = UNSET
    timesheet_decimal_digits: int | Unset = UNSET
    timesheet_interval: bool | Unset = UNSET
    timesheet_period_ends_on_day: str | Unset = UNSET
    timesheet_period_type: str | Unset = UNSET
    unifier_auth_code: str | Unset = UNSET
    unifier_company_short_name: str | Unset = UNSET
    unifier_integration_password: str | Unset = UNSET
    unifier_integration_user_name: str | Unset = UNSET
    unifier_web_service_url: str | Unset = UNSET
    use_calendar_time_periods_flag: bool | Unset = UNSET
    use_max_timesheet_resource_hours: bool | Unset = UNSET
    use_project_manager_approval: str | Unset = UNSET
    use_timesheets: bool | Unset = UNSET
    version_for_whats_new: str | Unset = UNSET
    wbs_category_label: str | Unset = UNSET
    wbs_code_separator: str | Unset = UNSET
    week_abbreviation: str | Unset = UNSET
    year_abbreviation: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_approved_ts_rejection = self.allow_approved_ts_rejection

        always_launch_online_help = self.always_launch_online_help

        base_currency_object_id = self.base_currency_object_id

        contract_management_url = self.contract_management_url

        create_date: str | Unset = UNSET
        if not isinstance(self.create_date, Unset):
            create_date = self.create_date.isoformat()

        create_user = self.create_user

        custom_label_1 = self.custom_label_1

        custom_label_2 = self.custom_label_2

        custom_label_3 = self.custom_label_3

        day_abbreviation = self.day_abbreviation

        default_duration = self.default_duration

        default_timesheet_approval_manager = self.default_timesheet_approval_manager

        eppm_consent_message = self.eppm_consent_message

        eppm_enable_consent = self.eppm_enable_consent

        ev_estimate_to_complete_factor = self.ev_estimate_to_complete_factor

        ev_estimate_to_complete_technique = self.ev_estimate_to_complete_technique

        ev_performance_pct_complete_custom_pct = self.ev_performance_pct_complete_custom_pct

        ev_performance_pct_complete_technique = self.ev_performance_pct_complete_technique

        earned_value_calculation = self.earned_value_calculation

        email_notify_ts_rejection = self.email_notify_ts_rejection

        enable_password_policy = self.enable_password_policy

        enable_ts_audit = self.enable_ts_audit

        enable_web_services_ip_check = self.enable_web_services_ip_check

        enable_whats_new_dialog = self.enable_whats_new_dialog

        exception_site_list = self.exception_site_list

        footer_label_1 = self.footer_label_1

        footer_label_2 = self.footer_label_2

        footer_label_3 = self.footer_label_3

        gateway_api_url = self.gateway_api_url

        gateway_export_erp_sync_name = self.gateway_export_erp_sync_name

        gateway_export_unifier_sync_name = self.gateway_export_unifier_sync_name

        gateway_import_erp_sync_name = self.gateway_import_erp_sync_name

        gateway_import_unifier_sync_name = self.gateway_import_unifier_sync_name

        gateway_p6_deployment_name = self.gateway_p6_deployment_name

        gateway_password = self.gateway_password

        gateway_unifier_enabled = self.gateway_unifier_enabled

        gateway_username = self.gateway_username

        header_label_1 = self.header_label_1

        header_label_2 = self.header_label_2

        header_label_3 = self.header_label_3

        hour_abbreviation = self.hour_abbreviation

        hours_per_day = self.hours_per_day

        hours_per_month = self.hours_per_month

        hours_per_week = self.hours_per_week

        hours_per_year = self.hours_per_year

        ip_site_list = self.ip_site_list

        last_update_date: str | Unset = UNSET
        if not isinstance(self.last_update_date, Unset):
            last_update_date = self.last_update_date.isoformat()

        last_update_user = self.last_update_user

        log_hours_after_actual_finish = self.log_hours_after_actual_finish

        log_hours_before_actual_start = self.log_hours_before_actual_start

        log_hours_completed_activities = self.log_hours_completed_activities

        log_hours_in_future = self.log_hours_in_future

        log_hours_not_started_activities = self.log_hours_not_started_activities

        max_activity_code_tree_levels = self.max_activity_code_tree_levels

        max_activity_codes_per_project = self.max_activity_codes_per_project

        max_activity_id_length = self.max_activity_id_length

        max_assignment_code_tree_level_cnt = self.max_assignment_code_tree_level_cnt

        max_baselines_per_project = self.max_baselines_per_project

        max_cost_account_length = self.max_cost_account_length

        max_cost_account_tree_levels = self.max_cost_account_tree_levels

        max_fp_calendar_count = self.max_fp_calendar_count

        max_obs_tree_levels = self.max_obs_tree_levels

        max_project_code_tree_levels = self.max_project_code_tree_levels

        max_project_id_length = self.max_project_id_length

        max_resource_code_tree_levels = self.max_resource_code_tree_levels

        max_resource_id_length = self.max_resource_id_length

        max_resource_tree_levels = self.max_resource_tree_levels

        max_role_code_tree_level_cnt = self.max_role_code_tree_level_cnt

        max_role_id_length = self.max_role_id_length

        max_role_tree_levels = self.max_role_tree_levels

        max_timesheet_resource_hours = self.max_timesheet_resource_hours

        max_wbs_code_length = self.max_wbs_code_length

        max_wbs_tree_levels = self.max_wbs_tree_levels

        maximum_baselines_copied_with_project = self.maximum_baselines_copied_with_project

        minute_abbreviation = self.minute_abbreviation

        month_abbreviation = self.month_abbreviation

        number_of_accessible_future_timesheets = self.number_of_accessible_future_timesheets

        number_of_accessible_past_timesheets = self.number_of_accessible_past_timesheets

        private_ip_allow_list = self.private_ip_allow_list

        report_enable_lazy_load = self.report_enable_lazy_load

        resources_can_assign_themselves_to_activities = self.resources_can_assign_themselves_to_activities

        resources_can_assign_themselves_to_activities_outside_their_obs_access = (
            self.resources_can_assign_themselves_to_activities_outside_their_obs_access
        )

        start_day_of_week = self.start_day_of_week

        summarize_by_calendar = self.summarize_by_calendar

        summarize_by_financial_periods = self.summarize_by_financial_periods

        summary_resource_spread_interval = self.summary_resource_spread_interval

        summary_wbs_spread_interval = self.summary_wbs_spread_interval

        team_member_consent_message = self.team_member_consent_message

        team_member_enable_consent = self.team_member_enable_consent

        time_window_completed_activities = self.time_window_completed_activities

        time_window_not_started_activities = self.time_window_not_started_activities

        timesheet_approval_level = self.timesheet_approval_level

        timesheet_decimal_digits = self.timesheet_decimal_digits

        timesheet_interval = self.timesheet_interval

        timesheet_period_ends_on_day = self.timesheet_period_ends_on_day

        timesheet_period_type = self.timesheet_period_type

        unifier_auth_code = self.unifier_auth_code

        unifier_company_short_name = self.unifier_company_short_name

        unifier_integration_password = self.unifier_integration_password

        unifier_integration_user_name = self.unifier_integration_user_name

        unifier_web_service_url = self.unifier_web_service_url

        use_calendar_time_periods_flag = self.use_calendar_time_periods_flag

        use_max_timesheet_resource_hours = self.use_max_timesheet_resource_hours

        use_project_manager_approval = self.use_project_manager_approval

        use_timesheets = self.use_timesheets

        version_for_whats_new = self.version_for_whats_new

        wbs_category_label = self.wbs_category_label

        wbs_code_separator = self.wbs_code_separator

        week_abbreviation = self.week_abbreviation

        year_abbreviation = self.year_abbreviation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_approved_ts_rejection is not UNSET:
            field_dict["AllowApprovedTSRejection"] = allow_approved_ts_rejection
        if always_launch_online_help is not UNSET:
            field_dict["AlwaysLaunchOnlineHelp"] = always_launch_online_help
        if base_currency_object_id is not UNSET:
            field_dict["BaseCurrencyObjectId"] = base_currency_object_id
        if contract_management_url is not UNSET:
            field_dict["ContractManagementURL"] = contract_management_url
        if create_date is not UNSET:
            field_dict["CreateDate"] = create_date
        if create_user is not UNSET:
            field_dict["CreateUser"] = create_user
        if custom_label_1 is not UNSET:
            field_dict["CustomLabel1"] = custom_label_1
        if custom_label_2 is not UNSET:
            field_dict["CustomLabel2"] = custom_label_2
        if custom_label_3 is not UNSET:
            field_dict["CustomLabel3"] = custom_label_3
        if day_abbreviation is not UNSET:
            field_dict["DayAbbreviation"] = day_abbreviation
        if default_duration is not UNSET:
            field_dict["DefaultDuration"] = default_duration
        if default_timesheet_approval_manager is not UNSET:
            field_dict["DefaultTimesheetApprovalManager"] = default_timesheet_approval_manager
        if eppm_consent_message is not UNSET:
            field_dict["EPPMConsentMessage"] = eppm_consent_message
        if eppm_enable_consent is not UNSET:
            field_dict["EPPMEnableConsent"] = eppm_enable_consent
        if ev_estimate_to_complete_factor is not UNSET:
            field_dict["EVEstimateToCompleteFactor"] = ev_estimate_to_complete_factor
        if ev_estimate_to_complete_technique is not UNSET:
            field_dict["EVEstimateToCompleteTechnique"] = ev_estimate_to_complete_technique
        if ev_performance_pct_complete_custom_pct is not UNSET:
            field_dict["EVPerformancePctCompleteCustomPct"] = ev_performance_pct_complete_custom_pct
        if ev_performance_pct_complete_technique is not UNSET:
            field_dict["EVPerformancePctCompleteTechnique"] = ev_performance_pct_complete_technique
        if earned_value_calculation is not UNSET:
            field_dict["EarnedValueCalculation"] = earned_value_calculation
        if email_notify_ts_rejection is not UNSET:
            field_dict["EmailNotifyTSRejection"] = email_notify_ts_rejection
        if enable_password_policy is not UNSET:
            field_dict["EnablePasswordPolicy"] = enable_password_policy
        if enable_ts_audit is not UNSET:
            field_dict["EnableTSAudit"] = enable_ts_audit
        if enable_web_services_ip_check is not UNSET:
            field_dict["EnableWebServicesIPCheck"] = enable_web_services_ip_check
        if enable_whats_new_dialog is not UNSET:
            field_dict["EnableWhatsNewDialog"] = enable_whats_new_dialog
        if exception_site_list is not UNSET:
            field_dict["ExceptionSiteList"] = exception_site_list
        if footer_label_1 is not UNSET:
            field_dict["FooterLabel1"] = footer_label_1
        if footer_label_2 is not UNSET:
            field_dict["FooterLabel2"] = footer_label_2
        if footer_label_3 is not UNSET:
            field_dict["FooterLabel3"] = footer_label_3
        if gateway_api_url is not UNSET:
            field_dict["GatewayApiUrl"] = gateway_api_url
        if gateway_export_erp_sync_name is not UNSET:
            field_dict["GatewayExportERPSyncName"] = gateway_export_erp_sync_name
        if gateway_export_unifier_sync_name is not UNSET:
            field_dict["GatewayExportUnifierSyncName"] = gateway_export_unifier_sync_name
        if gateway_import_erp_sync_name is not UNSET:
            field_dict["GatewayImportERPSyncName"] = gateway_import_erp_sync_name
        if gateway_import_unifier_sync_name is not UNSET:
            field_dict["GatewayImportUnifierSyncName"] = gateway_import_unifier_sync_name
        if gateway_p6_deployment_name is not UNSET:
            field_dict["GatewayP6DeploymentName"] = gateway_p6_deployment_name
        if gateway_password is not UNSET:
            field_dict["GatewayPassword"] = gateway_password
        if gateway_unifier_enabled is not UNSET:
            field_dict["GatewayUnifierEnabled"] = gateway_unifier_enabled
        if gateway_username is not UNSET:
            field_dict["GatewayUsername"] = gateway_username
        if header_label_1 is not UNSET:
            field_dict["HeaderLabel1"] = header_label_1
        if header_label_2 is not UNSET:
            field_dict["HeaderLabel2"] = header_label_2
        if header_label_3 is not UNSET:
            field_dict["HeaderLabel3"] = header_label_3
        if hour_abbreviation is not UNSET:
            field_dict["HourAbbreviation"] = hour_abbreviation
        if hours_per_day is not UNSET:
            field_dict["HoursPerDay"] = hours_per_day
        if hours_per_month is not UNSET:
            field_dict["HoursPerMonth"] = hours_per_month
        if hours_per_week is not UNSET:
            field_dict["HoursPerWeek"] = hours_per_week
        if hours_per_year is not UNSET:
            field_dict["HoursPerYear"] = hours_per_year
        if ip_site_list is not UNSET:
            field_dict["IPSiteList"] = ip_site_list
        if last_update_date is not UNSET:
            field_dict["LastUpdateDate"] = last_update_date
        if last_update_user is not UNSET:
            field_dict["LastUpdateUser"] = last_update_user
        if log_hours_after_actual_finish is not UNSET:
            field_dict["LogHoursAfterActualFinish"] = log_hours_after_actual_finish
        if log_hours_before_actual_start is not UNSET:
            field_dict["LogHoursBeforeActualStart"] = log_hours_before_actual_start
        if log_hours_completed_activities is not UNSET:
            field_dict["LogHoursCompletedActivities"] = log_hours_completed_activities
        if log_hours_in_future is not UNSET:
            field_dict["LogHoursInFuture"] = log_hours_in_future
        if log_hours_not_started_activities is not UNSET:
            field_dict["LogHoursNotStartedActivities"] = log_hours_not_started_activities
        if max_activity_code_tree_levels is not UNSET:
            field_dict["MaxActivityCodeTreeLevels"] = max_activity_code_tree_levels
        if max_activity_codes_per_project is not UNSET:
            field_dict["MaxActivityCodesPerProject"] = max_activity_codes_per_project
        if max_activity_id_length is not UNSET:
            field_dict["MaxActivityIdLength"] = max_activity_id_length
        if max_assignment_code_tree_level_cnt is not UNSET:
            field_dict["MaxAssignmentCodeTreeLevelCnt"] = max_assignment_code_tree_level_cnt
        if max_baselines_per_project is not UNSET:
            field_dict["MaxBaselinesPerProject"] = max_baselines_per_project
        if max_cost_account_length is not UNSET:
            field_dict["MaxCostAccountLength"] = max_cost_account_length
        if max_cost_account_tree_levels is not UNSET:
            field_dict["MaxCostAccountTreeLevels"] = max_cost_account_tree_levels
        if max_fp_calendar_count is not UNSET:
            field_dict["MaxFPCalendarCount"] = max_fp_calendar_count
        if max_obs_tree_levels is not UNSET:
            field_dict["MaxOBSTreeLevels"] = max_obs_tree_levels
        if max_project_code_tree_levels is not UNSET:
            field_dict["MaxProjectCodeTreeLevels"] = max_project_code_tree_levels
        if max_project_id_length is not UNSET:
            field_dict["MaxProjectIdLength"] = max_project_id_length
        if max_resource_code_tree_levels is not UNSET:
            field_dict["MaxResourceCodeTreeLevels"] = max_resource_code_tree_levels
        if max_resource_id_length is not UNSET:
            field_dict["MaxResourceIdLength"] = max_resource_id_length
        if max_resource_tree_levels is not UNSET:
            field_dict["MaxResourceTreeLevels"] = max_resource_tree_levels
        if max_role_code_tree_level_cnt is not UNSET:
            field_dict["MaxRoleCodeTreeLevelCnt"] = max_role_code_tree_level_cnt
        if max_role_id_length is not UNSET:
            field_dict["MaxRoleIdLength"] = max_role_id_length
        if max_role_tree_levels is not UNSET:
            field_dict["MaxRoleTreeLevels"] = max_role_tree_levels
        if max_timesheet_resource_hours is not UNSET:
            field_dict["MaxTimesheetResourceHours"] = max_timesheet_resource_hours
        if max_wbs_code_length is not UNSET:
            field_dict["MaxWBSCodeLength"] = max_wbs_code_length
        if max_wbs_tree_levels is not UNSET:
            field_dict["MaxWBSTreeLevels"] = max_wbs_tree_levels
        if maximum_baselines_copied_with_project is not UNSET:
            field_dict["MaximumBaselinesCopiedWithProject"] = maximum_baselines_copied_with_project
        if minute_abbreviation is not UNSET:
            field_dict["MinuteAbbreviation"] = minute_abbreviation
        if month_abbreviation is not UNSET:
            field_dict["MonthAbbreviation"] = month_abbreviation
        if number_of_accessible_future_timesheets is not UNSET:
            field_dict["NumberOfAccessibleFutureTimesheets"] = number_of_accessible_future_timesheets
        if number_of_accessible_past_timesheets is not UNSET:
            field_dict["NumberOfAccessiblePastTimesheets"] = number_of_accessible_past_timesheets
        if private_ip_allow_list is not UNSET:
            field_dict["PrivateIPAllowList"] = private_ip_allow_list
        if report_enable_lazy_load is not UNSET:
            field_dict["ReportEnableLazyLoad"] = report_enable_lazy_load
        if resources_can_assign_themselves_to_activities is not UNSET:
            field_dict["ResourcesCanAssignThemselvesToActivities"] = resources_can_assign_themselves_to_activities
        if resources_can_assign_themselves_to_activities_outside_their_obs_access is not UNSET:
            field_dict["ResourcesCanAssignThemselvesToActivitiesOutsideTheirOBSAccess"] = (
                resources_can_assign_themselves_to_activities_outside_their_obs_access
            )
        if start_day_of_week is not UNSET:
            field_dict["StartDayOfWeek"] = start_day_of_week
        if summarize_by_calendar is not UNSET:
            field_dict["SummarizeByCalendar"] = summarize_by_calendar
        if summarize_by_financial_periods is not UNSET:
            field_dict["SummarizeByFinancialPeriods"] = summarize_by_financial_periods
        if summary_resource_spread_interval is not UNSET:
            field_dict["SummaryResourceSpreadInterval"] = summary_resource_spread_interval
        if summary_wbs_spread_interval is not UNSET:
            field_dict["SummaryWBSSpreadInterval"] = summary_wbs_spread_interval
        if team_member_consent_message is not UNSET:
            field_dict["TeamMemberConsentMessage"] = team_member_consent_message
        if team_member_enable_consent is not UNSET:
            field_dict["TeamMemberEnableConsent"] = team_member_enable_consent
        if time_window_completed_activities is not UNSET:
            field_dict["TimeWindowCompletedActivities"] = time_window_completed_activities
        if time_window_not_started_activities is not UNSET:
            field_dict["TimeWindowNotStartedActivities"] = time_window_not_started_activities
        if timesheet_approval_level is not UNSET:
            field_dict["TimesheetApprovalLevel"] = timesheet_approval_level
        if timesheet_decimal_digits is not UNSET:
            field_dict["TimesheetDecimalDigits"] = timesheet_decimal_digits
        if timesheet_interval is not UNSET:
            field_dict["TimesheetInterval"] = timesheet_interval
        if timesheet_period_ends_on_day is not UNSET:
            field_dict["TimesheetPeriodEndsOnDay"] = timesheet_period_ends_on_day
        if timesheet_period_type is not UNSET:
            field_dict["TimesheetPeriodType"] = timesheet_period_type
        if unifier_auth_code is not UNSET:
            field_dict["UnifierAuthCode"] = unifier_auth_code
        if unifier_company_short_name is not UNSET:
            field_dict["UnifierCompanyShortName"] = unifier_company_short_name
        if unifier_integration_password is not UNSET:
            field_dict["UnifierIntegrationPassword"] = unifier_integration_password
        if unifier_integration_user_name is not UNSET:
            field_dict["UnifierIntegrationUserName"] = unifier_integration_user_name
        if unifier_web_service_url is not UNSET:
            field_dict["UnifierWebServiceURL"] = unifier_web_service_url
        if use_calendar_time_periods_flag is not UNSET:
            field_dict["UseCalendarTimePeriodsFlag"] = use_calendar_time_periods_flag
        if use_max_timesheet_resource_hours is not UNSET:
            field_dict["UseMaxTimesheetResourceHours"] = use_max_timesheet_resource_hours
        if use_project_manager_approval is not UNSET:
            field_dict["UseProjectManagerApproval"] = use_project_manager_approval
        if use_timesheets is not UNSET:
            field_dict["UseTimesheets"] = use_timesheets
        if version_for_whats_new is not UNSET:
            field_dict["VersionForWhatsNew"] = version_for_whats_new
        if wbs_category_label is not UNSET:
            field_dict["WBSCategoryLabel"] = wbs_category_label
        if wbs_code_separator is not UNSET:
            field_dict["WBSCodeSeparator"] = wbs_code_separator
        if week_abbreviation is not UNSET:
            field_dict["WeekAbbreviation"] = week_abbreviation
        if year_abbreviation is not UNSET:
            field_dict["YearAbbreviation"] = year_abbreviation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_approved_ts_rejection = d.pop("AllowApprovedTSRejection", UNSET)

        always_launch_online_help = d.pop("AlwaysLaunchOnlineHelp", UNSET)

        base_currency_object_id = d.pop("BaseCurrencyObjectId", UNSET)

        contract_management_url = d.pop("ContractManagementURL", UNSET)

        _create_date = d.pop("CreateDate", UNSET)
        create_date: datetime.datetime | Unset
        if isinstance(_create_date, Unset):
            create_date = UNSET
        else:
            create_date = isoparse(_create_date)

        create_user = d.pop("CreateUser", UNSET)

        custom_label_1 = d.pop("CustomLabel1", UNSET)

        custom_label_2 = d.pop("CustomLabel2", UNSET)

        custom_label_3 = d.pop("CustomLabel3", UNSET)

        day_abbreviation = d.pop("DayAbbreviation", UNSET)

        default_duration = d.pop("DefaultDuration", UNSET)

        default_timesheet_approval_manager = d.pop("DefaultTimesheetApprovalManager", UNSET)

        eppm_consent_message = d.pop("EPPMConsentMessage", UNSET)

        eppm_enable_consent = d.pop("EPPMEnableConsent", UNSET)

        ev_estimate_to_complete_factor = d.pop("EVEstimateToCompleteFactor", UNSET)

        ev_estimate_to_complete_technique = d.pop("EVEstimateToCompleteTechnique", UNSET)

        ev_performance_pct_complete_custom_pct = d.pop("EVPerformancePctCompleteCustomPct", UNSET)

        ev_performance_pct_complete_technique = d.pop("EVPerformancePctCompleteTechnique", UNSET)

        earned_value_calculation = d.pop("EarnedValueCalculation", UNSET)

        email_notify_ts_rejection = d.pop("EmailNotifyTSRejection", UNSET)

        enable_password_policy = d.pop("EnablePasswordPolicy", UNSET)

        enable_ts_audit = d.pop("EnableTSAudit", UNSET)

        enable_web_services_ip_check = d.pop("EnableWebServicesIPCheck", UNSET)

        enable_whats_new_dialog = d.pop("EnableWhatsNewDialog", UNSET)

        exception_site_list = d.pop("ExceptionSiteList", UNSET)

        footer_label_1 = d.pop("FooterLabel1", UNSET)

        footer_label_2 = d.pop("FooterLabel2", UNSET)

        footer_label_3 = d.pop("FooterLabel3", UNSET)

        gateway_api_url = d.pop("GatewayApiUrl", UNSET)

        gateway_export_erp_sync_name = d.pop("GatewayExportERPSyncName", UNSET)

        gateway_export_unifier_sync_name = d.pop("GatewayExportUnifierSyncName", UNSET)

        gateway_import_erp_sync_name = d.pop("GatewayImportERPSyncName", UNSET)

        gateway_import_unifier_sync_name = d.pop("GatewayImportUnifierSyncName", UNSET)

        gateway_p6_deployment_name = d.pop("GatewayP6DeploymentName", UNSET)

        gateway_password = d.pop("GatewayPassword", UNSET)

        gateway_unifier_enabled = d.pop("GatewayUnifierEnabled", UNSET)

        gateway_username = d.pop("GatewayUsername", UNSET)

        header_label_1 = d.pop("HeaderLabel1", UNSET)

        header_label_2 = d.pop("HeaderLabel2", UNSET)

        header_label_3 = d.pop("HeaderLabel3", UNSET)

        hour_abbreviation = d.pop("HourAbbreviation", UNSET)

        hours_per_day = d.pop("HoursPerDay", UNSET)

        hours_per_month = d.pop("HoursPerMonth", UNSET)

        hours_per_week = d.pop("HoursPerWeek", UNSET)

        hours_per_year = d.pop("HoursPerYear", UNSET)

        ip_site_list = d.pop("IPSiteList", UNSET)

        _last_update_date = d.pop("LastUpdateDate", UNSET)
        last_update_date: datetime.datetime | Unset
        if isinstance(_last_update_date, Unset):
            last_update_date = UNSET
        else:
            last_update_date = isoparse(_last_update_date)

        last_update_user = d.pop("LastUpdateUser", UNSET)

        log_hours_after_actual_finish = d.pop("LogHoursAfterActualFinish", UNSET)

        log_hours_before_actual_start = d.pop("LogHoursBeforeActualStart", UNSET)

        log_hours_completed_activities = d.pop("LogHoursCompletedActivities", UNSET)

        log_hours_in_future = d.pop("LogHoursInFuture", UNSET)

        log_hours_not_started_activities = d.pop("LogHoursNotStartedActivities", UNSET)

        max_activity_code_tree_levels = d.pop("MaxActivityCodeTreeLevels", UNSET)

        max_activity_codes_per_project = d.pop("MaxActivityCodesPerProject", UNSET)

        max_activity_id_length = d.pop("MaxActivityIdLength", UNSET)

        max_assignment_code_tree_level_cnt = d.pop("MaxAssignmentCodeTreeLevelCnt", UNSET)

        max_baselines_per_project = d.pop("MaxBaselinesPerProject", UNSET)

        max_cost_account_length = d.pop("MaxCostAccountLength", UNSET)

        max_cost_account_tree_levels = d.pop("MaxCostAccountTreeLevels", UNSET)

        max_fp_calendar_count = d.pop("MaxFPCalendarCount", UNSET)

        max_obs_tree_levels = d.pop("MaxOBSTreeLevels", UNSET)

        max_project_code_tree_levels = d.pop("MaxProjectCodeTreeLevels", UNSET)

        max_project_id_length = d.pop("MaxProjectIdLength", UNSET)

        max_resource_code_tree_levels = d.pop("MaxResourceCodeTreeLevels", UNSET)

        max_resource_id_length = d.pop("MaxResourceIdLength", UNSET)

        max_resource_tree_levels = d.pop("MaxResourceTreeLevels", UNSET)

        max_role_code_tree_level_cnt = d.pop("MaxRoleCodeTreeLevelCnt", UNSET)

        max_role_id_length = d.pop("MaxRoleIdLength", UNSET)

        max_role_tree_levels = d.pop("MaxRoleTreeLevels", UNSET)

        max_timesheet_resource_hours = d.pop("MaxTimesheetResourceHours", UNSET)

        max_wbs_code_length = d.pop("MaxWBSCodeLength", UNSET)

        max_wbs_tree_levels = d.pop("MaxWBSTreeLevels", UNSET)

        maximum_baselines_copied_with_project = d.pop("MaximumBaselinesCopiedWithProject", UNSET)

        minute_abbreviation = d.pop("MinuteAbbreviation", UNSET)

        month_abbreviation = d.pop("MonthAbbreviation", UNSET)

        number_of_accessible_future_timesheets = d.pop("NumberOfAccessibleFutureTimesheets", UNSET)

        number_of_accessible_past_timesheets = d.pop("NumberOfAccessiblePastTimesheets", UNSET)

        private_ip_allow_list = d.pop("PrivateIPAllowList", UNSET)

        report_enable_lazy_load = d.pop("ReportEnableLazyLoad", UNSET)

        resources_can_assign_themselves_to_activities = d.pop("ResourcesCanAssignThemselvesToActivities", UNSET)

        resources_can_assign_themselves_to_activities_outside_their_obs_access = d.pop(
            "ResourcesCanAssignThemselvesToActivitiesOutsideTheirOBSAccess", UNSET
        )

        start_day_of_week = d.pop("StartDayOfWeek", UNSET)

        summarize_by_calendar = d.pop("SummarizeByCalendar", UNSET)

        summarize_by_financial_periods = d.pop("SummarizeByFinancialPeriods", UNSET)

        summary_resource_spread_interval = d.pop("SummaryResourceSpreadInterval", UNSET)

        summary_wbs_spread_interval = d.pop("SummaryWBSSpreadInterval", UNSET)

        team_member_consent_message = d.pop("TeamMemberConsentMessage", UNSET)

        team_member_enable_consent = d.pop("TeamMemberEnableConsent", UNSET)

        time_window_completed_activities = d.pop("TimeWindowCompletedActivities", UNSET)

        time_window_not_started_activities = d.pop("TimeWindowNotStartedActivities", UNSET)

        timesheet_approval_level = d.pop("TimesheetApprovalLevel", UNSET)

        timesheet_decimal_digits = d.pop("TimesheetDecimalDigits", UNSET)

        timesheet_interval = d.pop("TimesheetInterval", UNSET)

        timesheet_period_ends_on_day = d.pop("TimesheetPeriodEndsOnDay", UNSET)

        timesheet_period_type = d.pop("TimesheetPeriodType", UNSET)

        unifier_auth_code = d.pop("UnifierAuthCode", UNSET)

        unifier_company_short_name = d.pop("UnifierCompanyShortName", UNSET)

        unifier_integration_password = d.pop("UnifierIntegrationPassword", UNSET)

        unifier_integration_user_name = d.pop("UnifierIntegrationUserName", UNSET)

        unifier_web_service_url = d.pop("UnifierWebServiceURL", UNSET)

        use_calendar_time_periods_flag = d.pop("UseCalendarTimePeriodsFlag", UNSET)

        use_max_timesheet_resource_hours = d.pop("UseMaxTimesheetResourceHours", UNSET)

        use_project_manager_approval = d.pop("UseProjectManagerApproval", UNSET)

        use_timesheets = d.pop("UseTimesheets", UNSET)

        version_for_whats_new = d.pop("VersionForWhatsNew", UNSET)

        wbs_category_label = d.pop("WBSCategoryLabel", UNSET)

        wbs_code_separator = d.pop("WBSCodeSeparator", UNSET)

        week_abbreviation = d.pop("WeekAbbreviation", UNSET)

        year_abbreviation = d.pop("YearAbbreviation", UNSET)

        global_preferences = cls(
            allow_approved_ts_rejection=allow_approved_ts_rejection,
            always_launch_online_help=always_launch_online_help,
            base_currency_object_id=base_currency_object_id,
            contract_management_url=contract_management_url,
            create_date=create_date,
            create_user=create_user,
            custom_label_1=custom_label_1,
            custom_label_2=custom_label_2,
            custom_label_3=custom_label_3,
            day_abbreviation=day_abbreviation,
            default_duration=default_duration,
            default_timesheet_approval_manager=default_timesheet_approval_manager,
            eppm_consent_message=eppm_consent_message,
            eppm_enable_consent=eppm_enable_consent,
            ev_estimate_to_complete_factor=ev_estimate_to_complete_factor,
            ev_estimate_to_complete_technique=ev_estimate_to_complete_technique,
            ev_performance_pct_complete_custom_pct=ev_performance_pct_complete_custom_pct,
            ev_performance_pct_complete_technique=ev_performance_pct_complete_technique,
            earned_value_calculation=earned_value_calculation,
            email_notify_ts_rejection=email_notify_ts_rejection,
            enable_password_policy=enable_password_policy,
            enable_ts_audit=enable_ts_audit,
            enable_web_services_ip_check=enable_web_services_ip_check,
            enable_whats_new_dialog=enable_whats_new_dialog,
            exception_site_list=exception_site_list,
            footer_label_1=footer_label_1,
            footer_label_2=footer_label_2,
            footer_label_3=footer_label_3,
            gateway_api_url=gateway_api_url,
            gateway_export_erp_sync_name=gateway_export_erp_sync_name,
            gateway_export_unifier_sync_name=gateway_export_unifier_sync_name,
            gateway_import_erp_sync_name=gateway_import_erp_sync_name,
            gateway_import_unifier_sync_name=gateway_import_unifier_sync_name,
            gateway_p6_deployment_name=gateway_p6_deployment_name,
            gateway_password=gateway_password,
            gateway_unifier_enabled=gateway_unifier_enabled,
            gateway_username=gateway_username,
            header_label_1=header_label_1,
            header_label_2=header_label_2,
            header_label_3=header_label_3,
            hour_abbreviation=hour_abbreviation,
            hours_per_day=hours_per_day,
            hours_per_month=hours_per_month,
            hours_per_week=hours_per_week,
            hours_per_year=hours_per_year,
            ip_site_list=ip_site_list,
            last_update_date=last_update_date,
            last_update_user=last_update_user,
            log_hours_after_actual_finish=log_hours_after_actual_finish,
            log_hours_before_actual_start=log_hours_before_actual_start,
            log_hours_completed_activities=log_hours_completed_activities,
            log_hours_in_future=log_hours_in_future,
            log_hours_not_started_activities=log_hours_not_started_activities,
            max_activity_code_tree_levels=max_activity_code_tree_levels,
            max_activity_codes_per_project=max_activity_codes_per_project,
            max_activity_id_length=max_activity_id_length,
            max_assignment_code_tree_level_cnt=max_assignment_code_tree_level_cnt,
            max_baselines_per_project=max_baselines_per_project,
            max_cost_account_length=max_cost_account_length,
            max_cost_account_tree_levels=max_cost_account_tree_levels,
            max_fp_calendar_count=max_fp_calendar_count,
            max_obs_tree_levels=max_obs_tree_levels,
            max_project_code_tree_levels=max_project_code_tree_levels,
            max_project_id_length=max_project_id_length,
            max_resource_code_tree_levels=max_resource_code_tree_levels,
            max_resource_id_length=max_resource_id_length,
            max_resource_tree_levels=max_resource_tree_levels,
            max_role_code_tree_level_cnt=max_role_code_tree_level_cnt,
            max_role_id_length=max_role_id_length,
            max_role_tree_levels=max_role_tree_levels,
            max_timesheet_resource_hours=max_timesheet_resource_hours,
            max_wbs_code_length=max_wbs_code_length,
            max_wbs_tree_levels=max_wbs_tree_levels,
            maximum_baselines_copied_with_project=maximum_baselines_copied_with_project,
            minute_abbreviation=minute_abbreviation,
            month_abbreviation=month_abbreviation,
            number_of_accessible_future_timesheets=number_of_accessible_future_timesheets,
            number_of_accessible_past_timesheets=number_of_accessible_past_timesheets,
            private_ip_allow_list=private_ip_allow_list,
            report_enable_lazy_load=report_enable_lazy_load,
            resources_can_assign_themselves_to_activities=resources_can_assign_themselves_to_activities,
            resources_can_assign_themselves_to_activities_outside_their_obs_access=resources_can_assign_themselves_to_activities_outside_their_obs_access,
            start_day_of_week=start_day_of_week,
            summarize_by_calendar=summarize_by_calendar,
            summarize_by_financial_periods=summarize_by_financial_periods,
            summary_resource_spread_interval=summary_resource_spread_interval,
            summary_wbs_spread_interval=summary_wbs_spread_interval,
            team_member_consent_message=team_member_consent_message,
            team_member_enable_consent=team_member_enable_consent,
            time_window_completed_activities=time_window_completed_activities,
            time_window_not_started_activities=time_window_not_started_activities,
            timesheet_approval_level=timesheet_approval_level,
            timesheet_decimal_digits=timesheet_decimal_digits,
            timesheet_interval=timesheet_interval,
            timesheet_period_ends_on_day=timesheet_period_ends_on_day,
            timesheet_period_type=timesheet_period_type,
            unifier_auth_code=unifier_auth_code,
            unifier_company_short_name=unifier_company_short_name,
            unifier_integration_password=unifier_integration_password,
            unifier_integration_user_name=unifier_integration_user_name,
            unifier_web_service_url=unifier_web_service_url,
            use_calendar_time_periods_flag=use_calendar_time_periods_flag,
            use_max_timesheet_resource_hours=use_max_timesheet_resource_hours,
            use_project_manager_approval=use_project_manager_approval,
            use_timesheets=use_timesheets,
            version_for_whats_new=version_for_whats_new,
            wbs_category_label=wbs_category_label,
            wbs_code_separator=wbs_code_separator,
            week_abbreviation=week_abbreviation,
            year_abbreviation=year_abbreviation,
        )

        global_preferences.additional_properties = d
        return global_preferences

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
