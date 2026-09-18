from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cbs_expense_spread import CBSExpenseSpread


T = TypeVar("T", bound="ReadCBSExpenseSpreadResponse")


@_attrs_define
class ReadCBSExpenseSpreadResponse:
    """ReadCBSExpenseSpreadResponse Entity

    Attributes:
        cbsexpense_spread (list[CBSExpenseSpread] | Unset):
        cbs_expense_spread (list[CBSExpenseSpread] | Unset):
    """

    cbsexpense_spread: list[CBSExpenseSpread] | Unset = UNSET
    cbs_expense_spread: list[CBSExpenseSpread] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cbsexpense_spread: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cbsexpense_spread, Unset):
            cbsexpense_spread = []
            for cbsexpense_spread_item_data in self.cbsexpense_spread:
                cbsexpense_spread_item = cbsexpense_spread_item_data.to_dict()
                cbsexpense_spread.append(cbsexpense_spread_item)

        cbs_expense_spread: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cbs_expense_spread, Unset):
            cbs_expense_spread = []
            for cbs_expense_spread_item_data in self.cbs_expense_spread:
                cbs_expense_spread_item = cbs_expense_spread_item_data.to_dict()
                cbs_expense_spread.append(cbs_expense_spread_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cbsexpense_spread is not UNSET:
            field_dict["cbsexpenseSpread"] = cbsexpense_spread
        if cbs_expense_spread is not UNSET:
            field_dict["CBSExpenseSpread"] = cbs_expense_spread

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cbs_expense_spread import CBSExpenseSpread

        d = dict(src_dict)
        _cbsexpense_spread = d.pop("cbsexpenseSpread", UNSET)
        cbsexpense_spread: list[CBSExpenseSpread] | Unset = UNSET
        if _cbsexpense_spread is not UNSET:
            cbsexpense_spread = []
            for cbsexpense_spread_item_data in _cbsexpense_spread:
                cbsexpense_spread_item = CBSExpenseSpread.from_dict(cbsexpense_spread_item_data)

                cbsexpense_spread.append(cbsexpense_spread_item)

        _cbs_expense_spread = d.pop("CBSExpenseSpread", UNSET)
        cbs_expense_spread: list[CBSExpenseSpread] | Unset = UNSET
        if _cbs_expense_spread is not UNSET:
            cbs_expense_spread = []
            for cbs_expense_spread_item_data in _cbs_expense_spread:
                cbs_expense_spread_item = CBSExpenseSpread.from_dict(cbs_expense_spread_item_data)

                cbs_expense_spread.append(cbs_expense_spread_item)

        read_cbs_expense_spread_response = cls(
            cbsexpense_spread=cbsexpense_spread,
            cbs_expense_spread=cbs_expense_spread,
        )

        read_cbs_expense_spread_response.additional_properties = d
        return read_cbs_expense_spread_response

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
