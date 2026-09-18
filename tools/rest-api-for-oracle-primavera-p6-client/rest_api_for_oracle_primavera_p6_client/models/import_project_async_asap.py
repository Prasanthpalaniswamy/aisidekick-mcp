from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.import_project_async_asap_currencies_import_in_option import (
    ImportProjectAsyncASAPCurrenciesImportInOption,
)
from ..models.import_project_async_asap_file_type import ImportProjectAsyncASAPFileType
from ..models.import_project_async_asap_log_level import ImportProjectAsyncASAPLogLevel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.import_project import ImportProject


T = TypeVar("T", bound="ImportProjectAsyncASAP")


@_attrs_define
class ImportProjectAsyncASAP:
    """
    Attributes:
        currencies_import_in_option (ImportProjectAsyncASAPCurrenciesImportInOption | Unset):
        import_project (list[ImportProject] | Unset):
        import_type (str | Unset):
        import_template_name (str | Unset):
        pre_import_customization_template_name (str | Unset):
        file_type (ImportProjectAsyncASAPFileType | Unset): Specifies the file type that the system supports.
        ignore_guid (bool | Unset): When this flag is set to true, the XMLImporter ignores all GUID fields in the XML
            file, and allows new GUID values to be generated. When this flag is set to false, the XMLImporter uses the GUID
            fields.
        ignore_sequence_number (bool | Unset): When this flag is set to true, the XMLImporter ignores all SequenceNumber
            fields in the XML file, and allows new SequenceNumber values to be generated. When this flag is set to false,
            XMLImporter uses the SequenceNumber fields.
        log_level (ImportProjectAsyncASAPLogLevel | Unset):
    """

    currencies_import_in_option: ImportProjectAsyncASAPCurrenciesImportInOption | Unset = UNSET
    import_project: list[ImportProject] | Unset = UNSET
    import_type: str | Unset = UNSET
    import_template_name: str | Unset = UNSET
    pre_import_customization_template_name: str | Unset = UNSET
    file_type: ImportProjectAsyncASAPFileType | Unset = UNSET
    ignore_guid: bool | Unset = UNSET
    ignore_sequence_number: bool | Unset = UNSET
    log_level: ImportProjectAsyncASAPLogLevel | Unset = UNSET
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

        import_type = self.import_type

        import_template_name = self.import_template_name

        pre_import_customization_template_name = self.pre_import_customization_template_name

        file_type: str | Unset = UNSET
        if not isinstance(self.file_type, Unset):
            file_type = self.file_type.value

        ignore_guid = self.ignore_guid

        ignore_sequence_number = self.ignore_sequence_number

        log_level: str | Unset = UNSET
        if not isinstance(self.log_level, Unset):
            log_level = self.log_level.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currencies_import_in_option is not UNSET:
            field_dict["CurrenciesImportInOption"] = currencies_import_in_option
        if import_project is not UNSET:
            field_dict["ImportProject"] = import_project
        if import_type is not UNSET:
            field_dict["ImportType"] = import_type
        if import_template_name is not UNSET:
            field_dict["ImportTemplateName"] = import_template_name
        if pre_import_customization_template_name is not UNSET:
            field_dict["PreImportCustomizationTemplateName"] = pre_import_customization_template_name
        if file_type is not UNSET:
            field_dict["FileType"] = file_type
        if ignore_guid is not UNSET:
            field_dict["IgnoreGUID"] = ignore_guid
        if ignore_sequence_number is not UNSET:
            field_dict["IgnoreSequenceNumber"] = ignore_sequence_number
        if log_level is not UNSET:
            field_dict["LogLevel"] = log_level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_project import ImportProject

        d = dict(src_dict)
        _currencies_import_in_option = d.pop("CurrenciesImportInOption", UNSET)
        currencies_import_in_option: ImportProjectAsyncASAPCurrenciesImportInOption | Unset
        if isinstance(_currencies_import_in_option, Unset):
            currencies_import_in_option = UNSET
        else:
            currencies_import_in_option = ImportProjectAsyncASAPCurrenciesImportInOption(_currencies_import_in_option)

        _import_project = d.pop("ImportProject", UNSET)
        import_project: list[ImportProject] | Unset = UNSET
        if _import_project is not UNSET:
            import_project = []
            for import_project_item_data in _import_project:
                import_project_item = ImportProject.from_dict(import_project_item_data)

                import_project.append(import_project_item)

        import_type = d.pop("ImportType", UNSET)

        import_template_name = d.pop("ImportTemplateName", UNSET)

        pre_import_customization_template_name = d.pop("PreImportCustomizationTemplateName", UNSET)

        _file_type = d.pop("FileType", UNSET)
        file_type: ImportProjectAsyncASAPFileType | Unset
        if isinstance(_file_type, Unset):
            file_type = UNSET
        else:
            file_type = ImportProjectAsyncASAPFileType(_file_type)

        ignore_guid = d.pop("IgnoreGUID", UNSET)

        ignore_sequence_number = d.pop("IgnoreSequenceNumber", UNSET)

        _log_level = d.pop("LogLevel", UNSET)
        log_level: ImportProjectAsyncASAPLogLevel | Unset
        if isinstance(_log_level, Unset):
            log_level = UNSET
        else:
            log_level = ImportProjectAsyncASAPLogLevel(_log_level)

        import_project_async_asap = cls(
            currencies_import_in_option=currencies_import_in_option,
            import_project=import_project,
            import_type=import_type,
            import_template_name=import_template_name,
            pre_import_customization_template_name=pre_import_customization_template_name,
            file_type=file_type,
            ignore_guid=ignore_guid,
            ignore_sequence_number=ignore_sequence_number,
            log_level=log_level,
        )

        import_project_async_asap.additional_properties = d
        return import_project_async_asap

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
