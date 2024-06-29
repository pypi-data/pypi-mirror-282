# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['PolicyAssignmentArgs', 'PolicyAssignment']

@pulumi.input_type
class PolicyAssignmentArgs:
    def __init__(__self__, *,
                 scope: pulumi.Input[str],
                 assignment_type: Optional[pulumi.Input[Union[str, 'AssignmentType']]] = None,
                 definition_version: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enforcement_mode: Optional[pulumi.Input[Union[str, 'EnforcementMode']]] = None,
                 identity: Optional[pulumi.Input['IdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 non_compliance_messages: Optional[pulumi.Input[Sequence[pulumi.Input['NonComplianceMessageArgs']]]] = None,
                 not_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 overrides: Optional[pulumi.Input[Sequence[pulumi.Input['OverrideArgs']]]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input['ParameterValuesValueArgs']]]] = None,
                 policy_assignment_name: Optional[pulumi.Input[str]] = None,
                 policy_definition_id: Optional[pulumi.Input[str]] = None,
                 resource_selectors: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceSelectorArgs']]]] = None):
        """
        The set of arguments for constructing a PolicyAssignment resource.
        :param pulumi.Input[str] scope: The scope of the policy assignment. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'), resource group (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}', or resource (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'
        :param pulumi.Input[Union[str, 'AssignmentType']] assignment_type: The type of policy assignment. Possible values are NotSpecified, System, SystemHidden, and Custom. Immutable.
        :param pulumi.Input[str] definition_version: The version of the policy definition to use.
        :param pulumi.Input[str] description: This message will be part of response in case of policy violation.
        :param pulumi.Input[str] display_name: The display name of the policy assignment.
        :param pulumi.Input[Union[str, 'EnforcementMode']] enforcement_mode: The policy assignment enforcement mode. Possible values are Default and DoNotEnforce.
        :param pulumi.Input['IdentityArgs'] identity: The managed identity associated with the policy assignment.
        :param pulumi.Input[str] location: The location of the policy assignment. Only required when utilizing managed identity.
        :param Any metadata: The policy assignment metadata. Metadata is an open ended object and is typically a collection of key value pairs.
        :param pulumi.Input[Sequence[pulumi.Input['NonComplianceMessageArgs']]] non_compliance_messages: The messages that describe why a resource is non-compliant with the policy.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] not_scopes: The policy's excluded scopes.
        :param pulumi.Input[Sequence[pulumi.Input['OverrideArgs']]] overrides: The policy property value override.
        :param pulumi.Input[Mapping[str, pulumi.Input['ParameterValuesValueArgs']]] parameters: The parameter values for the assigned policy rule. The keys are the parameter names.
        :param pulumi.Input[str] policy_assignment_name: The name of the policy assignment.
        :param pulumi.Input[str] policy_definition_id: The ID of the policy definition or policy set definition being assigned.
        :param pulumi.Input[Sequence[pulumi.Input['ResourceSelectorArgs']]] resource_selectors: The resource selector list to filter policies by resource properties.
        """
        pulumi.set(__self__, "scope", scope)
        if assignment_type is not None:
            pulumi.set(__self__, "assignment_type", assignment_type)
        if definition_version is not None:
            pulumi.set(__self__, "definition_version", definition_version)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if enforcement_mode is None:
            enforcement_mode = 'Default'
        if enforcement_mode is not None:
            pulumi.set(__self__, "enforcement_mode", enforcement_mode)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if non_compliance_messages is not None:
            pulumi.set(__self__, "non_compliance_messages", non_compliance_messages)
        if not_scopes is not None:
            pulumi.set(__self__, "not_scopes", not_scopes)
        if overrides is not None:
            pulumi.set(__self__, "overrides", overrides)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if policy_assignment_name is not None:
            pulumi.set(__self__, "policy_assignment_name", policy_assignment_name)
        if policy_definition_id is not None:
            pulumi.set(__self__, "policy_definition_id", policy_definition_id)
        if resource_selectors is not None:
            pulumi.set(__self__, "resource_selectors", resource_selectors)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input[str]:
        """
        The scope of the policy assignment. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'), resource group (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}', or resource (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="assignmentType")
    def assignment_type(self) -> Optional[pulumi.Input[Union[str, 'AssignmentType']]]:
        """
        The type of policy assignment. Possible values are NotSpecified, System, SystemHidden, and Custom. Immutable.
        """
        return pulumi.get(self, "assignment_type")

    @assignment_type.setter
    def assignment_type(self, value: Optional[pulumi.Input[Union[str, 'AssignmentType']]]):
        pulumi.set(self, "assignment_type", value)

    @property
    @pulumi.getter(name="definitionVersion")
    def definition_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the policy definition to use.
        """
        return pulumi.get(self, "definition_version")

    @definition_version.setter
    def definition_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "definition_version", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        This message will be part of response in case of policy violation.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the policy assignment.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="enforcementMode")
    def enforcement_mode(self) -> Optional[pulumi.Input[Union[str, 'EnforcementMode']]]:
        """
        The policy assignment enforcement mode. Possible values are Default and DoNotEnforce.
        """
        return pulumi.get(self, "enforcement_mode")

    @enforcement_mode.setter
    def enforcement_mode(self, value: Optional[pulumi.Input[Union[str, 'EnforcementMode']]]):
        pulumi.set(self, "enforcement_mode", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['IdentityArgs']]:
        """
        The managed identity associated with the policy assignment.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['IdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the policy assignment. Only required when utilizing managed identity.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        """
        The policy assignment metadata. Metadata is an open ended object and is typically a collection of key value pairs.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[Any]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter(name="nonComplianceMessages")
    def non_compliance_messages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NonComplianceMessageArgs']]]]:
        """
        The messages that describe why a resource is non-compliant with the policy.
        """
        return pulumi.get(self, "non_compliance_messages")

    @non_compliance_messages.setter
    def non_compliance_messages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NonComplianceMessageArgs']]]]):
        pulumi.set(self, "non_compliance_messages", value)

    @property
    @pulumi.getter(name="notScopes")
    def not_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The policy's excluded scopes.
        """
        return pulumi.get(self, "not_scopes")

    @not_scopes.setter
    def not_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "not_scopes", value)

    @property
    @pulumi.getter
    def overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OverrideArgs']]]]:
        """
        The policy property value override.
        """
        return pulumi.get(self, "overrides")

    @overrides.setter
    def overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OverrideArgs']]]]):
        pulumi.set(self, "overrides", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['ParameterValuesValueArgs']]]]:
        """
        The parameter values for the assigned policy rule. The keys are the parameter names.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['ParameterValuesValueArgs']]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="policyAssignmentName")
    def policy_assignment_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the policy assignment.
        """
        return pulumi.get(self, "policy_assignment_name")

    @policy_assignment_name.setter
    def policy_assignment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_assignment_name", value)

    @property
    @pulumi.getter(name="policyDefinitionId")
    def policy_definition_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the policy definition or policy set definition being assigned.
        """
        return pulumi.get(self, "policy_definition_id")

    @policy_definition_id.setter
    def policy_definition_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_definition_id", value)

    @property
    @pulumi.getter(name="resourceSelectors")
    def resource_selectors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ResourceSelectorArgs']]]]:
        """
        The resource selector list to filter policies by resource properties.
        """
        return pulumi.get(self, "resource_selectors")

    @resource_selectors.setter
    def resource_selectors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceSelectorArgs']]]]):
        pulumi.set(self, "resource_selectors", value)


