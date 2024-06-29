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
    'GetSnapshotPolicyResult',
    'AwaitableGetSnapshotPolicyResult',
    'get_snapshot_policy',
    'get_snapshot_policy_output',
]

@pulumi.output_type
class GetSnapshotPolicyResult:
    """
    Snapshot policy information
    """
    def __init__(__self__, daily_schedule=None, enabled=None, etag=None, hourly_schedule=None, id=None, location=None, monthly_schedule=None, name=None, provisioning_state=None, system_data=None, tags=None, type=None, weekly_schedule=None):
        if daily_schedule and not isinstance(daily_schedule, dict):
            raise TypeError("Expected argument 'daily_schedule' to be a dict")
        pulumi.set(__self__, "daily_schedule", daily_schedule)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if hourly_schedule and not isinstance(hourly_schedule, dict):
            raise TypeError("Expected argument 'hourly_schedule' to be a dict")
        pulumi.set(__self__, "hourly_schedule", hourly_schedule)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if monthly_schedule and not isinstance(monthly_schedule, dict):
            raise TypeError("Expected argument 'monthly_schedule' to be a dict")
        pulumi.set(__self__, "monthly_schedule", monthly_schedule)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
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
        if weekly_schedule and not isinstance(weekly_schedule, dict):
            raise TypeError("Expected argument 'weekly_schedule' to be a dict")
        pulumi.set(__self__, "weekly_schedule", weekly_schedule)

    @property
    @pulumi.getter(name="dailySchedule")
    def daily_schedule(self) -> Optional['outputs.DailyScheduleResponse']:
        """
        Schedule for daily snapshots
        """
        return pulumi.get(self, "daily_schedule")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        The property to decide policy is enabled or not
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="hourlySchedule")
    def hourly_schedule(self) -> Optional['outputs.HourlyScheduleResponse']:
        """
        Schedule for hourly snapshots
        """
        return pulumi.get(self, "hourly_schedule")

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
    @pulumi.getter(name="monthlySchedule")
    def monthly_schedule(self) -> Optional['outputs.MonthlyScheduleResponse']:
        """
        Schedule for monthly snapshots
        """
        return pulumi.get(self, "monthly_schedule")

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
        Azure lifecycle management
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

    @property
    @pulumi.getter(name="weeklySchedule")
    def weekly_schedule(self) -> Optional['outputs.WeeklyScheduleResponse']:
        """
        Schedule for weekly snapshots
        """
        return pulumi.get(self, "weekly_schedule")


class AwaitableGetSnapshotPolicyResult(GetSnapshotPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSnapshotPolicyResult(
            daily_schedule=self.daily_schedule,
            enabled=self.enabled,
            etag=self.etag,
            hourly_schedule=self.hourly_schedule,
            id=self.id,
            location=self.location,
            monthly_schedule=self.monthly_schedule,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            weekly_schedule=self.weekly_schedule)


def get_snapshot_policy(account_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        snapshot_policy_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSnapshotPolicyResult:
    """
    Get a snapshot Policy


    :param str account_name: The name of the NetApp account
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str snapshot_policy_name: The name of the snapshot policy
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['snapshotPolicyName'] = snapshot_policy_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:netapp/v20231101:getSnapshotPolicy', __args__, opts=opts, typ=GetSnapshotPolicyResult).value

    return AwaitableGetSnapshotPolicyResult(
        daily_schedule=pulumi.get(__ret__, 'daily_schedule'),
        enabled=pulumi.get(__ret__, 'enabled'),
        etag=pulumi.get(__ret__, 'etag'),
        hourly_schedule=pulumi.get(__ret__, 'hourly_schedule'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        monthly_schedule=pulumi.get(__ret__, 'monthly_schedule'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        weekly_schedule=pulumi.get(__ret__, 'weekly_schedule'))


@_utilities.lift_output_func(get_snapshot_policy)
def get_snapshot_policy_output(account_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               snapshot_policy_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSnapshotPolicyResult]:
    """
    Get a snapshot Policy


    :param str account_name: The name of the NetApp account
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str snapshot_policy_name: The name of the snapshot policy
    """
    ...
