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
    'GetDiskPoolResult',
    'AwaitableGetDiskPoolResult',
    'get_disk_pool',
    'get_disk_pool_output',
]

@pulumi.output_type
class GetDiskPoolResult:
    """
    Response for Disk pool request.
    """
    def __init__(__self__, additional_capabilities=None, availability_zones=None, disks=None, id=None, location=None, name=None, provisioning_state=None, status=None, subnet_id=None, system_data=None, tags=None, tier=None, type=None):
        if additional_capabilities and not isinstance(additional_capabilities, list):
            raise TypeError("Expected argument 'additional_capabilities' to be a list")
        pulumi.set(__self__, "additional_capabilities", additional_capabilities)
        if availability_zones and not isinstance(availability_zones, list):
            raise TypeError("Expected argument 'availability_zones' to be a list")
        pulumi.set(__self__, "availability_zones", availability_zones)
        if disks and not isinstance(disks, list):
            raise TypeError("Expected argument 'disks' to be a list")
        pulumi.set(__self__, "disks", disks)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if tier and not isinstance(tier, str):
            raise TypeError("Expected argument 'tier' to be a str")
        pulumi.set(__self__, "tier", tier)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="additionalCapabilities")
    def additional_capabilities(self) -> Optional[Sequence[str]]:
        """
        List of additional capabilities for Disk pool.
        """
        return pulumi.get(self, "additional_capabilities")

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Sequence[str]:
        """
        Logical zone for Disk pool resource; example: ["1"].
        """
        return pulumi.get(self, "availability_zones")

    @property
    @pulumi.getter
    def disks(self) -> Optional[Sequence['outputs.DiskResponse']]:
        """
        List of Azure Managed Disks to attach to a Disk pool. Can attach 8 disks at most.
        """
        return pulumi.get(self, "disks")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives.
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        State of the operation on the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Operational status of the Disk pool.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        Azure Resource ID of a Subnet for the Disk pool.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemMetadataResponse':
        """
        Resource metadata required by ARM RPC
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
    def tier(self) -> str:
        """
        Determines the SKU of VM deployed for Disk pool
        """
        return pulumi.get(self, "tier")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
        """
        return pulumi.get(self, "type")


class AwaitableGetDiskPoolResult(GetDiskPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDiskPoolResult(
            additional_capabilities=self.additional_capabilities,
            availability_zones=self.availability_zones,
            disks=self.disks,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            status=self.status,
            subnet_id=self.subnet_id,
            system_data=self.system_data,
            tags=self.tags,
            tier=self.tier,
            type=self.type)


def get_disk_pool(disk_pool_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDiskPoolResult:
    """
    Get a Disk pool.


    :param str disk_pool_name: The name of the Disk pool.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['diskPoolName'] = disk_pool_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:storagepool/v20200315preview:getDiskPool', __args__, opts=opts, typ=GetDiskPoolResult).value

    return AwaitableGetDiskPoolResult(
        additional_capabilities=pulumi.get(__ret__, 'additional_capabilities'),
        availability_zones=pulumi.get(__ret__, 'availability_zones'),
        disks=pulumi.get(__ret__, 'disks'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        status=pulumi.get(__ret__, 'status'),
        subnet_id=pulumi.get(__ret__, 'subnet_id'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        tier=pulumi.get(__ret__, 'tier'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_disk_pool)
def get_disk_pool_output(disk_pool_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDiskPoolResult]:
    """
    Get a Disk pool.


    :param str disk_pool_name: The name of the Disk pool.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
