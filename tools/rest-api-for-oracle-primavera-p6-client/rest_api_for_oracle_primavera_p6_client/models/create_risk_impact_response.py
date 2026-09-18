from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateRiskImpactResponse")


@_attrs_define
class CreateRiskImpactResponse:
    """CreateRiskImpactResponse Entity

    Attributes:
        risk_object_id (int | Unset): The unique ID of the associated risk.
        risk_threshold_object_id (int | Unset): The unique ID of the associated Risk Threshold Type.
    """

    risk_object_id: int | Unset = UNSET
    risk_threshold_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        risk_object_id = self.risk_object_id

        risk_threshold_object_id = self.risk_threshold_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if risk_object_id is not UNSET:
            field_dict["RiskObjectId"] = risk_object_id
        if risk_threshold_object_id is not UNSET:
            field_dict["RiskThresholdObjectId"] = risk_threshold_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        risk_object_id = d.pop("RiskObjectId", UNSET)

        risk_threshold_object_id = d.pop("RiskThresholdObjectId", UNSET)

        create_risk_impact_response = cls(
            risk_object_id=risk_object_id,
            risk_threshold_object_id=risk_threshold_object_id,
        )

        create_risk_impact_response.additional_properties = d
        return create_risk_impact_response

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
