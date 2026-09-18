from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_assignment_spread import ResourceAssignmentSpread


T = TypeVar("T", bound="UpdateResourceAssignmentSpread")


@_attrs_define
class UpdateResourceAssignmentSpread:
    """UpdateResourceAssignmentSpread Entity

    Attributes:
        period_type (str | Unset): Spread period type enumerations are used to specify the spread interval for EPS,
            project, WBS, Activity, and resource assignment spreads.
        resource_assignment_spread (list[ResourceAssignmentSpread] | Unset): The live resource assignment spread data.
    """

    period_type: str | Unset = UNSET
    resource_assignment_spread: list[ResourceAssignmentSpread] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period_type = self.period_type

        resource_assignment_spread: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.resource_assignment_spread, Unset):
            resource_assignment_spread = []
            for resource_assignment_spread_item_data in self.resource_assignment_spread:
                resource_assignment_spread_item = resource_assignment_spread_item_data.to_dict()
                resource_assignment_spread.append(resource_assignment_spread_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if period_type is not UNSET:
            field_dict["PeriodType"] = period_type
        if resource_assignment_spread is not UNSET:
            field_dict["ResourceAssignmentSpread"] = resource_assignment_spread

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_assignment_spread import ResourceAssignmentSpread

        d = dict(src_dict)
        period_type = d.pop("PeriodType", UNSET)

        _resource_assignment_spread = d.pop("ResourceAssignmentSpread", UNSET)
        resource_assignment_spread: list[ResourceAssignmentSpread] | Unset = UNSET
        if _resource_assignment_spread is not UNSET:
            resource_assignment_spread = []
            for resource_assignment_spread_item_data in _resource_assignment_spread:
                resource_assignment_spread_item = ResourceAssignmentSpread.from_dict(
                    resource_assignment_spread_item_data
                )

                resource_assignment_spread.append(resource_assignment_spread_item)

        update_resource_assignment_spread = cls(
            period_type=period_type,
            resource_assignment_spread=resource_assignment_spread,
        )

        update_resource_assignment_spread.additional_properties = d
        return update_resource_assignment_spread

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
