from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Project")


@_attrs_define
class Project:
    """Project Entity

    Attributes:
        id (str): The short code assigned to each Project element for identification. Each Project element is uniquely
            identified by this short code.
        name (str): The name of the Project element.
        parent_eps_object_id (int): The unique ID of the parent EPS of this project.
        activity_default_activity_type (str | Unset): The default type for activities. Possible values are 'Task
            Dependent', 'Resource Dependent', 'Level of Effort', or 'Milestone'. A 'Task Dependent' activity is scheduled
            using the activity's calendar rather than the calendars of the assigned resources. A 'Resource Dependent'
            activity is scheduled using the calendars of the assigned resources. This type is used when several resources
            are assigned to the activity, but they may work separately. A 'Milestone' is a zero-duration activity without
            resources, marking a significant project event. A 'Level of Effort' activity has a duration that is determined
            by its dependent activities. Administration-type activities are typically 'Level of Effort'.
        activity_default_calendar_name (str | Unset): The name of the calendar assigned to new activities by default.
            Can be null for baselines.
        activity_default_calendar_object_id (int | Unset): The unique ID of the calendar assigned to new activities by
            default. Can be null for baselines.
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
            numbering based on the prefix, suffix. Default = 'false'
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
            subtract actual from at complete when actual units and costs are updated. Default = 'true'
        added_by (str | Unset): The name of the user who added the project to the database.
        allow_negative_actual_units_flag (bool | Unset): The flag that indicates whether the project can allow the
            negative values for the actual units.
        allow_status_review (bool | Unset): The indicator that determines whether status updates to activities in a
            project are eligible for manual approval before committing changes.
        annual_discount_rate (float | Unset): The user-defined number field that identifies the discount rate for the
            project.
        anticipated_finish_date (datetime.datetime | Unset): The anticipated finish date of Project element. User-
            entered - not dependent upon any other fields. If there are no children, the anticipated finish date will be the
            finish date displayed in the columns.
        anticipated_start_date (datetime.datetime | Unset): The anticipated start date of Project element. User-entered
            - not dependent upon any other fields. If there are no children, the anticipated start date will be the start
            date displayed in the columns.
        assignment_default_driving_flag (bool | Unset): The default flag assigned to new assignments, to indicate
            whether assignments will drive activity dates.
        assignment_default_rate_type (str | Unset): The default rate type when adding resource assignments to a project.
            Valid values are 'Price / Unit', 'Price / Unit2', 'Price / Unit3', 'Price / Unit4', and 'Price / Unit5'.
        calculate_float_based_on_finish_date (bool | Unset): The flag that indicates how each activity's float will be
            calculated with respect to other projects in the scheduling batch. This setting only has an effect when
            scheduling multiple projects at the same time. If true, each activity's float is calculated based on its
            project's ScheduledFinishDate. If false, then each activity's float is calculated based on the latest
            ScheduledFinishDate of all of the projects in the scheduling batch.
        check_out_date (datetime.datetime | Unset): The date on which the project was checked out of the Project
            Management database.
        check_out_status (bool | Unset): The flag that indicates that the project is currently checked out to an
            external file or database and is being managed remotely.
        check_out_user_object_id (int | Unset): The unique ID of the User that checked out this project.
        compute_total_float_type (str | Unset): The method for calculating total float for all activities. Start Float
            is the difference between the early and late start dates (Start Float = Late Start - Early Start); Finish Float
            is the difference between the early and late finish dates (Finish Float = Late Finish - Early Finish); and
            Smallest of Start Float and Finish Float is the most critical float value.
        contains_summary_data (bool | Unset): The flag that indicates that the Project has been summarized.
        contract_management_group_name (str | Unset): The name of the Contract Management Group.
        contract_management_project_name (str | Unset): The name of the Contract Management Project.
        cost_quantity_recalculate_flag (bool | Unset): The flag that, when costs and quantities are linked, indicates
            whether the quantities should be updated when costs are updated,
        create_date (datetime.datetime | Unset): The date this project was created.
        create_user (str | Unset): The name of the user that created this project.
        critical_activity_float_limit (float | Unset): The duration used to determine if an activity is critical. When
            an activity has total float that is less than or equal to this duration, the activity is marked as critical.
        critical_activity_float_threshold (float | Unset): The maximum float time for activities before they are marked
            critical.
        critical_activity_path_type (str | Unset): The critical path type, which indicates how critical path activities
            are identified for the project, based on either 'Critical Float' or 'Longest Path'.
        critical_float_threshold (float | Unset): The option used for setting the critical float threshold value when
            scheduling projects.
        current_baseline_project_object_id (int | Unset): The unique ID of the project's baseline to use for computing
            summaries.
        current_budget (float | Unset): The sum of the original budget plus the approved and pending budgets from the
            budget change log.
        current_variance (float | Unset): The difference between the current budget and the total spending plan.
            Calculated as current budget - total spending plan. Not rolled up
        data_date (datetime.datetime | Unset): The current data date for the project. The project status is up to date
            as of the data date. The data date is modified when project actuals are applied.
        date_added (datetime.datetime | Unset): The date on which the project was added to the Project Management
            database.
        default_price_time_units (str | Unset): The time units associated with the project's default price per time.
            Valid values are 'Hour', 'Day', 'Week', 'Month', and 'Year'.
        description (str | Unset): The description of the Project.
        discount_application_period (str | Unset): the timescale for entering ROI spending and benefit plan. Valid
            values are 'Month', 'Quarter', or 'Year'.
        distributed_current_budget (float | Unset): The current budget values from one level lower.
        earned_value_compute_type (str | Unset): The technique used for computing earned-value percent complete for
            activities within the Project. Valid values are 'Activity Percent Complete', '0 / 100', '50 / 50', 'Custom
            Percent Complete', 'WBS Milestones Percent Complete', and 'Activity Percent Complete Using Resource Curves'.
        earned_value_etc_compute_type (str | Unset): The technique for computing earned-value estimate-to-complete for
            activities within the Project. Valid values are 'ETC = Remaining Cost for Activity', 'Performance Factor = 1',
            'Performance Factor = Custom Value', 'Performance Factor = 1 / Cost Performance Index', and 'Performance Factor
            = 1 / (Cost Performance Index * Schedule Performance Index)'.
        earned_value_etc_user_value (float | Unset): The user-defined performance factor, PF, for computing earned-value
            estimate-to-complete. ETC is computed as PF * (BAC - earned value).
        earned_value_user_percent (float | Unset): The user-defined percent complete for computing earned value for
            activities within the Project. A value of, say, 25 means that 25% of the planned amount is earned when the
            activity is started and the remainder is earned when the activity is completed.
        enable_prime_syc_flag (bool | Unset):
        enable_publication (bool | Unset): Enables the project to be processed by the Project Arbiter service.
        enable_summarization (bool | Unset): The option which, when true, directs the Summarizer service to
            automatically summarize the project. If this is false, the project will be skipped during the summary run.
        etl_interval (str | Unset): The time interval for ETL for use in P6 Analytics, could be 'None', 'Scheduled',
            'Immediate'.
        financial_period_template_id (int | Unset):
        finish_date (datetime.datetime | Unset): The finish date of the project. This is a summary method calculated
            from fields populated by the Summarizer job service.
        fiscal_year_start_month (int | Unset): The month that marks the beginning of the fiscal year for the project.
        forecast_finish_date (datetime.datetime | Unset): The alternate end date to be optionally used by the scheduler.
            The user sets the alternate end date by dragging the project bar in the Gantt Chart while manually leveling the
            resource profile in a resource analysis layout.
        forecast_start_date (datetime.datetime | Unset): The alternate start date to be optionally used by the
            scheduler. The user sets the alternate start date by dragging the project bar in the Gantt Chart around while
            manually leveling the resource profile in a resource analysis layout.
        guid (str | Unset): The globally unique ID generated by the system.
        has_future_bucket_data (bool | Unset): The flag that indicates whether a resource assignment in the project has
            future bucket data.
        history_interval (str | Unset): The time interval for how historical project data is stored for use in P6
            Analytics, could be 'Month', 'Week', 'Quarter', 'Year' and 'Financial Period'.
        history_level (str | Unset): The level of historical project data that is stored for use in P6 Analytics, cab be
            'None', 'Project', 'WBS' and 'Activity'.
        ignore_other_project_relationships (bool | Unset): Determines whether to ignore activity relationships between
            projects.
        independent_etc_labor_units (float | Unset): The user-entered ETC total labor.
        independent_etc_total_cost (float | Unset): The user-entered ETC total cost.
        integrated_type (str | Unset): The flag indicating whether the project is integrated with an Enterprise Resource
            Planning (ERP) system. 'Fusion' indicates the project is integrated with Oracle Fusion. 'ERP' indicates the
            project is integrated with another ERP system. 'Gateway' indicates the project is integrated with Oracle
            Primavera Gateway.
        is_template (bool | Unset): The boolean value indicating if this Project is a template Project.
        last_apply_actuals_date (datetime.datetime | Unset): The last date Apply Actuals was run for this project.
        last_financial_period_object_id (int | Unset): The unique ID of the last closed financial period for the
            project.
        last_level_date (datetime.datetime | Unset): The date the project was last leveled.
        last_published_on (datetime.datetime | Unset): The date the project was last published.
        last_schedule_date (datetime.datetime | Unset): The date the project was last scheduled.
        last_summarized_date (datetime.datetime | Unset): The date the project was last summarized.
        last_update_date (datetime.datetime | Unset): The date this project was last updated.
        last_update_user (str | Unset): The name of the user that last updated this project.
        latitude (float | Unset):
        level_all_resources (bool | Unset): The resources to level.
        level_date_flag (bool | Unset): Gets the date the project was last leveled.
        level_float_threshold_count (int | Unset): The amount of float you want to maintain when activities are delayed
            because of resource conflicts. You can type a new number and time unit.
        level_outer_assign (bool | Unset): Include resource assignments in other projects to level.
        level_outer_assign_priority (int | Unset): Set the range of the leveling priority that you specify when
            determining if a resource is over-allocated. Assignments in closed projects are considered.
        level_over_allocation_percent (float | Unset):
        level_priority_list (str | Unset): Lists the fields by which to prioritize resources when leveling. Priorities
            are used only when more than one activity competes for the same resource at the same time. Sort Order: The order
            in which to level resources according to the field names displayed. Double-click the Sort Order field to choose
            Ascending, Descending, or Hierarchy (option only appears for fields that are hierarchical)
        level_resource_list (str | Unset): Consists of the list of resources to level.
        level_within_float (bool | Unset): To delay activities with resource conflicts only up to their late finish
            date.
        leveling_priority (int | Unset): The priority for scheduling.
        limit_multiple_float_paths (bool | Unset): The option used for enabling/disabling limit multiple float paths
            when scheduling projects.
        link_actual_to_actual_this_period (bool | Unset): The flag that indicates whether actual units and costs are
            linked to actual-this-period units and costs. Setting this field to true asynchronously causes all actual-this-
            period values to be recalculated for the project via a job service. Default = 'true'.
        link_percent_complete_with_actual (bool | Unset): The flag that indicates whether actual units and cost should
            be recalculated when percent complete changes. Default = 'false'
        link_planned_and_at_completion_flag (bool | Unset): The flag that indicates whether the At Completion Cost/Units
            should be linked to Planned Cost/Units for not-started activities. Default = 'true'
        location_name (str | Unset): The name of the location assigned to the project.
        location_object_id (int | Unset): The unique ID of the location assigned to the project.
        longitude (float | Unset):
        make_open_ended_activities_critical (bool | Unset): The option used by the scheduler for automatically leveling
            resources when scheduling projects.
        maximum_multiple_float_paths (int | Unset): The number of critical float paths to calculate. For example, if you
            set the field to five, the module calculates the five most critical float paths ending with the activity you
            selected. The module ranks each float path from most critical to least critical, and stores the value for each
            activity in the Float Path field. For example, if you calculate five float paths, the module will store a value
            of one in the Float Path field for each activity in the most critical float path; the module will store a value
            of five for each activity in the least critical float path. Note: To view the critical float paths after you
            schedule the project, group activities in the Activity Table by Float Path and sort by Float Path Order. A Float
            Path value of one indicates that those activities are part of the most critical float path. The Float Path Order
            value indicates the order in which the activities were processed.
        multiple_float_paths_enabled (bool | Unset): The Boolean value that indicates whether multiple critical float
            paths (sequences of activities) should be calculated in the project schedule.
        multiple_float_paths_ending_activity_object_id (int | Unset): The activity in the WBS that you want to represent
            the end of the float paths. Typically, this will be a milestone activity or some other significant activity that
            has a start date or end date that cannot change. Note: if a value is not assigned, the module will choose an
            activity based on MultipleFloatPathsUseTotalFloat. If you are calculating multiple paths using Free Float, the
            module will choose the open-ended activity with the most critical Free Float. If you are calculating multiple
            paths using Total Float, the module will calculate the Total Float for all activity relationships, then choose
            the activity with the most critical Relationship Total Float.
        multiple_float_paths_use_total_float (bool | Unset):
        must_finish_by_date (datetime.datetime | Unset): The date by which all project activities must finish. If
            entered, it is used as the project late finish date by the project scheduler.
        net_present_value (float | Unset): The estimated net value, at the present time for the project
        obs_name (str | Unset): The name of the person/role in the organization, sometimes referred to as the
            "responsible manager".
        obs_object_id (int | Unset): The unique ID of the project manager from the project's OBS tree who is responsible
            for the Project.
        object_id (int | Unset): The unique ID generated by the system.
        original_budget (float | Unset): The original budget for the project.
        out_of_sequence_schedule_type (str | Unset): The type of logic used to schedule the progressed activities:
            'Retained Logic', 'Progress Override', or 'Actual Dates'.
        overall_project_score (int | Unset): The project score calculated based on all project code types assigned to
            this project.
        owner_resource_object_id (int | Unset): The unique ID of the Owner Resource of this project.
        parent_eps_id (str | Unset): The ID of the parent EPS of this project.
        parent_eps_name (str | Unset): The parent EPS of this project.
        payback_period (int | Unset): The PaybackPeriod for the project
        performance_percent_complete_by_labor_units (float | Unset):
        planned_start_date (datetime.datetime | Unset): The planned start date of the project. Used by the project
            scheduler.
        post_response_pessimistic_finish (datetime.datetime | Unset):
        post_response_pessimistic_start (datetime.datetime | Unset):
        pre_response_pessimistic_finish (datetime.datetime | Unset):
        pre_response_pessimistic_start (datetime.datetime | Unset):
        primary_resources_can_mark_activities_as_completed (bool | Unset): The flag that indicates whether primary
            resources can mark the project activities as completed. If not selected, a primary resource can only mark an
            activity as For Review. In this case the project manager reviews the activity and marks it as either Rejected or
            completed.
        primary_resources_can_update_activity_dates (bool | Unset):
        project_forecast_start_date (datetime.datetime | Unset): The alternate start date to be optionally used by the
            scheduler. The user sets the alternate start date by dragging the project bar in the Gantt Chart around while
            manually leveling the resource profile in a resource analysis layout.
        project_schedule_type (str | Unset): The type of schedule the project is based on. It can contain either
            "Duration" or "Resource" or "Cost".
        property_type (str | Unset): The project property name associated with the scheduling of projects.
        proposed_budget (float | Unset): The Proposed Budget, which is the sum of the original budget plus the approved
            and pending budgets from the budget change log.
        publication_priority (int | Unset): A priority value the Project Arbiter service uses to determine the order in
            which projects are submitted to the service queue, where 1 is highest priority and 100 is lowest priority.
        publish_level (str | Unset): The publish level for the project publication.
        relationship_lag_calendar (str | Unset): The calendar used to calculate the lag between predecessors and
            successors for all activities. Valid values are 'Predecessor Activity Calendar', 'Successor Activity Calendar',
            '24 Hour Calendar', and 'Project Default Calendar'. If you do not select a calendar, the successor activity
            calendar is used.
        reset_planned_to_remaining_flag (bool | Unset): The flag that indicates whether to reset Planned Duration and
            Units to Remaining Duration and Units, or to reset Remaining Duration and Units to Planned Duration and Units
            when the Activity Status is or becomes not started. Default = 'true'
        resource_can_be_assigned_to_same_activity_more_than_once (bool | Unset): The flag that indicates whether a
            resource can be assigned more than once to the same activity. This is useful when the resource is expected to
            perform more than one role on an activity, for example, documentation plus QA.
        resource_name (str | Unset):
        resources_can_assign_themselves_to_activities (bool | Unset): The flag that indicates whether timesheet
            application users are allowed to assign themselves to activities in this project.
        resources_can_assign_themselves_to_activities_outside_obs_access (bool | Unset):
        resources_can_edit_assignment_percent_complete (bool | Unset): The flag that indicates whether the project's
            resource update the remaining units or the percent complete for their activities in the timesheet application.
        resources_can_mark_assignment_as_completed (bool | Unset): The flag that indicates whether timesheet resources
            can mark the assignment as complete.
        resources_can_view_inactive_activities (bool | Unset): The flag that indicates whether timesheet resources can
            view inactive project activities.
        return_on_investment (float | Unset): The estimated return on investment for the project
        review_type (str | Unset):
        risk_exposure (float | Unset): The calculated exposure value for the project.
        risk_level (str | Unset): The risk level assigned to the project: 'Very High', 'High', 'Medium', 'Low', and
            'Very Low'.
        risk_matrix_name (str | Unset): The name of the risk matrix.
        risk_matrix_object_id (int | Unset): The unique ID of the associated Risk Matrix.
        risk_score (int | Unset): The calculated risk score for the project.
        schedule_wbs_hierarchy_type (str | Unset): The option used for specifying WBS Hierachy sync type.
        scheduled_finish_date (datetime.datetime | Unset): The early finish date of the latest activity in the project,
            as computed by the project scheduler.
        source_project_object_id (int | Unset): The unique ID of the project from which the reflection project was
            created, if the current project is a reflection project.
        start_date (datetime.datetime | Unset): The start date of the project. This is a summary method calculated from
            fields populated by the Summarizer job service.
        start_to_start_lag_calculation_type (bool | Unset): The method used to calculate lag when a start-to-start
            relationship exists and the predecessor starts out of sequence. Actual Start sets the successor's start
            according to the time elapsed from the predecessor's actual start (the successor's start date is the data date
            plus any remaining lag). Early Start sets the successor's start according to the amount of work that the
            predecessor activity accomplishes (the expired lag is calculated as the number of work periods between the
            actual start and the data date, and the successor's start date is the predecessor's internal early start plus
            any remaining lag).
        status (str | Unset): The project status: 'Planned', 'Active', 'Inactive', 'What-If', 'Requested', or
            'Template'.
        status_reviewer_name (str | Unset): The name of the user reviewing status updates.
        status_reviewer_object_id (str | Unset): The unique ID of the user reviewing status updates.
        strategic_priority (int | Unset): The project's priority. The range is from 1 to 10,000.
        summarize_resources_roles_by_wbs (bool | Unset):
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
            the Project for the current baseline.
        summary_baseline_total_cost (float | Unset): The Planned Total Cost for the activity in the primary baseline,
            including labor resources, nonlabor resources, and project expenses. Baseline Planned Total Cost = Baseline
            Planned Labor Cost + Baseline Planned Nonlabor Cost + Baseline Planned Expense Cost.
        summary_budget_at_completion_by_cost (float | Unset): The Planned Total Cost through activity completion.
            Computed as Planned Labor Cost + Planned Nonlabor Cost + Planned Expense Cost, same as the Planned Total Cost.
        summary_budget_at_completion_by_labor_units (float | Unset): The Baseline Labor Units
        summary_completed_activity_count (int | Unset): The number of activities that have an Actual Finish in the
            Project.
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
        summary_duration_percent_complete (float | Unset): The percent complete of the activity duration. Computed as
            (planned duration - remaining duration) / planned duration * 100. The planned duration is taken from the current
            plan, not from the baseline.
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
            Labor Units. (Estimate To Complete Labor Units is calculated based off of the Earned Value setting on the
            Project.)
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
            the Project. Computed as actual labor units / at complete labor units * 100. Always in the range 0 to 100.
        summary_labor_units_variance (float | Unset): The difference between baseline labor units and at completion
            labor units. Calculated as baseline labor units - at completion labor units.
        summary_level (str | Unset): The summary level for the project while performing project summarization.
        summary_material_cost_percent_complete (float | Unset): The percent complete of cost for all material resources
            assigned to the project. It is computed as Actual Material Cost / At Complete Material Cost * 100, and it is
            always in the range of 0 to 100.
        summary_material_cost_variance (float | Unset): The variance that is calculated as Baseline Material Cost - At
            Completion Material Cost.
        summary_non_labor_cost_percent_complete (float | Unset): The percent complete of cost for all non-labor
            resources assigned to the project. It is computed as Actual Nonlabor Cost / At Complete Nonlabor Cost * 100, and
            it is always in the range of 0 to 100.
        summary_non_labor_cost_variance (float | Unset): Tthe Baseline Planned Nonlabor Cost - At Completion Nonlabor
            Cost.
        summary_non_labor_units_percent_complete (float | Unset): The percent complete of units for all nonlabor
            resources for the Project. Computed as Actual Nonlabor Cost / At Completion Nonlabor Cost * 100. Always in the
            range 0 to 100.
        summary_non_labor_units_variance (float | Unset): The difference between baseline nonlabor units and at
            completion non labor units. Calculated as baseline nonlabor units - at completion nonlabor units.
        summary_not_started_activity_count (int | Unset): The number of activities that are currently not started.
        summary_performance_percent_complete_by_cost (float | Unset): he percent complete of performance for all labor
            resources, nonlabor resources, and expenses. Computed as Earned Value / Budget At Completion * 100. Always in
            the range 0 to 100.
        summary_performance_percent_complete_by_labor_units (float | Unset): The percent complete of performance for all
            labor resources. Computed as earned value labor units / baseline labor units * 100. Always in the range 0 to
            100.
        summary_planned_cost (float | Unset): The sum of all planned expense, non labor, labor, and material costs in
            the project.
        summary_planned_duration (float | Unset): The total working days between planned start and finish dates in the
            project.
        summary_planned_expense_cost (float | Unset): The sum of all planned expense costs in the project.
        summary_planned_finish_date (datetime.datetime | Unset): The latest planned finish date of all activities in the
            project.
        summary_planned_labor_cost (float | Unset): The sum of all planned labor costs in the project.
        summary_planned_labor_units (float | Unset): The sum of all planned labor units in the project.
        summary_planned_material_cost (float | Unset): The sum of all planned material costs in the project.
        summary_planned_non_labor_cost (float | Unset): The sum of all planned non labor costs in the project.
        summary_planned_non_labor_units (float | Unset): The sum of all planned non labor units in the project.
        summary_planned_start_date (datetime.datetime | Unset): The earliest planned start date of all activities in the
            project.
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
        summary_remaining_duration (float | Unset): The total working time from the Project remaining start date to the
            remaining finish date.
        summary_remaining_expense_cost (float | Unset): The remaining costs for all project expenses associated with the
            activities in the Project.
        summary_remaining_finish_date (datetime.datetime | Unset): The date the resource is scheduled to finish the
            remaining work for the activity. This date is computed by the project scheduler but can be updated manually by
            the project manager. Before the activity is started, the remaining finish date is the same as the planned finish
            date.
        summary_remaining_labor_cost (float | Unset): The remaining costs for all labor resources assigned to the
            activities. The remaining cost reflects the cost remaining for the Project.
        summary_remaining_labor_units (float | Unset): The remaining units for all labor resources assigned to the
            activities. The remaining units reflects the work remaining to be done for the Project.
        summary_remaining_material_cost (float | Unset): The remaining material costs for all project expenses
            associated with the activities in the Project.
        summary_remaining_non_labor_cost (float | Unset): The remaining nonlabor costs for all project expenses
            associated with the activities in the Project.
        summary_remaining_non_labor_units (float | Unset): The remaining units for all nonlabor resources assigned to
            the activities. The remaining units reflects the work remaining to be done for the Project.
        summary_remaining_start_date (datetime.datetime | Unset): The earliest remaining start of all activities
            assigned to the Project.
        summary_remaining_total_cost (float | Unset): The sum of all remaining total costs in the Project.
        summary_schedule_percent_complete (float | Unset): The measure that indicates how much of the Project baseline
            duration has been completed so far. Computed based on where the current data date falls between the activity's
            baseline start and finish dates. If the data date is earlier than the baseline start, the schedule % complete is
            0. If the data date is later than the baseline finish, the schedule % complete is 100. The schedule % complete
            indicates how much of the Project duration should be currently completed, relative to the selected baseline.
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
        summary_total_float (float | Unset): The amount of time the Project can be delayed before delaying the project
            finish date. Total float can be computed as late start - early start or as late finish - early finish; this
            option can be set when running the project scheduler.
        summary_units_percent_complete (float | Unset): The percent complete of units for the resource assignments in
            the Project. Computed as Actual Units / At Complete Units * 100. Always in the range 0 to 100.
        summary_variance_at_completion_by_labor_units (float | Unset): The Baseline Planned Total Labor Units minus
            Estimate at Completion Labor Units.
        sync_wbs_hierarchy_flag (bool | Unset): The option used for enabling/disabling WBS Hierachy sync.
        team_member_activity_fields (str | Unset): The list of activity fields that can be updated by a team member
            using the P6 Team Member interfaces.
        team_member_add_new_actual_units (bool | Unset): The indicator that determines whether team members enter new
            actual units.
        team_member_assignment_option (str | Unset): The indicator that determines whether team member can update
            activity fields, assignment fields, or both using the P6 Team Member interfaces.
        team_member_can_status_other_resources (bool | Unset): The indicator that determines whether team member can
            status other resource assignments on an activity.
        team_member_can_update_notebooks (bool | Unset): The indicator that determines whether notebooks can be updated
            by the team member.
        team_member_display_baseline_dates_flag (bool | Unset):
        team_member_display_planned_units (bool | Unset): The indicator that determines whether or not a team member can
            display planned units on activities and assignments.
        team_member_display_total_float_flag (bool | Unset):
        team_member_display_discussions_flag (bool | Unset):
        team_member_include_primary_resources (bool | Unset): Primary Resource Flag determines if Team Members status
            their activities as Primary Resources too.
        team_member_read_only_activity_fields (str | Unset):
        team_member_resource_assignment_fields (str | Unset):
        team_member_step_udf_viewable_fields (str | Unset):
        team_member_steps_add_deletable (bool | Unset): The flag which determines whether steps can be added or deleted
            in P6 Team Member interfaces.
        team_member_viewable_fields (str | Unset): The list of fields that are viewable by a team member using the P6
            Team Member interfaces.
        total_benefit_plan (float | Unset): The sum of the monthly benefit plan.
        total_benefit_plan_tally (float | Unset): The sum of the monthly benefit plan tally.
        total_funding (float | Unset): The total amount of funding contributed to the project by your funding sources.
        total_spending_plan (float | Unset): The sum of the monthly spending plan.
        total_spending_plan_tally (float | Unset): The sum of the monthly spending plan tally.
        unallocated_budget (float | Unset): The total current budget minus the distributed current budget.
        undistributed_current_variance (float | Unset): The total spending plan minus the total spending plan tally.
        unifier_cbs_tasks_only_flag (bool | Unset): The flag that indicates whether P6 will only send activities with
            CBS codes assigned.
        unifier_data_mapping_name (str | Unset): The Unifier data mapping name.
        unifier_delete_activities_flag (bool | Unset): The flag that indicates whether activities removed from the P6
            Schedule are deleted in Unifier.
        unifier_enabled_flag (bool | Unset): The flag that indicates whether P6 integration with Unifier schedule sheet
            is enabled.
        unifier_project_name (str | Unset): Field to specify Unifier project number.
        unifier_project_number (str | Unset): The Unifier project number.
        unifier_schedule_sheet_name (str | Unset): The Unifier schedule sheet name.
        use_expected_finish_dates (bool | Unset): The option used for setting activity finish dates as the expected
            finish dates when scheduling projects.
        use_project_baseline_for_earned_value (bool | Unset): The flag that indicates whether earned value should be
            calculated based on the project baseline or the user's primary baseline. This setting only affects Project
            Management, not the Integration API or Primavera's Web application.
        wbs_code_separator (str | Unset): The character used to separate the concatenated code fields for the project's
            WBS tree.
        wbs_hierarchy_levels (int | Unset): The option used for specifying WBS Hierachy sync level
        wbs_milestone_percent_complete (float | Unset): The WBSMilestonePercentComplete field determines whether to
            calculate earned value by defining milestones at the WBS level and assigning a level of significance or weight
            to each of them. As progress occurs and you mark each milestone complete, the WBS element's performance percent
            complete is calculated based on the weight of the milestone.
        wbs_object_id (int | Unset): The internal WBS ID of the project. This ID cannot be used to load a WBS object
            directly.
        web_site_root_directory (str | Unset): The root directory for storing project Web site files before they are
            published to the Web server.
        web_site_url (str | Unset): The project Web site URL, which is the Web address of the project's website.
        external (bool | Unset):
    """

    id: str
    name: str
    parent_eps_object_id: int
    activity_default_activity_type: str | Unset = UNSET
    activity_default_calendar_name: str | Unset = UNSET
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
    allow_negative_actual_units_flag: bool | Unset = UNSET
    allow_status_review: bool | Unset = UNSET
    annual_discount_rate: float | Unset = UNSET
    anticipated_finish_date: datetime.datetime | Unset = UNSET
    anticipated_start_date: datetime.datetime | Unset = UNSET
    assignment_default_driving_flag: bool | Unset = UNSET
    assignment_default_rate_type: str | Unset = UNSET
    calculate_float_based_on_finish_date: bool | Unset = UNSET
    check_out_date: datetime.datetime | Unset = UNSET
    check_out_status: bool | Unset = UNSET
    check_out_user_object_id: int | Unset = UNSET
    compute_total_float_type: str | Unset = UNSET
    contains_summary_data: bool | Unset = UNSET
    contract_management_group_name: str | Unset = UNSET
    contract_management_project_name: str | Unset = UNSET
    cost_quantity_recalculate_flag: bool | Unset = UNSET
    create_date: datetime.datetime | Unset = UNSET
    create_user: str | Unset = UNSET
    critical_activity_float_limit: float | Unset = UNSET
    critical_activity_float_threshold: float | Unset = UNSET
    critical_activity_path_type: str | Unset = UNSET
    critical_float_threshold: float | Unset = UNSET
    current_baseline_project_object_id: int | Unset = UNSET
    current_budget: float | Unset = UNSET
    current_variance: float | Unset = UNSET
    data_date: datetime.datetime | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    default_price_time_units: str | Unset = UNSET
    description: str | Unset = UNSET
    discount_application_period: str | Unset = UNSET
    distributed_current_budget: float | Unset = UNSET
    earned_value_compute_type: str | Unset = UNSET
    earned_value_etc_compute_type: str | Unset = UNSET
    earned_value_etc_user_value: float | Unset = UNSET
    earned_value_user_percent: float | Unset = UNSET
    enable_prime_syc_flag: bool | Unset = UNSET
    enable_publication: bool | Unset = UNSET
    enable_summarization: bool | Unset = UNSET
    etl_interval: str | Unset = UNSET
    financial_period_template_id: int | Unset = UNSET
    finish_date: datetime.datetime | Unset = UNSET
    fiscal_year_start_month: int | Unset = UNSET
    forecast_finish_date: datetime.datetime | Unset = UNSET
    forecast_start_date: datetime.datetime | Unset = UNSET
    guid: str | Unset = UNSET
    has_future_bucket_data: bool | Unset = UNSET
    history_interval: str | Unset = UNSET
    history_level: str | Unset = UNSET
    ignore_other_project_relationships: bool | Unset = UNSET
    independent_etc_labor_units: float | Unset = UNSET
    independent_etc_total_cost: float | Unset = UNSET
    integrated_type: str | Unset = UNSET
    is_template: bool | Unset = UNSET
    last_apply_actuals_date: datetime.datetime | Unset = UNSET
    last_financial_period_object_id: int | Unset = UNSET
    last_level_date: datetime.datetime | Unset = UNSET
    last_published_on: datetime.datetime | Unset = UNSET
    last_schedule_date: datetime.datetime | Unset = UNSET
    last_summarized_date: datetime.datetime | Unset = UNSET
    last_update_date: datetime.datetime | Unset = UNSET
    last_update_user: str | Unset = UNSET
    latitude: float | Unset = UNSET
    level_all_resources: bool | Unset = UNSET
    level_date_flag: bool | Unset = UNSET
    level_float_threshold_count: int | Unset = UNSET
    level_outer_assign: bool | Unset = UNSET
    level_outer_assign_priority: int | Unset = UNSET
    level_over_allocation_percent: float | Unset = UNSET
    level_priority_list: str | Unset = UNSET
    level_resource_list: str | Unset = UNSET
    level_within_float: bool | Unset = UNSET
    leveling_priority: int | Unset = UNSET
    limit_multiple_float_paths: bool | Unset = UNSET
    link_actual_to_actual_this_period: bool | Unset = UNSET
    link_percent_complete_with_actual: bool | Unset = UNSET
    link_planned_and_at_completion_flag: bool | Unset = UNSET
    location_name: str | Unset = UNSET
    location_object_id: int | Unset = UNSET
    longitude: float | Unset = UNSET
    make_open_ended_activities_critical: bool | Unset = UNSET
    maximum_multiple_float_paths: int | Unset = UNSET
    multiple_float_paths_enabled: bool | Unset = UNSET
    multiple_float_paths_ending_activity_object_id: int | Unset = UNSET
    multiple_float_paths_use_total_float: bool | Unset = UNSET
    must_finish_by_date: datetime.datetime | Unset = UNSET
    net_present_value: float | Unset = UNSET
    obs_name: str | Unset = UNSET
    obs_object_id: int | Unset = UNSET
    object_id: int | Unset = UNSET
    original_budget: float | Unset = UNSET
    out_of_sequence_schedule_type: str | Unset = UNSET
    overall_project_score: int | Unset = UNSET
    owner_resource_object_id: int | Unset = UNSET
    parent_eps_id: str | Unset = UNSET
    parent_eps_name: str | Unset = UNSET
    payback_period: int | Unset = UNSET
    performance_percent_complete_by_labor_units: float | Unset = UNSET
    planned_start_date: datetime.datetime | Unset = UNSET
    post_response_pessimistic_finish: datetime.datetime | Unset = UNSET
    post_response_pessimistic_start: datetime.datetime | Unset = UNSET
    pre_response_pessimistic_finish: datetime.datetime | Unset = UNSET
    pre_response_pessimistic_start: datetime.datetime | Unset = UNSET
    primary_resources_can_mark_activities_as_completed: bool | Unset = UNSET
    primary_resources_can_update_activity_dates: bool | Unset = UNSET
    project_forecast_start_date: datetime.datetime | Unset = UNSET
    project_schedule_type: str | Unset = UNSET
    property_type: str | Unset = UNSET
    proposed_budget: float | Unset = UNSET
    publication_priority: int | Unset = UNSET
    publish_level: str | Unset = UNSET
    relationship_lag_calendar: str | Unset = UNSET
    reset_planned_to_remaining_flag: bool | Unset = UNSET
    resource_can_be_assigned_to_same_activity_more_than_once: bool | Unset = UNSET
    resource_name: str | Unset = UNSET
    resources_can_assign_themselves_to_activities: bool | Unset = UNSET
    resources_can_assign_themselves_to_activities_outside_obs_access: bool | Unset = UNSET
    resources_can_edit_assignment_percent_complete: bool | Unset = UNSET
    resources_can_mark_assignment_as_completed: bool | Unset = UNSET
    resources_can_view_inactive_activities: bool | Unset = UNSET
    return_on_investment: float | Unset = UNSET
    review_type: str | Unset = UNSET
    risk_exposure: float | Unset = UNSET
    risk_level: str | Unset = UNSET
    risk_matrix_name: str | Unset = UNSET
    risk_matrix_object_id: int | Unset = UNSET
    risk_score: int | Unset = UNSET
    schedule_wbs_hierarchy_type: str | Unset = UNSET
    scheduled_finish_date: datetime.datetime | Unset = UNSET
    source_project_object_id: int | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    start_to_start_lag_calculation_type: bool | Unset = UNSET
    status: str | Unset = UNSET
    status_reviewer_name: str | Unset = UNSET
    status_reviewer_object_id: str | Unset = UNSET
    strategic_priority: int | Unset = UNSET
    summarize_resources_roles_by_wbs: bool | Unset = UNSET
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
    summary_level: str | Unset = UNSET
    summary_material_cost_percent_complete: float | Unset = UNSET
    summary_material_cost_variance: float | Unset = UNSET
    summary_non_labor_cost_percent_complete: float | Unset = UNSET
    summary_non_labor_cost_variance: float | Unset = UNSET
    summary_non_labor_units_percent_complete: float | Unset = UNSET
    summary_non_labor_units_variance: float | Unset = UNSET
    summary_not_started_activity_count: int | Unset = UNSET
    summary_performance_percent_complete_by_cost: float | Unset = UNSET
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
    sync_wbs_hierarchy_flag: bool | Unset = UNSET
    team_member_activity_fields: str | Unset = UNSET
    team_member_add_new_actual_units: bool | Unset = UNSET
    team_member_assignment_option: str | Unset = UNSET
    team_member_can_status_other_resources: bool | Unset = UNSET
    team_member_can_update_notebooks: bool | Unset = UNSET
    team_member_display_baseline_dates_flag: bool | Unset = UNSET
    team_member_display_planned_units: bool | Unset = UNSET
    team_member_display_total_float_flag: bool | Unset = UNSET
    team_member_display_discussions_flag: bool | Unset = UNSET
    team_member_include_primary_resources: bool | Unset = UNSET
    team_member_read_only_activity_fields: str | Unset = UNSET
    team_member_resource_assignment_fields: str | Unset = UNSET
    team_member_step_udf_viewable_fields: str | Unset = UNSET
    team_member_steps_add_deletable: bool | Unset = UNSET
    team_member_viewable_fields: str | Unset = UNSET
    total_benefit_plan: float | Unset = UNSET
    total_benefit_plan_tally: float | Unset = UNSET
    total_funding: float | Unset = UNSET
    total_spending_plan: float | Unset = UNSET
    total_spending_plan_tally: float | Unset = UNSET
    unallocated_budget: float | Unset = UNSET
    undistributed_current_variance: float | Unset = UNSET
    unifier_cbs_tasks_only_flag: bool | Unset = UNSET
    unifier_data_mapping_name: str | Unset = UNSET
    unifier_delete_activities_flag: bool | Unset = UNSET
    unifier_enabled_flag: bool | Unset = UNSET
    unifier_project_name: str | Unset = UNSET
    unifier_project_number: str | Unset = UNSET
    unifier_schedule_sheet_name: str | Unset = UNSET
    use_expected_finish_dates: bool | Unset = UNSET
    use_project_baseline_for_earned_value: bool | Unset = UNSET
    wbs_code_separator: str | Unset = UNSET
    wbs_hierarchy_levels: int | Unset = UNSET
    wbs_milestone_percent_complete: float | Unset = UNSET
    wbs_object_id: int | Unset = UNSET
    web_site_root_directory: str | Unset = UNSET
    web_site_url: str | Unset = UNSET
    external: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        parent_eps_object_id = self.parent_eps_object_id

        activity_default_activity_type = self.activity_default_activity_type

        activity_default_calendar_name = self.activity_default_calendar_name

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

        allow_negative_actual_units_flag = self.allow_negative_actual_units_flag

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

        calculate_float_based_on_finish_date = self.calculate_float_based_on_finish_date

        check_out_date: str | Unset = UNSET
        if not isinstance(self.check_out_date, Unset):
            check_out_date = self.check_out_date.isoformat()

        check_out_status = self.check_out_status

        check_out_user_object_id = self.check_out_user_object_id

        compute_total_float_type = self.compute_total_float_type

        contains_summary_data = self.contains_summary_data

        contract_management_group_name = self.contract_management_group_name

        contract_management_project_name = self.contract_management_project_name

        cost_quantity_recalculate_flag = self.cost_quantity_recalculate_flag

        create_date: str | Unset = UNSET
        if not isinstance(self.create_date, Unset):
            create_date = self.create_date.isoformat()

        create_user = self.create_user

        critical_activity_float_limit = self.critical_activity_float_limit

        critical_activity_float_threshold = self.critical_activity_float_threshold

        critical_activity_path_type = self.critical_activity_path_type

        critical_float_threshold = self.critical_float_threshold

        current_baseline_project_object_id = self.current_baseline_project_object_id

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

        earned_value_compute_type = self.earned_value_compute_type

        earned_value_etc_compute_type = self.earned_value_etc_compute_type

        earned_value_etc_user_value = self.earned_value_etc_user_value

        earned_value_user_percent = self.earned_value_user_percent

        enable_prime_syc_flag = self.enable_prime_syc_flag

        enable_publication = self.enable_publication

        enable_summarization = self.enable_summarization

        etl_interval = self.etl_interval

        financial_period_template_id = self.financial_period_template_id

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

        ignore_other_project_relationships = self.ignore_other_project_relationships

        independent_etc_labor_units = self.independent_etc_labor_units

        independent_etc_total_cost = self.independent_etc_total_cost

        integrated_type = self.integrated_type

        is_template = self.is_template

        last_apply_actuals_date: str | Unset = UNSET
        if not isinstance(self.last_apply_actuals_date, Unset):
            last_apply_actuals_date = self.last_apply_actuals_date.isoformat()

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

        last_update_date: str | Unset = UNSET
        if not isinstance(self.last_update_date, Unset):
            last_update_date = self.last_update_date.isoformat()

        last_update_user = self.last_update_user

        latitude = self.latitude

        level_all_resources = self.level_all_resources

        level_date_flag = self.level_date_flag

        level_float_threshold_count = self.level_float_threshold_count

        level_outer_assign = self.level_outer_assign

        level_outer_assign_priority = self.level_outer_assign_priority

        level_over_allocation_percent = self.level_over_allocation_percent

        level_priority_list = self.level_priority_list

        level_resource_list = self.level_resource_list

        level_within_float = self.level_within_float

        leveling_priority = self.leveling_priority

        limit_multiple_float_paths = self.limit_multiple_float_paths

        link_actual_to_actual_this_period = self.link_actual_to_actual_this_period

        link_percent_complete_with_actual = self.link_percent_complete_with_actual

        link_planned_and_at_completion_flag = self.link_planned_and_at_completion_flag

        location_name = self.location_name

        location_object_id = self.location_object_id

        longitude = self.longitude

        make_open_ended_activities_critical = self.make_open_ended_activities_critical

        maximum_multiple_float_paths = self.maximum_multiple_float_paths

        multiple_float_paths_enabled = self.multiple_float_paths_enabled

        multiple_float_paths_ending_activity_object_id = self.multiple_float_paths_ending_activity_object_id

        multiple_float_paths_use_total_float = self.multiple_float_paths_use_total_float

        must_finish_by_date: str | Unset = UNSET
        if not isinstance(self.must_finish_by_date, Unset):
            must_finish_by_date = self.must_finish_by_date.isoformat()

        net_present_value = self.net_present_value

        obs_name = self.obs_name

        obs_object_id = self.obs_object_id

        object_id = self.object_id

        original_budget = self.original_budget

        out_of_sequence_schedule_type = self.out_of_sequence_schedule_type

        overall_project_score = self.overall_project_score

        owner_resource_object_id = self.owner_resource_object_id

        parent_eps_id = self.parent_eps_id

        parent_eps_name = self.parent_eps_name

        payback_period = self.payback_period

        performance_percent_complete_by_labor_units = self.performance_percent_complete_by_labor_units

        planned_start_date: str | Unset = UNSET
        if not isinstance(self.planned_start_date, Unset):
            planned_start_date = self.planned_start_date.isoformat()

        post_response_pessimistic_finish: str | Unset = UNSET
        if not isinstance(self.post_response_pessimistic_finish, Unset):
            post_response_pessimistic_finish = self.post_response_pessimistic_finish.isoformat()

        post_response_pessimistic_start: str | Unset = UNSET
        if not isinstance(self.post_response_pessimistic_start, Unset):
            post_response_pessimistic_start = self.post_response_pessimistic_start.isoformat()

        pre_response_pessimistic_finish: str | Unset = UNSET
        if not isinstance(self.pre_response_pessimistic_finish, Unset):
            pre_response_pessimistic_finish = self.pre_response_pessimistic_finish.isoformat()

        pre_response_pessimistic_start: str | Unset = UNSET
        if not isinstance(self.pre_response_pessimistic_start, Unset):
            pre_response_pessimistic_start = self.pre_response_pessimistic_start.isoformat()

        primary_resources_can_mark_activities_as_completed = self.primary_resources_can_mark_activities_as_completed

        primary_resources_can_update_activity_dates = self.primary_resources_can_update_activity_dates

        project_forecast_start_date: str | Unset = UNSET
        if not isinstance(self.project_forecast_start_date, Unset):
            project_forecast_start_date = self.project_forecast_start_date.isoformat()

        project_schedule_type = self.project_schedule_type

        property_type = self.property_type

        proposed_budget = self.proposed_budget

        publication_priority = self.publication_priority

        publish_level = self.publish_level

        relationship_lag_calendar = self.relationship_lag_calendar

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

        resources_can_mark_assignment_as_completed = self.resources_can_mark_assignment_as_completed

        resources_can_view_inactive_activities = self.resources_can_view_inactive_activities

        return_on_investment = self.return_on_investment

        review_type = self.review_type

        risk_exposure = self.risk_exposure

        risk_level = self.risk_level

        risk_matrix_name = self.risk_matrix_name

        risk_matrix_object_id = self.risk_matrix_object_id

        risk_score = self.risk_score

        schedule_wbs_hierarchy_type = self.schedule_wbs_hierarchy_type

        scheduled_finish_date: str | Unset = UNSET
        if not isinstance(self.scheduled_finish_date, Unset):
            scheduled_finish_date = self.scheduled_finish_date.isoformat()

        source_project_object_id = self.source_project_object_id

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        start_to_start_lag_calculation_type = self.start_to_start_lag_calculation_type

        status = self.status

        status_reviewer_name = self.status_reviewer_name

        status_reviewer_object_id = self.status_reviewer_object_id

        strategic_priority = self.strategic_priority

        summarize_resources_roles_by_wbs = self.summarize_resources_roles_by_wbs

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

        summary_level = self.summary_level

        summary_material_cost_percent_complete = self.summary_material_cost_percent_complete

        summary_material_cost_variance = self.summary_material_cost_variance

        summary_non_labor_cost_percent_complete = self.summary_non_labor_cost_percent_complete

        summary_non_labor_cost_variance = self.summary_non_labor_cost_variance

        summary_non_labor_units_percent_complete = self.summary_non_labor_units_percent_complete

        summary_non_labor_units_variance = self.summary_non_labor_units_variance

        summary_not_started_activity_count = self.summary_not_started_activity_count

        summary_performance_percent_complete_by_cost = self.summary_performance_percent_complete_by_cost

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

        sync_wbs_hierarchy_flag = self.sync_wbs_hierarchy_flag

        team_member_activity_fields = self.team_member_activity_fields

        team_member_add_new_actual_units = self.team_member_add_new_actual_units

        team_member_assignment_option = self.team_member_assignment_option

        team_member_can_status_other_resources = self.team_member_can_status_other_resources

        team_member_can_update_notebooks = self.team_member_can_update_notebooks

        team_member_display_baseline_dates_flag = self.team_member_display_baseline_dates_flag

        team_member_display_planned_units = self.team_member_display_planned_units

        team_member_display_total_float_flag = self.team_member_display_total_float_flag

        team_member_display_discussions_flag = self.team_member_display_discussions_flag

        team_member_include_primary_resources = self.team_member_include_primary_resources

        team_member_read_only_activity_fields = self.team_member_read_only_activity_fields

        team_member_resource_assignment_fields = self.team_member_resource_assignment_fields

        team_member_step_udf_viewable_fields = self.team_member_step_udf_viewable_fields

        team_member_steps_add_deletable = self.team_member_steps_add_deletable

        team_member_viewable_fields = self.team_member_viewable_fields

        total_benefit_plan = self.total_benefit_plan

        total_benefit_plan_tally = self.total_benefit_plan_tally

        total_funding = self.total_funding

        total_spending_plan = self.total_spending_plan

        total_spending_plan_tally = self.total_spending_plan_tally

        unallocated_budget = self.unallocated_budget

        undistributed_current_variance = self.undistributed_current_variance

        unifier_cbs_tasks_only_flag = self.unifier_cbs_tasks_only_flag

        unifier_data_mapping_name = self.unifier_data_mapping_name

        unifier_delete_activities_flag = self.unifier_delete_activities_flag

        unifier_enabled_flag = self.unifier_enabled_flag

        unifier_project_name = self.unifier_project_name

        unifier_project_number = self.unifier_project_number

        unifier_schedule_sheet_name = self.unifier_schedule_sheet_name

        use_expected_finish_dates = self.use_expected_finish_dates

        use_project_baseline_for_earned_value = self.use_project_baseline_for_earned_value

        wbs_code_separator = self.wbs_code_separator

        wbs_hierarchy_levels = self.wbs_hierarchy_levels

        wbs_milestone_percent_complete = self.wbs_milestone_percent_complete

        wbs_object_id = self.wbs_object_id

        web_site_root_directory = self.web_site_root_directory

        web_site_url = self.web_site_url

        external = self.external

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
        if activity_default_calendar_name is not UNSET:
            field_dict["ActivityDefaultCalendarName"] = activity_default_calendar_name
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
        if allow_negative_actual_units_flag is not UNSET:
            field_dict["AllowNegativeActualUnitsFlag"] = allow_negative_actual_units_flag
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
        if calculate_float_based_on_finish_date is not UNSET:
            field_dict["CalculateFloatBasedOnFinishDate"] = calculate_float_based_on_finish_date
        if check_out_date is not UNSET:
            field_dict["CheckOutDate"] = check_out_date
        if check_out_status is not UNSET:
            field_dict["CheckOutStatus"] = check_out_status
        if check_out_user_object_id is not UNSET:
            field_dict["CheckOutUserObjectId"] = check_out_user_object_id
        if compute_total_float_type is not UNSET:
            field_dict["ComputeTotalFloatType"] = compute_total_float_type
        if contains_summary_data is not UNSET:
            field_dict["ContainsSummaryData"] = contains_summary_data
        if contract_management_group_name is not UNSET:
            field_dict["ContractManagementGroupName"] = contract_management_group_name
        if contract_management_project_name is not UNSET:
            field_dict["ContractManagementProjectName"] = contract_management_project_name
        if cost_quantity_recalculate_flag is not UNSET:
            field_dict["CostQuantityRecalculateFlag"] = cost_quantity_recalculate_flag
        if create_date is not UNSET:
            field_dict["CreateDate"] = create_date
        if create_user is not UNSET:
            field_dict["CreateUser"] = create_user
        if critical_activity_float_limit is not UNSET:
            field_dict["CriticalActivityFloatLimit"] = critical_activity_float_limit
        if critical_activity_float_threshold is not UNSET:
            field_dict["CriticalActivityFloatThreshold"] = critical_activity_float_threshold
        if critical_activity_path_type is not UNSET:
            field_dict["CriticalActivityPathType"] = critical_activity_path_type
        if critical_float_threshold is not UNSET:
            field_dict["CriticalFloatThreshold"] = critical_float_threshold
        if current_baseline_project_object_id is not UNSET:
            field_dict["CurrentBaselineProjectObjectId"] = current_baseline_project_object_id
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
        if earned_value_compute_type is not UNSET:
            field_dict["EarnedValueComputeType"] = earned_value_compute_type
        if earned_value_etc_compute_type is not UNSET:
            field_dict["EarnedValueETCComputeType"] = earned_value_etc_compute_type
        if earned_value_etc_user_value is not UNSET:
            field_dict["EarnedValueETCUserValue"] = earned_value_etc_user_value
        if earned_value_user_percent is not UNSET:
            field_dict["EarnedValueUserPercent"] = earned_value_user_percent
        if enable_prime_syc_flag is not UNSET:
            field_dict["EnablePrimeSycFlag"] = enable_prime_syc_flag
        if enable_publication is not UNSET:
            field_dict["EnablePublication"] = enable_publication
        if enable_summarization is not UNSET:
            field_dict["EnableSummarization"] = enable_summarization
        if etl_interval is not UNSET:
            field_dict["EtlInterval"] = etl_interval
        if financial_period_template_id is not UNSET:
            field_dict["FinancialPeriodTemplateId"] = financial_period_template_id
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
        if ignore_other_project_relationships is not UNSET:
            field_dict["IgnoreOtherProjectRelationships"] = ignore_other_project_relationships
        if independent_etc_labor_units is not UNSET:
            field_dict["IndependentETCLaborUnits"] = independent_etc_labor_units
        if independent_etc_total_cost is not UNSET:
            field_dict["IndependentETCTotalCost"] = independent_etc_total_cost
        if integrated_type is not UNSET:
            field_dict["IntegratedType"] = integrated_type
        if is_template is not UNSET:
            field_dict["IsTemplate"] = is_template
        if last_apply_actuals_date is not UNSET:
            field_dict["LastApplyActualsDate"] = last_apply_actuals_date
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
        if last_update_date is not UNSET:
            field_dict["LastUpdateDate"] = last_update_date
        if last_update_user is not UNSET:
            field_dict["LastUpdateUser"] = last_update_user
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if level_all_resources is not UNSET:
            field_dict["LevelAllResources"] = level_all_resources
        if level_date_flag is not UNSET:
            field_dict["LevelDateFlag"] = level_date_flag
        if level_float_threshold_count is not UNSET:
            field_dict["LevelFloatThresholdCount"] = level_float_threshold_count
        if level_outer_assign is not UNSET:
            field_dict["LevelOuterAssign"] = level_outer_assign
        if level_outer_assign_priority is not UNSET:
            field_dict["LevelOuterAssignPriority"] = level_outer_assign_priority
        if level_over_allocation_percent is not UNSET:
            field_dict["LevelOverAllocationPercent"] = level_over_allocation_percent
        if level_priority_list is not UNSET:
            field_dict["LevelPriorityList"] = level_priority_list
        if level_resource_list is not UNSET:
            field_dict["LevelResourceList"] = level_resource_list
        if level_within_float is not UNSET:
            field_dict["LevelWithinFloat"] = level_within_float
        if leveling_priority is not UNSET:
            field_dict["LevelingPriority"] = leveling_priority
        if limit_multiple_float_paths is not UNSET:
            field_dict["LimitMultipleFloatPaths"] = limit_multiple_float_paths
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
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if make_open_ended_activities_critical is not UNSET:
            field_dict["MakeOpenEndedActivitiesCritical"] = make_open_ended_activities_critical
        if maximum_multiple_float_paths is not UNSET:
            field_dict["MaximumMultipleFloatPaths"] = maximum_multiple_float_paths
        if multiple_float_paths_enabled is not UNSET:
            field_dict["MultipleFloatPathsEnabled"] = multiple_float_paths_enabled
        if multiple_float_paths_ending_activity_object_id is not UNSET:
            field_dict["MultipleFloatPathsEndingActivityObjectId"] = multiple_float_paths_ending_activity_object_id
        if multiple_float_paths_use_total_float is not UNSET:
            field_dict["MultipleFloatPathsUseTotalFloat"] = multiple_float_paths_use_total_float
        if must_finish_by_date is not UNSET:
            field_dict["MustFinishByDate"] = must_finish_by_date
        if net_present_value is not UNSET:
            field_dict["NetPresentValue"] = net_present_value
        if obs_name is not UNSET:
            field_dict["OBSName"] = obs_name
        if obs_object_id is not UNSET:
            field_dict["OBSObjectId"] = obs_object_id
        if object_id is not UNSET:
            field_dict["ObjectId"] = object_id
        if original_budget is not UNSET:
            field_dict["OriginalBudget"] = original_budget
        if out_of_sequence_schedule_type is not UNSET:
            field_dict["OutOfSequenceScheduleType"] = out_of_sequence_schedule_type
        if overall_project_score is not UNSET:
            field_dict["OverallProjectScore"] = overall_project_score
        if owner_resource_object_id is not UNSET:
            field_dict["OwnerResourceObjectId"] = owner_resource_object_id
        if parent_eps_id is not UNSET:
            field_dict["ParentEPSId"] = parent_eps_id
        if parent_eps_name is not UNSET:
            field_dict["ParentEPSName"] = parent_eps_name
        if payback_period is not UNSET:
            field_dict["PaybackPeriod"] = payback_period
        if performance_percent_complete_by_labor_units is not UNSET:
            field_dict["PerformancePercentCompleteByLaborUnits"] = performance_percent_complete_by_labor_units
        if planned_start_date is not UNSET:
            field_dict["PlannedStartDate"] = planned_start_date
        if post_response_pessimistic_finish is not UNSET:
            field_dict["PostResponsePessimisticFinish"] = post_response_pessimistic_finish
        if post_response_pessimistic_start is not UNSET:
            field_dict["PostResponsePessimisticStart"] = post_response_pessimistic_start
        if pre_response_pessimistic_finish is not UNSET:
            field_dict["PreResponsePessimisticFinish"] = pre_response_pessimistic_finish
        if pre_response_pessimistic_start is not UNSET:
            field_dict["PreResponsePessimisticStart"] = pre_response_pessimistic_start
        if primary_resources_can_mark_activities_as_completed is not UNSET:
            field_dict["PrimaryResourcesCanMarkActivitiesAsCompleted"] = (
                primary_resources_can_mark_activities_as_completed
            )
        if primary_resources_can_update_activity_dates is not UNSET:
            field_dict["PrimaryResourcesCanUpdateActivityDates"] = primary_resources_can_update_activity_dates
        if project_forecast_start_date is not UNSET:
            field_dict["ProjectForecastStartDate"] = project_forecast_start_date
        if project_schedule_type is not UNSET:
            field_dict["ProjectScheduleType"] = project_schedule_type
        if property_type is not UNSET:
            field_dict["PropertyType"] = property_type
        if proposed_budget is not UNSET:
            field_dict["ProposedBudget"] = proposed_budget
        if publication_priority is not UNSET:
            field_dict["PublicationPriority"] = publication_priority
        if publish_level is not UNSET:
            field_dict["PublishLevel"] = publish_level
        if relationship_lag_calendar is not UNSET:
            field_dict["RelationshipLagCalendar"] = relationship_lag_calendar
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
        if resources_can_mark_assignment_as_completed is not UNSET:
            field_dict["ResourcesCanMarkAssignmentAsCompleted"] = resources_can_mark_assignment_as_completed
        if resources_can_view_inactive_activities is not UNSET:
            field_dict["ResourcesCanViewInactiveActivities"] = resources_can_view_inactive_activities
        if return_on_investment is not UNSET:
            field_dict["ReturnOnInvestment"] = return_on_investment
        if review_type is not UNSET:
            field_dict["ReviewType"] = review_type
        if risk_exposure is not UNSET:
            field_dict["RiskExposure"] = risk_exposure
        if risk_level is not UNSET:
            field_dict["RiskLevel"] = risk_level
        if risk_matrix_name is not UNSET:
            field_dict["RiskMatrixName"] = risk_matrix_name
        if risk_matrix_object_id is not UNSET:
            field_dict["RiskMatrixObjectId"] = risk_matrix_object_id
        if risk_score is not UNSET:
            field_dict["RiskScore"] = risk_score
        if schedule_wbs_hierarchy_type is not UNSET:
            field_dict["ScheduleWBSHierarchyType"] = schedule_wbs_hierarchy_type
        if scheduled_finish_date is not UNSET:
            field_dict["ScheduledFinishDate"] = scheduled_finish_date
        if source_project_object_id is not UNSET:
            field_dict["SourceProjectObjectId"] = source_project_object_id
        if start_date is not UNSET:
            field_dict["StartDate"] = start_date
        if start_to_start_lag_calculation_type is not UNSET:
            field_dict["StartToStartLagCalculationType"] = start_to_start_lag_calculation_type
        if status is not UNSET:
            field_dict["Status"] = status
        if status_reviewer_name is not UNSET:
            field_dict["StatusReviewerName"] = status_reviewer_name
        if status_reviewer_object_id is not UNSET:
            field_dict["StatusReviewerObjectId"] = status_reviewer_object_id
        if strategic_priority is not UNSET:
            field_dict["StrategicPriority"] = strategic_priority
        if summarize_resources_roles_by_wbs is not UNSET:
            field_dict["SummarizeResourcesRolesByWBS"] = summarize_resources_roles_by_wbs
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
        if summary_level is not UNSET:
            field_dict["SummaryLevel"] = summary_level
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
        if summary_performance_percent_complete_by_cost is not UNSET:
            field_dict["SummaryPerformancePercentCompleteByCost"] = summary_performance_percent_complete_by_cost
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
        if sync_wbs_hierarchy_flag is not UNSET:
            field_dict["SyncWbsHierarchyFlag"] = sync_wbs_hierarchy_flag
        if team_member_activity_fields is not UNSET:
            field_dict["TeamMemberActivityFields"] = team_member_activity_fields
        if team_member_add_new_actual_units is not UNSET:
            field_dict["TeamMemberAddNewActualUnits"] = team_member_add_new_actual_units
        if team_member_assignment_option is not UNSET:
            field_dict["TeamMemberAssignmentOption"] = team_member_assignment_option
        if team_member_can_status_other_resources is not UNSET:
            field_dict["TeamMemberCanStatusOtherResources"] = team_member_can_status_other_resources
        if team_member_can_update_notebooks is not UNSET:
            field_dict["TeamMemberCanUpdateNotebooks"] = team_member_can_update_notebooks
        if team_member_display_baseline_dates_flag is not UNSET:
            field_dict["TeamMemberDisplayBaselineDatesFlag"] = team_member_display_baseline_dates_flag
        if team_member_display_planned_units is not UNSET:
            field_dict["TeamMemberDisplayPlannedUnits"] = team_member_display_planned_units
        if team_member_display_total_float_flag is not UNSET:
            field_dict["TeamMemberDisplayTotalFloatFlag"] = team_member_display_total_float_flag
        if team_member_display_discussions_flag is not UNSET:
            field_dict["TeamMemberDisplayDiscussionsFlag"] = team_member_display_discussions_flag
        if team_member_include_primary_resources is not UNSET:
            field_dict["TeamMemberIncludePrimaryResources"] = team_member_include_primary_resources
        if team_member_read_only_activity_fields is not UNSET:
            field_dict["TeamMemberReadOnlyActivityFields"] = team_member_read_only_activity_fields
        if team_member_resource_assignment_fields is not UNSET:
            field_dict["TeamMemberResourceAssignmentFields"] = team_member_resource_assignment_fields
        if team_member_step_udf_viewable_fields is not UNSET:
            field_dict["TeamMemberStepUDFViewableFields"] = team_member_step_udf_viewable_fields
        if team_member_steps_add_deletable is not UNSET:
            field_dict["TeamMemberStepsAddDeletable"] = team_member_steps_add_deletable
        if team_member_viewable_fields is not UNSET:
            field_dict["TeamMemberViewableFields"] = team_member_viewable_fields
        if total_benefit_plan is not UNSET:
            field_dict["TotalBenefitPlan"] = total_benefit_plan
        if total_benefit_plan_tally is not UNSET:
            field_dict["TotalBenefitPlanTally"] = total_benefit_plan_tally
        if total_funding is not UNSET:
            field_dict["TotalFunding"] = total_funding
        if total_spending_plan is not UNSET:
            field_dict["TotalSpendingPlan"] = total_spending_plan
        if total_spending_plan_tally is not UNSET:
            field_dict["TotalSpendingPlanTally"] = total_spending_plan_tally
        if unallocated_budget is not UNSET:
            field_dict["UnallocatedBudget"] = unallocated_budget
        if undistributed_current_variance is not UNSET:
            field_dict["UndistributedCurrentVariance"] = undistributed_current_variance
        if unifier_cbs_tasks_only_flag is not UNSET:
            field_dict["UnifierCBSTasksOnlyFlag"] = unifier_cbs_tasks_only_flag
        if unifier_data_mapping_name is not UNSET:
            field_dict["UnifierDataMappingName"] = unifier_data_mapping_name
        if unifier_delete_activities_flag is not UNSET:
            field_dict["UnifierDeleteActivitiesFlag"] = unifier_delete_activities_flag
        if unifier_enabled_flag is not UNSET:
            field_dict["UnifierEnabledFlag"] = unifier_enabled_flag
        if unifier_project_name is not UNSET:
            field_dict["UnifierProjectName"] = unifier_project_name
        if unifier_project_number is not UNSET:
            field_dict["UnifierProjectNumber"] = unifier_project_number
        if unifier_schedule_sheet_name is not UNSET:
            field_dict["UnifierScheduleSheetName"] = unifier_schedule_sheet_name
        if use_expected_finish_dates is not UNSET:
            field_dict["UseExpectedFinishDates"] = use_expected_finish_dates
        if use_project_baseline_for_earned_value is not UNSET:
            field_dict["UseProjectBaselineForEarnedValue"] = use_project_baseline_for_earned_value
        if wbs_code_separator is not UNSET:
            field_dict["WBSCodeSeparator"] = wbs_code_separator
        if wbs_hierarchy_levels is not UNSET:
            field_dict["WBSHierarchyLevels"] = wbs_hierarchy_levels
        if wbs_milestone_percent_complete is not UNSET:
            field_dict["WBSMilestonePercentComplete"] = wbs_milestone_percent_complete
        if wbs_object_id is not UNSET:
            field_dict["WBSObjectId"] = wbs_object_id
        if web_site_root_directory is not UNSET:
            field_dict["WebSiteRootDirectory"] = web_site_root_directory
        if web_site_url is not UNSET:
            field_dict["WebSiteURL"] = web_site_url
        if external is not UNSET:
            field_dict["External"] = external

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("Id")

        name = d.pop("Name")

        parent_eps_object_id = d.pop("ParentEPSObjectId")

        activity_default_activity_type = d.pop("ActivityDefaultActivityType", UNSET)

        activity_default_calendar_name = d.pop("ActivityDefaultCalendarName", UNSET)

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

        allow_negative_actual_units_flag = d.pop("AllowNegativeActualUnitsFlag", UNSET)

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

        calculate_float_based_on_finish_date = d.pop("CalculateFloatBasedOnFinishDate", UNSET)

        _check_out_date = d.pop("CheckOutDate", UNSET)
        check_out_date: datetime.datetime | Unset
        if isinstance(_check_out_date, Unset):
            check_out_date = UNSET
        else:
            check_out_date = isoparse(_check_out_date)

        check_out_status = d.pop("CheckOutStatus", UNSET)

        check_out_user_object_id = d.pop("CheckOutUserObjectId", UNSET)

        compute_total_float_type = d.pop("ComputeTotalFloatType", UNSET)

        contains_summary_data = d.pop("ContainsSummaryData", UNSET)

        contract_management_group_name = d.pop("ContractManagementGroupName", UNSET)

        contract_management_project_name = d.pop("ContractManagementProjectName", UNSET)

        cost_quantity_recalculate_flag = d.pop("CostQuantityRecalculateFlag", UNSET)

        _create_date = d.pop("CreateDate", UNSET)
        create_date: datetime.datetime | Unset
        if isinstance(_create_date, Unset):
            create_date = UNSET
        else:
            create_date = isoparse(_create_date)

        create_user = d.pop("CreateUser", UNSET)

        critical_activity_float_limit = d.pop("CriticalActivityFloatLimit", UNSET)

        critical_activity_float_threshold = d.pop("CriticalActivityFloatThreshold", UNSET)

        critical_activity_path_type = d.pop("CriticalActivityPathType", UNSET)

        critical_float_threshold = d.pop("CriticalFloatThreshold", UNSET)

        current_baseline_project_object_id = d.pop("CurrentBaselineProjectObjectId", UNSET)

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

        earned_value_compute_type = d.pop("EarnedValueComputeType", UNSET)

        earned_value_etc_compute_type = d.pop("EarnedValueETCComputeType", UNSET)

        earned_value_etc_user_value = d.pop("EarnedValueETCUserValue", UNSET)

        earned_value_user_percent = d.pop("EarnedValueUserPercent", UNSET)

        enable_prime_syc_flag = d.pop("EnablePrimeSycFlag", UNSET)

        enable_publication = d.pop("EnablePublication", UNSET)

        enable_summarization = d.pop("EnableSummarization", UNSET)

        etl_interval = d.pop("EtlInterval", UNSET)

        financial_period_template_id = d.pop("FinancialPeriodTemplateId", UNSET)

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

        ignore_other_project_relationships = d.pop("IgnoreOtherProjectRelationships", UNSET)

        independent_etc_labor_units = d.pop("IndependentETCLaborUnits", UNSET)

        independent_etc_total_cost = d.pop("IndependentETCTotalCost", UNSET)

        integrated_type = d.pop("IntegratedType", UNSET)

        is_template = d.pop("IsTemplate", UNSET)

        _last_apply_actuals_date = d.pop("LastApplyActualsDate", UNSET)
        last_apply_actuals_date: datetime.datetime | Unset
        if isinstance(_last_apply_actuals_date, Unset):
            last_apply_actuals_date = UNSET
        else:
            last_apply_actuals_date = isoparse(_last_apply_actuals_date)

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

        _last_update_date = d.pop("LastUpdateDate", UNSET)
        last_update_date: datetime.datetime | Unset
        if isinstance(_last_update_date, Unset):
            last_update_date = UNSET
        else:
            last_update_date = isoparse(_last_update_date)

        last_update_user = d.pop("LastUpdateUser", UNSET)

        latitude = d.pop("Latitude", UNSET)

        level_all_resources = d.pop("LevelAllResources", UNSET)

        level_date_flag = d.pop("LevelDateFlag", UNSET)

        level_float_threshold_count = d.pop("LevelFloatThresholdCount", UNSET)

        level_outer_assign = d.pop("LevelOuterAssign", UNSET)

        level_outer_assign_priority = d.pop("LevelOuterAssignPriority", UNSET)

        level_over_allocation_percent = d.pop("LevelOverAllocationPercent", UNSET)

        level_priority_list = d.pop("LevelPriorityList", UNSET)

        level_resource_list = d.pop("LevelResourceList", UNSET)

        level_within_float = d.pop("LevelWithinFloat", UNSET)

        leveling_priority = d.pop("LevelingPriority", UNSET)

        limit_multiple_float_paths = d.pop("LimitMultipleFloatPaths", UNSET)

        link_actual_to_actual_this_period = d.pop("LinkActualToActualThisPeriod", UNSET)

        link_percent_complete_with_actual = d.pop("LinkPercentCompleteWithActual", UNSET)

        link_planned_and_at_completion_flag = d.pop("LinkPlannedAndAtCompletionFlag", UNSET)

        location_name = d.pop("LocationName", UNSET)

        location_object_id = d.pop("LocationObjectId", UNSET)

        longitude = d.pop("Longitude", UNSET)

        make_open_ended_activities_critical = d.pop("MakeOpenEndedActivitiesCritical", UNSET)

        maximum_multiple_float_paths = d.pop("MaximumMultipleFloatPaths", UNSET)

        multiple_float_paths_enabled = d.pop("MultipleFloatPathsEnabled", UNSET)

        multiple_float_paths_ending_activity_object_id = d.pop("MultipleFloatPathsEndingActivityObjectId", UNSET)

        multiple_float_paths_use_total_float = d.pop("MultipleFloatPathsUseTotalFloat", UNSET)

        _must_finish_by_date = d.pop("MustFinishByDate", UNSET)
        must_finish_by_date: datetime.datetime | Unset
        if isinstance(_must_finish_by_date, Unset):
            must_finish_by_date = UNSET
        else:
            must_finish_by_date = isoparse(_must_finish_by_date)

        net_present_value = d.pop("NetPresentValue", UNSET)

        obs_name = d.pop("OBSName", UNSET)

        obs_object_id = d.pop("OBSObjectId", UNSET)

        object_id = d.pop("ObjectId", UNSET)

        original_budget = d.pop("OriginalBudget", UNSET)

        out_of_sequence_schedule_type = d.pop("OutOfSequenceScheduleType", UNSET)

        overall_project_score = d.pop("OverallProjectScore", UNSET)

        owner_resource_object_id = d.pop("OwnerResourceObjectId", UNSET)

        parent_eps_id = d.pop("ParentEPSId", UNSET)

        parent_eps_name = d.pop("ParentEPSName", UNSET)

        payback_period = d.pop("PaybackPeriod", UNSET)

        performance_percent_complete_by_labor_units = d.pop("PerformancePercentCompleteByLaborUnits", UNSET)

        _planned_start_date = d.pop("PlannedStartDate", UNSET)
        planned_start_date: datetime.datetime | Unset
        if isinstance(_planned_start_date, Unset):
            planned_start_date = UNSET
        else:
            planned_start_date = isoparse(_planned_start_date)

        _post_response_pessimistic_finish = d.pop("PostResponsePessimisticFinish", UNSET)
        post_response_pessimistic_finish: datetime.datetime | Unset
        if isinstance(_post_response_pessimistic_finish, Unset):
            post_response_pessimistic_finish = UNSET
        else:
            post_response_pessimistic_finish = isoparse(_post_response_pessimistic_finish)

        _post_response_pessimistic_start = d.pop("PostResponsePessimisticStart", UNSET)
        post_response_pessimistic_start: datetime.datetime | Unset
        if isinstance(_post_response_pessimistic_start, Unset):
            post_response_pessimistic_start = UNSET
        else:
            post_response_pessimistic_start = isoparse(_post_response_pessimistic_start)

        _pre_response_pessimistic_finish = d.pop("PreResponsePessimisticFinish", UNSET)
        pre_response_pessimistic_finish: datetime.datetime | Unset
        if isinstance(_pre_response_pessimistic_finish, Unset):
            pre_response_pessimistic_finish = UNSET
        else:
            pre_response_pessimistic_finish = isoparse(_pre_response_pessimistic_finish)

        _pre_response_pessimistic_start = d.pop("PreResponsePessimisticStart", UNSET)
        pre_response_pessimistic_start: datetime.datetime | Unset
        if isinstance(_pre_response_pessimistic_start, Unset):
            pre_response_pessimistic_start = UNSET
        else:
            pre_response_pessimistic_start = isoparse(_pre_response_pessimistic_start)

        primary_resources_can_mark_activities_as_completed = d.pop(
            "PrimaryResourcesCanMarkActivitiesAsCompleted", UNSET
        )

        primary_resources_can_update_activity_dates = d.pop("PrimaryResourcesCanUpdateActivityDates", UNSET)

        _project_forecast_start_date = d.pop("ProjectForecastStartDate", UNSET)
        project_forecast_start_date: datetime.datetime | Unset
        if isinstance(_project_forecast_start_date, Unset):
            project_forecast_start_date = UNSET
        else:
            project_forecast_start_date = isoparse(_project_forecast_start_date)

        project_schedule_type = d.pop("ProjectScheduleType", UNSET)

        property_type = d.pop("PropertyType", UNSET)

        proposed_budget = d.pop("ProposedBudget", UNSET)

        publication_priority = d.pop("PublicationPriority", UNSET)

        publish_level = d.pop("PublishLevel", UNSET)

        relationship_lag_calendar = d.pop("RelationshipLagCalendar", UNSET)

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

        resources_can_mark_assignment_as_completed = d.pop("ResourcesCanMarkAssignmentAsCompleted", UNSET)

        resources_can_view_inactive_activities = d.pop("ResourcesCanViewInactiveActivities", UNSET)

        return_on_investment = d.pop("ReturnOnInvestment", UNSET)

        review_type = d.pop("ReviewType", UNSET)

        risk_exposure = d.pop("RiskExposure", UNSET)

        risk_level = d.pop("RiskLevel", UNSET)

        risk_matrix_name = d.pop("RiskMatrixName", UNSET)

        risk_matrix_object_id = d.pop("RiskMatrixObjectId", UNSET)

        risk_score = d.pop("RiskScore", UNSET)

        schedule_wbs_hierarchy_type = d.pop("ScheduleWBSHierarchyType", UNSET)

        _scheduled_finish_date = d.pop("ScheduledFinishDate", UNSET)
        scheduled_finish_date: datetime.datetime | Unset
        if isinstance(_scheduled_finish_date, Unset):
            scheduled_finish_date = UNSET
        else:
            scheduled_finish_date = isoparse(_scheduled_finish_date)

        source_project_object_id = d.pop("SourceProjectObjectId", UNSET)

        _start_date = d.pop("StartDate", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        start_to_start_lag_calculation_type = d.pop("StartToStartLagCalculationType", UNSET)

        status = d.pop("Status", UNSET)

        status_reviewer_name = d.pop("StatusReviewerName", UNSET)

        status_reviewer_object_id = d.pop("StatusReviewerObjectId", UNSET)

        strategic_priority = d.pop("StrategicPriority", UNSET)

        summarize_resources_roles_by_wbs = d.pop("SummarizeResourcesRolesByWBS", UNSET)

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

        summary_level = d.pop("SummaryLevel", UNSET)

        summary_material_cost_percent_complete = d.pop("SummaryMaterialCostPercentComplete", UNSET)

        summary_material_cost_variance = d.pop("SummaryMaterialCostVariance", UNSET)

        summary_non_labor_cost_percent_complete = d.pop("SummaryNonLaborCostPercentComplete", UNSET)

        summary_non_labor_cost_variance = d.pop("SummaryNonLaborCostVariance", UNSET)

        summary_non_labor_units_percent_complete = d.pop("SummaryNonLaborUnitsPercentComplete", UNSET)

        summary_non_labor_units_variance = d.pop("SummaryNonLaborUnitsVariance", UNSET)

        summary_not_started_activity_count = d.pop("SummaryNotStartedActivityCount", UNSET)

        summary_performance_percent_complete_by_cost = d.pop("SummaryPerformancePercentCompleteByCost", UNSET)

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

        sync_wbs_hierarchy_flag = d.pop("SyncWbsHierarchyFlag", UNSET)

        team_member_activity_fields = d.pop("TeamMemberActivityFields", UNSET)

        team_member_add_new_actual_units = d.pop("TeamMemberAddNewActualUnits", UNSET)

        team_member_assignment_option = d.pop("TeamMemberAssignmentOption", UNSET)

        team_member_can_status_other_resources = d.pop("TeamMemberCanStatusOtherResources", UNSET)

        team_member_can_update_notebooks = d.pop("TeamMemberCanUpdateNotebooks", UNSET)

        team_member_display_baseline_dates_flag = d.pop("TeamMemberDisplayBaselineDatesFlag", UNSET)

        team_member_display_planned_units = d.pop("TeamMemberDisplayPlannedUnits", UNSET)

        team_member_display_total_float_flag = d.pop("TeamMemberDisplayTotalFloatFlag", UNSET)

        team_member_display_discussions_flag = d.pop("TeamMemberDisplayDiscussionsFlag", UNSET)

        team_member_include_primary_resources = d.pop("TeamMemberIncludePrimaryResources", UNSET)

        team_member_read_only_activity_fields = d.pop("TeamMemberReadOnlyActivityFields", UNSET)

        team_member_resource_assignment_fields = d.pop("TeamMemberResourceAssignmentFields", UNSET)

        team_member_step_udf_viewable_fields = d.pop("TeamMemberStepUDFViewableFields", UNSET)

        team_member_steps_add_deletable = d.pop("TeamMemberStepsAddDeletable", UNSET)

        team_member_viewable_fields = d.pop("TeamMemberViewableFields", UNSET)

        total_benefit_plan = d.pop("TotalBenefitPlan", UNSET)

        total_benefit_plan_tally = d.pop("TotalBenefitPlanTally", UNSET)

        total_funding = d.pop("TotalFunding", UNSET)

        total_spending_plan = d.pop("TotalSpendingPlan", UNSET)

        total_spending_plan_tally = d.pop("TotalSpendingPlanTally", UNSET)

        unallocated_budget = d.pop("UnallocatedBudget", UNSET)

        undistributed_current_variance = d.pop("UndistributedCurrentVariance", UNSET)

        unifier_cbs_tasks_only_flag = d.pop("UnifierCBSTasksOnlyFlag", UNSET)

        unifier_data_mapping_name = d.pop("UnifierDataMappingName", UNSET)

        unifier_delete_activities_flag = d.pop("UnifierDeleteActivitiesFlag", UNSET)

        unifier_enabled_flag = d.pop("UnifierEnabledFlag", UNSET)

        unifier_project_name = d.pop("UnifierProjectName", UNSET)

        unifier_project_number = d.pop("UnifierProjectNumber", UNSET)

        unifier_schedule_sheet_name = d.pop("UnifierScheduleSheetName", UNSET)

        use_expected_finish_dates = d.pop("UseExpectedFinishDates", UNSET)

        use_project_baseline_for_earned_value = d.pop("UseProjectBaselineForEarnedValue", UNSET)

        wbs_code_separator = d.pop("WBSCodeSeparator", UNSET)

        wbs_hierarchy_levels = d.pop("WBSHierarchyLevels", UNSET)

        wbs_milestone_percent_complete = d.pop("WBSMilestonePercentComplete", UNSET)

        wbs_object_id = d.pop("WBSObjectId", UNSET)

        web_site_root_directory = d.pop("WebSiteRootDirectory", UNSET)

        web_site_url = d.pop("WebSiteURL", UNSET)

        external = d.pop("External", UNSET)

        project = cls(
            id=id,
            name=name,
            parent_eps_object_id=parent_eps_object_id,
            activity_default_activity_type=activity_default_activity_type,
            activity_default_calendar_name=activity_default_calendar_name,
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
            allow_negative_actual_units_flag=allow_negative_actual_units_flag,
            allow_status_review=allow_status_review,
            annual_discount_rate=annual_discount_rate,
            anticipated_finish_date=anticipated_finish_date,
            anticipated_start_date=anticipated_start_date,
            assignment_default_driving_flag=assignment_default_driving_flag,
            assignment_default_rate_type=assignment_default_rate_type,
            calculate_float_based_on_finish_date=calculate_float_based_on_finish_date,
            check_out_date=check_out_date,
            check_out_status=check_out_status,
            check_out_user_object_id=check_out_user_object_id,
            compute_total_float_type=compute_total_float_type,
            contains_summary_data=contains_summary_data,
            contract_management_group_name=contract_management_group_name,
            contract_management_project_name=contract_management_project_name,
            cost_quantity_recalculate_flag=cost_quantity_recalculate_flag,
            create_date=create_date,
            create_user=create_user,
            critical_activity_float_limit=critical_activity_float_limit,
            critical_activity_float_threshold=critical_activity_float_threshold,
            critical_activity_path_type=critical_activity_path_type,
            critical_float_threshold=critical_float_threshold,
            current_baseline_project_object_id=current_baseline_project_object_id,
            current_budget=current_budget,
            current_variance=current_variance,
            data_date=data_date,
            date_added=date_added,
            default_price_time_units=default_price_time_units,
            description=description,
            discount_application_period=discount_application_period,
            distributed_current_budget=distributed_current_budget,
            earned_value_compute_type=earned_value_compute_type,
            earned_value_etc_compute_type=earned_value_etc_compute_type,
            earned_value_etc_user_value=earned_value_etc_user_value,
            earned_value_user_percent=earned_value_user_percent,
            enable_prime_syc_flag=enable_prime_syc_flag,
            enable_publication=enable_publication,
            enable_summarization=enable_summarization,
            etl_interval=etl_interval,
            financial_period_template_id=financial_period_template_id,
            finish_date=finish_date,
            fiscal_year_start_month=fiscal_year_start_month,
            forecast_finish_date=forecast_finish_date,
            forecast_start_date=forecast_start_date,
            guid=guid,
            has_future_bucket_data=has_future_bucket_data,
            history_interval=history_interval,
            history_level=history_level,
            ignore_other_project_relationships=ignore_other_project_relationships,
            independent_etc_labor_units=independent_etc_labor_units,
            independent_etc_total_cost=independent_etc_total_cost,
            integrated_type=integrated_type,
            is_template=is_template,
            last_apply_actuals_date=last_apply_actuals_date,
            last_financial_period_object_id=last_financial_period_object_id,
            last_level_date=last_level_date,
            last_published_on=last_published_on,
            last_schedule_date=last_schedule_date,
            last_summarized_date=last_summarized_date,
            last_update_date=last_update_date,
            last_update_user=last_update_user,
            latitude=latitude,
            level_all_resources=level_all_resources,
            level_date_flag=level_date_flag,
            level_float_threshold_count=level_float_threshold_count,
            level_outer_assign=level_outer_assign,
            level_outer_assign_priority=level_outer_assign_priority,
            level_over_allocation_percent=level_over_allocation_percent,
            level_priority_list=level_priority_list,
            level_resource_list=level_resource_list,
            level_within_float=level_within_float,
            leveling_priority=leveling_priority,
            limit_multiple_float_paths=limit_multiple_float_paths,
            link_actual_to_actual_this_period=link_actual_to_actual_this_period,
            link_percent_complete_with_actual=link_percent_complete_with_actual,
            link_planned_and_at_completion_flag=link_planned_and_at_completion_flag,
            location_name=location_name,
            location_object_id=location_object_id,
            longitude=longitude,
            make_open_ended_activities_critical=make_open_ended_activities_critical,
            maximum_multiple_float_paths=maximum_multiple_float_paths,
            multiple_float_paths_enabled=multiple_float_paths_enabled,
            multiple_float_paths_ending_activity_object_id=multiple_float_paths_ending_activity_object_id,
            multiple_float_paths_use_total_float=multiple_float_paths_use_total_float,
            must_finish_by_date=must_finish_by_date,
            net_present_value=net_present_value,
            obs_name=obs_name,
            obs_object_id=obs_object_id,
            object_id=object_id,
            original_budget=original_budget,
            out_of_sequence_schedule_type=out_of_sequence_schedule_type,
            overall_project_score=overall_project_score,
            owner_resource_object_id=owner_resource_object_id,
            parent_eps_id=parent_eps_id,
            parent_eps_name=parent_eps_name,
            payback_period=payback_period,
            performance_percent_complete_by_labor_units=performance_percent_complete_by_labor_units,
            planned_start_date=planned_start_date,
            post_response_pessimistic_finish=post_response_pessimistic_finish,
            post_response_pessimistic_start=post_response_pessimistic_start,
            pre_response_pessimistic_finish=pre_response_pessimistic_finish,
            pre_response_pessimistic_start=pre_response_pessimistic_start,
            primary_resources_can_mark_activities_as_completed=primary_resources_can_mark_activities_as_completed,
            primary_resources_can_update_activity_dates=primary_resources_can_update_activity_dates,
            project_forecast_start_date=project_forecast_start_date,
            project_schedule_type=project_schedule_type,
            property_type=property_type,
            proposed_budget=proposed_budget,
            publication_priority=publication_priority,
            publish_level=publish_level,
            relationship_lag_calendar=relationship_lag_calendar,
            reset_planned_to_remaining_flag=reset_planned_to_remaining_flag,
            resource_can_be_assigned_to_same_activity_more_than_once=resource_can_be_assigned_to_same_activity_more_than_once,
            resource_name=resource_name,
            resources_can_assign_themselves_to_activities=resources_can_assign_themselves_to_activities,
            resources_can_assign_themselves_to_activities_outside_obs_access=resources_can_assign_themselves_to_activities_outside_obs_access,
            resources_can_edit_assignment_percent_complete=resources_can_edit_assignment_percent_complete,
            resources_can_mark_assignment_as_completed=resources_can_mark_assignment_as_completed,
            resources_can_view_inactive_activities=resources_can_view_inactive_activities,
            return_on_investment=return_on_investment,
            review_type=review_type,
            risk_exposure=risk_exposure,
            risk_level=risk_level,
            risk_matrix_name=risk_matrix_name,
            risk_matrix_object_id=risk_matrix_object_id,
            risk_score=risk_score,
            schedule_wbs_hierarchy_type=schedule_wbs_hierarchy_type,
            scheduled_finish_date=scheduled_finish_date,
            source_project_object_id=source_project_object_id,
            start_date=start_date,
            start_to_start_lag_calculation_type=start_to_start_lag_calculation_type,
            status=status,
            status_reviewer_name=status_reviewer_name,
            status_reviewer_object_id=status_reviewer_object_id,
            strategic_priority=strategic_priority,
            summarize_resources_roles_by_wbs=summarize_resources_roles_by_wbs,
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
            summary_level=summary_level,
            summary_material_cost_percent_complete=summary_material_cost_percent_complete,
            summary_material_cost_variance=summary_material_cost_variance,
            summary_non_labor_cost_percent_complete=summary_non_labor_cost_percent_complete,
            summary_non_labor_cost_variance=summary_non_labor_cost_variance,
            summary_non_labor_units_percent_complete=summary_non_labor_units_percent_complete,
            summary_non_labor_units_variance=summary_non_labor_units_variance,
            summary_not_started_activity_count=summary_not_started_activity_count,
            summary_performance_percent_complete_by_cost=summary_performance_percent_complete_by_cost,
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
            sync_wbs_hierarchy_flag=sync_wbs_hierarchy_flag,
            team_member_activity_fields=team_member_activity_fields,
            team_member_add_new_actual_units=team_member_add_new_actual_units,
            team_member_assignment_option=team_member_assignment_option,
            team_member_can_status_other_resources=team_member_can_status_other_resources,
            team_member_can_update_notebooks=team_member_can_update_notebooks,
            team_member_display_baseline_dates_flag=team_member_display_baseline_dates_flag,
            team_member_display_planned_units=team_member_display_planned_units,
            team_member_display_total_float_flag=team_member_display_total_float_flag,
            team_member_display_discussions_flag=team_member_display_discussions_flag,
            team_member_include_primary_resources=team_member_include_primary_resources,
            team_member_read_only_activity_fields=team_member_read_only_activity_fields,
            team_member_resource_assignment_fields=team_member_resource_assignment_fields,
            team_member_step_udf_viewable_fields=team_member_step_udf_viewable_fields,
            team_member_steps_add_deletable=team_member_steps_add_deletable,
            team_member_viewable_fields=team_member_viewable_fields,
            total_benefit_plan=total_benefit_plan,
            total_benefit_plan_tally=total_benefit_plan_tally,
            total_funding=total_funding,
            total_spending_plan=total_spending_plan,
            total_spending_plan_tally=total_spending_plan_tally,
            unallocated_budget=unallocated_budget,
            undistributed_current_variance=undistributed_current_variance,
            unifier_cbs_tasks_only_flag=unifier_cbs_tasks_only_flag,
            unifier_data_mapping_name=unifier_data_mapping_name,
            unifier_delete_activities_flag=unifier_delete_activities_flag,
            unifier_enabled_flag=unifier_enabled_flag,
            unifier_project_name=unifier_project_name,
            unifier_project_number=unifier_project_number,
            unifier_schedule_sheet_name=unifier_schedule_sheet_name,
            use_expected_finish_dates=use_expected_finish_dates,
            use_project_baseline_for_earned_value=use_project_baseline_for_earned_value,
            wbs_code_separator=wbs_code_separator,
            wbs_hierarchy_levels=wbs_hierarchy_levels,
            wbs_milestone_percent_complete=wbs_milestone_percent_complete,
            wbs_object_id=wbs_object_id,
            web_site_root_directory=web_site_root_directory,
            web_site_url=web_site_url,
            external=external,
        )

        project.additional_properties = d
        return project

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
