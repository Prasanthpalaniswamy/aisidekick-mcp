from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.business_object_type import BusinessObjectType


T = TypeVar("T", bound="GlobalBusinessObjectOptions")


@_attrs_define
class GlobalBusinessObjectOptions:
    """
    Attributes:
        activity_code (BusinessObjectType | Unset): BusinessObjectType Entity
        activity_code_type (BusinessObjectType | Unset): BusinessObjectType Entity
        activity_code_type_eps (BusinessObjectType | Unset): BusinessObjectType Entity
        calendar (BusinessObjectType | Unset): BusinessObjectType Entity
        calendar_rsrc (BusinessObjectType | Unset): BusinessObjectType Entity
        cost_account (BusinessObjectType | Unset): BusinessObjectType Entity
        currency (BusinessObjectType | Unset): BusinessObjectType Entity
        document_category (BusinessObjectType | Unset): BusinessObjectType Entity
        document_status_code (BusinessObjectType | Unset): BusinessObjectType Entity
        expense_category (BusinessObjectType | Unset): BusinessObjectType Entity
        financial_period (BusinessObjectType | Unset): BusinessObjectType Entity
        funding_source (BusinessObjectType | Unset): BusinessObjectType Entity
        notebook_topic (BusinessObjectType | Unset): BusinessObjectType Entity
        obs (BusinessObjectType | Unset): BusinessObjectType Entity
        project_code (BusinessObjectType | Unset): BusinessObjectType Entity
        project_code_type (BusinessObjectType | Unset): BusinessObjectType Entity
        project_resource_category (BusinessObjectType | Unset): BusinessObjectType Entity
        resource (BusinessObjectType | Unset): BusinessObjectType Entity
        resource_code (BusinessObjectType | Unset): BusinessObjectType Entity
        resource_code_type (BusinessObjectType | Unset): BusinessObjectType Entity
        resource_curve (BusinessObjectType | Unset): BusinessObjectType Entity
        resource_rate (BusinessObjectType | Unset): BusinessObjectType Entity
        resource_role (BusinessObjectType | Unset): BusinessObjectType Entity
        risk_category (BusinessObjectType | Unset): BusinessObjectType Entity
        risk_matrix_score (BusinessObjectType | Unset): BusinessObjectType Entity
        risk_matrix_threshold (BusinessObjectType | Unset): BusinessObjectType Entity
        risk_matrix (BusinessObjectType | Unset): BusinessObjectType Entity
        risk_threshold (BusinessObjectType | Unset): BusinessObjectType Entity
        risk_threshold_level (BusinessObjectType | Unset): BusinessObjectType Entity
        role (BusinessObjectType | Unset): BusinessObjectType Entity
        role_rate (BusinessObjectType | Unset): BusinessObjectType Entity
        role_limit (BusinessObjectType | Unset): BusinessObjectType Entity
        shift (BusinessObjectType | Unset): BusinessObjectType Entity
        threshold_parameter (BusinessObjectType | Unset): BusinessObjectType Entity
        unit_of_measure (BusinessObjectType | Unset): BusinessObjectType Entity
        udf_code (BusinessObjectType | Unset): BusinessObjectType Entity
        udf_type (BusinessObjectType | Unset): BusinessObjectType Entity
        wbs_category (BusinessObjectType | Unset): BusinessObjectType Entity
    """

    activity_code: BusinessObjectType | Unset = UNSET
    activity_code_type: BusinessObjectType | Unset = UNSET
    activity_code_type_eps: BusinessObjectType | Unset = UNSET
    calendar: BusinessObjectType | Unset = UNSET
    calendar_rsrc: BusinessObjectType | Unset = UNSET
    cost_account: BusinessObjectType | Unset = UNSET
    currency: BusinessObjectType | Unset = UNSET
    document_category: BusinessObjectType | Unset = UNSET
    document_status_code: BusinessObjectType | Unset = UNSET
    expense_category: BusinessObjectType | Unset = UNSET
    financial_period: BusinessObjectType | Unset = UNSET
    funding_source: BusinessObjectType | Unset = UNSET
    notebook_topic: BusinessObjectType | Unset = UNSET
    obs: BusinessObjectType | Unset = UNSET
    project_code: BusinessObjectType | Unset = UNSET
    project_code_type: BusinessObjectType | Unset = UNSET
    project_resource_category: BusinessObjectType | Unset = UNSET
    resource: BusinessObjectType | Unset = UNSET
    resource_code: BusinessObjectType | Unset = UNSET
    resource_code_type: BusinessObjectType | Unset = UNSET
    resource_curve: BusinessObjectType | Unset = UNSET
    resource_rate: BusinessObjectType | Unset = UNSET
    resource_role: BusinessObjectType | Unset = UNSET
    risk_category: BusinessObjectType | Unset = UNSET
    risk_matrix_score: BusinessObjectType | Unset = UNSET
    risk_matrix_threshold: BusinessObjectType | Unset = UNSET
    risk_matrix: BusinessObjectType | Unset = UNSET
    risk_threshold: BusinessObjectType | Unset = UNSET
    risk_threshold_level: BusinessObjectType | Unset = UNSET
    role: BusinessObjectType | Unset = UNSET
    role_rate: BusinessObjectType | Unset = UNSET
    role_limit: BusinessObjectType | Unset = UNSET
    shift: BusinessObjectType | Unset = UNSET
    threshold_parameter: BusinessObjectType | Unset = UNSET
    unit_of_measure: BusinessObjectType | Unset = UNSET
    udf_code: BusinessObjectType | Unset = UNSET
    udf_type: BusinessObjectType | Unset = UNSET
    wbs_category: BusinessObjectType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.activity_code, Unset):
            activity_code = self.activity_code.to_dict()

        activity_code_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.activity_code_type, Unset):
            activity_code_type = self.activity_code_type.to_dict()

        activity_code_type_eps: dict[str, Any] | Unset = UNSET
        if not isinstance(self.activity_code_type_eps, Unset):
            activity_code_type_eps = self.activity_code_type_eps.to_dict()

        calendar: dict[str, Any] | Unset = UNSET
        if not isinstance(self.calendar, Unset):
            calendar = self.calendar.to_dict()

        calendar_rsrc: dict[str, Any] | Unset = UNSET
        if not isinstance(self.calendar_rsrc, Unset):
            calendar_rsrc = self.calendar_rsrc.to_dict()

        cost_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cost_account, Unset):
            cost_account = self.cost_account.to_dict()

        currency: dict[str, Any] | Unset = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.to_dict()

        document_category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.document_category, Unset):
            document_category = self.document_category.to_dict()

        document_status_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.document_status_code, Unset):
            document_status_code = self.document_status_code.to_dict()

        expense_category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expense_category, Unset):
            expense_category = self.expense_category.to_dict()

        financial_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.financial_period, Unset):
            financial_period = self.financial_period.to_dict()

        funding_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.funding_source, Unset):
            funding_source = self.funding_source.to_dict()

        notebook_topic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notebook_topic, Unset):
            notebook_topic = self.notebook_topic.to_dict()

        obs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.obs, Unset):
            obs = self.obs.to_dict()

        project_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_code, Unset):
            project_code = self.project_code.to_dict()

        project_code_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_code_type, Unset):
            project_code_type = self.project_code_type.to_dict()

        project_resource_category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_resource_category, Unset):
            project_resource_category = self.project_resource_category.to_dict()

        resource: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.to_dict()

        resource_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource_code, Unset):
            resource_code = self.resource_code.to_dict()

        resource_code_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource_code_type, Unset):
            resource_code_type = self.resource_code_type.to_dict()

        resource_curve: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource_curve, Unset):
            resource_curve = self.resource_curve.to_dict()

        resource_rate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource_rate, Unset):
            resource_rate = self.resource_rate.to_dict()

        resource_role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource_role, Unset):
            resource_role = self.resource_role.to_dict()

        risk_category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.risk_category, Unset):
            risk_category = self.risk_category.to_dict()

        risk_matrix_score: dict[str, Any] | Unset = UNSET
        if not isinstance(self.risk_matrix_score, Unset):
            risk_matrix_score = self.risk_matrix_score.to_dict()

        risk_matrix_threshold: dict[str, Any] | Unset = UNSET
        if not isinstance(self.risk_matrix_threshold, Unset):
            risk_matrix_threshold = self.risk_matrix_threshold.to_dict()

        risk_matrix: dict[str, Any] | Unset = UNSET
        if not isinstance(self.risk_matrix, Unset):
            risk_matrix = self.risk_matrix.to_dict()

        risk_threshold: dict[str, Any] | Unset = UNSET
        if not isinstance(self.risk_threshold, Unset):
            risk_threshold = self.risk_threshold.to_dict()

        risk_threshold_level: dict[str, Any] | Unset = UNSET
        if not isinstance(self.risk_threshold_level, Unset):
            risk_threshold_level = self.risk_threshold_level.to_dict()

        role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        role_rate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role_rate, Unset):
            role_rate = self.role_rate.to_dict()

        role_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role_limit, Unset):
            role_limit = self.role_limit.to_dict()

        shift: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shift, Unset):
            shift = self.shift.to_dict()

        threshold_parameter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.threshold_parameter, Unset):
            threshold_parameter = self.threshold_parameter.to_dict()

        unit_of_measure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unit_of_measure, Unset):
            unit_of_measure = self.unit_of_measure.to_dict()

        udf_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.udf_code, Unset):
            udf_code = self.udf_code.to_dict()

        udf_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.udf_type, Unset):
            udf_type = self.udf_type.to_dict()

        wbs_category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wbs_category, Unset):
            wbs_category = self.wbs_category.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity_code is not UNSET:
            field_dict["ActivityCode"] = activity_code
        if activity_code_type is not UNSET:
            field_dict["ActivityCodeType"] = activity_code_type
        if activity_code_type_eps is not UNSET:
            field_dict["ActivityCodeTypeEPS"] = activity_code_type_eps
        if calendar is not UNSET:
            field_dict["Calendar"] = calendar
        if calendar_rsrc is not UNSET:
            field_dict["CalendarRsrc"] = calendar_rsrc
        if cost_account is not UNSET:
            field_dict["CostAccount"] = cost_account
        if currency is not UNSET:
            field_dict["Currency"] = currency
        if document_category is not UNSET:
            field_dict["DocumentCategory"] = document_category
        if document_status_code is not UNSET:
            field_dict["DocumentStatusCode"] = document_status_code
        if expense_category is not UNSET:
            field_dict["ExpenseCategory"] = expense_category
        if financial_period is not UNSET:
            field_dict["FinancialPeriod"] = financial_period
        if funding_source is not UNSET:
            field_dict["FundingSource"] = funding_source
        if notebook_topic is not UNSET:
            field_dict["NotebookTopic"] = notebook_topic
        if obs is not UNSET:
            field_dict["OBS"] = obs
        if project_code is not UNSET:
            field_dict["ProjectCode"] = project_code
        if project_code_type is not UNSET:
            field_dict["ProjectCodeType"] = project_code_type
        if project_resource_category is not UNSET:
            field_dict["ProjectResourceCategory"] = project_resource_category
        if resource is not UNSET:
            field_dict["Resource"] = resource
        if resource_code is not UNSET:
            field_dict["ResourceCode"] = resource_code
        if resource_code_type is not UNSET:
            field_dict["ResourceCodeType"] = resource_code_type
        if resource_curve is not UNSET:
            field_dict["ResourceCurve"] = resource_curve
        if resource_rate is not UNSET:
            field_dict["ResourceRate"] = resource_rate
        if resource_role is not UNSET:
            field_dict["ResourceRole"] = resource_role
        if risk_category is not UNSET:
            field_dict["RiskCategory"] = risk_category
        if risk_matrix_score is not UNSET:
            field_dict["RiskMatrixScore"] = risk_matrix_score
        if risk_matrix_threshold is not UNSET:
            field_dict["RiskMatrixThreshold"] = risk_matrix_threshold
        if risk_matrix is not UNSET:
            field_dict["RiskMatrix"] = risk_matrix
        if risk_threshold is not UNSET:
            field_dict["RiskThreshold"] = risk_threshold
        if risk_threshold_level is not UNSET:
            field_dict["RiskThresholdLevel"] = risk_threshold_level
        if role is not UNSET:
            field_dict["Role"] = role
        if role_rate is not UNSET:
            field_dict["RoleRate"] = role_rate
        if role_limit is not UNSET:
            field_dict["RoleLimit"] = role_limit
        if shift is not UNSET:
            field_dict["Shift"] = shift
        if threshold_parameter is not UNSET:
            field_dict["ThresholdParameter"] = threshold_parameter
        if unit_of_measure is not UNSET:
            field_dict["UnitOfMeasure"] = unit_of_measure
        if udf_code is not UNSET:
            field_dict["UDFCode"] = udf_code
        if udf_type is not UNSET:
            field_dict["UDFType"] = udf_type
        if wbs_category is not UNSET:
            field_dict["WBSCategory"] = wbs_category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.business_object_type import BusinessObjectType

        d = dict(src_dict)
        _activity_code = d.pop("ActivityCode", UNSET)
        activity_code: BusinessObjectType | Unset
        if isinstance(_activity_code, Unset):
            activity_code = UNSET
        else:
            activity_code = BusinessObjectType.from_dict(_activity_code)

        _activity_code_type = d.pop("ActivityCodeType", UNSET)
        activity_code_type: BusinessObjectType | Unset
        if isinstance(_activity_code_type, Unset):
            activity_code_type = UNSET
        else:
            activity_code_type = BusinessObjectType.from_dict(_activity_code_type)

        _activity_code_type_eps = d.pop("ActivityCodeTypeEPS", UNSET)
        activity_code_type_eps: BusinessObjectType | Unset
        if isinstance(_activity_code_type_eps, Unset):
            activity_code_type_eps = UNSET
        else:
            activity_code_type_eps = BusinessObjectType.from_dict(_activity_code_type_eps)

        _calendar = d.pop("Calendar", UNSET)
        calendar: BusinessObjectType | Unset
        if isinstance(_calendar, Unset):
            calendar = UNSET
        else:
            calendar = BusinessObjectType.from_dict(_calendar)

        _calendar_rsrc = d.pop("CalendarRsrc", UNSET)
        calendar_rsrc: BusinessObjectType | Unset
        if isinstance(_calendar_rsrc, Unset):
            calendar_rsrc = UNSET
        else:
            calendar_rsrc = BusinessObjectType.from_dict(_calendar_rsrc)

        _cost_account = d.pop("CostAccount", UNSET)
        cost_account: BusinessObjectType | Unset
        if isinstance(_cost_account, Unset):
            cost_account = UNSET
        else:
            cost_account = BusinessObjectType.from_dict(_cost_account)

        _currency = d.pop("Currency", UNSET)
        currency: BusinessObjectType | Unset
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = BusinessObjectType.from_dict(_currency)

        _document_category = d.pop("DocumentCategory", UNSET)
        document_category: BusinessObjectType | Unset
        if isinstance(_document_category, Unset):
            document_category = UNSET
        else:
            document_category = BusinessObjectType.from_dict(_document_category)

        _document_status_code = d.pop("DocumentStatusCode", UNSET)
        document_status_code: BusinessObjectType | Unset
        if isinstance(_document_status_code, Unset):
            document_status_code = UNSET
        else:
            document_status_code = BusinessObjectType.from_dict(_document_status_code)

        _expense_category = d.pop("ExpenseCategory", UNSET)
        expense_category: BusinessObjectType | Unset
        if isinstance(_expense_category, Unset):
            expense_category = UNSET
        else:
            expense_category = BusinessObjectType.from_dict(_expense_category)

        _financial_period = d.pop("FinancialPeriod", UNSET)
        financial_period: BusinessObjectType | Unset
        if isinstance(_financial_period, Unset):
            financial_period = UNSET
        else:
            financial_period = BusinessObjectType.from_dict(_financial_period)

        _funding_source = d.pop("FundingSource", UNSET)
        funding_source: BusinessObjectType | Unset
        if isinstance(_funding_source, Unset):
            funding_source = UNSET
        else:
            funding_source = BusinessObjectType.from_dict(_funding_source)

        _notebook_topic = d.pop("NotebookTopic", UNSET)
        notebook_topic: BusinessObjectType | Unset
        if isinstance(_notebook_topic, Unset):
            notebook_topic = UNSET
        else:
            notebook_topic = BusinessObjectType.from_dict(_notebook_topic)

        _obs = d.pop("OBS", UNSET)
        obs: BusinessObjectType | Unset
        if isinstance(_obs, Unset):
            obs = UNSET
        else:
            obs = BusinessObjectType.from_dict(_obs)

        _project_code = d.pop("ProjectCode", UNSET)
        project_code: BusinessObjectType | Unset
        if isinstance(_project_code, Unset):
            project_code = UNSET
        else:
            project_code = BusinessObjectType.from_dict(_project_code)

        _project_code_type = d.pop("ProjectCodeType", UNSET)
        project_code_type: BusinessObjectType | Unset
        if isinstance(_project_code_type, Unset):
            project_code_type = UNSET
        else:
            project_code_type = BusinessObjectType.from_dict(_project_code_type)

        _project_resource_category = d.pop("ProjectResourceCategory", UNSET)
        project_resource_category: BusinessObjectType | Unset
        if isinstance(_project_resource_category, Unset):
            project_resource_category = UNSET
        else:
            project_resource_category = BusinessObjectType.from_dict(_project_resource_category)

        _resource = d.pop("Resource", UNSET)
        resource: BusinessObjectType | Unset
        if isinstance(_resource, Unset):
            resource = UNSET
        else:
            resource = BusinessObjectType.from_dict(_resource)

        _resource_code = d.pop("ResourceCode", UNSET)
        resource_code: BusinessObjectType | Unset
        if isinstance(_resource_code, Unset):
            resource_code = UNSET
        else:
            resource_code = BusinessObjectType.from_dict(_resource_code)

        _resource_code_type = d.pop("ResourceCodeType", UNSET)
        resource_code_type: BusinessObjectType | Unset
        if isinstance(_resource_code_type, Unset):
            resource_code_type = UNSET
        else:
            resource_code_type = BusinessObjectType.from_dict(_resource_code_type)

        _resource_curve = d.pop("ResourceCurve", UNSET)
        resource_curve: BusinessObjectType | Unset
        if isinstance(_resource_curve, Unset):
            resource_curve = UNSET
        else:
            resource_curve = BusinessObjectType.from_dict(_resource_curve)

        _resource_rate = d.pop("ResourceRate", UNSET)
        resource_rate: BusinessObjectType | Unset
        if isinstance(_resource_rate, Unset):
            resource_rate = UNSET
        else:
            resource_rate = BusinessObjectType.from_dict(_resource_rate)

        _resource_role = d.pop("ResourceRole", UNSET)
        resource_role: BusinessObjectType | Unset
        if isinstance(_resource_role, Unset):
            resource_role = UNSET
        else:
            resource_role = BusinessObjectType.from_dict(_resource_role)

        _risk_category = d.pop("RiskCategory", UNSET)
        risk_category: BusinessObjectType | Unset
        if isinstance(_risk_category, Unset):
            risk_category = UNSET
        else:
            risk_category = BusinessObjectType.from_dict(_risk_category)

        _risk_matrix_score = d.pop("RiskMatrixScore", UNSET)
        risk_matrix_score: BusinessObjectType | Unset
        if isinstance(_risk_matrix_score, Unset):
            risk_matrix_score = UNSET
        else:
            risk_matrix_score = BusinessObjectType.from_dict(_risk_matrix_score)

        _risk_matrix_threshold = d.pop("RiskMatrixThreshold", UNSET)
        risk_matrix_threshold: BusinessObjectType | Unset
        if isinstance(_risk_matrix_threshold, Unset):
            risk_matrix_threshold = UNSET
        else:
            risk_matrix_threshold = BusinessObjectType.from_dict(_risk_matrix_threshold)

        _risk_matrix = d.pop("RiskMatrix", UNSET)
        risk_matrix: BusinessObjectType | Unset
        if isinstance(_risk_matrix, Unset):
            risk_matrix = UNSET
        else:
            risk_matrix = BusinessObjectType.from_dict(_risk_matrix)

        _risk_threshold = d.pop("RiskThreshold", UNSET)
        risk_threshold: BusinessObjectType | Unset
        if isinstance(_risk_threshold, Unset):
            risk_threshold = UNSET
        else:
            risk_threshold = BusinessObjectType.from_dict(_risk_threshold)

        _risk_threshold_level = d.pop("RiskThresholdLevel", UNSET)
        risk_threshold_level: BusinessObjectType | Unset
        if isinstance(_risk_threshold_level, Unset):
            risk_threshold_level = UNSET
        else:
            risk_threshold_level = BusinessObjectType.from_dict(_risk_threshold_level)

        _role = d.pop("Role", UNSET)
        role: BusinessObjectType | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = BusinessObjectType.from_dict(_role)

        _role_rate = d.pop("RoleRate", UNSET)
        role_rate: BusinessObjectType | Unset
        if isinstance(_role_rate, Unset):
            role_rate = UNSET
        else:
            role_rate = BusinessObjectType.from_dict(_role_rate)

        _role_limit = d.pop("RoleLimit", UNSET)
        role_limit: BusinessObjectType | Unset
        if isinstance(_role_limit, Unset):
            role_limit = UNSET
        else:
            role_limit = BusinessObjectType.from_dict(_role_limit)

        _shift = d.pop("Shift", UNSET)
        shift: BusinessObjectType | Unset
        if isinstance(_shift, Unset):
            shift = UNSET
        else:
            shift = BusinessObjectType.from_dict(_shift)

        _threshold_parameter = d.pop("ThresholdParameter", UNSET)
        threshold_parameter: BusinessObjectType | Unset
        if isinstance(_threshold_parameter, Unset):
            threshold_parameter = UNSET
        else:
            threshold_parameter = BusinessObjectType.from_dict(_threshold_parameter)

        _unit_of_measure = d.pop("UnitOfMeasure", UNSET)
        unit_of_measure: BusinessObjectType | Unset
        if isinstance(_unit_of_measure, Unset):
            unit_of_measure = UNSET
        else:
            unit_of_measure = BusinessObjectType.from_dict(_unit_of_measure)

        _udf_code = d.pop("UDFCode", UNSET)
        udf_code: BusinessObjectType | Unset
        if isinstance(_udf_code, Unset):
            udf_code = UNSET
        else:
            udf_code = BusinessObjectType.from_dict(_udf_code)

        _udf_type = d.pop("UDFType", UNSET)
        udf_type: BusinessObjectType | Unset
        if isinstance(_udf_type, Unset):
            udf_type = UNSET
        else:
            udf_type = BusinessObjectType.from_dict(_udf_type)

        _wbs_category = d.pop("WBSCategory", UNSET)
        wbs_category: BusinessObjectType | Unset
        if isinstance(_wbs_category, Unset):
            wbs_category = UNSET
        else:
            wbs_category = BusinessObjectType.from_dict(_wbs_category)

        global_business_object_options = cls(
            activity_code=activity_code,
            activity_code_type=activity_code_type,
            activity_code_type_eps=activity_code_type_eps,
            calendar=calendar,
            calendar_rsrc=calendar_rsrc,
            cost_account=cost_account,
            currency=currency,
            document_category=document_category,
            document_status_code=document_status_code,
            expense_category=expense_category,
            financial_period=financial_period,
            funding_source=funding_source,
            notebook_topic=notebook_topic,
            obs=obs,
            project_code=project_code,
            project_code_type=project_code_type,
            project_resource_category=project_resource_category,
            resource=resource,
            resource_code=resource_code,
            resource_code_type=resource_code_type,
            resource_curve=resource_curve,
            resource_rate=resource_rate,
            resource_role=resource_role,
            risk_category=risk_category,
            risk_matrix_score=risk_matrix_score,
            risk_matrix_threshold=risk_matrix_threshold,
            risk_matrix=risk_matrix,
            risk_threshold=risk_threshold,
            risk_threshold_level=risk_threshold_level,
            role=role,
            role_rate=role_rate,
            role_limit=role_limit,
            shift=shift,
            threshold_parameter=threshold_parameter,
            unit_of_measure=unit_of_measure,
            udf_code=udf_code,
            udf_type=udf_type,
            wbs_category=wbs_category,
        )

        global_business_object_options.additional_properties = d
        return global_business_object_options

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
