from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleOptions")


@_attrs_define
class ScheduleOptions:
    """ScheduleOptions Entity

    Attributes:
        calculate_float_based_on_finish_date (bool | Unset): The flag that indicates how each activity's float will be
            calculated with respect to other projects in the scheduling batch. This setting only has an effect when
            scheduling multiple projects at the same time. If true, each activity's float is calculated based on its
            project's ScheduledFinishDate. If false, then each activity's float is calculated based on the latest
            ScheduledFinishDate of all of the projects in the scheduling batch.
        compute_total_float_type (str | Unset): The method for calculating total float for all activities. Start Float
            is the difference between the early and late start dates (Start Float = Late Start - Early Start); Finish Float
            is the difference between the early and late finish dates (Finish Float = Late Finish - Early Finish); and
            Smallest of Start Float and Finish Float is the most critical float value.
        create_date (datetime.datetime | Unset): The date this schedule option was created.
        create_user (str | Unset): The name of the user that created this schedule option.
        critical_activity_float_threshold (float | Unset): The maximum float time for activities before they are marked
            critical.
        critical_activity_path_type (str | Unset): The critical path type, which indicates how critical path activities
            are identified for the project, based on either 'Critical Float' or 'Longest Path'.
        external_project_priority_limit (int | Unset):
        ignore_other_project_relationships (bool | Unset): The option used by the scheduler for treating activity
            relationships between projects when scheduling.
        include_external_res_ass (bool | Unset):
        last_update_date (datetime.datetime | Unset): The date this schedule option was last updated.
        last_update_user (str | Unset): The name of the user that last updated this schedule option.
        level_all_resources (bool | Unset):
        level_within_float (bool | Unset):
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
        min_float_to_preserve (int | Unset):
        multiple_float_paths_enabled (bool | Unset): The Boolean value that indicates whether multiple critical float
            paths (sequences of activities) should be calculated in the project schedule.
        multiple_float_paths_ending_activity_object_id (int | Unset): The activity in the WBS that you want to represent
            the end of the float paths. Typically, this will be a milestone activity or some other significant activity that
            has a start date or end date that cannot change. Note: if a value is not assigned, the module will choose an
            activity based on MultipleFloatPathsUseTotalFloat. If you are calculating multiple paths using Free Float, the
            module will choose the open-ended activity with the most critical Free Float. If you are calculating multiple
            paths using Total Float, the module will calculate the Total Float for all activity relationships, then choose
            the activity with the most critical Relationship Total Float.
        multiple_float_paths_ending_activity_short_name (str | Unset):
        multiple_float_paths_use_total_float (bool | Unset): The Boolean value that decides whether or not to use total
            float in multiple float path calculations.If True, then based on the activity you want the paths to end on, the
            module determines which predecessor activity has the most critical Relationship Total Float on the backward
            pass. The module repeats this process until an activity is reached that has no relationship. The module begins
            the forward pass from this activity and determines which successor activity has the most critical Relationship
            Successor Total Float. The module repeats this process until an activity is reached that has no relationship.
            These activities represent the most critical float path. The process begins again until the remaining sub-
            critical paths are calculated.If False, then critical float paths are defined based on longest path. The most
            critical path will be identical to the critical path that is derived when you choose to define critical
            activities as Longest Path in the General tab. In a multicalendar project, the longest path is calculated by
            identifying the activities that have an early finish equal to the latest calculated early finish for the project
            and tracing all driving relationships for those activities back to the project start date. After the most
            critical path is identified, the module will calculate the remaining sub-critical paths.
        out_of_sequence_schedule_type (str | Unset): The type of logic used to schedule the progressed activities:
            'Retained Logic', 'Progress Override', or 'Actual Dates'.
        over_allocation_percentage (float | Unset):
        preserve_scheduled_early_and_late_dates (bool | Unset):
        priority_list (str | Unset):
        project_id (str | Unset): The short code that uniquely identifies the project.
        project_object_id (int | Unset): The unique ID of the associated project.
        relationship_lag_calendar (str | Unset): The calendar used to calculate the lag between predecessors and
            successors for all activities. Valid values are 'Predecessor Activity Calendar', 'Successor Activity Calendar',
            '24 Hour Calendar', and 'Project Default Calendar'. If you do not select a calendar, the successor activity
            calendar is used.
        resource_list (str | Unset):
        start_to_start_lag_calculation_type (bool | Unset): he method used to calculate lag when a start-to-start
            relationship exists and the predecessor starts out of sequence. Actual Start sets the successor's start
            according to the time elapsed from the predecessor's actual start (the successor's start date is the data date
            plus any remaining lag). Early Start sets the successor's start according to the amount of work that the
            predecessor activity accomplishes (the expired lag is calculated as the number of work periods between the
            actual start and the data date, and the successor's start date is the predecessor's internal early start plus
            any remaining lag).
        use_expected_finish_dates (bool | Unset): The option used for setting activity finish dates as the expected
            finish dates when scheduling projects.
        user_name (str | Unset): The user's login name.
        user_object_id (int | Unset): The unique ID of the associated user.
    """

    calculate_float_based_on_finish_date: bool | Unset = UNSET
    compute_total_float_type: str | Unset = UNSET
    create_date: datetime.datetime | Unset = UNSET
    create_user: str | Unset = UNSET
    critical_activity_float_threshold: float | Unset = UNSET
    critical_activity_path_type: str | Unset = UNSET
    external_project_priority_limit: int | Unset = UNSET
    ignore_other_project_relationships: bool | Unset = UNSET
    include_external_res_ass: bool | Unset = UNSET
    last_update_date: datetime.datetime | Unset = UNSET
    last_update_user: str | Unset = UNSET
    level_all_resources: bool | Unset = UNSET
    level_within_float: bool | Unset = UNSET
    make_open_ended_activities_critical: bool | Unset = UNSET
    maximum_multiple_float_paths: int | Unset = UNSET
    min_float_to_preserve: int | Unset = UNSET
    multiple_float_paths_enabled: bool | Unset = UNSET
    multiple_float_paths_ending_activity_object_id: int | Unset = UNSET
    multiple_float_paths_ending_activity_short_name: str | Unset = UNSET
    multiple_float_paths_use_total_float: bool | Unset = UNSET
    out_of_sequence_schedule_type: str | Unset = UNSET
    over_allocation_percentage: float | Unset = UNSET
    preserve_scheduled_early_and_late_dates: bool | Unset = UNSET
    priority_list: str | Unset = UNSET
    project_id: str | Unset = UNSET
    project_object_id: int | Unset = UNSET
    relationship_lag_calendar: str | Unset = UNSET
    resource_list: str | Unset = UNSET
    start_to_start_lag_calculation_type: bool | Unset = UNSET
    use_expected_finish_dates: bool | Unset = UNSET
    user_name: str | Unset = UNSET
    user_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        calculate_float_based_on_finish_date = self.calculate_float_based_on_finish_date

        compute_total_float_type = self.compute_total_float_type

        create_date: str | Unset = UNSET
        if not isinstance(self.create_date, Unset):
            create_date = self.create_date.isoformat()

        create_user = self.create_user

        critical_activity_float_threshold = self.critical_activity_float_threshold

        critical_activity_path_type = self.critical_activity_path_type

        external_project_priority_limit = self.external_project_priority_limit

        ignore_other_project_relationships = self.ignore_other_project_relationships

        include_external_res_ass = self.include_external_res_ass

        last_update_date: str | Unset = UNSET
        if not isinstance(self.last_update_date, Unset):
            last_update_date = self.last_update_date.isoformat()

        last_update_user = self.last_update_user

        level_all_resources = self.level_all_resources

        level_within_float = self.level_within_float

        make_open_ended_activities_critical = self.make_open_ended_activities_critical

        maximum_multiple_float_paths = self.maximum_multiple_float_paths

        min_float_to_preserve = self.min_float_to_preserve

        multiple_float_paths_enabled = self.multiple_float_paths_enabled

        multiple_float_paths_ending_activity_object_id = self.multiple_float_paths_ending_activity_object_id

        multiple_float_paths_ending_activity_short_name = self.multiple_float_paths_ending_activity_short_name

        multiple_float_paths_use_total_float = self.multiple_float_paths_use_total_float

        out_of_sequence_schedule_type = self.out_of_sequence_schedule_type

        over_allocation_percentage = self.over_allocation_percentage

        preserve_scheduled_early_and_late_dates = self.preserve_scheduled_early_and_late_dates

        priority_list = self.priority_list

        project_id = self.project_id

        project_object_id = self.project_object_id

        relationship_lag_calendar = self.relationship_lag_calendar

        resource_list = self.resource_list

        start_to_start_lag_calculation_type = self.start_to_start_lag_calculation_type

        use_expected_finish_dates = self.use_expected_finish_dates

        user_name = self.user_name

        user_object_id = self.user_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if calculate_float_based_on_finish_date is not UNSET:
            field_dict["CalculateFloatBasedOnFinishDate"] = calculate_float_based_on_finish_date
        if compute_total_float_type is not UNSET:
            field_dict["ComputeTotalFloatType"] = compute_total_float_type
        if create_date is not UNSET:
            field_dict["CreateDate"] = create_date
        if create_user is not UNSET:
            field_dict["CreateUser"] = create_user
        if critical_activity_float_threshold is not UNSET:
            field_dict["CriticalActivityFloatThreshold"] = critical_activity_float_threshold
        if critical_activity_path_type is not UNSET:
            field_dict["CriticalActivityPathType"] = critical_activity_path_type
        if external_project_priority_limit is not UNSET:
            field_dict["ExternalProjectPriorityLimit"] = external_project_priority_limit
        if ignore_other_project_relationships is not UNSET:
            field_dict["IgnoreOtherProjectRelationships"] = ignore_other_project_relationships
        if include_external_res_ass is not UNSET:
            field_dict["IncludeExternalResAss"] = include_external_res_ass
        if last_update_date is not UNSET:
            field_dict["LastUpdateDate"] = last_update_date
        if last_update_user is not UNSET:
            field_dict["LastUpdateUser"] = last_update_user
        if level_all_resources is not UNSET:
            field_dict["LevelAllResources"] = level_all_resources
        if level_within_float is not UNSET:
            field_dict["LevelWithinFloat"] = level_within_float
        if make_open_ended_activities_critical is not UNSET:
            field_dict["MakeOpenEndedActivitiesCritical"] = make_open_ended_activities_critical
        if maximum_multiple_float_paths is not UNSET:
            field_dict["MaximumMultipleFloatPaths"] = maximum_multiple_float_paths
        if min_float_to_preserve is not UNSET:
            field_dict["MinFloatToPreserve"] = min_float_to_preserve
        if multiple_float_paths_enabled is not UNSET:
            field_dict["MultipleFloatPathsEnabled"] = multiple_float_paths_enabled
        if multiple_float_paths_ending_activity_object_id is not UNSET:
            field_dict["MultipleFloatPathsEndingActivityObjectId"] = multiple_float_paths_ending_activity_object_id
        if multiple_float_paths_ending_activity_short_name is not UNSET:
            field_dict["MultipleFloatPathsEndingActivityShortName"] = multiple_float_paths_ending_activity_short_name
        if multiple_float_paths_use_total_float is not UNSET:
            field_dict["MultipleFloatPathsUseTotalFloat"] = multiple_float_paths_use_total_float
        if out_of_sequence_schedule_type is not UNSET:
            field_dict["OutOfSequenceScheduleType"] = out_of_sequence_schedule_type
        if over_allocation_percentage is not UNSET:
            field_dict["OverAllocationPercentage"] = over_allocation_percentage
        if preserve_scheduled_early_and_late_dates is not UNSET:
            field_dict["PreserveScheduledEarlyAndLateDates"] = preserve_scheduled_early_and_late_dates
        if priority_list is not UNSET:
            field_dict["PriorityList"] = priority_list
        if project_id is not UNSET:
            field_dict["ProjectId"] = project_id
        if project_object_id is not UNSET:
            field_dict["ProjectObjectId"] = project_object_id
        if relationship_lag_calendar is not UNSET:
            field_dict["RelationshipLagCalendar"] = relationship_lag_calendar
        if resource_list is not UNSET:
            field_dict["ResourceList"] = resource_list
        if start_to_start_lag_calculation_type is not UNSET:
            field_dict["StartToStartLagCalculationType"] = start_to_start_lag_calculation_type
        if use_expected_finish_dates is not UNSET:
            field_dict["UseExpectedFinishDates"] = use_expected_finish_dates
        if user_name is not UNSET:
            field_dict["UserName"] = user_name
        if user_object_id is not UNSET:
            field_dict["UserObjectId"] = user_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        calculate_float_based_on_finish_date = d.pop("CalculateFloatBasedOnFinishDate", UNSET)

        compute_total_float_type = d.pop("ComputeTotalFloatType", UNSET)

        _create_date = d.pop("CreateDate", UNSET)
        create_date: datetime.datetime | Unset
        if isinstance(_create_date, Unset):
            create_date = UNSET
        else:
            create_date = isoparse(_create_date)

        create_user = d.pop("CreateUser", UNSET)

        critical_activity_float_threshold = d.pop("CriticalActivityFloatThreshold", UNSET)

        critical_activity_path_type = d.pop("CriticalActivityPathType", UNSET)

        external_project_priority_limit = d.pop("ExternalProjectPriorityLimit", UNSET)

        ignore_other_project_relationships = d.pop("IgnoreOtherProjectRelationships", UNSET)

        include_external_res_ass = d.pop("IncludeExternalResAss", UNSET)

        _last_update_date = d.pop("LastUpdateDate", UNSET)
        last_update_date: datetime.datetime | Unset
        if isinstance(_last_update_date, Unset):
            last_update_date = UNSET
        else:
            last_update_date = isoparse(_last_update_date)

        last_update_user = d.pop("LastUpdateUser", UNSET)

        level_all_resources = d.pop("LevelAllResources", UNSET)

        level_within_float = d.pop("LevelWithinFloat", UNSET)

        make_open_ended_activities_critical = d.pop("MakeOpenEndedActivitiesCritical", UNSET)

        maximum_multiple_float_paths = d.pop("MaximumMultipleFloatPaths", UNSET)

        min_float_to_preserve = d.pop("MinFloatToPreserve", UNSET)

        multiple_float_paths_enabled = d.pop("MultipleFloatPathsEnabled", UNSET)

        multiple_float_paths_ending_activity_object_id = d.pop("MultipleFloatPathsEndingActivityObjectId", UNSET)

        multiple_float_paths_ending_activity_short_name = d.pop("MultipleFloatPathsEndingActivityShortName", UNSET)

        multiple_float_paths_use_total_float = d.pop("MultipleFloatPathsUseTotalFloat", UNSET)

        out_of_sequence_schedule_type = d.pop("OutOfSequenceScheduleType", UNSET)

        over_allocation_percentage = d.pop("OverAllocationPercentage", UNSET)

        preserve_scheduled_early_and_late_dates = d.pop("PreserveScheduledEarlyAndLateDates", UNSET)

        priority_list = d.pop("PriorityList", UNSET)

        project_id = d.pop("ProjectId", UNSET)

        project_object_id = d.pop("ProjectObjectId", UNSET)

        relationship_lag_calendar = d.pop("RelationshipLagCalendar", UNSET)

        resource_list = d.pop("ResourceList", UNSET)

        start_to_start_lag_calculation_type = d.pop("StartToStartLagCalculationType", UNSET)

        use_expected_finish_dates = d.pop("UseExpectedFinishDates", UNSET)

        user_name = d.pop("UserName", UNSET)

        user_object_id = d.pop("UserObjectId", UNSET)

        schedule_options = cls(
            calculate_float_based_on_finish_date=calculate_float_based_on_finish_date,
            compute_total_float_type=compute_total_float_type,
            create_date=create_date,
            create_user=create_user,
            critical_activity_float_threshold=critical_activity_float_threshold,
            critical_activity_path_type=critical_activity_path_type,
            external_project_priority_limit=external_project_priority_limit,
            ignore_other_project_relationships=ignore_other_project_relationships,
            include_external_res_ass=include_external_res_ass,
            last_update_date=last_update_date,
            last_update_user=last_update_user,
            level_all_resources=level_all_resources,
            level_within_float=level_within_float,
            make_open_ended_activities_critical=make_open_ended_activities_critical,
            maximum_multiple_float_paths=maximum_multiple_float_paths,
            min_float_to_preserve=min_float_to_preserve,
            multiple_float_paths_enabled=multiple_float_paths_enabled,
            multiple_float_paths_ending_activity_object_id=multiple_float_paths_ending_activity_object_id,
            multiple_float_paths_ending_activity_short_name=multiple_float_paths_ending_activity_short_name,
            multiple_float_paths_use_total_float=multiple_float_paths_use_total_float,
            out_of_sequence_schedule_type=out_of_sequence_schedule_type,
            over_allocation_percentage=over_allocation_percentage,
            preserve_scheduled_early_and_late_dates=preserve_scheduled_early_and_late_dates,
            priority_list=priority_list,
            project_id=project_id,
            project_object_id=project_object_id,
            relationship_lag_calendar=relationship_lag_calendar,
            resource_list=resource_list,
            start_to_start_lag_calculation_type=start_to_start_lag_calculation_type,
            use_expected_finish_dates=use_expected_finish_dates,
            user_name=user_name,
            user_object_id=user_object_id,
        )

        schedule_options.additional_properties = d
        return schedule_options

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
