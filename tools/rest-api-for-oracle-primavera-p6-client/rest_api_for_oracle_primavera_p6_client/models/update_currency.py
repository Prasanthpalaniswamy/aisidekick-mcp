from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="UpdateCurrency")


@_attrs_define
class UpdateCurrency:
    """Updates Currency objects and recalculate resource rate if exchange rate is changed in the database with the option
    to update resource rate.

        Attributes:
            update_resource_rates (int | Unset): Update Resource Rate options and values can be set 1/2/3
            currency (list[Currency] | Unset): List of Currency Entity
    """

    update_resource_rates: int | Unset = UNSET
    currency: list[Currency] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        update_resource_rates = self.update_resource_rates

        currency: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.currency, Unset):
            currency = []
            for currency_item_data in self.currency:
                currency_item = currency_item_data.to_dict()
                currency.append(currency_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if update_resource_rates is not UNSET:
            field_dict["UpdateResourceRates"] = update_resource_rates
        if currency is not UNSET:
            field_dict["Currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency import Currency

        d = dict(src_dict)
        update_resource_rates = d.pop("UpdateResourceRates", UNSET)

        _currency = d.pop("Currency", UNSET)
        currency: list[Currency] | Unset = UNSET
        if _currency is not UNSET:
            currency = []
            for currency_item_data in _currency:
                currency_item = Currency.from_dict(currency_item_data)

                currency.append(currency_item)

        update_currency = cls(
            update_resource_rates=update_resource_rates,
            currency=currency,
        )

        update_currency.additional_properties = d
        return update_currency

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
