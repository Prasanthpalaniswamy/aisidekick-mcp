from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleCheckOption")


@_attrs_define
class ScheduleCheckOption:
    """ScheduleCheckOption Entity

    Attributes:
        check_bei_tripwire (bool | Unset): The baseline execution index.
        check_hard_constraints (bool | Unset): Checks for the constraints that prevent activities from being moved.
        check_invalid_progress (bool | Unset): Checks for activities that have invalid progress dates.
        check_lags (bool | Unset): Checks for relationships that have a positive lag duration.
        check_large_durations (bool | Unset): Checks for activities that have a remaining duration that is greater than
            the specified LargeDurationCriteria value..
        check_large_float (bool | Unset): Checks for activities that have a float value greater than the specified
            LargeFloatCriteria value.
        check_late_activities (bool | Unset): Checks for activities that are scheduled to finish later than the project
            baseline.
        check_logic (bool | Unset): Checks for activities with missing predecessors or successors.
        check_long_lags (bool | Unset): Checks for relationships that have a lag duration that is greater than the
            specified LongLagsCriteria value.
        check_negative_float (bool | Unset): Checks for activities that have a total float less than 0.
        check_negative_lags (bool | Unset): Checks for relationships that have a lag duration less than 0.
        check_relation_ships (bool | Unset): Checks for the relationships that are set
        check_resources (bool | Unset): Checks for activities that do not have an expense or an assigned resource.
        check_soft_constraints (bool | Unset): Checks for constraints that do not prevent activities from being moved.
        hard_constraint_target (int | Unset): Checks for constraints that prevent activities from being moved.
        lags_target (int | Unset): Relationships that have a positive lag duration.
        large_duration_criteria (int | Unset): The value of the Large Duration Criteria.
        large_duration_target (int | Unset): Activities that have a remaining duration greater than the Large Duration
            Criteria.
        large_float_criteria (int | Unset): The value of the Large Float Criteria.
        large_float_target (int | Unset): Activities that have a total float greater than the Large Float Criteria.
        late_activities_target (int | Unset): Activities that are scheduled to finish later than the project baseline.
        logic_target (int | Unset): Activities that are missing predecessors or successors.
        long_lags_criteria (int | Unset): The value of the Long Lags Criteria.
        long_lags_target (int | Unset): Relationships that have a lag duration greater than the Long Lags Criteria.
        negative_float_target (int | Unset): Activities that have a total float less than 0.
        negative_lags_target (int | Unset): Relationships that have a lag duration less than 0.
        progress_date_target (int | Unset): Activities that have invalid progress dates.
        proj_prop_type_int (int | Unset): The enum values that are associated with the Project Property Type.
        project_object_id (int | Unset): The unique identifier of the project which has a schedule you want to check.
        prop_value (str | Unset): The Project Property Type value.
        relationship_target (int | Unset): The relationships that are finish to start.
        resources_target (int | Unset): Activities that do not have an expense or an assigned resource.
        schedule_check_data (str | Unset): The ScheduleCheck data.
        schedule_check_options_id (int | Unset): The unique id for ScheduleCheckOptions.
        soft_constraint_target (int | Unset): Constraints that do not prevent activities from being moved.
        bei_tripwire_target (float | Unset): The baseline execution index.
    """

    check_bei_tripwire: bool | Unset = UNSET
    check_hard_constraints: bool | Unset = UNSET
    check_invalid_progress: bool | Unset = UNSET
    check_lags: bool | Unset = UNSET
    check_large_durations: bool | Unset = UNSET
    check_large_float: bool | Unset = UNSET
    check_late_activities: bool | Unset = UNSET
    check_logic: bool | Unset = UNSET
    check_long_lags: bool | Unset = UNSET
    check_negative_float: bool | Unset = UNSET
    check_negative_lags: bool | Unset = UNSET
    check_relation_ships: bool | Unset = UNSET
    check_resources: bool | Unset = UNSET
    check_soft_constraints: bool | Unset = UNSET
    hard_constraint_target: int | Unset = UNSET
    lags_target: int | Unset = UNSET
    large_duration_criteria: int | Unset = UNSET
    large_duration_target: int | Unset = UNSET
    large_float_criteria: int | Unset = UNSET
    large_float_target: int | Unset = UNSET
    late_activities_target: int | Unset = UNSET
    logic_target: int | Unset = UNSET
    long_lags_criteria: int | Unset = UNSET
    long_lags_target: int | Unset = UNSET
    negative_float_target: int | Unset = UNSET
    negative_lags_target: int | Unset = UNSET
    progress_date_target: int | Unset = UNSET
    proj_prop_type_int: int | Unset = UNSET
    project_object_id: int | Unset = UNSET
    prop_value: str | Unset = UNSET
    relationship_target: int | Unset = UNSET
    resources_target: int | Unset = UNSET
    schedule_check_data: str | Unset = UNSET
    schedule_check_options_id: int | Unset = UNSET
    soft_constraint_target: int | Unset = UNSET
    bei_tripwire_target: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        check_bei_tripwire = self.check_bei_tripwire

        check_hard_constraints = self.check_hard_constraints

        check_invalid_progress = self.check_invalid_progress

        check_lags = self.check_lags

        check_large_durations = self.check_large_durations

        check_large_float = self.check_large_float

        check_late_activities = self.check_late_activities

        check_logic = self.check_logic

        check_long_lags = self.check_long_lags

        check_negative_float = self.check_negative_float

        check_negative_lags = self.check_negative_lags

        check_relation_ships = self.check_relation_ships

        check_resources = self.check_resources

        check_soft_constraints = self.check_soft_constraints

        hard_constraint_target = self.hard_constraint_target

        lags_target = self.lags_target

        large_duration_criteria = self.large_duration_criteria

        large_duration_target = self.large_duration_target

        large_float_criteria = self.large_float_criteria

        large_float_target = self.large_float_target

        late_activities_target = self.late_activities_target

        logic_target = self.logic_target

        long_lags_criteria = self.long_lags_criteria

        long_lags_target = self.long_lags_target

        negative_float_target = self.negative_float_target

        negative_lags_target = self.negative_lags_target

        progress_date_target = self.progress_date_target

        proj_prop_type_int = self.proj_prop_type_int

        project_object_id = self.project_object_id

        prop_value = self.prop_value

        relationship_target = self.relationship_target

        resources_target = self.resources_target

        schedule_check_data = self.schedule_check_data

        schedule_check_options_id = self.schedule_check_options_id

        soft_constraint_target = self.soft_constraint_target

        bei_tripwire_target = self.bei_tripwire_target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if check_bei_tripwire is not UNSET:
            field_dict["CheckBEITripwire"] = check_bei_tripwire
        if check_hard_constraints is not UNSET:
            field_dict["CheckHardConstraints"] = check_hard_constraints
        if check_invalid_progress is not UNSET:
            field_dict["CheckInvalidProgress"] = check_invalid_progress
        if check_lags is not UNSET:
            field_dict["CheckLags"] = check_lags
        if check_large_durations is not UNSET:
            field_dict["CheckLargeDurations"] = check_large_durations
        if check_large_float is not UNSET:
            field_dict["CheckLargeFloat"] = check_large_float
        if check_late_activities is not UNSET:
            field_dict["CheckLateActivities"] = check_late_activities
        if check_logic is not UNSET:
            field_dict["CheckLogic"] = check_logic
        if check_long_lags is not UNSET:
            field_dict["CheckLongLags"] = check_long_lags
        if check_negative_float is not UNSET:
            field_dict["CheckNegativeFloat"] = check_negative_float
        if check_negative_lags is not UNSET:
            field_dict["CheckNegativeLags"] = check_negative_lags
        if check_relation_ships is not UNSET:
            field_dict["CheckRelationShips"] = check_relation_ships
        if check_resources is not UNSET:
            field_dict["CheckResources"] = check_resources
        if check_soft_constraints is not UNSET:
            field_dict["CheckSoftConstraints"] = check_soft_constraints
        if hard_constraint_target is not UNSET:
            field_dict["HardConstraintTarget"] = hard_constraint_target
        if lags_target is not UNSET:
            field_dict["LagsTarget"] = lags_target
        if large_duration_criteria is not UNSET:
            field_dict["LargeDurationCriteria"] = large_duration_criteria
        if large_duration_target is not UNSET:
            field_dict["LargeDurationTarget"] = large_duration_target
        if large_float_criteria is not UNSET:
            field_dict["LargeFloatCriteria"] = large_float_criteria
        if large_float_target is not UNSET:
            field_dict["LargeFloatTarget"] = large_float_target
        if late_activities_target is not UNSET:
            field_dict["LateActivitiesTarget"] = late_activities_target
        if logic_target is not UNSET:
            field_dict["LogicTarget"] = logic_target
        if long_lags_criteria is not UNSET:
            field_dict["LongLagsCriteria"] = long_lags_criteria
        if long_lags_target is not UNSET:
            field_dict["LongLagsTarget"] = long_lags_target
        if negative_float_target is not UNSET:
            field_dict["NegativeFloatTarget"] = negative_float_target
        if negative_lags_target is not UNSET:
            field_dict["NegativeLagsTarget"] = negative_lags_target
        if progress_date_target is not UNSET:
            field_dict["ProgressDateTarget"] = progress_date_target
        if proj_prop_type_int is not UNSET:
            field_dict["ProjPropTypeInt"] = proj_prop_type_int
        if project_object_id is not UNSET:
            field_dict["ProjectObjectId"] = project_object_id
        if prop_value is not UNSET:
            field_dict["PropValue"] = prop_value
        if relationship_target is not UNSET:
            field_dict["RelationshipTarget"] = relationship_target
        if resources_target is not UNSET:
            field_dict["ResourcesTarget"] = resources_target
        if schedule_check_data is not UNSET:
            field_dict["ScheduleCheckData"] = schedule_check_data
        if schedule_check_options_id is not UNSET:
            field_dict["ScheduleCheckOptionsId"] = schedule_check_options_id
        if soft_constraint_target is not UNSET:
            field_dict["SoftConstraintTarget"] = soft_constraint_target
        if bei_tripwire_target is not UNSET:
            field_dict["BEITripwireTarget"] = bei_tripwire_target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        check_bei_tripwire = d.pop("CheckBEITripwire", UNSET)

        check_hard_constraints = d.pop("CheckHardConstraints", UNSET)

        check_invalid_progress = d.pop("CheckInvalidProgress", UNSET)

        check_lags = d.pop("CheckLags", UNSET)

        check_large_durations = d.pop("CheckLargeDurations", UNSET)

        check_large_float = d.pop("CheckLargeFloat", UNSET)

        check_late_activities = d.pop("CheckLateActivities", UNSET)

        check_logic = d.pop("CheckLogic", UNSET)

        check_long_lags = d.pop("CheckLongLags", UNSET)

        check_negative_float = d.pop("CheckNegativeFloat", UNSET)

        check_negative_lags = d.pop("CheckNegativeLags", UNSET)

        check_relation_ships = d.pop("CheckRelationShips", UNSET)

        check_resources = d.pop("CheckResources", UNSET)

        check_soft_constraints = d.pop("CheckSoftConstraints", UNSET)

        hard_constraint_target = d.pop("HardConstraintTarget", UNSET)

        lags_target = d.pop("LagsTarget", UNSET)

        large_duration_criteria = d.pop("LargeDurationCriteria", UNSET)

        large_duration_target = d.pop("LargeDurationTarget", UNSET)

        large_float_criteria = d.pop("LargeFloatCriteria", UNSET)

        large_float_target = d.pop("LargeFloatTarget", UNSET)

        late_activities_target = d.pop("LateActivitiesTarget", UNSET)

        logic_target = d.pop("LogicTarget", UNSET)

        long_lags_criteria = d.pop("LongLagsCriteria", UNSET)

        long_lags_target = d.pop("LongLagsTarget", UNSET)

        negative_float_target = d.pop("NegativeFloatTarget", UNSET)

        negative_lags_target = d.pop("NegativeLagsTarget", UNSET)

        progress_date_target = d.pop("ProgressDateTarget", UNSET)

        proj_prop_type_int = d.pop("ProjPropTypeInt", UNSET)

        project_object_id = d.pop("ProjectObjectId", UNSET)

        prop_value = d.pop("PropValue", UNSET)

        relationship_target = d.pop("RelationshipTarget", UNSET)

        resources_target = d.pop("ResourcesTarget", UNSET)

        schedule_check_data = d.pop("ScheduleCheckData", UNSET)

        schedule_check_options_id = d.pop("ScheduleCheckOptionsId", UNSET)

        soft_constraint_target = d.pop("SoftConstraintTarget", UNSET)

        bei_tripwire_target = d.pop("BEITripwireTarget", UNSET)

        schedule_check_option = cls(
            check_bei_tripwire=check_bei_tripwire,
            check_hard_constraints=check_hard_constraints,
            check_invalid_progress=check_invalid_progress,
            check_lags=check_lags,
            check_large_durations=check_large_durations,
            check_large_float=check_large_float,
            check_late_activities=check_late_activities,
            check_logic=check_logic,
            check_long_lags=check_long_lags,
            check_negative_float=check_negative_float,
            check_negative_lags=check_negative_lags,
            check_relation_ships=check_relation_ships,
            check_resources=check_resources,
            check_soft_constraints=check_soft_constraints,
            hard_constraint_target=hard_constraint_target,
            lags_target=lags_target,
            large_duration_criteria=large_duration_criteria,
            large_duration_target=large_duration_target,
            large_float_criteria=large_float_criteria,
            large_float_target=large_float_target,
            late_activities_target=late_activities_target,
            logic_target=logic_target,
            long_lags_criteria=long_lags_criteria,
            long_lags_target=long_lags_target,
            negative_float_target=negative_float_target,
            negative_lags_target=negative_lags_target,
            progress_date_target=progress_date_target,
            proj_prop_type_int=proj_prop_type_int,
            project_object_id=project_object_id,
            prop_value=prop_value,
            relationship_target=relationship_target,
            resources_target=resources_target,
            schedule_check_data=schedule_check_data,
            schedule_check_options_id=schedule_check_options_id,
            soft_constraint_target=soft_constraint_target,
            bei_tripwire_target=bei_tripwire_target,
        )

        schedule_check_option.additional_properties = d
        return schedule_check_option

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
