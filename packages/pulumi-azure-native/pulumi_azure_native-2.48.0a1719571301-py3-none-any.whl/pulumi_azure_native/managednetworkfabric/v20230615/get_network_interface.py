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
    'GetNetworkInterfaceResult',
    'AwaitableGetNetworkInterfaceResult',
    'get_network_interface',
    'get_network_interface_output',
]

@pulumi.output_type
class GetNetworkInterfaceResult:
    """
    Defines the NetworkInterface resource.
    """
    def __init__(__self__, administrative_state=None, annotation=None, connected_to=None, id=None, interface_type=None, ipv4_address=None, ipv6_address=None, name=None, physical_identifier=None, provisioning_state=None, system_data=None, type=None):
        if administrative_state and not isinstance(administrative_state, str):
            raise TypeError("Expected argument 'administrative_state' to be a str")
        pulumi.set(__self__, "administrative_state", administrative_state)
        if annotation and not isinstance(annotation, str):
            raise TypeError("Expected argument 'annotation' to be a str")
        pulumi.set(__self__, "annotation", annotation)
        if connected_to and not isinstance(connected_to, str):
            raise TypeError("Expected argument 'connected_to' to be a str")
        pulumi.set(__self__, "connected_to", connected_to)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if interface_type and not isinstance(interface_type, str):
            raise TypeError("Expected argument 'interface_type' to be a str")
        pulumi.set(__self__, "interface_type", interface_type)
        if ipv4_address and not isinstance(ipv4_address, str):
            raise TypeError("Expected argument 'ipv4_address' to be a str")
        pulumi.set(__self__, "ipv4_address", ipv4_address)
        if ipv6_address and not isinstance(ipv6_address, str):
            raise TypeError("Expected argument 'ipv6_address' to be a str")
        pulumi.set(__self__, "ipv6_address", ipv6_address)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if physical_identifier and not isinstance(physical_identifier, str):
            raise TypeError("Expected argument 'physical_identifier' to be a str")
        pulumi.set(__self__, "physical_identifier", physical_identifier)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> str:
        """
        Administrative state of the resource.
        """
        return pulumi.get(self, "administrative_state")

    @property
    @pulumi.getter
    def annotation(self) -> Optional[str]:
        """
        Switch configuration description.
        """
        return pulumi.get(self, "annotation")

    @property
    @pulumi.getter(name="connectedTo")
    def connected_to(self) -> str:
        """
        The ARM resource id of the interface or compute server its connected to.
        """
        return pulumi.get(self, "connected_to")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="interfaceType")
    def interface_type(self) -> str:
        """
        The Interface Type. Example: Management/Data
        """
        return pulumi.get(self, "interface_type")

    @property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> str:
        """
        IPv4Address of the interface.
        """
        return pulumi.get(self, "ipv4_address")

    @property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> str:
        """
        IPv6Address of the interface.
        """
        return pulumi.get(self, "ipv6_address")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="physicalIdentifier")
    def physical_identifier(self) -> str:
        """
        Physical Identifier of the network interface.
        """
        return pulumi.get(self, "physical_identifier")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the resource.
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
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetNetworkInterfaceResult(GetNetworkInterfaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkInterfaceResult(
            administrative_state=self.administrative_state,
            annotation=self.annotation,
            connected_to=self.connected_to,
            id=self.id,
            interface_type=self.interface_type,
            ipv4_address=self.ipv4_address,
            ipv6_address=self.ipv6_address,
            name=self.name,
            physical_identifier=self.physical_identifier,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_network_interface(network_device_name: Optional[str] = None,
                          network_interface_name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkInterfaceResult:
    """
    Get the Network Interface resource details.


    :param str network_device_name: Name of the Network Device.
    :param str network_interface_name: Name of the Network Interface.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['networkDeviceName'] = network_device_name
    __args__['networkInterfaceName'] = network_interface_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:managednetworkfabric/v20230615:getNetworkInterface', __args__, opts=opts, typ=GetNetworkInterfaceResult).value

    return AwaitableGetNetworkInterfaceResult(
        administrative_state=pulumi.get(__ret__, 'administrative_state'),
        annotation=pulumi.get(__ret__, 'annotation'),
        connected_to=pulumi.get(__ret__, 'connected_to'),
        id=pulumi.get(__ret__, 'id'),
        interface_type=pulumi.get(__ret__, 'interface_type'),
        ipv4_address=pulumi.get(__ret__, 'ipv4_address'),
        ipv6_address=pulumi.get(__ret__, 'ipv6_address'),
        name=pulumi.get(__ret__, 'name'),
        physical_identifier=pulumi.get(__ret__, 'physical_identifier'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_network_interface)
def get_network_interface_output(network_device_name: Optional[pulumi.Input[str]] = None,
                                 network_interface_name: Optional[pulumi.Input[str]] = None,
                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkInterfaceResult]:
    """
    Get the Network Interface resource details.


    :param str network_device_name: Name of the Network Device.
    :param str network_interface_name: Name of the Network Interface.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
