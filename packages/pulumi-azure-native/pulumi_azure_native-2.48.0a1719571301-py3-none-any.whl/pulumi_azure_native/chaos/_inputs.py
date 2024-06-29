# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'BranchArgs',
    'ContinuousActionArgs',
    'DelayActionArgs',
    'DiscreteActionArgs',
    'ExperimentPropertiesArgs',
    'KeyValuePairArgs',
    'ListSelectorArgs',
    'QuerySelectorArgs',
    'ResourceIdentityArgs',
    'SimpleFilterParametersArgs',
    'SimpleFilterArgs',
    'StepArgs',
    'TargetReferenceArgs',
]

@pulumi.input_type
class BranchArgs:
    def __init__(__self__, *,
                 actions: pulumi.Input[Sequence[pulumi.Input[Union['ContinuousActionArgs', 'DelayActionArgs', 'DiscreteActionArgs']]]],
                 name: pulumi.Input[str]):
        """
        Model that represents a branch in the step.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ContinuousActionArgs', 'DelayActionArgs', 'DiscreteActionArgs']]]] actions: List of actions.
        :param pulumi.Input[str] name: String of the branch name.
        """
        pulumi.set(__self__, "actions", actions)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[Union['ContinuousActionArgs', 'DelayActionArgs', 'DiscreteActionArgs']]]]:
        """
        List of actions.
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[Union['ContinuousActionArgs', 'DelayActionArgs', 'DiscreteActionArgs']]]]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        String of the branch name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class ContinuousActionArgs:
    def __init__(__self__, *,
                 duration: pulumi.Input[str],
                 name: pulumi.Input[str],
                 parameters: pulumi.Input[Sequence[pulumi.Input['KeyValuePairArgs']]],
                 selector_id: pulumi.Input[str],
                 type: pulumi.Input[str]):
        """
        Model that represents a continuous action.
        :param pulumi.Input[str] duration: ISO8601 formatted string that represents a duration.
        :param pulumi.Input[str] name: String that represents a Capability URN.
        :param pulumi.Input[Sequence[pulumi.Input['KeyValuePairArgs']]] parameters: List of key value pairs.
        :param pulumi.Input[str] selector_id: String that represents a selector.
        :param pulumi.Input[str] type: Enum that discriminates between action models.
               Expected value is 'continuous'.
        """
        pulumi.set(__self__, "duration", duration)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "parameters", parameters)
        pulumi.set(__self__, "selector_id", selector_id)
        pulumi.set(__self__, "type", 'continuous')

    @property
    @pulumi.getter
    def duration(self) -> pulumi.Input[str]:
        """
        ISO8601 formatted string that represents a duration.
        """
        return pulumi.get(self, "duration")

    @duration.setter
    def duration(self, value: pulumi.Input[str]):
        pulumi.set(self, "duration", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        String that represents a Capability URN.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[Sequence[pulumi.Input['KeyValuePairArgs']]]:
        """
        List of key value pairs.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: pulumi.Input[Sequence[pulumi.Input['KeyValuePairArgs']]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="selectorId")
    def selector_id(self) -> pulumi.Input[str]:
        """
        String that represents a selector.
        """
        return pulumi.get(self, "selector_id")

    @selector_id.setter
    def selector_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "selector_id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Enum that discriminates between action models.
        Expected value is 'continuous'.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class DelayActionArgs:
    def __init__(__self__, *,
                 duration: pulumi.Input[str],
                 name: pulumi.Input[str],
                 type: pulumi.Input[str]):
        """
        Model that represents a delay action.
        :param pulumi.Input[str] duration: ISO8601 formatted string that represents a duration.
        :param pulumi.Input[str] name: String that represents a Capability URN.
        :param pulumi.Input[str] type: Enum that discriminates between action models.
               Expected value is 'delay'.
        """
        pulumi.set(__self__, "duration", duration)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", 'delay')

    @property
    @pulumi.getter
    def duration(self) -> pulumi.Input[str]:
        """
        ISO8601 formatted string that represents a duration.
        """
        return pulumi.get(self, "duration")

    @duration.setter
    def duration(self, value: pulumi.Input[str]):
        pulumi.set(self, "duration", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        String that represents a Capability URN.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Enum that discriminates between action models.
        Expected value is 'delay'.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class DiscreteActionArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 parameters: pulumi.Input[Sequence[pulumi.Input['KeyValuePairArgs']]],
                 selector_id: pulumi.Input[str],
                 type: pulumi.Input[str]):
        """
        Model that represents a discrete action.
        :param pulumi.Input[str] name: String that represents a Capability URN.
        :param pulumi.Input[Sequence[pulumi.Input['KeyValuePairArgs']]] parameters: List of key value pairs.
        :param pulumi.Input[str] selector_id: String that represents a selector.
        :param pulumi.Input[str] type: Enum that discriminates between action models.
               Expected value is 'discrete'.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "parameters", parameters)
        pulumi.set(__self__, "selector_id", selector_id)
        pulumi.set(__self__, "type", 'discrete')

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        String that represents a Capability URN.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[Sequence[pulumi.Input['KeyValuePairArgs']]]:
        """
        List of key value pairs.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: pulumi.Input[Sequence[pulumi.Input['KeyValuePairArgs']]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="selectorId")
    def selector_id(self) -> pulumi.Input[str]:
        """
        String that represents a selector.
        """
        return pulumi.get(self, "selector_id")

    @selector_id.setter
    def selector_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "selector_id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Enum that discriminates between action models.
        Expected value is 'discrete'.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class ExperimentPropertiesArgs:
    def __init__(__self__, *,
                 selectors: pulumi.Input[Sequence[pulumi.Input[Union['ListSelectorArgs', 'QuerySelectorArgs']]]],
                 steps: pulumi.Input[Sequence[pulumi.Input['StepArgs']]],
                 start_on_creation: Optional[pulumi.Input[bool]] = None):
        """
        Model that represents the Experiment properties model.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ListSelectorArgs', 'QuerySelectorArgs']]]] selectors: List of selectors.
        :param pulumi.Input[Sequence[pulumi.Input['StepArgs']]] steps: List of steps.
        :param pulumi.Input[bool] start_on_creation: A boolean value that indicates if experiment should be started on creation or not.
        """
        pulumi.set(__self__, "selectors", selectors)
        pulumi.set(__self__, "steps", steps)
        if start_on_creation is not None:
            pulumi.set(__self__, "start_on_creation", start_on_creation)

    @property
    @pulumi.getter
    def selectors(self) -> pulumi.Input[Sequence[pulumi.Input[Union['ListSelectorArgs', 'QuerySelectorArgs']]]]:
        """
        List of selectors.
        """
        return pulumi.get(self, "selectors")

    @selectors.setter
    def selectors(self, value: pulumi.Input[Sequence[pulumi.Input[Union['ListSelectorArgs', 'QuerySelectorArgs']]]]):
        pulumi.set(self, "selectors", value)

    @property
    @pulumi.getter
    def steps(self) -> pulumi.Input[Sequence[pulumi.Input['StepArgs']]]:
        """
        List of steps.
        """
        return pulumi.get(self, "steps")

    @steps.setter
    def steps(self, value: pulumi.Input[Sequence[pulumi.Input['StepArgs']]]):
        pulumi.set(self, "steps", value)

    @property
    @pulumi.getter(name="startOnCreation")
    def start_on_creation(self) -> Optional[pulumi.Input[bool]]:
        """
        A boolean value that indicates if experiment should be started on creation or not.
        """
        return pulumi.get(self, "start_on_creation")

    @start_on_creation.setter
    def start_on_creation(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "start_on_creation", value)


