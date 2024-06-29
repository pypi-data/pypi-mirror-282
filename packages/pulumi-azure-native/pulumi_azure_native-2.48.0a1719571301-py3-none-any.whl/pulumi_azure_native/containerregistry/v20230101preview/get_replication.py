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
    'GetReplicationResult',
    'AwaitableGetReplicationResult',
    'get_replication',
    'get_replication_output',
]

@pulumi.output_type
class GetReplicationResult:
    """
    An object that represents a replication for a container registry.
    """
    def __init__(__self__, id=None, location=None, name=None, provisioning_state=None, region_endpoint_enabled=None, status=None, system_data=None, tags=None, type=None, zone_redundancy=None):
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
        if region_endpoint_enabled and not isinstance(region_endpoint_enabled, bool):
            raise TypeError("Expected argument 'region_endpoint_enabled' to be a bool")
        pulumi.set(__self__, "region_endpoint_enabled", region_endpoint_enabled)
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
        if zone_redundancy and not isinstance(zone_redundancy, str):
            raise TypeError("Expected argument 'zone_redundancy' to be a str")
        pulumi.set(__self__, "zone_redundancy", zone_redundancy)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The location of the resource. This cannot be changed after the resource is created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the replication at the time the operation was called.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="regionEndpointEnabled")
    def region_endpoint_enabled(self) -> Optional[bool]:
        """
        Specifies whether the replication's regional endpoint is enabled. Requests will not be routed to a replication whose regional endpoint is disabled, however its data will continue to be synced with other replications.
        """
        return pulumi.get(self, "region_endpoint_enabled")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.StatusResponse':
        """
        The status of the replication at the time the operation was called.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="zoneRedundancy")
    def zone_redundancy(self) -> Optional[str]:
        """
        Whether or not zone redundancy is enabled for this container registry replication
        """
        return pulumi.get(self, "zone_redundancy")


class AwaitableGetReplicationResult(GetReplicationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReplicationResult(
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            region_endpoint_enabled=self.region_endpoint_enabled,
            status=self.status,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            zone_redundancy=self.zone_redundancy)


def get_replication(registry_name: Optional[str] = None,
                    replication_name: Optional[str] = None,
                    resource_group_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReplicationResult:
    """
    Gets the properties of the specified replication.


    :param str registry_name: The name of the container registry.
    :param str replication_name: The name of the replication.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['registryName'] = registry_name
    __args__['replicationName'] = replication_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerregistry/v20230101preview:getReplication', __args__, opts=opts, typ=GetReplicationResult).value

    return AwaitableGetReplicationResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        region_endpoint_enabled=pulumi.get(__ret__, 'region_endpoint_enabled'),
        status=pulumi.get(__ret__, 'status'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        zone_redundancy=pulumi.get(__ret__, 'zone_redundancy'))


@_utilities.lift_output_func(get_replication)
def get_replication_output(registry_name: Optional[pulumi.Input[str]] = None,
                           replication_name: Optional[pulumi.Input[str]] = None,
                           resource_group_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReplicationResult]:
    """
    Gets the properties of the specified replication.


    :param str registry_name: The name of the container registry.
    :param str replication_name: The name of the replication.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
