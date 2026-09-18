from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Values")


@_attrs_define
class Values:
    """
    Attributes:
        value_0 (float | Unset):
        value_5 (float | Unset):
        value_10 (float | Unset):
        value_15 (float | Unset):
        value_20 (float | Unset):
        value_25 (float | Unset):
        value_30 (float | Unset):
        value_35 (float | Unset):
        value_40 (float | Unset):
        value_45 (float | Unset):
        value_50 (float | Unset):
        value_55 (float | Unset):
        value_60 (float | Unset):
        value_65 (float | Unset):
        value_70 (float | Unset):
        value_75 (float | Unset):
        value_80 (float | Unset):
        value_85 (float | Unset):
        value_90 (float | Unset):
        value_95 (float | Unset):
        value_100 (float | Unset):
    """

    value_0: float | Unset = UNSET
    value_5: float | Unset = UNSET
    value_10: float | Unset = UNSET
    value_15: float | Unset = UNSET
    value_20: float | Unset = UNSET
    value_25: float | Unset = UNSET
    value_30: float | Unset = UNSET
    value_35: float | Unset = UNSET
    value_40: float | Unset = UNSET
    value_45: float | Unset = UNSET
    value_50: float | Unset = UNSET
    value_55: float | Unset = UNSET
    value_60: float | Unset = UNSET
    value_65: float | Unset = UNSET
    value_70: float | Unset = UNSET
    value_75: float | Unset = UNSET
    value_80: float | Unset = UNSET
    value_85: float | Unset = UNSET
    value_90: float | Unset = UNSET
    value_95: float | Unset = UNSET
    value_100: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value_0 = self.value_0

        value_5 = self.value_5

        value_10 = self.value_10

        value_15 = self.value_15

        value_20 = self.value_20

        value_25 = self.value_25

        value_30 = self.value_30

        value_35 = self.value_35

        value_40 = self.value_40

        value_45 = self.value_45

        value_50 = self.value_50

        value_55 = self.value_55

        value_60 = self.value_60

        value_65 = self.value_65

        value_70 = self.value_70

        value_75 = self.value_75

        value_80 = self.value_80

        value_85 = self.value_85

        value_90 = self.value_90

        value_95 = self.value_95

        value_100 = self.value_100

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value_0 is not UNSET:
            field_dict["Value0"] = value_0
        if value_5 is not UNSET:
            field_dict["Value5"] = value_5
        if value_10 is not UNSET:
            field_dict["Value10"] = value_10
        if value_15 is not UNSET:
            field_dict["Value15"] = value_15
        if value_20 is not UNSET:
            field_dict["Value20"] = value_20
        if value_25 is not UNSET:
            field_dict["Value25"] = value_25
        if value_30 is not UNSET:
            field_dict["Value30"] = value_30
        if value_35 is not UNSET:
            field_dict["Value35"] = value_35
        if value_40 is not UNSET:
            field_dict["Value40"] = value_40
        if value_45 is not UNSET:
            field_dict["Value45"] = value_45
        if value_50 is not UNSET:
            field_dict["Value50"] = value_50
        if value_55 is not UNSET:
            field_dict["Value55"] = value_55
        if value_60 is not UNSET:
            field_dict["Value60"] = value_60
        if value_65 is not UNSET:
            field_dict["Value65"] = value_65
        if value_70 is not UNSET:
            field_dict["Value70"] = value_70
        if value_75 is not UNSET:
            field_dict["Value75"] = value_75
        if value_80 is not UNSET:
            field_dict["Value80"] = value_80
        if value_85 is not UNSET:
            field_dict["Value85"] = value_85
        if value_90 is not UNSET:
            field_dict["Value90"] = value_90
        if value_95 is not UNSET:
            field_dict["Value95"] = value_95
        if value_100 is not UNSET:
            field_dict["Value100"] = value_100

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value_0 = d.pop("Value0", UNSET)

        value_5 = d.pop("Value5", UNSET)

        value_10 = d.pop("Value10", UNSET)

        value_15 = d.pop("Value15", UNSET)

        value_20 = d.pop("Value20", UNSET)

        value_25 = d.pop("Value25", UNSET)

        value_30 = d.pop("Value30", UNSET)

        value_35 = d.pop("Value35", UNSET)

        value_40 = d.pop("Value40", UNSET)

        value_45 = d.pop("Value45", UNSET)

        value_50 = d.pop("Value50", UNSET)

        value_55 = d.pop("Value55", UNSET)

        value_60 = d.pop("Value60", UNSET)

        value_65 = d.pop("Value65", UNSET)

        value_70 = d.pop("Value70", UNSET)

        value_75 = d.pop("Value75", UNSET)

        value_80 = d.pop("Value80", UNSET)

        value_85 = d.pop("Value85", UNSET)

        value_90 = d.pop("Value90", UNSET)

        value_95 = d.pop("Value95", UNSET)

        value_100 = d.pop("Value100", UNSET)

        values = cls(
            value_0=value_0,
            value_5=value_5,
            value_10=value_10,
            value_15=value_15,
            value_20=value_20,
            value_25=value_25,
            value_30=value_30,
            value_35=value_35,
            value_40=value_40,
            value_45=value_45,
            value_50=value_50,
            value_55=value_55,
            value_60=value_60,
            value_65=value_65,
            value_70=value_70,
            value_75=value_75,
            value_80=value_80,
            value_85=value_85,
            value_90=value_90,
            value_95=value_95,
            value_100=value_100,
        )

        values.additional_properties = d
        return values

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
