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

__all__ = [
    'GetDeploymentSettingResult',
    'AwaitableGetDeploymentSettingResult',
    'get_deployment_setting',
    'get_deployment_setting_output',
]

@pulumi.output_type
class GetDeploymentSettingResult:
    """
    Edge device resource
    """
    def __init__(__self__, arc_node_resource_ids=None, deployment_configuration=None, deployment_mode=None, id=None, name=None, provisioning_state=None, reported_properties=None, system_data=None, type=None):
        if arc_node_resource_ids and not isinstance(arc_node_resource_ids, list):
            raise TypeError("Expected argument 'arc_node_resource_ids' to be a list")
        pulumi.set(__self__, "arc_node_resource_ids", arc_node_resource_ids)
        if deployment_configuration and not isinstance(deployment_configuration, dict):
            raise TypeError("Expected argument 'deployment_configuration' to be a dict")
        pulumi.set(__self__, "deployment_configuration", deployment_configuration)
        if deployment_mode and not isinstance(deployment_mode, str):
            raise TypeError("Expected argument 'deployment_mode' to be a str")
        pulumi.set(__self__, "deployment_mode", deployment_mode)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if reported_properties and not isinstance(reported_properties, dict):
            raise TypeError("Expected argument 'reported_properties' to be a dict")
        pulumi.set(__self__, "reported_properties", reported_properties)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="arcNodeResourceIds")
    def arc_node_resource_ids(self) -> Sequence[str]:
        """
        Azure resource ids of Arc machines to be part of cluster.
        """
        return pulumi.get(self, "arc_node_resource_ids")

    @property
    @pulumi.getter(name="deploymentConfiguration")
    def deployment_configuration(self) -> 'outputs.DeploymentConfigurationResponse':
        """
        Scale units will contains list of deployment data
        """
        return pulumi.get(self, "deployment_configuration")

    @property
    @pulumi.getter(name="deploymentMode")
    def deployment_mode(self) -> str:
        """
        The deployment mode for cluster deployment.
        """
        return pulumi.get(self, "deployment_mode")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        DeploymentSetting provisioning state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="reportedProperties")
    def reported_properties(self) -> 'outputs.EceReportedPropertiesResponse':
        """
        Deployment Status reported from cluster.
        """
        return pulumi.get(self, "reported_properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetDeploymentSettingResult(GetDeploymentSettingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDeploymentSettingResult(
            arc_node_resource_ids=self.arc_node_resource_ids,
            deployment_configuration=self.deployment_configuration,
            deployment_mode=self.deployment_mode,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            reported_properties=self.reported_properties,
            system_data=self.system_data,
            type=self.type)


def get_deployment_setting(cluster_name: Optional[str] = None,
                           deployment_settings_name: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDeploymentSettingResult:
    """
    Get a DeploymentSetting


    :param str cluster_name: The name of the cluster.
    :param str deployment_settings_name: Name of Deployment Setting
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['deploymentSettingsName'] = deployment_settings_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azurestackhci/v20240215preview:getDeploymentSetting', __args__, opts=opts, typ=GetDeploymentSettingResult).value

    return AwaitableGetDeploymentSettingResult(
        arc_node_resource_ids=pulumi.get(__ret__, 'arc_node_resource_ids'),
        deployment_configuration=pulumi.get(__ret__, 'deployment_configuration'),
        deployment_mode=pulumi.get(__ret__, 'deployment_mode'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        reported_properties=pulumi.get(__ret__, 'reported_properties'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_deployment_setting)
def get_deployment_setting_output(cluster_name: Optional[pulumi.Input[str]] = None,
                                  deployment_settings_name: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDeploymentSettingResult]:
    """
    Get a DeploymentSetting


    :param str cluster_name: The name of the cluster.
    :param str deployment_settings_name: Name of Deployment Setting
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
