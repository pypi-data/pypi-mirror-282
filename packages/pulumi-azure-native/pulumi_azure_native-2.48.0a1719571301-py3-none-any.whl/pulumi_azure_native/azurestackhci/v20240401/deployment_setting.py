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

__all__ = ['DeploymentSettingArgs', 'DeploymentSetting']

@pulumi.input_type
class DeploymentSettingArgs:
    def __init__(__self__, *,
                 arc_node_resource_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 cluster_name: pulumi.Input[str],
                 deployment_configuration: pulumi.Input['DeploymentConfigurationArgs'],
                 deployment_mode: pulumi.Input[Union[str, 'DeploymentMode']],
                 resource_group_name: pulumi.Input[str],
                 deployment_settings_name: Optional[pulumi.Input[str]] = None,
                 operation_type: Optional[pulumi.Input[Union[str, 'OperationType']]] = None):
        """
        The set of arguments for constructing a DeploymentSetting resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] arc_node_resource_ids: Azure resource ids of Arc machines to be part of cluster.
        :param pulumi.Input[str] cluster_name: The name of the cluster.
        :param pulumi.Input['DeploymentConfigurationArgs'] deployment_configuration: Scale units will contains list of deployment data
        :param pulumi.Input[Union[str, 'DeploymentMode']] deployment_mode: The deployment mode for cluster deployment.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] deployment_settings_name: Name of Deployment Setting
        :param pulumi.Input[Union[str, 'OperationType']] operation_type: The intended operation for a cluster.
        """
        pulumi.set(__self__, "arc_node_resource_ids", arc_node_resource_ids)
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "deployment_configuration", deployment_configuration)
        pulumi.set(__self__, "deployment_mode", deployment_mode)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if deployment_settings_name is not None:
            pulumi.set(__self__, "deployment_settings_name", deployment_settings_name)
        if operation_type is None:
            operation_type = 'ClusterProvisioning'
        if operation_type is not None:
            pulumi.set(__self__, "operation_type", operation_type)

    @property
    @pulumi.getter(name="arcNodeResourceIds")
    def arc_node_resource_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Azure resource ids of Arc machines to be part of cluster.
        """
        return pulumi.get(self, "arc_node_resource_ids")

    @arc_node_resource_ids.setter
    def arc_node_resource_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "arc_node_resource_ids", value)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        The name of the cluster.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="deploymentConfiguration")
    def deployment_configuration(self) -> pulumi.Input['DeploymentConfigurationArgs']:
        """
        Scale units will contains list of deployment data
        """
        return pulumi.get(self, "deployment_configuration")

    @deployment_configuration.setter
    def deployment_configuration(self, value: pulumi.Input['DeploymentConfigurationArgs']):
        pulumi.set(self, "deployment_configuration", value)

    @property
    @pulumi.getter(name="deploymentMode")
    def deployment_mode(self) -> pulumi.Input[Union[str, 'DeploymentMode']]:
        """
        The deployment mode for cluster deployment.
        """
        return pulumi.get(self, "deployment_mode")

    @deployment_mode.setter
    def deployment_mode(self, value: pulumi.Input[Union[str, 'DeploymentMode']]):
        pulumi.set(self, "deployment_mode", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="deploymentSettingsName")
    def deployment_settings_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of Deployment Setting
        """
        return pulumi.get(self, "deployment_settings_name")

    @deployment_settings_name.setter
    def deployment_settings_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_settings_name", value)

    @property
    @pulumi.getter(name="operationType")
    def operation_type(self) -> Optional[pulumi.Input[Union[str, 'OperationType']]]:
        """
        The intended operation for a cluster.
        """
        return pulumi.get(self, "operation_type")

    @operation_type.setter
    def operation_type(self, value: Optional[pulumi.Input[Union[str, 'OperationType']]]):
        pulumi.set(self, "operation_type", value)


