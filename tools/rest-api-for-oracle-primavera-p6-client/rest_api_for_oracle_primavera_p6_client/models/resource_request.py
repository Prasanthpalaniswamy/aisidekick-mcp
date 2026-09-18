from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_request_criterion import ResourceRequestCriterion


T = TypeVar("T", bound="ResourceRequest")


@_attrs_define
class ResourceRequest:
    """
    Attributes:
        finish_date (datetime.datetime | Unset):
        match_all_criteria (bool | Unset):
        name (str | Unset):
        requested_units (float | Unset):
        sequence_number (int | Unset):
        show_only_labor_resources (bool | Unset):
        show_overallocated_resources (bool | Unset):
        sort_results_by_availability (bool | Unset):
        start_date (datetime.datetime | Unset):
        use_activity_dates (bool | Unset):
        resource_request_criterion (list[ResourceRequestCriterion] | Unset):
    """

    finish_date: datetime.datetime | Unset = UNSET
    match_all_criteria: bool | Unset = UNSET
    name: str | Unset = UNSET
    requested_units: float | Unset = UNSET
    sequence_number: int | Unset = UNSET
    show_only_labor_resources: bool | Unset = UNSET
    show_overallocated_resources: bool | Unset = UNSET
    sort_results_by_availability: bool | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    use_activity_dates: bool | Unset = UNSET
    resource_request_criterion: list[ResourceRequestCriterion] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        finish_date: str | Unset = UNSET
        if not isinstance(self.finish_date, Unset):
            finish_date = self.finish_date.isoformat()

        match_all_criteria = self.match_all_criteria

        name = self.name

        requested_units = self.requested_units

        sequence_number = self.sequence_number

        show_only_labor_resources = self.show_only_labor_resources

        show_overallocated_resources = self.show_overallocated_resources

        sort_results_by_availability = self.sort_results_by_availability

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        use_activity_dates = self.use_activity_dates

        resource_request_criterion: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.resource_request_criterion, Unset):
            resource_request_criterion = []
            for resource_request_criterion_item_data in self.resource_request_criterion:
                resource_request_criterion_item = resource_request_criterion_item_data.to_dict()
                resource_request_criterion.append(resource_request_criterion_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if finish_date is not UNSET:
            field_dict["FinishDate"] = finish_date
        if match_all_criteria is not UNSET:
            field_dict["MatchAllCriteria"] = match_all_criteria
        if name is not UNSET:
            field_dict["Name"] = name
        if requested_units is not UNSET:
            field_dict["RequestedUnits"] = requested_units
        if sequence_number is not UNSET:
            field_dict["SequenceNumber"] = sequence_number
        if show_only_labor_resources is not UNSET:
            field_dict["ShowOnlyLaborResources"] = show_only_labor_resources
        if show_overallocated_resources is not UNSET:
            field_dict["ShowOverallocatedResources"] = show_overallocated_resources
        if sort_results_by_availability is not UNSET:
            field_dict["SortResultsByAvailability"] = sort_results_by_availability
        if start_date is not UNSET:
            field_dict["StartDate"] = start_date
        if use_activity_dates is not UNSET:
            field_dict["UseActivityDates"] = use_activity_dates
        if resource_request_criterion is not UNSET:
            field_dict["ResourceRequestCriterion"] = resource_request_criterion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_request_criterion import ResourceRequestCriterion

        d = dict(src_dict)
        _finish_date = d.pop("FinishDate", UNSET)
        finish_date: datetime.datetime | Unset
        if isinstance(_finish_date, Unset):
            finish_date = UNSET
        else:
            finish_date = isoparse(_finish_date)

        match_all_criteria = d.pop("MatchAllCriteria", UNSET)

        name = d.pop("Name", UNSET)

        requested_units = d.pop("RequestedUnits", UNSET)

        sequence_number = d.pop("SequenceNumber", UNSET)

        show_only_labor_resources = d.pop("ShowOnlyLaborResources", UNSET)

        show_overallocated_resources = d.pop("ShowOverallocatedResources", UNSET)

        sort_results_by_availability = d.pop("SortResultsByAvailability", UNSET)

        _start_date = d.pop("StartDate", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        use_activity_dates = d.pop("UseActivityDates", UNSET)

        _resource_request_criterion = d.pop("ResourceRequestCriterion", UNSET)
        resource_request_criterion: list[ResourceRequestCriterion] | Unset = UNSET
        if _resource_request_criterion is not UNSET:
            resource_request_criterion = []
            for resource_request_criterion_item_data in _resource_request_criterion:
                resource_request_criterion_item = ResourceRequestCriterion.from_dict(
                    resource_request_criterion_item_data
                )

                resource_request_criterion.append(resource_request_criterion_item)

        resource_request = cls(
            finish_date=finish_date,
            match_all_criteria=match_all_criteria,
            name=name,
            requested_units=requested_units,
            sequence_number=sequence_number,
            show_only_labor_resources=show_only_labor_resources,
            show_overallocated_resources=show_overallocated_resources,
            sort_results_by_availability=sort_results_by_availability,
            start_date=start_date,
            use_activity_dates=use_activity_dates,
            resource_request_criterion=resource_request_criterion,
        )

        resource_request.additional_properties = d
        return resource_request

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
