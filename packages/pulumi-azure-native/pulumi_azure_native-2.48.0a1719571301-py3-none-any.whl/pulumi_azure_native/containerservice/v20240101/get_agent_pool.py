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
    Agent Pool.
    """
    def __init__(__self__, availability_zones=None, capacity_reservation_group_id=None, count=None, creation_data=None, current_orchestrator_version=None, enable_auto_scaling=None, enable_encryption_at_host=None, enable_fips=None, enable_node_public_ip=None, enable_ultra_ssd=None, gpu_instance_profile=None, host_group_id=None, id=None, kubelet_config=None, kubelet_disk_type=None, linux_os_config=None, max_count=None, max_pods=None, min_count=None, mode=None, name=None, network_profile=None, node_image_version=None, node_labels=None, node_public_ip_prefix_id=None, node_taints=None, orchestrator_version=None, os_disk_size_gb=None, os_disk_type=None, os_sku=None, os_type=None, pod_subnet_id=None, power_state=None, provisioning_state=None, proximity_placement_group_id=None, scale_down_mode=None, scale_set_eviction_policy=None, scale_set_priority=None, spot_max_price=None, tags=None, type=None, upgrade_settings=None, vm_size=None, vnet_subnet_id=None, workload_runtime=None):
        if availability_zones and not isinstance(availability_zones, list):
            raise TypeError("Expected argument 'availability_zones' to be a list")
        pulumi.set(__self__, "availability_zones", availability_zones)
        if capacity_reservation_group_id and not isinstance(capacity_reservation_group_id, str):
            raise TypeError("Expected argument 'capacity_reservation_group_id' to be a str")
        pulumi.set(__self__, "capacity_reservation_group_id", capacity_reservation_group_id)
        if count and not isinstance(count, int):
            raise TypeError("Expected argument 'count' to be a int")
        pulumi.set(__self__, "count", count)
        if creation_data and not isinstance(creation_data, dict):
            raise TypeError("Expected argument 'creation_data' to be a dict")
        pulumi.set(__self__, "creation_data", creation_data)
        if current_orchestrator_version and not isinstance(current_orchestrator_version, str):
            raise TypeError("Expected argument 'current_orchestrator_version' to be a str")
        pulumi.set(__self__, "current_orchestrator_version", current_orchestrator_version)
        if enable_auto_scaling and not isinstance(enable_auto_scaling, bool):
            raise TypeError("Expected argument 'enable_auto_scaling' to be a bool")
        pulumi.set(__self__, "enable_auto_scaling", enable_auto_scaling)
        if enable_encryption_at_host and not isinstance(enable_encryption_at_host, bool):
            raise TypeError("Expected argument 'enable_encryption_at_host' to be a bool")
        pulumi.set(__self__, "enable_encryption_at_host", enable_encryption_at_host)
        if enable_fips and not isinstance(enable_fips, bool):
            raise TypeError("Expected argument 'enable_fips' to be a bool")
        pulumi.set(__self__, "enable_fips", enable_fips)
        if enable_node_public_ip and not isinstance(enable_node_public_ip, bool):
            raise TypeError("Expected argument 'enable_node_public_ip' to be a bool")
        pulumi.set(__self__, "enable_node_public_ip", enable_node_public_ip)
        if enable_ultra_ssd and not isinstance(enable_ultra_ssd, bool):
            raise TypeError("Expected argument 'enable_ultra_ssd' to be a bool")
        pulumi.set(__self__, "enable_ultra_ssd", enable_ultra_ssd)
        if gpu_instance_profile and not isinstance(gpu_instance_profile, str):
            raise TypeError("Expected argument 'gpu_instance_profile' to be a str")
        pulumi.set(__self__, "gpu_instance_profile", gpu_instance_profile)
        if host_group_id and not isinstance(host_group_id, str):
            raise TypeError("Expected argument 'host_group_id' to be a str")
        pulumi.set(__self__, "host_group_id", host_group_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kubelet_config and not isinstance(kubelet_config, dict):
            raise TypeError("Expected argument 'kubelet_config' to be a dict")
        pulumi.set(__self__, "kubelet_config", kubelet_config)
        if kubelet_disk_type and not isinstance(kubelet_disk_type, str):
            raise TypeError("Expected argument 'kubelet_disk_type' to be a str")
        pulumi.set(__self__, "kubelet_disk_type", kubelet_disk_type)
        if linux_os_config and not isinstance(linux_os_config, dict):
            raise TypeError("Expected argument 'linux_os_config' to be a dict")
        pulumi.set(__self__, "linux_os_config", linux_os_config)
        if max_count and not isinstance(max_count, int):
            raise TypeError("Expected argument 'max_count' to be a int")
        pulumi.set(__self__, "max_count", max_count)
        if max_pods and not isinstance(max_pods, int):
            raise TypeError("Expected argument 'max_pods' to be a int")
        pulumi.set(__self__, "max_pods", max_pods)
        if min_count and not isinstance(min_count, int):
            raise TypeError("Expected argument 'min_count' to be a int")
        pulumi.set(__self__, "min_count", min_count)
        if mode and not isinstance(mode, str):
            raise TypeError("Expected argument 'mode' to be a str")
        pulumi.set(__self__, "mode", mode)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_profile and not isinstance(network_profile, dict):
            raise TypeError("Expected argument 'network_profile' to be a dict")
        pulumi.set(__self__, "network_profile", network_profile)
        if node_image_version and not isinstance(node_image_version, str):
            raise TypeError("Expected argument 'node_image_version' to be a str")
        pulumi.set(__self__, "node_image_version", node_image_version)
        if node_labels and not isinstance(node_labels, dict):
            raise TypeError("Expected argument 'node_labels' to be a dict")
        pulumi.set(__self__, "node_labels", node_labels)
        if node_public_ip_prefix_id and not isinstance(node_public_ip_prefix_id, str):
            raise TypeError("Expected argument 'node_public_ip_prefix_id' to be a str")
        pulumi.set(__self__, "node_public_ip_prefix_id", node_public_ip_prefix_id)
        if node_taints and not isinstance(node_taints, list):
            raise TypeError("Expected argument 'node_taints' to be a list")
        pulumi.set(__self__, "node_taints", node_taints)
        if orchestrator_version and not isinstance(orchestrator_version, str):
            raise TypeError("Expected argument 'orchestrator_version' to be a str")
        pulumi.set(__self__, "orchestrator_version", orchestrator_version)
        if os_disk_size_gb and not isinstance(os_disk_size_gb, int):
            raise TypeError("Expected argument 'os_disk_size_gb' to be a int")
        pulumi.set(__self__, "os_disk_size_gb", os_disk_size_gb)
        if os_disk_type and not isinstance(os_disk_type, str):
            raise TypeError("Expected argument 'os_disk_type' to be a str")
        pulumi.set(__self__, "os_disk_type", os_disk_type)
        if os_sku and not isinstance(os_sku, str):
            raise TypeError("Expected argument 'os_sku' to be a str")
        pulumi.set(__self__, "os_sku", os_sku)
        if os_type and not isinstance(os_type, str):
            raise TypeError("Expected argument 'os_type' to be a str")
        pulumi.set(__self__, "os_type", os_type)
        if pod_subnet_id and not isinstance(pod_subnet_id, str):
            raise TypeError("Expected argument 'pod_subnet_id' to be a str")
        pulumi.set(__self__, "pod_subnet_id", pod_subnet_id)
        if power_state and not isinstance(power_state, dict):
            raise TypeError("Expected argument 'power_state' to be a dict")
        pulumi.set(__self__, "power_state", power_state)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if proximity_placement_group_id and not isinstance(proximity_placement_group_id, str):
            raise TypeError("Expected argument 'proximity_placement_group_id' to be a str")
        pulumi.set(__self__, "proximity_placement_group_id", proximity_placement_group_id)
        if scale_down_mode and not isinstance(scale_down_mode, str):
            raise TypeError("Expected argument 'scale_down_mode' to be a str")
        pulumi.set(__self__, "scale_down_mode", scale_down_mode)
        if scale_set_eviction_policy and not isinstance(scale_set_eviction_policy, str):
            raise TypeError("Expected argument 'scale_set_eviction_policy' to be a str")
        pulumi.set(__self__, "scale_set_eviction_policy", scale_set_eviction_policy)
        if scale_set_priority and not isinstance(scale_set_priority, str):
            raise TypeError("Expected argument 'scale_set_priority' to be a str")
        pulumi.set(__self__, "scale_set_priority", scale_set_priority)
        if spot_max_price and not isinstance(spot_max_price, float):
            raise TypeError("Expected argument 'spot_max_price' to be a float")
        pulumi.set(__self__, "spot_max_price", spot_max_price)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if upgrade_settings and not isinstance(upgrade_settings, dict):
            raise TypeError("Expected argument 'upgrade_settings' to be a dict")
        pulumi.set(__self__, "upgrade_settings", upgrade_settings)
        if vm_size and not isinstance(vm_size, str):
            raise TypeError("Expected argument 'vm_size' to be a str")
        pulumi.set(__self__, "vm_size", vm_size)
        if vnet_subnet_id and not isinstance(vnet_subnet_id, str):
            raise TypeError("Expected argument 'vnet_subnet_id' to be a str")
        pulumi.set(__self__, "vnet_subnet_id", vnet_subnet_id)
        if workload_runtime and not isinstance(workload_runtime, str):
            raise TypeError("Expected argument 'workload_runtime' to be a str")
        pulumi.set(__self__, "workload_runtime", workload_runtime)

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[Sequence[str]]:
        """
        The list of Availability zones to use for nodes. This can only be specified if the AgentPoolType property is 'VirtualMachineScaleSets'.
        """
        return pulumi.get(self, "availability_zones")

    @property
    @pulumi.getter(name="capacityReservationGroupID")
    def capacity_reservation_group_id(self) -> Optional[str]:
        """
        AKS will associate the specified agent pool with the Capacity Reservation Group.
        """
        return pulumi.get(self, "capacity_reservation_group_id")

    @property
    @pulumi.getter
    def count(self) -> Optional[int]:
        """
        Number of agents (VMs) to host docker containers. Allowed values must be in the range of 0 to 1000 (inclusive) for user pools and in the range of 1 to 1000 (inclusive) for system pools. The default value is 1.
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> Optional['outputs.CreationDataResponse']:
        """
        CreationData to be used to specify the source Snapshot ID if the node pool will be created/upgraded using a snapshot.
        """
        return pulumi.get(self, "creation_data")

    @property
    @pulumi.getter(name="currentOrchestratorVersion")
    def current_orchestrator_version(self) -> str:
        """
        If orchestratorVersion is a fully specified version <major.minor.patch>, this field will be exactly equal to it. If orchestratorVersion is <major.minor>, this field will contain the full <major.minor.patch> version being used.
        """
        return pulumi.get(self, "current_orchestrator_version")

    @property
    @pulumi.getter(name="enableAutoScaling")
    def enable_auto_scaling(self) -> Optional[bool]:
        """
        Whether to enable auto-scaler
        """
        return pulumi.get(self, "enable_auto_scaling")

    @property
    @pulumi.getter(name="enableEncryptionAtHost")
    def enable_encryption_at_host(self) -> Optional[bool]:
        """
        This is only supported on certain VM sizes and in certain Azure regions. For more information, see: https://docs.microsoft.com/azure/aks/enable-host-encryption
        """
        return pulumi.get(self, "enable_encryption_at_host")

    @property
    @pulumi.getter(name="enableFIPS")
    def enable_fips(self) -> Optional[bool]:
        """
        See [Add a FIPS-enabled node pool](https://docs.microsoft.com/azure/aks/use-multiple-node-pools#add-a-fips-enabled-node-pool-preview) for more details.
        """
        return pulumi.get(self, "enable_fips")

    @property
    @pulumi.getter(name="enableNodePublicIP")
    def enable_node_public_ip(self) -> Optional[bool]:
        """
        Some scenarios may require nodes in a node pool to receive their own dedicated public IP addresses. A common scenario is for gaming workloads, where a console needs to make a direct connection to a cloud virtual machine to minimize hops. For more information see [assigning a public IP per node](https://docs.microsoft.com/azure/aks/use-multiple-node-pools#assign-a-public-ip-per-node-for-your-node-pools). The default is false.
        """
        return pulumi.get(self, "enable_node_public_ip")

    @property
    @pulumi.getter(name="enableUltraSSD")
    def enable_ultra_ssd(self) -> Optional[bool]:
        """
        Whether to enable UltraSSD
        """
        return pulumi.get(self, "enable_ultra_ssd")

    @property
    @pulumi.getter(name="gpuInstanceProfile")
    def gpu_instance_profile(self) -> Optional[str]:
        """
        GPUInstanceProfile to be used to specify GPU MIG instance profile for supported GPU VM SKU.
        """
        return pulumi.get(self, "gpu_instance_profile")

    @property
    @pulumi.getter(name="hostGroupID")
    def host_group_id(self) -> Optional[str]:
        """
        This is of the form: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}. For more information see [Azure dedicated hosts](https://docs.microsoft.com/azure/virtual-machines/dedicated-hosts).
        """
        return pulumi.get(self, "host_group_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="kubeletConfig")
    def kubelet_config(self) -> Optional['outputs.KubeletConfigResponse']:
        """
        The Kubelet configuration on the agent pool nodes.
        """
        return pulumi.get(self, "kubelet_config")

    @property
    @pulumi.getter(name="kubeletDiskType")
    def kubelet_disk_type(self) -> Optional[str]:
        """
        Determines the placement of emptyDir volumes, container runtime data root, and Kubelet ephemeral storage.
        """
        return pulumi.get(self, "kubelet_disk_type")

    @property
    @pulumi.getter(name="linuxOSConfig")
    def linux_os_config(self) -> Optional['outputs.LinuxOSConfigResponse']:
        """
        The OS configuration of Linux agent nodes.
        """
        return pulumi.get(self, "linux_os_config")

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
    def mode(self) -> Optional[str]:
        """
        A cluster must have at least one 'System' Agent Pool at all times. For additional information on agent pool restrictions and best practices, see: https://docs.microsoft.com/azure/aks/use-system-pools
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional['outputs.AgentPoolNetworkProfileResponse']:
        """
        Network-related settings of an agent pool.
        """
        return pulumi.get(self, "network_profile")

    @property
    @pulumi.getter(name="nodeImageVersion")
    def node_image_version(self) -> str:
        """
        The version of node image
        """
        return pulumi.get(self, "node_image_version")

    @property
    @pulumi.getter(name="nodeLabels")
    def node_labels(self) -> Optional[Mapping[str, str]]:
        """
        The node labels to be persisted across all nodes in agent pool.
        """
        return pulumi.get(self, "node_labels")

    @property
    @pulumi.getter(name="nodePublicIPPrefixID")
    def node_public_ip_prefix_id(self) -> Optional[str]:
        """
        This is of the form: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPPrefixes/{publicIPPrefixName}
        """
        return pulumi.get(self, "node_public_ip_prefix_id")

    @property
    @pulumi.getter(name="nodeTaints")
    def node_taints(self) -> Optional[Sequence[str]]:
        """
        The taints added to new nodes during node pool create and scale. For example, key=value:NoSchedule.
        """
        return pulumi.get(self, "node_taints")

    @property
    @pulumi.getter(name="orchestratorVersion")
    def orchestrator_version(self) -> Optional[str]:
        """
        Both patch version <major.minor.patch> (e.g. 1.20.13) and <major.minor> (e.g. 1.20) are supported. When <major.minor> is specified, the latest supported GA patch version is chosen automatically. Updating the cluster with the same <major.minor> once it has been created (e.g. 1.14.x -> 1.14) will not trigger an upgrade, even if a newer patch version is available. As a best practice, you should upgrade all node pools in an AKS cluster to the same Kubernetes version. The node pool version must have the same major version as the control plane. The node pool minor version must be within two minor versions of the control plane version. The node pool version cannot be greater than the control plane version. For more information see [upgrading a node pool](https://docs.microsoft.com/azure/aks/use-multiple-node-pools#upgrade-a-node-pool).
        """
        return pulumi.get(self, "orchestrator_version")

    @property
    @pulumi.getter(name="osDiskSizeGB")
    def os_disk_size_gb(self) -> Optional[int]:
        """
        OS Disk Size in GB to be used to specify the disk size for every machine in the master/agent pool. If you specify 0, it will apply the default osDisk size according to the vmSize specified.
        """
        return pulumi.get(self, "os_disk_size_gb")

    @property
    @pulumi.getter(name="osDiskType")
    def os_disk_type(self) -> Optional[str]:
        """
        The default is 'Ephemeral' if the VM supports it and has a cache disk larger than the requested OSDiskSizeGB. Otherwise, defaults to 'Managed'. May not be changed after creation. For more information see [Ephemeral OS](https://docs.microsoft.com/azure/aks/cluster-configuration#ephemeral-os).
        """
        return pulumi.get(self, "os_disk_type")

    @property
    @pulumi.getter(name="osSKU")
    def os_sku(self) -> Optional[str]:
        """
        Specifies the OS SKU used by the agent pool. The default is Ubuntu if OSType is Linux. The default is Windows2019 when Kubernetes <= 1.24 or Windows2022 when Kubernetes >= 1.25 if OSType is Windows.
        """
        return pulumi.get(self, "os_sku")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[str]:
        """
        The operating system type. The default is Linux.
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter(name="podSubnetID")
    def pod_subnet_id(self) -> Optional[str]:
        """
        If omitted, pod IPs are statically assigned on the node subnet (see vnetSubnetID for more details). This is of the form: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/subnets/{subnetName}
        """
        return pulumi.get(self, "pod_subnet_id")

    @property
    @pulumi.getter(name="powerState")
    def power_state(self) -> Optional['outputs.PowerStateResponse']:
        """
        When an Agent Pool is first created it is initially Running. The Agent Pool can be stopped by setting this field to Stopped. A stopped Agent Pool stops all of its VMs and does not accrue billing charges. An Agent Pool can only be stopped if it is Running and provisioning state is Succeeded
        """
        return pulumi.get(self, "power_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The current deployment or provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="proximityPlacementGroupID")
    def proximity_placement_group_id(self) -> Optional[str]:
        """
        The ID for Proximity Placement Group.
        """
        return pulumi.get(self, "proximity_placement_group_id")

    @property
    @pulumi.getter(name="scaleDownMode")
    def scale_down_mode(self) -> Optional[str]:
        """
        This also effects the cluster autoscaler behavior. If not specified, it defaults to Delete.
        """
        return pulumi.get(self, "scale_down_mode")

    @property
    @pulumi.getter(name="scaleSetEvictionPolicy")
    def scale_set_eviction_policy(self) -> Optional[str]:
        """
        This cannot be specified unless the scaleSetPriority is 'Spot'. If not specified, the default is 'Delete'.
        """
        return pulumi.get(self, "scale_set_eviction_policy")

    @property
    @pulumi.getter(name="scaleSetPriority")
    def scale_set_priority(self) -> Optional[str]:
        """
        The Virtual Machine Scale Set priority. If not specified, the default is 'Regular'.
        """
        return pulumi.get(self, "scale_set_priority")

    @property
    @pulumi.getter(name="spotMaxPrice")
    def spot_max_price(self) -> Optional[float]:
        """
        Possible values are any decimal value greater than zero or -1 which indicates the willingness to pay any on-demand price. For more details on spot pricing, see [spot VMs pricing](https://docs.microsoft.com/azure/virtual-machines/spot-vms#pricing)
        """
        return pulumi.get(self, "spot_max_price")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The tags to be persisted on the agent pool virtual machine scale set.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(self) -> Optional['outputs.AgentPoolUpgradeSettingsResponse']:
        """
        Settings for upgrading the agentpool
        """
        return pulumi.get(self, "upgrade_settings")

    @property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[str]:
        """
        VM size availability varies by region. If a node contains insufficient compute resources (memory, cpu, etc) pods might fail to run correctly. For more details on restricted VM sizes, see: https://docs.microsoft.com/azure/aks/quotas-skus-regions
        """
        return pulumi.get(self, "vm_size")

    @property
    @pulumi.getter(name="vnetSubnetID")
    def vnet_subnet_id(self) -> Optional[str]:
        """
        If this is not specified, a VNET and subnet will be generated and used. If no podSubnetID is specified, this applies to nodes and pods, otherwise it applies to just nodes. This is of the form: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/subnets/{subnetName}
        """
        return pulumi.get(self, "vnet_subnet_id")

    @property
    @pulumi.getter(name="workloadRuntime")
    def workload_runtime(self) -> Optional[str]:
        """
        Determines the type of workload a node can run.
        """
        return pulumi.get(self, "workload_runtime")


class AwaitableGetAgentPoolResult(GetAgentPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAgentPoolResult(
            availability_zones=self.availability_zones,
            capacity_reservation_group_id=self.capacity_reservation_group_id,
            count=self.count,
            creation_data=self.creation_data,
            current_orchestrator_version=self.current_orchestrator_version,
            enable_auto_scaling=self.enable_auto_scaling,
            enable_encryption_at_host=self.enable_encryption_at_host,
            enable_fips=self.enable_fips,
            enable_node_public_ip=self.enable_node_public_ip,
            enable_ultra_ssd=self.enable_ultra_ssd,
            gpu_instance_profile=self.gpu_instance_profile,
            host_group_id=self.host_group_id,
            id=self.id,
            kubelet_config=self.kubelet_config,
            kubelet_disk_type=self.kubelet_disk_type,
            linux_os_config=self.linux_os_config,
            max_count=self.max_count,
            max_pods=self.max_pods,
            min_count=self.min_count,
            mode=self.mode,
            name=self.name,
            network_profile=self.network_profile,
            node_image_version=self.node_image_version,
            node_labels=self.node_labels,
            node_public_ip_prefix_id=self.node_public_ip_prefix_id,
            node_taints=self.node_taints,
            orchestrator_version=self.orchestrator_version,
            os_disk_size_gb=self.os_disk_size_gb,
            os_disk_type=self.os_disk_type,
            os_sku=self.os_sku,
            os_type=self.os_type,
            pod_subnet_id=self.pod_subnet_id,
            power_state=self.power_state,
            provisioning_state=self.provisioning_state,
            proximity_placement_group_id=self.proximity_placement_group_id,
            scale_down_mode=self.scale_down_mode,
            scale_set_eviction_policy=self.scale_set_eviction_policy,
            scale_set_priority=self.scale_set_priority,
            spot_max_price=self.spot_max_price,
            tags=self.tags,
            type=self.type,
            upgrade_settings=self.upgrade_settings,
            vm_size=self.vm_size,
            vnet_subnet_id=self.vnet_subnet_id,
            workload_runtime=self.workload_runtime)


def get_agent_pool(agent_pool_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   resource_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAgentPoolResult:
    """
    Agent Pool.


    :param str agent_pool_name: The name of the agent pool.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the managed cluster resource.
    """
    __args__ = dict()
    __args__['agentPoolName'] = agent_pool_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerservice/v20240101:getAgentPool', __args__, opts=opts, typ=GetAgentPoolResult).value

    return AwaitableGetAgentPoolResult(
        availability_zones=pulumi.get(__ret__, 'availability_zones'),
        capacity_reservation_group_id=pulumi.get(__ret__, 'capacity_reservation_group_id'),
        count=pulumi.get(__ret__, 'count'),
        creation_data=pulumi.get(__ret__, 'creation_data'),
        current_orchestrator_version=pulumi.get(__ret__, 'current_orchestrator_version'),
        enable_auto_scaling=pulumi.get(__ret__, 'enable_auto_scaling'),
        enable_encryption_at_host=pulumi.get(__ret__, 'enable_encryption_at_host'),
        enable_fips=pulumi.get(__ret__, 'enable_fips'),
        enable_node_public_ip=pulumi.get(__ret__, 'enable_node_public_ip'),
        enable_ultra_ssd=pulumi.get(__ret__, 'enable_ultra_ssd'),
        gpu_instance_profile=pulumi.get(__ret__, 'gpu_instance_profile'),
        host_group_id=pulumi.get(__ret__, 'host_group_id'),
        id=pulumi.get(__ret__, 'id'),
        kubelet_config=pulumi.get(__ret__, 'kubelet_config'),
        kubelet_disk_type=pulumi.get(__ret__, 'kubelet_disk_type'),
        linux_os_config=pulumi.get(__ret__, 'linux_os_config'),
        max_count=pulumi.get(__ret__, 'max_count'),
        max_pods=pulumi.get(__ret__, 'max_pods'),
        min_count=pulumi.get(__ret__, 'min_count'),
        mode=pulumi.get(__ret__, 'mode'),
        name=pulumi.get(__ret__, 'name'),
        network_profile=pulumi.get(__ret__, 'network_profile'),
        node_image_version=pulumi.get(__ret__, 'node_image_version'),
        node_labels=pulumi.get(__ret__, 'node_labels'),
        node_public_ip_prefix_id=pulumi.get(__ret__, 'node_public_ip_prefix_id'),
        node_taints=pulumi.get(__ret__, 'node_taints'),
        orchestrator_version=pulumi.get(__ret__, 'orchestrator_version'),
        os_disk_size_gb=pulumi.get(__ret__, 'os_disk_size_gb'),
        os_disk_type=pulumi.get(__ret__, 'os_disk_type'),
        os_sku=pulumi.get(__ret__, 'os_sku'),
        os_type=pulumi.get(__ret__, 'os_type'),
        pod_subnet_id=pulumi.get(__ret__, 'pod_subnet_id'),
        power_state=pulumi.get(__ret__, 'power_state'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        proximity_placement_group_id=pulumi.get(__ret__, 'proximity_placement_group_id'),
        scale_down_mode=pulumi.get(__ret__, 'scale_down_mode'),
        scale_set_eviction_policy=pulumi.get(__ret__, 'scale_set_eviction_policy'),
        scale_set_priority=pulumi.get(__ret__, 'scale_set_priority'),
        spot_max_price=pulumi.get(__ret__, 'spot_max_price'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        upgrade_settings=pulumi.get(__ret__, 'upgrade_settings'),
        vm_size=pulumi.get(__ret__, 'vm_size'),
        vnet_subnet_id=pulumi.get(__ret__, 'vnet_subnet_id'),
        workload_runtime=pulumi.get(__ret__, 'workload_runtime'))


@_utilities.lift_output_func(get_agent_pool)
def get_agent_pool_output(agent_pool_name: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          resource_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAgentPoolResult]:
    """
    Agent Pool.


    :param str agent_pool_name: The name of the agent pool.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the managed cluster resource.
    """
    ...
