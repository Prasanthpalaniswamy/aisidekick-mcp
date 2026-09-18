from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.holiday_or_exception import HolidayOrException


T = TypeVar("T", bound="HolidayOrExceptions")


@_attrs_define
class HolidayOrExceptions:
    """HolidayOrExceptions

    Attributes:
        holiday_or_exception (list[HolidayOrException] | Unset):
    """

    holiday_or_exception: list[HolidayOrException] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        holiday_or_exception: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.holiday_or_exception, Unset):
            holiday_or_exception = []
            for holiday_or_exception_item_data in self.holiday_or_exception:
                holiday_or_exception_item = holiday_or_exception_item_data.to_dict()
                holiday_or_exception.append(holiday_or_exception_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if holiday_or_exception is not UNSET:
            field_dict["HolidayOrException"] = holiday_or_exception

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.holiday_or_exception import HolidayOrException

        d = dict(src_dict)
        _holiday_or_exception = d.pop("HolidayOrException", UNSET)
        holiday_or_exception: list[HolidayOrException] | Unset = UNSET
        if _holiday_or_exception is not UNSET:
            holiday_or_exception = []
            for holiday_or_exception_item_data in _holiday_or_exception:
                holiday_or_exception_item = HolidayOrException.from_dict(holiday_or_exception_item_data)

                holiday_or_exception.append(holiday_or_exception_item)

        holiday_or_exceptions = cls(
            holiday_or_exception=holiday_or_exception,
        )

        holiday_or_exceptions.additional_properties = d
        return holiday_or_exceptions

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
