from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HasPrivilegeResponse")


@_attrs_define
class HasPrivilegeResponse:
    """
    Attributes:
        return_ (bool | Unset):
        Return (bool | Unset):
    """

    return_: bool | Unset = UNSET
    Return: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return_ = self.return_

        Return = self.Return

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if return_ is not UNSET:
            field_dict["return"] = return_
        if Return is not UNSET:
            field_dict["Return"] = Return

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        return_ = d.pop("return", UNSET)

        Return = d.pop("Return", UNSET)

        has_privilege_response = cls(
            return_=return_,
            Return=Return,
        )

        has_privilege_response.additional_properties = d
        return has_privilege_response

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
