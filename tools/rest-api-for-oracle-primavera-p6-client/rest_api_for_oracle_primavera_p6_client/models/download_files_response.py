from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DownloadFilesResponse")


@_attrs_define
class DownloadFilesResponse:
    """DownloadFilesResponse Entity

    Attributes:
        number_of_files (int | Unset):
    """

    number_of_files: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number_of_files = self.number_of_files

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if number_of_files is not UNSET:
            field_dict["NumberOfFiles"] = number_of_files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        number_of_files = d.pop("NumberOfFiles", UNSET)

        download_files_response = cls(
            number_of_files=number_of_files,
        )

        download_files_response.additional_properties = d
        return download_files_response

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
