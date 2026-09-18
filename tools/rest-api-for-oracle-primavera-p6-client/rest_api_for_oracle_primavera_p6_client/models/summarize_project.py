from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SummarizeProject")


@_attrs_define
class SummarizeProject:
    """SummarizeProject Entity

    Attributes:
        object_id (list[int] | Unset): The unique identifier of the project you want to summarize.
        portfolio_object_id (list[int] | Unset):
        project_code_object_id (list[int] | Unset):
        timeout (int | Unset): The amount of time in seconds that the server side will wait for the job service to
            complete before it returns with the current job status. The Timeout parameter is optional. When this operation
            is used without specifying a Timeout parameter or with a Timeout of 0, the server immediately returns without
            waiting for the job service to complete.
    """

    object_id: list[int] | Unset = UNSET
    portfolio_object_id: list[int] | Unset = UNSET
    project_code_object_id: list[int] | Unset = UNSET
    timeout: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_id: list[int] | Unset = UNSET
        if not isinstance(self.object_id, Unset):
            object_id = self.object_id

        portfolio_object_id: list[int] | Unset = UNSET
        if not isinstance(self.portfolio_object_id, Unset):
            portfolio_object_id = self.portfolio_object_id

        project_code_object_id: list[int] | Unset = UNSET
        if not isinstance(self.project_code_object_id, Unset):
            project_code_object_id = self.project_code_object_id

        timeout = self.timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_id is not UNSET:
            field_dict["ObjectId"] = object_id
        if portfolio_object_id is not UNSET:
            field_dict["PortfolioObjectId"] = portfolio_object_id
        if project_code_object_id is not UNSET:
            field_dict["ProjectCodeObjectId"] = project_code_object_id
        if timeout is not UNSET:
            field_dict["Timeout"] = timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_id = cast(list[int], d.pop("ObjectId", UNSET))

        portfolio_object_id = cast(list[int], d.pop("PortfolioObjectId", UNSET))

        project_code_object_id = cast(list[int], d.pop("ProjectCodeObjectId", UNSET))

        timeout = d.pop("Timeout", UNSET)

        summarize_project = cls(
            object_id=object_id,
            portfolio_object_id=portfolio_object_id,
            project_code_object_id=project_code_object_id,
            timeout=timeout,
        )

        summarize_project.additional_properties = d
        return summarize_project

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
