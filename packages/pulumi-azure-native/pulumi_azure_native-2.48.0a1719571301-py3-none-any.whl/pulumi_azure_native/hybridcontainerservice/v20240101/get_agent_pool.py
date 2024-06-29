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
    """
    The agentPool resource definition
    """
    def __init__(__self__, count=None, enable_auto_scaling=None, extended_location=None, id=None, kubernetes_version=None, max_count=None, max_pods=None, min_count=None, name=None, node_labels=None, node_taints=None, os_sku=None, os_type=None, provisioning_state=None, status=None, system_data=None, tags=None, type=None, vm_size=None):
        if count and not isinstance(count, int):
            raise TypeError("Expected argument 'count' to be a int")
        pulumi.set(__self__, "count", count)
        if enable_auto_scaling and not isinstance(enable_auto_scaling, bool):
            raise TypeError("Expected argument 'enable_auto_scaling' to be a bool")
        pulumi.set(__self__, "enable_auto_scaling", enable_auto_scaling)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kubernetes_version and not isinstance(kubernetes_version, str):
            raise TypeError("Expected argument 'kubernetes_version' to be a str")
        pulumi.set(__self__, "kubernetes_version", kubernetes_version)
        if max_count and not isinstance(max_count, int):
            raise TypeError("Expected argument 'max_count' to be a int")
        pulumi.set(__self__, "max_count", max_count)
        if max_pods and not isinstance(max_pods, int):
            raise TypeError("Expected argument 'max_pods' to be a int")
        pulumi.set(__self__, "max_pods", max_pods)
        if min_count and not isinstance(min_count, int):
            raise TypeError("Expected argument 'min_count' to be a int")
        pulumi.set(__self__, "min_count", min_count)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if node_labels and not isinstance(node_labels, dict):
            raise TypeError("Expected argument 'node_labels' to be a dict")
        pulumi.set(__self__, "node_labels", node_labels)
        if node_taints and not isinstance(node_taints, list):
            raise TypeError("Expected argument 'node_taints' to be a list")
        pulumi.set(__self__, "node_taints", node_taints)
        if os_sku and not isinstance(os_sku, str):
            raise TypeError("Expected argument 'os_sku' to be a str")
        pulumi.set(__self__, "os_sku", os_sku)
        if os_type and not isinstance(os_type, str):
            raise TypeError("Expected argument 'os_type' to be a str")
        pulumi.set(__self__, "os_type", os_type)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if status and not isinstance(status, dict):
            raise TypeError("Expected argument 'status' to be a dict")
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
        if vm_size and not isinstance(vm_size, str):
            raise TypeError("Expected argument 'vm_size' to be a str")
        pulumi.set(__self__, "vm_size", vm_size)

    @property
    @pulumi.getter
    def count(self) -> Optional[int]:
        """
        Number of nodes in the agent pool. The default value is 1.
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter(name="enableAutoScaling")
    def enable_auto_scaling(self) -> Optional[bool]:
        """
        Whether to enable auto-scaler. Default value is false
        """
        return pulumi.get(self, "enable_auto_scaling")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional['outputs.ExtendedLocationResponse']:
        """
        Extended location pointing to the underlying infrastructure
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
        Version of Kubernetes in use by the agent pool. This is inherited from the kubernetesVersion of the provisioned cluster.
        """
        return pulumi.get(self, "kubernetes_version")

    @property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> Optional[int]:
        """
        The maximum number of nodes for auto-scaling
        """
        return pulumi.get(self, "max_count")

    @property
    @pulumi.getter(name="maxPods")
    def max_pods(self) -> Optional[int]:
        """
        The maximum number of pods that can run on a node.
        """
        return pulumi.get(self, "max_pods")

    @property
    @pulumi.getter(name="minCount")
    def min_count(self) -> Optional[int]:
        """
        The minimum number of nodes for auto-scaling
        """
        return pulumi.get(self, "min_count")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeLabels")
    def node_labels(self) -> Optional[Mapping[str, str]]:
        """
        The node labels to be persisted across all nodes in agent pool.
        """
        return pulumi.get(self, "node_labels")

    @property
    @pulumi.getter(name="nodeTaints")
    def node_taints(self) -> Optional[Sequence[str]]:
        """
        Taints added to new nodes during node pool create and scale. For example, key=value:NoSchedule.
        """
        return pulumi.get(self, "node_taints")

    @property
    @pulumi.getter(name="osSKU")
    def os_sku(self) -> Optional[str]:
        """
        Specifies the OS SKU used by the agent pool. The default is CBLMariner if OSType is Linux. The default is Windows2019 when OSType is Windows.
        """
        return pulumi.get(self, "os_sku")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[str]:
        """
        OSType to be used to specify OS type for the VMs. Choose from Linux and Windows. Default to Linux. Possible values include: 'Linux', 'Windows'
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The status of the latest long running operation for the agent pool.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> Optional['outputs.AgentPoolProvisioningStatusResponseStatus']:
        """
        The observed status of the agent pool.
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
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[str]:
        """
        The VM sku size of the agent pool node VMs.
        """
        return pulumi.get(self, "vm_size")


class AwaitableGetAgentPoolResult(GetAgentPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAgentPoolResult(
            count=self.count,
            enable_auto_scaling=self.enable_auto_scaling,
            extended_location=self.extended_location,
            id=self.id,
            kubernetes_version=self.kubernetes_version,
            max_count=self.max_count,
            max_pods=self.max_pods,
            min_count=self.min_count,
            name=self.name,
            node_labels=self.node_labels,
            node_taints=self.node_taints,
            os_sku=self.os_sku,
            os_type=self.os_type,
            provisioning_state=self.provisioning_state,
            status=self.status,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            vm_size=self.vm_size)


def get_agent_pool(agent_pool_name: Optional[str] = None,
                   connected_cluster_resource_uri: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAgentPoolResult:
    """
    Gets the specified agent pool in the provisioned cluster


    :param str agent_pool_name: Parameter for the name of the agent pool in the provisioned cluster.
    :param str connected_cluster_resource_uri: The fully qualified Azure Resource Manager identifier of the connected cluster resource.
    """
    __args__ = dict()
    __args__['agentPoolName'] = agent_pool_name
    __args__['connectedClusterResourceUri'] = connected_cluster_resource_uri
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:hybridcontainerservice/v20240101:getAgentPool', __args__, opts=opts, typ=GetAgentPoolResult).value

    return AwaitableGetAgentPoolResult(
        count=pulumi.get(__ret__, 'count'),
        enable_auto_scaling=pulumi.get(__ret__, 'enable_auto_scaling'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        id=pulumi.get(__ret__, 'id'),
        kubernetes_version=pulumi.get(__ret__, 'kubernetes_version'),
        max_count=pulumi.get(__ret__, 'max_count'),
        max_pods=pulumi.get(__ret__, 'max_pods'),
        min_count=pulumi.get(__ret__, 'min_count'),
        name=pulumi.get(__ret__, 'name'),
        node_labels=pulumi.get(__ret__, 'node_labels'),
        node_taints=pulumi.get(__ret__, 'node_taints'),
        os_sku=pulumi.get(__ret__, 'os_sku'),
        os_type=pulumi.get(__ret__, 'os_type'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        status=pulumi.get(__ret__, 'status'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        vm_size=pulumi.get(__ret__, 'vm_size'))


@_utilities.lift_output_func(get_agent_pool)
def get_agent_pool_output(agent_pool_name: Optional[pulumi.Input[str]] = None,
                          connected_cluster_resource_uri: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAgentPoolResult]:
    """
    Gets the specified agent pool in the provisioned cluster


    :param str agent_pool_name: Parameter for the name of the agent pool in the provisioned cluster.
    :param str connected_cluster_resource_uri: The fully qualified Azure Resource Manager identifier of the connected cluster resource.
    """
    ...
