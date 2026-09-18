from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.import_projects_currencies_import_in_option import ImportProjectsCurrenciesImportInOption
from ..models.import_projects_default_global_import_option import ImportProjectsDefaultGlobalImportOption
from ..models.import_projects_default_project_specific_import_option import (
    ImportProjectsDefaultProjectSpecificImportOption,
)
from ..models.import_projects_file_type import ImportProjectsFileType
from ..models.import_projects_log_level import ImportProjectsLogLevel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.business_object_options import BusinessObjectOptions
    from ..models.import_project import ImportProject


T = TypeVar("T", bound="ImportProjects")


@_attrs_define
class ImportProjects:
    """
    Attributes:
        currencies_import_in_option (ImportProjectsCurrenciesImportInOption | Unset):
        import_project (list[ImportProject] | Unset):
        file_type (ImportProjectsFileType | Unset): Specifies the file type that the system imports.
        import_type (str | Unset): Specifies the Import type that the system imports.
        business_object_options (BusinessObjectOptions | Unset): Specifies which business objects to import according to
            the following rules:

            If no BusinessObjectOptions are specified, then all of the business objects in the project are imported. If any
            BusinessObjectOptions are specified, then only those business objects specified by the BusinessObjectOptions
            element are imported.
        ignore_guid (bool | Unset): When this flag is set to true, the XMLImporter ignores all GUID fields in the XML
            file, and allows new GUID values to be generated. When this flag is set to false, the XMLImporter uses the GUID
            fields.
        ignore_sequence_number (bool | Unset): When this flag is set to true, the XMLImporter ignores all SequenceNumber
            fields in the XML file, and allows new SequenceNumber values to be generated. When this flag is set to false,
            XMLImporter uses the SequenceNumber fields.
        log_level (ImportProjectsLogLevel | Unset):
        default_global_import_option (ImportProjectsDefaultGlobalImportOption | Unset): Import options that may be
            applied to projects globally.
        default_project_specific_import_option (ImportProjectsDefaultProjectSpecificImportOption | Unset): Import
            options that may be applied to specific projects.
    """

    currencies_import_in_option: ImportProjectsCurrenciesImportInOption | Unset = UNSET
    import_project: list[ImportProject] | Unset = UNSET
    file_type: ImportProjectsFileType | Unset = UNSET
    import_type: str | Unset = UNSET
    business_object_options: BusinessObjectOptions | Unset = UNSET
    ignore_guid: bool | Unset = UNSET
    ignore_sequence_number: bool | Unset = UNSET
    log_level: ImportProjectsLogLevel | Unset = UNSET
    default_global_import_option: ImportProjectsDefaultGlobalImportOption | Unset = UNSET
    default_project_specific_import_option: ImportProjectsDefaultProjectSpecificImportOption | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currencies_import_in_option: str | Unset = UNSET
        if not isinstance(self.currencies_import_in_option, Unset):
            currencies_import_in_option = self.currencies_import_in_option.value

        import_project: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.import_project, Unset):
            import_project = []
            for import_project_item_data in self.import_project:
                import_project_item = import_project_item_data.to_dict()
                import_project.append(import_project_item)

        file_type: str | Unset = UNSET
        if not isinstance(self.file_type, Unset):
            file_type = self.file_type.value

        import_type = self.import_type

        business_object_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.business_object_options, Unset):
            business_object_options = self.business_object_options.to_dict()

        ignore_guid = self.ignore_guid

        ignore_sequence_number = self.ignore_sequence_number

        log_level: str | Unset = UNSET
        if not isinstance(self.log_level, Unset):
            log_level = self.log_level.value

        default_global_import_option: str | Unset = UNSET
        if not isinstance(self.default_global_import_option, Unset):
            default_global_import_option = self.default_global_import_option.value

        default_project_specific_import_option: str | Unset = UNSET
        if not isinstance(self.default_project_specific_import_option, Unset):
            default_project_specific_import_option = self.default_project_specific_import_option.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currencies_import_in_option is not UNSET:
            field_dict["CurrenciesImportInOption"] = currencies_import_in_option
        if import_project is not UNSET:
            field_dict["ImportProject"] = import_project
        if file_type is not UNSET:
            field_dict["FileType"] = file_type
        if import_type is not UNSET:
            field_dict["ImportType"] = import_type
        if business_object_options is not UNSET:
            field_dict["BusinessObjectOptions"] = business_object_options
        if ignore_guid is not UNSET:
            field_dict["IgnoreGUID"] = ignore_guid
        if ignore_sequence_number is not UNSET:
            field_dict["IgnoreSequenceNumber"] = ignore_sequence_number
        if log_level is not UNSET:
            field_dict["LogLevel"] = log_level
        if default_global_import_option is not UNSET:
            field_dict["DefaultGlobalImportOption"] = default_global_import_option
        if default_project_specific_import_option is not UNSET:
            field_dict["DefaultProjectSpecificImportOption"] = default_project_specific_import_option

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.business_object_options import BusinessObjectOptions
        from ..models.import_project import ImportProject

        d = dict(src_dict)
        _currencies_import_in_option = d.pop("CurrenciesImportInOption", UNSET)
        currencies_import_in_option: ImportProjectsCurrenciesImportInOption | Unset
        if isinstance(_currencies_import_in_option, Unset):
            currencies_import_in_option = UNSET
        else:
            currencies_import_in_option = ImportProjectsCurrenciesImportInOption(_currencies_import_in_option)

        _import_project = d.pop("ImportProject", UNSET)
        import_project: list[ImportProject] | Unset = UNSET
        if _import_project is not UNSET:
            import_project = []
            for import_project_item_data in _import_project:
                import_project_item = ImportProject.from_dict(import_project_item_data)

                import_project.append(import_project_item)

        _file_type = d.pop("FileType", UNSET)
        file_type: ImportProjectsFileType | Unset
        if isinstance(_file_type, Unset):
            file_type = UNSET
        else:
            file_type = ImportProjectsFileType(_file_type)

        import_type = d.pop("ImportType", UNSET)

        _business_object_options = d.pop("BusinessObjectOptions", UNSET)
        business_object_options: BusinessObjectOptions | Unset
        if isinstance(_business_object_options, Unset):
            business_object_options = UNSET
        else:
            business_object_options = BusinessObjectOptions.from_dict(_business_object_options)

        ignore_guid = d.pop("IgnoreGUID", UNSET)

        ignore_sequence_number = d.pop("IgnoreSequenceNumber", UNSET)

        _log_level = d.pop("LogLevel", UNSET)
        log_level: ImportProjectsLogLevel | Unset
        if isinstance(_log_level, Unset):
            log_level = UNSET
        else:
            log_level = ImportProjectsLogLevel(_log_level)

        _default_global_import_option = d.pop("DefaultGlobalImportOption", UNSET)
        default_global_import_option: ImportProjectsDefaultGlobalImportOption | Unset
        if isinstance(_default_global_import_option, Unset):
            default_global_import_option = UNSET
        else:
            default_global_import_option = ImportProjectsDefaultGlobalImportOption(_default_global_import_option)

        _default_project_specific_import_option = d.pop("DefaultProjectSpecificImportOption", UNSET)
        default_project_specific_import_option: ImportProjectsDefaultProjectSpecificImportOption | Unset
        if isinstance(_default_project_specific_import_option, Unset):
            default_project_specific_import_option = UNSET
        else:
            default_project_specific_import_option = ImportProjectsDefaultProjectSpecificImportOption(
                _default_project_specific_import_option
            )

        import_projects = cls(
            currencies_import_in_option=currencies_import_in_option,
            import_project=import_project,
            file_type=file_type,
            import_type=import_type,
            business_object_options=business_object_options,
            ignore_guid=ignore_guid,
            ignore_sequence_number=ignore_sequence_number,
            log_level=log_level,
            default_global_import_option=default_global_import_option,
            default_project_specific_import_option=default_project_specific_import_option,
        )

        import_projects.additional_properties = d
        return import_projects

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
