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

__all__ = ['RemediationAtResourceGroupArgs', 'RemediationAtResourceGroup']

@pulumi.input_type
class RemediationAtResourceGroupArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 failure_threshold: Optional[pulumi.Input['RemediationPropertiesFailureThresholdArgs']] = None,
                 filters: Optional[pulumi.Input['RemediationFiltersArgs']] = None,
                 parallel_deployments: Optional[pulumi.Input[int]] = None,
                 policy_assignment_id: Optional[pulumi.Input[str]] = None,
                 policy_definition_reference_id: Optional[pulumi.Input[str]] = None,
                 remediation_name: Optional[pulumi.Input[str]] = None,
                 resource_count: Optional[pulumi.Input[int]] = None,
                 resource_discovery_mode: Optional[pulumi.Input[Union[str, 'ResourceDiscoveryMode']]] = None):
        """
        The set of arguments for constructing a RemediationAtResourceGroup resource.
        :param pulumi.Input[str] resource_group_name: Resource group name.
        :param pulumi.Input['RemediationPropertiesFailureThresholdArgs'] failure_threshold: The remediation failure threshold settings
        :param pulumi.Input['RemediationFiltersArgs'] filters: The filters that will be applied to determine which resources to remediate.
        :param pulumi.Input[int] parallel_deployments: Determines how many resources to remediate at any given time. Can be used to increase or reduce the pace of the remediation. If not provided, the default parallel deployments value is used.
        :param pulumi.Input[str] policy_assignment_id: The resource ID of the policy assignment that should be remediated.
        :param pulumi.Input[str] policy_definition_reference_id: The policy definition reference ID of the individual definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.
        :param pulumi.Input[str] remediation_name: The name of the remediation.
        :param pulumi.Input[int] resource_count: Determines the max number of resources that can be remediated by the remediation job. If not provided, the default resource count is used.
        :param pulumi.Input[Union[str, 'ResourceDiscoveryMode']] resource_discovery_mode: The way resources to remediate are discovered. Defaults to ExistingNonCompliant if not specified.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if failure_threshold is not None:
            pulumi.set(__self__, "failure_threshold", failure_threshold)
        if filters is not None:
            pulumi.set(__self__, "filters", filters)
        if parallel_deployments is not None:
            pulumi.set(__self__, "parallel_deployments", parallel_deployments)
        if policy_assignment_id is not None:
            pulumi.set(__self__, "policy_assignment_id", policy_assignment_id)
        if policy_definition_reference_id is not None:
            pulumi.set(__self__, "policy_definition_reference_id", policy_definition_reference_id)
        if remediation_name is not None:
            pulumi.set(__self__, "remediation_name", remediation_name)
        if resource_count is not None:
            pulumi.set(__self__, "resource_count", resource_count)
        if resource_discovery_mode is not None:
            pulumi.set(__self__, "resource_discovery_mode", resource_discovery_mode)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[pulumi.Input['RemediationPropertiesFailureThresholdArgs']]:
        """
        The remediation failure threshold settings
        """
        return pulumi.get(self, "failure_threshold")

    @failure_threshold.setter
    def failure_threshold(self, value: Optional[pulumi.Input['RemediationPropertiesFailureThresholdArgs']]):
        pulumi.set(self, "failure_threshold", value)

    @property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input['RemediationFiltersArgs']]:
        """
        The filters that will be applied to determine which resources to remediate.
        """
        return pulumi.get(self, "filters")

    @filters.setter
    def filters(self, value: Optional[pulumi.Input['RemediationFiltersArgs']]):
        pulumi.set(self, "filters", value)

    @property
    @pulumi.getter(name="parallelDeployments")
    def parallel_deployments(self) -> Optional[pulumi.Input[int]]:
        """
        Determines how many resources to remediate at any given time. Can be used to increase or reduce the pace of the remediation. If not provided, the default parallel deployments value is used.
        """
        return pulumi.get(self, "parallel_deployments")

    @parallel_deployments.setter
    def parallel_deployments(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "parallel_deployments", value)

    @property
    @pulumi.getter(name="policyAssignmentId")
    def policy_assignment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the policy assignment that should be remediated.
        """
        return pulumi.get(self, "policy_assignment_id")

    @policy_assignment_id.setter
    def policy_assignment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_assignment_id", value)

    @property
    @pulumi.getter(name="policyDefinitionReferenceId")
    def policy_definition_reference_id(self) -> Optional[pulumi.Input[str]]:
        """
        The policy definition reference ID of the individual definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.
        """
        return pulumi.get(self, "policy_definition_reference_id")

    @policy_definition_reference_id.setter
    def policy_definition_reference_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_definition_reference_id", value)

    @property
    @pulumi.getter(name="remediationName")
    def remediation_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the remediation.
        """
        return pulumi.get(self, "remediation_name")

    @remediation_name.setter
    def remediation_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remediation_name", value)

    @property
    @pulumi.getter(name="resourceCount")
    def resource_count(self) -> Optional[pulumi.Input[int]]:
        """
        Determines the max number of resources that can be remediated by the remediation job. If not provided, the default resource count is used.
        """
        return pulumi.get(self, "resource_count")

    @resource_count.setter
    def resource_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "resource_count", value)

    @property
    @pulumi.getter(name="resourceDiscoveryMode")
    def resource_discovery_mode(self) -> Optional[pulumi.Input[Union[str, 'ResourceDiscoveryMode']]]:
        """
        The way resources to remediate are discovered. Defaults to ExistingNonCompliant if not specified.
        """
        return pulumi.get(self, "resource_discovery_mode")

    @resource_discovery_mode.setter
    def resource_discovery_mode(self, value: Optional[pulumi.Input[Union[str, 'ResourceDiscoveryMode']]]):
        pulumi.set(self, "resource_discovery_mode", value)


class RemediationAtResourceGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 failure_threshold: Optional[pulumi.Input[pulumi.InputType['RemediationPropertiesFailureThresholdArgs']]] = None,
                 filters: Optional[pulumi.Input[pulumi.InputType['RemediationFiltersArgs']]] = None,
                 parallel_deployments: Optional[pulumi.Input[int]] = None,
                 policy_assignment_id: Optional[pulumi.Input[str]] = None,
                 policy_definition_reference_id: Optional[pulumi.Input[str]] = None,
                 remediation_name: Optional[pulumi.Input[str]] = None,
                 resource_count: Optional[pulumi.Input[int]] = None,
                 resource_discovery_mode: Optional[pulumi.Input[Union[str, 'ResourceDiscoveryMode']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The remediation definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['RemediationPropertiesFailureThresholdArgs']] failure_threshold: The remediation failure threshold settings
        :param pulumi.Input[pulumi.InputType['RemediationFiltersArgs']] filters: The filters that will be applied to determine which resources to remediate.
        :param pulumi.Input[int] parallel_deployments: Determines how many resources to remediate at any given time. Can be used to increase or reduce the pace of the remediation. If not provided, the default parallel deployments value is used.
        :param pulumi.Input[str] policy_assignment_id: The resource ID of the policy assignment that should be remediated.
        :param pulumi.Input[str] policy_definition_reference_id: The policy definition reference ID of the individual definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.
        :param pulumi.Input[str] remediation_name: The name of the remediation.
        :param pulumi.Input[int] resource_count: Determines the max number of resources that can be remediated by the remediation job. If not provided, the default resource count is used.
        :param pulumi.Input[Union[str, 'ResourceDiscoveryMode']] resource_discovery_mode: The way resources to remediate are discovered. Defaults to ExistingNonCompliant if not specified.
        :param pulumi.Input[str] resource_group_name: Resource group name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RemediationAtResourceGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The remediation definition.

        :param str resource_name: The name of the resource.
        :param RemediationAtResourceGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RemediationAtResourceGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 failure_threshold: Optional[pulumi.Input[pulumi.InputType['RemediationPropertiesFailureThresholdArgs']]] = None,
                 filters: Optional[pulumi.Input[pulumi.InputType['RemediationFiltersArgs']]] = None,
                 parallel_deployments: Optional[pulumi.Input[int]] = None,
                 policy_assignment_id: Optional[pulumi.Input[str]] = None,
                 policy_definition_reference_id: Optional[pulumi.Input[str]] = None,
                 remediation_name: Optional[pulumi.Input[str]] = None,
                 resource_count: Optional[pulumi.Input[int]] = None,
                 resource_discovery_mode: Optional[pulumi.Input[Union[str, 'ResourceDiscoveryMode']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RemediationAtResourceGroupArgs.__new__(RemediationAtResourceGroupArgs)

            __props__.__dict__["failure_threshold"] = failure_threshold
            __props__.__dict__["filters"] = filters
            __props__.__dict__["parallel_deployments"] = parallel_deployments
            __props__.__dict__["policy_assignment_id"] = policy_assignment_id
            __props__.__dict__["policy_definition_reference_id"] = policy_definition_reference_id
            __props__.__dict__["remediation_name"] = remediation_name
            __props__.__dict__["resource_count"] = resource_count
            __props__.__dict__["resource_discovery_mode"] = resource_discovery_mode
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["correlation_id"] = None
            __props__.__dict__["created_on"] = None
            __props__.__dict__["deployment_status"] = None
            __props__.__dict__["last_updated_on"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status_message"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:policyinsights:RemediationAtResourceGroup"), pulumi.Alias(type_="azure-native:policyinsights/v20180701preview:RemediationAtResourceGroup"), pulumi.Alias(type_="azure-native:policyinsights/v20190701:RemediationAtResourceGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(RemediationAtResourceGroup, __self__).__init__(
            'azure-native:policyinsights/v20211001:RemediationAtResourceGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RemediationAtResourceGroup':
        """
        Get an existing RemediationAtResourceGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RemediationAtResourceGroupArgs.__new__(RemediationAtResourceGroupArgs)

        __props__.__dict__["correlation_id"] = None
        __props__.__dict__["created_on"] = None
        __props__.__dict__["deployment_status"] = None
        __props__.__dict__["failure_threshold"] = None
        __props__.__dict__["filters"] = None
        __props__.__dict__["last_updated_on"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parallel_deployments"] = None
        __props__.__dict__["policy_assignment_id"] = None
        __props__.__dict__["policy_definition_reference_id"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_count"] = None
        __props__.__dict__["resource_discovery_mode"] = None
        __props__.__dict__["status_message"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return RemediationAtResourceGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> pulumi.Output[str]:
        """
        The remediation correlation Id. Can be used to find events related to the remediation in the activity log.
        """
        return pulumi.get(self, "correlation_id")

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> pulumi.Output[str]:
        """
        The time at which the remediation was created.
        """
        return pulumi.get(self, "created_on")

    @property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> pulumi.Output['outputs.RemediationDeploymentSummaryResponse']:
        """
        The deployment status summary for all deployments created by the remediation.
        """
        return pulumi.get(self, "deployment_status")

    @property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> pulumi.Output[Optional['outputs.RemediationPropertiesResponseFailureThreshold']]:
        """
        The remediation failure threshold settings
        """
        return pulumi.get(self, "failure_threshold")

    @property
    @pulumi.getter
    def filters(self) -> pulumi.Output[Optional['outputs.RemediationFiltersResponse']]:
        """
        The filters that will be applied to determine which resources to remediate.
        """
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> pulumi.Output[str]:
        """
        The time at which the remediation was last updated.
        """
        return pulumi.get(self, "last_updated_on")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the remediation.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parallelDeployments")
    def parallel_deployments(self) -> pulumi.Output[Optional[int]]:
        """
        Determines how many resources to remediate at any given time. Can be used to increase or reduce the pace of the remediation. If not provided, the default parallel deployments value is used.
        """
        return pulumi.get(self, "parallel_deployments")

    @property
    @pulumi.getter(name="policyAssignmentId")
    def policy_assignment_id(self) -> pulumi.Output[Optional[str]]:
        """
        The resource ID of the policy assignment that should be remediated.
        """
        return pulumi.get(self, "policy_assignment_id")

    @property
    @pulumi.getter(name="policyDefinitionReferenceId")
    def policy_definition_reference_id(self) -> pulumi.Output[Optional[str]]:
        """
        The policy definition reference ID of the individual definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.
        """
        return pulumi.get(self, "policy_definition_reference_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The status of the remediation. This refers to the entire remediation task, not individual deployments. Allowed values are Evaluating, Canceled, Cancelling, Failed, Complete, or Succeeded.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceCount")
    def resource_count(self) -> pulumi.Output[Optional[int]]:
        """
        Determines the max number of resources that can be remediated by the remediation job. If not provided, the default resource count is used.
        """
        return pulumi.get(self, "resource_count")

    @property
    @pulumi.getter(name="resourceDiscoveryMode")
    def resource_discovery_mode(self) -> pulumi.Output[Optional[str]]:
        """
        The way resources to remediate are discovered. Defaults to ExistingNonCompliant if not specified.
        """
        return pulumi.get(self, "resource_discovery_mode")

    @property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Output[str]:
        """
        The remediation status message. Provides additional details regarding the state of the remediation.
        """
        return pulumi.get(self, "status_message")

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
        The type of the remediation.
        """
        return pulumi.get(self, "type")

