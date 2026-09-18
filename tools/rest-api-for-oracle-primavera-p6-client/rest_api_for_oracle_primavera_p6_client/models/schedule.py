from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Schedule")


@_attrs_define
class Schedule:
    """Schedule Entity

    Attributes:
        project_object_id (list[int] | Unset): The unique identifier of the project.
        eps_object_id (list[int] | Unset):
        portfolio_object_id (list[int] | Unset):
        project_code_object_id (list[int] | Unset):
        new_data_date (datetime.datetime | Unset): The new data date.
        timeout (int | Unset): The amount of time in seconds that the server side will wait for the job service to
            complete before it returns with the current job status. The Timeout parameter is optional. When you use this
            operation without specifying a Timeout parameter or with a Timeout of 0, the server immediately returns without
            waiting for the job service to complete.
    """

    project_object_id: list[int] | Unset = UNSET
    eps_object_id: list[int] | Unset = UNSET
    portfolio_object_id: list[int] | Unset = UNSET
    project_code_object_id: list[int] | Unset = UNSET
    new_data_date: datetime.datetime | Unset = UNSET
    timeout: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_object_id: list[int] | Unset = UNSET
        if not isinstance(self.project_object_id, Unset):
            project_object_id = self.project_object_id

        eps_object_id: list[int] | Unset = UNSET
        if not isinstance(self.eps_object_id, Unset):
            eps_object_id = self.eps_object_id

        portfolio_object_id: list[int] | Unset = UNSET
        if not isinstance(self.portfolio_object_id, Unset):
            portfolio_object_id = self.portfolio_object_id

        project_code_object_id: list[int] | Unset = UNSET
        if not isinstance(self.project_code_object_id, Unset):
            project_code_object_id = self.project_code_object_id

        new_data_date: str | Unset = UNSET
        if not isinstance(self.new_data_date, Unset):
            new_data_date = self.new_data_date.isoformat()

        timeout = self.timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_object_id is not UNSET:
            field_dict["ProjectObjectId"] = project_object_id
        if eps_object_id is not UNSET:
            field_dict["EPSObjectId"] = eps_object_id
        if portfolio_object_id is not UNSET:
            field_dict["PortfolioObjectId"] = portfolio_object_id
        if project_code_object_id is not UNSET:
            field_dict["ProjectCodeObjectId"] = project_code_object_id
        if new_data_date is not UNSET:
            field_dict["NewDataDate"] = new_data_date
        if timeout is not UNSET:
            field_dict["Timeout"] = timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_object_id = cast(list[int], d.pop("ProjectObjectId", UNSET))

        eps_object_id = cast(list[int], d.pop("EPSObjectId", UNSET))

        portfolio_object_id = cast(list[int], d.pop("PortfolioObjectId", UNSET))

        project_code_object_id = cast(list[int], d.pop("ProjectCodeObjectId", UNSET))

        _new_data_date = d.pop("NewDataDate", UNSET)
        new_data_date: datetime.datetime | Unset
        if isinstance(_new_data_date, Unset):
            new_data_date = UNSET
        else:
            new_data_date = isoparse(_new_data_date)

        timeout = d.pop("Timeout", UNSET)

        schedule = cls(
            project_object_id=project_object_id,
            eps_object_id=eps_object_id,
            portfolio_object_id=portfolio_object_id,
            project_code_object_id=project_code_object_id,
            new_data_date=new_data_date,
            timeout=timeout,
        )

        schedule.additional_properties = d
        return schedule

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
