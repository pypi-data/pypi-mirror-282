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

__all__ = ['PolicyExemptionArgs', 'PolicyExemption']

@pulumi.input_type
class PolicyExemptionArgs:
    def __init__(__self__, *,
                 exemption_category: pulumi.Input[Union[str, 'ExemptionCategory']],
                 policy_assignment_id: pulumi.Input[str],
                 scope: pulumi.Input[str],
                 assignment_scope_validation: Optional[pulumi.Input[Union[str, 'AssignmentScopeValidation']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 expires_on: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 policy_definition_reference_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 policy_exemption_name: Optional[pulumi.Input[str]] = None,
                 resource_selectors: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceSelectorArgs']]]] = None):
        """
        The set of arguments for constructing a PolicyExemption resource.
        :param pulumi.Input[Union[str, 'ExemptionCategory']] exemption_category: The policy exemption category. Possible values are Waiver and Mitigated.
        :param pulumi.Input[str] policy_assignment_id: The ID of the policy assignment that is being exempted.
        :param pulumi.Input[str] scope: The scope of the policy exemption. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'), resource group (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}', or resource (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'
        :param pulumi.Input[Union[str, 'AssignmentScopeValidation']] assignment_scope_validation: The option whether validate the exemption is at or under the assignment scope.
        :param pulumi.Input[str] description: The description of the policy exemption.
        :param pulumi.Input[str] display_name: The display name of the policy exemption.
        :param pulumi.Input[str] expires_on: The expiration date and time (in UTC ISO 8601 format yyyy-MM-ddTHH:mm:ssZ) of the policy exemption.
        :param Any metadata: The policy exemption metadata. Metadata is an open ended object and is typically a collection of key value pairs.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policy_definition_reference_ids: The policy definition reference ID list when the associated policy assignment is an assignment of a policy set definition.
        :param pulumi.Input[str] policy_exemption_name: The name of the policy exemption to delete.
        :param pulumi.Input[Sequence[pulumi.Input['ResourceSelectorArgs']]] resource_selectors: The resource selector list to filter policies by resource properties.
        """
        pulumi.set(__self__, "exemption_category", exemption_category)
        pulumi.set(__self__, "policy_assignment_id", policy_assignment_id)
        pulumi.set(__self__, "scope", scope)
        if assignment_scope_validation is None:
            assignment_scope_validation = 'Default'
        if assignment_scope_validation is not None:
            pulumi.set(__self__, "assignment_scope_validation", assignment_scope_validation)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if expires_on is not None:
            pulumi.set(__self__, "expires_on", expires_on)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if policy_definition_reference_ids is not None:
            pulumi.set(__self__, "policy_definition_reference_ids", policy_definition_reference_ids)
        if policy_exemption_name is not None:
            pulumi.set(__self__, "policy_exemption_name", policy_exemption_name)
        if resource_selectors is not None:
            pulumi.set(__self__, "resource_selectors", resource_selectors)

    @property
    @pulumi.getter(name="exemptionCategory")
    def exemption_category(self) -> pulumi.Input[Union[str, 'ExemptionCategory']]:
        """
        The policy exemption category. Possible values are Waiver and Mitigated.
        """
        return pulumi.get(self, "exemption_category")

    @exemption_category.setter
    def exemption_category(self, value: pulumi.Input[Union[str, 'ExemptionCategory']]):
        pulumi.set(self, "exemption_category", value)

    @property
    @pulumi.getter(name="policyAssignmentId")
    def policy_assignment_id(self) -> pulumi.Input[str]:
        """
        The ID of the policy assignment that is being exempted.
        """
        return pulumi.get(self, "policy_assignment_id")

    @policy_assignment_id.setter
    def policy_assignment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_assignment_id", value)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input[str]:
        """
        The scope of the policy exemption. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'), resource group (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}', or resource (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="assignmentScopeValidation")
    def assignment_scope_validation(self) -> Optional[pulumi.Input[Union[str, 'AssignmentScopeValidation']]]:
        """
        The option whether validate the exemption is at or under the assignment scope.
        """
        return pulumi.get(self, "assignment_scope_validation")

    @assignment_scope_validation.setter
    def assignment_scope_validation(self, value: Optional[pulumi.Input[Union[str, 'AssignmentScopeValidation']]]):
        pulumi.set(self, "assignment_scope_validation", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the policy exemption.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the policy exemption.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="expiresOn")
    def expires_on(self) -> Optional[pulumi.Input[str]]:
        """
        The expiration date and time (in UTC ISO 8601 format yyyy-MM-ddTHH:mm:ssZ) of the policy exemption.
        """
        return pulumi.get(self, "expires_on")

    @expires_on.setter
    def expires_on(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expires_on", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        """
        The policy exemption metadata. Metadata is an open ended object and is typically a collection of key value pairs.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[Any]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter(name="policyDefinitionReferenceIds")
    def policy_definition_reference_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The policy definition reference ID list when the associated policy assignment is an assignment of a policy set definition.
        """
        return pulumi.get(self, "policy_definition_reference_ids")

    @policy_definition_reference_ids.setter
    def policy_definition_reference_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "policy_definition_reference_ids", value)

    @property
    @pulumi.getter(name="policyExemptionName")
    def policy_exemption_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the policy exemption to delete.
        """
        return pulumi.get(self, "policy_exemption_name")

    @policy_exemption_name.setter
    def policy_exemption_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_exemption_name", value)

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


class PolicyExemption(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assignment_scope_validation: Optional[pulumi.Input[Union[str, 'AssignmentScopeValidation']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 exemption_category: Optional[pulumi.Input[Union[str, 'ExemptionCategory']]] = None,
                 expires_on: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 policy_assignment_id: Optional[pulumi.Input[str]] = None,
                 policy_definition_reference_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 policy_exemption_name: Optional[pulumi.Input[str]] = None,
                 resource_selectors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceSelectorArgs']]]]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The policy exemption.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'AssignmentScopeValidation']] assignment_scope_validation: The option whether validate the exemption is at or under the assignment scope.
        :param pulumi.Input[str] description: The description of the policy exemption.
        :param pulumi.Input[str] display_name: The display name of the policy exemption.
        :param pulumi.Input[Union[str, 'ExemptionCategory']] exemption_category: The policy exemption category. Possible values are Waiver and Mitigated.
        :param pulumi.Input[str] expires_on: The expiration date and time (in UTC ISO 8601 format yyyy-MM-ddTHH:mm:ssZ) of the policy exemption.
        :param Any metadata: The policy exemption metadata. Metadata is an open ended object and is typically a collection of key value pairs.
        :param pulumi.Input[str] policy_assignment_id: The ID of the policy assignment that is being exempted.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policy_definition_reference_ids: The policy definition reference ID list when the associated policy assignment is an assignment of a policy set definition.
        :param pulumi.Input[str] policy_exemption_name: The name of the policy exemption to delete.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceSelectorArgs']]]] resource_selectors: The resource selector list to filter policies by resource properties.
        :param pulumi.Input[str] scope: The scope of the policy exemption. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'), resource group (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}', or resource (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PolicyExemptionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The policy exemption.

        :param str resource_name: The name of the resource.
        :param PolicyExemptionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PolicyExemptionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assignment_scope_validation: Optional[pulumi.Input[Union[str, 'AssignmentScopeValidation']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 exemption_category: Optional[pulumi.Input[Union[str, 'ExemptionCategory']]] = None,
                 expires_on: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 policy_assignment_id: Optional[pulumi.Input[str]] = None,
                 policy_definition_reference_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 policy_exemption_name: Optional[pulumi.Input[str]] = None,
                 resource_selectors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceSelectorArgs']]]]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PolicyExemptionArgs.__new__(PolicyExemptionArgs)

            if assignment_scope_validation is None:
                assignment_scope_validation = 'Default'
            __props__.__dict__["assignment_scope_validation"] = assignment_scope_validation
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            if exemption_category is None and not opts.urn:
                raise TypeError("Missing required property 'exemption_category'")
            __props__.__dict__["exemption_category"] = exemption_category
            __props__.__dict__["expires_on"] = expires_on
            __props__.__dict__["metadata"] = metadata
            if policy_assignment_id is None and not opts.urn:
                raise TypeError("Missing required property 'policy_assignment_id'")
            __props__.__dict__["policy_assignment_id"] = policy_assignment_id
            __props__.__dict__["policy_definition_reference_ids"] = policy_definition_reference_ids
            __props__.__dict__["policy_exemption_name"] = policy_exemption_name
            __props__.__dict__["resource_selectors"] = resource_selectors
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:authorization:PolicyExemption"), pulumi.Alias(type_="azure-native:authorization/v20200701preview:PolicyExemption")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PolicyExemption, __self__).__init__(
            'azure-native:authorization/v20220701preview:PolicyExemption',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PolicyExemption':
        """
        Get an existing PolicyExemption resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PolicyExemptionArgs.__new__(PolicyExemptionArgs)

        __props__.__dict__["assignment_scope_validation"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["exemption_category"] = None
        __props__.__dict__["expires_on"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["policy_assignment_id"] = None
        __props__.__dict__["policy_definition_reference_ids"] = None
        __props__.__dict__["resource_selectors"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return PolicyExemption(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="assignmentScopeValidation")
    def assignment_scope_validation(self) -> pulumi.Output[Optional[str]]:
        """
        The option whether validate the exemption is at or under the assignment scope.
        """
        return pulumi.get(self, "assignment_scope_validation")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the policy exemption.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The display name of the policy exemption.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="exemptionCategory")
    def exemption_category(self) -> pulumi.Output[str]:
        """
        The policy exemption category. Possible values are Waiver and Mitigated.
        """
        return pulumi.get(self, "exemption_category")

    @property
    @pulumi.getter(name="expiresOn")
    def expires_on(self) -> pulumi.Output[Optional[str]]:
        """
        The expiration date and time (in UTC ISO 8601 format yyyy-MM-ddTHH:mm:ssZ) of the policy exemption.
        """
        return pulumi.get(self, "expires_on")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Any]]:
        """
        The policy exemption metadata. Metadata is an open ended object and is typically a collection of key value pairs.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the policy exemption.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyAssignmentId")
    def policy_assignment_id(self) -> pulumi.Output[str]:
        """
        The ID of the policy assignment that is being exempted.
        """
        return pulumi.get(self, "policy_assignment_id")

    @property
    @pulumi.getter(name="policyDefinitionReferenceIds")
    def policy_definition_reference_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The policy definition reference ID list when the associated policy assignment is an assignment of a policy set definition.
        """
        return pulumi.get(self, "policy_definition_reference_ids")

    @property
    @pulumi.getter(name="resourceSelectors")
    def resource_selectors(self) -> pulumi.Output[Optional[Sequence['outputs.ResourceSelectorResponse']]]:
        """
        The resource selector list to filter policies by resource properties.
        """
        return pulumi.get(self, "resource_selectors")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource (Microsoft.Authorization/policyExemptions).
        """
        return pulumi.get(self, "type")

