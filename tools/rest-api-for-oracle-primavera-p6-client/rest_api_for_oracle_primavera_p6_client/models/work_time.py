from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkTime")


@_attrs_define
class WorkTime:
    """
    Attributes:
        finish (datetime.datetime | Unset):
        start (datetime.datetime | Unset):
    """

    finish: datetime.datetime | Unset = UNSET
    start: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        finish: str | Unset = UNSET
        if not isinstance(self.finish, Unset):
            finish = self.finish.isoformat()

        start: str | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if finish is not UNSET:
            field_dict["Finish"] = finish
        if start is not UNSET:
            field_dict["Start"] = start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _finish = d.pop("Finish", UNSET)
        finish: datetime.datetime | Unset
        if isinstance(_finish, Unset):
            finish = UNSET
        else:
            finish = isoparse(_finish)

        _start = d.pop("Start", UNSET)
        start: datetime.datetime | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start)

        work_time = cls(
            finish=finish,
            start=start,
        )

        work_time.additional_properties = d
        return work_time

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
