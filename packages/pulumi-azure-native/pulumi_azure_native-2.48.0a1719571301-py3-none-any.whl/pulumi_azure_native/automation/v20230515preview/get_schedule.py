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
    'GetScheduleResult',
    'AwaitableGetScheduleResult',
    'get_schedule',
    'get_schedule_output',
]

@pulumi.output_type
class GetScheduleResult:
    """
    Definition of the schedule.
    """
    def __init__(__self__, advanced_schedule=None, creation_time=None, description=None, expiry_time=None, expiry_time_offset_minutes=None, frequency=None, id=None, interval=None, is_enabled=None, last_modified_time=None, name=None, next_run=None, next_run_offset_minutes=None, start_time=None, start_time_offset_minutes=None, system_data=None, time_zone=None, type=None):
        if advanced_schedule and not isinstance(advanced_schedule, dict):
            raise TypeError("Expected argument 'advanced_schedule' to be a dict")
        pulumi.set(__self__, "advanced_schedule", advanced_schedule)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if expiry_time and not isinstance(expiry_time, str):
            raise TypeError("Expected argument 'expiry_time' to be a str")
        pulumi.set(__self__, "expiry_time", expiry_time)
        if expiry_time_offset_minutes and not isinstance(expiry_time_offset_minutes, float):
            raise TypeError("Expected argument 'expiry_time_offset_minutes' to be a float")
        pulumi.set(__self__, "expiry_time_offset_minutes", expiry_time_offset_minutes)
        if frequency and not isinstance(frequency, str):
            raise TypeError("Expected argument 'frequency' to be a str")
        pulumi.set(__self__, "frequency", frequency)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if interval and not isinstance(interval, dict):
            raise TypeError("Expected argument 'interval' to be a dict")
        pulumi.set(__self__, "interval", interval)
        if is_enabled and not isinstance(is_enabled, bool):
            raise TypeError("Expected argument 'is_enabled' to be a bool")
        pulumi.set(__self__, "is_enabled", is_enabled)
        if last_modified_time and not isinstance(last_modified_time, str):
            raise TypeError("Expected argument 'last_modified_time' to be a str")
        pulumi.set(__self__, "last_modified_time", last_modified_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if next_run and not isinstance(next_run, str):
            raise TypeError("Expected argument 'next_run' to be a str")
        pulumi.set(__self__, "next_run", next_run)
        if next_run_offset_minutes and not isinstance(next_run_offset_minutes, float):
            raise TypeError("Expected argument 'next_run_offset_minutes' to be a float")
        pulumi.set(__self__, "next_run_offset_minutes", next_run_offset_minutes)
        if start_time and not isinstance(start_time, str):
            raise TypeError("Expected argument 'start_time' to be a str")
        pulumi.set(__self__, "start_time", start_time)
        if start_time_offset_minutes and not isinstance(start_time_offset_minutes, float):
            raise TypeError("Expected argument 'start_time_offset_minutes' to be a float")
        pulumi.set(__self__, "start_time_offset_minutes", start_time_offset_minutes)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if time_zone and not isinstance(time_zone, str):
            raise TypeError("Expected argument 'time_zone' to be a str")
        pulumi.set(__self__, "time_zone", time_zone)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="advancedSchedule")
    def advanced_schedule(self) -> Optional['outputs.AdvancedScheduleResponse']:
        """
        Gets or sets the advanced schedule.
        """
        return pulumi.get(self, "advanced_schedule")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[str]:
        """
        Gets or sets the creation time.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Gets or sets the description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[str]:
        """
        Gets or sets the end time of the schedule.
        """
        return pulumi.get(self, "expiry_time")

    @property
    @pulumi.getter(name="expiryTimeOffsetMinutes")
    def expiry_time_offset_minutes(self) -> Optional[float]:
        """
        Gets or sets the expiry time's offset in minutes.
        """
        return pulumi.get(self, "expiry_time_offset_minutes")

    @property
    @pulumi.getter
    def frequency(self) -> Optional[str]:
        """
        Gets or sets the frequency of the schedule.
        """
        return pulumi.get(self, "frequency")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def interval(self) -> Optional[Any]:
        """
        Gets or sets the interval of the schedule.
        """
        return pulumi.get(self, "interval")

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[bool]:
        """
        Gets or sets a value indicating whether this schedule is enabled.
        """
        return pulumi.get(self, "is_enabled")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[str]:
        """
        Gets or sets the last modified time.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nextRun")
    def next_run(self) -> Optional[str]:
        """
        Gets or sets the next run time of the schedule.
        """
        return pulumi.get(self, "next_run")

    @property
    @pulumi.getter(name="nextRunOffsetMinutes")
    def next_run_offset_minutes(self) -> Optional[float]:
        """
        Gets or sets the next run time's offset in minutes.
        """
        return pulumi.get(self, "next_run_offset_minutes")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[str]:
        """
        Gets or sets the start time of the schedule.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter(name="startTimeOffsetMinutes")
    def start_time_offset_minutes(self) -> float:
        """
        Gets the start time's offset in minutes.
        """
        return pulumi.get(self, "start_time_offset_minutes")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[str]:
        """
        Gets or sets the time zone of the schedule.
        """
        return pulumi.get(self, "time_zone")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetScheduleResult(GetScheduleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScheduleResult(
            advanced_schedule=self.advanced_schedule,
            creation_time=self.creation_time,
            description=self.description,
            expiry_time=self.expiry_time,
            expiry_time_offset_minutes=self.expiry_time_offset_minutes,
            frequency=self.frequency,
            id=self.id,
            interval=self.interval,
            is_enabled=self.is_enabled,
            last_modified_time=self.last_modified_time,
            name=self.name,
            next_run=self.next_run,
            next_run_offset_minutes=self.next_run_offset_minutes,
            start_time=self.start_time,
            start_time_offset_minutes=self.start_time_offset_minutes,
            system_data=self.system_data,
            time_zone=self.time_zone,
            type=self.type)


def get_schedule(automation_account_name: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 schedule_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScheduleResult:
    """
    Retrieve the schedule identified by schedule name.


    :param str automation_account_name: The name of the automation account.
    :param str resource_group_name: Name of an Azure Resource group.
    :param str schedule_name: The schedule name.
    """
    __args__ = dict()
    __args__['automationAccountName'] = automation_account_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['scheduleName'] = schedule_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:automation/v20230515preview:getSchedule', __args__, opts=opts, typ=GetScheduleResult).value

    return AwaitableGetScheduleResult(
        advanced_schedule=pulumi.get(__ret__, 'advanced_schedule'),
        creation_time=pulumi.get(__ret__, 'creation_time'),
        description=pulumi.get(__ret__, 'description'),
        expiry_time=pulumi.get(__ret__, 'expiry_time'),
        expiry_time_offset_minutes=pulumi.get(__ret__, 'expiry_time_offset_minutes'),
        frequency=pulumi.get(__ret__, 'frequency'),
        id=pulumi.get(__ret__, 'id'),
        interval=pulumi.get(__ret__, 'interval'),
        is_enabled=pulumi.get(__ret__, 'is_enabled'),
        last_modified_time=pulumi.get(__ret__, 'last_modified_time'),
        name=pulumi.get(__ret__, 'name'),
        next_run=pulumi.get(__ret__, 'next_run'),
        next_run_offset_minutes=pulumi.get(__ret__, 'next_run_offset_minutes'),
        start_time=pulumi.get(__ret__, 'start_time'),
        start_time_offset_minutes=pulumi.get(__ret__, 'start_time_offset_minutes'),
        system_data=pulumi.get(__ret__, 'system_data'),
        time_zone=pulumi.get(__ret__, 'time_zone'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_schedule)
def get_schedule_output(automation_account_name: Optional[pulumi.Input[str]] = None,
                        resource_group_name: Optional[pulumi.Input[str]] = None,
                        schedule_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetScheduleResult]:
    """
    Retrieve the schedule identified by schedule name.


    :param str automation_account_name: The name of the automation account.
    :param str resource_group_name: Name of an Azure Resource group.
    :param str schedule_name: The schedule name.
    """
    ...
