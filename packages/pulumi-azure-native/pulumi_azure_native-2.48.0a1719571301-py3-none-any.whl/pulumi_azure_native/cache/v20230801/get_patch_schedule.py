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
    'GetPatchScheduleResult',
    'AwaitableGetPatchScheduleResult',
    'get_patch_schedule',
    'get_patch_schedule_output',
]

@pulumi.output_type
class GetPatchScheduleResult:
    """
    Response to put/get patch schedules for Redis cache.
    """
    def __init__(__self__, id=None, location=None, name=None, schedule_entries=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if schedule_entries and not isinstance(schedule_entries, list):
            raise TypeError("Expected argument 'schedule_entries' to be a list")
        pulumi.set(__self__, "schedule_entries", schedule_entries)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

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
    @pulumi.getter(name="scheduleEntries")
    def schedule_entries(self) -> Sequence['outputs.ScheduleEntryResponse']:
        """
        List of patch schedules for a Redis cache.
        """
        return pulumi.get(self, "schedule_entries")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetPatchScheduleResult(GetPatchScheduleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPatchScheduleResult(
            id=self.id,
            location=self.location,
            name=self.name,
            schedule_entries=self.schedule_entries,
            type=self.type)


def get_patch_schedule(default: Optional[str] = None,
                       name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPatchScheduleResult:
    """
    Gets the patching schedule of a redis cache.


    :param str default: Default string modeled as parameter for auto generation to work correctly.
    :param str name: The name of the redis cache.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['default'] = default
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cache/v20230801:getPatchSchedule', __args__, opts=opts, typ=GetPatchScheduleResult).value

    return AwaitableGetPatchScheduleResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        schedule_entries=pulumi.get(__ret__, 'schedule_entries'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_patch_schedule)
def get_patch_schedule_output(default: Optional[pulumi.Input[str]] = None,
                              name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPatchScheduleResult]:
    """
    Gets the patching schedule of a redis cache.


    :param str default: Default string modeled as parameter for auto generation to work correctly.
    :param str name: The name of the redis cache.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
