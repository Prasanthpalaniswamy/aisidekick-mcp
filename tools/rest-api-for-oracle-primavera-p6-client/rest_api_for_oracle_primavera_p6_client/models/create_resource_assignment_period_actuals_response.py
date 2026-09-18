from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateResourceAssignmentPeriodActualsResponse")


@_attrs_define
class CreateResourceAssignmentPeriodActualsResponse:
    """CreateResourceAssignmentPeriodActualsResponse Entity

    Attributes:
        financial_period_object_id (int | Unset): The unique ID of the associated financial period.
        resource_assignment_object_id (int | Unset): The unique ID of the associated resource assignment.
    """

    financial_period_object_id: int | Unset = UNSET
    resource_assignment_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        financial_period_object_id = self.financial_period_object_id

        resource_assignment_object_id = self.resource_assignment_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if financial_period_object_id is not UNSET:
            field_dict["FinancialPeriodObjectId"] = financial_period_object_id
        if resource_assignment_object_id is not UNSET:
            field_dict["ResourceAssignmentObjectId"] = resource_assignment_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        financial_period_object_id = d.pop("FinancialPeriodObjectId", UNSET)

        resource_assignment_object_id = d.pop("ResourceAssignmentObjectId", UNSET)

        create_resource_assignment_period_actuals_response = cls(
            financial_period_object_id=financial_period_object_id,
            resource_assignment_object_id=resource_assignment_object_id,
        )

        create_resource_assignment_period_actuals_response.additional_properties = d
        return create_resource_assignment_period_actuals_response

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
