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
    'GetStartStopManagedInstanceScheduleResult',
    'AwaitableGetStartStopManagedInstanceScheduleResult',
    'get_start_stop_managed_instance_schedule',
    'get_start_stop_managed_instance_schedule_output',
]

@pulumi.output_type
class GetStartStopManagedInstanceScheduleResult:
    """
    Managed instance's Start/Stop schedule.
    """
    def __init__(__self__, description=None, id=None, name=None, next_execution_time=None, next_run_action=None, schedule_list=None, system_data=None, time_zone_id=None, type=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if next_execution_time and not isinstance(next_execution_time, str):
            raise TypeError("Expected argument 'next_execution_time' to be a str")
        pulumi.set(__self__, "next_execution_time", next_execution_time)
        if next_run_action and not isinstance(next_run_action, str):
            raise TypeError("Expected argument 'next_run_action' to be a str")
        pulumi.set(__self__, "next_run_action", next_run_action)
        if schedule_list and not isinstance(schedule_list, list):
            raise TypeError("Expected argument 'schedule_list' to be a list")
        pulumi.set(__self__, "schedule_list", schedule_list)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if time_zone_id and not isinstance(time_zone_id, str):
            raise TypeError("Expected argument 'time_zone_id' to be a str")
        pulumi.set(__self__, "time_zone_id", time_zone_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the schedule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nextExecutionTime")
    def next_execution_time(self) -> str:
        """
        Timestamp when the next action will be executed in the corresponding schedule time zone.
        """
        return pulumi.get(self, "next_execution_time")

    @property
    @pulumi.getter(name="nextRunAction")
    def next_run_action(self) -> str:
        """
        Next action to be executed (Start or Stop)
        """
        return pulumi.get(self, "next_run_action")

    @property
    @pulumi.getter(name="scheduleList")
    def schedule_list(self) -> Sequence['outputs.ScheduleItemResponse']:
        """
        Schedule list.
        """
        return pulumi.get(self, "schedule_list")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        System data of the scheduled resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="timeZoneId")
    def time_zone_id(self) -> Optional[str]:
        """
        The time zone of the schedule.
        """
        return pulumi.get(self, "time_zone_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetStartStopManagedInstanceScheduleResult(GetStartStopManagedInstanceScheduleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStartStopManagedInstanceScheduleResult(
            description=self.description,
            id=self.id,
            name=self.name,
            next_execution_time=self.next_execution_time,
            next_run_action=self.next_run_action,
            schedule_list=self.schedule_list,
            system_data=self.system_data,
            time_zone_id=self.time_zone_id,
            type=self.type)


def get_start_stop_managed_instance_schedule(managed_instance_name: Optional[str] = None,
                                             resource_group_name: Optional[str] = None,
                                             start_stop_schedule_name: Optional[str] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStartStopManagedInstanceScheduleResult:
    """
    Gets the managed instance's Start/Stop schedule.


    :param str managed_instance_name: The name of the managed instance.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str start_stop_schedule_name: Name of the managed instance Start/Stop schedule.
    """
    __args__ = dict()
    __args__['managedInstanceName'] = managed_instance_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['startStopScheduleName'] = start_stop_schedule_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20230801preview:getStartStopManagedInstanceSchedule', __args__, opts=opts, typ=GetStartStopManagedInstanceScheduleResult).value

    return AwaitableGetStartStopManagedInstanceScheduleResult(
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        next_execution_time=pulumi.get(__ret__, 'next_execution_time'),
        next_run_action=pulumi.get(__ret__, 'next_run_action'),
        schedule_list=pulumi.get(__ret__, 'schedule_list'),
        system_data=pulumi.get(__ret__, 'system_data'),
        time_zone_id=pulumi.get(__ret__, 'time_zone_id'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_start_stop_managed_instance_schedule)
def get_start_stop_managed_instance_schedule_output(managed_instance_name: Optional[pulumi.Input[str]] = None,
                                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                                    start_stop_schedule_name: Optional[pulumi.Input[str]] = None,
                                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStartStopManagedInstanceScheduleResult]:
    """
    Gets the managed instance's Start/Stop schedule.


    :param str managed_instance_name: The name of the managed instance.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str start_stop_schedule_name: Name of the managed instance Start/Stop schedule.
    """
    ...
