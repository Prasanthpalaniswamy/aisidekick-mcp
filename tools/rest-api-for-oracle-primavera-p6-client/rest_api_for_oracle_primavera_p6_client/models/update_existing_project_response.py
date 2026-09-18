from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateExistingProjectResponse")


@_attrs_define
class UpdateExistingProjectResponse:
    """UpdateExistingProjectResponse Entity

    Attributes:
        log_file (str | Unset): Contains the logging information from the ImportProjects operation.
        error_message (str | Unset): If an exception is thrown, ErrorMessage contains the message part of the exception.
        success (bool | Unset): Boolean flag that indicates whether the UpdateExistingProject operation was successful.
    """

    log_file: str | Unset = UNSET
    error_message: str | Unset = UNSET
    success: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        log_file = self.log_file

        error_message = self.error_message

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if log_file is not UNSET:
            field_dict["LogFile"] = log_file
        if error_message is not UNSET:
            field_dict["ErrorMessage"] = error_message
        if success is not UNSET:
            field_dict["Success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        log_file = d.pop("LogFile", UNSET)

        error_message = d.pop("ErrorMessage", UNSET)

        success = d.pop("Success", UNSET)

        update_existing_project_response = cls(
            log_file=log_file,
            error_message=error_message,
            success=success,
        )

        update_existing_project_response.additional_properties = d
        return update_existing_project_response

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