@pulumi.input_type
class KeyValuePairArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A map to describe the settings of an action.
        :param pulumi.Input[str] key: The name of the setting for the action.
        :param pulumi.Input[str] value: The value of the setting for the action.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The name of the setting for the action.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value of the setting for the action.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ListSelectorArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 targets: pulumi.Input[Sequence[pulumi.Input['TargetReferenceArgs']]],
                 type: pulumi.Input[str],
                 filter: Optional[pulumi.Input['SimpleFilterArgs']] = None):
        """
        Model that represents a list selector.
        :param pulumi.Input[str] id: String of the selector ID.
        :param pulumi.Input[Sequence[pulumi.Input['TargetReferenceArgs']]] targets: List of Target references.
        :param pulumi.Input[str] type: Enum of the selector type.
               Expected value is 'List'.
        :param pulumi.Input['SimpleFilterArgs'] filter: Model that represents available filter types that can be applied to a targets list.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "targets", targets)
        pulumi.set(__self__, "type", 'List')
        if filter is not None:
            pulumi.set(__self__, "filter", filter)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        String of the selector ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def targets(self) -> pulumi.Input[Sequence[pulumi.Input['TargetReferenceArgs']]]:
        """
        List of Target references.
        """
        return pulumi.get(self, "targets")

    @targets.setter
    def targets(self, value: pulumi.Input[Sequence[pulumi.Input['TargetReferenceArgs']]]):
        pulumi.set(self, "targets", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Enum of the selector type.
        Expected value is 'List'.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input['SimpleFilterArgs']]:
        """
        Model that represents available filter types that can be applied to a targets list.
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input['SimpleFilterArgs']]):
        pulumi.set(self, "filter", value)