class PolicyAssignment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assignment_type: Optional[pulumi.Input[Union[str, 'AssignmentType']]] = None,
                 definition_version: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enforcement_mode: Optional[pulumi.Input[Union[str, 'EnforcementMode']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 non_compliance_messages: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NonComplianceMessageArgs']]]]] = None,
                 not_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 overrides: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OverrideArgs']]]]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ParameterValuesValueArgs']]]]] = None,
                 policy_assignment_name: Optional[pulumi.Input[str]] = None,
                 policy_definition_id: Optional[pulumi.Input[str]] = None,
                 resource_selectors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceSelectorArgs']]]]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The policy assignment.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'AssignmentType']] assignment_type: The type of policy assignment. Possible values are NotSpecified, System, SystemHidden, and Custom. Immutable.
        :param pulumi.Input[str] definition_version: The version of the policy definition to use.
        :param pulumi.Input[str] description: This message will be part of response in case of policy violation.
        :param pulumi.Input[str] display_name: The display name of the policy assignment.
        :param pulumi.Input[Union[str, 'EnforcementMode']] enforcement_mode: The policy assignment enforcement mode. Possible values are Default and DoNotEnforce.
        :param pulumi.Input[pulumi.InputType['IdentityArgs']] identity: The managed identity associated with the policy assignment.
        :param pulumi.Input[str] location: The location of the policy assignment. Only required when utilizing managed identity.
        :param Any metadata: The policy assignment metadata. Metadata is an open ended object and is typically a collection of key value pairs.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NonComplianceMessageArgs']]]] non_compliance_messages: The messages that describe why a resource is non-compliant with the policy.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] not_scopes: The policy's excluded scopes.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OverrideArgs']]]] overrides: The policy property value override.
        :param pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ParameterValuesValueArgs']]]] parameters: The parameter values for the assigned policy rule. The keys are the parameter names.
        :param pulumi.Input[str] policy_assignment_name: The name of the policy assignment.
        :param pulumi.Input[str] policy_definition_id: The ID of the policy definition or policy set definition being assigned.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceSelectorArgs']]]] resource_selectors: The resource selector list to filter policies by resource properties.
        :param pulumi.Input[str] scope: The scope of the policy assignment. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'), resource group (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}', or resource (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PolicyAssignmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The policy assignment.

        :param str resource_name: The name of the resource.
        :param PolicyAssignmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PolicyAssignmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assignment_type: Optional[pulumi.Input[Union[str, 'AssignmentType']]] = None,
                 definition_version: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enforcement_mode: Optional[pulumi.Input[Union[str, 'EnforcementMode']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 non_compliance_messages: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NonComplianceMessageArgs']]]]] = None,
                 not_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 overrides: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OverrideArgs']]]]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ParameterValuesValueArgs']]]]] = None,
                 policy_assignment_name: Optional[pulumi.Input[str]] = None,
                 policy_definition_id: Optional[pulumi.Input[str]] = None,
                 resource_selectors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceSelectorArgs']]]]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PolicyAssignmentArgs.__new__(PolicyAssignmentArgs)

            __props__.__dict__["assignment_type"] = assignment_type
            __props__.__dict__["definition_version"] = definition_version
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            if enforcement_mode is None:
                enforcement_mode = 'Default'
            __props__.__dict__["enforcement_mode"] = enforcement_mode
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["non_compliance_messages"] = non_compliance_messages
            __props__.__dict__["not_scopes"] = not_scopes
            __props__.__dict__["overrides"] = overrides
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["policy_assignment_name"] = policy_assignment_name
            __props__.__dict__["policy_definition_id"] = policy_definition_id
            __props__.__dict__["resource_selectors"] = resource_selectors
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:authorization:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20151001preview:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20160401:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20161201:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20170601preview:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20180301:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20180501:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20190101:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20190601:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20190901:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20200301:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20200901:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20210601:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20220601:PolicyAssignment"), pulumi.Alias(type_="azure-native:authorization/v20230401:PolicyAssignment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PolicyAssignment, __self__).__init__(
            'azure-native:authorization/v20240401:PolicyAssignment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PolicyAssignment':
        """
        Get an existing PolicyAssignment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PolicyAssignmentArgs.__new__(PolicyAssignmentArgs)

        __props__.__dict__["assignment_type"] = None
        __props__.__dict__["definition_version"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["enforcement_mode"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["non_compliance_messages"] = None
        __props__.__dict__["not_scopes"] = None
        __props__.__dict__["overrides"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["policy_definition_id"] = None
        __props__.__dict__["resource_selectors"] = None
        __props__.__dict__["scope"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return PolicyAssignment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="assignmentType")
    def assignment_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of policy assignment. Possible values are NotSpecified, System, SystemHidden, and Custom. Immutable.
        """
        return pulumi.get(self, "assignment_type")

    @property
    @pulumi.getter(name="definitionVersion")
    def definition_version(self) -> pulumi.Output[Optional[str]]:
        """
        The version of the policy definition to use.
        """
        return pulumi.get(self, "definition_version")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        This message will be part of response in case of policy violation.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The display name of the policy assignment.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="enforcementMode")
    def enforcement_mode(self) -> pulumi.Output[Optional[str]]:
        """
        The policy assignment enforcement mode. Possible values are Default and DoNotEnforce.
        """
        return pulumi.get(self, "enforcement_mode")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityResponse']]:
        """
        The managed identity associated with the policy assignment.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The location of the policy assignment. Only required when utilizing managed identity.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Any]]:
        """
        The policy assignment metadata. Metadata is an open ended object and is typically a collection of key value pairs.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the policy assignment.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nonComplianceMessages")
    def non_compliance_messages(self) -> pulumi.Output[Optional[Sequence['outputs.NonComplianceMessageResponse']]]:
        """
        The messages that describe why a resource is non-compliant with the policy.
        """
        return pulumi.get(self, "non_compliance_messages")

    @property
    @pulumi.getter(name="notScopes")
    def not_scopes(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The policy's excluded scopes.
        """
        return pulumi.get(self, "not_scopes")

    @property
    @pulumi.getter
    def overrides(self) -> pulumi.Output[Optional[Sequence['outputs.OverrideResponse']]]:
        """
        The policy property value override.
        """
        return pulumi.get(self, "overrides")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.ParameterValuesValueResponse']]]:
        """
        The parameter values for the assigned policy rule. The keys are the parameter names.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="policyDefinitionId")
    def policy_definition_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the policy definition or policy set definition being assigned.
        """
        return pulumi.get(self, "policy_definition_id")

    @property
    @pulumi.getter(name="resourceSelectors")
    def resource_selectors(self) -> pulumi.Output[Optional[Sequence['outputs.ResourceSelectorResponse']]]:
        """
        The resource selector list to filter policies by resource properties.
        """
        return pulumi.get(self, "resource_selectors")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[str]:
        """
        The scope for the policy assignment.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the policy assignment.
        """
        return pulumi.get(self, "type")

