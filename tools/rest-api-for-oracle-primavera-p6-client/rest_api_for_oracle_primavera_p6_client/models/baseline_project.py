from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BaselineProject")


@_attrs_define
class BaselineProject:
    """BaselineProject Entity

    Attributes:
        id (str): The short code assigned to each WBS element for identification. Each WBS element is uniquely
            identified by concatenating its own code together with its parents' codes.
        name (str): The name of the baseline project.
        parent_eps_object_id (int): The unique ID of the parent EPS of this baseline project.
        activity_default_activity_type (str | Unset): The default type for activities. Possible values are 'Task
            Dependent', 'Resource Dependent', 'Level of Effort', or 'Milestone'. A 'Task Dependent' activity is scheduled
            using the activity's calendar rather than the calendars of the assigned resources. A 'Resource Dependent'
            activity is scheduled using the calendars of the assigned resources. This type is used when several resources
            are assigned to the activity, but they may work separately. A 'Milestone' is a zero-duration activity without
            resources, marking a significant project event. A 'Level of Effort' activity has a duration that is determined
            by its dependent activities. Administration-type activities are typically 'Level of Effort'.
        activity_default_calendar_object_id (int | Unset): The unique ID of the calendar assigned to new activities by
            default. Can be null for EPS and baselines.
        activity_default_cost_account_object_id (int | Unset): The unique ID of the cost account assigned to new
            activities and project expenses by default.
        activity_default_duration_type (str | Unset): The duration type assigned to new activities by default. Valid
            values are 'Fixed Units/Time', 'Fixed Duration and Units/Time', 'Fixed Units', or 'Fixed Duration and Units'.
        activity_default_percent_complete_type (str | Unset): The percent complete type assigned to new activities by
            default. Valid values are 'Physical', 'Duration', and 'Units'.
        activity_default_price_per_unit (float | Unset): The price used to estimate resource costs for activities that
            have planned, actual, or remaining units, but no resource assignments. This price is also used to compute costs
            for activities in cases where resources are assigned but the resources have no prices. Resource cost is computed
            as the resource units multiplied by the price per time.
        activity_default_review_required (bool | Unset): The indicator that determines whether status changes for new
            activities must be approved by default.
        activity_id_based_on_selected_activity (bool | Unset): The flag that indicates how to auto-number activity IDs
            for new activities-Y/N - Y means use the selected activity's activity ID as prefix, N means use standard auto-
            numbering based on the prefix, suffix. Default = 'N'
        activity_id_increment (int | Unset): The increment used for auto-numbering of activity IDs. When a new activity
            is created, the activity ID is automatically generated using auto-numbering. Activity ID auto-numbering
            concatenates the prefix and the suffix, with the suffix incremented to make the code unique. Example: 'A',
            '1000', '10' yields activity IDs of 'A1010', 'A1020', 'A1030', etc.
        activity_id_prefix (str | Unset): The prefix used for auto-numbering of activity IDs. When a new activity is
            created, the activity ID is automatically generated using auto-numbering. Activity ID auto-numbering
            concatenates the prefix and the suffix, with the suffix incremented to make the code unique. Example: 'A',
            '1000', '10' yields activity IDs of 'A1010', 'A1020', 'A1030', etc.
        activity_id_suffix (int | Unset): The suffix used for auto-numbering of activity IDs. When a new activity is
            created, the activity ID is automatically generated using auto-numbering. Activity ID auto-numbering
            concatenates the prefix and the suffix, with the suffix incremented to make the code unique. Example: 'A',
            '1000', '10' yields activity IDs of 'A1010', 'A1020', 'A1030', etc.
        activity_percent_complete_based_on_activity_steps (bool | Unset): The flag that indicates whether activity
            physical percent complete is automatically computed from the activity steps completed.
        add_actual_to_remaining (bool | Unset): The flag that indicates whether to add actual to remaining or to
            subtract actual from at complete when actual units and costs are updated. Default = 'Y'
        added_by (str | Unset): The name of the user who added the project to the database.
        allow_status_review (bool | Unset): The indicator that determines whether status updates to activities in a
            project are eligible for manual approval before commiting changes.
        annual_discount_rate (float | Unset): The user-defined number field that identifies the discount rate for the
            project.
        anticipated_finish_date (datetime.datetime | Unset): The anticipated finish date of WBS, project and EPS
            elements. User-entered - not dependent upon any other fields. If there are no children, the anticipated finish
            date will be the finish date displayed in the columns.
        anticipated_start_date (datetime.datetime | Unset): The anticipated start date of WBS, project and EPS elements.
            User-entered - not dependent upon any other fields. If there are no children, the anticipated start date will be
            the start date displayed in the columns.
        assignment_default_driving_flag (bool | Unset): The default flag assigned to new assignments, to indicate
            whether assignments will drive activity dates.
        assignment_default_rate_type (str | Unset): The default rate type when adding resource assignments to a project.
            Valid values are 'Price / Unit', 'Price / Unit2', 'Price / Unit3', 'Price / Unit4', and 'Price / Unit5'.
        baseline_type_name (str | Unset): The name of the baseline type for this project baseline. Baseline types are
            used to categorize project baselines.
        baseline_type_object_id (int | Unset): The unique ID of the baseline type.
        check_out_date (datetime.datetime | Unset): The date on which the baseline project was checked out of the
            Project Management database.
        check_out_status (bool | Unset): The flag that indicates that the baseline project is currently checked out to
            an external file or database and is being managed remotely.
        check_out_user_object_id (int | Unset): The unique ID of the User that checked out this baseline project.
        contains_summary_data (bool | Unset): The flag that indicates that the WBS has been summarized.
        cost_quantity_recalculate_flag (bool | Unset): The flag that indicates whether quantities should be updated when
            costs are updated, if costs and quantities are linked.
        create_date (datetime.datetime | Unset): The date this project baseline was created.
        create_user (str | Unset): The name of the user that created this project baseline.
        critical_activity_float_limit (float | Unset): The duration used to determine if an activity is critical. When
            an activity has total float that is less than or equal to this duration, the activity is marked as critical.
        critical_activity_path_type (str | Unset): The critical path type, which indicates how critical path activities
            are identified for the project, based on either 'Critical Float' or 'Longest Path'.
        current_budget (float | Unset): The sum of the original budget plus the approved and pending budgets from the
            budget change log.
        current_variance (float | Unset): The current budget minus the total spending plan.
        data_date (datetime.datetime | Unset): The current data date for the project. The project status is up to date
            as of the data date. The data date is modified when project actuals are applied.
        date_added (datetime.datetime | Unset): The date on which the project was added to the Project Management
            database.
        default_price_time_units (str | Unset): The time units associated with the project's default price per time.
            Valid values are 'Hour', 'Day', 'Week', 'Month', and 'Year'.
        description (str | Unset): The description of the Project.
        discount_application_period (str | Unset): The timescale for entering ROI spending and benefit plan. Valid
            values are 'Month', 'Quarter', or 'Year'.
        distributed_current_budget (float | Unset): The sum of the current budget values from one level lower.
        enable_publication (bool | Unset): Enables the project to be processed by the Project Arbiter service.
        enable_summarization (bool | Unset): The flag which, when true, causes the Summarizer service to automatically
            summarize the project. If this is false, the project will be skipped during the summary run.
        financial_period_tmpl_id (int | Unset):
        finish_date (datetime.datetime | Unset): The finish date of the baseline project. This field depends on summary
            data that was created when the original project was last summarized before this baseline was created.
        fiscal_year_start_month (int | Unset): The month that marks the beginning of the fiscal year for the project.
        forecast_finish_date (datetime.datetime | Unset): The alternate end date to be optionally used by the scheduler.
        forecast_start_date (datetime.datetime | Unset): The alternate start date to be optionally used by the
            scheduler.
        guid (str | Unset): The globally unique ID generated by the system.
        has_future_bucket_data (bool | Unset): The flag that indicates whether a resource assignment in the baseline has
            future bucket data.
        history_interval (str | Unset): The time interval for how historical project data is stored for use in P6
            Analytics, could be 'Month', 'Week', 'Quarter', 'Year' and 'Financial Period'.
        history_level (str | Unset): The level of historical project data that is stored for use in P6 Analytics, can be
            'None', 'Project', 'WBS' and 'Activity'.
        independent_etc_labor_units (float | Unset): The user-entered ETC total labor.
        independent_etc_total_cost (float | Unset): The user-entered ETC total cost.
        last_baseline_update_date (datetime.datetime | Unset): The date this project baseline was last changed by
            Baseline Update in Project Management.
        last_financial_period_object_id (int | Unset): The unique ID of the last closed financial period for the
            baseline project.
        last_level_date (datetime.datetime | Unset): The date the project was last leveled.
        last_published_on (datetime.datetime | Unset): The date the project was last published.
        last_schedule_date (datetime.datetime | Unset): The date the project was last scheduled.
        last_summarized_date (datetime.datetime | Unset): The date the project was last summarized.
        last_update_baseline_options (str | Unset): The last options used when the baseline project was updated by the
            Update Baseline module.
        last_update_date (datetime.datetime | Unset): The date this project baseline was last updated.
        last_update_user (str | Unset): The name of the user that last updated this project baseline.
        leveling_priority (int | Unset): The priority for scheduling.
        link_actual_to_actual_this_period (bool | Unset): The flag that determines whether actual units and costs are
            linked to actual-this-period units and costs. Default = 'Y'
        link_percent_complete_with_actual (bool | Unset): The flag that determines whether actual units and cost should
            be recalculated when percent complete changes. Default = 'N'
        link_planned_and_at_completion_flag (bool | Unset): The flag that indicates whether the At Completion Cost/Units
            should be linked to Planned Cost/Units for not-started activities. Default = 'Y'
        location_name (str | Unset): The name of the location assigned to the project.
        location_object_id (int | Unset): The unique ID of the location assigned to the project.
        must_finish_by_date (datetime.datetime | Unset): The date by which all project activities must finish. If
            entered, it is used as the project late finish date by the project scheduler.
        obs_name (str | Unset): The name of the person/role in the organization, sometimes referred to as the
            "responsible manager".
        obs_object_id (int | Unset): The unique ID of the project manager from the project's OBS tree who is responsible
            for the WBS.
        object_id (int | Unset): The unique ID generated by the system.
        original_budget (float | Unset): The original budget for the baseline project.
        original_project_object_id (int | Unset): The unique ID of the project from which the project baseline was
            created, if the current project is a project baseline.
        owner_resource_object_id (int | Unset): The unique ID of the Owner Resource of this baseline project.
        parent_eps_id (str | Unset):
        parent_eps_name (str | Unset):
        planned_start_date (datetime.datetime | Unset): The planned start date of the project. Used by the project
            scheduler.
        primary_resources_can_mark_activities_as_completed (bool | Unset): The flag that indicates whether primary
            resources can mark the project activities as completed. If not selected, a primary resource can only mark an
            activity as For Review. In this case the project manager reviews the activity and marks it as either Rejected or
            completed.
        project_forecast_start_date (datetime.datetime | Unset): The alternate start date to be optionally used by the
            scheduler. The user sets the alternate start date by dragging the project bar in the Gantt Chart while manually
            leveling the resource profile in a resource analysis layout.
        project_schedule_type (str | Unset): The type of schedule data to send to Primavera Unifier.
        proposed_budget (float | Unset): The sum of the original budget plus the approved and pending budgets from the
            budget change log.
        publication_priority (int | Unset): A priority value the Project Arbiter service uses to determine the order in
            which projects are submitted to the service queue, where 1 is highest priority and 100 is lowest priority.
        reset_planned_to_remaining_flag (bool | Unset): The flag that indicates whether to reset Planned Duration and
            Units to Remaining Duration and Units, or to reset Remaining Duration and Units to Planned Duration and Units
            when the Activity Status is or becomes not started. Default = 'Y'
        resource_can_be_assigned_to_same_activity_more_than_once (bool | Unset): The flag that indicates whether a
            resource can be assigned more than once to the same activity. This is useful when the resource is expected to
            perform more than one role on an activity, for example, documentation plus QA.
        resource_name (str | Unset):
        resources_can_assign_themselves_to_activities (bool | Unset): The flag that indicates whether timesheet
            application users are allowed to assign themselves to activities in this project.
        resources_can_assign_themselves_to_activities_outside_obs_access (bool | Unset):
        resources_can_edit_assignment_percent_complete (bool | Unset): The flag that indicates whether the project's
            resource can use the timesheet application to update remaining units or percent complete for their activities.
        risk_exposure (float | Unset): The calculated exposure value for the project.
        risk_level (str | Unset): The risk level assigned to the project: 'Very High', 'High', 'Medium', 'Low', and
            'Very Low'.
        risk_matrix_object_id (int | Unset): The unique ID of the associated Risk Matrix.
        risk_score (int | Unset): The calculated risk score for the project.
        scheduled_finish_date (datetime.datetime | Unset): The early finish date of the latest activity in the project,
            as computed by the project scheduler.
        start_date (datetime.datetime | Unset): The start date of the baseline project. This field depends on summary
            data that was created when the original project was last summarized before this baseline was created.
        status (str | Unset): The project status: 'Planned', 'Active', 'Inactive', 'What-If', or 'Requested'.
        status_reviewer_name (str | Unset): The the name of the user reviewing status updates.
        status_reviewer_object_id (str | Unset): The unique ID of the user reviewing status updates.
        strategic_priority (int | Unset): The baseline project's priority. The range is from 1 to 10,000.
        summarize_to_wbs_level (int | Unset): The maximum level within the project's WBS to perform summarization -
            default to 2.
        summarized_data_date (datetime.datetime | Unset): The data date of the project when it was last summarized-only
            updated by summarizer.
        summary_accounting_variance_by_cost (float | Unset): The Planned Value minus the Actual Cost. A negative value
            indicates that the Actual Cost has exceeded the Planned Value.
        summary_accounting_variance_by_labor_units (float | Unset): The Planned Value Labor Units minus the Actual
            Units. Negative value indicates that Actual Units have exceeded the Planned Value Labor Units.
        summary_activity_count (int | Unset): The number of activities that are currently in progress.
        summary_actual_duration (float | Unset): The actual duration.
        summary_actual_expense_cost (float | Unset): The actual costs for all project expenses associated with the
            project.
        summary_actual_finish_date (datetime.datetime | Unset): The latest actual finish date of all activities in the
            project.
        summary_actual_labor_cost (float | Unset): The actual cost for all labor resources assigned to the activity.
        summary_actual_labor_units (float | Unset): The actual labor units.
        summary_actual_material_cost (float | Unset): The actual units for all material resources assigned to the
            activity.
        summary_actual_non_labor_cost (float | Unset): The actual units for all nonlabor resources assigned to the
            activity.
        summary_actual_non_labor_units (float | Unset): The actual nonlabor units.
        summary_actual_start_date (datetime.datetime | Unset): The earliest actual start date of all activities in the
            project.
        summary_actual_this_period_cost (float | Unset): The actual this period cost (will be labor or nonlabor).
        summary_actual_this_period_labor_cost (float | Unset): The actual this period labor cost
        summary_actual_this_period_labor_units (float | Unset): The actual this period labor units.
        summary_actual_this_period_material_cost (float | Unset): The actual this period material cost.
        summary_actual_this_period_non_labor_cost (float | Unset): The actual this period nonlabor cost.
        summary_actual_this_period_non_labor_units (float | Unset): The actual this period nonlabor units.
        summary_actual_total_cost (float | Unset): The actual labor cost + actual nonlabor cost + actual expense cost as
            of the project data date.
        summary_actual_value_by_cost (float | Unset): The actual total cost incurred on the activity as of the project
            data date, computed as Actual Labor Cost + Actual Nonlabor Cost + Actual Material Cost + Actual Expense Cost.
        summary_actual_value_by_labor_units (float | Unset): The actual total labor units for the activity as of the
            project data date (i.e., actual total cost by labor units).
        summary_at_completion_duration (float | Unset): The duration at completion.
        summary_at_completion_expense_cost (float | Unset): The sum of the actual plus remaining cost for all project
            expenses associated with the cost account. Computed as Actual Expense Cost + Remaining Expense Cost.
        summary_at_completion_labor_cost (float | Unset): The sum of the actual plus remaining costs for all labor
            resources assigned to the activity. Computed as actual labor cost + remaining labor cost. Same as the planned
            labor costs if the activity is not started and the actual labor costs once the activity is completed.
        summary_at_completion_labor_units (float | Unset): The sum of the actual plus remaining units for all labor
            resources assigned to the activity. Computed as actual labor units + remaining labor units. Same as the planned
            labor units if the activity is not started and the actual labor units once the activity is completed.
        summary_at_completion_material_cost (float | Unset): The material cost at completion. It is the sum of the
            actual plus remaining costs for all material resources assigned to the activity. Computed as actual material
            cost + remaining material cost. Same as the planned material costs if the activity is not started and the actual
            material costs once the activity is completed.
        summary_at_completion_non_labor_cost (float | Unset): The nonlabor cost at completion. It is the sum of the
            actual plus remaining costs for all nonlabor resources assigned to the activity. Computed as actual nonlabor
            cost + remaining nonlabor cost. Same as the planned nonlabor costs if the activity is not started and the actual
            nonlabor costs once the activity is completed.
        summary_at_completion_non_labor_units (float | Unset): The nonlabor units at completion. It is the sum of the
            actual plus remaining units for all nonlabor resources assigned to the activity. Computed as actual nonlabor
            units + remaining nonlabor units. Same as the planned nonlabor units if the activity is not started and the
            actual nonlabor units once the activity is completed.
        summary_at_completion_total_cost (float | Unset): The estimated cost at completion for the activity. Computed as
            the actual total cost plus the estimate-to-complete cost; EAC = ACWP + ETC. Note that the method for computing
            ETC depends on the earned-value technique selected for the activity's WBS.
        summary_at_completion_total_cost_variance (float | Unset): The Baseline Planned Total Cost - At Completion Total
            Cost.
        summary_baseline_completed_activity_count (int | Unset): The number of completed activities in the baseline.
        summary_baseline_duration (float | Unset): The planned duration for the activity in the primary baseline.
            Planned duration is the total working time from the activity current start date to the current finish date. Same
            as the actual duration plus the remaining duration. The total working time is computed using the activity's
            calendar.
        summary_baseline_expense_cost (float | Unset): The planned cost for all project expenses associated with the
            activity in the primary baseline. Computed as the baseline actual expense cost plus the baseline remaining
            expense cost.
        summary_baseline_finish_date (datetime.datetime | Unset): The current latest finish date of all activities in
            the project for the current baseline.
        summary_baseline_in_progress_activity_count (int | Unset): The number of in-progress activities in the baseline.
        summary_baseline_labor_cost (float | Unset): The planned cost for all labor resources assigned to the activity
            in the primary baseline. Computed from the baseline At Completion labor units. If no resources are assigned,
            computed as the activity Baseline Planned Labor Units * Project Default Price / Time.
        summary_baseline_labor_units (float | Unset): The planned units for all labor resources assigned to the activity
            in the primary baseline. Computed as the baseline actual labor units plus the baseline remaining labor units.
        summary_baseline_material_cost (float | Unset): The planned cost for all material resources assigned to the
            activity in the primary baseline. Computed from the baseline At Completion nonlabor units. If no resources are
            assigned.
        summary_baseline_non_labor_cost (float | Unset): The planned cost for all nonlabor resources assigned to the
            activity in the primary baseline. Computed from the baseline At Completion nonlabor units. If no resources are
            assigned, computed as the activity Baseline Planned Nonlabor Units * Project Default Price / Time.
        summary_baseline_non_labor_units (float | Unset): The planned units for all nonlabor resources assigned to the
            activity in the primary baseline. Computed as the baseline actual nonlabor units plus the baseline remaining
            nonlabor units.
        summary_baseline_not_started_activity_count (int | Unset): The number of activities not started in the baseline.
        summary_baseline_start_date (datetime.datetime | Unset): The current earliest start date of all activities in
            the WBS for the current baseline.
        summary_baseline_total_cost (float | Unset): The Planned Total Cost for the activity in the primary baseline,
            including labor resources, nonlabor resources, and project expenses. Baseline Planned Total Cost = Baseline
            Planned Labor Cost + Baseline Planned Nonlabor Cost + Baseline Planned Expense Cost.
        summary_budget_at_completion_by_cost (float | Unset): The Planned Total Cost through activity completion.
            Computed as Planned Labor Cost + Planned Nonlabor Cost + Planned Expense Cost, same as the Planned Total Cost.
        summary_budget_at_completion_by_labor_units (float | Unset): The Baseline Planned Labor Cost + Baseline Planned
            Nonlabor Cost + Baseline Planned Expense Cost. Same as the Baseline Planned Total Cost.
        summary_completed_activity_count (int | Unset): The number of activities that have an Actual Finish in the WBS.
        summary_cost_percent_complete (float | Unset): The percent complete of cost for all nonlabor resources assigned.
            Computed as Actual Nonlabor Cost / At Completion Nonlabor Cost * 100. Always in the range 0 to 100.
        summary_cost_percent_of_planned (float | Unset): The activity actual cost percent of planned. Computed as actual
            total cost / baseline total cost * 100, or equivalently as ACWP / BAC * 100. The value can exceed 100. The
            baseline total cost is the activity's at completion cost from the current baseline. This field is named
            SummaryCostPercentOfBudget in Primavera's Engineering & Construction and Maintenance & Turnaround solutions.
        summary_cost_performance_index_by_cost (float | Unset): The Earned Value divided by the Actual Cost. A value
            less than 1 indicates that the Actual Cost has exceeded the Planned Value.
        summary_cost_performance_index_by_labor_units (float | Unset): The Earned Value Labor Units / Actual Labor
            Units.
        summary_cost_variance_by_cost (float | Unset): The Earned Value minus the Actual Cost. A negative value
            indicates that the Actual Cost has exceeded the Planned Value.
        summary_cost_variance_by_labor_units (float | Unset): The Earned Value Labor Cost minus Actual Value Labor Cost.
        summary_cost_variance_index (float | Unset): The value that is calculated as the Cost Variance divided by Earned
            Value.
        summary_cost_variance_index_by_cost (float | Unset): The Cost Variance divided by Earned Value.
        summary_cost_variance_index_by_labor_units (float | Unset): The Cost Variance Labor Units divided by Earned
            Value Labor Units.
        summary_duration_percent_complete (float | Unset): The activity actual duration percent of planned. Computed as
            (baseline planned duration - remaining duration) / baseline planned duration * 100. The baseline planned
            duration is the activity's at complete duration from the primary baseline.
        summary_duration_percent_of_planned (float | Unset): The summary actual duration percent of planned of all
            activities under this project. Computed as actual duration / baseline duration * 100. The value can exceed 100.
            The Baseline duration is the activity's at complete duration from the current baseline.
        summary_duration_variance (float | Unset): The duration between the activity's baseline duration and the at
            complete duration. Computed as baseline planned duration - at completion duration.
        summary_earned_value_by_cost (float | Unset): The Budget at Completion * Performance % Complete. The method for
            computing the Performance Percent Complete depends on the Earned Value technique selected for the activity's
            WBS. Budget at Completion is computed from the primary baseline.
        summary_earned_value_by_labor_units (float | Unset): The portion of the baseline labor units that is actually
            completed as of the project data date. Computed as Baseline Labor Units * Performance % Complete. The planned
            labor units performed is essentially the labor units Earned Value for the activity. The method for computing the
            Performance % Complete depends on the Earned Value technique selected for the activity's WBS. The Baseline Labor
            Units is taken from the current baseline.
        summary_estimate_at_completion_by_cost (float | Unset): The Actual Cost plus the Estimate to Complete Cost. The
            method for computing Estimate to Complete depends on the Earned Value technique selected for the activity's WBS.
        summary_estimate_at_completion_by_labor_units (float | Unset): The Actual Labor Units + Estimate To Complete
            Labor Units. (Estimate To Complete Labor Units is calculated based off of the Earned Value setting on the WBS.)
        summary_estimate_at_completion_high_percent_by_labor_units (float | Unset): The high forecast of Estimate At
            Completion (EAC) by labor units.
        summary_estimate_at_completion_low_percent_by_labor_units (float | Unset): The low forecast of Estimate At
            Completion (EAC) by labor units.
        summary_estimate_to_complete_by_cost (float | Unset): The Remaining Total Cost for the activity or the
            Performance Factor * (Budget at Completion - Earned Value), depending on the Earned Value technique selected for
            the activity's WBS (calculated from the primary baseline).
        summary_estimate_to_complete_by_labor_units (float | Unset): The estimated quantity to complete the activity.
            Computed as either the remaining total units for the activity, or as Performance Factor * (Baseline Planned
            Labor Units - Planned Quantity of Work Performed), depending on the Earned Value Technique selected for the
            activity's WBS.
        summary_expense_cost_percent_complete (float | Unset): The percent complete of cost for all expenses associated
            with the project. It is computed as Actual Expense Cost / At Complete Expense Cost * 100, and it is always in
            the range of 0 to 100.
        summary_expense_cost_variance (float | Unset): The Baseline Planned Expense Cost - At Completion Expense Cost
            (At Completion Expense Cost = Actual Expense Cost + Remaining Expense Cost).
        summary_finish_date_variance (float | Unset): The duration between the finish date in the current project and
            the baseline finish date. Calculated as finish date - baseline finish date.
        summary_in_progress_activity_count (int | Unset): The number of activities that are currently in progress.
        summary_labor_cost_percent_complete (float | Unset): The percent complete of cost for all labor resources
            assigned to the project. It is computed as Actual Labor Cost / At Complete Labor Cost * 100, and it is always in
            the range of 0 to 100.
        summary_labor_cost_variance (float | Unset): The Baseline Planned Labor Cost - At Completion Labor Cost.
        summary_labor_units_percent_complete (float | Unset): The percent complete of units for all labor resources for
            the WBS. Computed as actual labor units / at complete labor units * 100. Always in the range 0 to 100.
        summary_labor_units_variance (float | Unset): The difference between baseline labor units and at completion
            labor units. Calculated as baseline labor units - at completion labor units.
        summary_material_cost_percent_complete (float | Unset): The percent complete of cost for all material resources
            assigned to the project. It is computed as Actual Material Cost / At Complete Material Cost * 100, and it is
            always in the range of 0 to 100.
        summary_material_cost_variance (float | Unset): The variance that is calculated as Baseline Material Cost - At
            Completion Material Cost.
        summary_non_labor_cost_percent_complete (float | Unset): The percent complete of cost for all non-labor
            resources assigned to the project. It is computed as Actual Nonlabor Cost / At Complete Nonlabor Cost * 100, and
            it is always in the range of 0 to 100.
        summary_non_labor_cost_variance (float | Unset): The Baseline Planned Nonlabor Cost - At Completion Nonlabor
            Cost.
        summary_non_labor_units_percent_complete (float | Unset): The percent complete of units for all nonlabor
            resources for the Project. Computed as Actual Nonlabor Cost / At Completion Nonlabor Cost * 100. Always in the
            range 0 to 100.
        summary_non_labor_units_variance (float | Unset): The difference between baseline nonlabor units and at
            completion non labor units. Calculated as baseline nonlabor units - at completion nonlabor units.
        summary_not_started_activity_count (int | Unset): The number of activities that are currently not started.
        summary_performance_percent_complete_by_labor_units (float | Unset): The percent complete of units for the
            resource assignments in the WBS Computed as Actual Units / At Complete Units * 100. Always in the range 0 to
            100.
        summary_planned_cost (float | Unset): The sum of all planned expense, non labor, labor, and material costs in
            the baseline project.
        summary_planned_duration (float | Unset): The total working days between planned start and finish dates in the
            baseline project.
        summary_planned_expense_cost (float | Unset): The sum of all planned expense costs in the baseline project.
        summary_planned_finish_date (datetime.datetime | Unset): The latest planned finish date of all activities in the
            baseline project.
        summary_planned_labor_cost (float | Unset): The sum of all planned labor costs in the baseline project.
        summary_planned_labor_units (float | Unset): The sum of all planned labor units in the baseline project.
        summary_planned_material_cost (float | Unset): The sum of all planned material costs in the baseline project.
        summary_planned_non_labor_cost (float | Unset): The sum of all planned non labor costs in the baseline project.
        summary_planned_non_labor_units (float | Unset): The sum of all planned non labor units in the baseline project.
        summary_planned_start_date (datetime.datetime | Unset): The earliest planned start date of all activities in the
            baseline project.
        summary_planned_value_by_cost (float | Unset): The Budget at Completion * Schedule % Complete. The Schedule %
            Complete specifies how much of the activity's baseline duration has been completed so far. Budget at Completion
            is computed from the primary baseline
        summary_planned_value_by_labor_units (float | Unset): The portion of the baseline labor units that is scheduled
            to be completed as of the project data date. Computed as Baseline Labor Units * Schedule % Complete. The
            Schedule % Complete specifies how much of the activity's baseline duration has been completed so far. The
            Baseline Labor Units is taken from the current baseline.
        summary_progress_finish_date (datetime.datetime | Unset): The date the activity is expected to be finished
            according to the progress made on the activity's work products. The expected finish date is entered manually by
            people familiar with progress of the activity's work products.
        summary_remaining_duration (float | Unset): The total working time from the WBS remaining start date to the
            remaining finish date.
        summary_remaining_expense_cost (float | Unset): The remaining costs for all project expenses associated with the
            activities in the WBS.
        summary_remaining_finish_date (datetime.datetime | Unset): The date the resource is scheduled to finish the
            remaining work for the activity. This date is computed by the project scheduler but can be updated manually by
            the project manager. Before the activity is started, the remaining finish date is the same as the planned finish
            date.
        summary_remaining_labor_cost (float | Unset): The remaining costs for all labor resources assigned to the
            activities. The remaining cost reflects the cost remaining for the WBS.
        summary_remaining_labor_units (float | Unset): The remaining units for all labor resources assigned to the
            activities. The remaining units reflects the work remaining to be done for the WBS.
        summary_remaining_material_cost (float | Unset): The remaining material costs for all project expenses
            associated with the activities in the WBS.
        summary_remaining_non_labor_cost (float | Unset): The remaining nonlabor costs for all project expenses
            associated with the activities in the WBS.
        summary_remaining_non_labor_units (float | Unset): The remaining units for all nonlabor resources assigned to
            the activities. The remaining units reflects the work remaining to be done for the WBS.
        summary_remaining_start_date (datetime.datetime | Unset): The earliest remaining start of all activities
            assigned to the WBS.
        summary_remaining_total_cost (float | Unset): The sum of all remaining total costs in the WBS.
        summary_schedule_percent_complete (float | Unset): The measure that indicates how much of the WBS baseline
            duration has been completed so far. Computed based on where the current data date falls between the activity's
            baseline start and finish dates. If the data date is earlier than the baseline start, the schedule % complete is
            0. If the data date is later than the baseline finish, the schedule % complete is 100. The schedule % complete
            indicates how much of the WBS duration should be currently completed, relative to the selected baseline.
        summary_schedule_percent_complete_by_labor_units (float | Unset): The percent complete of units for all labor
            resources. Computed as Actual Labor Units / At Completion Labor Units * 100. Always in the range 0 to 100.
        summary_schedule_performance_index_by_cost (float | Unset): The Earned Value divided by the Planned Value. A
            value less than 1 indicates that less work was actually performed than was scheduled.
        summary_schedule_performance_index_by_labor_units (float | Unset): The Earned Value Labor Units divided by
            Planned Value Labor Units.
        summary_schedule_variance_by_cost (float | Unset): The Earned Value divided by the Planned Value. A negative
            value indicates that less work was actually performed than was scheduled.
        summary_schedule_variance_by_labor_units (float | Unset): The Earned Value Labor Units minus the Planned Value
            Labor Units.
        summary_schedule_variance_index (float | Unset): The value that is calculated as the Schedule Variance Labor
            Units divided by Planned Value Labor Units.
        summary_schedule_variance_index_by_cost (float | Unset): The Schedule Variance divided by the Planned Value.
        summary_schedule_variance_index_by_labor_units (float | Unset): The Schedule Variance Labor Units divided by the
            Planned Value Labor Units.
        summary_start_date_variance (float | Unset): The duration between the start date in the current project and the
            baseline start date. Calculated as start date - baseline start date.
        summary_to_complete_performance_index_by_cost (float | Unset): The (Budget at Completion - Earned Value) divided
            by (Estimate at Completion - Actual Cost).
        summary_total_cost_variance (float | Unset): The value that is calculated as baseline total cost - total cost.
        summary_total_float (float | Unset): The amount of time the WBS can be delayed before delaying the project
            finish date. Total float can be computed as late start - early start or as late finish - early finish; this
            option can be set when running the project scheduler.
        summary_units_percent_complete (float | Unset): The percent complete of units for the resource assignments in
            the WBS. Computed as Actual Units / At Complete Units * 100. Always in the range 0 to 100.
        summary_variance_at_completion_by_labor_units (float | Unset): The Baseline Planned Total Labor Units minus
            Estimate at Completion Labor Units.
        team_member_activity_fields (str | Unset): The list of activity fields that can be updated by a team member
            using the P6 Team Member interfaces.
        team_member_assignment_option (str | Unset): The indicator that determines whether team member can update
            activity fields, assignment fields, or both using the P6 Team Member interfaces.
        team_member_resource_assignment_fields (str | Unset): The list of assignment fields that can be updated by a
            team member using the P6 Team Member interfaces.
        team_member_step_udf_viewable_fields (str | Unset):
        team_member_viewable_fields (str | Unset): The list of fields that are viewable by a team member using the P6
            Team Member interfaces.
        total_benefit_plan (float | Unset): The sum of the monthly benefit plan.
        total_benefit_plan_tally (float | Unset): The sum of the monthly benefit plan tally.
        total_spending_plan (float | Unset): The sum of the monthly spending plan.
        total_spending_plan_tally (float | Unset): The sum of the monthly spending plan tally.
        unallocated_budget (float | Unset): The total current budget minus the distributed current budget.
        undistributed_current_variance (float | Unset): The total spending plan minus the total spending plan tally.
        wbs_code_separator (str | Unset): The character used to separate the concatenated code fields for the project's
            WBS tree.
        wbs_object_id (int | Unset): The internal WBS ID of the project. This ID cannot be used to load a WBS object
            directly.
        web_site_root_directory (str | Unset): The root directory for storing project Web site files before they are
            published to the Web server.
        web_site_url (str | Unset): The project Web site URL, which is the Web address of the project's website.
    """

    id: str
    name: str
    parent_eps_object_id: int
    activity_default_activity_type: str | Unset = UNSET
    activity_default_calendar_object_id: int | Unset = UNSET
    activity_default_cost_account_object_id: int | Unset = UNSET
    activity_default_duration_type: str | Unset = UNSET
    activity_default_percent_complete_type: str | Unset = UNSET
    activity_default_price_per_unit: float | Unset = UNSET
    activity_default_review_required: bool | Unset = UNSET
    activity_id_based_on_selected_activity: bool | Unset = UNSET
    activity_id_increment: int | Unset = UNSET
    activity_id_prefix: str | Unset = UNSET
    activity_id_suffix: int | Unset = UNSET
    activity_percent_complete_based_on_activity_steps: bool | Unset = UNSET
    add_actual_to_remaining: bool | Unset = UNSET
    added_by: str | Unset = UNSET
    allow_status_review: bool | Unset = UNSET
    annual_discount_rate: float | Unset = UNSET
    anticipated_finish_date: datetime.datetime | Unset = UNSET
    anticipated_start_date: datetime.datetime | Unset = UNSET
    assignment_default_driving_flag: bool | Unset = UNSET
    assignment_default_rate_type: str | Unset = UNSET
    baseline_type_name: str | Unset = UNSET
    baseline_type_object_id: int | Unset = UNSET
    check_out_date: datetime.datetime | Unset = UNSET
    check_out_status: bool | Unset = UNSET
    check_out_user_object_id: int | Unset = UNSET
    contains_summary_data: bool | Unset = UNSET
    cost_quantity_recalculate_flag: bool | Unset = UNSET
    create_date: datetime.datetime | Unset = UNSET
    create_user: str | Unset = UNSET
    critical_activity_float_limit: float | Unset = UNSET
    critical_activity_path_type: str | Unset = UNSET
    current_budget: float | Unset = UNSET
    current_variance: float | Unset = UNSET
    data_date: datetime.datetime | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    default_price_time_units: str | Unset = UNSET
    description: str | Unset = UNSET
    discount_application_period: str | Unset = UNSET
    distributed_current_budget: float | Unset = UNSET
    enable_publication: bool | Unset = UNSET
    enable_summarization: bool | Unset = UNSET
    financial_period_tmpl_id: int | Unset = UNSET
    finish_date: datetime.datetime | Unset = UNSET
    fiscal_year_start_month: int | Unset = UNSET
    forecast_finish_date: datetime.datetime | Unset = UNSET
    forecast_start_date: datetime.datetime | Unset = UNSET
    guid: str | Unset = UNSET
    has_future_bucket_data: bool | Unset = UNSET
    history_interval: str | Unset = UNSET
    history_level: str | Unset = UNSET
    independent_etc_labor_units: float | Unset = UNSET
    independent_etc_total_cost: float | Unset = UNSET
    last_baseline_update_date: datetime.datetime | Unset = UNSET
    last_financial_period_object_id: int | Unset = UNSET
    last_level_date: datetime.datetime | Unset = UNSET
    last_published_on: datetime.datetime | Unset = UNSET
    last_schedule_date: datetime.datetime | Unset = UNSET
    last_summarized_date: datetime.datetime | Unset = UNSET
    last_update_baseline_options: str | Unset = UNSET
    last_update_date: datetime.datetime | Unset = UNSET
    last_update_user: str | Unset = UNSET
    leveling_priority: int | Unset = UNSET
    link_actual_to_actual_this_period: bool | Unset = UNSET
    link_percent_complete_with_actual: bool | Unset = UNSET
    link_planned_and_at_completion_flag: bool | Unset = UNSET
    location_name: str | Unset = UNSET
    location_object_id: int | Unset = UNSET
    must_finish_by_date: datetime.datetime | Unset = UNSET
    obs_name: str | Unset = UNSET
    obs_object_id: int | Unset = UNSET
    object_id: int | Unset = UNSET
    original_budget: float | Unset = UNSET
    original_project_object_id: int | Unset = UNSET
    owner_resource_object_id: int | Unset = UNSET
    parent_eps_id: str | Unset = UNSET
    parent_eps_name: str | Unset = UNSET
    planned_start_date: datetime.datetime | Unset = UNSET
    primary_resources_can_mark_activities_as_completed: bool | Unset = UNSET
    project_forecast_start_date: datetime.datetime | Unset = UNSET
    project_schedule_type: str | Unset = UNSET
    proposed_budget: float | Unset = UNSET
    publication_priority: int | Unset = UNSET
    reset_planned_to_remaining_flag: bool | Unset = UNSET
    resource_can_be_assigned_to_same_activity_more_than_once: bool | Unset = UNSET
    resource_name: str | Unset = UNSET
    resources_can_assign_themselves_to_activities: bool | Unset = UNSET
    resources_can_assign_themselves_to_activities_outside_obs_access: bool | Unset = UNSET
    resources_can_edit_assignment_percent_complete: bool | Unset = UNSET
    risk_exposure: float | Unset = UNSET
    risk_level: str | Unset = UNSET
    risk_matrix_object_id: int | Unset = UNSET
    risk_score: int | Unset = UNSET
    scheduled_finish_date: datetime.datetime | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    status: str | Unset = UNSET
    status_reviewer_name: str | Unset = UNSET
    status_reviewer_object_id: str | Unset = UNSET
    strategic_priority: int | Unset = UNSET
    summarize_to_wbs_level: int | Unset = UNSET
    summarized_data_date: datetime.datetime | Unset = UNSET
    summary_accounting_variance_by_cost: float | Unset = UNSET
    summary_accounting_variance_by_labor_units: float | Unset = UNSET
    summary_activity_count: int | Unset = UNSET
    summary_actual_duration: float | Unset = UNSET
    summary_actual_expense_cost: float | Unset = UNSET
    summary_actual_finish_date: datetime.datetime | Unset = UNSET
    summary_actual_labor_cost: float | Unset = UNSET
    summary_actual_labor_units: float | Unset = UNSET
    summary_actual_material_cost: float | Unset = UNSET
    summary_actual_non_labor_cost: float | Unset = UNSET
    summary_actual_non_labor_units: float | Unset = UNSET
    summary_actual_start_date: datetime.datetime | Unset = UNSET
    summary_actual_this_period_cost: float | Unset = UNSET
    summary_actual_this_period_labor_cost: float | Unset = UNSET
    summary_actual_this_period_labor_units: float | Unset = UNSET
    summary_actual_this_period_material_cost: float | Unset = UNSET
    summary_actual_this_period_non_labor_cost: float | Unset = UNSET
    summary_actual_this_period_non_labor_units: float | Unset = UNSET
    summary_actual_total_cost: float | Unset = UNSET
    summary_actual_value_by_cost: float | Unset = UNSET
    summary_actual_value_by_labor_units: float | Unset = UNSET
    summary_at_completion_duration: float | Unset = UNSET
    summary_at_completion_expense_cost: float | Unset = UNSET
    summary_at_completion_labor_cost: float | Unset = UNSET
    summary_at_completion_labor_units: float | Unset = UNSET
    summary_at_completion_material_cost: float | Unset = UNSET
    summary_at_completion_non_labor_cost: float | Unset = UNSET
    summary_at_completion_non_labor_units: float | Unset = UNSET
    summary_at_completion_total_cost: float | Unset = UNSET
    summary_at_completion_total_cost_variance: float | Unset = UNSET
    summary_baseline_completed_activity_count: int | Unset = UNSET
    summary_baseline_duration: float | Unset = UNSET
    summary_baseline_expense_cost: float | Unset = UNSET
    summary_baseline_finish_date: datetime.datetime | Unset = UNSET
    summary_baseline_in_progress_activity_count: int | Unset = UNSET
    summary_baseline_labor_cost: float | Unset = UNSET
    summary_baseline_labor_units: float | Unset = UNSET
    summary_baseline_material_cost: float | Unset = UNSET
    summary_baseline_non_labor_cost: float | Unset = UNSET
    summary_baseline_non_labor_units: float | Unset = UNSET
    summary_baseline_not_started_activity_count: int | Unset = UNSET
    summary_baseline_start_date: datetime.datetime | Unset = UNSET
    summary_baseline_total_cost: float | Unset = UNSET
    summary_budget_at_completion_by_cost: float | Unset = UNSET
    summary_budget_at_completion_by_labor_units: float | Unset = UNSET
    summary_completed_activity_count: int | Unset = UNSET
    summary_cost_percent_complete: float | Unset = UNSET
    summary_cost_percent_of_planned: float | Unset = UNSET
    summary_cost_performance_index_by_cost: float | Unset = UNSET
    summary_cost_performance_index_by_labor_units: float | Unset = UNSET
    summary_cost_variance_by_cost: float | Unset = UNSET
    summary_cost_variance_by_labor_units: float | Unset = UNSET
    summary_cost_variance_index: float | Unset = UNSET
    summary_cost_variance_index_by_cost: float | Unset = UNSET
    summary_cost_variance_index_by_labor_units: float | Unset = UNSET
    summary_duration_percent_complete: float | Unset = UNSET
    summary_duration_percent_of_planned: float | Unset = UNSET
    summary_duration_variance: float | Unset = UNSET
    summary_earned_value_by_cost: float | Unset = UNSET
    summary_earned_value_by_labor_units: float | Unset = UNSET
    summary_estimate_at_completion_by_cost: float | Unset = UNSET
    summary_estimate_at_completion_by_labor_units: float | Unset = UNSET
    summary_estimate_at_completion_high_percent_by_labor_units: float | Unset = UNSET
    summary_estimate_at_completion_low_percent_by_labor_units: float | Unset = UNSET
    summary_estimate_to_complete_by_cost: float | Unset = UNSET
    summary_estimate_to_complete_by_labor_units: float | Unset = UNSET
    summary_expense_cost_percent_complete: float | Unset = UNSET
    summary_expense_cost_variance: float | Unset = UNSET
    summary_finish_date_variance: float | Unset = UNSET
    summary_in_progress_activity_count: int | Unset = UNSET
    summary_labor_cost_percent_complete: float | Unset = UNSET
    summary_labor_cost_variance: float | Unset = UNSET
    summary_labor_units_percent_complete: float | Unset = UNSET
    summary_labor_units_variance: float | Unset = UNSET
    summary_material_cost_percent_complete: float | Unset = UNSET
    summary_material_cost_variance: float | Unset = UNSET
    summary_non_labor_cost_percent_complete: float | Unset = UNSET
    summary_non_labor_cost_variance: float | Unset = UNSET
    summary_non_labor_units_percent_complete: float | Unset = UNSET
    summary_non_labor_units_variance: float | Unset = UNSET
    summary_not_started_activity_count: int | Unset = UNSET
    summary_performance_percent_complete_by_labor_units: float | Unset = UNSET
    summary_planned_cost: float | Unset = UNSET
    summary_planned_duration: float | Unset = UNSET
    summary_planned_expense_cost: float | Unset = UNSET
    summary_planned_finish_date: datetime.datetime | Unset = UNSET
    summary_planned_labor_cost: float | Unset = UNSET
    summary_planned_labor_units: float | Unset = UNSET
    summary_planned_material_cost: float | Unset = UNSET
    summary_planned_non_labor_cost: float | Unset = UNSET
    summary_planned_non_labor_units: float | Unset = UNSET
    summary_planned_start_date: datetime.datetime | Unset = UNSET
    summary_planned_value_by_cost: float | Unset = UNSET
    summary_planned_value_by_labor_units: float | Unset = UNSET
    summary_progress_finish_date: datetime.datetime | Unset = UNSET
    summary_remaining_duration: float | Unset = UNSET
    summary_remaining_expense_cost: float | Unset = UNSET
    summary_remaining_finish_date: datetime.datetime | Unset = UNSET
    summary_remaining_labor_cost: float | Unset = UNSET
    summary_remaining_labor_units: float | Unset = UNSET
    summary_remaining_material_cost: float | Unset = UNSET
    summary_remaining_non_labor_cost: float | Unset = UNSET
    summary_remaining_non_labor_units: float | Unset = UNSET
    summary_remaining_start_date: datetime.datetime | Unset = UNSET
    summary_remaining_total_cost: float | Unset = UNSET
    summary_schedule_percent_complete: float | Unset = UNSET
    summary_schedule_percent_complete_by_labor_units: float | Unset = UNSET
    summary_schedule_performance_index_by_cost: float | Unset = UNSET
    summary_schedule_performance_index_by_labor_units: float | Unset = UNSET
    summary_schedule_variance_by_cost: float | Unset = UNSET
    summary_schedule_variance_by_labor_units: float | Unset = UNSET
    summary_schedule_variance_index: float | Unset = UNSET
    summary_schedule_variance_index_by_cost: float | Unset = UNSET
    summary_schedule_variance_index_by_labor_units: float | Unset = UNSET
    summary_start_date_variance: float | Unset = UNSET
    summary_to_complete_performance_index_by_cost: float | Unset = UNSET
    summary_total_cost_variance: float | Unset = UNSET
    summary_total_float: float | Unset = UNSET
    summary_units_percent_complete: float | Unset = UNSET
    summary_variance_at_completion_by_labor_units: float | Unset = UNSET
    team_member_activity_fields: str | Unset = UNSET
    team_member_assignment_option: str | Unset = UNSET
    team_member_resource_assignment_fields: str | Unset = UNSET
    team_member_step_udf_viewable_fields: str | Unset = UNSET
    team_member_viewable_fields: str | Unset = UNSET
    total_benefit_plan: float | Unset = UNSET
    total_benefit_plan_tally: float | Unset = UNSET
    total_spending_plan: float | Unset = UNSET
    total_spending_plan_tally: float | Unset = UNSET
    unallocated_budget: float | Unset = UNSET
    undistributed_current_variance: float | Unset = UNSET
    wbs_code_separator: str | Unset = UNSET
    wbs_object_id: int | Unset = UNSET
    web_site_root_directory: str | Unset = UNSET
    web_site_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        parent_eps_object_id = self.parent_eps_object_id

        activity_default_activity_type = self.activity_default_activity_type

        activity_default_calendar_object_id = self.activity_default_calendar_object_id

        activity_default_cost_account_object_id = self.activity_default_cost_account_object_id

        activity_default_duration_type = self.activity_default_duration_type

        activity_default_percent_complete_type = self.activity_default_percent_complete_type

        activity_default_price_per_unit = self.activity_default_price_per_unit

        activity_default_review_required = self.activity_default_review_required

        activity_id_based_on_selected_activity = self.activity_id_based_on_selected_activity

        activity_id_increment = self.activity_id_increment

        activity_id_prefix = self.activity_id_prefix

        activity_id_suffix = self.activity_id_suffix

        activity_percent_complete_based_on_activity_steps = self.activity_percent_complete_based_on_activity_steps

        add_actual_to_remaining = self.add_actual_to_remaining

        added_by = self.added_by

        allow_status_review = self.allow_status_review

        annual_discount_rate = self.annual_discount_rate

        anticipated_finish_date: str | Unset = UNSET
        if not isinstance(self.anticipated_finish_date, Unset):
            anticipated_finish_date = self.anticipated_finish_date.isoformat()

        anticipated_start_date: str | Unset = UNSET
        if not isinstance(self.anticipated_start_date, Unset):
            anticipated_start_date = self.anticipated_start_date.isoformat()

        assignment_default_driving_flag = self.assignment_default_driving_flag

        assignment_default_rate_type = self.assignment_default_rate_type

        baseline_type_name = self.baseline_type_name

        baseline_type_object_id = self.baseline_type_object_id

        check_out_date: str | Unset = UNSET
        if not isinstance(self.check_out_date, Unset):
            check_out_date = self.check_out_date.isoformat()

        check_out_status = self.check_out_status

        check_out_user_object_id = self.check_out_user_object_id

        contains_summary_data = self.contains_summary_data

        cost_quantity_recalculate_flag = self.cost_quantity_recalculate_flag

        create_date: str | Unset = UNSET
        if not isinstance(self.create_date, Unset):
            create_date = self.create_date.isoformat()

        create_user = self.create_user

        critical_activity_float_limit = self.critical_activity_float_limit

        critical_activity_path_type = self.critical_activity_path_type

        current_budget = self.current_budget

        current_variance = self.current_variance

        data_date: str | Unset = UNSET
        if not isinstance(self.data_date, Unset):
            data_date = self.data_date.isoformat()

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        default_price_time_units = self.default_price_time_units

        description = self.description

        discount_application_period = self.discount_application_period

        distributed_current_budget = self.distributed_current_budget

        enable_publication = self.enable_publication

        enable_summarization = self.enable_summarization

        financial_period_tmpl_id = self.financial_period_tmpl_id

        finish_date: str | Unset = UNSET
        if not isinstance(self.finish_date, Unset):
            finish_date = self.finish_date.isoformat()

        fiscal_year_start_month = self.fiscal_year_start_month

        forecast_finish_date: str | Unset = UNSET
        if not isinstance(self.forecast_finish_date, Unset):
            forecast_finish_date = self.forecast_finish_date.isoformat()

        forecast_start_date: str | Unset = UNSET
        if not isinstance(self.forecast_start_date, Unset):
            forecast_start_date = self.forecast_start_date.isoformat()

        guid = self.guid

        has_future_bucket_data = self.has_future_bucket_data

        history_interval = self.history_interval

        history_level = self.history_level

        independent_etc_labor_units = self.independent_etc_labor_units

        independent_etc_total_cost = self.independent_etc_total_cost

        last_baseline_update_date: str | Unset = UNSET
        if not isinstance(self.last_baseline_update_date, Unset):
            last_baseline_update_date = self.last_baseline_update_date.isoformat()

        last_financial_period_object_id = self.last_financial_period_object_id

        last_level_date: str | Unset = UNSET
        if not isinstance(self.last_level_date, Unset):
            last_level_date = self.last_level_date.isoformat()

        last_published_on: str | Unset = UNSET
        if not isinstance(self.last_published_on, Unset):
            last_published_on = self.last_published_on.isoformat()

        last_schedule_date: str | Unset = UNSET
        if not isinstance(self.last_schedule_date, Unset):
            last_schedule_date = self.last_schedule_date.isoformat()

        last_summarized_date: str | Unset = UNSET
        if not isinstance(self.last_summarized_date, Unset):
            last_summarized_date = self.last_summarized_date.isoformat()

        last_update_baseline_options = self.last_update_baseline_options

        last_update_date: str | Unset = UNSET
        if not isinstance(self.last_update_date, Unset):
            last_update_date = self.last_update_date.isoformat()

        last_update_user = self.last_update_user

        leveling_priority = self.leveling_priority

        link_actual_to_actual_this_period = self.link_actual_to_actual_this_period

        link_percent_complete_with_actual = self.link_percent_complete_with_actual

        link_planned_and_at_completion_flag = self.link_planned_and_at_completion_flag

        location_name = self.location_name

        location_object_id = self.location_object_id

        must_finish_by_date: str | Unset = UNSET
        if not isinstance(self.must_finish_by_date, Unset):
            must_finish_by_date = self.must_finish_by_date.isoformat()

        obs_name = self.obs_name

        obs_object_id = self.obs_object_id

        object_id = self.object_id

        original_budget = self.original_budget

        original_project_object_id = self.original_project_object_id

        owner_resource_object_id = self.owner_resource_object_id

        parent_eps_id = self.parent_eps_id

        parent_eps_name = self.parent_eps_name

        planned_start_date: str | Unset = UNSET
        if not isinstance(self.planned_start_date, Unset):
            planned_start_date = self.planned_start_date.isoformat()

        primary_resources_can_mark_activities_as_completed = self.primary_resources_can_mark_activities_as_completed

        project_forecast_start_date: str | Unset = UNSET
        if not isinstance(self.project_forecast_start_date, Unset):
            project_forecast_start_date = self.project_forecast_start_date.isoformat()

        project_schedule_type = self.project_schedule_type

        proposed_budget = self.proposed_budget

        publication_priority = self.publication_priority

        reset_planned_to_remaining_flag = self.reset_planned_to_remaining_flag

        resource_can_be_assigned_to_same_activity_more_than_once = (
            self.resource_can_be_assigned_to_same_activity_more_than_once
        )

        resource_name = self.resource_name

        resources_can_assign_themselves_to_activities = self.resources_can_assign_themselves_to_activities

        resources_can_assign_themselves_to_activities_outside_obs_access = (
            self.resources_can_assign_themselves_to_activities_outside_obs_access
        )

        resources_can_edit_assignment_percent_complete = self.resources_can_edit_assignment_percent_complete

        risk_exposure = self.risk_exposure

        risk_level = self.risk_level

        risk_matrix_object_id = self.risk_matrix_object_id

        risk_score = self.risk_score

        scheduled_finish_date: str | Unset = UNSET
        if not isinstance(self.scheduled_finish_date, Unset):
            scheduled_finish_date = self.scheduled_finish_date.isoformat()

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        status = self.status

        status_reviewer_name = self.status_reviewer_name

        status_reviewer_object_id = self.status_reviewer_object_id

        strategic_priority = self.strategic_priority

        summarize_to_wbs_level = self.summarize_to_wbs_level

        summarized_data_date: str | Unset = UNSET
        if not isinstance(self.summarized_data_date, Unset):
            summarized_data_date = self.summarized_data_date.isoformat()

        summary_accounting_variance_by_cost = self.summary_accounting_variance_by_cost

        summary_accounting_variance_by_labor_units = self.summary_accounting_variance_by_labor_units

        summary_activity_count = self.summary_activity_count

        summary_actual_duration = self.summary_actual_duration

        summary_actual_expense_cost = self.summary_actual_expense_cost

        summary_actual_finish_date: str | Unset = UNSET
        if not isinstance(self.summary_actual_finish_date, Unset):
            summary_actual_finish_date = self.summary_actual_finish_date.isoformat()

        summary_actual_labor_cost = self.summary_actual_labor_cost

        summary_actual_labor_units = self.summary_actual_labor_units

        summary_actual_material_cost = self.summary_actual_material_cost

        summary_actual_non_labor_cost = self.summary_actual_non_labor_cost

        summary_actual_non_labor_units = self.summary_actual_non_labor_units

        summary_actual_start_date: str | Unset = UNSET
        if not isinstance(self.summary_actual_start_date, Unset):
            summary_actual_start_date = self.summary_actual_start_date.isoformat()

        summary_actual_this_period_cost = self.summary_actual_this_period_cost

        summary_actual_this_period_labor_cost = self.summary_actual_this_period_labor_cost

        summary_actual_this_period_labor_units = self.summary_actual_this_period_labor_units

        summary_actual_this_period_material_cost = self.summary_actual_this_period_material_cost

        summary_actual_this_period_non_labor_cost = self.summary_actual_this_period_non_labor_cost

        summary_actual_this_period_non_labor_units = self.summary_actual_this_period_non_labor_units

        summary_actual_total_cost = self.summary_actual_total_cost

        summary_actual_value_by_cost = self.summary_actual_value_by_cost

        summary_actual_value_by_labor_units = self.summary_actual_value_by_labor_units

        summary_at_completion_duration = self.summary_at_completion_duration

        summary_at_completion_expense_cost = self.summary_at_completion_expense_cost

        summary_at_completion_labor_cost = self.summary_at_completion_labor_cost

        summary_at_completion_labor_units = self.summary_at_completion_labor_units

        summary_at_completion_material_cost = self.summary_at_completion_material_cost

        summary_at_completion_non_labor_cost = self.summary_at_completion_non_labor_cost

        summary_at_completion_non_labor_units = self.summary_at_completion_non_labor_units

        summary_at_completion_total_cost = self.summary_at_completion_total_cost

        summary_at_completion_total_cost_variance = self.summary_at_completion_total_cost_variance

        summary_baseline_completed_activity_count = self.summary_baseline_completed_activity_count

        summary_baseline_duration = self.summary_baseline_duration

        summary_baseline_expense_cost = self.summary_baseline_expense_cost

        summary_baseline_finish_date: str | Unset = UNSET
        if not isinstance(self.summary_baseline_finish_date, Unset):
            summary_baseline_finish_date = self.summary_baseline_finish_date.isoformat()

        summary_baseline_in_progress_activity_count = self.summary_baseline_in_progress_activity_count

        summary_baseline_labor_cost = self.summary_baseline_labor_cost

        summary_baseline_labor_units = self.summary_baseline_labor_units

        summary_baseline_material_cost = self.summary_baseline_material_cost

        summary_baseline_non_labor_cost = self.summary_baseline_non_labor_cost

        summary_baseline_non_labor_units = self.summary_baseline_non_labor_units

        summary_baseline_not_started_activity_count = self.summary_baseline_not_started_activity_count

        summary_baseline_start_date: str | Unset = UNSET
        if not isinstance(self.summary_baseline_start_date, Unset):
            summary_baseline_start_date = self.summary_baseline_start_date.isoformat()

        summary_baseline_total_cost = self.summary_baseline_total_cost

        summary_budget_at_completion_by_cost = self.summary_budget_at_completion_by_cost

        summary_budget_at_completion_by_labor_units = self.summary_budget_at_completion_by_labor_units

        summary_completed_activity_count = self.summary_completed_activity_count

        summary_cost_percent_complete = self.summary_cost_percent_complete

        summary_cost_percent_of_planned = self.summary_cost_percent_of_planned

        summary_cost_performance_index_by_cost = self.summary_cost_performance_index_by_cost

        summary_cost_performance_index_by_labor_units = self.summary_cost_performance_index_by_labor_units

        summary_cost_variance_by_cost = self.summary_cost_variance_by_cost

        summary_cost_variance_by_labor_units = self.summary_cost_variance_by_labor_units

        summary_cost_variance_index = self.summary_cost_variance_index

        summary_cost_variance_index_by_cost = self.summary_cost_variance_index_by_cost

        summary_cost_variance_index_by_labor_units = self.summary_cost_variance_index_by_labor_units

        summary_duration_percent_complete = self.summary_duration_percent_complete

        summary_duration_percent_of_planned = self.summary_duration_percent_of_planned

        summary_duration_variance = self.summary_duration_variance

        summary_earned_value_by_cost = self.summary_earned_value_by_cost

        summary_earned_value_by_labor_units = self.summary_earned_value_by_labor_units

        summary_estimate_at_completion_by_cost = self.summary_estimate_at_completion_by_cost

        summary_estimate_at_completion_by_labor_units = self.summary_estimate_at_completion_by_labor_units

        summary_estimate_at_completion_high_percent_by_labor_units = (
            self.summary_estimate_at_completion_high_percent_by_labor_units
        )

        summary_estimate_at_completion_low_percent_by_labor_units = (
            self.summary_estimate_at_completion_low_percent_by_labor_units
        )

        summary_estimate_to_complete_by_cost = self.summary_estimate_to_complete_by_cost

        summary_estimate_to_complete_by_labor_units = self.summary_estimate_to_complete_by_labor_units

        summary_expense_cost_percent_complete = self.summary_expense_cost_percent_complete

        summary_expense_cost_variance = self.summary_expense_cost_variance

        summary_finish_date_variance = self.summary_finish_date_variance

        summary_in_progress_activity_count = self.summary_in_progress_activity_count

        summary_labor_cost_percent_complete = self.summary_labor_cost_percent_complete

        summary_labor_cost_variance = self.summary_labor_cost_variance

        summary_labor_units_percent_complete = self.summary_labor_units_percent_complete

        summary_labor_units_variance = self.summary_labor_units_variance

        summary_material_cost_percent_complete = self.summary_material_cost_percent_complete

        summary_material_cost_variance = self.summary_material_cost_variance

        summary_non_labor_cost_percent_complete = self.summary_non_labor_cost_percent_complete

        summary_non_labor_cost_variance = self.summary_non_labor_cost_variance

        summary_non_labor_units_percent_complete = self.summary_non_labor_units_percent_complete

        summary_non_labor_units_variance = self.summary_non_labor_units_variance

        summary_not_started_activity_count = self.summary_not_started_activity_count

        summary_performance_percent_complete_by_labor_units = self.summary_performance_percent_complete_by_labor_units

        summary_planned_cost = self.summary_planned_cost

        summary_planned_duration = self.summary_planned_duration

        summary_planned_expense_cost = self.summary_planned_expense_cost

        summary_planned_finish_date: str | Unset = UNSET
        if not isinstance(self.summary_planned_finish_date, Unset):
            summary_planned_finish_date = self.summary_planned_finish_date.isoformat()

        summary_planned_labor_cost = self.summary_planned_labor_cost

        summary_planned_labor_units = self.summary_planned_labor_units

        summary_planned_material_cost = self.summary_planned_material_cost

        summary_planned_non_labor_cost = self.summary_planned_non_labor_cost

        summary_planned_non_labor_units = self.summary_planned_non_labor_units

        summary_planned_start_date: str | Unset = UNSET
        if not isinstance(self.summary_planned_start_date, Unset):
            summary_planned_start_date = self.summary_planned_start_date.isoformat()

        summary_planned_value_by_cost = self.summary_planned_value_by_cost

        summary_planned_value_by_labor_units = self.summary_planned_value_by_labor_units

        summary_progress_finish_date: str | Unset = UNSET
        if not isinstance(self.summary_progress_finish_date, Unset):
            summary_progress_finish_date = self.summary_progress_finish_date.isoformat()

        summary_remaining_duration = self.summary_remaining_duration

        summary_remaining_expense_cost = self.summary_remaining_expense_cost

        summary_remaining_finish_date: str | Unset = UNSET
        if not isinstance(self.summary_remaining_finish_date, Unset):
            summary_remaining_finish_date = self.summary_remaining_finish_date.isoformat()

        summary_remaining_labor_cost = self.summary_remaining_labor_cost

        summary_remaining_labor_units = self.summary_remaining_labor_units

        summary_remaining_material_cost = self.summary_remaining_material_cost

        summary_remaining_non_labor_cost = self.summary_remaining_non_labor_cost

        summary_remaining_non_labor_units = self.summary_remaining_non_labor_units

        summary_remaining_start_date: str | Unset = UNSET
        if not isinstance(self.summary_remaining_start_date, Unset):
            summary_remaining_start_date = self.summary_remaining_start_date.isoformat()

        summary_remaining_total_cost = self.summary_remaining_total_cost

        summary_schedule_percent_complete = self.summary_schedule_percent_complete

        summary_schedule_percent_complete_by_labor_units = self.summary_schedule_percent_complete_by_labor_units

        summary_schedule_performance_index_by_cost = self.summary_schedule_performance_index_by_cost

        summary_schedule_performance_index_by_labor_units = self.summary_schedule_performance_index_by_labor_units

        summary_schedule_variance_by_cost = self.summary_schedule_variance_by_cost

        summary_schedule_variance_by_labor_units = self.summary_schedule_variance_by_labor_units

        summary_schedule_variance_index = self.summary_schedule_variance_index

        summary_schedule_variance_index_by_cost = self.summary_schedule_variance_index_by_cost

        summary_schedule_variance_index_by_labor_units = self.summary_schedule_variance_index_by_labor_units

        summary_start_date_variance = self.summary_start_date_variance

        summary_to_complete_performance_index_by_cost = self.summary_to_complete_performance_index_by_cost

        summary_total_cost_variance = self.summary_total_cost_variance

        summary_total_float = self.summary_total_float

        summary_units_percent_complete = self.summary_units_percent_complete

        summary_variance_at_completion_by_labor_units = self.summary_variance_at_completion_by_labor_units

        team_member_activity_fields = self.team_member_activity_fields

        team_member_assignment_option = self.team_member_assignment_option

        team_member_resource_assignment_fields = self.team_member_resource_assignment_fields

        team_member_step_udf_viewable_fields = self.team_member_step_udf_viewable_fields

        team_member_viewable_fields = self.team_member_viewable_fields

        total_benefit_plan = self.total_benefit_plan

        total_benefit_plan_tally = self.total_benefit_plan_tally

        total_spending_plan = self.total_spending_plan

        total_spending_plan_tally = self.total_spending_plan_tally

        unallocated_budget = self.unallocated_budget

        undistributed_current_variance = self.undistributed_current_variance

        wbs_code_separator = self.wbs_code_separator

        wbs_object_id = self.wbs_object_id

        web_site_root_directory = self.web_site_root_directory

        web_site_url = self.web_site_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Id": id,
                "Name": name,
                "ParentEPSObjectId": parent_eps_object_id,
            }
        )
        if activity_default_activity_type is not UNSET:
            field_dict["ActivityDefaultActivityType"] = activity_default_activity_type
        if activity_default_calendar_object_id is not UNSET:
            field_dict["ActivityDefaultCalendarObjectId"] = activity_default_calendar_object_id
        if activity_default_cost_account_object_id is not UNSET:
            field_dict["ActivityDefaultCostAccountObjectId"] = activity_default_cost_account_object_id
        if activity_default_duration_type is not UNSET:
            field_dict["ActivityDefaultDurationType"] = activity_default_duration_type
        if activity_default_percent_complete_type is not UNSET:
            field_dict["ActivityDefaultPercentCompleteType"] = activity_default_percent_complete_type
        if activity_default_price_per_unit is not UNSET:
            field_dict["ActivityDefaultPricePerUnit"] = activity_default_price_per_unit
        if activity_default_review_required is not UNSET:
            field_dict["ActivityDefaultReviewRequired"] = activity_default_review_required
        if activity_id_based_on_selected_activity is not UNSET:
            field_dict["ActivityIdBasedOnSelectedActivity"] = activity_id_based_on_selected_activity
        if activity_id_increment is not UNSET:
            field_dict["ActivityIdIncrement"] = activity_id_increment
        if activity_id_prefix is not UNSET:
            field_dict["ActivityIdPrefix"] = activity_id_prefix
        if activity_id_suffix is not UNSET:
            field_dict["ActivityIdSuffix"] = activity_id_suffix
        if activity_percent_complete_based_on_activity_steps is not UNSET:
            field_dict["ActivityPercentCompleteBasedOnActivitySteps"] = (
                activity_percent_complete_based_on_activity_steps
            )
        if add_actual_to_remaining is not UNSET:
            field_dict["AddActualToRemaining"] = add_actual_to_remaining
        if added_by is not UNSET:
            field_dict["AddedBy"] = added_by
        if allow_status_review is not UNSET:
            field_dict["AllowStatusReview"] = allow_status_review
        if annual_discount_rate is not UNSET:
            field_dict["AnnualDiscountRate"] = annual_discount_rate
        if anticipated_finish_date is not UNSET:
            field_dict["AnticipatedFinishDate"] = anticipated_finish_date
        if anticipated_start_date is not UNSET:
            field_dict["AnticipatedStartDate"] = anticipated_start_date
        if assignment_default_driving_flag is not UNSET:
            field_dict["AssignmentDefaultDrivingFlag"] = assignment_default_driving_flag
        if assignment_default_rate_type is not UNSET:
            field_dict["AssignmentDefaultRateType"] = assignment_default_rate_type
        if baseline_type_name is not UNSET:
            field_dict["BaselineTypeName"] = baseline_type_name
        if baseline_type_object_id is not UNSET:
            field_dict["BaselineTypeObjectId"] = baseline_type_object_id
        if check_out_date is not UNSET:
            field_dict["CheckOutDate"] = check_out_date
        if check_out_status is not UNSET:
            field_dict["CheckOutStatus"] = check_out_status
        if check_out_user_object_id is not UNSET:
            field_dict["CheckOutUserObjectId"] = check_out_user_object_id
        if contains_summary_data is not UNSET:
            field_dict["ContainsSummaryData"] = contains_summary_data
        if cost_quantity_recalculate_flag is not UNSET:
            field_dict["CostQuantityRecalculateFlag"] = cost_quantity_recalculate_flag
        if create_date is not UNSET:
            field_dict["CreateDate"] = create_date
        if create_user is not UNSET:
            field_dict["CreateUser"] = create_user
        if critical_activity_float_limit is not UNSET:
            field_dict["CriticalActivityFloatLimit"] = critical_activity_float_limit
        if critical_activity_path_type is not UNSET:
            field_dict["CriticalActivityPathType"] = critical_activity_path_type
        if current_budget is not UNSET:
            field_dict["CurrentBudget"] = current_budget
        if current_variance is not UNSET:
            field_dict["CurrentVariance"] = current_variance
        if data_date is not UNSET:
            field_dict["DataDate"] = data_date
        if date_added is not UNSET:
            field_dict["DateAdded"] = date_added
        if default_price_time_units is not UNSET:
            field_dict["DefaultPriceTimeUnits"] = default_price_time_units
        if description is not UNSET:
            field_dict["Description"] = description
        if discount_application_period is not UNSET:
            field_dict["DiscountApplicationPeriod"] = discount_application_period
        if distributed_current_budget is not UNSET:
            field_dict["DistributedCurrentBudget"] = distributed_current_budget
        if enable_publication is not UNSET:
            field_dict["EnablePublication"] = enable_publication
        if enable_summarization is not UNSET:
            field_dict["EnableSummarization"] = enable_summarization
        if financial_period_tmpl_id is not UNSET:
            field_dict["FinancialPeriodTmplId"] = financial_period_tmpl_id
        if finish_date is not UNSET:
            field_dict["FinishDate"] = finish_date
        if fiscal_year_start_month is not UNSET:
            field_dict["FiscalYearStartMonth"] = fiscal_year_start_month
        if forecast_finish_date is not UNSET:
            field_dict["ForecastFinishDate"] = forecast_finish_date
        if forecast_start_date is not UNSET:
            field_dict["ForecastStartDate"] = forecast_start_date
        if guid is not UNSET:
            field_dict["GUID"] = guid
        if has_future_bucket_data is not UNSET:
            field_dict["HasFutureBucketData"] = has_future_bucket_data
        if history_interval is not UNSET:
            field_dict["HistoryInterval"] = history_interval
        if history_level is not UNSET:
            field_dict["HistoryLevel"] = history_level
        if independent_etc_labor_units is not UNSET:
            field_dict["IndependentETCLaborUnits"] = independent_etc_labor_units
        if independent_etc_total_cost is not UNSET:
            field_dict["IndependentETCTotalCost"] = independent_etc_total_cost
        if last_baseline_update_date is not UNSET:
            field_dict["LastBaselineUpdateDate"] = last_baseline_update_date
        if last_financial_period_object_id is not UNSET:
            field_dict["LastFinancialPeriodObjectId"] = last_financial_period_object_id
        if last_level_date is not UNSET:
            field_dict["LastLevelDate"] = last_level_date
        if last_published_on is not UNSET:
            field_dict["LastPublishedOn"] = last_published_on
        if last_schedule_date is not UNSET:
            field_dict["LastScheduleDate"] = last_schedule_date
        if last_summarized_date is not UNSET:
            field_dict["LastSummarizedDate"] = last_summarized_date
        if last_update_baseline_options is not UNSET:
            field_dict["LastUpdateBaselineOptions"] = last_update_baseline_options
        if last_update_date is not UNSET:
            field_dict["LastUpdateDate"] = last_update_date
        if last_update_user is not UNSET:
            field_dict["LastUpdateUser"] = last_update_user
        if leveling_priority is not UNSET:
            field_dict["LevelingPriority"] = leveling_priority
        if link_actual_to_actual_this_period is not UNSET:
            field_dict["LinkActualToActualThisPeriod"] = link_actual_to_actual_this_period
        if link_percent_complete_with_actual is not UNSET:
            field_dict["LinkPercentCompleteWithActual"] = link_percent_complete_with_actual
        if link_planned_and_at_completion_flag is not UNSET:
            field_dict["LinkPlannedAndAtCompletionFlag"] = link_planned_and_at_completion_flag
        if location_name is not UNSET:
            field_dict["LocationName"] = location_name
        if location_object_id is not UNSET:
            field_dict["LocationObjectId"] = location_object_id
        if must_finish_by_date is not UNSET:
            field_dict["MustFinishByDate"] = must_finish_by_date
        if obs_name is not UNSET:
            field_dict["OBSName"] = obs_name
        if obs_object_id is not UNSET:
            field_dict["OBSObjectId"] = obs_object_id
        if object_id is not UNSET:
            field_dict["ObjectId"] = object_id
        if original_budget is not UNSET:
            field_dict["OriginalBudget"] = original_budget
        if original_project_object_id is not UNSET:
            field_dict["OriginalProjectObjectId"] = original_project_object_id
        if owner_resource_object_id is not UNSET:
            field_dict["OwnerResourceObjectId"] = owner_resource_object_id
        if parent_eps_id is not UNSET:
            field_dict["ParentEPSId"] = parent_eps_id
        if parent_eps_name is not UNSET:
            field_dict["ParentEPSName"] = parent_eps_name
        if planned_start_date is not UNSET:
            field_dict["PlannedStartDate"] = planned_start_date
        if primary_resources_can_mark_activities_as_completed is not UNSET:
            field_dict["PrimaryResourcesCanMarkActivitiesAsCompleted"] = (
                primary_resources_can_mark_activities_as_completed
            )
        if project_forecast_start_date is not UNSET:
            field_dict["ProjectForecastStartDate"] = project_forecast_start_date
        if project_schedule_type is not UNSET:
            field_dict["ProjectScheduleType"] = project_schedule_type
        if proposed_budget is not UNSET:
            field_dict["ProposedBudget"] = proposed_budget
        if publication_priority is not UNSET:
            field_dict["PublicationPriority"] = publication_priority
        if reset_planned_to_remaining_flag is not UNSET:
            field_dict["ResetPlannedToRemainingFlag"] = reset_planned_to_remaining_flag
        if resource_can_be_assigned_to_same_activity_more_than_once is not UNSET:
            field_dict["ResourceCanBeAssignedToSameActivityMoreThanOnce"] = (
                resource_can_be_assigned_to_same_activity_more_than_once
            )
        if resource_name is not UNSET:
            field_dict["ResourceName"] = resource_name
        if resources_can_assign_themselves_to_activities is not UNSET:
            field_dict["ResourcesCanAssignThemselvesToActivities"] = resources_can_assign_themselves_to_activities
        if resources_can_assign_themselves_to_activities_outside_obs_access is not UNSET:
            field_dict["ResourcesCanAssignThemselvesToActivitiesOutsideOBSAccess"] = (
                resources_can_assign_themselves_to_activities_outside_obs_access
            )
        if resources_can_edit_assignment_percent_complete is not UNSET:
            field_dict["ResourcesCanEditAssignmentPercentComplete"] = resources_can_edit_assignment_percent_complete
        if risk_exposure is not UNSET:
            field_dict["RiskExposure"] = risk_exposure
        if risk_level is not UNSET:
            field_dict["RiskLevel"] = risk_level
        if risk_matrix_object_id is not UNSET:
            field_dict["RiskMatrixObjectId"] = risk_matrix_object_id
        if risk_score is not UNSET:
            field_dict["RiskScore"] = risk_score
        if scheduled_finish_date is not UNSET:
            field_dict["ScheduledFinishDate"] = scheduled_finish_date
        if start_date is not UNSET:
            field_dict["StartDate"] = start_date
        if status is not UNSET:
            field_dict["Status"] = status
        if status_reviewer_name is not UNSET:
            field_dict["StatusReviewerName"] = status_reviewer_name
        if status_reviewer_object_id is not UNSET:
            field_dict["StatusReviewerObjectId"] = status_reviewer_object_id
        if strategic_priority is not UNSET:
            field_dict["StrategicPriority"] = strategic_priority
        if summarize_to_wbs_level is not UNSET:
            field_dict["SummarizeToWBSLevel"] = summarize_to_wbs_level
        if summarized_data_date is not UNSET:
            field_dict["SummarizedDataDate"] = summarized_data_date
        if summary_accounting_variance_by_cost is not UNSET:
            field_dict["SummaryAccountingVarianceByCost"] = summary_accounting_variance_by_cost
        if summary_accounting_variance_by_labor_units is not UNSET:
            field_dict["SummaryAccountingVarianceByLaborUnits"] = summary_accounting_variance_by_labor_units
        if summary_activity_count is not UNSET:
            field_dict["SummaryActivityCount"] = summary_activity_count
        if summary_actual_duration is not UNSET:
            field_dict["SummaryActualDuration"] = summary_actual_duration
        if summary_actual_expense_cost is not UNSET:
            field_dict["SummaryActualExpenseCost"] = summary_actual_expense_cost
        if summary_actual_finish_date is not UNSET:
            field_dict["SummaryActualFinishDate"] = summary_actual_finish_date
        if summary_actual_labor_cost is not UNSET:
            field_dict["SummaryActualLaborCost"] = summary_actual_labor_cost
        if summary_actual_labor_units is not UNSET:
            field_dict["SummaryActualLaborUnits"] = summary_actual_labor_units
        if summary_actual_material_cost is not UNSET:
            field_dict["SummaryActualMaterialCost"] = summary_actual_material_cost
        if summary_actual_non_labor_cost is not UNSET:
            field_dict["SummaryActualNonLaborCost"] = summary_actual_non_labor_cost
        if summary_actual_non_labor_units is not UNSET:
            field_dict["SummaryActualNonLaborUnits"] = summary_actual_non_labor_units
        if summary_actual_start_date is not UNSET:
            field_dict["SummaryActualStartDate"] = summary_actual_start_date
        if summary_actual_this_period_cost is not UNSET:
            field_dict["SummaryActualThisPeriodCost"] = summary_actual_this_period_cost
        if summary_actual_this_period_labor_cost is not UNSET:
            field_dict["SummaryActualThisPeriodLaborCost"] = summary_actual_this_period_labor_cost
        if summary_actual_this_period_labor_units is not UNSET:
            field_dict["SummaryActualThisPeriodLaborUnits"] = summary_actual_this_period_labor_units
        if summary_actual_this_period_material_cost is not UNSET:
            field_dict["SummaryActualThisPeriodMaterialCost"] = summary_actual_this_period_material_cost
        if summary_actual_this_period_non_labor_cost is not UNSET:
            field_dict["SummaryActualThisPeriodNonLaborCost"] = summary_actual_this_period_non_labor_cost
        if summary_actual_this_period_non_labor_units is not UNSET:
            field_dict["SummaryActualThisPeriodNonLaborUnits"] = summary_actual_this_period_non_labor_units
        if summary_actual_total_cost is not UNSET:
            field_dict["SummaryActualTotalCost"] = summary_actual_total_cost
        if summary_actual_value_by_cost is not UNSET:
            field_dict["SummaryActualValueByCost"] = summary_actual_value_by_cost
        if summary_actual_value_by_labor_units is not UNSET:
            field_dict["SummaryActualValueByLaborUnits"] = summary_actual_value_by_labor_units
        if summary_at_completion_duration is not UNSET:
            field_dict["SummaryAtCompletionDuration"] = summary_at_completion_duration
        if summary_at_completion_expense_cost is not UNSET:
            field_dict["SummaryAtCompletionExpenseCost"] = summary_at_completion_expense_cost
        if summary_at_completion_labor_cost is not UNSET:
            field_dict["SummaryAtCompletionLaborCost"] = summary_at_completion_labor_cost
        if summary_at_completion_labor_units is not UNSET:
            field_dict["SummaryAtCompletionLaborUnits"] = summary_at_completion_labor_units
        if summary_at_completion_material_cost is not UNSET:
            field_dict["SummaryAtCompletionMaterialCost"] = summary_at_completion_material_cost
        if summary_at_completion_non_labor_cost is not UNSET:
            field_dict["SummaryAtCompletionNonLaborCost"] = summary_at_completion_non_labor_cost
        if summary_at_completion_non_labor_units is not UNSET:
            field_dict["SummaryAtCompletionNonLaborUnits"] = summary_at_completion_non_labor_units
        if summary_at_completion_total_cost is not UNSET:
            field_dict["SummaryAtCompletionTotalCost"] = summary_at_completion_total_cost
        if summary_at_completion_total_cost_variance is not UNSET:
            field_dict["SummaryAtCompletionTotalCostVariance"] = summary_at_completion_total_cost_variance
        if summary_baseline_completed_activity_count is not UNSET:
            field_dict["SummaryBaselineCompletedActivityCount"] = summary_baseline_completed_activity_count
        if summary_baseline_duration is not UNSET:
            field_dict["SummaryBaselineDuration"] = summary_baseline_duration
        if summary_baseline_expense_cost is not UNSET:
            field_dict["SummaryBaselineExpenseCost"] = summary_baseline_expense_cost
        if summary_baseline_finish_date is not UNSET:
            field_dict["SummaryBaselineFinishDate"] = summary_baseline_finish_date
        if summary_baseline_in_progress_activity_count is not UNSET:
            field_dict["SummaryBaselineInProgressActivityCount"] = summary_baseline_in_progress_activity_count
        if summary_baseline_labor_cost is not UNSET:
            field_dict["SummaryBaselineLaborCost"] = summary_baseline_labor_cost
        if summary_baseline_labor_units is not UNSET:
            field_dict["SummaryBaselineLaborUnits"] = summary_baseline_labor_units
        if summary_baseline_material_cost is not UNSET:
            field_dict["SummaryBaselineMaterialCost"] = summary_baseline_material_cost
        if summary_baseline_non_labor_cost is not UNSET:
            field_dict["SummaryBaselineNonLaborCost"] = summary_baseline_non_labor_cost
        if summary_baseline_non_labor_units is not UNSET:
            field_dict["SummaryBaselineNonLaborUnits"] = summary_baseline_non_labor_units
        if summary_baseline_not_started_activity_count is not UNSET:
            field_dict["SummaryBaselineNotStartedActivityCount"] = summary_baseline_not_started_activity_count
        if summary_baseline_start_date is not UNSET:
            field_dict["SummaryBaselineStartDate"] = summary_baseline_start_date
        if summary_baseline_total_cost is not UNSET:
            field_dict["SummaryBaselineTotalCost"] = summary_baseline_total_cost
        if summary_budget_at_completion_by_cost is not UNSET:
            field_dict["SummaryBudgetAtCompletionByCost"] = summary_budget_at_completion_by_cost
        if summary_budget_at_completion_by_labor_units is not UNSET:
            field_dict["SummaryBudgetAtCompletionByLaborUnits"] = summary_budget_at_completion_by_labor_units
        if summary_completed_activity_count is not UNSET:
            field_dict["SummaryCompletedActivityCount"] = summary_completed_activity_count
        if summary_cost_percent_complete is not UNSET:
            field_dict["SummaryCostPercentComplete"] = summary_cost_percent_complete
        if summary_cost_percent_of_planned is not UNSET:
            field_dict["SummaryCostPercentOfPlanned"] = summary_cost_percent_of_planned
        if summary_cost_performance_index_by_cost is not UNSET:
            field_dict["SummaryCostPerformanceIndexByCost"] = summary_cost_performance_index_by_cost
        if summary_cost_performance_index_by_labor_units is not UNSET:
            field_dict["SummaryCostPerformanceIndexByLaborUnits"] = summary_cost_performance_index_by_labor_units
        if summary_cost_variance_by_cost is not UNSET:
            field_dict["SummaryCostVarianceByCost"] = summary_cost_variance_by_cost
        if summary_cost_variance_by_labor_units is not UNSET:
            field_dict["SummaryCostVarianceByLaborUnits"] = summary_cost_variance_by_labor_units
        if summary_cost_variance_index is not UNSET:
            field_dict["SummaryCostVarianceIndex"] = summary_cost_variance_index
        if summary_cost_variance_index_by_cost is not UNSET:
            field_dict["SummaryCostVarianceIndexByCost"] = summary_cost_variance_index_by_cost
        if summary_cost_variance_index_by_labor_units is not UNSET:
            field_dict["SummaryCostVarianceIndexByLaborUnits"] = summary_cost_variance_index_by_labor_units
        if summary_duration_percent_complete is not UNSET:
            field_dict["SummaryDurationPercentComplete"] = summary_duration_percent_complete
        if summary_duration_percent_of_planned is not UNSET:
            field_dict["SummaryDurationPercentOfPlanned"] = summary_duration_percent_of_planned
        if summary_duration_variance is not UNSET:
            field_dict["SummaryDurationVariance"] = summary_duration_variance
        if summary_earned_value_by_cost is not UNSET:
            field_dict["SummaryEarnedValueByCost"] = summary_earned_value_by_cost
        if summary_earned_value_by_labor_units is not UNSET:
            field_dict["SummaryEarnedValueByLaborUnits"] = summary_earned_value_by_labor_units
        if summary_estimate_at_completion_by_cost is not UNSET:
            field_dict["SummaryEstimateAtCompletionByCost"] = summary_estimate_at_completion_by_cost
        if summary_estimate_at_completion_by_labor_units is not UNSET:
            field_dict["SummaryEstimateAtCompletionByLaborUnits"] = summary_estimate_at_completion_by_labor_units
        if summary_estimate_at_completion_high_percent_by_labor_units is not UNSET:
            field_dict["SummaryEstimateAtCompletionHighPercentByLaborUnits"] = (
                summary_estimate_at_completion_high_percent_by_labor_units
            )
        if summary_estimate_at_completion_low_percent_by_labor_units is not UNSET:
            field_dict["SummaryEstimateAtCompletionLowPercentByLaborUnits"] = (
                summary_estimate_at_completion_low_percent_by_labor_units
            )
        if summary_estimate_to_complete_by_cost is not UNSET:
            field_dict["SummaryEstimateToCompleteByCost"] = summary_estimate_to_complete_by_cost
        if summary_estimate_to_complete_by_labor_units is not UNSET:
            field_dict["SummaryEstimateToCompleteByLaborUnits"] = summary_estimate_to_complete_by_labor_units
        if summary_expense_cost_percent_complete is not UNSET:
            field_dict["SummaryExpenseCostPercentComplete"] = summary_expense_cost_percent_complete
        if summary_expense_cost_variance is not UNSET:
            field_dict["SummaryExpenseCostVariance"] = summary_expense_cost_variance
        if summary_finish_date_variance is not UNSET:
            field_dict["SummaryFinishDateVariance"] = summary_finish_date_variance
        if summary_in_progress_activity_count is not UNSET:
            field_dict["SummaryInProgressActivityCount"] = summary_in_progress_activity_count
        if summary_labor_cost_percent_complete is not UNSET:
            field_dict["SummaryLaborCostPercentComplete"] = summary_labor_cost_percent_complete
        if summary_labor_cost_variance is not UNSET:
            field_dict["SummaryLaborCostVariance"] = summary_labor_cost_variance
        if summary_labor_units_percent_complete is not UNSET:
            field_dict["SummaryLaborUnitsPercentComplete"] = summary_labor_units_percent_complete
        if summary_labor_units_variance is not UNSET:
            field_dict["SummaryLaborUnitsVariance"] = summary_labor_units_variance
        if summary_material_cost_percent_complete is not UNSET:
            field_dict["SummaryMaterialCostPercentComplete"] = summary_material_cost_percent_complete
        if summary_material_cost_variance is not UNSET:
            field_dict["SummaryMaterialCostVariance"] = summary_material_cost_variance
        if summary_non_labor_cost_percent_complete is not UNSET:
            field_dict["SummaryNonLaborCostPercentComplete"] = summary_non_labor_cost_percent_complete
        if summary_non_labor_cost_variance is not UNSET:
            field_dict["SummaryNonLaborCostVariance"] = summary_non_labor_cost_variance
        if summary_non_labor_units_percent_complete is not UNSET:
            field_dict["SummaryNonLaborUnitsPercentComplete"] = summary_non_labor_units_percent_complete
        if summary_non_labor_units_variance is not UNSET:
            field_dict["SummaryNonLaborUnitsVariance"] = summary_non_labor_units_variance
        if summary_not_started_activity_count is not UNSET:
            field_dict["SummaryNotStartedActivityCount"] = summary_not_started_activity_count
        if summary_performance_percent_complete_by_labor_units is not UNSET:
            field_dict["SummaryPerformancePercentCompleteByLaborUnits"] = (
                summary_performance_percent_complete_by_labor_units
            )
        if summary_planned_cost is not UNSET:
            field_dict["SummaryPlannedCost"] = summary_planned_cost
        if summary_planned_duration is not UNSET:
            field_dict["SummaryPlannedDuration"] = summary_planned_duration
        if summary_planned_expense_cost is not UNSET:
            field_dict["SummaryPlannedExpenseCost"] = summary_planned_expense_cost
        if summary_planned_finish_date is not UNSET:
            field_dict["SummaryPlannedFinishDate"] = summary_planned_finish_date
        if summary_planned_labor_cost is not UNSET:
            field_dict["SummaryPlannedLaborCost"] = summary_planned_labor_cost
        if summary_planned_labor_units is not UNSET:
            field_dict["SummaryPlannedLaborUnits"] = summary_planned_labor_units
        if summary_planned_material_cost is not UNSET:
            field_dict["SummaryPlannedMaterialCost"] = summary_planned_material_cost
        if summary_planned_non_labor_cost is not UNSET:
            field_dict["SummaryPlannedNonLaborCost"] = summary_planned_non_labor_cost
        if summary_planned_non_labor_units is not UNSET:
            field_dict["SummaryPlannedNonLaborUnits"] = summary_planned_non_labor_units
        if summary_planned_start_date is not UNSET:
            field_dict["SummaryPlannedStartDate"] = summary_planned_start_date
        if summary_planned_value_by_cost is not UNSET:
            field_dict["SummaryPlannedValueByCost"] = summary_planned_value_by_cost
        if summary_planned_value_by_labor_units is not UNSET:
            field_dict["SummaryPlannedValueByLaborUnits"] = summary_planned_value_by_labor_units
        if summary_progress_finish_date is not UNSET:
            field_dict["SummaryProgressFinishDate"] = summary_progress_finish_date
        if summary_remaining_duration is not UNSET:
            field_dict["SummaryRemainingDuration"] = summary_remaining_duration
        if summary_remaining_expense_cost is not UNSET:
            field_dict["SummaryRemainingExpenseCost"] = summary_remaining_expense_cost
        if summary_remaining_finish_date is not UNSET:
            field_dict["SummaryRemainingFinishDate"] = summary_remaining_finish_date
        if summary_remaining_labor_cost is not UNSET:
            field_dict["SummaryRemainingLaborCost"] = summary_remaining_labor_cost
        if summary_remaining_labor_units is not UNSET:
            field_dict["SummaryRemainingLaborUnits"] = summary_remaining_labor_units
        if summary_remaining_material_cost is not UNSET:
            field_dict["SummaryRemainingMaterialCost"] = summary_remaining_material_cost
        if summary_remaining_non_labor_cost is not UNSET:
            field_dict["SummaryRemainingNonLaborCost"] = summary_remaining_non_labor_cost
        if summary_remaining_non_labor_units is not UNSET:
            field_dict["SummaryRemainingNonLaborUnits"] = summary_remaining_non_labor_units
        if summary_remaining_start_date is not UNSET:
            field_dict["SummaryRemainingStartDate"] = summary_remaining_start_date
        if summary_remaining_total_cost is not UNSET:
            field_dict["SummaryRemainingTotalCost"] = summary_remaining_total_cost
        if summary_schedule_percent_complete is not UNSET:
            field_dict["SummarySchedulePercentComplete"] = summary_schedule_percent_complete
        if summary_schedule_percent_complete_by_labor_units is not UNSET:
            field_dict["SummarySchedulePercentCompleteByLaborUnits"] = summary_schedule_percent_complete_by_labor_units
        if summary_schedule_performance_index_by_cost is not UNSET:
            field_dict["SummarySchedulePerformanceIndexByCost"] = summary_schedule_performance_index_by_cost
        if summary_schedule_performance_index_by_labor_units is not UNSET:
            field_dict["SummarySchedulePerformanceIndexByLaborUnits"] = (
                summary_schedule_performance_index_by_labor_units
            )
        if summary_schedule_variance_by_cost is not UNSET:
            field_dict["SummaryScheduleVarianceByCost"] = summary_schedule_variance_by_cost
        if summary_schedule_variance_by_labor_units is not UNSET:
            field_dict["SummaryScheduleVarianceByLaborUnits"] = summary_schedule_variance_by_labor_units
        if summary_schedule_variance_index is not UNSET:
            field_dict["SummaryScheduleVarianceIndex"] = summary_schedule_variance_index
        if summary_schedule_variance_index_by_cost is not UNSET:
            field_dict["SummaryScheduleVarianceIndexByCost"] = summary_schedule_variance_index_by_cost
        if summary_schedule_variance_index_by_labor_units is not UNSET:
            field_dict["SummaryScheduleVarianceIndexByLaborUnits"] = summary_schedule_variance_index_by_labor_units
        if summary_start_date_variance is not UNSET:
            field_dict["SummaryStartDateVariance"] = summary_start_date_variance
        if summary_to_complete_performance_index_by_cost is not UNSET:
            field_dict["SummaryToCompletePerformanceIndexByCost"] = summary_to_complete_performance_index_by_cost
        if summary_total_cost_variance is not UNSET:
            field_dict["SummaryTotalCostVariance"] = summary_total_cost_variance
        if summary_total_float is not UNSET:
            field_dict["SummaryTotalFloat"] = summary_total_float
        if summary_units_percent_complete is not UNSET:
            field_dict["SummaryUnitsPercentComplete"] = summary_units_percent_complete
        if summary_variance_at_completion_by_labor_units is not UNSET:
            field_dict["SummaryVarianceAtCompletionByLaborUnits"] = summary_variance_at_completion_by_labor_units
        if team_member_activity_fields is not UNSET:
            field_dict["TeamMemberActivityFields"] = team_member_activity_fields
        if team_member_assignment_option is not UNSET:
            field_dict["TeamMemberAssignmentOption"] = team_member_assignment_option
        if team_member_resource_assignment_fields is not UNSET:
            field_dict["TeamMemberResourceAssignmentFields"] = team_member_resource_assignment_fields
        if team_member_step_udf_viewable_fields is not UNSET:
            field_dict["TeamMemberStepUDFViewableFields"] = team_member_step_udf_viewable_fields
        if team_member_viewable_fields is not UNSET:
            field_dict["TeamMemberViewableFields"] = team_member_viewable_fields
        if total_benefit_plan is not UNSET:
            field_dict["TotalBenefitPlan"] = total_benefit_plan
        if total_benefit_plan_tally is not UNSET:
            field_dict["TotalBenefitPlanTally"] = total_benefit_plan_tally
        if total_spending_plan is not UNSET:
            field_dict["TotalSpendingPlan"] = total_spending_plan
        if total_spending_plan_tally is not UNSET:
            field_dict["TotalSpendingPlanTally"] = total_spending_plan_tally
        if unallocated_budget is not UNSET:
            field_dict["UnallocatedBudget"] = unallocated_budget
        if undistributed_current_variance is not UNSET:
            field_dict["UndistributedCurrentVariance"] = undistributed_current_variance
        if wbs_code_separator is not UNSET:
            field_dict["WBSCodeSeparator"] = wbs_code_separator
        if wbs_object_id is not UNSET:
            field_dict["WBSObjectId"] = wbs_object_id
        if web_site_root_directory is not UNSET:
            field_dict["WebSiteRootDirectory"] = web_site_root_directory
        if web_site_url is not UNSET:
            field_dict["WebSiteURL"] = web_site_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("Id")

        name = d.pop("Name")

        parent_eps_object_id = d.pop("ParentEPSObjectId")

        activity_default_activity_type = d.pop("ActivityDefaultActivityType", UNSET)

        activity_default_calendar_object_id = d.pop("ActivityDefaultCalendarObjectId", UNSET)

        activity_default_cost_account_object_id = d.pop("ActivityDefaultCostAccountObjectId", UNSET)

        activity_default_duration_type = d.pop("ActivityDefaultDurationType", UNSET)

        activity_default_percent_complete_type = d.pop("ActivityDefaultPercentCompleteType", UNSET)

        activity_default_price_per_unit = d.pop("ActivityDefaultPricePerUnit", UNSET)

        activity_default_review_required = d.pop("ActivityDefaultReviewRequired", UNSET)

        activity_id_based_on_selected_activity = d.pop("ActivityIdBasedOnSelectedActivity", UNSET)

        activity_id_increment = d.pop("ActivityIdIncrement", UNSET)

        activity_id_prefix = d.pop("ActivityIdPrefix", UNSET)

        activity_id_suffix = d.pop("ActivityIdSuffix", UNSET)

        activity_percent_complete_based_on_activity_steps = d.pop("ActivityPercentCompleteBasedOnActivitySteps", UNSET)

        add_actual_to_remaining = d.pop("AddActualToRemaining", UNSET)

        added_by = d.pop("AddedBy", UNSET)

        allow_status_review = d.pop("AllowStatusReview", UNSET)

        annual_discount_rate = d.pop("AnnualDiscountRate", UNSET)

        _anticipated_finish_date = d.pop("AnticipatedFinishDate", UNSET)
        anticipated_finish_date: datetime.datetime | Unset
        if isinstance(_anticipated_finish_date, Unset):
            anticipated_finish_date = UNSET
        else:
            anticipated_finish_date = isoparse(_anticipated_finish_date)

        _anticipated_start_date = d.pop("AnticipatedStartDate", UNSET)
        anticipated_start_date: datetime.datetime | Unset
        if isinstance(_anticipated_start_date, Unset):
            anticipated_start_date = UNSET
        else:
            anticipated_start_date = isoparse(_anticipated_start_date)

        assignment_default_driving_flag = d.pop("AssignmentDefaultDrivingFlag", UNSET)

        assignment_default_rate_type = d.pop("AssignmentDefaultRateType", UNSET)

        baseline_type_name = d.pop("BaselineTypeName", UNSET)

        baseline_type_object_id = d.pop("BaselineTypeObjectId", UNSET)

        _check_out_date = d.pop("CheckOutDate", UNSET)
        check_out_date: datetime.datetime | Unset
        if isinstance(_check_out_date, Unset):
            check_out_date = UNSET
        else:
            check_out_date = isoparse(_check_out_date)

        check_out_status = d.pop("CheckOutStatus", UNSET)

        check_out_user_object_id = d.pop("CheckOutUserObjectId", UNSET)

        contains_summary_data = d.pop("ContainsSummaryData", UNSET)

        cost_quantity_recalculate_flag = d.pop("CostQuantityRecalculateFlag", UNSET)

        _create_date = d.pop("CreateDate", UNSET)
        create_date: datetime.datetime | Unset
        if isinstance(_create_date, Unset):
            create_date = UNSET
        else:
            create_date = isoparse(_create_date)

        create_user = d.pop("CreateUser", UNSET)

        critical_activity_float_limit = d.pop("CriticalActivityFloatLimit", UNSET)

        critical_activity_path_type = d.pop("CriticalActivityPathType", UNSET)

        current_budget = d.pop("CurrentBudget", UNSET)

        current_variance = d.pop("CurrentVariance", UNSET)

        _data_date = d.pop("DataDate", UNSET)
        data_date: datetime.datetime | Unset
        if isinstance(_data_date, Unset):
            data_date = UNSET
        else:
            data_date = isoparse(_data_date)

        _date_added = d.pop("DateAdded", UNSET)
        date_added: datetime.datetime | Unset
        if isinstance(_date_added, Unset):
            date_added = UNSET
        else:
            date_added = isoparse(_date_added)

        default_price_time_units = d.pop("DefaultPriceTimeUnits", UNSET)

        description = d.pop("Description", UNSET)

        discount_application_period = d.pop("DiscountApplicationPeriod", UNSET)

        distributed_current_budget = d.pop("DistributedCurrentBudget", UNSET)

        enable_publication = d.pop("EnablePublication", UNSET)

        enable_summarization = d.pop("EnableSummarization", UNSET)

        financial_period_tmpl_id = d.pop("FinancialPeriodTmplId", UNSET)

        _finish_date = d.pop("FinishDate", UNSET)
        finish_date: datetime.datetime | Unset
        if isinstance(_finish_date, Unset):
            finish_date = UNSET
        else:
            finish_date = isoparse(_finish_date)

        fiscal_year_start_month = d.pop("FiscalYearStartMonth", UNSET)

        _forecast_finish_date = d.pop("ForecastFinishDate", UNSET)
        forecast_finish_date: datetime.datetime | Unset
        if isinstance(_forecast_finish_date, Unset):
            forecast_finish_date = UNSET
        else:
            forecast_finish_date = isoparse(_forecast_finish_date)

        _forecast_start_date = d.pop("ForecastStartDate", UNSET)
        forecast_start_date: datetime.datetime | Unset
        if isinstance(_forecast_start_date, Unset):
            forecast_start_date = UNSET
        else:
            forecast_start_date = isoparse(_forecast_start_date)

        guid = d.pop("GUID", UNSET)

        has_future_bucket_data = d.pop("HasFutureBucketData", UNSET)

        history_interval = d.pop("HistoryInterval", UNSET)

        history_level = d.pop("HistoryLevel", UNSET)

        independent_etc_labor_units = d.pop("IndependentETCLaborUnits", UNSET)

        independent_etc_total_cost = d.pop("IndependentETCTotalCost", UNSET)

        _last_baseline_update_date = d.pop("LastBaselineUpdateDate", UNSET)
        last_baseline_update_date: datetime.datetime | Unset
        if isinstance(_last_baseline_update_date, Unset):
            last_baseline_update_date = UNSET
        else:
            last_baseline_update_date = isoparse(_last_baseline_update_date)

        last_financial_period_object_id = d.pop("LastFinancialPeriodObjectId", UNSET)

        _last_level_date = d.pop("LastLevelDate", UNSET)
        last_level_date: datetime.datetime | Unset
        if isinstance(_last_level_date, Unset):
            last_level_date = UNSET
        else:
            last_level_date = isoparse(_last_level_date)

        _last_published_on = d.pop("LastPublishedOn", UNSET)
        last_published_on: datetime.datetime | Unset
        if isinstance(_last_published_on, Unset):
            last_published_on = UNSET
        else:
            last_published_on = isoparse(_last_published_on)

        _last_schedule_date = d.pop("LastScheduleDate", UNSET)
        last_schedule_date: datetime.datetime | Unset
        if isinstance(_last_schedule_date, Unset):
            last_schedule_date = UNSET
        else:
            last_schedule_date = isoparse(_last_schedule_date)

        _last_summarized_date = d.pop("LastSummarizedDate", UNSET)
        last_summarized_date: datetime.datetime | Unset
        if isinstance(_last_summarized_date, Unset):
            last_summarized_date = UNSET
        else:
            last_summarized_date = isoparse(_last_summarized_date)

        last_update_baseline_options = d.pop("LastUpdateBaselineOptions", UNSET)

        _last_update_date = d.pop("LastUpdateDate", UNSET)
        last_update_date: datetime.datetime | Unset
        if isinstance(_last_update_date, Unset):
            last_update_date = UNSET
        else:
            last_update_date = isoparse(_last_update_date)

        last_update_user = d.pop("LastUpdateUser", UNSET)

        leveling_priority = d.pop("LevelingPriority", UNSET)

        link_actual_to_actual_this_period = d.pop("LinkActualToActualThisPeriod", UNSET)

        link_percent_complete_with_actual = d.pop("LinkPercentCompleteWithActual", UNSET)

        link_planned_and_at_completion_flag = d.pop("LinkPlannedAndAtCompletionFlag", UNSET)

        location_name = d.pop("LocationName", UNSET)

        location_object_id = d.pop("LocationObjectId", UNSET)

        _must_finish_by_date = d.pop("MustFinishByDate", UNSET)
        must_finish_by_date: datetime.datetime | Unset
        if isinstance(_must_finish_by_date, Unset):
            must_finish_by_date = UNSET
        else:
            must_finish_by_date = isoparse(_must_finish_by_date)

        obs_name = d.pop("OBSName", UNSET)

        obs_object_id = d.pop("OBSObjectId", UNSET)

        object_id = d.pop("ObjectId", UNSET)

        original_budget = d.pop("OriginalBudget", UNSET)

        original_project_object_id = d.pop("OriginalProjectObjectId", UNSET)

        owner_resource_object_id = d.pop("OwnerResourceObjectId", UNSET)

        parent_eps_id = d.pop("ParentEPSId", UNSET)

        parent_eps_name = d.pop("ParentEPSName", UNSET)

        _planned_start_date = d.pop("PlannedStartDate", UNSET)
        planned_start_date: datetime.datetime | Unset
        if isinstance(_planned_start_date, Unset):
            planned_start_date = UNSET
        else:
            planned_start_date = isoparse(_planned_start_date)

        primary_resources_can_mark_activities_as_completed = d.pop(
            "PrimaryResourcesCanMarkActivitiesAsCompleted", UNSET
        )

        _project_forecast_start_date = d.pop("ProjectForecastStartDate", UNSET)
        project_forecast_start_date: datetime.datetime | Unset
        if isinstance(_project_forecast_start_date, Unset):
            project_forecast_start_date = UNSET
        else:
            project_forecast_start_date = isoparse(_project_forecast_start_date)

        project_schedule_type = d.pop("ProjectScheduleType", UNSET)

        proposed_budget = d.pop("ProposedBudget", UNSET)

        publication_priority = d.pop("PublicationPriority", UNSET)

        reset_planned_to_remaining_flag = d.pop("ResetPlannedToRemainingFlag", UNSET)

        resource_can_be_assigned_to_same_activity_more_than_once = d.pop(
            "ResourceCanBeAssignedToSameActivityMoreThanOnce", UNSET
        )

        resource_name = d.pop("ResourceName", UNSET)

        resources_can_assign_themselves_to_activities = d.pop("ResourcesCanAssignThemselvesToActivities", UNSET)

        resources_can_assign_themselves_to_activities_outside_obs_access = d.pop(
            "ResourcesCanAssignThemselvesToActivitiesOutsideOBSAccess", UNSET
        )

        resources_can_edit_assignment_percent_complete = d.pop("ResourcesCanEditAssignmentPercentComplete", UNSET)

        risk_exposure = d.pop("RiskExposure", UNSET)

        risk_level = d.pop("RiskLevel", UNSET)

        risk_matrix_object_id = d.pop("RiskMatrixObjectId", UNSET)

        risk_score = d.pop("RiskScore", UNSET)

        _scheduled_finish_date = d.pop("ScheduledFinishDate", UNSET)
        scheduled_finish_date: datetime.datetime | Unset
        if isinstance(_scheduled_finish_date, Unset):
            scheduled_finish_date = UNSET
        else:
            scheduled_finish_date = isoparse(_scheduled_finish_date)

        _start_date = d.pop("StartDate", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        status = d.pop("Status", UNSET)

        status_reviewer_name = d.pop("StatusReviewerName", UNSET)

        status_reviewer_object_id = d.pop("StatusReviewerObjectId", UNSET)

        strategic_priority = d.pop("StrategicPriority", UNSET)

        summarize_to_wbs_level = d.pop("SummarizeToWBSLevel", UNSET)

        _summarized_data_date = d.pop("SummarizedDataDate", UNSET)
        summarized_data_date: datetime.datetime | Unset
        if isinstance(_summarized_data_date, Unset):
            summarized_data_date = UNSET
        else:
            summarized_data_date = isoparse(_summarized_data_date)

        summary_accounting_variance_by_cost = d.pop("SummaryAccountingVarianceByCost", UNSET)

        summary_accounting_variance_by_labor_units = d.pop("SummaryAccountingVarianceByLaborUnits", UNSET)

        summary_activity_count = d.pop("SummaryActivityCount", UNSET)

        summary_actual_duration = d.pop("SummaryActualDuration", UNSET)

        summary_actual_expense_cost = d.pop("SummaryActualExpenseCost", UNSET)

        _summary_actual_finish_date = d.pop("SummaryActualFinishDate", UNSET)
        summary_actual_finish_date: datetime.datetime | Unset
        if isinstance(_summary_actual_finish_date, Unset):
            summary_actual_finish_date = UNSET
        else:
            summary_actual_finish_date = isoparse(_summary_actual_finish_date)

        summary_actual_labor_cost = d.pop("SummaryActualLaborCost", UNSET)

        summary_actual_labor_units = d.pop("SummaryActualLaborUnits", UNSET)

        summary_actual_material_cost = d.pop("SummaryActualMaterialCost", UNSET)

        summary_actual_non_labor_cost = d.pop("SummaryActualNonLaborCost", UNSET)

        summary_actual_non_labor_units = d.pop("SummaryActualNonLaborUnits", UNSET)

        _summary_actual_start_date = d.pop("SummaryActualStartDate", UNSET)
        summary_actual_start_date: datetime.datetime | Unset
        if isinstance(_summary_actual_start_date, Unset):
            summary_actual_start_date = UNSET
        else:
            summary_actual_start_date = isoparse(_summary_actual_start_date)

        summary_actual_this_period_cost = d.pop("SummaryActualThisPeriodCost", UNSET)

        summary_actual_this_period_labor_cost = d.pop("SummaryActualThisPeriodLaborCost", UNSET)

        summary_actual_this_period_labor_units = d.pop("SummaryActualThisPeriodLaborUnits", UNSET)

        summary_actual_this_period_material_cost = d.pop("SummaryActualThisPeriodMaterialCost", UNSET)

        summary_actual_this_period_non_labor_cost = d.pop("SummaryActualThisPeriodNonLaborCost", UNSET)

        summary_actual_this_period_non_labor_units = d.pop("SummaryActualThisPeriodNonLaborUnits", UNSET)

        summary_actual_total_cost = d.pop("SummaryActualTotalCost", UNSET)

        summary_actual_value_by_cost = d.pop("SummaryActualValueByCost", UNSET)

        summary_actual_value_by_labor_units = d.pop("SummaryActualValueByLaborUnits", UNSET)

        summary_at_completion_duration = d.pop("SummaryAtCompletionDuration", UNSET)

        summary_at_completion_expense_cost = d.pop("SummaryAtCompletionExpenseCost", UNSET)

        summary_at_completion_labor_cost = d.pop("SummaryAtCompletionLaborCost", UNSET)

        summary_at_completion_labor_units = d.pop("SummaryAtCompletionLaborUnits", UNSET)

        summary_at_completion_material_cost = d.pop("SummaryAtCompletionMaterialCost", UNSET)

        summary_at_completion_non_labor_cost = d.pop("SummaryAtCompletionNonLaborCost", UNSET)

        summary_at_completion_non_labor_units = d.pop("SummaryAtCompletionNonLaborUnits", UNSET)

        summary_at_completion_total_cost = d.pop("SummaryAtCompletionTotalCost", UNSET)

        summary_at_completion_total_cost_variance = d.pop("SummaryAtCompletionTotalCostVariance", UNSET)

        summary_baseline_completed_activity_count = d.pop("SummaryBaselineCompletedActivityCount", UNSET)

        summary_baseline_duration = d.pop("SummaryBaselineDuration", UNSET)

        summary_baseline_expense_cost = d.pop("SummaryBaselineExpenseCost", UNSET)

        _summary_baseline_finish_date = d.pop("SummaryBaselineFinishDate", UNSET)
        summary_baseline_finish_date: datetime.datetime | Unset
        if isinstance(_summary_baseline_finish_date, Unset):
            summary_baseline_finish_date = UNSET
        else:
            summary_baseline_finish_date = isoparse(_summary_baseline_finish_date)

        summary_baseline_in_progress_activity_count = d.pop("SummaryBaselineInProgressActivityCount", UNSET)

        summary_baseline_labor_cost = d.pop("SummaryBaselineLaborCost", UNSET)

        summary_baseline_labor_units = d.pop("SummaryBaselineLaborUnits", UNSET)

        summary_baseline_material_cost = d.pop("SummaryBaselineMaterialCost", UNSET)

        summary_baseline_non_labor_cost = d.pop("SummaryBaselineNonLaborCost", UNSET)

        summary_baseline_non_labor_units = d.pop("SummaryBaselineNonLaborUnits", UNSET)

        summary_baseline_not_started_activity_count = d.pop("SummaryBaselineNotStartedActivityCount", UNSET)

        _summary_baseline_start_date = d.pop("SummaryBaselineStartDate", UNSET)
        summary_baseline_start_date: datetime.datetime | Unset
        if isinstance(_summary_baseline_start_date, Unset):
            summary_baseline_start_date = UNSET
        else:
            summary_baseline_start_date = isoparse(_summary_baseline_start_date)

        summary_baseline_total_cost = d.pop("SummaryBaselineTotalCost", UNSET)

        summary_budget_at_completion_by_cost = d.pop("SummaryBudgetAtCompletionByCost", UNSET)

        summary_budget_at_completion_by_labor_units = d.pop("SummaryBudgetAtCompletionByLaborUnits", UNSET)

        summary_completed_activity_count = d.pop("SummaryCompletedActivityCount", UNSET)

        summary_cost_percent_complete = d.pop("SummaryCostPercentComplete", UNSET)

        summary_cost_percent_of_planned = d.pop("SummaryCostPercentOfPlanned", UNSET)

        summary_cost_performance_index_by_cost = d.pop("SummaryCostPerformanceIndexByCost", UNSET)

        summary_cost_performance_index_by_labor_units = d.pop("SummaryCostPerformanceIndexByLaborUnits", UNSET)

        summary_cost_variance_by_cost = d.pop("SummaryCostVarianceByCost", UNSET)

        summary_cost_variance_by_labor_units = d.pop("SummaryCostVarianceByLaborUnits", UNSET)

        summary_cost_variance_index = d.pop("SummaryCostVarianceIndex", UNSET)

        summary_cost_variance_index_by_cost = d.pop("SummaryCostVarianceIndexByCost", UNSET)

        summary_cost_variance_index_by_labor_units = d.pop("SummaryCostVarianceIndexByLaborUnits", UNSET)

        summary_duration_percent_complete = d.pop("SummaryDurationPercentComplete", UNSET)

        summary_duration_percent_of_planned = d.pop("SummaryDurationPercentOfPlanned", UNSET)

        summary_duration_variance = d.pop("SummaryDurationVariance", UNSET)

        summary_earned_value_by_cost = d.pop("SummaryEarnedValueByCost", UNSET)

        summary_earned_value_by_labor_units = d.pop("SummaryEarnedValueByLaborUnits", UNSET)

        summary_estimate_at_completion_by_cost = d.pop("SummaryEstimateAtCompletionByCost", UNSET)

        summary_estimate_at_completion_by_labor_units = d.pop("SummaryEstimateAtCompletionByLaborUnits", UNSET)

        summary_estimate_at_completion_high_percent_by_labor_units = d.pop(
            "SummaryEstimateAtCompletionHighPercentByLaborUnits", UNSET
        )

        summary_estimate_at_completion_low_percent_by_labor_units = d.pop(
            "SummaryEstimateAtCompletionLowPercentByLaborUnits", UNSET
        )

        summary_estimate_to_complete_by_cost = d.pop("SummaryEstimateToCompleteByCost", UNSET)

        summary_estimate_to_complete_by_labor_units = d.pop("SummaryEstimateToCompleteByLaborUnits", UNSET)

        summary_expense_cost_percent_complete = d.pop("SummaryExpenseCostPercentComplete", UNSET)

        summary_expense_cost_variance = d.pop("SummaryExpenseCostVariance", UNSET)

        summary_finish_date_variance = d.pop("SummaryFinishDateVariance", UNSET)

        summary_in_progress_activity_count = d.pop("SummaryInProgressActivityCount", UNSET)

        summary_labor_cost_percent_complete = d.pop("SummaryLaborCostPercentComplete", UNSET)

        summary_labor_cost_variance = d.pop("SummaryLaborCostVariance", UNSET)

        summary_labor_units_percent_complete = d.pop("SummaryLaborUnitsPercentComplete", UNSET)

        summary_labor_units_variance = d.pop("SummaryLaborUnitsVariance", UNSET)

        summary_material_cost_percent_complete = d.pop("SummaryMaterialCostPercentComplete", UNSET)

        summary_material_cost_variance = d.pop("SummaryMaterialCostVariance", UNSET)

        summary_non_labor_cost_percent_complete = d.pop("SummaryNonLaborCostPercentComplete", UNSET)

        summary_non_labor_cost_variance = d.pop("SummaryNonLaborCostVariance", UNSET)

        summary_non_labor_units_percent_complete = d.pop("SummaryNonLaborUnitsPercentComplete", UNSET)

        summary_non_labor_units_variance = d.pop("SummaryNonLaborUnitsVariance", UNSET)

        summary_not_started_activity_count = d.pop("SummaryNotStartedActivityCount", UNSET)

        summary_performance_percent_complete_by_labor_units = d.pop(
            "SummaryPerformancePercentCompleteByLaborUnits", UNSET
        )

        summary_planned_cost = d.pop("SummaryPlannedCost", UNSET)

        summary_planned_duration = d.pop("SummaryPlannedDuration", UNSET)

        summary_planned_expense_cost = d.pop("SummaryPlannedExpenseCost", UNSET)

        _summary_planned_finish_date = d.pop("SummaryPlannedFinishDate", UNSET)
        summary_planned_finish_date: datetime.datetime | Unset
        if isinstance(_summary_planned_finish_date, Unset):
            summary_planned_finish_date = UNSET
        else:
            summary_planned_finish_date = isoparse(_summary_planned_finish_date)

        summary_planned_labor_cost = d.pop("SummaryPlannedLaborCost", UNSET)

        summary_planned_labor_units = d.pop("SummaryPlannedLaborUnits", UNSET)

        summary_planned_material_cost = d.pop("SummaryPlannedMaterialCost", UNSET)

        summary_planned_non_labor_cost = d.pop("SummaryPlannedNonLaborCost", UNSET)

        summary_planned_non_labor_units = d.pop("SummaryPlannedNonLaborUnits", UNSET)

        _summary_planned_start_date = d.pop("SummaryPlannedStartDate", UNSET)
        summary_planned_start_date: datetime.datetime | Unset
        if isinstance(_summary_planned_start_date, Unset):
            summary_planned_start_date = UNSET
        else:
            summary_planned_start_date = isoparse(_summary_planned_start_date)

        summary_planned_value_by_cost = d.pop("SummaryPlannedValueByCost", UNSET)

        summary_planned_value_by_labor_units = d.pop("SummaryPlannedValueByLaborUnits", UNSET)

        _summary_progress_finish_date = d.pop("SummaryProgressFinishDate", UNSET)
        summary_progress_finish_date: datetime.datetime | Unset
        if isinstance(_summary_progress_finish_date, Unset):
            summary_progress_finish_date = UNSET
        else:
            summary_progress_finish_date = isoparse(_summary_progress_finish_date)

        summary_remaining_duration = d.pop("SummaryRemainingDuration", UNSET)

        summary_remaining_expense_cost = d.pop("SummaryRemainingExpenseCost", UNSET)

        _summary_remaining_finish_date = d.pop("SummaryRemainingFinishDate", UNSET)
        summary_remaining_finish_date: datetime.datetime | Unset
        if isinstance(_summary_remaining_finish_date, Unset):
            summary_remaining_finish_date = UNSET
        else:
            summary_remaining_finish_date = isoparse(_summary_remaining_finish_date)

        summary_remaining_labor_cost = d.pop("SummaryRemainingLaborCost", UNSET)

        summary_remaining_labor_units = d.pop("SummaryRemainingLaborUnits", UNSET)

        summary_remaining_material_cost = d.pop("SummaryRemainingMaterialCost", UNSET)

        summary_remaining_non_labor_cost = d.pop("SummaryRemainingNonLaborCost", UNSET)

        summary_remaining_non_labor_units = d.pop("SummaryRemainingNonLaborUnits", UNSET)

        _summary_remaining_start_date = d.pop("SummaryRemainingStartDate", UNSET)
        summary_remaining_start_date: datetime.datetime | Unset
        if isinstance(_summary_remaining_start_date, Unset):
            summary_remaining_start_date = UNSET
        else:
            summary_remaining_start_date = isoparse(_summary_remaining_start_date)

        summary_remaining_total_cost = d.pop("SummaryRemainingTotalCost", UNSET)

        summary_schedule_percent_complete = d.pop("SummarySchedulePercentComplete", UNSET)

        summary_schedule_percent_complete_by_labor_units = d.pop("SummarySchedulePercentCompleteByLaborUnits", UNSET)

        summary_schedule_performance_index_by_cost = d.pop("SummarySchedulePerformanceIndexByCost", UNSET)

        summary_schedule_performance_index_by_labor_units = d.pop("SummarySchedulePerformanceIndexByLaborUnits", UNSET)

        summary_schedule_variance_by_cost = d.pop("SummaryScheduleVarianceByCost", UNSET)

        summary_schedule_variance_by_labor_units = d.pop("SummaryScheduleVarianceByLaborUnits", UNSET)

        summary_schedule_variance_index = d.pop("SummaryScheduleVarianceIndex", UNSET)

        summary_schedule_variance_index_by_cost = d.pop("SummaryScheduleVarianceIndexByCost", UNSET)

        summary_schedule_variance_index_by_labor_units = d.pop("SummaryScheduleVarianceIndexByLaborUnits", UNSET)

        summary_start_date_variance = d.pop("SummaryStartDateVariance", UNSET)

        summary_to_complete_performance_index_by_cost = d.pop("SummaryToCompletePerformanceIndexByCost", UNSET)

        summary_total_cost_variance = d.pop("SummaryTotalCostVariance", UNSET)

        summary_total_float = d.pop("SummaryTotalFloat", UNSET)

        summary_units_percent_complete = d.pop("SummaryUnitsPercentComplete", UNSET)

        summary_variance_at_completion_by_labor_units = d.pop("SummaryVarianceAtCompletionByLaborUnits", UNSET)

        team_member_activity_fields = d.pop("TeamMemberActivityFields", UNSET)

        team_member_assignment_option = d.pop("TeamMemberAssignmentOption", UNSET)

        team_member_resource_assignment_fields = d.pop("TeamMemberResourceAssignmentFields", UNSET)

        team_member_step_udf_viewable_fields = d.pop("TeamMemberStepUDFViewableFields", UNSET)

        team_member_viewable_fields = d.pop("TeamMemberViewableFields", UNSET)

        total_benefit_plan = d.pop("TotalBenefitPlan", UNSET)

        total_benefit_plan_tally = d.pop("TotalBenefitPlanTally", UNSET)

        total_spending_plan = d.pop("TotalSpendingPlan", UNSET)

        total_spending_plan_tally = d.pop("TotalSpendingPlanTally", UNSET)

        unallocated_budget = d.pop("UnallocatedBudget", UNSET)

        undistributed_current_variance = d.pop("UndistributedCurrentVariance", UNSET)

        wbs_code_separator = d.pop("WBSCodeSeparator", UNSET)

        wbs_object_id = d.pop("WBSObjectId", UNSET)

        web_site_root_directory = d.pop("WebSiteRootDirectory", UNSET)

        web_site_url = d.pop("WebSiteURL", UNSET)

        baseline_project = cls(
            id=id,
            name=name,
            parent_eps_object_id=parent_eps_object_id,
            activity_default_activity_type=activity_default_activity_type,
            activity_default_calendar_object_id=activity_default_calendar_object_id,
            activity_default_cost_account_object_id=activity_default_cost_account_object_id,
            activity_default_duration_type=activity_default_duration_type,
            activity_default_percent_complete_type=activity_default_percent_complete_type,
            activity_default_price_per_unit=activity_default_price_per_unit,
            activity_default_review_required=activity_default_review_required,
            activity_id_based_on_selected_activity=activity_id_based_on_selected_activity,
            activity_id_increment=activity_id_increment,
            activity_id_prefix=activity_id_prefix,
            activity_id_suffix=activity_id_suffix,
            activity_percent_complete_based_on_activity_steps=activity_percent_complete_based_on_activity_steps,
            add_actual_to_remaining=add_actual_to_remaining,
            added_by=added_by,
            allow_status_review=allow_status_review,
            annual_discount_rate=annual_discount_rate,
            anticipated_finish_date=anticipated_finish_date,
            anticipated_start_date=anticipated_start_date,
            assignment_default_driving_flag=assignment_default_driving_flag,
            assignment_default_rate_type=assignment_default_rate_type,
            baseline_type_name=baseline_type_name,
            baseline_type_object_id=baseline_type_object_id,
            check_out_date=check_out_date,
            check_out_status=check_out_status,
            check_out_user_object_id=check_out_user_object_id,
            contains_summary_data=contains_summary_data,
            cost_quantity_recalculate_flag=cost_quantity_recalculate_flag,
            create_date=create_date,
            create_user=create_user,
            critical_activity_float_limit=critical_activity_float_limit,
            critical_activity_path_type=critical_activity_path_type,
            current_budget=current_budget,
            current_variance=current_variance,
            data_date=data_date,
            date_added=date_added,
            default_price_time_units=default_price_time_units,
            description=description,
            discount_application_period=discount_application_period,
            distributed_current_budget=distributed_current_budget,
            enable_publication=enable_publication,
            enable_summarization=enable_summarization,
            financial_period_tmpl_id=financial_period_tmpl_id,
            finish_date=finish_date,
            fiscal_year_start_month=fiscal_year_start_month,
            forecast_finish_date=forecast_finish_date,
            forecast_start_date=forecast_start_date,
            guid=guid,
            has_future_bucket_data=has_future_bucket_data,
            history_interval=history_interval,
            history_level=history_level,
            independent_etc_labor_units=independent_etc_labor_units,
            independent_etc_total_cost=independent_etc_total_cost,
            last_baseline_update_date=last_baseline_update_date,
            last_financial_period_object_id=last_financial_period_object_id,
            last_level_date=last_level_date,
            last_published_on=last_published_on,
            last_schedule_date=last_schedule_date,
            last_summarized_date=last_summarized_date,
            last_update_baseline_options=last_update_baseline_options,
            last_update_date=last_update_date,
            last_update_user=last_update_user,
            leveling_priority=leveling_priority,
            link_actual_to_actual_this_period=link_actual_to_actual_this_period,
            link_percent_complete_with_actual=link_percent_complete_with_actual,
            link_planned_and_at_completion_flag=link_planned_and_at_completion_flag,
            location_name=location_name,
            location_object_id=location_object_id,
            must_finish_by_date=must_finish_by_date,
            obs_name=obs_name,
            obs_object_id=obs_object_id,
            object_id=object_id,
            original_budget=original_budget,
            original_project_object_id=original_project_object_id,
            owner_resource_object_id=owner_resource_object_id,
            parent_eps_id=parent_eps_id,
            parent_eps_name=parent_eps_name,
            planned_start_date=planned_start_date,
            primary_resources_can_mark_activities_as_completed=primary_resources_can_mark_activities_as_completed,
            project_forecast_start_date=project_forecast_start_date,
            project_schedule_type=project_schedule_type,
            proposed_budget=proposed_budget,
            publication_priority=publication_priority,
            reset_planned_to_remaining_flag=reset_planned_to_remaining_flag,
            resource_can_be_assigned_to_same_activity_more_than_once=resource_can_be_assigned_to_same_activity_more_than_once,
            resource_name=resource_name,
            resources_can_assign_themselves_to_activities=resources_can_assign_themselves_to_activities,
            resources_can_assign_themselves_to_activities_outside_obs_access=resources_can_assign_themselves_to_activities_outside_obs_access,
            resources_can_edit_assignment_percent_complete=resources_can_edit_assignment_percent_complete,
            risk_exposure=risk_exposure,
            risk_level=risk_level,
            risk_matrix_object_id=risk_matrix_object_id,
            risk_score=risk_score,
            scheduled_finish_date=scheduled_finish_date,
            start_date=start_date,
            status=status,
            status_reviewer_name=status_reviewer_name,
            status_reviewer_object_id=status_reviewer_object_id,
            strategic_priority=strategic_priority,
            summarize_to_wbs_level=summarize_to_wbs_level,
            summarized_data_date=summarized_data_date,
            summary_accounting_variance_by_cost=summary_accounting_variance_by_cost,
            summary_accounting_variance_by_labor_units=summary_accounting_variance_by_labor_units,
            summary_activity_count=summary_activity_count,
            summary_actual_duration=summary_actual_duration,
            summary_actual_expense_cost=summary_actual_expense_cost,
            summary_actual_finish_date=summary_actual_finish_date,
            summary_actual_labor_cost=summary_actual_labor_cost,
            summary_actual_labor_units=summary_actual_labor_units,
            summary_actual_material_cost=summary_actual_material_cost,
            summary_actual_non_labor_cost=summary_actual_non_labor_cost,
            summary_actual_non_labor_units=summary_actual_non_labor_units,
            summary_actual_start_date=summary_actual_start_date,
            summary_actual_this_period_cost=summary_actual_this_period_cost,
            summary_actual_this_period_labor_cost=summary_actual_this_period_labor_cost,
            summary_actual_this_period_labor_units=summary_actual_this_period_labor_units,
            summary_actual_this_period_material_cost=summary_actual_this_period_material_cost,
            summary_actual_this_period_non_labor_cost=summary_actual_this_period_non_labor_cost,
            summary_actual_this_period_non_labor_units=summary_actual_this_period_non_labor_units,
            summary_actual_total_cost=summary_actual_total_cost,
            summary_actual_value_by_cost=summary_actual_value_by_cost,
            summary_actual_value_by_labor_units=summary_actual_value_by_labor_units,
            summary_at_completion_duration=summary_at_completion_duration,
            summary_at_completion_expense_cost=summary_at_completion_expense_cost,
            summary_at_completion_labor_cost=summary_at_completion_labor_cost,
            summary_at_completion_labor_units=summary_at_completion_labor_units,
            summary_at_completion_material_cost=summary_at_completion_material_cost,
            summary_at_completion_non_labor_cost=summary_at_completion_non_labor_cost,
            summary_at_completion_non_labor_units=summary_at_completion_non_labor_units,
            summary_at_completion_total_cost=summary_at_completion_total_cost,
            summary_at_completion_total_cost_variance=summary_at_completion_total_cost_variance,
            summary_baseline_completed_activity_count=summary_baseline_completed_activity_count,
            summary_baseline_duration=summary_baseline_duration,
            summary_baseline_expense_cost=summary_baseline_expense_cost,
            summary_baseline_finish_date=summary_baseline_finish_date,
            summary_baseline_in_progress_activity_count=summary_baseline_in_progress_activity_count,
            summary_baseline_labor_cost=summary_baseline_labor_cost,
            summary_baseline_labor_units=summary_baseline_labor_units,
            summary_baseline_material_cost=summary_baseline_material_cost,
            summary_baseline_non_labor_cost=summary_baseline_non_labor_cost,
            summary_baseline_non_labor_units=summary_baseline_non_labor_units,
            summary_baseline_not_started_activity_count=summary_baseline_not_started_activity_count,
            summary_baseline_start_date=summary_baseline_start_date,
            summary_baseline_total_cost=summary_baseline_total_cost,
            summary_budget_at_completion_by_cost=summary_budget_at_completion_by_cost,
            summary_budget_at_completion_by_labor_units=summary_budget_at_completion_by_labor_units,
            summary_completed_activity_count=summary_completed_activity_count,
            summary_cost_percent_complete=summary_cost_percent_complete,
            summary_cost_percent_of_planned=summary_cost_percent_of_planned,
            summary_cost_performance_index_by_cost=summary_cost_performance_index_by_cost,
            summary_cost_performance_index_by_labor_units=summary_cost_performance_index_by_labor_units,
            summary_cost_variance_by_cost=summary_cost_variance_by_cost,
            summary_cost_variance_by_labor_units=summary_cost_variance_by_labor_units,
            summary_cost_variance_index=summary_cost_variance_index,
            summary_cost_variance_index_by_cost=summary_cost_variance_index_by_cost,
            summary_cost_variance_index_by_labor_units=summary_cost_variance_index_by_labor_units,
            summary_duration_percent_complete=summary_duration_percent_complete,
            summary_duration_percent_of_planned=summary_duration_percent_of_planned,
            summary_duration_variance=summary_duration_variance,
            summary_earned_value_by_cost=summary_earned_value_by_cost,
            summary_earned_value_by_labor_units=summary_earned_value_by_labor_units,
            summary_estimate_at_completion_by_cost=summary_estimate_at_completion_by_cost,
            summary_estimate_at_completion_by_labor_units=summary_estimate_at_completion_by_labor_units,
            summary_estimate_at_completion_high_percent_by_labor_units=summary_estimate_at_completion_high_percent_by_labor_units,
            summary_estimate_at_completion_low_percent_by_labor_units=summary_estimate_at_completion_low_percent_by_labor_units,
            summary_estimate_to_complete_by_cost=summary_estimate_to_complete_by_cost,
            summary_estimate_to_complete_by_labor_units=summary_estimate_to_complete_by_labor_units,
            summary_expense_cost_percent_complete=summary_expense_cost_percent_complete,
            summary_expense_cost_variance=summary_expense_cost_variance,
            summary_finish_date_variance=summary_finish_date_variance,
            summary_in_progress_activity_count=summary_in_progress_activity_count,
            summary_labor_cost_percent_complete=summary_labor_cost_percent_complete,
            summary_labor_cost_variance=summary_labor_cost_variance,
            summary_labor_units_percent_complete=summary_labor_units_percent_complete,
            summary_labor_units_variance=summary_labor_units_variance,
            summary_material_cost_percent_complete=summary_material_cost_percent_complete,
            summary_material_cost_variance=summary_material_cost_variance,
            summary_non_labor_cost_percent_complete=summary_non_labor_cost_percent_complete,
            summary_non_labor_cost_variance=summary_non_labor_cost_variance,
            summary_non_labor_units_percent_complete=summary_non_labor_units_percent_complete,
            summary_non_labor_units_variance=summary_non_labor_units_variance,
            summary_not_started_activity_count=summary_not_started_activity_count,
            summary_performance_percent_complete_by_labor_units=summary_performance_percent_complete_by_labor_units,
            summary_planned_cost=summary_planned_cost,
            summary_planned_duration=summary_planned_duration,
            summary_planned_expense_cost=summary_planned_expense_cost,
            summary_planned_finish_date=summary_planned_finish_date,
            summary_planned_labor_cost=summary_planned_labor_cost,
            summary_planned_labor_units=summary_planned_labor_units,
            summary_planned_material_cost=summary_planned_material_cost,
            summary_planned_non_labor_cost=summary_planned_non_labor_cost,
            summary_planned_non_labor_units=summary_planned_non_labor_units,
            summary_planned_start_date=summary_planned_start_date,
            summary_planned_value_by_cost=summary_planned_value_by_cost,
            summary_planned_value_by_labor_units=summary_planned_value_by_labor_units,
            summary_progress_finish_date=summary_progress_finish_date,
            summary_remaining_duration=summary_remaining_duration,
            summary_remaining_expense_cost=summary_remaining_expense_cost,
            summary_remaining_finish_date=summary_remaining_finish_date,
            summary_remaining_labor_cost=summary_remaining_labor_cost,
            summary_remaining_labor_units=summary_remaining_labor_units,
            summary_remaining_material_cost=summary_remaining_material_cost,
            summary_remaining_non_labor_cost=summary_remaining_non_labor_cost,
            summary_remaining_non_labor_units=summary_remaining_non_labor_units,
            summary_remaining_start_date=summary_remaining_start_date,
            summary_remaining_total_cost=summary_remaining_total_cost,
            summary_schedule_percent_complete=summary_schedule_percent_complete,
            summary_schedule_percent_complete_by_labor_units=summary_schedule_percent_complete_by_labor_units,
            summary_schedule_performance_index_by_cost=summary_schedule_performance_index_by_cost,
            summary_schedule_performance_index_by_labor_units=summary_schedule_performance_index_by_labor_units,
            summary_schedule_variance_by_cost=summary_schedule_variance_by_cost,
            summary_schedule_variance_by_labor_units=summary_schedule_variance_by_labor_units,
            summary_schedule_variance_index=summary_schedule_variance_index,
            summary_schedule_variance_index_by_cost=summary_schedule_variance_index_by_cost,
            summary_schedule_variance_index_by_labor_units=summary_schedule_variance_index_by_labor_units,
            summary_start_date_variance=summary_start_date_variance,
            summary_to_complete_performance_index_by_cost=summary_to_complete_performance_index_by_cost,
            summary_total_cost_variance=summary_total_cost_variance,
            summary_total_float=summary_total_float,
            summary_units_percent_complete=summary_units_percent_complete,
            summary_variance_at_completion_by_labor_units=summary_variance_at_completion_by_labor_units,
            team_member_activity_fields=team_member_activity_fields,
            team_member_assignment_option=team_member_assignment_option,
            team_member_resource_assignment_fields=team_member_resource_assignment_fields,
            team_member_step_udf_viewable_fields=team_member_step_udf_viewable_fields,
            team_member_viewable_fields=team_member_viewable_fields,
            total_benefit_plan=total_benefit_plan,
            total_benefit_plan_tally=total_benefit_plan_tally,
            total_spending_plan=total_spending_plan,
            total_spending_plan_tally=total_spending_plan_tally,
            unallocated_budget=unallocated_budget,
            undistributed_current_variance=undistributed_current_variance,
            wbs_code_separator=wbs_code_separator,
            wbs_object_id=wbs_object_id,
            web_site_root_directory=web_site_root_directory,
            web_site_url=web_site_url,
        )

        baseline_project.additional_properties = d
        return baseline_project

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
