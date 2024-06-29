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
    'GetClusterPoolResult',
    'AwaitableGetClusterPoolResult',
    'get_cluster_pool',
    'get_cluster_pool_output',
]

@pulumi.output_type
class GetClusterPoolResult:
    """
    Cluster pool.
    """
    def __init__(__self__, aks_cluster_profile=None, aks_managed_resource_group_name=None, cluster_pool_profile=None, compute_profile=None, deployment_id=None, id=None, location=None, log_analytics_profile=None, managed_resource_group_name=None, name=None, network_profile=None, provisioning_state=None, status=None, system_data=None, tags=None, type=None):
        if aks_cluster_profile and not isinstance(aks_cluster_profile, dict):
            raise TypeError("Expected argument 'aks_cluster_profile' to be a dict")
        pulumi.set(__self__, "aks_cluster_profile", aks_cluster_profile)
        if aks_managed_resource_group_name and not isinstance(aks_managed_resource_group_name, str):
            raise TypeError("Expected argument 'aks_managed_resource_group_name' to be a str")
        pulumi.set(__self__, "aks_managed_resource_group_name", aks_managed_resource_group_name)
        if cluster_pool_profile and not isinstance(cluster_pool_profile, dict):
            raise TypeError("Expected argument 'cluster_pool_profile' to be a dict")
        pulumi.set(__self__, "cluster_pool_profile", cluster_pool_profile)
        if compute_profile and not isinstance(compute_profile, dict):
            raise TypeError("Expected argument 'compute_profile' to be a dict")
        pulumi.set(__self__, "compute_profile", compute_profile)
        if deployment_id and not isinstance(deployment_id, str):
            raise TypeError("Expected argument 'deployment_id' to be a str")
        pulumi.set(__self__, "deployment_id", deployment_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if log_analytics_profile and not isinstance(log_analytics_profile, dict):
            raise TypeError("Expected argument 'log_analytics_profile' to be a dict")
        pulumi.set(__self__, "log_analytics_profile", log_analytics_profile)
        if managed_resource_group_name and not isinstance(managed_resource_group_name, str):
            raise TypeError("Expected argument 'managed_resource_group_name' to be a str")
        pulumi.set(__self__, "managed_resource_group_name", managed_resource_group_name)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_profile and not isinstance(network_profile, dict):
            raise TypeError("Expected argument 'network_profile' to be a dict")
        pulumi.set(__self__, "network_profile", network_profile)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="aksClusterProfile")
    def aks_cluster_profile(self) -> 'outputs.ClusterPoolResourcePropertiesResponseAksClusterProfile':
        """
        Properties of underlying AKS cluster.
        """
        return pulumi.get(self, "aks_cluster_profile")

    @property
    @pulumi.getter(name="aksManagedResourceGroupName")
    def aks_managed_resource_group_name(self) -> str:
        """
        A resource group created by AKS, to hold the infrastructure resources created by AKS on-behalf of customers. It is generated by cluster pool name and managed resource group name by pattern: MC_{managedResourceGroupName}_{clusterPoolName}_{region}
        """
        return pulumi.get(self, "aks_managed_resource_group_name")

    @property
    @pulumi.getter(name="clusterPoolProfile")
    def cluster_pool_profile(self) -> Optional['outputs.ClusterPoolResourcePropertiesResponseClusterPoolProfile']:
        """
        CLuster pool profile.
        """
        return pulumi.get(self, "cluster_pool_profile")

    @property
    @pulumi.getter(name="computeProfile")
    def compute_profile(self) -> 'outputs.ClusterPoolResourcePropertiesResponseComputeProfile':
        """
        CLuster pool compute profile.
        """
        return pulumi.get(self, "compute_profile")

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> str:
        """
        A unique id generated by the RP to identify the resource.
        """
        return pulumi.get(self, "deployment_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="logAnalyticsProfile")
    def log_analytics_profile(self) -> Optional['outputs.ClusterPoolResourcePropertiesResponseLogAnalyticsProfile']:
        """
        Cluster pool log analytics profile to enable OMS agent for AKS cluster.
        """
        return pulumi.get(self, "log_analytics_profile")

    @property
    @pulumi.getter(name="managedResourceGroupName")
    def managed_resource_group_name(self) -> Optional[str]:
        """
        A resource group created by RP, to hold the resources created by RP on-behalf of customers. It will also be used to generate aksManagedResourceGroupName by pattern: MC_{managedResourceGroupName}_{clusterPoolName}_{region}. Please make sure it meets resource group name restriction.
        """
        return pulumi.get(self, "managed_resource_group_name")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional['outputs.ClusterPoolResourcePropertiesResponseNetworkProfile']:
        """
        Cluster pool network profile.
        """
        return pulumi.get(self, "network_profile")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Business status of the resource.
        """
        return pulumi.get(self, "status")

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
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetClusterPoolResult(GetClusterPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterPoolResult(
            aks_cluster_profile=self.aks_cluster_profile,
            aks_managed_resource_group_name=self.aks_managed_resource_group_name,
            cluster_pool_profile=self.cluster_pool_profile,
            compute_profile=self.compute_profile,
            deployment_id=self.deployment_id,
            id=self.id,
            location=self.location,
            log_analytics_profile=self.log_analytics_profile,
            managed_resource_group_name=self.managed_resource_group_name,
            name=self.name,
            network_profile=self.network_profile,
            provisioning_state=self.provisioning_state,
            status=self.status,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_cluster_pool(cluster_pool_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterPoolResult:
    """
    Gets a cluster pool.


    :param str cluster_pool_name: The name of the cluster pool.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['clusterPoolName'] = cluster_pool_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:hdinsight/v20231101preview:getClusterPool', __args__, opts=opts, typ=GetClusterPoolResult).value

    return AwaitableGetClusterPoolResult(
        aks_cluster_profile=pulumi.get(__ret__, 'aks_cluster_profile'),
        aks_managed_resource_group_name=pulumi.get(__ret__, 'aks_managed_resource_group_name'),
        cluster_pool_profile=pulumi.get(__ret__, 'cluster_pool_profile'),
        compute_profile=pulumi.get(__ret__, 'compute_profile'),
        deployment_id=pulumi.get(__ret__, 'deployment_id'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        log_analytics_profile=pulumi.get(__ret__, 'log_analytics_profile'),
        managed_resource_group_name=pulumi.get(__ret__, 'managed_resource_group_name'),
        name=pulumi.get(__ret__, 'name'),
        network_profile=pulumi.get(__ret__, 'network_profile'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        status=pulumi.get(__ret__, 'status'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_cluster_pool)
def get_cluster_pool_output(cluster_pool_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterPoolResult]:
    """
    Gets a cluster pool.


    :param str cluster_pool_name: The name of the cluster pool.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
