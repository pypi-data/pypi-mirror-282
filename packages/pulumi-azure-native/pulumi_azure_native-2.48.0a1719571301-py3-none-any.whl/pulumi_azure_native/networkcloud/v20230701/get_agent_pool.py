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
    'GetAgentPoolResult',
    'AwaitableGetAgentPoolResult',
    'get_agent_pool',
    'get_agent_pool_output',
]

@pulumi.output_type
class GetAgentPoolResult:
    def __init__(__self__, administrator_configuration=None, agent_options=None, attached_network_configuration=None, availability_zones=None, count=None, detailed_status=None, detailed_status_message=None, extended_location=None, id=None, kubernetes_version=None, labels=None, location=None, mode=None, name=None, provisioning_state=None, system_data=None, tags=None, taints=None, type=None, upgrade_settings=None, vm_sku_name=None):
        if administrator_configuration and not isinstance(administrator_configuration, dict):
            raise TypeError("Expected argument 'administrator_configuration' to be a dict")
        pulumi.set(__self__, "administrator_configuration", administrator_configuration)
        if agent_options and not isinstance(agent_options, dict):
            raise TypeError("Expected argument 'agent_options' to be a dict")
        pulumi.set(__self__, "agent_options", agent_options)
        if attached_network_configuration and not isinstance(attached_network_configuration, dict):
            raise TypeError("Expected argument 'attached_network_configuration' to be a dict")
        pulumi.set(__self__, "attached_network_configuration", attached_network_configuration)
        if availability_zones and not isinstance(availability_zones, list):
            raise TypeError("Expected argument 'availability_zones' to be a list")
        pulumi.set(__self__, "availability_zones", availability_zones)
        if count and not isinstance(count, float):
            raise TypeError("Expected argument 'count' to be a float")
        pulumi.set(__self__, "count", count)
        if detailed_status and not isinstance(detailed_status, str):
            raise TypeError("Expected argument 'detailed_status' to be a str")
        pulumi.set(__self__, "detailed_status", detailed_status)
        if detailed_status_message and not isinstance(detailed_status_message, str):
            raise TypeError("Expected argument 'detailed_status_message' to be a str")
        pulumi.set(__self__, "detailed_status_message", detailed_status_message)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kubernetes_version and not isinstance(kubernetes_version, str):
            raise TypeError("Expected argument 'kubernetes_version' to be a str")
        pulumi.set(__self__, "kubernetes_version", kubernetes_version)
        if labels and not isinstance(labels, list):
            raise TypeError("Expected argument 'labels' to be a list")
        pulumi.set(__self__, "labels", labels)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if mode and not isinstance(mode, str):
            raise TypeError("Expected argument 'mode' to be a str")
        pulumi.set(__self__, "mode", mode)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if taints and not isinstance(taints, list):
            raise TypeError("Expected argument 'taints' to be a list")
        pulumi.set(__self__, "taints", taints)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if upgrade_settings and not isinstance(upgrade_settings, dict):
            raise TypeError("Expected argument 'upgrade_settings' to be a dict")
        pulumi.set(__self__, "upgrade_settings", upgrade_settings)
        if vm_sku_name and not isinstance(vm_sku_name, str):
            raise TypeError("Expected argument 'vm_sku_name' to be a str")
        pulumi.set(__self__, "vm_sku_name", vm_sku_name)

    @property
    @pulumi.getter(name="administratorConfiguration")
    def administrator_configuration(self) -> Optional['outputs.AdministratorConfigurationResponse']:
        """
        The administrator credentials to be used for the nodes in this agent pool.
        """
        return pulumi.get(self, "administrator_configuration")

    @property
    @pulumi.getter(name="agentOptions")
    def agent_options(self) -> Optional['outputs.AgentOptionsResponse']:
        """
        The configurations that will be applied to each agent in this agent pool.
        """
        return pulumi.get(self, "agent_options")

    @property
    @pulumi.getter(name="attachedNetworkConfiguration")
    def attached_network_configuration(self) -> Optional['outputs.AttachedNetworkConfigurationResponse']:
        """
        The configuration of networks being attached to the agent pool for use by the workloads that run on this Kubernetes cluster.
        """
        return pulumi.get(self, "attached_network_configuration")

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[Sequence[str]]:
        """
        The list of availability zones of the Network Cloud cluster used for the provisioning of nodes in this agent pool. If not specified, all availability zones will be used.
        """
        return pulumi.get(self, "availability_zones")

    @property
    @pulumi.getter
    def count(self) -> float:
        """
        The number of virtual machines that use this configuration.
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> str:
        """
        The current status of the agent pool.
        """
        return pulumi.get(self, "detailed_status")

    @property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> str:
        """
        The descriptive message about the current detailed status.
        """
        return pulumi.get(self, "detailed_status_message")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional['outputs.ExtendedLocationResponse']:
        """
        The extended location of the cluster associated with the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> str:
        """
        The Kubernetes version running in this agent pool.
        """
        return pulumi.get(self, "kubernetes_version")

    @property
    @pulumi.getter
    def labels(self) -> Optional[Sequence['outputs.KubernetesLabelResponse']]:
        """
        The labels applied to the nodes in this agent pool.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def mode(self) -> str:
        """
        The selection of how this agent pool is utilized, either as a system pool or a user pool. System pools run the features and critical services for the Kubernetes Cluster, while user pools are dedicated to user workloads. Every Kubernetes cluster must contain at least one system node pool with at least one node.
        """
        return pulumi.get(self, "mode")

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
        The provisioning state of the agent pool.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def taints(self) -> Optional[Sequence['outputs.KubernetesLabelResponse']]:
        """
        The taints applied to the nodes in this agent pool.
        """
        return pulumi.get(self, "taints")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(self) -> Optional['outputs.AgentPoolUpgradeSettingsResponse']:
        """
        The configuration of the agent pool.
        """
        return pulumi.get(self, "upgrade_settings")

    @property
    @pulumi.getter(name="vmSkuName")
    def vm_sku_name(self) -> str:
        """
        The name of the VM SKU that determines the size of resources allocated for node VMs.
        """
        return pulumi.get(self, "vm_sku_name")


class AwaitableGetAgentPoolResult(GetAgentPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAgentPoolResult(
            administrator_configuration=self.administrator_configuration,
            agent_options=self.agent_options,
            attached_network_configuration=self.attached_network_configuration,
            availability_zones=self.availability_zones,
            count=self.count,
            detailed_status=self.detailed_status,
            detailed_status_message=self.detailed_status_message,
            extended_location=self.extended_location,
            id=self.id,
            kubernetes_version=self.kubernetes_version,
            labels=self.labels,
            location=self.location,
            mode=self.mode,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            taints=self.taints,
            type=self.type,
            upgrade_settings=self.upgrade_settings,
            vm_sku_name=self.vm_sku_name)


def get_agent_pool(agent_pool_name: Optional[str] = None,
                   kubernetes_cluster_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAgentPoolResult:
    """
    Get properties of the provided Kubernetes cluster agent pool.


    :param str agent_pool_name: The name of the Kubernetes cluster agent pool.
    :param str kubernetes_cluster_name: The name of the Kubernetes cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['agentPoolName'] = agent_pool_name
    __args__['kubernetesClusterName'] = kubernetes_cluster_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:networkcloud/v20230701:getAgentPool', __args__, opts=opts, typ=GetAgentPoolResult).value

    return AwaitableGetAgentPoolResult(
        administrator_configuration=pulumi.get(__ret__, 'administrator_configuration'),
        agent_options=pulumi.get(__ret__, 'agent_options'),
        attached_network_configuration=pulumi.get(__ret__, 'attached_network_configuration'),
        availability_zones=pulumi.get(__ret__, 'availability_zones'),
        count=pulumi.get(__ret__, 'count'),
        detailed_status=pulumi.get(__ret__, 'detailed_status'),
        detailed_status_message=pulumi.get(__ret__, 'detailed_status_message'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        id=pulumi.get(__ret__, 'id'),
        kubernetes_version=pulumi.get(__ret__, 'kubernetes_version'),
        labels=pulumi.get(__ret__, 'labels'),
        location=pulumi.get(__ret__, 'location'),
        mode=pulumi.get(__ret__, 'mode'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        taints=pulumi.get(__ret__, 'taints'),
        type=pulumi.get(__ret__, 'type'),
        upgrade_settings=pulumi.get(__ret__, 'upgrade_settings'),
        vm_sku_name=pulumi.get(__ret__, 'vm_sku_name'))


@_utilities.lift_output_func(get_agent_pool)
def get_agent_pool_output(agent_pool_name: Optional[pulumi.Input[str]] = None,
                          kubernetes_cluster_name: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAgentPoolResult]:
    """
    Get properties of the provided Kubernetes cluster agent pool.


    :param str agent_pool_name: The name of the Kubernetes cluster agent pool.
    :param str kubernetes_cluster_name: The name of the Kubernetes cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
