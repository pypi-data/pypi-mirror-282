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

__all__ = ['WorkloadDeploymentArgs', 'WorkloadDeployment']

@pulumi.input_type
class WorkloadDeploymentArgs:
    def __init__(__self__, *,
                 modernize_project_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 properties: Optional[pulumi.Input['WorkloadDeploymentModelPropertiesArgs']] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workload_deployment_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WorkloadDeployment resource.
        :param pulumi.Input[str] modernize_project_name: ModernizeProject name.
        :param pulumi.Input[str] resource_group_name: Name of the Azure Resource Group that project is part of.
        :param pulumi.Input['WorkloadDeploymentModelPropertiesArgs'] properties: Workload deployment model properties.
        :param pulumi.Input[str] subscription_id: Azure Subscription Id in which project was created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Gets or sets the resource tags.
        :param pulumi.Input[str] workload_deployment_name: Workload deployment name.
        """
        pulumi.set(__self__, "modernize_project_name", modernize_project_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if subscription_id is not None:
            pulumi.set(__self__, "subscription_id", subscription_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if workload_deployment_name is not None:
            pulumi.set(__self__, "workload_deployment_name", workload_deployment_name)

    @property
    @pulumi.getter(name="modernizeProjectName")
    def modernize_project_name(self) -> pulumi.Input[str]:
        """
        ModernizeProject name.
        """
        return pulumi.get(self, "modernize_project_name")

    @modernize_project_name.setter
    def modernize_project_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "modernize_project_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the Azure Resource Group that project is part of.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['WorkloadDeploymentModelPropertiesArgs']]:
        """
        Workload deployment model properties.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['WorkloadDeploymentModelPropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        Azure Subscription Id in which project was created.
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Gets or sets the resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="workloadDeploymentName")
    def workload_deployment_name(self) -> Optional[pulumi.Input[str]]:
        """
        Workload deployment name.
        """
        return pulumi.get(self, "workload_deployment_name")

    @workload_deployment_name.setter
    def workload_deployment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workload_deployment_name", value)


class WorkloadDeployment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 modernize_project_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['WorkloadDeploymentModelPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workload_deployment_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Workload deployment model.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] modernize_project_name: ModernizeProject name.
        :param pulumi.Input[pulumi.InputType['WorkloadDeploymentModelPropertiesArgs']] properties: Workload deployment model properties.
        :param pulumi.Input[str] resource_group_name: Name of the Azure Resource Group that project is part of.
        :param pulumi.Input[str] subscription_id: Azure Subscription Id in which project was created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Gets or sets the resource tags.
        :param pulumi.Input[str] workload_deployment_name: Workload deployment name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkloadDeploymentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Workload deployment model.

        :param str resource_name: The name of the resource.
        :param WorkloadDeploymentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkloadDeploymentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 modernize_project_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['WorkloadDeploymentModelPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workload_deployment_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkloadDeploymentArgs.__new__(WorkloadDeploymentArgs)

            if modernize_project_name is None and not opts.urn:
                raise TypeError("Missing required property 'modernize_project_name'")
            __props__.__dict__["modernize_project_name"] = modernize_project_name
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["subscription_id"] = subscription_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["workload_deployment_name"] = workload_deployment_name
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:migrate:WorkloadDeployment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WorkloadDeployment, __self__).__init__(
            'azure-native:migrate/v20220501preview:WorkloadDeployment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkloadDeployment':
        """
        Get an existing WorkloadDeployment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkloadDeploymentArgs.__new__(WorkloadDeploymentArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return WorkloadDeployment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Gets or sets the name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.WorkloadDeploymentModelPropertiesResponse']:
        """
        Workload deployment model properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.WorkloadDeploymentModelResponseSystemData']:
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Gets or sets the resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Gets or sets the type of the resource.
        """
        return pulumi.get(self, "type")