class DeploymentSetting(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 arc_node_resource_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 deployment_configuration: Optional[pulumi.Input[pulumi.InputType['DeploymentConfigurationArgs']]] = None,
                 deployment_mode: Optional[pulumi.Input[Union[str, 'DeploymentMode']]] = None,
                 deployment_settings_name: Optional[pulumi.Input[str]] = None,
                 operation_type: Optional[pulumi.Input[Union[str, 'OperationType']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Edge device resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] arc_node_resource_ids: Azure resource ids of Arc machines to be part of cluster.
        :param pulumi.Input[str] cluster_name: The name of the cluster.
        :param pulumi.Input[pulumi.InputType['DeploymentConfigurationArgs']] deployment_configuration: Scale units will contains list of deployment data
        :param pulumi.Input[Union[str, 'DeploymentMode']] deployment_mode: The deployment mode for cluster deployment.
        :param pulumi.Input[str] deployment_settings_name: Name of Deployment Setting
        :param pulumi.Input[Union[str, 'OperationType']] operation_type: The intended operation for a cluster.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DeploymentSettingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Edge device resource

        :param str resource_name: The name of the resource.
        :param DeploymentSettingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeploymentSettingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 arc_node_resource_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 deployment_configuration: Optional[pulumi.Input[pulumi.InputType['DeploymentConfigurationArgs']]] = None,
                 deployment_mode: Optional[pulumi.Input[Union[str, 'DeploymentMode']]] = None,
                 deployment_settings_name: Optional[pulumi.Input[str]] = None,
                 operation_type: Optional[pulumi.Input[Union[str, 'OperationType']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeploymentSettingArgs.__new__(DeploymentSettingArgs)

            if arc_node_resource_ids is None and not opts.urn:
                raise TypeError("Missing required property 'arc_node_resource_ids'")
            __props__.__dict__["arc_node_resource_ids"] = arc_node_resource_ids
            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            if deployment_configuration is None and not opts.urn:
                raise TypeError("Missing required property 'deployment_configuration'")
            __props__.__dict__["deployment_configuration"] = deployment_configuration
            if deployment_mode is None and not opts.urn:
                raise TypeError("Missing required property 'deployment_mode'")
            __props__.__dict__["deployment_mode"] = deployment_mode
            __props__.__dict__["deployment_settings_name"] = deployment_settings_name
            if operation_type is None:
                operation_type = 'ClusterProvisioning'
            __props__.__dict__["operation_type"] = operation_type
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["reported_properties"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:azurestackhci:DeploymentSetting"), pulumi.Alias(type_="azure-native:azurestackhci/v20230801preview:DeploymentSetting"), pulumi.Alias(type_="azure-native:azurestackhci/v20231101preview:DeploymentSetting"), pulumi.Alias(type_="azure-native:azurestackhci/v20240101:DeploymentSetting"), pulumi.Alias(type_="azure-native:azurestackhci/v20240215preview:DeploymentSetting")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DeploymentSetting, __self__).__init__(
            'azure-native:azurestackhci/v20240401:DeploymentSetting',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DeploymentSetting':
        """
        Get an existing DeploymentSetting resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DeploymentSettingArgs.__new__(DeploymentSettingArgs)

        __props__.__dict__["arc_node_resource_ids"] = None
        __props__.__dict__["deployment_configuration"] = None
        __props__.__dict__["deployment_mode"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["operation_type"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["reported_properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return DeploymentSetting(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="arcNodeResourceIds")
    def arc_node_resource_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        Azure resource ids of Arc machines to be part of cluster.
        """
        return pulumi.get(self, "arc_node_resource_ids")

    @property
    @pulumi.getter(name="deploymentConfiguration")
    def deployment_configuration(self) -> pulumi.Output['outputs.DeploymentConfigurationResponse']:
        """
        Scale units will contains list of deployment data
        """
        return pulumi.get(self, "deployment_configuration")

    @property
    @pulumi.getter(name="deploymentMode")
    def deployment_mode(self) -> pulumi.Output[str]:
        """
        The deployment mode for cluster deployment.
        """
        return pulumi.get(self, "deployment_mode")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="operationType")
    def operation_type(self) -> pulumi.Output[Optional[str]]:
        """
        The intended operation for a cluster.
        """
        return pulumi.get(self, "operation_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        DeploymentSetting provisioning state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="reportedProperties")
    def reported_properties(self) -> pulumi.Output['outputs.EceReportedPropertiesResponse']:
        """
        Deployment Status reported from cluster.
        """
        return pulumi.get(self, "reported_properties")

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
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

