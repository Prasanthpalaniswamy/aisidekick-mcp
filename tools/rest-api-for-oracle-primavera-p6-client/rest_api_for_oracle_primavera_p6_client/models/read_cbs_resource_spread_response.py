from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cbs_resource_spread import CBSResourceSpread


T = TypeVar("T", bound="ReadCBSResourceSpreadResponse")


@_attrs_define
class ReadCBSResourceSpreadResponse:
    """ReadCBSResourceSpreadResponse Entity

    Attributes:
        cbsresource_spread (list[CBSResourceSpread] | Unset):
        cbs_resource_spread (list[CBSResourceSpread] | Unset):
    """

    cbsresource_spread: list[CBSResourceSpread] | Unset = UNSET
    cbs_resource_spread: list[CBSResourceSpread] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cbsresource_spread: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cbsresource_spread, Unset):
            cbsresource_spread = []
            for cbsresource_spread_item_data in self.cbsresource_spread:
                cbsresource_spread_item = cbsresource_spread_item_data.to_dict()
                cbsresource_spread.append(cbsresource_spread_item)

        cbs_resource_spread: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cbs_resource_spread, Unset):
            cbs_resource_spread = []
            for cbs_resource_spread_item_data in self.cbs_resource_spread:
                cbs_resource_spread_item = cbs_resource_spread_item_data.to_dict()
                cbs_resource_spread.append(cbs_resource_spread_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cbsresource_spread is not UNSET:
            field_dict["cbsresourceSpread"] = cbsresource_spread
        if cbs_resource_spread is not UNSET:
            field_dict["CBSResourceSpread"] = cbs_resource_spread

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cbs_resource_spread import CBSResourceSpread

        d = dict(src_dict)
        _cbsresource_spread = d.pop("cbsresourceSpread", UNSET)
        cbsresource_spread: list[CBSResourceSpread] | Unset = UNSET
        if _cbsresource_spread is not UNSET:
            cbsresource_spread = []
            for cbsresource_spread_item_data in _cbsresource_spread:
                cbsresource_spread_item = CBSResourceSpread.from_dict(cbsresource_spread_item_data)

                cbsresource_spread.append(cbsresource_spread_item)

        _cbs_resource_spread = d.pop("CBSResourceSpread", UNSET)
        cbs_resource_spread: list[CBSResourceSpread] | Unset = UNSET
        if _cbs_resource_spread is not UNSET:
            cbs_resource_spread = []
            for cbs_resource_spread_item_data in _cbs_resource_spread:
                cbs_resource_spread_item = CBSResourceSpread.from_dict(cbs_resource_spread_item_data)

                cbs_resource_spread.append(cbs_resource_spread_item)

        read_cbs_resource_spread_response = cls(
            cbsresource_spread=cbsresource_spread,
            cbs_resource_spread=cbs_resource_spread,
        )

        read_cbs_resource_spread_response.additional_properties = d
        return read_cbs_resource_spread_response

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
