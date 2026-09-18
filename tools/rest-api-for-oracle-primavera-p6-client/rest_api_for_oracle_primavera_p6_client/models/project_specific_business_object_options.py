from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.business_object_type import BusinessObjectType
    from ..models.delete_unreferenced_type import DeleteUnreferencedType


T = TypeVar("T", bound="ProjectSpecificBusinessObjectOptions")


@_attrs_define
class ProjectSpecificBusinessObjectOptions:
    """
    Attributes:
        activity (DeleteUnreferencedType | Unset):
        activity_code (BusinessObjectType | Unset): BusinessObjectType Entity
        activity_code_type (BusinessObjectType | Unset): BusinessObjectType Entity
        activity_expense (BusinessObjectType | Unset): BusinessObjectType Entity
        activity_note (BusinessObjectType | Unset): BusinessObjectType Entity
        activity_period_actual (BusinessObjectType | Unset): BusinessObjectType Entity
        activity_risk (BusinessObjectType | Unset): BusinessObjectType Entity
        activity_step (BusinessObjectType | Unset): BusinessObjectType Entity
        calendar (BusinessObjectType | Unset): BusinessObjectType Entity
        document (BusinessObjectType | Unset): BusinessObjectType Entity
        project_budget_change_log (BusinessObjectType | Unset): BusinessObjectType Entity
        project_funding (BusinessObjectType | Unset): BusinessObjectType Entity
        project_issue (BusinessObjectType | Unset): BusinessObjectType Entity
        project_note (BusinessObjectType | Unset): BusinessObjectType Entity
        project_resource (BusinessObjectType | Unset): BusinessObjectType Entity
        project_resource_quantity (BusinessObjectType | Unset): BusinessObjectType Entity
        project_spending_plan (BusinessObjectType | Unset): BusinessObjectType Entity
        project_threshold (DeleteUnreferencedType | Unset):
        relationship (DeleteUnreferencedType | Unset):
        ext_relationship (DeleteUnreferencedType | Unset):
        resource_assignment (DeleteUnreferencedType | Unset):
        resource_assignment_period_actual (BusinessObjectType | Unset): BusinessObjectType Entity
        risk (BusinessObjectType | Unset): BusinessObjectType Entity
        risk_impact (BusinessObjectType | Unset): BusinessObjectType Entity
        risk_response_action (BusinessObjectType | Unset): BusinessObjectType Entity
        risk_response_action_impact (BusinessObjectType | Unset): BusinessObjectType Entity
        risk_response_plan (BusinessObjectType | Unset): BusinessObjectType Entity
        wbs (BusinessObjectType | Unset): BusinessObjectType Entity
        wbs_milestone (BusinessObjectType | Unset): BusinessObjectType Entity
    """

    activity: DeleteUnreferencedType | Unset = UNSET
    activity_code: BusinessObjectType | Unset = UNSET
    activity_code_type: BusinessObjectType | Unset = UNSET
    activity_expense: BusinessObjectType | Unset = UNSET
    activity_note: BusinessObjectType | Unset = UNSET
    activity_period_actual: BusinessObjectType | Unset = UNSET
    activity_risk: BusinessObjectType | Unset = UNSET
    activity_step: BusinessObjectType | Unset = UNSET
    calendar: BusinessObjectType | Unset = UNSET
    document: BusinessObjectType | Unset = UNSET
    project_budget_change_log: BusinessObjectType | Unset = UNSET
    project_funding: BusinessObjectType | Unset = UNSET
    project_issue: BusinessObjectType | Unset = UNSET
    project_note: BusinessObjectType | Unset = UNSET
    project_resource: BusinessObjectType | Unset = UNSET
    project_resource_quantity: BusinessObjectType | Unset = UNSET
    project_spending_plan: BusinessObjectType | Unset = UNSET
    project_threshold: DeleteUnreferencedType | Unset = UNSET
    relationship: DeleteUnreferencedType | Unset = UNSET
    ext_relationship: DeleteUnreferencedType | Unset = UNSET
    resource_assignment: DeleteUnreferencedType | Unset = UNSET
    resource_assignment_period_actual: BusinessObjectType | Unset = UNSET
    risk: BusinessObjectType | Unset = UNSET
    risk_impact: BusinessObjectType | Unset = UNSET
    risk_response_action: BusinessObjectType | Unset = UNSET
    risk_response_action_impact: BusinessObjectType | Unset = UNSET
    risk_response_plan: BusinessObjectType | Unset = UNSET
    wbs: BusinessObjectType | Unset = UNSET
    wbs_milestone: BusinessObjectType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.activity, Unset):
            activity = self.activity.to_dict()

        activity_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.activity_code, Unset):
            activity_code = self.activity_code.to_dict()

        activity_code_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.activity_code_type, Unset):
            activity_code_type = self.activity_code_type.to_dict()

        activity_expense: dict[str, Any] | Unset = UNSET
        if not isinstance(self.activity_expense, Unset):
            activity_expense = self.activity_expense.to_dict()

        activity_note: dict[str, Any] | Unset = UNSET
        if not isinstance(self.activity_note, Unset):
            activity_note = self.activity_note.to_dict()

        activity_period_actual: dict[str, Any] | Unset = UNSET
        if not isinstance(self.activity_period_actual, Unset):
            activity_period_actual = self.activity_period_actual.to_dict()

        activity_risk: dict[str, Any] | Unset = UNSET
        if not isinstance(self.activity_risk, Unset):
            activity_risk = self.activity_risk.to_dict()

        activity_step: dict[str, Any] | Unset = UNSET
        if not isinstance(self.activity_step, Unset):
            activity_step = self.activity_step.to_dict()

        calendar: dict[str, Any] | Unset = UNSET
        if not isinstance(self.calendar, Unset):
            calendar = self.calendar.to_dict()

        document: dict[str, Any] | Unset = UNSET
        if not isinstance(self.document, Unset):
            document = self.document.to_dict()

        project_budget_change_log: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_budget_change_log, Unset):
            project_budget_change_log = self.project_budget_change_log.to_dict()

        project_funding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_funding, Unset):
            project_funding = self.project_funding.to_dict()

        project_issue: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_issue, Unset):
            project_issue = self.project_issue.to_dict()

        project_note: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_note, Unset):
            project_note = self.project_note.to_dict()

        project_resource: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_resource, Unset):
            project_resource = self.project_resource.to_dict()

        project_resource_quantity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_resource_quantity, Unset):
            project_resource_quantity = self.project_resource_quantity.to_dict()

        project_spending_plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_spending_plan, Unset):
            project_spending_plan = self.project_spending_plan.to_dict()

        project_threshold: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_threshold, Unset):
            project_threshold = self.project_threshold.to_dict()

        relationship: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relationship, Unset):
            relationship = self.relationship.to_dict()

        ext_relationship: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ext_relationship, Unset):
            ext_relationship = self.ext_relationship.to_dict()

        resource_assignment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource_assignment, Unset):
            resource_assignment = self.resource_assignment.to_dict()

        resource_assignment_period_actual: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource_assignment_period_actual, Unset):
            resource_assignment_period_actual = self.resource_assignment_period_actual.to_dict()

        risk: dict[str, Any] | Unset = UNSET
        if not isinstance(self.risk, Unset):
            risk = self.risk.to_dict()

        risk_impact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.risk_impact, Unset):
            risk_impact = self.risk_impact.to_dict()

        risk_response_action: dict[str, Any] | Unset = UNSET
        if not isinstance(self.risk_response_action, Unset):
            risk_response_action = self.risk_response_action.to_dict()

        risk_response_action_impact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.risk_response_action_impact, Unset):
            risk_response_action_impact = self.risk_response_action_impact.to_dict()

        risk_response_plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.risk_response_plan, Unset):
            risk_response_plan = self.risk_response_plan.to_dict()

        wbs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wbs, Unset):
            wbs = self.wbs.to_dict()

        wbs_milestone: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wbs_milestone, Unset):
            wbs_milestone = self.wbs_milestone.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity is not UNSET:
            field_dict["Activity"] = activity
        if activity_code is not UNSET:
            field_dict["ActivityCode"] = activity_code
        if activity_code_type is not UNSET:
            field_dict["ActivityCodeType"] = activity_code_type
        if activity_expense is not UNSET:
            field_dict["ActivityExpense"] = activity_expense
        if activity_note is not UNSET:
            field_dict["ActivityNote"] = activity_note
        if activity_period_actual is not UNSET:
            field_dict["ActivityPeriodActual"] = activity_period_actual
        if activity_risk is not UNSET:
            field_dict["ActivityRisk"] = activity_risk
        if activity_step is not UNSET:
            field_dict["ActivityStep"] = activity_step
        if calendar is not UNSET:
            field_dict["Calendar"] = calendar
        if document is not UNSET:
            field_dict["Document"] = document
        if project_budget_change_log is not UNSET:
            field_dict["ProjectBudgetChangeLog"] = project_budget_change_log
        if project_funding is not UNSET:
            field_dict["ProjectFunding"] = project_funding
        if project_issue is not UNSET:
            field_dict["ProjectIssue"] = project_issue
        if project_note is not UNSET:
            field_dict["ProjectNote"] = project_note
        if project_resource is not UNSET:
            field_dict["ProjectResource"] = project_resource
        if project_resource_quantity is not UNSET:
            field_dict["ProjectResourceQuantity"] = project_resource_quantity
        if project_spending_plan is not UNSET:
            field_dict["ProjectSpendingPlan"] = project_spending_plan
        if project_threshold is not UNSET:
            field_dict["ProjectThreshold"] = project_threshold
        if relationship is not UNSET:
            field_dict["Relationship"] = relationship
        if ext_relationship is not UNSET:
            field_dict["ExtRelationship"] = ext_relationship
        if resource_assignment is not UNSET:
            field_dict["ResourceAssignment"] = resource_assignment
        if resource_assignment_period_actual is not UNSET:
            field_dict["ResourceAssignmentPeriodActual"] = resource_assignment_period_actual
        if risk is not UNSET:
            field_dict["Risk"] = risk
        if risk_impact is not UNSET:
            field_dict["RiskImpact"] = risk_impact
        if risk_response_action is not UNSET:
            field_dict["RiskResponseAction"] = risk_response_action
        if risk_response_action_impact is not UNSET:
            field_dict["RiskResponseActionImpact"] = risk_response_action_impact
        if risk_response_plan is not UNSET:
            field_dict["RiskResponsePlan"] = risk_response_plan
        if wbs is not UNSET:
            field_dict["WBS"] = wbs
        if wbs_milestone is not UNSET:
            field_dict["WBSMilestone"] = wbs_milestone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.business_object_type import BusinessObjectType
        from ..models.delete_unreferenced_type import DeleteUnreferencedType

        d = dict(src_dict)
        _activity = d.pop("Activity", UNSET)
        activity: DeleteUnreferencedType | Unset
        if isinstance(_activity, Unset):
            activity = UNSET
        else:
            activity = DeleteUnreferencedType.from_dict(_activity)

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

        _activity_expense = d.pop("ActivityExpense", UNSET)
        activity_expense: BusinessObjectType | Unset
        if isinstance(_activity_expense, Unset):
            activity_expense = UNSET
        else:
            activity_expense = BusinessObjectType.from_dict(_activity_expense)

        _activity_note = d.pop("ActivityNote", UNSET)
        activity_note: BusinessObjectType | Unset
        if isinstance(_activity_note, Unset):
            activity_note = UNSET
        else:
            activity_note = BusinessObjectType.from_dict(_activity_note)

        _activity_period_actual = d.pop("ActivityPeriodActual", UNSET)
        activity_period_actual: BusinessObjectType | Unset
        if isinstance(_activity_period_actual, Unset):
            activity_period_actual = UNSET
        else:
            activity_period_actual = BusinessObjectType.from_dict(_activity_period_actual)

        _activity_risk = d.pop("ActivityRisk", UNSET)
        activity_risk: BusinessObjectType | Unset
        if isinstance(_activity_risk, Unset):
            activity_risk = UNSET
        else:
            activity_risk = BusinessObjectType.from_dict(_activity_risk)

        _activity_step = d.pop("ActivityStep", UNSET)
        activity_step: BusinessObjectType | Unset
        if isinstance(_activity_step, Unset):
            activity_step = UNSET
        else:
            activity_step = BusinessObjectType.from_dict(_activity_step)

        _calendar = d.pop("Calendar", UNSET)
        calendar: BusinessObjectType | Unset
        if isinstance(_calendar, Unset):
            calendar = UNSET
        else:
            calendar = BusinessObjectType.from_dict(_calendar)

        _document = d.pop("Document", UNSET)
        document: BusinessObjectType | Unset
        if isinstance(_document, Unset):
            document = UNSET
        else:
            document = BusinessObjectType.from_dict(_document)

        _project_budget_change_log = d.pop("ProjectBudgetChangeLog", UNSET)
        project_budget_change_log: BusinessObjectType | Unset
        if isinstance(_project_budget_change_log, Unset):
            project_budget_change_log = UNSET
        else:
            project_budget_change_log = BusinessObjectType.from_dict(_project_budget_change_log)

        _project_funding = d.pop("ProjectFunding", UNSET)
        project_funding: BusinessObjectType | Unset
        if isinstance(_project_funding, Unset):
            project_funding = UNSET
        else:
            project_funding = BusinessObjectType.from_dict(_project_funding)

        _project_issue = d.pop("ProjectIssue", UNSET)
        project_issue: BusinessObjectType | Unset
        if isinstance(_project_issue, Unset):
            project_issue = UNSET
        else:
            project_issue = BusinessObjectType.from_dict(_project_issue)

        _project_note = d.pop("ProjectNote", UNSET)
        project_note: BusinessObjectType | Unset
        if isinstance(_project_note, Unset):
            project_note = UNSET
        else:
            project_note = BusinessObjectType.from_dict(_project_note)

        _project_resource = d.pop("ProjectResource", UNSET)
        project_resource: BusinessObjectType | Unset
        if isinstance(_project_resource, Unset):
            project_resource = UNSET
        else:
            project_resource = BusinessObjectType.from_dict(_project_resource)

        _project_resource_quantity = d.pop("ProjectResourceQuantity", UNSET)
        project_resource_quantity: BusinessObjectType | Unset
        if isinstance(_project_resource_quantity, Unset):
            project_resource_quantity = UNSET
        else:
            project_resource_quantity = BusinessObjectType.from_dict(_project_resource_quantity)

        _project_spending_plan = d.pop("ProjectSpendingPlan", UNSET)
        project_spending_plan: BusinessObjectType | Unset
        if isinstance(_project_spending_plan, Unset):
            project_spending_plan = UNSET
        else:
            project_spending_plan = BusinessObjectType.from_dict(_project_spending_plan)

        _project_threshold = d.pop("ProjectThreshold", UNSET)
        project_threshold: DeleteUnreferencedType | Unset
        if isinstance(_project_threshold, Unset):
            project_threshold = UNSET
        else:
            project_threshold = DeleteUnreferencedType.from_dict(_project_threshold)

        _relationship = d.pop("Relationship", UNSET)
        relationship: DeleteUnreferencedType | Unset
        if isinstance(_relationship, Unset):
            relationship = UNSET
        else:
            relationship = DeleteUnreferencedType.from_dict(_relationship)

        _ext_relationship = d.pop("ExtRelationship", UNSET)
        ext_relationship: DeleteUnreferencedType | Unset
        if isinstance(_ext_relationship, Unset):
            ext_relationship = UNSET
        else:
            ext_relationship = DeleteUnreferencedType.from_dict(_ext_relationship)

        _resource_assignment = d.pop("ResourceAssignment", UNSET)
        resource_assignment: DeleteUnreferencedType | Unset
        if isinstance(_resource_assignment, Unset):
            resource_assignment = UNSET
        else:
            resource_assignment = DeleteUnreferencedType.from_dict(_resource_assignment)

        _resource_assignment_period_actual = d.pop("ResourceAssignmentPeriodActual", UNSET)
        resource_assignment_period_actual: BusinessObjectType | Unset
        if isinstance(_resource_assignment_period_actual, Unset):
            resource_assignment_period_actual = UNSET
        else:
            resource_assignment_period_actual = BusinessObjectType.from_dict(_resource_assignment_period_actual)

        _risk = d.pop("Risk", UNSET)
        risk: BusinessObjectType | Unset
        if isinstance(_risk, Unset):
            risk = UNSET
        else:
            risk = BusinessObjectType.from_dict(_risk)

        _risk_impact = d.pop("RiskImpact", UNSET)
        risk_impact: BusinessObjectType | Unset
        if isinstance(_risk_impact, Unset):
            risk_impact = UNSET
        else:
            risk_impact = BusinessObjectType.from_dict(_risk_impact)

        _risk_response_action = d.pop("RiskResponseAction", UNSET)
        risk_response_action: BusinessObjectType | Unset
        if isinstance(_risk_response_action, Unset):
            risk_response_action = UNSET
        else:
            risk_response_action = BusinessObjectType.from_dict(_risk_response_action)

        _risk_response_action_impact = d.pop("RiskResponseActionImpact", UNSET)
        risk_response_action_impact: BusinessObjectType | Unset
        if isinstance(_risk_response_action_impact, Unset):
            risk_response_action_impact = UNSET
        else:
            risk_response_action_impact = BusinessObjectType.from_dict(_risk_response_action_impact)

        _risk_response_plan = d.pop("RiskResponsePlan", UNSET)
        risk_response_plan: BusinessObjectType | Unset
        if isinstance(_risk_response_plan, Unset):
            risk_response_plan = UNSET
        else:
            risk_response_plan = BusinessObjectType.from_dict(_risk_response_plan)

        _wbs = d.pop("WBS", UNSET)
        wbs: BusinessObjectType | Unset
        if isinstance(_wbs, Unset):
            wbs = UNSET
        else:
            wbs = BusinessObjectType.from_dict(_wbs)

        _wbs_milestone = d.pop("WBSMilestone", UNSET)
        wbs_milestone: BusinessObjectType | Unset
        if isinstance(_wbs_milestone, Unset):
            wbs_milestone = UNSET
        else:
            wbs_milestone = BusinessObjectType.from_dict(_wbs_milestone)

        project_specific_business_object_options = cls(
            activity=activity,
            activity_code=activity_code,
            activity_code_type=activity_code_type,
            activity_expense=activity_expense,
            activity_note=activity_note,
            activity_period_actual=activity_period_actual,
            activity_risk=activity_risk,
            activity_step=activity_step,
            calendar=calendar,
            document=document,
            project_budget_change_log=project_budget_change_log,
            project_funding=project_funding,
            project_issue=project_issue,
            project_note=project_note,
            project_resource=project_resource,
            project_resource_quantity=project_resource_quantity,
            project_spending_plan=project_spending_plan,
            project_threshold=project_threshold,
            relationship=relationship,
            ext_relationship=ext_relationship,
            resource_assignment=resource_assignment,
            resource_assignment_period_actual=resource_assignment_period_actual,
            risk=risk,
            risk_impact=risk_impact,
            risk_response_action=risk_response_action,
            risk_response_action_impact=risk_response_action_impact,
            risk_response_plan=risk_response_plan,
            wbs=wbs,
            wbs_milestone=wbs_milestone,
        )

        project_specific_business_object_options.additional_properties = d
        return project_specific_business_object_options

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
