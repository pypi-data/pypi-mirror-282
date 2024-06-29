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
    'GetCapacityReservationGroupResult',
    'AwaitableGetCapacityReservationGroupResult',
    'get_capacity_reservation_group',
    'get_capacity_reservation_group_output',
]

@pulumi.output_type
class GetCapacityReservationGroupResult:
    """
    Specifies information about the capacity reservation group that the capacity reservations should be assigned to. Currently, a capacity reservation can only be added to a capacity reservation group at creation time. An existing capacity reservation cannot be added or moved to another capacity reservation group.
    """
    def __init__(__self__, capacity_reservations=None, id=None, instance_view=None, location=None, name=None, sharing_profile=None, tags=None, type=None, virtual_machines_associated=None, zones=None):
        if capacity_reservations and not isinstance(capacity_reservations, list):
            raise TypeError("Expected argument 'capacity_reservations' to be a list")
        pulumi.set(__self__, "capacity_reservations", capacity_reservations)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_view and not isinstance(instance_view, dict):
            raise TypeError("Expected argument 'instance_view' to be a dict")
        pulumi.set(__self__, "instance_view", instance_view)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if sharing_profile and not isinstance(sharing_profile, dict):
            raise TypeError("Expected argument 'sharing_profile' to be a dict")
        pulumi.set(__self__, "sharing_profile", sharing_profile)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_machines_associated and not isinstance(virtual_machines_associated, list):
            raise TypeError("Expected argument 'virtual_machines_associated' to be a list")
        pulumi.set(__self__, "virtual_machines_associated", virtual_machines_associated)
        if zones and not isinstance(zones, list):
            raise TypeError("Expected argument 'zones' to be a list")
        pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter(name="capacityReservations")
    def capacity_reservations(self) -> Sequence['outputs.SubResourceReadOnlyResponse']:
        """
        A list of all capacity reservation resource ids that belong to capacity reservation group.
        """
        return pulumi.get(self, "capacity_reservations")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> 'outputs.CapacityReservationGroupInstanceViewResponse':
        """
        The capacity reservation group instance view which has the list of instance views for all the capacity reservations that belong to the capacity reservation group.
        """
        return pulumi.get(self, "instance_view")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sharingProfile")
    def sharing_profile(self) -> Optional['outputs.ResourceSharingProfileResponse']:
        """
        Specifies the settings to enable sharing across subscriptions for the capacity reservation group resource. Pls. keep in mind the capacity reservation group resource generally can be shared across subscriptions belonging to a single azure AAD tenant or cross AAD tenant if there is a trust relationship established between the AAD tenants. **Note:** Minimum api-version: 2023-09-01. Please refer to https://aka.ms/computereservationsharing for more details.
        """
        return pulumi.get(self, "sharing_profile")

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
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualMachinesAssociated")
    def virtual_machines_associated(self) -> Sequence['outputs.SubResourceReadOnlyResponse']:
        """
        A list of references to all virtual machines associated to the capacity reservation group.
        """
        return pulumi.get(self, "virtual_machines_associated")

    @property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[str]]:
        """
        Availability Zones to use for this capacity reservation group. The zones can be assigned only during creation. If not provided, the group supports only regional resources in the region. If provided, enforces each capacity reservation in the group to be in one of the zones.
        """
        return pulumi.get(self, "zones")


class AwaitableGetCapacityReservationGroupResult(GetCapacityReservationGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCapacityReservationGroupResult(
            capacity_reservations=self.capacity_reservations,
            id=self.id,
            instance_view=self.instance_view,
            location=self.location,
            name=self.name,
            sharing_profile=self.sharing_profile,
            tags=self.tags,
            type=self.type,
            virtual_machines_associated=self.virtual_machines_associated,
            zones=self.zones)


def get_capacity_reservation_group(capacity_reservation_group_name: Optional[str] = None,
                                   expand: Optional[str] = None,
                                   resource_group_name: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCapacityReservationGroupResult:
    """
    The operation that retrieves information about a capacity reservation group.


    :param str capacity_reservation_group_name: The name of the capacity reservation group.
    :param str expand: The expand expression to apply on the operation. 'InstanceView' will retrieve the list of instance views of the capacity reservations under the capacity reservation group which is a snapshot of the runtime properties of a capacity reservation that is managed by the platform and can change outside of control plane operations.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['capacityReservationGroupName'] = capacity_reservation_group_name
    __args__['expand'] = expand
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:compute/v20230901:getCapacityReservationGroup', __args__, opts=opts, typ=GetCapacityReservationGroupResult).value

    return AwaitableGetCapacityReservationGroupResult(
        capacity_reservations=pulumi.get(__ret__, 'capacity_reservations'),
        id=pulumi.get(__ret__, 'id'),
        instance_view=pulumi.get(__ret__, 'instance_view'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        sharing_profile=pulumi.get(__ret__, 'sharing_profile'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        virtual_machines_associated=pulumi.get(__ret__, 'virtual_machines_associated'),
        zones=pulumi.get(__ret__, 'zones'))


@_utilities.lift_output_func(get_capacity_reservation_group)
def get_capacity_reservation_group_output(capacity_reservation_group_name: Optional[pulumi.Input[str]] = None,
                                          expand: Optional[pulumi.Input[Optional[str]]] = None,
                                          resource_group_name: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCapacityReservationGroupResult]:
    """
    The operation that retrieves information about a capacity reservation group.


    :param str capacity_reservation_group_name: The name of the capacity reservation group.
    :param str expand: The expand expression to apply on the operation. 'InstanceView' will retrieve the list of instance views of the capacity reservations under the capacity reservation group which is a snapshot of the runtime properties of a capacity reservation that is managed by the platform and can change outside of control plane operations.
    :param str resource_group_name: The name of the resource group.
    """
    ...
