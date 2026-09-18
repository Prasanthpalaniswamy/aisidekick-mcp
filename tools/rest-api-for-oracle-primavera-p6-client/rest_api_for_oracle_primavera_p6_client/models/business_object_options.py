from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.global_business_object_options import GlobalBusinessObjectOptions
    from ..models.project_specific_business_object_options import ProjectSpecificBusinessObjectOptions


T = TypeVar("T", bound="BusinessObjectOptions")


@_attrs_define
class BusinessObjectOptions:
    """Specifies which business objects to import according to the following rules:

    If no BusinessObjectOptions are specified, then all of the business objects in the project are imported. If any
    BusinessObjectOptions are specified, then only those business objects specified by the BusinessObjectOptions element
    are imported.

        Attributes:
            global_ (GlobalBusinessObjectOptions | Unset):
            project_specific (ProjectSpecificBusinessObjectOptions | Unset):
    """

    global_: GlobalBusinessObjectOptions | Unset = UNSET
    project_specific: ProjectSpecificBusinessObjectOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        global_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.global_, Unset):
            global_ = self.global_.to_dict()

        project_specific: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_specific, Unset):
            project_specific = self.project_specific.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if global_ is not UNSET:
            field_dict["Global"] = global_
        if project_specific is not UNSET:
            field_dict["ProjectSpecific"] = project_specific

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.global_business_object_options import GlobalBusinessObjectOptions
        from ..models.project_specific_business_object_options import ProjectSpecificBusinessObjectOptions

        d = dict(src_dict)
        _global_ = d.pop("Global", UNSET)
        global_: GlobalBusinessObjectOptions | Unset
        if isinstance(_global_, Unset):
            global_ = UNSET
        else:
            global_ = GlobalBusinessObjectOptions.from_dict(_global_)

        _project_specific = d.pop("ProjectSpecific", UNSET)
        project_specific: ProjectSpecificBusinessObjectOptions | Unset
        if isinstance(_project_specific, Unset):
            project_specific = UNSET
        else:
            project_specific = ProjectSpecificBusinessObjectOptions.from_dict(_project_specific)

        business_object_options = cls(
            global_=global_,
            project_specific=project_specific,
        )

        business_object_options.additional_properties = d
        return business_object_options

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
