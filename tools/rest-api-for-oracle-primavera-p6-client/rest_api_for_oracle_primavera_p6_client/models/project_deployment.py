from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectDeployment")


@_attrs_define
class ProjectDeployment:
    """ProjectDeployment Entity

    Attributes:
        deployment_name (str | Unset):
        deployment_object_id (int | Unset):
        object_id (int | Unset):
        project_object_id (int | Unset):
        provider_name (str | Unset):
    """

    deployment_name: str | Unset = UNSET
    deployment_object_id: int | Unset = UNSET
    object_id: int | Unset = UNSET
    project_object_id: int | Unset = UNSET
    provider_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deployment_name = self.deployment_name

        deployment_object_id = self.deployment_object_id

        object_id = self.object_id

        project_object_id = self.project_object_id

        provider_name = self.provider_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deployment_name is not UNSET:
            field_dict["DeploymentName"] = deployment_name
        if deployment_object_id is not UNSET:
            field_dict["DeploymentObjectId"] = deployment_object_id
        if object_id is not UNSET:
            field_dict["ObjectId"] = object_id
        if project_object_id is not UNSET:
            field_dict["ProjectObjectId"] = project_object_id
        if provider_name is not UNSET:
            field_dict["ProviderName"] = provider_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deployment_name = d.pop("DeploymentName", UNSET)

        deployment_object_id = d.pop("DeploymentObjectId", UNSET)

        object_id = d.pop("ObjectId", UNSET)

        project_object_id = d.pop("ProjectObjectId", UNSET)

        provider_name = d.pop("ProviderName", UNSET)

        project_deployment = cls(
            deployment_name=deployment_name,
            deployment_object_id=deployment_object_id,
            object_id=object_id,
            project_object_id=project_object_id,
            provider_name=provider_name,
        )

        project_deployment.additional_properties = d
        return project_deployment

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