@pulumi.input_type
class QuerySelectorArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 query_string: pulumi.Input[str],
                 subscription_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 type: pulumi.Input[str],
                 filter: Optional[pulumi.Input['SimpleFilterArgs']] = None):
        """
        Model that represents a query selector.
        :param pulumi.Input[str] id: String of the selector ID.
        :param pulumi.Input[str] query_string: Azure Resource Graph (ARG) Query Language query for target resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subscription_ids: Subscription id list to scope resource query.
        :param pulumi.Input[str] type: Enum of the selector type.
               Expected value is 'Query'.
        :param pulumi.Input['SimpleFilterArgs'] filter: Model that represents available filter types that can be applied to a targets list.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "query_string", query_string)
        pulumi.set(__self__, "subscription_ids", subscription_ids)
        pulumi.set(__self__, "type", 'Query')
        if filter is not None:
            pulumi.set(__self__, "filter", filter)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        String of the selector ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="queryString")
    def query_string(self) -> pulumi.Input[str]:
        """
        Azure Resource Graph (ARG) Query Language query for target resources.
        """
        return pulumi.get(self, "query_string")

    @query_string.setter
    def query_string(self, value: pulumi.Input[str]):
        pulumi.set(self, "query_string", value)

    @property
    @pulumi.getter(name="subscriptionIds")
    def subscription_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Subscription id list to scope resource query.
        """
        return pulumi.get(self, "subscription_ids")

    @subscription_ids.setter
    def subscription_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "subscription_ids", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Enum of the selector type.
        Expected value is 'Query'.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input['SimpleFilterArgs']]:
        """
        Model that represents available filter types that can be applied to a targets list.
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input['SimpleFilterArgs']]):
        pulumi.set(self, "filter", value)


@pulumi.input_type
class ResourceIdentityArgs:
    def __init__(__self__, *,
                 type: pulumi.Input['ResourceIdentityType'],
                 user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The identity of a resource.
        :param pulumi.Input['ResourceIdentityType'] type: String of the resource identity type.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_assigned_identities: The list of user identities associated with the Experiment. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        """
        pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input['ResourceIdentityType']:
        """
        String of the resource identity type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input['ResourceIdentityType']):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of user identities associated with the Experiment. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        """
        return pulumi.get(self, "user_assigned_identities")

    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "user_assigned_identities", value)


@pulumi.input_type
class SimpleFilterParametersArgs:
    def __init__(__self__, *,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Model that represents the Simple filter parameters.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: List of Azure availability zones to filter targets by.
        """
        if zones is not None:
            pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter
    def zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of Azure availability zones to filter targets by.
        """
        return pulumi.get(self, "zones")

    @zones.setter
    def zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "zones", value)


@pulumi.input_type
class SimpleFilterArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 parameters: Optional[pulumi.Input['SimpleFilterParametersArgs']] = None):
        """
        Model that represents a simple target filter.
        :param pulumi.Input[str] type: Enum that discriminates between filter types. Currently only `Simple` type is supported.
               Expected value is 'Simple'.
        :param pulumi.Input['SimpleFilterParametersArgs'] parameters: Model that represents the Simple filter parameters.
        """
        pulumi.set(__self__, "type", 'Simple')
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Enum that discriminates between filter types. Currently only `Simple` type is supported.
        Expected value is 'Simple'.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input['SimpleFilterParametersArgs']]:
        """
        Model that represents the Simple filter parameters.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input['SimpleFilterParametersArgs']]):
        pulumi.set(self, "parameters", value)


@pulumi.input_type
class StepArgs:
    def __init__(__self__, *,
                 branches: pulumi.Input[Sequence[pulumi.Input['BranchArgs']]],
                 name: pulumi.Input[str]):
        """
        Model that represents a step in the Experiment resource.
        :param pulumi.Input[Sequence[pulumi.Input['BranchArgs']]] branches: List of branches.
        :param pulumi.Input[str] name: String of the step name.
        """
        pulumi.set(__self__, "branches", branches)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def branches(self) -> pulumi.Input[Sequence[pulumi.Input['BranchArgs']]]:
        """
        List of branches.
        """
        return pulumi.get(self, "branches")

    @branches.setter
    def branches(self, value: pulumi.Input[Sequence[pulumi.Input['BranchArgs']]]):
        pulumi.set(self, "branches", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        String of the step name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class TargetReferenceArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 type: pulumi.Input[Union[str, 'TargetReferenceType']]):
        """
        Model that represents a reference to a Target in the selector.
        :param pulumi.Input[str] id: String of the resource ID of a Target resource.
        :param pulumi.Input[Union[str, 'TargetReferenceType']] type: Enum of the Target reference type.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        String of the resource ID of a Target resource.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[str, 'TargetReferenceType']]:
        """
        Enum of the Target reference type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[Union[str, 'TargetReferenceType']]):
        pulumi.set(self, "type", value)


