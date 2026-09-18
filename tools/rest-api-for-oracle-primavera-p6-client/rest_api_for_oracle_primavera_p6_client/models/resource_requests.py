from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_request import ResourceRequest


T = TypeVar("T", bound="ResourceRequests")


@_attrs_define
class ResourceRequests:
    """
    Attributes:
        resource_request (list[ResourceRequest] | Unset):
    """

    resource_request: list[ResourceRequest] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_request: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.resource_request, Unset):
            resource_request = []
            for resource_request_item_data in self.resource_request:
                resource_request_item = resource_request_item_data.to_dict()
                resource_request.append(resource_request_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_request is not UNSET:
            field_dict["ResourceRequest"] = resource_request

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_request import ResourceRequest

        d = dict(src_dict)
        _resource_request = d.pop("ResourceRequest", UNSET)
        resource_request: list[ResourceRequest] | Unset = UNSET
        if _resource_request is not UNSET:
            resource_request = []
            for resource_request_item_data in _resource_request:
                resource_request_item = ResourceRequest.from_dict(resource_request_item_data)

                resource_request.append(resource_request_item)

        resource_requests = cls(
            resource_request=resource_request,
        )

        resource_requests.additional_properties = d
        return resource_requests

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
