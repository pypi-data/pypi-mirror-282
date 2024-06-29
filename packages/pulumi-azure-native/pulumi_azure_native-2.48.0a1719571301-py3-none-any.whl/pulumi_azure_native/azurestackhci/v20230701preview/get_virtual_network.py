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
    'GetVirtualNetworkResult',
    'AwaitableGetVirtualNetworkResult',
    'get_virtual_network',
    'get_virtual_network_output',
]

@pulumi.output_type
class GetVirtualNetworkResult:
    """
    The virtual network resource definition.
    """
    def __init__(__self__, dhcp_options=None, extended_location=None, id=None, location=None, name=None, network_type=None, provisioning_state=None, status=None, subnets=None, system_data=None, tags=None, type=None, vm_switch_name=None):
        if dhcp_options and not isinstance(dhcp_options, dict):
            raise TypeError("Expected argument 'dhcp_options' to be a dict")
        pulumi.set(__self__, "dhcp_options", dhcp_options)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_type and not isinstance(network_type, str):
            raise TypeError("Expected argument 'network_type' to be a str")
        pulumi.set(__self__, "network_type", network_type)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if status and not isinstance(status, dict):
            raise TypeError("Expected argument 'status' to be a dict")
        pulumi.set(__self__, "status", status)
        if subnets and not isinstance(subnets, list):
            raise TypeError("Expected argument 'subnets' to be a list")
        pulumi.set(__self__, "subnets", subnets)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if vm_switch_name and not isinstance(vm_switch_name, str):
            raise TypeError("Expected argument 'vm_switch_name' to be a str")
        pulumi.set(__self__, "vm_switch_name", vm_switch_name)

    @property
    @pulumi.getter(name="dhcpOptions")
    def dhcp_options(self) -> Optional['outputs.VirtualNetworkPropertiesResponseDhcpOptions']:
        """
        DhcpOptions contains an array of DNS servers available to VMs deployed in the virtual network. Standard DHCP option for a subnet overrides VNET DHCP options.
        """
        return pulumi.get(self, "dhcp_options")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional['outputs.ExtendedLocationResponse']:
        """
        The extendedLocation of the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
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
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[str]:
        """
        Type of the network
        """
        return pulumi.get(self, "network_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the virtual network.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.VirtualNetworkStatusResponse':
        """
        The observed state of virtual networks
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def subnets(self) -> Optional[Sequence['outputs.VirtualNetworkPropertiesResponseSubnets']]:
        """
        Subnet - list of subnets under the virtual network
        """
        return pulumi.get(self, "subnets")

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

    @property
    @pulumi.getter(name="vmSwitchName")
    def vm_switch_name(self) -> Optional[str]:
        """
        name of the network switch to be used for VMs
        """
        return pulumi.get(self, "vm_switch_name")


class AwaitableGetVirtualNetworkResult(GetVirtualNetworkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualNetworkResult(
            dhcp_options=self.dhcp_options,
            extended_location=self.extended_location,
            id=self.id,
            location=self.location,
            name=self.name,
            network_type=self.network_type,
            provisioning_state=self.provisioning_state,
            status=self.status,
            subnets=self.subnets,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            vm_switch_name=self.vm_switch_name)


def get_virtual_network(resource_group_name: Optional[str] = None,
                        virtual_network_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualNetworkResult:
    """
    The virtual network resource definition.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str virtual_network_name: Name of the virtual network
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['virtualNetworkName'] = virtual_network_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azurestackhci/v20230701preview:getVirtualNetwork', __args__, opts=opts, typ=GetVirtualNetworkResult).value

    return AwaitableGetVirtualNetworkResult(
        dhcp_options=pulumi.get(__ret__, 'dhcp_options'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        network_type=pulumi.get(__ret__, 'network_type'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        status=pulumi.get(__ret__, 'status'),
        subnets=pulumi.get(__ret__, 'subnets'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        vm_switch_name=pulumi.get(__ret__, 'vm_switch_name'))


@_utilities.lift_output_func(get_virtual_network)
def get_virtual_network_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                               virtual_network_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualNetworkResult]:
    """
    The virtual network resource definition.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str virtual_network_name: Name of the virtual network
    """
    ...
