# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'AutomationRuleModifyPropertiesActionActionConfigurationArgs',
    'AutomationRuleModifyPropertiesActionArgs',
    'AutomationRulePropertyValuesConditionConditionPropertiesArgs',
    'AutomationRulePropertyValuesConditionArgs',
    'AutomationRuleRunPlaybookActionActionConfigurationArgs',
    'AutomationRuleRunPlaybookActionArgs',
    'AutomationRuleTriggeringLogicArgs',
    'IncidentInfoArgs',
    'IncidentLabelArgs',
    'IncidentOwnerInfoArgs',
    'UserInfoArgs',
    'WatchlistUserInfoArgs',
]

@pulumi.input_type
class AutomationRuleModifyPropertiesActionActionConfigurationArgs:
    def __init__(__self__, *,
                 classification: Optional[pulumi.Input[Union[str, 'IncidentClassification']]] = None,
                 classification_comment: Optional[pulumi.Input[str]] = None,
                 classification_reason: Optional[pulumi.Input[Union[str, 'IncidentClassificationReason']]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input['IncidentLabelArgs']]]] = None,
                 owner: Optional[pulumi.Input['IncidentOwnerInfoArgs']] = None,
                 severity: Optional[pulumi.Input[Union[str, 'IncidentSeverity']]] = None,
                 status: Optional[pulumi.Input[Union[str, 'IncidentStatus']]] = None):
        """
        The configuration of the modify properties automation rule action
        :param pulumi.Input[Union[str, 'IncidentClassification']] classification: The reason the incident was closed
        :param pulumi.Input[str] classification_comment: Describes the reason the incident was closed
        :param pulumi.Input[Union[str, 'IncidentClassificationReason']] classification_reason: The classification reason to close the incident with
        :param pulumi.Input[Sequence[pulumi.Input['IncidentLabelArgs']]] labels: List of labels to add to the incident
        :param pulumi.Input['IncidentOwnerInfoArgs'] owner: Describes a user that the incident is assigned to
        :param pulumi.Input[Union[str, 'IncidentSeverity']] severity: The severity of the incident
        :param pulumi.Input[Union[str, 'IncidentStatus']] status: The status of the incident
        """
        if classification is not None:
            pulumi.set(__self__, "classification", classification)
        if classification_comment is not None:
            pulumi.set(__self__, "classification_comment", classification_comment)
        if classification_reason is not None:
            pulumi.set(__self__, "classification_reason", classification_reason)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)
        if severity is not None:
            pulumi.set(__self__, "severity", severity)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def classification(self) -> Optional[pulumi.Input[Union[str, 'IncidentClassification']]]:
        """
        The reason the incident was closed
        """
        return pulumi.get(self, "classification")

    @classification.setter
    def classification(self, value: Optional[pulumi.Input[Union[str, 'IncidentClassification']]]):
        pulumi.set(self, "classification", value)

    @property
    @pulumi.getter(name="classificationComment")
    def classification_comment(self) -> Optional[pulumi.Input[str]]:
        """
        Describes the reason the incident was closed
        """
        return pulumi.get(self, "classification_comment")

    @classification_comment.setter
    def classification_comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "classification_comment", value)

    @property
    @pulumi.getter(name="classificationReason")
    def classification_reason(self) -> Optional[pulumi.Input[Union[str, 'IncidentClassificationReason']]]:
        """
        The classification reason to close the incident with
        """
        return pulumi.get(self, "classification_reason")

    @classification_reason.setter
    def classification_reason(self, value: Optional[pulumi.Input[Union[str, 'IncidentClassificationReason']]]):
        pulumi.set(self, "classification_reason", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IncidentLabelArgs']]]]:
        """
        List of labels to add to the incident
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IncidentLabelArgs']]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input['IncidentOwnerInfoArgs']]:
        """
        Describes a user that the incident is assigned to
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input['IncidentOwnerInfoArgs']]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[Union[str, 'IncidentSeverity']]]:
        """
        The severity of the incident
        """
        return pulumi.get(self, "severity")

    @severity.setter
    def severity(self, value: Optional[pulumi.Input[Union[str, 'IncidentSeverity']]]):
        pulumi.set(self, "severity", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'IncidentStatus']]]:
        """
        The status of the incident
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'IncidentStatus']]]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class AutomationRuleModifyPropertiesActionArgs:
    def __init__(__self__, *,
                 action_configuration: pulumi.Input['AutomationRuleModifyPropertiesActionActionConfigurationArgs'],
                 action_type: pulumi.Input[str],
                 order: pulumi.Input[int]):
        """
        Describes an automation rule action to modify an object's properties
        :param pulumi.Input['AutomationRuleModifyPropertiesActionActionConfigurationArgs'] action_configuration: The configuration of the modify properties automation rule action
        :param pulumi.Input[str] action_type: The type of the automation rule action
               Expected value is 'ModifyProperties'.
        :param pulumi.Input[int] order: The order of execution of the automation rule action
        """
        pulumi.set(__self__, "action_configuration", action_configuration)
        pulumi.set(__self__, "action_type", 'ModifyProperties')
        pulumi.set(__self__, "order", order)

    @property
    @pulumi.getter(name="actionConfiguration")
    def action_configuration(self) -> pulumi.Input['AutomationRuleModifyPropertiesActionActionConfigurationArgs']:
        """
        The configuration of the modify properties automation rule action
        """
        return pulumi.get(self, "action_configuration")

    @action_configuration.setter
    def action_configuration(self, value: pulumi.Input['AutomationRuleModifyPropertiesActionActionConfigurationArgs']):
        pulumi.set(self, "action_configuration", value)

    @property
    @pulumi.getter(name="actionType")
    def action_type(self) -> pulumi.Input[str]:
        """
        The type of the automation rule action
        Expected value is 'ModifyProperties'.
        """
        return pulumi.get(self, "action_type")

    @action_type.setter
    def action_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "action_type", value)

    @property
    @pulumi.getter
    def order(self) -> pulumi.Input[int]:
        """
        The order of execution of the automation rule action
        """
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: pulumi.Input[int]):
        pulumi.set(self, "order", value)


@pulumi.input_type
class AutomationRulePropertyValuesConditionConditionPropertiesArgs:
    def __init__(__self__, *,
                 operator: Optional[pulumi.Input[Union[str, 'AutomationRulePropertyConditionSupportedOperator']]] = None,
                 property_name: Optional[pulumi.Input[Union[str, 'AutomationRulePropertyConditionSupportedProperty']]] = None,
                 property_values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The configuration of the automation rule condition
        :param pulumi.Input[Union[str, 'AutomationRulePropertyConditionSupportedOperator']] operator: The operator to use for evaluation the condition
        :param pulumi.Input[Union[str, 'AutomationRulePropertyConditionSupportedProperty']] property_name: The property to evaluate
        :param pulumi.Input[Sequence[pulumi.Input[str]]] property_values: The values to use for evaluating the condition
        """
        if operator is not None:
            pulumi.set(__self__, "operator", operator)
        if property_name is not None:
            pulumi.set(__self__, "property_name", property_name)
        if property_values is not None:
            pulumi.set(__self__, "property_values", property_values)

    @property
    @pulumi.getter
    def operator(self) -> Optional[pulumi.Input[Union[str, 'AutomationRulePropertyConditionSupportedOperator']]]:
        """
        The operator to use for evaluation the condition
        """
        return pulumi.get(self, "operator")

    @operator.setter
    def operator(self, value: Optional[pulumi.Input[Union[str, 'AutomationRulePropertyConditionSupportedOperator']]]):
        pulumi.set(self, "operator", value)

    @property
    @pulumi.getter(name="propertyName")
    def property_name(self) -> Optional[pulumi.Input[Union[str, 'AutomationRulePropertyConditionSupportedProperty']]]:
        """
        The property to evaluate
        """
        return pulumi.get(self, "property_name")

    @property_name.setter
    def property_name(self, value: Optional[pulumi.Input[Union[str, 'AutomationRulePropertyConditionSupportedProperty']]]):
        pulumi.set(self, "property_name", value)

    @property
    @pulumi.getter(name="propertyValues")
    def property_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The values to use for evaluating the condition
        """
        return pulumi.get(self, "property_values")

    @property_values.setter
    def property_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "property_values", value)


@pulumi.input_type
class AutomationRulePropertyValuesConditionArgs:
    def __init__(__self__, *,
                 condition_properties: pulumi.Input['AutomationRulePropertyValuesConditionConditionPropertiesArgs'],
                 condition_type: pulumi.Input[str]):
        """
        Describes an automation rule condition that evaluates a property's value
        :param pulumi.Input['AutomationRulePropertyValuesConditionConditionPropertiesArgs'] condition_properties: The configuration of the automation rule condition
        :param pulumi.Input[str] condition_type: The type of the automation rule condition
               Expected value is 'Property'.
        """
        pulumi.set(__self__, "condition_properties", condition_properties)
        pulumi.set(__self__, "condition_type", 'Property')

    @property
    @pulumi.getter(name="conditionProperties")
    def condition_properties(self) -> pulumi.Input['AutomationRulePropertyValuesConditionConditionPropertiesArgs']:
        """
        The configuration of the automation rule condition
        """
        return pulumi.get(self, "condition_properties")

    @condition_properties.setter
    def condition_properties(self, value: pulumi.Input['AutomationRulePropertyValuesConditionConditionPropertiesArgs']):
        pulumi.set(self, "condition_properties", value)

    @property
    @pulumi.getter(name="conditionType")
    def condition_type(self) -> pulumi.Input[str]:
        """
        The type of the automation rule condition
        Expected value is 'Property'.
        """
        return pulumi.get(self, "condition_type")

    @condition_type.setter
    def condition_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "condition_type", value)


@pulumi.input_type
class AutomationRuleRunPlaybookActionActionConfigurationArgs:
    def __init__(__self__, *,
                 logic_app_resource_id: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        The configuration of the run playbook automation rule action
        :param pulumi.Input[str] logic_app_resource_id: The resource id of the playbook resource
        :param pulumi.Input[str] tenant_id: The tenant id of the playbook resource
        """
        if logic_app_resource_id is not None:
            pulumi.set(__self__, "logic_app_resource_id", logic_app_resource_id)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter(name="logicAppResourceId")
    def logic_app_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource id of the playbook resource
        """
        return pulumi.get(self, "logic_app_resource_id")

    @logic_app_resource_id.setter
    def logic_app_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "logic_app_resource_id", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The tenant id of the playbook resource
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


@pulumi.input_type
class AutomationRuleRunPlaybookActionArgs:
    def __init__(__self__, *,
                 action_configuration: pulumi.Input['AutomationRuleRunPlaybookActionActionConfigurationArgs'],
                 action_type: pulumi.Input[str],
                 order: pulumi.Input[int]):
        """
        Describes an automation rule action to run a playbook
        :param pulumi.Input['AutomationRuleRunPlaybookActionActionConfigurationArgs'] action_configuration: The configuration of the run playbook automation rule action
        :param pulumi.Input[str] action_type: The type of the automation rule action
               Expected value is 'RunPlaybook'.
        :param pulumi.Input[int] order: The order of execution of the automation rule action
        """
        pulumi.set(__self__, "action_configuration", action_configuration)
        pulumi.set(__self__, "action_type", 'RunPlaybook')
        pulumi.set(__self__, "order", order)

    @property
    @pulumi.getter(name="actionConfiguration")
    def action_configuration(self) -> pulumi.Input['AutomationRuleRunPlaybookActionActionConfigurationArgs']:
        """
        The configuration of the run playbook automation rule action
        """
        return pulumi.get(self, "action_configuration")

    @action_configuration.setter
    def action_configuration(self, value: pulumi.Input['AutomationRuleRunPlaybookActionActionConfigurationArgs']):
        pulumi.set(self, "action_configuration", value)

    @property
    @pulumi.getter(name="actionType")
    def action_type(self) -> pulumi.Input[str]:
        """
        The type of the automation rule action
        Expected value is 'RunPlaybook'.
        """
        return pulumi.get(self, "action_type")

    @action_type.setter
    def action_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "action_type", value)

    @property
    @pulumi.getter
    def order(self) -> pulumi.Input[int]:
        """
        The order of execution of the automation rule action
        """
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: pulumi.Input[int]):
        pulumi.set(self, "order", value)


@pulumi.input_type
class AutomationRuleTriggeringLogicArgs:
    def __init__(__self__, *,
                 is_enabled: pulumi.Input[bool],
                 triggers_on: pulumi.Input[Union[str, 'TriggersOn']],
                 triggers_when: pulumi.Input[Union[str, 'TriggersWhen']],
                 conditions: Optional[pulumi.Input[Sequence[pulumi.Input['AutomationRulePropertyValuesConditionArgs']]]] = None,
                 expiration_time_utc: Optional[pulumi.Input[str]] = None):
        """
        Describes automation rule triggering logic
        :param pulumi.Input[bool] is_enabled: Determines whether the automation rule is enabled or disabled.
        :param pulumi.Input[Union[str, 'TriggersOn']] triggers_on: The type of object the automation rule triggers on
        :param pulumi.Input[Union[str, 'TriggersWhen']] triggers_when: The type of event the automation rule triggers on
        :param pulumi.Input[Sequence[pulumi.Input['AutomationRulePropertyValuesConditionArgs']]] conditions: The conditions to evaluate to determine if the automation rule should be triggered on a given object
        :param pulumi.Input[str] expiration_time_utc: Determines when the automation rule should automatically expire and be disabled.
        """
        pulumi.set(__self__, "is_enabled", is_enabled)
        pulumi.set(__self__, "triggers_on", triggers_on)
        pulumi.set(__self__, "triggers_when", triggers_when)
        if conditions is not None:
            pulumi.set(__self__, "conditions", conditions)
        if expiration_time_utc is not None:
            pulumi.set(__self__, "expiration_time_utc", expiration_time_utc)

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Input[bool]:
        """
        Determines whether the automation rule is enabled or disabled.
        """
        return pulumi.get(self, "is_enabled")

    @is_enabled.setter
    def is_enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "is_enabled", value)

    @property
    @pulumi.getter(name="triggersOn")
    def triggers_on(self) -> pulumi.Input[Union[str, 'TriggersOn']]:
        """
        The type of object the automation rule triggers on
        """
        return pulumi.get(self, "triggers_on")

    @triggers_on.setter
    def triggers_on(self, value: pulumi.Input[Union[str, 'TriggersOn']]):
        pulumi.set(self, "triggers_on", value)

    @property
    @pulumi.getter(name="triggersWhen")
    def triggers_when(self) -> pulumi.Input[Union[str, 'TriggersWhen']]:
        """
        The type of event the automation rule triggers on
        """
        return pulumi.get(self, "triggers_when")

    @triggers_when.setter
    def triggers_when(self, value: pulumi.Input[Union[str, 'TriggersWhen']]):
        pulumi.set(self, "triggers_when", value)

    @property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AutomationRulePropertyValuesConditionArgs']]]]:
        """
        The conditions to evaluate to determine if the automation rule should be triggered on a given object
        """
        return pulumi.get(self, "conditions")

    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AutomationRulePropertyValuesConditionArgs']]]]):
        pulumi.set(self, "conditions", value)

    @property
    @pulumi.getter(name="expirationTimeUtc")
    def expiration_time_utc(self) -> Optional[pulumi.Input[str]]:
        """
        Determines when the automation rule should automatically expire and be disabled.
        """
        return pulumi.get(self, "expiration_time_utc")

    @expiration_time_utc.setter
    def expiration_time_utc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiration_time_utc", value)


@pulumi.input_type
class IncidentInfoArgs:
    def __init__(__self__, *,
                 incident_id: Optional[pulumi.Input[str]] = None,
                 relation_name: Optional[pulumi.Input[str]] = None,
                 severity: Optional[pulumi.Input[Union[str, 'IncidentSeverity']]] = None,
                 title: Optional[pulumi.Input[str]] = None):
        """
        Describes related incident information for the bookmark
        :param pulumi.Input[str] incident_id: Incident Id
        :param pulumi.Input[str] relation_name: Relation Name
        :param pulumi.Input[Union[str, 'IncidentSeverity']] severity: The severity of the incident
        :param pulumi.Input[str] title: The title of the incident
        """
        if incident_id is not None:
            pulumi.set(__self__, "incident_id", incident_id)
        if relation_name is not None:
            pulumi.set(__self__, "relation_name", relation_name)
        if severity is not None:
            pulumi.set(__self__, "severity", severity)
        if title is not None:
            pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter(name="incidentId")
    def incident_id(self) -> Optional[pulumi.Input[str]]:
        """
        Incident Id
        """
        return pulumi.get(self, "incident_id")

    @incident_id.setter
    def incident_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "incident_id", value)

    @property
    @pulumi.getter(name="relationName")
    def relation_name(self) -> Optional[pulumi.Input[str]]:
        """
        Relation Name
        """
        return pulumi.get(self, "relation_name")

    @relation_name.setter
    def relation_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "relation_name", value)

    @property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[Union[str, 'IncidentSeverity']]]:
        """
        The severity of the incident
        """
        return pulumi.get(self, "severity")

    @severity.setter
    def severity(self, value: Optional[pulumi.Input[Union[str, 'IncidentSeverity']]]):
        pulumi.set(self, "severity", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        The title of the incident
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)


@pulumi.input_type
class IncidentLabelArgs:
    def __init__(__self__, *,
                 label_name: pulumi.Input[str]):
        """
        Represents an incident label
        :param pulumi.Input[str] label_name: The name of the label
        """
        pulumi.set(__self__, "label_name", label_name)

    @property
    @pulumi.getter(name="labelName")
    def label_name(self) -> pulumi.Input[str]:
        """
        The name of the label
        """
        return pulumi.get(self, "label_name")

    @label_name.setter
    def label_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "label_name", value)


@pulumi.input_type
class IncidentOwnerInfoArgs:
    def __init__(__self__, *,
                 assigned_to: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 object_id: Optional[pulumi.Input[str]] = None,
                 user_principal_name: Optional[pulumi.Input[str]] = None):
        """
        Information on the user an incident is assigned to
        :param pulumi.Input[str] assigned_to: The name of the user the incident is assigned to.
        :param pulumi.Input[str] email: The email of the user the incident is assigned to.
        :param pulumi.Input[str] object_id: The object id of the user the incident is assigned to.
        :param pulumi.Input[str] user_principal_name: The user principal name of the user the incident is assigned to.
        """
        if assigned_to is not None:
            pulumi.set(__self__, "assigned_to", assigned_to)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if object_id is not None:
            pulumi.set(__self__, "object_id", object_id)
        if user_principal_name is not None:
            pulumi.set(__self__, "user_principal_name", user_principal_name)

    @property
    @pulumi.getter(name="assignedTo")
    def assigned_to(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the user the incident is assigned to.
        """
        return pulumi.get(self, "assigned_to")

    @assigned_to.setter
    def assigned_to(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "assigned_to", value)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        The email of the user the incident is assigned to.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[str]]:
        """
        The object id of the user the incident is assigned to.
        """
        return pulumi.get(self, "object_id")

    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "object_id", value)

    @property
    @pulumi.getter(name="userPrincipalName")
    def user_principal_name(self) -> Optional[pulumi.Input[str]]:
        """
        The user principal name of the user the incident is assigned to.
        """
        return pulumi.get(self, "user_principal_name")

    @user_principal_name.setter
    def user_principal_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_principal_name", value)


@pulumi.input_type
class UserInfoArgs:
    def __init__(__self__, *,
                 object_id: Optional[pulumi.Input[str]] = None):
        """
        User information that made some action
        :param pulumi.Input[str] object_id: The object id of the user.
        """
        if object_id is not None:
            pulumi.set(__self__, "object_id", object_id)

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[str]]:
        """
        The object id of the user.
        """
        return pulumi.get(self, "object_id")

    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "object_id", value)


@pulumi.input_type
class WatchlistUserInfoArgs:
    def __init__(__self__, *,
                 object_id: Optional[pulumi.Input[str]] = None):
        """
        User information that made some action
        :param pulumi.Input[str] object_id: The object id of the user.
        """
        if object_id is not None:
            pulumi.set(__self__, "object_id", object_id)

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[str]]:
        """
        The object id of the user.
        """
        return pulumi.get(self, "object_id")

    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "object_id", value)


