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
    'GetManagedNetworkPeeringPolicyResult',
    'AwaitableGetManagedNetworkPeeringPolicyResult',
    'get_managed_network_peering_policy',
    'get_managed_network_peering_policy_output',
]

@pulumi.output_type
class GetManagedNetworkPeeringPolicyResult:
    """
    The Managed Network Peering Policy resource
    """
    def __init__(__self__, id=None, location=None, name=None, properties=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
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
    @pulumi.getter
    def properties(self) -> 'outputs.ManagedNetworkPeeringPolicyPropertiesResponse':
        """
        Gets or sets the properties of a Managed Network Policy
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
        """
        return pulumi.get(self, "type")


class AwaitableGetManagedNetworkPeeringPolicyResult(GetManagedNetworkPeeringPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedNetworkPeeringPolicyResult(
            id=self.id,
            location=self.location,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_managed_network_peering_policy(managed_network_name: Optional[str] = None,
                                       managed_network_peering_policy_name: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedNetworkPeeringPolicyResult:
    """
    The Get ManagedNetworkPeeringPolicies operation gets a Managed Network Peering Policy resource, specified by the  resource group, Managed Network name, and peering policy name


    :param str managed_network_name: The name of the Managed Network.
    :param str managed_network_peering_policy_name: The name of the Managed Network Peering Policy.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['managedNetworkName'] = managed_network_name
    __args__['managedNetworkPeeringPolicyName'] = managed_network_peering_policy_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:managednetwork/v20190601preview:getManagedNetworkPeeringPolicy', __args__, opts=opts, typ=GetManagedNetworkPeeringPolicyResult).value

    return AwaitableGetManagedNetworkPeeringPolicyResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_managed_network_peering_policy)
def get_managed_network_peering_policy_output(managed_network_name: Optional[pulumi.Input[str]] = None,
                                              managed_network_peering_policy_name: Optional[pulumi.Input[str]] = None,
                                              resource_group_name: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedNetworkPeeringPolicyResult]:
    """
    The Get ManagedNetworkPeeringPolicies operation gets a Managed Network Peering Policy resource, specified by the  resource group, Managed Network name, and peering policy name


    :param str managed_network_name: The name of the Managed Network.
    :param str managed_network_peering_policy_name: The name of the Managed Network Peering Policy.
    :param str resource_group_name: The name of the resource group.
    """
    ...
