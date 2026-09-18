from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentResourceResponse")


@_attrs_define
class DocumentResourceResponse:
    """DocumentResourceResponse Entity

    Attributes:
        success (str | Unset):
        document_object_id (str | Unset):
        title (str | Unset):
        security_policy (str | Unset):
        author (str | Unset):
        version (str | Unset):
        size (str | Unset):
        last_update_user (str | Unset):
        last_update_date (str | Unset):
        review_status (str | Unset):
        owner (str | Unset):
        document_category_name (str | Unset):
        reference_number (str | Unset):
        project_object_id (str | Unset):
        project_id_name (str | Unset):
        error_message (str | Unset):
    """

    success: str | Unset = UNSET
    document_object_id: str | Unset = UNSET
    title: str | Unset = UNSET
    security_policy: str | Unset = UNSET
    author: str | Unset = UNSET
    version: str | Unset = UNSET
    size: str | Unset = UNSET
    last_update_user: str | Unset = UNSET
    last_update_date: str | Unset = UNSET
    review_status: str | Unset = UNSET
    owner: str | Unset = UNSET
    document_category_name: str | Unset = UNSET
    reference_number: str | Unset = UNSET
    project_object_id: str | Unset = UNSET
    project_id_name: str | Unset = UNSET
    error_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        document_object_id = self.document_object_id

        title = self.title

        security_policy = self.security_policy

        author = self.author

        version = self.version

        size = self.size

        last_update_user = self.last_update_user

        last_update_date = self.last_update_date

        review_status = self.review_status

        owner = self.owner

        document_category_name = self.document_category_name

        reference_number = self.reference_number

        project_object_id = self.project_object_id

        project_id_name = self.project_id_name

        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["Success"] = success
        if document_object_id is not UNSET:
            field_dict["DocumentObjectId"] = document_object_id
        if title is not UNSET:
            field_dict["Title"] = title
        if security_policy is not UNSET:
            field_dict["SecurityPolicy"] = security_policy
        if author is not UNSET:
            field_dict["Author"] = author
        if version is not UNSET:
            field_dict["Version"] = version
        if size is not UNSET:
            field_dict["Size"] = size
        if last_update_user is not UNSET:
            field_dict["LastUpdateUser"] = last_update_user
        if last_update_date is not UNSET:
            field_dict["LastUpdateDate"] = last_update_date
        if review_status is not UNSET:
            field_dict["ReviewStatus"] = review_status
        if owner is not UNSET:
            field_dict["Owner"] = owner
        if document_category_name is not UNSET:
            field_dict["DocumentCategoryName"] = document_category_name
        if reference_number is not UNSET:
            field_dict["ReferenceNumber"] = reference_number
        if project_object_id is not UNSET:
            field_dict["ProjectObjectId"] = project_object_id
        if project_id_name is not UNSET:
            field_dict["ProjectIdName"] = project_id_name
        if error_message is not UNSET:
            field_dict["ErrorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("Success", UNSET)

        document_object_id = d.pop("DocumentObjectId", UNSET)

        title = d.pop("Title", UNSET)

        security_policy = d.pop("SecurityPolicy", UNSET)

        author = d.pop("Author", UNSET)

        version = d.pop("Version", UNSET)

        size = d.pop("Size", UNSET)

        last_update_user = d.pop("LastUpdateUser", UNSET)

        last_update_date = d.pop("LastUpdateDate", UNSET)

        review_status = d.pop("ReviewStatus", UNSET)

        owner = d.pop("Owner", UNSET)

        document_category_name = d.pop("DocumentCategoryName", UNSET)

        reference_number = d.pop("ReferenceNumber", UNSET)

        project_object_id = d.pop("ProjectObjectId", UNSET)

        project_id_name = d.pop("ProjectIdName", UNSET)

        error_message = d.pop("ErrorMessage", UNSET)

        document_resource_response = cls(
            success=success,
            document_object_id=document_object_id,
            title=title,
            security_policy=security_policy,
            author=author,
            version=version,
            size=size,
            last_update_user=last_update_user,
            last_update_date=last_update_date,
            review_status=review_status,
            owner=owner,
            document_category_name=document_category_name,
            reference_number=reference_number,
            project_object_id=project_object_id,
            project_id_name=project_id_name,
            error_message=error_message,
        )

        document_resource_response.additional_properties = d
        return document_resource_response

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
