from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportProjectAsyncASAPResponse")


@_attrs_define
class ImportProjectAsyncASAPResponse:
    """ImportProjectAsyncASAPResponse Entity

    Attributes:
        error_message (str | Unset):
        job_object_id (str | Unset):
        success (bool | Unset):
        success_message (str | Unset):
    """

    error_message: str | Unset = UNSET
    job_object_id: str | Unset = UNSET
    success: bool | Unset = UNSET
    success_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_message = self.error_message

        job_object_id = self.job_object_id

        success = self.success

        success_message = self.success_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_message is not UNSET:
            field_dict["ErrorMessage"] = error_message
        if job_object_id is not UNSET:
            field_dict["JobObjectId"] = job_object_id
        if success is not UNSET:
            field_dict["Success"] = success
        if success_message is not UNSET:
            field_dict["SuccessMessage"] = success_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error_message = d.pop("ErrorMessage", UNSET)

        job_object_id = d.pop("JobObjectId", UNSET)

        success = d.pop("Success", UNSET)

        success_message = d.pop("SuccessMessage", UNSET)

        import_project_async_asap_response = cls(
            error_message=error_message,
            job_object_id=job_object_id,
            success=success,
            success_message=success_message,
        )

        import_project_async_asap_response.additional_properties = d
        return import_project_async_asap_response

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
