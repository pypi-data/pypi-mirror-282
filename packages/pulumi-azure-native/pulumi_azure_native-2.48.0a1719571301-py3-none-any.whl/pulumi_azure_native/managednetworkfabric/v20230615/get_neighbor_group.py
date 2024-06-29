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
    'GetNeighborGroupResult',
    'AwaitableGetNeighborGroupResult',
    'get_neighbor_group',
    'get_neighbor_group_output',
]

@pulumi.output_type
class GetNeighborGroupResult:
    """
    Defines the Neighbor Group.
    """
    def __init__(__self__, annotation=None, destination=None, id=None, location=None, name=None, network_tap_ids=None, network_tap_rule_ids=None, provisioning_state=None, system_data=None, tags=None, type=None):
        if annotation and not isinstance(annotation, str):
            raise TypeError("Expected argument 'annotation' to be a str")
        pulumi.set(__self__, "annotation", annotation)
        if destination and not isinstance(destination, dict):
            raise TypeError("Expected argument 'destination' to be a dict")
        pulumi.set(__self__, "destination", destination)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_tap_ids and not isinstance(network_tap_ids, list):
            raise TypeError("Expected argument 'network_tap_ids' to be a list")
        pulumi.set(__self__, "network_tap_ids", network_tap_ids)
        if network_tap_rule_ids and not isinstance(network_tap_rule_ids, list):
            raise TypeError("Expected argument 'network_tap_rule_ids' to be a list")
        pulumi.set(__self__, "network_tap_rule_ids", network_tap_rule_ids)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
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
    @pulumi.getter
    def annotation(self) -> Optional[str]:
        """
        Switch configuration description.
        """
        return pulumi.get(self, "annotation")

    @property
    @pulumi.getter
    def destination(self) -> 'outputs.NeighborGroupDestinationResponse':
        """
        An array of destination IPv4 Addresses or IPv6 Addresses.
        """
        return pulumi.get(self, "destination")

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
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkTapIds")
    def network_tap_ids(self) -> Sequence[str]:
        """
        List of NetworkTap IDs where neighbor group is associated.
        """
        return pulumi.get(self, "network_tap_ids")

    @property
    @pulumi.getter(name="networkTapRuleIds")
    def network_tap_rule_ids(self) -> Sequence[str]:
        """
        List of Network Tap Rule IDs where neighbor group is associated.
        """
        return pulumi.get(self, "network_tap_rule_ids")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the resource.
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
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetNeighborGroupResult(GetNeighborGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNeighborGroupResult(
            annotation=self.annotation,
            destination=self.destination,
            id=self.id,
            location=self.location,
            name=self.name,
            network_tap_ids=self.network_tap_ids,
            network_tap_rule_ids=self.network_tap_rule_ids,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_neighbor_group(neighbor_group_name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNeighborGroupResult:
    """
    Gets the Neighbor Group.


    :param str neighbor_group_name: Name of the Neighbor Group.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['neighborGroupName'] = neighbor_group_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:managednetworkfabric/v20230615:getNeighborGroup', __args__, opts=opts, typ=GetNeighborGroupResult).value

    return AwaitableGetNeighborGroupResult(
        annotation=pulumi.get(__ret__, 'annotation'),
        destination=pulumi.get(__ret__, 'destination'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        network_tap_ids=pulumi.get(__ret__, 'network_tap_ids'),
        network_tap_rule_ids=pulumi.get(__ret__, 'network_tap_rule_ids'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_neighbor_group)
def get_neighbor_group_output(neighbor_group_name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNeighborGroupResult]:
    """
    Gets the Neighbor Group.


    :param str neighbor_group_name: Name of the Neighbor Group.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
