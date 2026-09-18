from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_existing_project_default_global_import_option import UpdateExistingProjectDefaultGlobalImportOption
from ..models.update_existing_project_default_project_specific_import_option import (
    UpdateExistingProjectDefaultProjectSpecificImportOption,
)
from ..models.update_existing_project_file_type import UpdateExistingProjectFileType
from ..models.update_existing_project_log_level import UpdateExistingProjectLogLevel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.business_object_options import BusinessObjectOptions


T = TypeVar("T", bound="UpdateExistingProject")


@_attrs_define
class UpdateExistingProject:
    """
    Attributes:
        default_global_import_option (UpdateExistingProjectDefaultGlobalImportOption | Unset): Import options that may
            be applied to projects globally.
        default_project_specific_import_option (UpdateExistingProjectDefaultProjectSpecificImportOption | Unset): Import
            options that may be applied to specific projects.
        project_object_id (int | Unset): Unique Id of associated project.
        file_type (UpdateExistingProjectFileType | Unset): Specifies the file type that the system imports.
        ignore_guid (bool | Unset): When this flag is set to true, the XMLImporter ignores all GUID fields in the XML
            file, and allows new GUID values to be generated. When this flag is set to false, the XMLImporter uses the GUID
            fields.
        ignore_sequence_number (bool | Unset): When this flag is set to true, the XMLImporter ignores all SequenceNumber
            fields in the XML file, and allows new SequenceNumber values to be generated. When this flag is set to false,
            XMLImporter uses the SequenceNumber fields.
        log_level (UpdateExistingProjectLogLevel | Unset): string
            restricted to
            SEVERE
            WARNING
            INFO
            CONFIG
            FINE
            FINER
            FINEST
        business_object_options (BusinessObjectOptions | Unset): Specifies which business objects to import according to
            the following rules:

            If no BusinessObjectOptions are specified, then all of the business objects in the project are imported. If any
            BusinessObjectOptions are specified, then only those business objects specified by the BusinessObjectOptions
            element are imported.
    """

    default_global_import_option: UpdateExistingProjectDefaultGlobalImportOption | Unset = UNSET
    default_project_specific_import_option: UpdateExistingProjectDefaultProjectSpecificImportOption | Unset = UNSET
    project_object_id: int | Unset = UNSET
    file_type: UpdateExistingProjectFileType | Unset = UNSET
    ignore_guid: bool | Unset = UNSET
    ignore_sequence_number: bool | Unset = UNSET
    log_level: UpdateExistingProjectLogLevel | Unset = UNSET
    business_object_options: BusinessObjectOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_global_import_option: str | Unset = UNSET
        if not isinstance(self.default_global_import_option, Unset):
            default_global_import_option = self.default_global_import_option.value

        default_project_specific_import_option: str | Unset = UNSET
        if not isinstance(self.default_project_specific_import_option, Unset):
            default_project_specific_import_option = self.default_project_specific_import_option.value

        project_object_id = self.project_object_id

        file_type: str | Unset = UNSET
        if not isinstance(self.file_type, Unset):
            file_type = self.file_type.value

        ignore_guid = self.ignore_guid

        ignore_sequence_number = self.ignore_sequence_number

        log_level: str | Unset = UNSET
        if not isinstance(self.log_level, Unset):
            log_level = self.log_level.value

        business_object_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.business_object_options, Unset):
            business_object_options = self.business_object_options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_global_import_option is not UNSET:
            field_dict["DefaultGlobalImportOption"] = default_global_import_option
        if default_project_specific_import_option is not UNSET:
            field_dict["DefaultProjectSpecificImportOption"] = default_project_specific_import_option
        if project_object_id is not UNSET:
            field_dict["ProjectObjectId"] = project_object_id
        if file_type is not UNSET:
            field_dict["FileType"] = file_type
        if ignore_guid is not UNSET:
            field_dict["IgnoreGUID"] = ignore_guid
        if ignore_sequence_number is not UNSET:
            field_dict["IgnoreSequenceNumber"] = ignore_sequence_number
        if log_level is not UNSET:
            field_dict["LogLevel"] = log_level
        if business_object_options is not UNSET:
            field_dict["BusinessObjectOptions"] = business_object_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.business_object_options import BusinessObjectOptions

        d = dict(src_dict)
        _default_global_import_option = d.pop("DefaultGlobalImportOption", UNSET)
        default_global_import_option: UpdateExistingProjectDefaultGlobalImportOption | Unset
        if isinstance(_default_global_import_option, Unset):
            default_global_import_option = UNSET
        else:
            default_global_import_option = UpdateExistingProjectDefaultGlobalImportOption(_default_global_import_option)

        _default_project_specific_import_option = d.pop("DefaultProjectSpecificImportOption", UNSET)
        default_project_specific_import_option: UpdateExistingProjectDefaultProjectSpecificImportOption | Unset
        if isinstance(_default_project_specific_import_option, Unset):
            default_project_specific_import_option = UNSET
        else:
            default_project_specific_import_option = UpdateExistingProjectDefaultProjectSpecificImportOption(
                _default_project_specific_import_option
            )

        project_object_id = d.pop("ProjectObjectId", UNSET)

        _file_type = d.pop("FileType", UNSET)
        file_type: UpdateExistingProjectFileType | Unset
        if isinstance(_file_type, Unset):
            file_type = UNSET
        else:
            file_type = UpdateExistingProjectFileType(_file_type)

        ignore_guid = d.pop("IgnoreGUID", UNSET)

        ignore_sequence_number = d.pop("IgnoreSequenceNumber", UNSET)

        _log_level = d.pop("LogLevel", UNSET)
        log_level: UpdateExistingProjectLogLevel | Unset
        if isinstance(_log_level, Unset):
            log_level = UNSET
        else:
            log_level = UpdateExistingProjectLogLevel(_log_level)

        _business_object_options = d.pop("BusinessObjectOptions", UNSET)
        business_object_options: BusinessObjectOptions | Unset
        if isinstance(_business_object_options, Unset):
            business_object_options = UNSET
        else:
            business_object_options = BusinessObjectOptions.from_dict(_business_object_options)

        update_existing_project = cls(
            default_global_import_option=default_global_import_option,
            default_project_specific_import_option=default_project_specific_import_option,
            project_object_id=project_object_id,
            file_type=file_type,
            ignore_guid=ignore_guid,
            ignore_sequence_number=ignore_sequence_number,
            log_level=log_level,
            business_object_options=business_object_options,
        )

        update_existing_project.additional_properties = d
        return update_existing_project

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
