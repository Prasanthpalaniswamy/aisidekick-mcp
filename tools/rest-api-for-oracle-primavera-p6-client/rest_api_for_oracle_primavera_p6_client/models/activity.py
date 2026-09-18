from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Activity")


@_attrs_define
class Activity:
    """Activity Entity

    Attributes:
        project_object_id (int): The unique ID of the associated project.
        wbs_object_id (int): The unique ID of the WBS for the activity.
        accounting_variance (float | Unset): The difference between the planned value of work scheduled and the actual
            cost of work performed. Computed as accounting variance = planned value - actual cost . A negative value
            indicates that actual costs have exceeded the scheduled costs.
        accounting_variance_labor_units (float | Unset): The difference between the planned value of work scheduled and
            the actual work performed. Computed as accounting variance labor units = planned value labor units - actual
            units. A negative value indicates that actual costs have exceeded the scheduled costs.
        activity_owner_user_id (int | Unset): The unique user ID of the activity owner.
        actual_duration (float | Unset): The total working time from the activity actual start date to the actual finish
            date (for completed activities), or to the current data date (for in-progress activities). The actual working
            time is computed using the activity's calendar.
        actual_expense_cost (float | Unset): The actual costs for all project expenses associated with the activity.
        actual_finish_date (datetime.datetime | Unset): The date on which the activity is actually finished.
        actual_labor_cost (float | Unset): The actual costs for all labor resources assigned to the activity. If no
            resources are assigned, computed as the activity actual labor units * project default price / time.
        actual_labor_units (float | Unset): The actual units for all labor resources assigned to the activity.
        actual_material_cost (float | Unset): The sum of all regular and overtime costs for material resources.
        actual_non_labor_cost (float | Unset): The actual costs for all nonlabor resources assigned to the activity. If
            no resources are assigned, computed as the activity actual nonlabor units * project default price / time.
        actual_non_labor_units (float | Unset): The actual units for all nonlabor resources assigned to the activity.
        actual_start_date (datetime.datetime | Unset): The date on which the activity is actually started.
        actual_this_period_labor_cost (float | Unset): The actual this period labor cost for all labor resources
            assigned to the activity.
        actual_this_period_labor_units (float | Unset): The actual this period labor units (hours) for all labor
            resources assigned to the activity.
        actual_this_period_material_cost (float | Unset): The sum of all material resource costs for the current period.
        actual_this_period_non_labor_cost (float | Unset): The actual this period nonlabor cost for all nonlabor
            resources assigned to the activity. If no resources are assigned, computed as the activity actual nonlabor units
            * project default price / time.
        actual_this_period_non_labor_units (float | Unset): The actual this period nonlabor units (hours) for all
            nonlabor resources assigned to the activity.
        actual_total_cost (float | Unset): The actual total cost for the activity, including labor resources, nonlabor
            resources, and project expenses. Actual total cost = actual labor costs + actual nonlabor costs + actual expense
            costs.
        actual_total_units (float | Unset): The sum of Actual Labor Units and Actual Nonlabor Units.
        at_completion_duration (float | Unset): The total working time from the activity's current start date to the
            current finish date. The current start date is the planned start date until the activity is started, then it is
            the actual start date. The current finish date is the activity planned finish date while the activity is not
            started, the remaining finish date while the activity is in progress, and the actual finish date once the
            activity is completed. The total working time is computed using the activity's calendar.
        at_completion_expense_cost (float | Unset): The total working time from the activity's current start date to the
            current finish date. The current start date is the planned start date until the activity is started, then it is
            the actual start date. The current finish date is the activity planned finish date while the activity is not
            started, the remaining finish date while the activity is in progress, and the actual finish date once the
            activity is completed. The total working time is computed using the activity's calendar.
        at_completion_labor_cost (float | Unset): The sum of the actual plus remaining costs for all labor resources
            assigned to the activity. Computed as actual labor cost + remaining labor cost. Same as the planned labor costs
            if the activity is not started and the actual labor costs once the activity is completed.
        at_completion_labor_units (float | Unset): The sum of the actual plus remaining units for all labor resources
            assigned to the activity. Computed as actual labor units + remaining labor units. Same as the planned labor
            units if the activity is not started and the actual labor units once the activity is completed.
        at_completion_labor_units_variance (float | Unset): The project baseline planned total labor units minus the
            estimate at completion labor units.
        at_completion_material_cost (float | Unset): The project baseline planned total labor units minus the estimate
            at completion labor units.
        at_completion_non_labor_cost (float | Unset): The sum of the actual plus remaining costs for all nonlabor
            resources assigned to the activity. Computed as actual nonlabor cost + remaining nonlabor cost. Same as the
            planned nonlabor costs if the activity is not started and the actual nonlabor costs once the activity is
            completed.
        at_completion_non_labor_units (float | Unset): The sum of the actual plus remaining units for all nonlabor
            resources assigned to the activity. Computed as actual nonlabor units + remaining nonlabor units. Same as the
            planned nonlabor units if the activity is not started and the actual nonlabor units once the activity is
            completed.
        at_completion_total_cost (float | Unset): The total cost at completion for the activity, including labor
            resources, nonlabor resources, and project expenses. At completion total cost = at completion labor cost + at
            completion nonlabor cost + at completion expense cost.
        at_completion_total_units (float | Unset): The sum of the actual plus remaining units for the resource
            assignment on the activity.
        at_completion_variance (float | Unset): The difference between the project baseline total cost and the current
            estimate of total cost. Computed as VAC = BAC - EAC. A negative value indicates an estimated cost overrun. BAC
            is computed from the current project baseline.
        auto_compute_actuals (bool | Unset): The option that determines whether the activity's actual and remaining
            units, start date, finish date, and percent complete are computed automatically using the planned dates, planned
            units and the schedule percent complete. If this option is selected, the actual/remaining units and actual dates
            are automatically updated when project actuals are applied. Use this option to assume that all work for the
            activity proceeds according to plan.
        baseline_1_duration (float | Unset): The duration for the activity in the primary baseline. The duration is the
            total working time from the activity current start date to the current finish date. Same as the actual duration
            plus the remaining duration. The total working time is computed using the activity's calendar.
        baseline_1_finish_date (datetime.datetime | Unset): The current finish date of the activity in the primary
            baseline. Set to the activity planned finish date while the activity is not started, the remaining finish date
            while the activity is in progress, and the actual finish date once the activity is completed.
        baseline_1_planned_duration (float | Unset): The planned duration for the activity in the primary baseline.
            Planned duration is the total working time from the activity current start date to the current finish date. Same
            as the actual duration plus the remaining duration. The total working time is computed using the activity's
            calendar. This field is named Baseline 1 Budgeted Duration in Primavera's Engineering & Construction and
            Maintenance & Turnaround solutions.
        baseline_1_planned_expense_cost (float | Unset): The planned costs for all project expenses associated with the
            activity. This field is named Baseline 1 Budgeted Expense Cost in Primavera's Engineering & Construction and
            Maintenance & Turnaround solutions.
        baseline_1_planned_labor_cost (float | Unset): The cost at completion for all labor resources assigned to the
            activity in the primary baseline. Computed from the primary baseline at completion labor units. If no resources
            are assigned, computed as the activity BL labor units * project default price / time. This field is named
            Baseline 1 Budgeted Labor Cost in Primavera's Engineering & Construction and Maintenance & Turnaround solutions.
        baseline_1_planned_labor_units (float | Unset): The planned units for all labor resources assigned to the
            activity. This field is named Baseline 1 Budgeted Labor Units in Primavera's Engineering & Construction and
            Maintenance & Turnaround solutions.
        baseline_1_planned_material_cost (float | Unset): The Planned Material Cost for a primary baseline activity.
        baseline_1_planned_non_labor_cost (float | Unset): The planned costs for all nonlabor resources assigned to the
            activity. If no resources are assigned, computed as the activity planned nonlabor units * project default price
            / time. This field is named Baseline 1 Budgeted Non Labor Cost in Primavera's Engineering & Construction and
            Maintenance & Turnaround solutions.
        baseline_1_planned_non_labor_units (float | Unset): The planned units for all nonlabor resources assigned to the
            activity. This field is named Baseline 1 Budgeted Non Labor Units in Primavera's Engineering & Construction and
            Maintenance & Turnaround solutions.
        baseline_1_planned_total_cost (float | Unset): The planned total cost for the activity, including labor
            resources, nonlabor resources, and project expenses. Planned total cost = planned labor cost + planned nonlabor
            cost + planned expense cost. This field is named Baseline 1 Budgeted Total Cost in Primavera's Engineering &
            Construction and Maintenance & Turnaround solutions.
        baseline_1_start_date (datetime.datetime | Unset): The current start date of the activity in the primary
            baseline. Set to the planned start date until the activity is started, then set to the actual start date.
        baseline_duration (float | Unset): The duration for the activity in the project baseline. The duration is the
            total working time from the activity current start date to the current finish date. Same as the actual duration
            plus the remaining duration. The total working time is computed using the activity's calendar.
        baseline_finish_date (datetime.datetime | Unset): The current finish date of the activity in the project
            baseline. Set to the activity planned finish date while the activity is not started, the remaining finish date
            while the activity is in progress, and the actual finish date once the activity is completed.
        baseline_planned_duration (float | Unset): The planned duration for the activity in the project baseline.
            Planned duration is the total working time from the activity current start date to the current finish date. Same
            as the actual duration plus the remaining duration. The total working time is computed using the activity's
            calendar. This field is named Baseline Budgeted Duration in Primavera's Engineering & Construction and
            Maintenance & Turnaround solutions.
        baseline_planned_expense_cost (float | Unset): The planned costs for all project expenses associated with the
            activity. This field is named Baseline Budgeted Expense Cost in Primavera's Engineering & Construction and
            Maintenance & Turnaround solutions.
        baseline_planned_labor_cost (float | Unset): The cost at completion for all labor resources assigned to the
            activity in the project baseline. Computed from the baseline at completion labor units. If no resources are
            assigned, computed as the activity BL labor units * project default price / time. This field is named Baseline
            Budgeted Labor Cost in Primavera's Engineering & Construction and Maintenance & Turnaround solutions.
        baseline_planned_labor_units (float | Unset): The planned units for all labor resources assigned to the
            activity. This field is named Baseline Budgeted Labor Units in Primavera's Engineering & Construction and
            Maintenance & Turnaround solutions.
        baseline_planned_material_cost (float | Unset): The Planned Material Cost for a project baseline activity.
        baseline_planned_non_labor_cost (float | Unset): The planned costs for all nonlabor resources assigned to the
            activity. If no resources are assigned, computed as the activity planned nonlabor units * project default price
            / time. This field is named Baseline Budgeted Non Labor Cost in Primavera's Engineering & Construction and
            Maintenance & Turnaround solutions.
        baseline_planned_non_labor_units (float | Unset): The planned units for all nonlabor resources assigned to the
            activity. This field is named Baseline Budgeted Non Labor Units in Primavera's Engineering & Construction and
            Maintenance & Turnaround solutions.
        baseline_planned_total_cost (float | Unset): The planned total cost for the activity, including labor resources,
            nonlabor resources, and project expenses. Planned total cost = planned labor cost + planned nonlabor cost +
            planned expense cost. This field is named Baseline Budgeted Total Cost in Primavera's Engineering & Construction
            and Maintenance & Turnaround solutions.
        baseline_start_date (datetime.datetime | Unset): The current start date of the activity in the project baseline.
            Set to the planned start date until the activity is started, then set to the actual start date.
        budget_at_completion (float | Unset): The planned total cost through activity completion. Computed as planned
            labor cost + planned nonlabor cost + planned expense cost, same as the planned total cost.
        cbs_code (str | Unset): The unique name of the Unifier CBS Code. Assign CBS codes to activities so that you can
            filter which activities you will send to Unifier.
        cbs_id (int | Unset): The unique Id of CBS Code.
        cbs_object_id (int | Unset): The identifier of the CoUnifier CBS.
        calendar_name (str | Unset): The name of the calendar.
        calendar_object_id (int | Unset): The unique ID of the calendar assigned to the activity. Activity calendars can
            be assigned from the global calendar pool or the project calendar pool.
        cost_percent_complete (float | Unset): The percent complete of costs for all labor resources, nonlabor
            resources, and expenses for the activity. Computed as actual total cost / at completion total cost * 100. Always
            in the range 0 to 100.
        cost_percent_of_planned (float | Unset): The percent complete of planned costs for all labor resources, nonlabor
            resources, and expenses for the activity. Computed as actual total cost / BL planned total cost * 100. The value
            can exceed 100.
        cost_performance_index (float | Unset): The earned value divided by the actual cost. A value less than 1
            indicates that actual cost have exceeded the planned value.
        cost_performance_index_labor_units (float | Unset): The ratio of the earned value labor units and the actual
            work performed. Computed as CPI labor units = earned value labor units / actual labor units .
        cost_variance (float | Unset): The difference between the earned value and the actual cost of work performed.
            Computed as CV = earned value - actual costs. A negative value indicates that actual costs have exceeded the
            value of work performed.
        cost_variance_index (float | Unset): The ratio of the cost variance and the earned value of work performed.
            Computed as CVI = cost variance / earned value.
        cost_variance_index_labor_units (float | Unset): The ratio of the cost variance labor units and the earned value
            of work performed. Computed as CVI labor units = CV labor units / earned value labor units
        cost_variance_labor_units (float | Unset): The difference between the earned value of labor units and the actual
            cost of labor units. Calculated as CV labor units = earned value planned units - actual units. A negative value
            indicates that actual costs have exceeded the value of work performed.
        create_date (datetime.datetime | Unset): The date this activity was created.
        create_user (str | Unset): The name of the user that created this activity.
        data_date (datetime.datetime | Unset): The current data date for the project. The project status is up to date
            as of the data date. The data date is modified when project actuals are applied.
        duration_1_variance (float | Unset): The duration between the activity's primary baseline duration and the at
            complete duration. Computed as primary baseline duration - at completion duration.
        duration_percent_complete (float | Unset): The percent complete of the activity duration. Computed as (planned
            duration - remaining duration) / planned duration * 100. Always in the range 0 to 100. The planned duration is
            taken from the current plan, not from the baseline.
        duration_percent_of_planned (float | Unset): The activity actual duration percent of planned. Computed as actual
            duration / BL duration * 100. The value can exceed 100. The BL duration is the activity's at completion duration
            from the project baseline.
        duration_type (str | Unset): The duration type of the activity. One of 'Fixed Units/Time', 'Fixed Duration and
            Units/Time', 'Fixed Units', or 'Fixed Duration and Units'. For 'Fixed Units/Time' activities, the resource units
            per time are constant when the activity duration or units are changed. This type is used when an activity has
            fixed resources with fixed productivity output per time period. For 'Fixed Duration and Units/Time' activities,
            the activity duration is constant as the units or resource units per time are changed. This type is used when
            the activity is to be completed within a fixed time period regardless of the resources assigned. For 'Fixed
            Units' activities, the activity units are constant when the duration or resource units per time are changed.
            This type is used when the total amount of work is fixed, and increasing the resources can decrease the activity
            duration.
        duration_variance (float | Unset): The duration between the activity's project baseline duration and the at
            complete duration. Computed as project baseline duration - at completion duration.
        early_finish_date (datetime.datetime | Unset): The earliest possible date the activity can finish. This date is
            computed by the project scheduler based on network logic, schedule constraints, and resource availability.
        early_start_date (datetime.datetime | Unset): The earliest possible date the remaining work for the activity can
            begin. This date is computed by the project scheduler based on network logic, schedule constraints, and resource
            availability.
        earned_value_cost (float | Unset): The portion of the project baseline total cost of the activity that is
            actually completed as of the project data date. Computed as earned value = BAC * performance % complete. The
            method for computing performance % complete depends on the earned-value technique selected for the activity's
            WBS. BAC is computed from the project baseline.
        earned_value_labor_units (float | Unset): The portion of the project baseline labor units that is actually
            completed as of the project data date. Computed as labor units earned value = project baseline labor units *
            performance % complete. The method for computing performance % complete depends on the earned-value technique
            selected for the activity's WBS. The BL labor units is taken from the project baseline.
        estimate_at_completion_cost (float | Unset): The estimated cost at completion for the activity. Computed as the
            actual total cost plus the estimate-to-complete cost; EAC = ACWP + ETC. Note that the method for computing ETC
            depends on the earned-value technique selected for the activity's WBS.
        estimate_at_completion_labor_units (float | Unset): The estimated labor units at completion of the activity.
            Calculated as actual labor units + estimate to complete labor units. estimate to complete labor units is
            calculated based off of the earned value setting on the WBS.
        estimate_to_complete (float | Unset): The estimated cost to complete the activity. Computed as either the
            remaining total cost for the activity (remaining total cost), or as PF * (BAC - earned value), depending on the
            earned-value technique selected for the activity's WBS. BAC is computed from the project baseline.
        estimate_to_complete_labor_units (float | Unset): The estimated quantity to complete the activity. Computed as
            either the remaining total units for the activity (remaining total units), or as PF * (BL labor units - earned
            value), depending on the earned-value technique selected for the activity's WBS.
        estimated_weight (float | Unset):
        expected_finish_date (datetime.datetime | Unset): The date the activity is expected to be finished according to
            the progress made on the activity's work products. The expected finish date is entered manually by people
            familiar with progress of the activity's work products.
        expense_cost_1_variance (float | Unset): The difference between primary baseline expense cost and at completion
            expense cost. Calculated as primary baseline expense cost - at completion expense cost (at completion expense
            cost = actual expense cost + remaining expense cost).
        expense_cost_percent_complete (float | Unset): The percent complete of costs for all expenses associated with
            the activity. Computed as actual expense cost / at completion expense cost * 100. Always in the range 0 to 100.
        expense_cost_variance (float | Unset): The difference between project baseline expense cost and at completion
            expense cost. Calculated as project baseline expense cost - at completion expense cost (at completion expense
            cost = actual expense cost + remaining expense cost).
        external_early_start_date (datetime.datetime | Unset): The date value that determines the early start date for
            imported activities with external constraints lost (relations from/to external projects that do not exist in the
            database). This field is the relationship early finish date (REF) when the lost relationship type is FS or SS.
            When the relationship type is SF or FF, this field is calculated as REF - RD of the successor.
        external_late_finish_date (datetime.datetime | Unset): The date value that determines the Late Finish Date for
            imported activities with external constraints lost (from/to external projects that do not exist in the
            database). This field is the relationship late finish date (RLF) when the lost relationship type is FS or FF.
            When the relationship type is SS or SF, this field is calculated as RLS + RD of the predecessor.
        feedback (str | Unset): The feedback from the resource.
        financial_period_tmpl_id (int | Unset):
        finish_date (datetime.datetime | Unset): The current finish date of the activity. Set to the activity planned
            finish date while the activity is not started, the remaining finish date while the activity is in progress, and
            the actual finish date once the activity is completed.
        finish_date_1_variance (float | Unset): The duration between the finish date in the current project and the
            primary baseline finish date. Calculated as finish date - primary baseline finish date.
        finish_date_variance (float | Unset): The duration between the finish date in the current project and the
            project baseline finish date. Calculated as finish date - project baseline finish date.
        float_path (int | Unset): The integer representing the critical path this activity is on. The value 1 is the
            most critical path, value 2 is the second most critical path, etc.
        float_path_order (int | Unset): The integer representing the order in which this object was found on one of the
            critical paths.
        free_float (float | Unset): The amount of time the activity can be delayed before delaying the start date of any
            successor activity.
        guid (str | Unset): The globally unique ID generated by the system.
        has_future_bucket_data (bool | Unset): The flag that indicates whether a resource assignment on the activity has
            future bucket data.
        id (str | Unset): The short ID that uniquely identifies the activity within the project.
        is_baseline (bool | Unset): The boolean value indicating if this business object is related to a Project or
            Baseline
        is_critical (bool | Unset): The flag that indicates whether the activity is critical. An activity is critical
            when its total Float is below the critical duration specified for the project. Delaying critical activities will
            delay the finish date of the project.
        is_longest_path (bool | Unset): The flag that indicates whether an activity is on the longest path. Default =
            'N'
        is_new_feedback (bool | Unset): The flag that indicates that a resource has sent feedback notes about this
            activity which have not been reviewed yet.
        is_starred (bool | Unset): The boolean value indicating if this business object has been assigned a star in P6
            Team Member
        is_template (bool | Unset): The boolean value indicating if this business object is related to a template
            Project.
        is_work_package (bool | Unset): Indicates if this WBS is a workpackage in Prime or not.
        labor_cost_1_variance (float | Unset): The difference between primary baseline labor cost and at completion
            labor cost. Calculated as BL labor cost - at completion labor cost
        labor_cost_percent_complete (float | Unset): The percent complete of costs for all labor resources assigned to
            the activity. Computed as actual labor cost / at completion labor cost * 100. Always in the range 0 to 100.
        labor_cost_variance (float | Unset): The difference between project baseline labor cost and at completion labor
            cost. Calculated as BL labor cost - at completion labor cost
        labor_units_1_variance (float | Unset): The difference between primary baseline labor units and at completion
            labor units. Calculated as BL labor units - at completion labor units.
        labor_units_percent_complete (float | Unset): The percent complete of units for all labor resources for the
            activity. Computed as actual labor units / at completion labor units * 100. Always in the range 0 to 100.
        labor_units_variance (float | Unset): The difference between project baseline labor units and at completion
            labor units. Calculated as BL labor units - at completion labor units.
        last_update_date (datetime.datetime | Unset): The date this activity was last updated.
        last_update_user (str | Unset): The name of the user that last updated this activity.
        late_finish_date (datetime.datetime | Unset): The latest possible date the activity must finish without delaying
            the project finish date. This date is computed by the project scheduler based on network logic, schedule
            constraints, and resource availability.
        late_start_date (datetime.datetime | Unset): The latest possible date the remaining work for the activity must
            begin without delaying the project finish date. This date is computed by the project scheduler based on network
            logic, schedule constraints, and resource availability.
        leveling_priority (str | Unset): The activity priority used to prioritize activities in a project when
            performing resource leveling. Valid values are 'Top', 'High', 'Normal', 'Low', and 'Lowest'.
        location_name (str | Unset): The name of the location assigned to the activity.
        location_object_id (int | Unset): The unique ID of the location assigned to the activity.
        material_cost_1_variance (float | Unset): The primary Baseline Planned Material Cost minus the At Completion
            Material Cost.
        material_cost_percent_complete (float | Unset): The percent complete of costs for all material resources
            assigned to the activity. Computed as actual nonlabor cost / at completion nonlabor cost * 100. Always in the
            range 0 to 100.
        material_cost_variance (float | Unset): The project BaselinePlannedMaterialCost minus the
            AtCompletionMaterialCost.
        maximum_duration (float | Unset): The maximum duration of the activity.
        minimum_duration (float | Unset): The minimum duration of the activity.
        most_likely_duration (float | Unset): The most likely duration of the activity.
        name (str | Unset): The name of the activity. The activity name does not have to be unique.
        non_labor_cost_1_variance (float | Unset): The difference between the primary baseline nonlabor cost and at
            completion nonlabor cost. Calculated as BL nonlabor cost - at completion nonlabor cost.
        non_labor_cost_percent_complete (float | Unset): The percent complete of costs for all nonlabor resources
            assigned to the activity. Computed as actual nonlabor cost / at completion nonlabor cost * 100. Always in the
            range 0 to 100.
        non_labor_cost_variance (float | Unset): The difference between the project baseline labor cost and at
            completion labor cost. Calculated as BL nonlabor cost - at completion nonlabor cost.
        non_labor_units_1_variance (float | Unset): The difference between the primary baseline nonlabor units and at
            completion nonlabor units. Calculated as BL nonlabor units - at completion nonlabor units.
        non_labor_units_percent_complete (float | Unset): The percent complete of units for all nonlabor resources for
            the activity. Computed as actual nonlabor units / at completion nonlabor units * 100. Always in the range 0 to
            100.
        non_labor_units_variance (float | Unset): The difference between the project baseline labor units and at
            completion labor units. Calculated as BL nonlabor units - at completion nonlabor units.
        notes_to_resources (str | Unset): The notes from the project manager to the timesheet resources.
        object_id (int | Unset): The unique ID generated by the system.
        owner_id_array (str | Unset): A comma separated list of activity owner IDs.
        owner_names_array (str | Unset): A comma separated list of activity owner names.
        percent_complete (float | Unset): The activity percent complete. This value is tied to the activity duration %
            complete, units % complete, or physical % complete, depending on the setting for the activity's percent complete
            type, which is one of Duration, Units, or Physical. Always in the range 0 to 100.
        percent_complete_type (str | Unset): The activity percent complete type: 'Physical', 'Duration', or 'Units'.
        performance_percent_complete (float | Unset): The activity performance percent complete. The performance percent
            complete is used to compute earned value and may be based on the activity % complete, on the 0/100 rule, on the
            50/50 rule, etc., depending on the technique for computing earned-value percent complete for the activity's WBS.
            The performance % complete specifies what percentage of the activity's planned worth has been earned so far.
        performance_percent_complete_by_labor_units (float | Unset):
        physical_percent_complete (float | Unset): The physical percent complete, which can either be user entered or
            calculated from the activity's weighted steps.
        planned_duration (float | Unset): The total working time from the activity planned start date to the planned
            finish date. The planned working time is computed using the activity's calendar. This field is named
            OriginalDuration in Primavera's Engineering & Construction and Maintenance & Turnaround solutions.
        planned_expense_cost (float | Unset): The planned costs for all project expenses associated with the activity.
            This field is named BudgetedExpenseCost in Primavera's Engineering & Construction and Maintenance & Turnaround
            solutions.
        planned_finish_date (datetime.datetime | Unset): The date the activity is scheduled to finish. This date is
            computed by the project scheduler but can be updated manually by the project manager. This date is not changed
            by the project scheduler after the activity has been started.
        planned_labor_cost (float | Unset): The planned costs for all labor resources assigned to the activity. If no
            resources are assigned, computed as the activity planned labor units * project default price / time. This field
            is named BudgetedLaborCost in Primavera's Engineering & Construction and Maintenance & Turnaround solutions.
        planned_labor_units (float | Unset): The planned units for all labor resources assigned to the activity. This
            field is named BudgetedLaborUnits in Primavera's Engineering & Construction and Maintenance & Turnaround
            solutions.
        planned_material_cost (float | Unset): The sum of all material resource costs.
        planned_non_labor_cost (float | Unset): The planned costs for all nonlabor resources assigned to the activity.
            If no resources are assigned, computed as the activity planned nonlabor units * project default price / time.
            This field is named BudgetedNonLaborCost in Primavera's Engineering & Construction and Maintenance & Turnaround
            solutions.
        planned_non_labor_units (float | Unset): The planned units for all nonlabor resources assigned to the activity.
            This field is named BudgetedNonLaborUnits in Primavera's Engineering & Construction and Maintenance & Turnaround
            solutions.
        planned_start_date (datetime.datetime | Unset): The date the activity is scheduled to begin. This date is
            computed by the project scheduler but can be updated manually by the project manager. This date is not changed
            by the project scheduler after the activity has been started.
        planned_total_cost (float | Unset): The planned total cost for the activity, including labor resources, nonlabor
            resources, and project expenses. Planned total cost = planned labor cost + planned nonlabor cost + planned
            material cost + planned expense cost. This field is named BudgetedTotalCost in Primavera's Engineering &
            Construction and Maintenance & Turnaround solutions.
        planned_total_units (float | Unset): The sum of Planned Labor Units and Planned Nonlabor Units. This field is
            named BudgetedTotalUnits in Primavera's Engineering & Construction and Maintenance & Turnaround solutions.
        planned_value_cost (float | Unset): The portion of the project baseline total cost of the activity that is
            scheduled to be completed as of the project data date. Computed as BAC * schedule % complete. Also known as the
            work scheduled to be performed for the activity. The schedule % complete specifies how much of the activity's
            project baseline duration has been completed so far. BAC is computed from the project baseline.
        planned_value_labor_units (float | Unset): The portion of the project baseline labor units that is scheduled to
            be completed as of the project data date. Computed as BL labor units * schedule % complete. The schedule %
            complete specifies how much of the activity's project baseline duration has been completed so far. BL labor
            units is taken from the project baseline.
        post_resp_criticality_index (float | Unset):
        post_response_pessimistic_finish (datetime.datetime | Unset): The Post Response Pessimistic Finish date
            calculated by Oracle Prime during quantitative risk analysis.
        post_response_pessimistic_start (datetime.datetime | Unset): The Post Response Pessimistic Start date calculated
            by Oracle Prime during quantitative risk analysis.
        pre_resp_criticality_index (float | Unset):
        pre_response_pessimistic_finish (datetime.datetime | Unset): The Pre Response Pessimistic Finish date calculated
            by Oracle Prime during quantitative risk analysis.
        pre_response_pessimistic_start (datetime.datetime | Unset): The Pre Response Pessimistic Start date calculated
            by Oracle Prime during quantitative risk analysis.
        primary_constraint_date (datetime.datetime | Unset): The constraint date for the activity, if the activity has a
            constraint. The activity's constraint type determines whether this is a start date or finish date. Activity
            constraints are used by the project scheduler.
        primary_constraint_type (str | Unset): The type of constraint applied to the activity start or finish date.
            Activity constraints are used by the project scheduler. Start date constraints are 'Start On', 'Start On or
            Before', and 'Start On or After'. Finish date constraints are 'Finish On', 'Finish On or Before', and 'Finish On
            or After'. Another type of constraint, 'As Late As Possible', schedules the activity as late as possible based
            on the available free float.
        primary_resource_id (str | Unset): The name of the resource.
        primary_resource_name (str | Unset): The name of the resource.
        primary_resource_object_id (int | Unset): The unique ID of the primary resource for the activity. The primary
            resource is responsible for the overall work on the activity and updates the activity status using Timesheets.
        project_flag (str | Unset): Indicates if this WBS node is a Project/EPS node.
        project_id (str | Unset): The short code of the associated project.
        project_name (str | Unset): The name of the associated project.
        project_project_flag (str | Unset): Indicates if this Project/EPS nose is a Project or EPS.
        remaining_duration (float | Unset): The remaining duration of the activity. Remaining duration is the total
            working time from the activity remaining start date to the remaining finish date. The remaining working time is
            computed using the activity's calendar. Before the activity is started, the remaining duration is the same as
            the planned duration. After the activity is completed the remaining duration is zero.
        remaining_early_finish_date (datetime.datetime | Unset): The remaining late end date, which is calculated by the
            scheduler.
        remaining_early_start_date (datetime.datetime | Unset): The date the remaining work for the activity is
            scheduled to begin. This date is computed by the project scheduler but can be updated manually by the project
            manager. Before the activity is started, the remaining start date is the same as the planned start date. This is
            the start date that Timesheets users follow.
        remaining_expense_cost (float | Unset): The remaining costs for all project expenses associated with the
            activity.
        remaining_float (float | Unset): The amount of time remaining by which the activity can be delayed before
            delaying the project finish date. Computed as late finish - remaining finish. If the remaining finish is the
            same as the early finish (in general, when the activity is not started), then the remaining float is the same as
            the total float.
        remaining_labor_cost (float | Unset): The remaining costs for all labor resources assigned to the activity. If
            no resources are assigned, computed as the activity remaining labor units * project default price / time.
        remaining_labor_units (float | Unset): The remaining units for all labor resources assigned to the activity. The
            remaining units reflects the work remaining to be done for the activity. Before the activity is started, the
            remaining units are the same as the planned units. After the activity is completed, the remaining units are
            zero.
        remaining_late_finish_date (datetime.datetime | Unset): The remaining late finish date calculated by the
            scheduler.
        remaining_late_start_date (datetime.datetime | Unset): The remaining late start date calculated by the
            scheduler.
        remaining_material_cost (float | Unset): The sum of all material resource remaining costs.
        remaining_non_labor_cost (float | Unset): The remaining costs for all nonlabor resources assigned to the
            activity. If no resources are assigned, computed as the activity remaining nonlabor units * project default
            price / time.
        remaining_non_labor_units (float | Unset): The remaining units for all nonlabor resources assigned to the
            activity. The remaining units reflects the work remaining to be done for the activity. Before the activity is
            started, the remaining units are the same as the planned units. After the activity is completed, the remaining
            units are zero.
        remaining_total_cost (float | Unset): The remaining total cost for the activity, including labor resources,
            nonlabor resources, and project expenses. Remaining total cost = remaining labor costs + remaining nonlabor
            costs + remaining expense costs.
        remaining_total_units (float | Unset): The sum of Remaining Labor Units and Remaining Nonlabor Units.
        resume_date (datetime.datetime | Unset): The date when a suspended task or resource dependent activity should be
            resumed. The resume date must be later than the suspend date and earlier than the actual finish date. The
            Suspend/Resume period behaves like a nonworktime on the activity calendar or resource calendar for task and
            resource dependent activities.
        review_finish_date (datetime.datetime | Unset): The finish date of the activity as proposed by the primary
            resource using Timesheets, while the activity is in "For Review" state. If the project manager approves the
            activity completion, the review finish is copied to the actual finish.
        review_required (bool | Unset): The indicator that determines whether the activity status updates made in Team
            Member interfaces must be approved before committing changes.
        review_status (str | Unset): The activity review status. Valid values are 'OK', 'For Review', and 'Rejected'.
            Primary resources set the status to 'For Review' when they believe the activity is completed but are not allowed
            to mark activities as completed.
        schedule_percent_complete (float | Unset): The activity schedule percent complete, which specifies how much of
            the activity's project baseline duration has been completed so far. Computed based on where the current data
            date falls relative to the activity's project baseline start and finish dates. If the data date is earlier than
            the BL start, the schedule % complete is 0. If the data date is later than the BL finish, the schedule %
            complete is 100. The schedule % complete indicates how much of the activity duration should be currently
            completed, relative to the selected project baseline.
        schedule_performance_index (float | Unset): The ratio of the earned value of work performed and the work
            scheduled to be performed. Computed as SPI = earned value/ planned value. A value less than 1 indicates that
            less work was actually performed than was scheduled.
        schedule_performance_index_labor_units (float | Unset): The ratio of the earned value of labor units and the
            planned value of labor units. Computed as SPI labor units = earned value labor units / planned value labor
            units.
        schedule_variance (float | Unset): The difference between the earned value of work performed and the work
            scheduled to be performed. Computed as SV = earned value - planned value. A negative value indicates that less
            work was actually performed than was scheduled.
        schedule_variance_index (float | Unset): The ratio of the schedule variance and the work scheduled to be
            performed. Computed as SVI = SV / planned value.
        schedule_variance_index_labor_units (float | Unset): The ratio of the schedule variance and the work scheduled
            to be performed. Computed as SVI labor units = SV labor units / planned value labor units.
        schedule_variance_labor_units (float | Unset): The difference between the earned value of work performed and the
            work scheduled to be performed. Computed as SV labor units = earned value labor units - planned value labor
            units.
        scope_percent_complete (float | Unset):
        secondary_constraint_date (datetime.datetime | Unset): The date to be used for the cstr_type2 assignment, if the
            activity has a cstr_type2 value. The activity's constraint type determines whether this is a start date or
            finish date. Activity constraints are used by the project scheduler.
        secondary_constraint_type (str | Unset): The additional constraint to be used by the scheduler. If more than one
            constraint is assigned, this value should be restricted to one of the following: "Start On or Before", "Start On
            or After", "Finish On or Before", or "Finish On or After".
        start_date (datetime.datetime | Unset): The start date of the activity. Set to the remaining start date until
            the activity is started, then set to the actual start date.
        start_date_1_variance (float | Unset): The duration between the start date in the current project and the
            primary baseline start date. Calculated as start date - primary baseline start date.
        start_date_variance (float | Unset): The duration between the start date in the current project and the project
            baseline start date. Calculated as start date - project baseline start date.
        status (str | Unset): The current status of the activity, either 'Not Started', 'In Progress', or 'Completed'.
        status_code (str | Unset): The project status, either 'Planned', 'Active', 'Inactive', 'What-If', 'Requested',
            or 'Template'.
        suspend_date (datetime.datetime | Unset): The start date when the progress of a task or resource dependent
            activity is delayed from. The suspend date must be later than the actual start date, which the activity must
            have. The progress of the activity can be resumed by setting the resume date. The Suspend/Resume period behaves
            like a nonworktime on the activity calendar or resource calendar for task and resource dependent activities.
        task_status_completion (str | Unset):
        task_status_dates (str | Unset):
        task_status_indicator (bool | Unset):
        to_complete_performance_index (float | Unset): The TCPI, which is calculated as (budget at completion - earned
            value) / (estimate at completion - ACWP).
        total_cost_1_variance (float | Unset): The difference between the primary baseline total cost and the at
            completion total cost. Calculated as BL total cost - at completion total cost.
        total_cost_variance (float | Unset): The difference between the project baseline total cost and the at
            completion total cost. Calculated as BL total cost - at completion total cost.
        total_float (float | Unset): The amount of time the activity can be delayed before delaying the project finish
            date. Total float can be computed as late start - early start or as late finish - early finish; this option can
            be set when running the project scheduler.
        type_ (str | Unset): The type of activity, either 'Task Dependent', 'Resource Dependent', 'Level of Effort',
            'Start Milestone', 'Finish Milestone', or 'WBS Summary'. A 'Task Dependent' activity is scheduled using the
            activity's calendar rather than the calendars of the assigned resources. A 'Resource Dependent' activity is
            scheduled using the calendars of the assigned resources. This type is used when several resources are assigned
            to the activity, but they may work separately. A 'Start Milestone' or 'Finish Milestone' is a zero-duration
            activity without resources, marking a significant project event. A 'Level of Effort' activity has a duration
            that is determined by its dependent activities. Administration-type activities are typically 'Level of Effort'.
            A 'WBS Summary' comprises a group of activities that share a common WBS level. For example, all activities whose
            WBS codes start with A (A.1, A.1.1, A.1.1.2, A.2, A.3 and so forth) can be part of one WBS activity whose WBS
            code is A.
        units_percent_complete (float | Unset): The percent complete of units for all labor and nonlabor resources
            assigned to the activity. Computed as actual units / at completion units * 100. Always in the range 0 to 100.
        unread_comment_count (int | Unset): The number of Team Member Discussion comments associated with the Activity
            which have not yet been read.
        wbs_code (str | Unset): The short code assigned to each WBS element for identification. Each WBS element is
            uniquely identified by concatenating its own code together with its parents' codes.
        wbs_name (str | Unset): The name of the WBS element.
        wbs_name_path (str | Unset):
        wbs_path (str | Unset): The WBS hierarchy of the activity.
        work_package_id (str | Unset):
        work_package_name (str | Unset):
    """

    project_object_id: int
    wbs_object_id: int
    accounting_variance: float | Unset = UNSET
    accounting_variance_labor_units: float | Unset = UNSET
    activity_owner_user_id: int | Unset = UNSET
    actual_duration: float | Unset = UNSET
    actual_expense_cost: float | Unset = UNSET
    actual_finish_date: datetime.datetime | Unset = UNSET
    actual_labor_cost: float | Unset = UNSET
    actual_labor_units: float | Unset = UNSET
    actual_material_cost: float | Unset = UNSET
    actual_non_labor_cost: float | Unset = UNSET
    actual_non_labor_units: float | Unset = UNSET
    actual_start_date: datetime.datetime | Unset = UNSET
    actual_this_period_labor_cost: float | Unset = UNSET
    actual_this_period_labor_units: float | Unset = UNSET
    actual_this_period_material_cost: float | Unset = UNSET
    actual_this_period_non_labor_cost: float | Unset = UNSET
    actual_this_period_non_labor_units: float | Unset = UNSET
    actual_total_cost: float | Unset = UNSET
    actual_total_units: float | Unset = UNSET
    at_completion_duration: float | Unset = UNSET
    at_completion_expense_cost: float | Unset = UNSET
    at_completion_labor_cost: float | Unset = UNSET
    at_completion_labor_units: float | Unset = UNSET
    at_completion_labor_units_variance: float | Unset = UNSET
    at_completion_material_cost: float | Unset = UNSET
    at_completion_non_labor_cost: float | Unset = UNSET
    at_completion_non_labor_units: float | Unset = UNSET
    at_completion_total_cost: float | Unset = UNSET
    at_completion_total_units: float | Unset = UNSET
    at_completion_variance: float | Unset = UNSET
    auto_compute_actuals: bool | Unset = UNSET
    baseline_1_duration: float | Unset = UNSET
    baseline_1_finish_date: datetime.datetime | Unset = UNSET
    baseline_1_planned_duration: float | Unset = UNSET
    baseline_1_planned_expense_cost: float | Unset = UNSET
    baseline_1_planned_labor_cost: float | Unset = UNSET
    baseline_1_planned_labor_units: float | Unset = UNSET
    baseline_1_planned_material_cost: float | Unset = UNSET
    baseline_1_planned_non_labor_cost: float | Unset = UNSET
    baseline_1_planned_non_labor_units: float | Unset = UNSET
    baseline_1_planned_total_cost: float | Unset = UNSET
    baseline_1_start_date: datetime.datetime | Unset = UNSET
    baseline_duration: float | Unset = UNSET
    baseline_finish_date: datetime.datetime | Unset = UNSET
    baseline_planned_duration: float | Unset = UNSET
    baseline_planned_expense_cost: float | Unset = UNSET
    baseline_planned_labor_cost: float | Unset = UNSET
    baseline_planned_labor_units: float | Unset = UNSET
    baseline_planned_material_cost: float | Unset = UNSET
    baseline_planned_non_labor_cost: float | Unset = UNSET
    baseline_planned_non_labor_units: float | Unset = UNSET
    baseline_planned_total_cost: float | Unset = UNSET
    baseline_start_date: datetime.datetime | Unset = UNSET
    budget_at_completion: float | Unset = UNSET
    cbs_code: str | Unset = UNSET
    cbs_id: int | Unset = UNSET
    cbs_object_id: int | Unset = UNSET
    calendar_name: str | Unset = UNSET
    calendar_object_id: int | Unset = UNSET
    cost_percent_complete: float | Unset = UNSET
    cost_percent_of_planned: float | Unset = UNSET
    cost_performance_index: float | Unset = UNSET
    cost_performance_index_labor_units: float | Unset = UNSET
    cost_variance: float | Unset = UNSET
    cost_variance_index: float | Unset = UNSET
    cost_variance_index_labor_units: float | Unset = UNSET
    cost_variance_labor_units: float | Unset = UNSET
    create_date: datetime.datetime | Unset = UNSET
    create_user: str | Unset = UNSET
    data_date: datetime.datetime | Unset = UNSET
    duration_1_variance: float | Unset = UNSET
    duration_percent_complete: float | Unset = UNSET
    duration_percent_of_planned: float | Unset = UNSET
    duration_type: str | Unset = UNSET
    duration_variance: float | Unset = UNSET
    early_finish_date: datetime.datetime | Unset = UNSET
    early_start_date: datetime.datetime | Unset = UNSET
    earned_value_cost: float | Unset = UNSET
    earned_value_labor_units: float | Unset = UNSET
    estimate_at_completion_cost: float | Unset = UNSET
    estimate_at_completion_labor_units: float | Unset = UNSET
    estimate_to_complete: float | Unset = UNSET
    estimate_to_complete_labor_units: float | Unset = UNSET
    estimated_weight: float | Unset = UNSET
    expected_finish_date: datetime.datetime | Unset = UNSET
    expense_cost_1_variance: float | Unset = UNSET
    expense_cost_percent_complete: float | Unset = UNSET
    expense_cost_variance: float | Unset = UNSET
    external_early_start_date: datetime.datetime | Unset = UNSET
    external_late_finish_date: datetime.datetime | Unset = UNSET
    feedback: str | Unset = UNSET
    financial_period_tmpl_id: int | Unset = UNSET
    finish_date: datetime.datetime | Unset = UNSET
    finish_date_1_variance: float | Unset = UNSET
    finish_date_variance: float | Unset = UNSET
    float_path: int | Unset = UNSET
    float_path_order: int | Unset = UNSET
    free_float: float | Unset = UNSET
    guid: str | Unset = UNSET
    has_future_bucket_data: bool | Unset = UNSET
    id: str | Unset = UNSET
    is_baseline: bool | Unset = UNSET
    is_critical: bool | Unset = UNSET
    is_longest_path: bool | Unset = UNSET
    is_new_feedback: bool | Unset = UNSET
    is_starred: bool | Unset = UNSET
    is_template: bool | Unset = UNSET
    is_work_package: bool | Unset = UNSET
    labor_cost_1_variance: float | Unset = UNSET
    labor_cost_percent_complete: float | Unset = UNSET
    labor_cost_variance: float | Unset = UNSET
    labor_units_1_variance: float | Unset = UNSET
    labor_units_percent_complete: float | Unset = UNSET
    labor_units_variance: float | Unset = UNSET
    last_update_date: datetime.datetime | Unset = UNSET
    last_update_user: str | Unset = UNSET
    late_finish_date: datetime.datetime | Unset = UNSET
    late_start_date: datetime.datetime | Unset = UNSET
    leveling_priority: str | Unset = UNSET
    location_name: str | Unset = UNSET
    location_object_id: int | Unset = UNSET
    material_cost_1_variance: float | Unset = UNSET
    material_cost_percent_complete: float | Unset = UNSET
    material_cost_variance: float | Unset = UNSET
    maximum_duration: float | Unset = UNSET
    minimum_duration: float | Unset = UNSET
    most_likely_duration: float | Unset = UNSET
    name: str | Unset = UNSET
    non_labor_cost_1_variance: float | Unset = UNSET
    non_labor_cost_percent_complete: float | Unset = UNSET
    non_labor_cost_variance: float | Unset = UNSET
    non_labor_units_1_variance: float | Unset = UNSET
    non_labor_units_percent_complete: float | Unset = UNSET
    non_labor_units_variance: float | Unset = UNSET
    notes_to_resources: str | Unset = UNSET
    object_id: int | Unset = UNSET
    owner_id_array: str | Unset = UNSET
    owner_names_array: str | Unset = UNSET
    percent_complete: float | Unset = UNSET
    percent_complete_type: str | Unset = UNSET
    performance_percent_complete: float | Unset = UNSET
    performance_percent_complete_by_labor_units: float | Unset = UNSET
    physical_percent_complete: float | Unset = UNSET
    planned_duration: float | Unset = UNSET
    planned_expense_cost: float | Unset = UNSET
    planned_finish_date: datetime.datetime | Unset = UNSET
    planned_labor_cost: float | Unset = UNSET
    planned_labor_units: float | Unset = UNSET
    planned_material_cost: float | Unset = UNSET
    planned_non_labor_cost: float | Unset = UNSET
    planned_non_labor_units: float | Unset = UNSET
    planned_start_date: datetime.datetime | Unset = UNSET
    planned_total_cost: float | Unset = UNSET
    planned_total_units: float | Unset = UNSET
    planned_value_cost: float | Unset = UNSET
    planned_value_labor_units: float | Unset = UNSET
    post_resp_criticality_index: float | Unset = UNSET
    post_response_pessimistic_finish: datetime.datetime | Unset = UNSET
    post_response_pessimistic_start: datetime.datetime | Unset = UNSET
    pre_resp_criticality_index: float | Unset = UNSET
    pre_response_pessimistic_finish: datetime.datetime | Unset = UNSET
    pre_response_pessimistic_start: datetime.datetime | Unset = UNSET
    primary_constraint_date: datetime.datetime | Unset = UNSET
    primary_constraint_type: str | Unset = UNSET
    primary_resource_id: str | Unset = UNSET
    primary_resource_name: str | Unset = UNSET
    primary_resource_object_id: int | Unset = UNSET
    project_flag: str | Unset = UNSET
    project_id: str | Unset = UNSET
    project_name: str | Unset = UNSET
    project_project_flag: str | Unset = UNSET
    remaining_duration: float | Unset = UNSET
    remaining_early_finish_date: datetime.datetime | Unset = UNSET
    remaining_early_start_date: datetime.datetime | Unset = UNSET
    remaining_expense_cost: float | Unset = UNSET
    remaining_float: float | Unset = UNSET
    remaining_labor_cost: float | Unset = UNSET
    remaining_labor_units: float | Unset = UNSET
    remaining_late_finish_date: datetime.datetime | Unset = UNSET
    remaining_late_start_date: datetime.datetime | Unset = UNSET
    remaining_material_cost: float | Unset = UNSET
    remaining_non_labor_cost: float | Unset = UNSET
    remaining_non_labor_units: float | Unset = UNSET
    remaining_total_cost: float | Unset = UNSET
    remaining_total_units: float | Unset = UNSET
    resume_date: datetime.datetime | Unset = UNSET
    review_finish_date: datetime.datetime | Unset = UNSET
    review_required: bool | Unset = UNSET
    review_status: str | Unset = UNSET
    schedule_percent_complete: float | Unset = UNSET
    schedule_performance_index: float | Unset = UNSET
    schedule_performance_index_labor_units: float | Unset = UNSET
    schedule_variance: float | Unset = UNSET
    schedule_variance_index: float | Unset = UNSET
    schedule_variance_index_labor_units: float | Unset = UNSET
    schedule_variance_labor_units: float | Unset = UNSET
    scope_percent_complete: float | Unset = UNSET
    secondary_constraint_date: datetime.datetime | Unset = UNSET
    secondary_constraint_type: str | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    start_date_1_variance: float | Unset = UNSET
    start_date_variance: float | Unset = UNSET
    status: str | Unset = UNSET
    status_code: str | Unset = UNSET
    suspend_date: datetime.datetime | Unset = UNSET
    task_status_completion: str | Unset = UNSET
    task_status_dates: str | Unset = UNSET
    task_status_indicator: bool | Unset = UNSET
    to_complete_performance_index: float | Unset = UNSET
    total_cost_1_variance: float | Unset = UNSET
    total_cost_variance: float | Unset = UNSET
    total_float: float | Unset = UNSET
    type_: str | Unset = UNSET
    units_percent_complete: float | Unset = UNSET
    unread_comment_count: int | Unset = UNSET
    wbs_code: str | Unset = UNSET
    wbs_name: str | Unset = UNSET
    wbs_name_path: str | Unset = UNSET
    wbs_path: str | Unset = UNSET
    work_package_id: str | Unset = UNSET
    work_package_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_object_id = self.project_object_id

        wbs_object_id = self.wbs_object_id

        accounting_variance = self.accounting_variance

        accounting_variance_labor_units = self.accounting_variance_labor_units

        activity_owner_user_id = self.activity_owner_user_id

        actual_duration = self.actual_duration

        actual_expense_cost = self.actual_expense_cost

        actual_finish_date: str | Unset = UNSET
        if not isinstance(self.actual_finish_date, Unset):
            actual_finish_date = self.actual_finish_date.isoformat()

        actual_labor_cost = self.actual_labor_cost

        actual_labor_units = self.actual_labor_units

        actual_material_cost = self.actual_material_cost

        actual_non_labor_cost = self.actual_non_labor_cost

        actual_non_labor_units = self.actual_non_labor_units

        actual_start_date: str | Unset = UNSET
        if not isinstance(self.actual_start_date, Unset):
            actual_start_date = self.actual_start_date.isoformat()

        actual_this_period_labor_cost = self.actual_this_period_labor_cost

        actual_this_period_labor_units = self.actual_this_period_labor_units

        actual_this_period_material_cost = self.actual_this_period_material_cost

        actual_this_period_non_labor_cost = self.actual_this_period_non_labor_cost

        actual_this_period_non_labor_units = self.actual_this_period_non_labor_units

        actual_total_cost = self.actual_total_cost

        actual_total_units = self.actual_total_units

        at_completion_duration = self.at_completion_duration

        at_completion_expense_cost = self.at_completion_expense_cost

        at_completion_labor_cost = self.at_completion_labor_cost

        at_completion_labor_units = self.at_completion_labor_units

        at_completion_labor_units_variance = self.at_completion_labor_units_variance

        at_completion_material_cost = self.at_completion_material_cost

        at_completion_non_labor_cost = self.at_completion_non_labor_cost

        at_completion_non_labor_units = self.at_completion_non_labor_units

        at_completion_total_cost = self.at_completion_total_cost

        at_completion_total_units = self.at_completion_total_units

        at_completion_variance = self.at_completion_variance

        auto_compute_actuals = self.auto_compute_actuals

        baseline_1_duration = self.baseline_1_duration

        baseline_1_finish_date: str | Unset = UNSET
        if not isinstance(self.baseline_1_finish_date, Unset):
            baseline_1_finish_date = self.baseline_1_finish_date.isoformat()

        baseline_1_planned_duration = self.baseline_1_planned_duration

        baseline_1_planned_expense_cost = self.baseline_1_planned_expense_cost

        baseline_1_planned_labor_cost = self.baseline_1_planned_labor_cost

        baseline_1_planned_labor_units = self.baseline_1_planned_labor_units

        baseline_1_planned_material_cost = self.baseline_1_planned_material_cost

        baseline_1_planned_non_labor_cost = self.baseline_1_planned_non_labor_cost

        baseline_1_planned_non_labor_units = self.baseline_1_planned_non_labor_units

        baseline_1_planned_total_cost = self.baseline_1_planned_total_cost

        baseline_1_start_date: str | Unset = UNSET
        if not isinstance(self.baseline_1_start_date, Unset):
            baseline_1_start_date = self.baseline_1_start_date.isoformat()

        baseline_duration = self.baseline_duration

        baseline_finish_date: str | Unset = UNSET
        if not isinstance(self.baseline_finish_date, Unset):
            baseline_finish_date = self.baseline_finish_date.isoformat()

        baseline_planned_duration = self.baseline_planned_duration

        baseline_planned_expense_cost = self.baseline_planned_expense_cost

        baseline_planned_labor_cost = self.baseline_planned_labor_cost

        baseline_planned_labor_units = self.baseline_planned_labor_units

        baseline_planned_material_cost = self.baseline_planned_material_cost

        baseline_planned_non_labor_cost = self.baseline_planned_non_labor_cost

        baseline_planned_non_labor_units = self.baseline_planned_non_labor_units

        baseline_planned_total_cost = self.baseline_planned_total_cost

        baseline_start_date: str | Unset = UNSET
        if not isinstance(self.baseline_start_date, Unset):
            baseline_start_date = self.baseline_start_date.isoformat()

        budget_at_completion = self.budget_at_completion

        cbs_code = self.cbs_code

        cbs_id = self.cbs_id

        cbs_object_id = self.cbs_object_id

        calendar_name = self.calendar_name

        calendar_object_id = self.calendar_object_id

        cost_percent_complete = self.cost_percent_complete

        cost_percent_of_planned = self.cost_percent_of_planned

        cost_performance_index = self.cost_performance_index

        cost_performance_index_labor_units = self.cost_performance_index_labor_units

        cost_variance = self.cost_variance

        cost_variance_index = self.cost_variance_index

        cost_variance_index_labor_units = self.cost_variance_index_labor_units

        cost_variance_labor_units = self.cost_variance_labor_units

        create_date: str | Unset = UNSET
        if not isinstance(self.create_date, Unset):
            create_date = self.create_date.isoformat()

        create_user = self.create_user

        data_date: str | Unset = UNSET
        if not isinstance(self.data_date, Unset):
            data_date = self.data_date.isoformat()

        duration_1_variance = self.duration_1_variance

        duration_percent_complete = self.duration_percent_complete

        duration_percent_of_planned = self.duration_percent_of_planned

        duration_type = self.duration_type

        duration_variance = self.duration_variance

        early_finish_date: str | Unset = UNSET
        if not isinstance(self.early_finish_date, Unset):
            early_finish_date = self.early_finish_date.isoformat()

        early_start_date: str | Unset = UNSET
        if not isinstance(self.early_start_date, Unset):
            early_start_date = self.early_start_date.isoformat()

        earned_value_cost = self.earned_value_cost

        earned_value_labor_units = self.earned_value_labor_units

        estimate_at_completion_cost = self.estimate_at_completion_cost

        estimate_at_completion_labor_units = self.estimate_at_completion_labor_units

        estimate_to_complete = self.estimate_to_complete

        estimate_to_complete_labor_units = self.estimate_to_complete_labor_units

        estimated_weight = self.estimated_weight

        expected_finish_date: str | Unset = UNSET
        if not isinstance(self.expected_finish_date, Unset):
            expected_finish_date = self.expected_finish_date.isoformat()

        expense_cost_1_variance = self.expense_cost_1_variance

        expense_cost_percent_complete = self.expense_cost_percent_complete

        expense_cost_variance = self.expense_cost_variance

        external_early_start_date: str | Unset = UNSET
        if not isinstance(self.external_early_start_date, Unset):
            external_early_start_date = self.external_early_start_date.isoformat()

        external_late_finish_date: str | Unset = UNSET
        if not isinstance(self.external_late_finish_date, Unset):
            external_late_finish_date = self.external_late_finish_date.isoformat()

        feedback = self.feedback

        financial_period_tmpl_id = self.financial_period_tmpl_id

        finish_date: str | Unset = UNSET
        if not isinstance(self.finish_date, Unset):
            finish_date = self.finish_date.isoformat()

        finish_date_1_variance = self.finish_date_1_variance

        finish_date_variance = self.finish_date_variance

        float_path = self.float_path

        float_path_order = self.float_path_order

        free_float = self.free_float

        guid = self.guid

        has_future_bucket_data = self.has_future_bucket_data

        id = self.id

        is_baseline = self.is_baseline

        is_critical = self.is_critical

        is_longest_path = self.is_longest_path

        is_new_feedback = self.is_new_feedback

        is_starred = self.is_starred

        is_template = self.is_template

        is_work_package = self.is_work_package

        labor_cost_1_variance = self.labor_cost_1_variance

        labor_cost_percent_complete = self.labor_cost_percent_complete

        labor_cost_variance = self.labor_cost_variance

        labor_units_1_variance = self.labor_units_1_variance

        labor_units_percent_complete = self.labor_units_percent_complete

        labor_units_variance = self.labor_units_variance

        last_update_date: str | Unset = UNSET
        if not isinstance(self.last_update_date, Unset):
            last_update_date = self.last_update_date.isoformat()

        last_update_user = self.last_update_user

        late_finish_date: str | Unset = UNSET
        if not isinstance(self.late_finish_date, Unset):
            late_finish_date = self.late_finish_date.isoformat()

        late_start_date: str | Unset = UNSET
        if not isinstance(self.late_start_date, Unset):
            late_start_date = self.late_start_date.isoformat()

        leveling_priority = self.leveling_priority

        location_name = self.location_name

        location_object_id = self.location_object_id

        material_cost_1_variance = self.material_cost_1_variance

        material_cost_percent_complete = self.material_cost_percent_complete

        material_cost_variance = self.material_cost_variance

        maximum_duration = self.maximum_duration

        minimum_duration = self.minimum_duration

        most_likely_duration = self.most_likely_duration

        name = self.name

        non_labor_cost_1_variance = self.non_labor_cost_1_variance

        non_labor_cost_percent_complete = self.non_labor_cost_percent_complete

        non_labor_cost_variance = self.non_labor_cost_variance

        non_labor_units_1_variance = self.non_labor_units_1_variance

        non_labor_units_percent_complete = self.non_labor_units_percent_complete

        non_labor_units_variance = self.non_labor_units_variance

        notes_to_resources = self.notes_to_resources

        object_id = self.object_id

        owner_id_array = self.owner_id_array

        owner_names_array = self.owner_names_array

        percent_complete = self.percent_complete

        percent_complete_type = self.percent_complete_type

        performance_percent_complete = self.performance_percent_complete

        performance_percent_complete_by_labor_units = self.performance_percent_complete_by_labor_units

        physical_percent_complete = self.physical_percent_complete

        planned_duration = self.planned_duration

        planned_expense_cost = self.planned_expense_cost

        planned_finish_date: str | Unset = UNSET
        if not isinstance(self.planned_finish_date, Unset):
            planned_finish_date = self.planned_finish_date.isoformat()

        planned_labor_cost = self.planned_labor_cost

        planned_labor_units = self.planned_labor_units

        planned_material_cost = self.planned_material_cost

        planned_non_labor_cost = self.planned_non_labor_cost

        planned_non_labor_units = self.planned_non_labor_units

        planned_start_date: str | Unset = UNSET
        if not isinstance(self.planned_start_date, Unset):
            planned_start_date = self.planned_start_date.isoformat()

        planned_total_cost = self.planned_total_cost

        planned_total_units = self.planned_total_units

        planned_value_cost = self.planned_value_cost

        planned_value_labor_units = self.planned_value_labor_units

        post_resp_criticality_index = self.post_resp_criticality_index

        post_response_pessimistic_finish: str | Unset = UNSET
        if not isinstance(self.post_response_pessimistic_finish, Unset):
            post_response_pessimistic_finish = self.post_response_pessimistic_finish.isoformat()

        post_response_pessimistic_start: str | Unset = UNSET
        if not isinstance(self.post_response_pessimistic_start, Unset):
            post_response_pessimistic_start = self.post_response_pessimistic_start.isoformat()

        pre_resp_criticality_index = self.pre_resp_criticality_index

        pre_response_pessimistic_finish: str | Unset = UNSET
        if not isinstance(self.pre_response_pessimistic_finish, Unset):
            pre_response_pessimistic_finish = self.pre_response_pessimistic_finish.isoformat()

        pre_response_pessimistic_start: str | Unset = UNSET
        if not isinstance(self.pre_response_pessimistic_start, Unset):
            pre_response_pessimistic_start = self.pre_response_pessimistic_start.isoformat()

        primary_constraint_date: str | Unset = UNSET
        if not isinstance(self.primary_constraint_date, Unset):
            primary_constraint_date = self.primary_constraint_date.isoformat()

        primary_constraint_type = self.primary_constraint_type

        primary_resource_id = self.primary_resource_id

        primary_resource_name = self.primary_resource_name

        primary_resource_object_id = self.primary_resource_object_id

        project_flag = self.project_flag

        project_id = self.project_id

        project_name = self.project_name

        project_project_flag = self.project_project_flag

        remaining_duration = self.remaining_duration

        remaining_early_finish_date: str | Unset = UNSET
        if not isinstance(self.remaining_early_finish_date, Unset):
            remaining_early_finish_date = self.remaining_early_finish_date.isoformat()

        remaining_early_start_date: str | Unset = UNSET
        if not isinstance(self.remaining_early_start_date, Unset):
            remaining_early_start_date = self.remaining_early_start_date.isoformat()

        remaining_expense_cost = self.remaining_expense_cost

        remaining_float = self.remaining_float

        remaining_labor_cost = self.remaining_labor_cost

        remaining_labor_units = self.remaining_labor_units

        remaining_late_finish_date: str | Unset = UNSET
        if not isinstance(self.remaining_late_finish_date, Unset):
            remaining_late_finish_date = self.remaining_late_finish_date.isoformat()

        remaining_late_start_date: str | Unset = UNSET
        if not isinstance(self.remaining_late_start_date, Unset):
            remaining_late_start_date = self.remaining_late_start_date.isoformat()

        remaining_material_cost = self.remaining_material_cost

        remaining_non_labor_cost = self.remaining_non_labor_cost

        remaining_non_labor_units = self.remaining_non_labor_units

        remaining_total_cost = self.remaining_total_cost

        remaining_total_units = self.remaining_total_units

        resume_date: str | Unset = UNSET
        if not isinstance(self.resume_date, Unset):
            resume_date = self.resume_date.isoformat()

        review_finish_date: str | Unset = UNSET
        if not isinstance(self.review_finish_date, Unset):
            review_finish_date = self.review_finish_date.isoformat()

        review_required = self.review_required

        review_status = self.review_status

        schedule_percent_complete = self.schedule_percent_complete

        schedule_performance_index = self.schedule_performance_index

        schedule_performance_index_labor_units = self.schedule_performance_index_labor_units

        schedule_variance = self.schedule_variance

        schedule_variance_index = self.schedule_variance_index

        schedule_variance_index_labor_units = self.schedule_variance_index_labor_units

        schedule_variance_labor_units = self.schedule_variance_labor_units

        scope_percent_complete = self.scope_percent_complete

        secondary_constraint_date: str | Unset = UNSET
        if not isinstance(self.secondary_constraint_date, Unset):
            secondary_constraint_date = self.secondary_constraint_date.isoformat()

        secondary_constraint_type = self.secondary_constraint_type

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        start_date_1_variance = self.start_date_1_variance

        start_date_variance = self.start_date_variance

        status = self.status

        status_code = self.status_code

        suspend_date: str | Unset = UNSET
        if not isinstance(self.suspend_date, Unset):
            suspend_date = self.suspend_date.isoformat()

        task_status_completion = self.task_status_completion

        task_status_dates = self.task_status_dates

        task_status_indicator = self.task_status_indicator

        to_complete_performance_index = self.to_complete_performance_index

        total_cost_1_variance = self.total_cost_1_variance

        total_cost_variance = self.total_cost_variance

        total_float = self.total_float

        type_ = self.type_

        units_percent_complete = self.units_percent_complete

        unread_comment_count = self.unread_comment_count

        wbs_code = self.wbs_code

        wbs_name = self.wbs_name

        wbs_name_path = self.wbs_name_path

        wbs_path = self.wbs_path

        work_package_id = self.work_package_id

        work_package_name = self.work_package_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ProjectObjectId": project_object_id,
                "WBSObjectId": wbs_object_id,
            }
        )
        if accounting_variance is not UNSET:
            field_dict["AccountingVariance"] = accounting_variance
        if accounting_variance_labor_units is not UNSET:
            field_dict["AccountingVarianceLaborUnits"] = accounting_variance_labor_units
        if activity_owner_user_id is not UNSET:
            field_dict["ActivityOwnerUserId"] = activity_owner_user_id
        if actual_duration is not UNSET:
            field_dict["ActualDuration"] = actual_duration
        if actual_expense_cost is not UNSET:
            field_dict["ActualExpenseCost"] = actual_expense_cost
        if actual_finish_date is not UNSET:
            field_dict["ActualFinishDate"] = actual_finish_date
        if actual_labor_cost is not UNSET:
            field_dict["ActualLaborCost"] = actual_labor_cost
        if actual_labor_units is not UNSET:
            field_dict["ActualLaborUnits"] = actual_labor_units
        if actual_material_cost is not UNSET:
            field_dict["ActualMaterialCost"] = actual_material_cost
        if actual_non_labor_cost is not UNSET:
            field_dict["ActualNonLaborCost"] = actual_non_labor_cost
        if actual_non_labor_units is not UNSET:
            field_dict["ActualNonLaborUnits"] = actual_non_labor_units
        if actual_start_date is not UNSET:
            field_dict["ActualStartDate"] = actual_start_date
        if actual_this_period_labor_cost is not UNSET:
            field_dict["ActualThisPeriodLaborCost"] = actual_this_period_labor_cost
        if actual_this_period_labor_units is not UNSET:
            field_dict["ActualThisPeriodLaborUnits"] = actual_this_period_labor_units
        if actual_this_period_material_cost is not UNSET:
            field_dict["ActualThisPeriodMaterialCost"] = actual_this_period_material_cost
        if actual_this_period_non_labor_cost is not UNSET:
            field_dict["ActualThisPeriodNonLaborCost"] = actual_this_period_non_labor_cost
        if actual_this_period_non_labor_units is not UNSET:
            field_dict["ActualThisPeriodNonLaborUnits"] = actual_this_period_non_labor_units
        if actual_total_cost is not UNSET:
            field_dict["ActualTotalCost"] = actual_total_cost
        if actual_total_units is not UNSET:
            field_dict["ActualTotalUnits"] = actual_total_units
        if at_completion_duration is not UNSET:
            field_dict["AtCompletionDuration"] = at_completion_duration
        if at_completion_expense_cost is not UNSET:
            field_dict["AtCompletionExpenseCost"] = at_completion_expense_cost
        if at_completion_labor_cost is not UNSET:
            field_dict["AtCompletionLaborCost"] = at_completion_labor_cost
        if at_completion_labor_units is not UNSET:
            field_dict["AtCompletionLaborUnits"] = at_completion_labor_units
        if at_completion_labor_units_variance is not UNSET:
            field_dict["AtCompletionLaborUnitsVariance"] = at_completion_labor_units_variance
        if at_completion_material_cost is not UNSET:
            field_dict["AtCompletionMaterialCost"] = at_completion_material_cost
        if at_completion_non_labor_cost is not UNSET:
            field_dict["AtCompletionNonLaborCost"] = at_completion_non_labor_cost
        if at_completion_non_labor_units is not UNSET:
            field_dict["AtCompletionNonLaborUnits"] = at_completion_non_labor_units
        if at_completion_total_cost is not UNSET:
            field_dict["AtCompletionTotalCost"] = at_completion_total_cost
        if at_completion_total_units is not UNSET:
            field_dict["AtCompletionTotalUnits"] = at_completion_total_units
        if at_completion_variance is not UNSET:
            field_dict["AtCompletionVariance"] = at_completion_variance
        if auto_compute_actuals is not UNSET:
            field_dict["AutoComputeActuals"] = auto_compute_actuals
        if baseline_1_duration is not UNSET:
            field_dict["Baseline1Duration"] = baseline_1_duration
        if baseline_1_finish_date is not UNSET:
            field_dict["Baseline1FinishDate"] = baseline_1_finish_date
        if baseline_1_planned_duration is not UNSET:
            field_dict["Baseline1PlannedDuration"] = baseline_1_planned_duration
        if baseline_1_planned_expense_cost is not UNSET:
            field_dict["Baseline1PlannedExpenseCost"] = baseline_1_planned_expense_cost
        if baseline_1_planned_labor_cost is not UNSET:
            field_dict["Baseline1PlannedLaborCost"] = baseline_1_planned_labor_cost
        if baseline_1_planned_labor_units is not UNSET:
            field_dict["Baseline1PlannedLaborUnits"] = baseline_1_planned_labor_units
        if baseline_1_planned_material_cost is not UNSET:
            field_dict["Baseline1PlannedMaterialCost"] = baseline_1_planned_material_cost
        if baseline_1_planned_non_labor_cost is not UNSET:
            field_dict["Baseline1PlannedNonLaborCost"] = baseline_1_planned_non_labor_cost
        if baseline_1_planned_non_labor_units is not UNSET:
            field_dict["Baseline1PlannedNonLaborUnits"] = baseline_1_planned_non_labor_units
        if baseline_1_planned_total_cost is not UNSET:
            field_dict["Baseline1PlannedTotalCost"] = baseline_1_planned_total_cost
        if baseline_1_start_date is not UNSET:
            field_dict["Baseline1StartDate"] = baseline_1_start_date
        if baseline_duration is not UNSET:
            field_dict["BaselineDuration"] = baseline_duration
        if baseline_finish_date is not UNSET:
            field_dict["BaselineFinishDate"] = baseline_finish_date
        if baseline_planned_duration is not UNSET:
            field_dict["BaselinePlannedDuration"] = baseline_planned_duration
        if baseline_planned_expense_cost is not UNSET:
            field_dict["BaselinePlannedExpenseCost"] = baseline_planned_expense_cost
        if baseline_planned_labor_cost is not UNSET:
            field_dict["BaselinePlannedLaborCost"] = baseline_planned_labor_cost
        if baseline_planned_labor_units is not UNSET:
            field_dict["BaselinePlannedLaborUnits"] = baseline_planned_labor_units
        if baseline_planned_material_cost is not UNSET:
            field_dict["BaselinePlannedMaterialCost"] = baseline_planned_material_cost
        if baseline_planned_non_labor_cost is not UNSET:
            field_dict["BaselinePlannedNonLaborCost"] = baseline_planned_non_labor_cost
        if baseline_planned_non_labor_units is not UNSET:
            field_dict["BaselinePlannedNonLaborUnits"] = baseline_planned_non_labor_units
        if baseline_planned_total_cost is not UNSET:
            field_dict["BaselinePlannedTotalCost"] = baseline_planned_total_cost
        if baseline_start_date is not UNSET:
            field_dict["BaselineStartDate"] = baseline_start_date
        if budget_at_completion is not UNSET:
            field_dict["BudgetAtCompletion"] = budget_at_completion
        if cbs_code is not UNSET:
            field_dict["CBSCode"] = cbs_code
        if cbs_id is not UNSET:
            field_dict["CBSId"] = cbs_id
        if cbs_object_id is not UNSET:
            field_dict["CBSObjectId"] = cbs_object_id
        if calendar_name is not UNSET:
            field_dict["CalendarName"] = calendar_name
        if calendar_object_id is not UNSET:
            field_dict["CalendarObjectId"] = calendar_object_id
        if cost_percent_complete is not UNSET:
            field_dict["CostPercentComplete"] = cost_percent_complete
        if cost_percent_of_planned is not UNSET:
            field_dict["CostPercentOfPlanned"] = cost_percent_of_planned
        if cost_performance_index is not UNSET:
            field_dict["CostPerformanceIndex"] = cost_performance_index
        if cost_performance_index_labor_units is not UNSET:
            field_dict["CostPerformanceIndexLaborUnits"] = cost_performance_index_labor_units
        if cost_variance is not UNSET:
            field_dict["CostVariance"] = cost_variance
        if cost_variance_index is not UNSET:
            field_dict["CostVarianceIndex"] = cost_variance_index
        if cost_variance_index_labor_units is not UNSET:
            field_dict["CostVarianceIndexLaborUnits"] = cost_variance_index_labor_units
        if cost_variance_labor_units is not UNSET:
            field_dict["CostVarianceLaborUnits"] = cost_variance_labor_units
        if create_date is not UNSET:
            field_dict["CreateDate"] = create_date
        if create_user is not UNSET:
            field_dict["CreateUser"] = create_user
        if data_date is not UNSET:
            field_dict["DataDate"] = data_date
        if duration_1_variance is not UNSET:
            field_dict["Duration1Variance"] = duration_1_variance
        if duration_percent_complete is not UNSET:
            field_dict["DurationPercentComplete"] = duration_percent_complete
        if duration_percent_of_planned is not UNSET:
            field_dict["DurationPercentOfPlanned"] = duration_percent_of_planned
        if duration_type is not UNSET:
            field_dict["DurationType"] = duration_type
        if duration_variance is not UNSET:
            field_dict["DurationVariance"] = duration_variance
        if early_finish_date is not UNSET:
            field_dict["EarlyFinishDate"] = early_finish_date
        if early_start_date is not UNSET:
            field_dict["EarlyStartDate"] = early_start_date
        if earned_value_cost is not UNSET:
            field_dict["EarnedValueCost"] = earned_value_cost
        if earned_value_labor_units is not UNSET:
            field_dict["EarnedValueLaborUnits"] = earned_value_labor_units
        if estimate_at_completion_cost is not UNSET:
            field_dict["EstimateAtCompletionCost"] = estimate_at_completion_cost
        if estimate_at_completion_labor_units is not UNSET:
            field_dict["EstimateAtCompletionLaborUnits"] = estimate_at_completion_labor_units
        if estimate_to_complete is not UNSET:
            field_dict["EstimateToComplete"] = estimate_to_complete
        if estimate_to_complete_labor_units is not UNSET:
            field_dict["EstimateToCompleteLaborUnits"] = estimate_to_complete_labor_units
        if estimated_weight is not UNSET:
            field_dict["EstimatedWeight"] = estimated_weight
        if expected_finish_date is not UNSET:
            field_dict["ExpectedFinishDate"] = expected_finish_date
        if expense_cost_1_variance is not UNSET:
            field_dict["ExpenseCost1Variance"] = expense_cost_1_variance
        if expense_cost_percent_complete is not UNSET:
            field_dict["ExpenseCostPercentComplete"] = expense_cost_percent_complete
        if expense_cost_variance is not UNSET:
            field_dict["ExpenseCostVariance"] = expense_cost_variance
        if external_early_start_date is not UNSET:
            field_dict["ExternalEarlyStartDate"] = external_early_start_date
        if external_late_finish_date is not UNSET:
            field_dict["ExternalLateFinishDate"] = external_late_finish_date
        if feedback is not UNSET:
            field_dict["Feedback"] = feedback
        if financial_period_tmpl_id is not UNSET:
            field_dict["FinancialPeriodTmplId"] = financial_period_tmpl_id
        if finish_date is not UNSET:
            field_dict["FinishDate"] = finish_date
        if finish_date_1_variance is not UNSET:
            field_dict["FinishDate1Variance"] = finish_date_1_variance
        if finish_date_variance is not UNSET:
            field_dict["FinishDateVariance"] = finish_date_variance
        if float_path is not UNSET:
            field_dict["FloatPath"] = float_path
        if float_path_order is not UNSET:
            field_dict["FloatPathOrder"] = float_path_order
        if free_float is not UNSET:
            field_dict["FreeFloat"] = free_float
        if guid is not UNSET:
            field_dict["GUID"] = guid
        if has_future_bucket_data is not UNSET:
            field_dict["HasFutureBucketData"] = has_future_bucket_data
        if id is not UNSET:
            field_dict["Id"] = id
        if is_baseline is not UNSET:
            field_dict["IsBaseline"] = is_baseline
        if is_critical is not UNSET:
            field_dict["IsCritical"] = is_critical
        if is_longest_path is not UNSET:
            field_dict["IsLongestPath"] = is_longest_path
        if is_new_feedback is not UNSET:
            field_dict["IsNewFeedback"] = is_new_feedback
        if is_starred is not UNSET:
            field_dict["IsStarred"] = is_starred
        if is_template is not UNSET:
            field_dict["IsTemplate"] = is_template
        if is_work_package is not UNSET:
            field_dict["IsWorkPackage"] = is_work_package
        if labor_cost_1_variance is not UNSET:
            field_dict["LaborCost1Variance"] = labor_cost_1_variance
        if labor_cost_percent_complete is not UNSET:
            field_dict["LaborCostPercentComplete"] = labor_cost_percent_complete
        if labor_cost_variance is not UNSET:
            field_dict["LaborCostVariance"] = labor_cost_variance
        if labor_units_1_variance is not UNSET:
            field_dict["LaborUnits1Variance"] = labor_units_1_variance
        if labor_units_percent_complete is not UNSET:
            field_dict["LaborUnitsPercentComplete"] = labor_units_percent_complete
        if labor_units_variance is not UNSET:
            field_dict["LaborUnitsVariance"] = labor_units_variance
        if last_update_date is not UNSET:
            field_dict["LastUpdateDate"] = last_update_date
        if last_update_user is not UNSET:
            field_dict["LastUpdateUser"] = last_update_user
        if late_finish_date is not UNSET:
            field_dict["LateFinishDate"] = late_finish_date
        if late_start_date is not UNSET:
            field_dict["LateStartDate"] = late_start_date
        if leveling_priority is not UNSET:
            field_dict["LevelingPriority"] = leveling_priority
        if location_name is not UNSET:
            field_dict["LocationName"] = location_name
        if location_object_id is not UNSET:
            field_dict["LocationObjectId"] = location_object_id
        if material_cost_1_variance is not UNSET:
            field_dict["MaterialCost1Variance"] = material_cost_1_variance
        if material_cost_percent_complete is not UNSET:
            field_dict["MaterialCostPercentComplete"] = material_cost_percent_complete
        if material_cost_variance is not UNSET:
            field_dict["MaterialCostVariance"] = material_cost_variance
        if maximum_duration is not UNSET:
            field_dict["MaximumDuration"] = maximum_duration
        if minimum_duration is not UNSET:
            field_dict["MinimumDuration"] = minimum_duration
        if most_likely_duration is not UNSET:
            field_dict["MostLikelyDuration"] = most_likely_duration
        if name is not UNSET:
            field_dict["Name"] = name
        if non_labor_cost_1_variance is not UNSET:
            field_dict["NonLaborCost1Variance"] = non_labor_cost_1_variance
        if non_labor_cost_percent_complete is not UNSET:
            field_dict["NonLaborCostPercentComplete"] = non_labor_cost_percent_complete
        if non_labor_cost_variance is not UNSET:
            field_dict["NonLaborCostVariance"] = non_labor_cost_variance
        if non_labor_units_1_variance is not UNSET:
            field_dict["NonLaborUnits1Variance"] = non_labor_units_1_variance
        if non_labor_units_percent_complete is not UNSET:
            field_dict["NonLaborUnitsPercentComplete"] = non_labor_units_percent_complete
        if non_labor_units_variance is not UNSET:
            field_dict["NonLaborUnitsVariance"] = non_labor_units_variance
        if notes_to_resources is not UNSET:
            field_dict["NotesToResources"] = notes_to_resources
        if object_id is not UNSET:
            field_dict["ObjectId"] = object_id
        if owner_id_array is not UNSET:
            field_dict["OwnerIDArray"] = owner_id_array
        if owner_names_array is not UNSET:
            field_dict["OwnerNamesArray"] = owner_names_array
        if percent_complete is not UNSET:
            field_dict["PercentComplete"] = percent_complete
        if percent_complete_type is not UNSET:
            field_dict["PercentCompleteType"] = percent_complete_type
        if performance_percent_complete is not UNSET:
            field_dict["PerformancePercentComplete"] = performance_percent_complete
        if performance_percent_complete_by_labor_units is not UNSET:
            field_dict["PerformancePercentCompleteByLaborUnits"] = performance_percent_complete_by_labor_units
        if physical_percent_complete is not UNSET:
            field_dict["PhysicalPercentComplete"] = physical_percent_complete
        if planned_duration is not UNSET:
            field_dict["PlannedDuration"] = planned_duration
        if planned_expense_cost is not UNSET:
            field_dict["PlannedExpenseCost"] = planned_expense_cost
        if planned_finish_date is not UNSET:
            field_dict["PlannedFinishDate"] = planned_finish_date
        if planned_labor_cost is not UNSET:
            field_dict["PlannedLaborCost"] = planned_labor_cost
        if planned_labor_units is not UNSET:
            field_dict["PlannedLaborUnits"] = planned_labor_units
        if planned_material_cost is not UNSET:
            field_dict["PlannedMaterialCost"] = planned_material_cost
        if planned_non_labor_cost is not UNSET:
            field_dict["PlannedNonLaborCost"] = planned_non_labor_cost
        if planned_non_labor_units is not UNSET:
            field_dict["PlannedNonLaborUnits"] = planned_non_labor_units
        if planned_start_date is not UNSET:
            field_dict["PlannedStartDate"] = planned_start_date
        if planned_total_cost is not UNSET:
            field_dict["PlannedTotalCost"] = planned_total_cost
        if planned_total_units is not UNSET:
            field_dict["PlannedTotalUnits"] = planned_total_units
        if planned_value_cost is not UNSET:
            field_dict["PlannedValueCost"] = planned_value_cost
        if planned_value_labor_units is not UNSET:
            field_dict["PlannedValueLaborUnits"] = planned_value_labor_units
        if post_resp_criticality_index is not UNSET:
            field_dict["PostRespCriticalityIndex"] = post_resp_criticality_index
        if post_response_pessimistic_finish is not UNSET:
            field_dict["PostResponsePessimisticFinish"] = post_response_pessimistic_finish
        if post_response_pessimistic_start is not UNSET:
            field_dict["PostResponsePessimisticStart"] = post_response_pessimistic_start
        if pre_resp_criticality_index is not UNSET:
            field_dict["PreRespCriticalityIndex"] = pre_resp_criticality_index
        if pre_response_pessimistic_finish is not UNSET:
            field_dict["PreResponsePessimisticFinish"] = pre_response_pessimistic_finish
        if pre_response_pessimistic_start is not UNSET:
            field_dict["PreResponsePessimisticStart"] = pre_response_pessimistic_start
        if primary_constraint_date is not UNSET:
            field_dict["PrimaryConstraintDate"] = primary_constraint_date
        if primary_constraint_type is not UNSET:
            field_dict["PrimaryConstraintType"] = primary_constraint_type
        if primary_resource_id is not UNSET:
            field_dict["PrimaryResourceId"] = primary_resource_id
        if primary_resource_name is not UNSET:
            field_dict["PrimaryResourceName"] = primary_resource_name
        if primary_resource_object_id is not UNSET:
            field_dict["PrimaryResourceObjectId"] = primary_resource_object_id
        if project_flag is not UNSET:
            field_dict["ProjectFlag"] = project_flag
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if project_name is not UNSET:
            field_dict["ProjectName"] = project_name
        if project_project_flag is not UNSET:
            field_dict["ProjectProjectFlag"] = project_project_flag
        if remaining_duration is not UNSET:
            field_dict["RemainingDuration"] = remaining_duration
        if remaining_early_finish_date is not UNSET:
            field_dict["RemainingEarlyFinishDate"] = remaining_early_finish_date
        if remaining_early_start_date is not UNSET:
            field_dict["RemainingEarlyStartDate"] = remaining_early_start_date
        if remaining_expense_cost is not UNSET:
            field_dict["RemainingExpenseCost"] = remaining_expense_cost
        if remaining_float is not UNSET:
            field_dict["RemainingFloat"] = remaining_float
        if remaining_labor_cost is not UNSET:
            field_dict["RemainingLaborCost"] = remaining_labor_cost
        if remaining_labor_units is not UNSET:
            field_dict["RemainingLaborUnits"] = remaining_labor_units
        if remaining_late_finish_date is not UNSET:
            field_dict["RemainingLateFinishDate"] = remaining_late_finish_date
        if remaining_late_start_date is not UNSET:
            field_dict["RemainingLateStartDate"] = remaining_late_start_date
        if remaining_material_cost is not UNSET:
            field_dict["RemainingMaterialCost"] = remaining_material_cost
        if remaining_non_labor_cost is not UNSET:
            field_dict["RemainingNonLaborCost"] = remaining_non_labor_cost
        if remaining_non_labor_units is not UNSET:
            field_dict["RemainingNonLaborUnits"] = remaining_non_labor_units
        if remaining_total_cost is not UNSET:
            field_dict["RemainingTotalCost"] = remaining_total_cost
        if remaining_total_units is not UNSET:
            field_dict["RemainingTotalUnits"] = remaining_total_units
        if resume_date is not UNSET:
            field_dict["ResumeDate"] = resume_date
        if review_finish_date is not UNSET:
            field_dict["ReviewFinishDate"] = review_finish_date
        if review_required is not UNSET:
            field_dict["ReviewRequired"] = review_required
        if review_status is not UNSET:
            field_dict["ReviewStatus"] = review_status
        if schedule_percent_complete is not UNSET:
            field_dict["SchedulePercentComplete"] = schedule_percent_complete
        if schedule_performance_index is not UNSET:
            field_dict["SchedulePerformanceIndex"] = schedule_performance_index
        if schedule_performance_index_labor_units is not UNSET:
            field_dict["SchedulePerformanceIndexLaborUnits"] = schedule_performance_index_labor_units
        if schedule_variance is not UNSET:
            field_dict["ScheduleVariance"] = schedule_variance
        if schedule_variance_index is not UNSET:
            field_dict["ScheduleVarianceIndex"] = schedule_variance_index
        if schedule_variance_index_labor_units is not UNSET:
            field_dict["ScheduleVarianceIndexLaborUnits"] = schedule_variance_index_labor_units
        if schedule_variance_labor_units is not UNSET:
            field_dict["ScheduleVarianceLaborUnits"] = schedule_variance_labor_units
        if scope_percent_complete is not UNSET:
            field_dict["ScopePercentComplete"] = scope_percent_complete
        if secondary_constraint_date is not UNSET:
            field_dict["SecondaryConstraintDate"] = secondary_constraint_date
        if secondary_constraint_type is not UNSET:
            field_dict["SecondaryConstraintType"] = secondary_constraint_type
        if start_date is not UNSET:
            field_dict["StartDate"] = start_date
        if start_date_1_variance is not UNSET:
            field_dict["StartDate1Variance"] = start_date_1_variance
        if start_date_variance is not UNSET:
            field_dict["StartDateVariance"] = start_date_variance
        if status is not UNSET:
            field_dict["Status"] = status
        if status_code is not UNSET:
            field_dict["StatusCode"] = status_code
        if suspend_date is not UNSET:
            field_dict["SuspendDate"] = suspend_date
        if task_status_completion is not UNSET:
            field_dict["TaskStatusCompletion"] = task_status_completion
        if task_status_dates is not UNSET:
            field_dict["TaskStatusDates"] = task_status_dates
        if task_status_indicator is not UNSET:
            field_dict["TaskStatusIndicator"] = task_status_indicator
        if to_complete_performance_index is not UNSET:
            field_dict["ToCompletePerformanceIndex"] = to_complete_performance_index
        if total_cost_1_variance is not UNSET:
            field_dict["TotalCost1Variance"] = total_cost_1_variance
        if total_cost_variance is not UNSET:
            field_dict["TotalCostVariance"] = total_cost_variance
        if total_float is not UNSET:
            field_dict["TotalFloat"] = total_float
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if units_percent_complete is not UNSET:
            field_dict["UnitsPercentComplete"] = units_percent_complete
        if unread_comment_count is not UNSET:
            field_dict["UnreadCommentCount"] = unread_comment_count
        if wbs_code is not UNSET:
            field_dict["WBSCode"] = wbs_code
        if wbs_name is not UNSET:
            field_dict["WBSName"] = wbs_name
        if wbs_name_path is not UNSET:
            field_dict["WBSNamePath"] = wbs_name_path
        if wbs_path is not UNSET:
            field_dict["WBSPath"] = wbs_path
        if work_package_id is not UNSET:
            field_dict["WorkPackageId"] = work_package_id
        if work_package_name is not UNSET:
            field_dict["WorkPackageName"] = work_package_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_object_id = d.pop("ProjectObjectId")

        wbs_object_id = d.pop("WBSObjectId")

        accounting_variance = d.pop("AccountingVariance", UNSET)

        accounting_variance_labor_units = d.pop("AccountingVarianceLaborUnits", UNSET)

        activity_owner_user_id = d.pop("ActivityOwnerUserId", UNSET)

        actual_duration = d.pop("ActualDuration", UNSET)

        actual_expense_cost = d.pop("ActualExpenseCost", UNSET)

        _actual_finish_date = d.pop("ActualFinishDate", UNSET)
        actual_finish_date: datetime.datetime | Unset
        if isinstance(_actual_finish_date, Unset):
            actual_finish_date = UNSET
        else:
            actual_finish_date = isoparse(_actual_finish_date)

        actual_labor_cost = d.pop("ActualLaborCost", UNSET)

        actual_labor_units = d.pop("ActualLaborUnits", UNSET)

        actual_material_cost = d.pop("ActualMaterialCost", UNSET)

        actual_non_labor_cost = d.pop("ActualNonLaborCost", UNSET)

        actual_non_labor_units = d.pop("ActualNonLaborUnits", UNSET)

        _actual_start_date = d.pop("ActualStartDate", UNSET)
        actual_start_date: datetime.datetime | Unset
        if isinstance(_actual_start_date, Unset):
            actual_start_date = UNSET
        else:
            actual_start_date = isoparse(_actual_start_date)

        actual_this_period_labor_cost = d.pop("ActualThisPeriodLaborCost", UNSET)

        actual_this_period_labor_units = d.pop("ActualThisPeriodLaborUnits", UNSET)

        actual_this_period_material_cost = d.pop("ActualThisPeriodMaterialCost", UNSET)

        actual_this_period_non_labor_cost = d.pop("ActualThisPeriodNonLaborCost", UNSET)

        actual_this_period_non_labor_units = d.pop("ActualThisPeriodNonLaborUnits", UNSET)

        actual_total_cost = d.pop("ActualTotalCost", UNSET)

        actual_total_units = d.pop("ActualTotalUnits", UNSET)

        at_completion_duration = d.pop("AtCompletionDuration", UNSET)

        at_completion_expense_cost = d.pop("AtCompletionExpenseCost", UNSET)

        at_completion_labor_cost = d.pop("AtCompletionLaborCost", UNSET)

        at_completion_labor_units = d.pop("AtCompletionLaborUnits", UNSET)

        at_completion_labor_units_variance = d.pop("AtCompletionLaborUnitsVariance", UNSET)

        at_completion_material_cost = d.pop("AtCompletionMaterialCost", UNSET)

        at_completion_non_labor_cost = d.pop("AtCompletionNonLaborCost", UNSET)

        at_completion_non_labor_units = d.pop("AtCompletionNonLaborUnits", UNSET)

        at_completion_total_cost = d.pop("AtCompletionTotalCost", UNSET)

        at_completion_total_units = d.pop("AtCompletionTotalUnits", UNSET)

        at_completion_variance = d.pop("AtCompletionVariance", UNSET)

        auto_compute_actuals = d.pop("AutoComputeActuals", UNSET)

        baseline_1_duration = d.pop("Baseline1Duration", UNSET)

        _baseline_1_finish_date = d.pop("Baseline1FinishDate", UNSET)
        baseline_1_finish_date: datetime.datetime | Unset
        if isinstance(_baseline_1_finish_date, Unset):
            baseline_1_finish_date = UNSET
        else:
            baseline_1_finish_date = isoparse(_baseline_1_finish_date)

        baseline_1_planned_duration = d.pop("Baseline1PlannedDuration", UNSET)

        baseline_1_planned_expense_cost = d.pop("Baseline1PlannedExpenseCost", UNSET)

        baseline_1_planned_labor_cost = d.pop("Baseline1PlannedLaborCost", UNSET)

        baseline_1_planned_labor_units = d.pop("Baseline1PlannedLaborUnits", UNSET)

        baseline_1_planned_material_cost = d.pop("Baseline1PlannedMaterialCost", UNSET)

        baseline_1_planned_non_labor_cost = d.pop("Baseline1PlannedNonLaborCost", UNSET)

        baseline_1_planned_non_labor_units = d.pop("Baseline1PlannedNonLaborUnits", UNSET)

        baseline_1_planned_total_cost = d.pop("Baseline1PlannedTotalCost", UNSET)

        _baseline_1_start_date = d.pop("Baseline1StartDate", UNSET)
        baseline_1_start_date: datetime.datetime | Unset
        if isinstance(_baseline_1_start_date, Unset):
            baseline_1_start_date = UNSET
        else:
            baseline_1_start_date = isoparse(_baseline_1_start_date)

        baseline_duration = d.pop("BaselineDuration", UNSET)

        _baseline_finish_date = d.pop("BaselineFinishDate", UNSET)
        baseline_finish_date: datetime.datetime | Unset
        if isinstance(_baseline_finish_date, Unset):
            baseline_finish_date = UNSET
        else:
            baseline_finish_date = isoparse(_baseline_finish_date)

        baseline_planned_duration = d.pop("BaselinePlannedDuration", UNSET)

        baseline_planned_expense_cost = d.pop("BaselinePlannedExpenseCost", UNSET)

        baseline_planned_labor_cost = d.pop("BaselinePlannedLaborCost", UNSET)

        baseline_planned_labor_units = d.pop("BaselinePlannedLaborUnits", UNSET)

        baseline_planned_material_cost = d.pop("BaselinePlannedMaterialCost", UNSET)

        baseline_planned_non_labor_cost = d.pop("BaselinePlannedNonLaborCost", UNSET)

        baseline_planned_non_labor_units = d.pop("BaselinePlannedNonLaborUnits", UNSET)

        baseline_planned_total_cost = d.pop("BaselinePlannedTotalCost", UNSET)

        _baseline_start_date = d.pop("BaselineStartDate", UNSET)
        baseline_start_date: datetime.datetime | Unset
        if isinstance(_baseline_start_date, Unset):
            baseline_start_date = UNSET
        else:
            baseline_start_date = isoparse(_baseline_start_date)

        budget_at_completion = d.pop("BudgetAtCompletion", UNSET)

        cbs_code = d.pop("CBSCode", UNSET)

        cbs_id = d.pop("CBSId", UNSET)

        cbs_object_id = d.pop("CBSObjectId", UNSET)

        calendar_name = d.pop("CalendarName", UNSET)

        calendar_object_id = d.pop("CalendarObjectId", UNSET)

        cost_percent_complete = d.pop("CostPercentComplete", UNSET)

        cost_percent_of_planned = d.pop("CostPercentOfPlanned", UNSET)

        cost_performance_index = d.pop("CostPerformanceIndex", UNSET)

        cost_performance_index_labor_units = d.pop("CostPerformanceIndexLaborUnits", UNSET)

        cost_variance = d.pop("CostVariance", UNSET)

        cost_variance_index = d.pop("CostVarianceIndex", UNSET)

        cost_variance_index_labor_units = d.pop("CostVarianceIndexLaborUnits", UNSET)

        cost_variance_labor_units = d.pop("CostVarianceLaborUnits", UNSET)

        _create_date = d.pop("CreateDate", UNSET)
        create_date: datetime.datetime | Unset
        if isinstance(_create_date, Unset):
            create_date = UNSET
        else:
            create_date = isoparse(_create_date)

        create_user = d.pop("CreateUser", UNSET)

        _data_date = d.pop("DataDate", UNSET)
        data_date: datetime.datetime | Unset
        if isinstance(_data_date, Unset):
            data_date = UNSET
        else:
            data_date = isoparse(_data_date)

        duration_1_variance = d.pop("Duration1Variance", UNSET)

        duration_percent_complete = d.pop("DurationPercentComplete", UNSET)

        duration_percent_of_planned = d.pop("DurationPercentOfPlanned", UNSET)

        duration_type = d.pop("DurationType", UNSET)

        duration_variance = d.pop("DurationVariance", UNSET)

        _early_finish_date = d.pop("EarlyFinishDate", UNSET)
        early_finish_date: datetime.datetime | Unset
        if isinstance(_early_finish_date, Unset):
            early_finish_date = UNSET
        else:
            early_finish_date = isoparse(_early_finish_date)

        _early_start_date = d.pop("EarlyStartDate", UNSET)
        early_start_date: datetime.datetime | Unset
        if isinstance(_early_start_date, Unset):
            early_start_date = UNSET
        else:
            early_start_date = isoparse(_early_start_date)

        earned_value_cost = d.pop("EarnedValueCost", UNSET)

        earned_value_labor_units = d.pop("EarnedValueLaborUnits", UNSET)

        estimate_at_completion_cost = d.pop("EstimateAtCompletionCost", UNSET)

        estimate_at_completion_labor_units = d.pop("EstimateAtCompletionLaborUnits", UNSET)

        estimate_to_complete = d.pop("EstimateToComplete", UNSET)

        estimate_to_complete_labor_units = d.pop("EstimateToCompleteLaborUnits", UNSET)

        estimated_weight = d.pop("EstimatedWeight", UNSET)

        _expected_finish_date = d.pop("ExpectedFinishDate", UNSET)
        expected_finish_date: datetime.datetime | Unset
        if isinstance(_expected_finish_date, Unset):
            expected_finish_date = UNSET
        else:
            expected_finish_date = isoparse(_expected_finish_date)

        expense_cost_1_variance = d.pop("ExpenseCost1Variance", UNSET)

        expense_cost_percent_complete = d.pop("ExpenseCostPercentComplete", UNSET)

        expense_cost_variance = d.pop("ExpenseCostVariance", UNSET)

        _external_early_start_date = d.pop("ExternalEarlyStartDate", UNSET)
        external_early_start_date: datetime.datetime | Unset
        if isinstance(_external_early_start_date, Unset):
            external_early_start_date = UNSET
        else:
            external_early_start_date = isoparse(_external_early_start_date)

        _external_late_finish_date = d.pop("ExternalLateFinishDate", UNSET)
        external_late_finish_date: datetime.datetime | Unset
        if isinstance(_external_late_finish_date, Unset):
            external_late_finish_date = UNSET
        else:
            external_late_finish_date = isoparse(_external_late_finish_date)

        feedback = d.pop("Feedback", UNSET)

        financial_period_tmpl_id = d.pop("FinancialPeriodTmplId", UNSET)

        _finish_date = d.pop("FinishDate", UNSET)
        finish_date: datetime.datetime | Unset
        if isinstance(_finish_date, Unset):
            finish_date = UNSET
        else:
            finish_date = isoparse(_finish_date)

        finish_date_1_variance = d.pop("FinishDate1Variance", UNSET)

        finish_date_variance = d.pop("FinishDateVariance", UNSET)

        float_path = d.pop("FloatPath", UNSET)

        float_path_order = d.pop("FloatPathOrder", UNSET)

        free_float = d.pop("FreeFloat", UNSET)

        guid = d.pop("GUID", UNSET)

        has_future_bucket_data = d.pop("HasFutureBucketData", UNSET)

        id = d.pop("Id", UNSET)

        is_baseline = d.pop("IsBaseline", UNSET)

        is_critical = d.pop("IsCritical", UNSET)

        is_longest_path = d.pop("IsLongestPath", UNSET)

        is_new_feedback = d.pop("IsNewFeedback", UNSET)

        is_starred = d.pop("IsStarred", UNSET)

        is_template = d.pop("IsTemplate", UNSET)

        is_work_package = d.pop("IsWorkPackage", UNSET)

        labor_cost_1_variance = d.pop("LaborCost1Variance", UNSET)

        labor_cost_percent_complete = d.pop("LaborCostPercentComplete", UNSET)

        labor_cost_variance = d.pop("LaborCostVariance", UNSET)

        labor_units_1_variance = d.pop("LaborUnits1Variance", UNSET)

        labor_units_percent_complete = d.pop("LaborUnitsPercentComplete", UNSET)

        labor_units_variance = d.pop("LaborUnitsVariance", UNSET)

        _last_update_date = d.pop("LastUpdateDate", UNSET)
        last_update_date: datetime.datetime | Unset
        if isinstance(_last_update_date, Unset):
            last_update_date = UNSET
        else:
            last_update_date = isoparse(_last_update_date)

        last_update_user = d.pop("LastUpdateUser", UNSET)

        _late_finish_date = d.pop("LateFinishDate", UNSET)
        late_finish_date: datetime.datetime | Unset
        if isinstance(_late_finish_date, Unset):
            late_finish_date = UNSET
        else:
            late_finish_date = isoparse(_late_finish_date)

        _late_start_date = d.pop("LateStartDate", UNSET)
        late_start_date: datetime.datetime | Unset
        if isinstance(_late_start_date, Unset):
            late_start_date = UNSET
        else:
            late_start_date = isoparse(_late_start_date)

        leveling_priority = d.pop("LevelingPriority", UNSET)

        location_name = d.pop("LocationName", UNSET)

        location_object_id = d.pop("LocationObjectId", UNSET)

        material_cost_1_variance = d.pop("MaterialCost1Variance", UNSET)

        material_cost_percent_complete = d.pop("MaterialCostPercentComplete", UNSET)

        material_cost_variance = d.pop("MaterialCostVariance", UNSET)

        maximum_duration = d.pop("MaximumDuration", UNSET)

        minimum_duration = d.pop("MinimumDuration", UNSET)

        most_likely_duration = d.pop("MostLikelyDuration", UNSET)

        name = d.pop("Name", UNSET)

        non_labor_cost_1_variance = d.pop("NonLaborCost1Variance", UNSET)

        non_labor_cost_percent_complete = d.pop("NonLaborCostPercentComplete", UNSET)

        non_labor_cost_variance = d.pop("NonLaborCostVariance", UNSET)

        non_labor_units_1_variance = d.pop("NonLaborUnits1Variance", UNSET)

        non_labor_units_percent_complete = d.pop("NonLaborUnitsPercentComplete", UNSET)

        non_labor_units_variance = d.pop("NonLaborUnitsVariance", UNSET)

        notes_to_resources = d.pop("NotesToResources", UNSET)

        object_id = d.pop("ObjectId", UNSET)

        owner_id_array = d.pop("OwnerIDArray", UNSET)

        owner_names_array = d.pop("OwnerNamesArray", UNSET)

        percent_complete = d.pop("PercentComplete", UNSET)

        percent_complete_type = d.pop("PercentCompleteType", UNSET)

        performance_percent_complete = d.pop("PerformancePercentComplete", UNSET)

        performance_percent_complete_by_labor_units = d.pop("PerformancePercentCompleteByLaborUnits", UNSET)

        physical_percent_complete = d.pop("PhysicalPercentComplete", UNSET)

        planned_duration = d.pop("PlannedDuration", UNSET)

        planned_expense_cost = d.pop("PlannedExpenseCost", UNSET)

        _planned_finish_date = d.pop("PlannedFinishDate", UNSET)
        planned_finish_date: datetime.datetime | Unset
        if isinstance(_planned_finish_date, Unset):
            planned_finish_date = UNSET
        else:
            planned_finish_date = isoparse(_planned_finish_date)

        planned_labor_cost = d.pop("PlannedLaborCost", UNSET)

        planned_labor_units = d.pop("PlannedLaborUnits", UNSET)

        planned_material_cost = d.pop("PlannedMaterialCost", UNSET)

        planned_non_labor_cost = d.pop("PlannedNonLaborCost", UNSET)

        planned_non_labor_units = d.pop("PlannedNonLaborUnits", UNSET)

        _planned_start_date = d.pop("PlannedStartDate", UNSET)
        planned_start_date: datetime.datetime | Unset
        if isinstance(_planned_start_date, Unset):
            planned_start_date = UNSET
        else:
            planned_start_date = isoparse(_planned_start_date)

        planned_total_cost = d.pop("PlannedTotalCost", UNSET)

        planned_total_units = d.pop("PlannedTotalUnits", UNSET)

        planned_value_cost = d.pop("PlannedValueCost", UNSET)

        planned_value_labor_units = d.pop("PlannedValueLaborUnits", UNSET)

        post_resp_criticality_index = d.pop("PostRespCriticalityIndex", UNSET)

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

        pre_resp_criticality_index = d.pop("PreRespCriticalityIndex", UNSET)

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

        _primary_constraint_date = d.pop("PrimaryConstraintDate", UNSET)
        primary_constraint_date: datetime.datetime | Unset
        if isinstance(_primary_constraint_date, Unset):
            primary_constraint_date = UNSET
        else:
            primary_constraint_date = isoparse(_primary_constraint_date)

        primary_constraint_type = d.pop("PrimaryConstraintType", UNSET)

        primary_resource_id = d.pop("PrimaryResourceId", UNSET)

        primary_resource_name = d.pop("PrimaryResourceName", UNSET)

        primary_resource_object_id = d.pop("PrimaryResourceObjectId", UNSET)

        project_flag = d.pop("ProjectFlag", UNSET)

        project_id = d.pop("ProjectId", UNSET)

        project_name = d.pop("ProjectName", UNSET)

        project_project_flag = d.pop("ProjectProjectFlag", UNSET)

        remaining_duration = d.pop("RemainingDuration", UNSET)

        _remaining_early_finish_date = d.pop("RemainingEarlyFinishDate", UNSET)
        remaining_early_finish_date: datetime.datetime | Unset
        if isinstance(_remaining_early_finish_date, Unset):
            remaining_early_finish_date = UNSET
        else:
            remaining_early_finish_date = isoparse(_remaining_early_finish_date)

        _remaining_early_start_date = d.pop("RemainingEarlyStartDate", UNSET)
        remaining_early_start_date: datetime.datetime | Unset
        if isinstance(_remaining_early_start_date, Unset):
            remaining_early_start_date = UNSET
        else:
            remaining_early_start_date = isoparse(_remaining_early_start_date)

        remaining_expense_cost = d.pop("RemainingExpenseCost", UNSET)

        remaining_float = d.pop("RemainingFloat", UNSET)

        remaining_labor_cost = d.pop("RemainingLaborCost", UNSET)

        remaining_labor_units = d.pop("RemainingLaborUnits", UNSET)

        _remaining_late_finish_date = d.pop("RemainingLateFinishDate", UNSET)
        remaining_late_finish_date: datetime.datetime | Unset
        if isinstance(_remaining_late_finish_date, Unset):
            remaining_late_finish_date = UNSET
        else:
            remaining_late_finish_date = isoparse(_remaining_late_finish_date)

        _remaining_late_start_date = d.pop("RemainingLateStartDate", UNSET)
        remaining_late_start_date: datetime.datetime | Unset
        if isinstance(_remaining_late_start_date, Unset):
            remaining_late_start_date = UNSET
        else:
            remaining_late_start_date = isoparse(_remaining_late_start_date)

        remaining_material_cost = d.pop("RemainingMaterialCost", UNSET)

        remaining_non_labor_cost = d.pop("RemainingNonLaborCost", UNSET)

        remaining_non_labor_units = d.pop("RemainingNonLaborUnits", UNSET)

        remaining_total_cost = d.pop("RemainingTotalCost", UNSET)

        remaining_total_units = d.pop("RemainingTotalUnits", UNSET)

        _resume_date = d.pop("ResumeDate", UNSET)
        resume_date: datetime.datetime | Unset
        if isinstance(_resume_date, Unset):
            resume_date = UNSET
        else:
            resume_date = isoparse(_resume_date)

        _review_finish_date = d.pop("ReviewFinishDate", UNSET)
        review_finish_date: datetime.datetime | Unset
        if isinstance(_review_finish_date, Unset):
            review_finish_date = UNSET
        else:
            review_finish_date = isoparse(_review_finish_date)

        review_required = d.pop("ReviewRequired", UNSET)

        review_status = d.pop("ReviewStatus", UNSET)

        schedule_percent_complete = d.pop("SchedulePercentComplete", UNSET)

        schedule_performance_index = d.pop("SchedulePerformanceIndex", UNSET)

        schedule_performance_index_labor_units = d.pop("SchedulePerformanceIndexLaborUnits", UNSET)

        schedule_variance = d.pop("ScheduleVariance", UNSET)

        schedule_variance_index = d.pop("ScheduleVarianceIndex", UNSET)

        schedule_variance_index_labor_units = d.pop("ScheduleVarianceIndexLaborUnits", UNSET)

        schedule_variance_labor_units = d.pop("ScheduleVarianceLaborUnits", UNSET)

        scope_percent_complete = d.pop("ScopePercentComplete", UNSET)

        _secondary_constraint_date = d.pop("SecondaryConstraintDate", UNSET)
        secondary_constraint_date: datetime.datetime | Unset
        if isinstance(_secondary_constraint_date, Unset):
            secondary_constraint_date = UNSET
        else:
            secondary_constraint_date = isoparse(_secondary_constraint_date)

        secondary_constraint_type = d.pop("SecondaryConstraintType", UNSET)

        _start_date = d.pop("StartDate", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        start_date_1_variance = d.pop("StartDate1Variance", UNSET)

        start_date_variance = d.pop("StartDateVariance", UNSET)

        status = d.pop("Status", UNSET)

        status_code = d.pop("StatusCode", UNSET)

        _suspend_date = d.pop("SuspendDate", UNSET)
        suspend_date: datetime.datetime | Unset
        if isinstance(_suspend_date, Unset):
            suspend_date = UNSET
        else:
            suspend_date = isoparse(_suspend_date)

        task_status_completion = d.pop("TaskStatusCompletion", UNSET)

        task_status_dates = d.pop("TaskStatusDates", UNSET)

        task_status_indicator = d.pop("TaskStatusIndicator", UNSET)

        to_complete_performance_index = d.pop("ToCompletePerformanceIndex", UNSET)

        total_cost_1_variance = d.pop("TotalCost1Variance", UNSET)

        total_cost_variance = d.pop("TotalCostVariance", UNSET)

        total_float = d.pop("TotalFloat", UNSET)

        type_ = d.pop("Type", UNSET)

        units_percent_complete = d.pop("UnitsPercentComplete", UNSET)

        unread_comment_count = d.pop("UnreadCommentCount", UNSET)

        wbs_code = d.pop("WBSCode", UNSET)

        wbs_name = d.pop("WBSName", UNSET)

        wbs_name_path = d.pop("WBSNamePath", UNSET)

        wbs_path = d.pop("WBSPath", UNSET)

        work_package_id = d.pop("WorkPackageId", UNSET)

        work_package_name = d.pop("WorkPackageName", UNSET)

        activity = cls(
            project_object_id=project_object_id,
            wbs_object_id=wbs_object_id,
            accounting_variance=accounting_variance,
            accounting_variance_labor_units=accounting_variance_labor_units,
            activity_owner_user_id=activity_owner_user_id,
            actual_duration=actual_duration,
            actual_expense_cost=actual_expense_cost,
            actual_finish_date=actual_finish_date,
            actual_labor_cost=actual_labor_cost,
            actual_labor_units=actual_labor_units,
            actual_material_cost=actual_material_cost,
            actual_non_labor_cost=actual_non_labor_cost,
            actual_non_labor_units=actual_non_labor_units,
            actual_start_date=actual_start_date,
            actual_this_period_labor_cost=actual_this_period_labor_cost,
            actual_this_period_labor_units=actual_this_period_labor_units,
            actual_this_period_material_cost=actual_this_period_material_cost,
            actual_this_period_non_labor_cost=actual_this_period_non_labor_cost,
            actual_this_period_non_labor_units=actual_this_period_non_labor_units,
            actual_total_cost=actual_total_cost,
            actual_total_units=actual_total_units,
            at_completion_duration=at_completion_duration,
            at_completion_expense_cost=at_completion_expense_cost,
            at_completion_labor_cost=at_completion_labor_cost,
            at_completion_labor_units=at_completion_labor_units,
            at_completion_labor_units_variance=at_completion_labor_units_variance,
            at_completion_material_cost=at_completion_material_cost,
            at_completion_non_labor_cost=at_completion_non_labor_cost,
            at_completion_non_labor_units=at_completion_non_labor_units,
            at_completion_total_cost=at_completion_total_cost,
            at_completion_total_units=at_completion_total_units,
            at_completion_variance=at_completion_variance,
            auto_compute_actuals=auto_compute_actuals,
            baseline_1_duration=baseline_1_duration,
            baseline_1_finish_date=baseline_1_finish_date,
            baseline_1_planned_duration=baseline_1_planned_duration,
            baseline_1_planned_expense_cost=baseline_1_planned_expense_cost,
            baseline_1_planned_labor_cost=baseline_1_planned_labor_cost,
            baseline_1_planned_labor_units=baseline_1_planned_labor_units,
            baseline_1_planned_material_cost=baseline_1_planned_material_cost,
            baseline_1_planned_non_labor_cost=baseline_1_planned_non_labor_cost,
            baseline_1_planned_non_labor_units=baseline_1_planned_non_labor_units,
            baseline_1_planned_total_cost=baseline_1_planned_total_cost,
            baseline_1_start_date=baseline_1_start_date,
            baseline_duration=baseline_duration,
            baseline_finish_date=baseline_finish_date,
            baseline_planned_duration=baseline_planned_duration,
            baseline_planned_expense_cost=baseline_planned_expense_cost,
            baseline_planned_labor_cost=baseline_planned_labor_cost,
            baseline_planned_labor_units=baseline_planned_labor_units,
            baseline_planned_material_cost=baseline_planned_material_cost,
            baseline_planned_non_labor_cost=baseline_planned_non_labor_cost,
            baseline_planned_non_labor_units=baseline_planned_non_labor_units,
            baseline_planned_total_cost=baseline_planned_total_cost,
            baseline_start_date=baseline_start_date,
            budget_at_completion=budget_at_completion,
            cbs_code=cbs_code,
            cbs_id=cbs_id,
            cbs_object_id=cbs_object_id,
            calendar_name=calendar_name,
            calendar_object_id=calendar_object_id,
            cost_percent_complete=cost_percent_complete,
            cost_percent_of_planned=cost_percent_of_planned,
            cost_performance_index=cost_performance_index,
            cost_performance_index_labor_units=cost_performance_index_labor_units,
            cost_variance=cost_variance,
            cost_variance_index=cost_variance_index,
            cost_variance_index_labor_units=cost_variance_index_labor_units,
            cost_variance_labor_units=cost_variance_labor_units,
            create_date=create_date,
            create_user=create_user,
            data_date=data_date,
            duration_1_variance=duration_1_variance,
            duration_percent_complete=duration_percent_complete,
            duration_percent_of_planned=duration_percent_of_planned,
            duration_type=duration_type,
            duration_variance=duration_variance,
            early_finish_date=early_finish_date,
            early_start_date=early_start_date,
            earned_value_cost=earned_value_cost,
            earned_value_labor_units=earned_value_labor_units,
            estimate_at_completion_cost=estimate_at_completion_cost,
            estimate_at_completion_labor_units=estimate_at_completion_labor_units,
            estimate_to_complete=estimate_to_complete,
            estimate_to_complete_labor_units=estimate_to_complete_labor_units,
            estimated_weight=estimated_weight,
            expected_finish_date=expected_finish_date,
            expense_cost_1_variance=expense_cost_1_variance,
            expense_cost_percent_complete=expense_cost_percent_complete,
            expense_cost_variance=expense_cost_variance,
            external_early_start_date=external_early_start_date,
            external_late_finish_date=external_late_finish_date,
            feedback=feedback,
            financial_period_tmpl_id=financial_period_tmpl_id,
            finish_date=finish_date,
            finish_date_1_variance=finish_date_1_variance,
            finish_date_variance=finish_date_variance,
            float_path=float_path,
            float_path_order=float_path_order,
            free_float=free_float,
            guid=guid,
            has_future_bucket_data=has_future_bucket_data,
            id=id,
            is_baseline=is_baseline,
            is_critical=is_critical,
            is_longest_path=is_longest_path,
            is_new_feedback=is_new_feedback,
            is_starred=is_starred,
            is_template=is_template,
            is_work_package=is_work_package,
            labor_cost_1_variance=labor_cost_1_variance,
            labor_cost_percent_complete=labor_cost_percent_complete,
            labor_cost_variance=labor_cost_variance,
            labor_units_1_variance=labor_units_1_variance,
            labor_units_percent_complete=labor_units_percent_complete,
            labor_units_variance=labor_units_variance,
            last_update_date=last_update_date,
            last_update_user=last_update_user,
            late_finish_date=late_finish_date,
            late_start_date=late_start_date,
            leveling_priority=leveling_priority,
            location_name=location_name,
            location_object_id=location_object_id,
            material_cost_1_variance=material_cost_1_variance,
            material_cost_percent_complete=material_cost_percent_complete,
            material_cost_variance=material_cost_variance,
            maximum_duration=maximum_duration,
            minimum_duration=minimum_duration,
            most_likely_duration=most_likely_duration,
            name=name,
            non_labor_cost_1_variance=non_labor_cost_1_variance,
            non_labor_cost_percent_complete=non_labor_cost_percent_complete,
            non_labor_cost_variance=non_labor_cost_variance,
            non_labor_units_1_variance=non_labor_units_1_variance,
            non_labor_units_percent_complete=non_labor_units_percent_complete,
            non_labor_units_variance=non_labor_units_variance,
            notes_to_resources=notes_to_resources,
            object_id=object_id,
            owner_id_array=owner_id_array,
            owner_names_array=owner_names_array,
            percent_complete=percent_complete,
            percent_complete_type=percent_complete_type,
            performance_percent_complete=performance_percent_complete,
            performance_percent_complete_by_labor_units=performance_percent_complete_by_labor_units,
            physical_percent_complete=physical_percent_complete,
            planned_duration=planned_duration,
            planned_expense_cost=planned_expense_cost,
            planned_finish_date=planned_finish_date,
            planned_labor_cost=planned_labor_cost,
            planned_labor_units=planned_labor_units,
            planned_material_cost=planned_material_cost,
            planned_non_labor_cost=planned_non_labor_cost,
            planned_non_labor_units=planned_non_labor_units,
            planned_start_date=planned_start_date,
            planned_total_cost=planned_total_cost,
            planned_total_units=planned_total_units,
            planned_value_cost=planned_value_cost,
            planned_value_labor_units=planned_value_labor_units,
            post_resp_criticality_index=post_resp_criticality_index,
            post_response_pessimistic_finish=post_response_pessimistic_finish,
            post_response_pessimistic_start=post_response_pessimistic_start,
            pre_resp_criticality_index=pre_resp_criticality_index,
            pre_response_pessimistic_finish=pre_response_pessimistic_finish,
            pre_response_pessimistic_start=pre_response_pessimistic_start,
            primary_constraint_date=primary_constraint_date,
            primary_constraint_type=primary_constraint_type,
            primary_resource_id=primary_resource_id,
            primary_resource_name=primary_resource_name,
            primary_resource_object_id=primary_resource_object_id,
            project_flag=project_flag,
            project_id=project_id,
            project_name=project_name,
            project_project_flag=project_project_flag,
            remaining_duration=remaining_duration,
            remaining_early_finish_date=remaining_early_finish_date,
            remaining_early_start_date=remaining_early_start_date,
            remaining_expense_cost=remaining_expense_cost,
            remaining_float=remaining_float,
            remaining_labor_cost=remaining_labor_cost,
            remaining_labor_units=remaining_labor_units,
            remaining_late_finish_date=remaining_late_finish_date,
            remaining_late_start_date=remaining_late_start_date,
            remaining_material_cost=remaining_material_cost,
            remaining_non_labor_cost=remaining_non_labor_cost,
            remaining_non_labor_units=remaining_non_labor_units,
            remaining_total_cost=remaining_total_cost,
            remaining_total_units=remaining_total_units,
            resume_date=resume_date,
            review_finish_date=review_finish_date,
            review_required=review_required,
            review_status=review_status,
            schedule_percent_complete=schedule_percent_complete,
            schedule_performance_index=schedule_performance_index,
            schedule_performance_index_labor_units=schedule_performance_index_labor_units,
            schedule_variance=schedule_variance,
            schedule_variance_index=schedule_variance_index,
            schedule_variance_index_labor_units=schedule_variance_index_labor_units,
            schedule_variance_labor_units=schedule_variance_labor_units,
            scope_percent_complete=scope_percent_complete,
            secondary_constraint_date=secondary_constraint_date,
            secondary_constraint_type=secondary_constraint_type,
            start_date=start_date,
            start_date_1_variance=start_date_1_variance,
            start_date_variance=start_date_variance,
            status=status,
            status_code=status_code,
            suspend_date=suspend_date,
            task_status_completion=task_status_completion,
            task_status_dates=task_status_dates,
            task_status_indicator=task_status_indicator,
            to_complete_performance_index=to_complete_performance_index,
            total_cost_1_variance=total_cost_1_variance,
            total_cost_variance=total_cost_variance,
            total_float=total_float,
            type_=type_,
            units_percent_complete=units_percent_complete,
            unread_comment_count=unread_comment_count,
            wbs_code=wbs_code,
            wbs_name=wbs_name,
            wbs_name_path=wbs_name_path,
            wbs_path=wbs_path,
            work_package_id=work_package_id,
            work_package_name=work_package_name,
        )

        activity.additional_properties = d
        return activity

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
