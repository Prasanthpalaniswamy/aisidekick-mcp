from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Resource")


@_attrs_define
class Resource:
    """Resource Entity

    Attributes:
        auto_compute_actuals (bool | Unset):
        calculate_cost_from_units (bool | Unset):
        calendar_name (str | Unset):
        calendar_object_id (int | Unset):
        create_date (datetime.datetime | Unset):
        create_user (str | Unset):
        currency_id (str | Unset):
        currency_name (str | Unset):
        currency_object_id (int | Unset):
        default_units_per_time (float | Unset):
        effective_date (datetime.datetime | Unset):
        email_address (str | Unset):
        employee_id (str | Unset):
        guid (str | Unset):
        id (str | Unset):
        integrated_type (str | Unset):
        is_active (bool | Unset):
        is_over_time_allowed (bool | Unset):
        last_update_date (datetime.datetime | Unset):
        last_update_user (str | Unset):
        latitude (float | Unset):
        location_name (str | Unset):
        location_object_id (int | Unset):
        longitude (float | Unset):
        max_units_per_time (float | Unset):
        name (str | Unset):
        object_id (int | Unset):
        office_phone (str | Unset):
        other_phone (str | Unset):
        overtime_factor (float | Unset):
        parent_object_id (int | Unset):
        price_per_unit (float | Unset):
        primary_role_id (str | Unset):
        primary_role_name (str | Unset):
        primary_role_object_id (int | Unset):
        resource_notes (str | Unset):
        resource_type (str | Unset):
        sequence_number (int | Unset):
        shift_object_id (int | Unset):
        timesheet_approval_manager (str | Unset):
        timesheet_approval_manager_object_id (int | Unset):
        title (str | Unset):
        unit_of_measure_abbreviation (str | Unset):
        unit_of_measure_name (str | Unset):
        unit_of_measure_object_id (int | Unset):
        use_timesheets (bool | Unset):
        user_name (str | Unset):
        user_object_id (int | Unset):
    """

    auto_compute_actuals: bool | Unset = UNSET
    calculate_cost_from_units: bool | Unset = UNSET
    calendar_name: str | Unset = UNSET
    calendar_object_id: int | Unset = UNSET
    create_date: datetime.datetime | Unset = UNSET
    create_user: str | Unset = UNSET
    currency_id: str | Unset = UNSET
    currency_name: str | Unset = UNSET
    currency_object_id: int | Unset = UNSET
    default_units_per_time: float | Unset = UNSET
    effective_date: datetime.datetime | Unset = UNSET
    email_address: str | Unset = UNSET
    employee_id: str | Unset = UNSET
    guid: str | Unset = UNSET
    id: str | Unset = UNSET
    integrated_type: str | Unset = UNSET
    is_active: bool | Unset = UNSET
    is_over_time_allowed: bool | Unset = UNSET
    last_update_date: datetime.datetime | Unset = UNSET
    last_update_user: str | Unset = UNSET
    latitude: float | Unset = UNSET
    location_name: str | Unset = UNSET
    location_object_id: int | Unset = UNSET
    longitude: float | Unset = UNSET
    max_units_per_time: float | Unset = UNSET
    name: str | Unset = UNSET
    object_id: int | Unset = UNSET
    office_phone: str | Unset = UNSET
    other_phone: str | Unset = UNSET
    overtime_factor: float | Unset = UNSET
    parent_object_id: int | Unset = UNSET
    price_per_unit: float | Unset = UNSET
    primary_role_id: str | Unset = UNSET
    primary_role_name: str | Unset = UNSET
    primary_role_object_id: int | Unset = UNSET
    resource_notes: str | Unset = UNSET
    resource_type: str | Unset = UNSET
    sequence_number: int | Unset = UNSET
    shift_object_id: int | Unset = UNSET
    timesheet_approval_manager: str | Unset = UNSET
    timesheet_approval_manager_object_id: int | Unset = UNSET
    title: str | Unset = UNSET
    unit_of_measure_abbreviation: str | Unset = UNSET
    unit_of_measure_name: str | Unset = UNSET
    unit_of_measure_object_id: int | Unset = UNSET
    use_timesheets: bool | Unset = UNSET
    user_name: str | Unset = UNSET
    user_object_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_compute_actuals = self.auto_compute_actuals

        calculate_cost_from_units = self.calculate_cost_from_units

        calendar_name = self.calendar_name

        calendar_object_id = self.calendar_object_id

        create_date: str | Unset = UNSET
        if not isinstance(self.create_date, Unset):
            create_date = self.create_date.isoformat()

        create_user = self.create_user

        currency_id = self.currency_id

        currency_name = self.currency_name

        currency_object_id = self.currency_object_id

        default_units_per_time = self.default_units_per_time

        effective_date: str | Unset = UNSET
        if not isinstance(self.effective_date, Unset):
            effective_date = self.effective_date.isoformat()

        email_address = self.email_address

        employee_id = self.employee_id

        guid = self.guid

        id = self.id

        integrated_type = self.integrated_type

        is_active = self.is_active

        is_over_time_allowed = self.is_over_time_allowed

        last_update_date: str | Unset = UNSET
        if not isinstance(self.last_update_date, Unset):
            last_update_date = self.last_update_date.isoformat()

        last_update_user = self.last_update_user

        latitude = self.latitude

        location_name = self.location_name

        location_object_id = self.location_object_id

        longitude = self.longitude

        max_units_per_time = self.max_units_per_time

        name = self.name

        object_id = self.object_id

        office_phone = self.office_phone

        other_phone = self.other_phone

        overtime_factor = self.overtime_factor

        parent_object_id = self.parent_object_id

        price_per_unit = self.price_per_unit

        primary_role_id = self.primary_role_id

        primary_role_name = self.primary_role_name

        primary_role_object_id = self.primary_role_object_id

        resource_notes = self.resource_notes

        resource_type = self.resource_type

        sequence_number = self.sequence_number

        shift_object_id = self.shift_object_id

        timesheet_approval_manager = self.timesheet_approval_manager

        timesheet_approval_manager_object_id = self.timesheet_approval_manager_object_id

        title = self.title

        unit_of_measure_abbreviation = self.unit_of_measure_abbreviation

        unit_of_measure_name = self.unit_of_measure_name

        unit_of_measure_object_id = self.unit_of_measure_object_id

        use_timesheets = self.use_timesheets

        user_name = self.user_name

        user_object_id = self.user_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_compute_actuals is not UNSET:
            field_dict["AutoComputeActuals"] = auto_compute_actuals
        if calculate_cost_from_units is not UNSET:
            field_dict["CalculateCostFromUnits"] = calculate_cost_from_units
        if calendar_name is not UNSET:
            field_dict["CalendarName"] = calendar_name
        if calendar_object_id is not UNSET:
            field_dict["CalendarObjectId"] = calendar_object_id
        if create_date is not UNSET:
            field_dict["CreateDate"] = create_date
        if create_user is not UNSET:
            field_dict["CreateUser"] = create_user
        if currency_id is not UNSET:
            field_dict["CurrencyId"] = currency_id
        if currency_name is not UNSET:
            field_dict["CurrencyName"] = currency_name
        if currency_object_id is not UNSET:
            field_dict["CurrencyObjectId"] = currency_object_id
        if default_units_per_time is not UNSET:
            field_dict["DefaultUnitsPerTime"] = default_units_per_time
        if effective_date is not UNSET:
            field_dict["EffectiveDate"] = effective_date
        if email_address is not UNSET:
            field_dict["EmailAddress"] = email_address
        if employee_id is not UNSET:
            field_dict["EmployeeId"] = employee_id
        if guid is not UNSET:
            field_dict["GUID"] = guid
        if id is not UNSET:
            field_dict["Id"] = id
        if integrated_type is not UNSET:
            field_dict["IntegratedType"] = integrated_type
        if is_active is not UNSET:
            field_dict["IsActive"] = is_active
        if is_over_time_allowed is not UNSET:
            field_dict["IsOverTimeAllowed"] = is_over_time_allowed
        if last_update_date is not UNSET:
            field_dict["LastUpdateDate"] = last_update_date
        if last_update_user is not UNSET:
            field_dict["LastUpdateUser"] = last_update_user
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if location_name is not UNSET:
            field_dict["LocationName"] = location_name
        if location_object_id is not UNSET:
            field_dict["LocationObjectId"] = location_object_id
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if max_units_per_time is not UNSET:
            field_dict["MaxUnitsPerTime"] = max_units_per_time
        if name is not UNSET:
            field_dict["Name"] = name
        if object_id is not UNSET:
            field_dict["ObjectId"] = object_id
        if office_phone is not UNSET:
            field_dict["OfficePhone"] = office_phone
        if other_phone is not UNSET:
            field_dict["OtherPhone"] = other_phone
        if overtime_factor is not UNSET:
            field_dict["OvertimeFactor"] = overtime_factor
        if parent_object_id is not UNSET:
            field_dict["ParentObjectId"] = parent_object_id
        if price_per_unit is not UNSET:
            field_dict["PricePerUnit"] = price_per_unit
        if primary_role_id is not UNSET:
            field_dict["PrimaryRoleId"] = primary_role_id
        if primary_role_name is not UNSET:
            field_dict["PrimaryRoleName"] = primary_role_name
        if primary_role_object_id is not UNSET:
            field_dict["PrimaryRoleObjectId"] = primary_role_object_id
        if resource_notes is not UNSET:
            field_dict["ResourceNotes"] = resource_notes
        if resource_type is not UNSET:
            field_dict["ResourceType"] = resource_type
        if sequence_number is not UNSET:
            field_dict["SequenceNumber"] = sequence_number
        if shift_object_id is not UNSET:
            field_dict["ShiftObjectId"] = shift_object_id
        if timesheet_approval_manager is not UNSET:
            field_dict["TimesheetApprovalManager"] = timesheet_approval_manager
        if timesheet_approval_manager_object_id is not UNSET:
            field_dict["TimesheetApprovalManagerObjectId"] = timesheet_approval_manager_object_id
        if title is not UNSET:
            field_dict["Title"] = title
        if unit_of_measure_abbreviation is not UNSET:
            field_dict["UnitOfMeasureAbbreviation"] = unit_of_measure_abbreviation
        if unit_of_measure_name is not UNSET:
            field_dict["UnitOfMeasureName"] = unit_of_measure_name
        if unit_of_measure_object_id is not UNSET:
            field_dict["UnitOfMeasureObjectId"] = unit_of_measure_object_id
        if use_timesheets is not UNSET:
            field_dict["UseTimesheets"] = use_timesheets
        if user_name is not UNSET:
            field_dict["UserName"] = user_name
        if user_object_id is not UNSET:
            field_dict["UserObjectId"] = user_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_compute_actuals = d.pop("AutoComputeActuals", UNSET)

        calculate_cost_from_units = d.pop("CalculateCostFromUnits", UNSET)

        calendar_name = d.pop("CalendarName", UNSET)

        calendar_object_id = d.pop("CalendarObjectId", UNSET)

        _create_date = d.pop("CreateDate", UNSET)
        create_date: datetime.datetime | Unset
        if isinstance(_create_date, Unset):
            create_date = UNSET
        else:
            create_date = isoparse(_create_date)

        create_user = d.pop("CreateUser", UNSET)

        currency_id = d.pop("CurrencyId", UNSET)

        currency_name = d.pop("CurrencyName", UNSET)

        currency_object_id = d.pop("CurrencyObjectId", UNSET)

        default_units_per_time = d.pop("DefaultUnitsPerTime", UNSET)

        _effective_date = d.pop("EffectiveDate", UNSET)
        effective_date: datetime.datetime | Unset
        if isinstance(_effective_date, Unset):
            effective_date = UNSET
        else:
            effective_date = isoparse(_effective_date)

        email_address = d.pop("EmailAddress", UNSET)

        employee_id = d.pop("EmployeeId", UNSET)

        guid = d.pop("GUID", UNSET)

        id = d.pop("Id", UNSET)

        integrated_type = d.pop("IntegratedType", UNSET)

        is_active = d.pop("IsActive", UNSET)

        is_over_time_allowed = d.pop("IsOverTimeAllowed", UNSET)

        _last_update_date = d.pop("LastUpdateDate", UNSET)
        last_update_date: datetime.datetime | Unset
        if isinstance(_last_update_date, Unset):
            last_update_date = UNSET
        else:
            last_update_date = isoparse(_last_update_date)

        last_update_user = d.pop("LastUpdateUser", UNSET)

        latitude = d.pop("Latitude", UNSET)

        location_name = d.pop("LocationName", UNSET)

        location_object_id = d.pop("LocationObjectId", UNSET)

        longitude = d.pop("Longitude", UNSET)

        max_units_per_time = d.pop("MaxUnitsPerTime", UNSET)

        name = d.pop("Name", UNSET)

        object_id = d.pop("ObjectId", UNSET)

        office_phone = d.pop("OfficePhone", UNSET)

        other_phone = d.pop("OtherPhone", UNSET)

        overtime_factor = d.pop("OvertimeFactor", UNSET)

        parent_object_id = d.pop("ParentObjectId", UNSET)

        price_per_unit = d.pop("PricePerUnit", UNSET)

        primary_role_id = d.pop("PrimaryRoleId", UNSET)

        primary_role_name = d.pop("PrimaryRoleName", UNSET)

        primary_role_object_id = d.pop("PrimaryRoleObjectId", UNSET)

        resource_notes = d.pop("ResourceNotes", UNSET)

        resource_type = d.pop("ResourceType", UNSET)

        sequence_number = d.pop("SequenceNumber", UNSET)

        shift_object_id = d.pop("ShiftObjectId", UNSET)

        timesheet_approval_manager = d.pop("TimesheetApprovalManager", UNSET)

        timesheet_approval_manager_object_id = d.pop("TimesheetApprovalManagerObjectId", UNSET)

        title = d.pop("Title", UNSET)

        unit_of_measure_abbreviation = d.pop("UnitOfMeasureAbbreviation", UNSET)

        unit_of_measure_name = d.pop("UnitOfMeasureName", UNSET)

        unit_of_measure_object_id = d.pop("UnitOfMeasureObjectId", UNSET)

        use_timesheets = d.pop("UseTimesheets", UNSET)

        user_name = d.pop("UserName", UNSET)

        user_object_id = d.pop("UserObjectId", UNSET)

        resource = cls(
            auto_compute_actuals=auto_compute_actuals,
            calculate_cost_from_units=calculate_cost_from_units,
            calendar_name=calendar_name,
            calendar_object_id=calendar_object_id,
            create_date=create_date,
            create_user=create_user,
            currency_id=currency_id,
            currency_name=currency_name,
            currency_object_id=currency_object_id,
            default_units_per_time=default_units_per_time,
            effective_date=effective_date,
            email_address=email_address,
            employee_id=employee_id,
            guid=guid,
            id=id,
            integrated_type=integrated_type,
            is_active=is_active,
            is_over_time_allowed=is_over_time_allowed,
            last_update_date=last_update_date,
            last_update_user=last_update_user,
            latitude=latitude,
            location_name=location_name,
            location_object_id=location_object_id,
            longitude=longitude,
            max_units_per_time=max_units_per_time,
            name=name,
            object_id=object_id,
            office_phone=office_phone,
            other_phone=other_phone,
            overtime_factor=overtime_factor,
            parent_object_id=parent_object_id,
            price_per_unit=price_per_unit,
            primary_role_id=primary_role_id,
            primary_role_name=primary_role_name,
            primary_role_object_id=primary_role_object_id,
            resource_notes=resource_notes,
            resource_type=resource_type,
            sequence_number=sequence_number,
            shift_object_id=shift_object_id,
            timesheet_approval_manager=timesheet_approval_manager,
            timesheet_approval_manager_object_id=timesheet_approval_manager_object_id,
            title=title,
            unit_of_measure_abbreviation=unit_of_measure_abbreviation,
            unit_of_measure_name=unit_of_measure_name,
            unit_of_measure_object_id=unit_of_measure_object_id,
            use_timesheets=use_timesheets,
            user_name=user_name,
            user_object_id=user_object_id,
        )

        resource.additional_properties = d
        return resource

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
