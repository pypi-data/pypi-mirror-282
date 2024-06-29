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
    'GetScalingPlanPersonalScheduleResult',
    'AwaitableGetScalingPlanPersonalScheduleResult',
    'get_scaling_plan_personal_schedule',
    'get_scaling_plan_personal_schedule_output',
]

@pulumi.output_type
class GetScalingPlanPersonalScheduleResult:
    """
    Represents a ScalingPlanPersonalSchedule definition.
    """
    def __init__(__self__, days_of_week=None, id=None, name=None, off_peak_action_on_disconnect=None, off_peak_action_on_logoff=None, off_peak_minutes_to_wait_on_disconnect=None, off_peak_minutes_to_wait_on_logoff=None, off_peak_start_time=None, off_peak_start_vm_on_connect=None, peak_action_on_disconnect=None, peak_action_on_logoff=None, peak_minutes_to_wait_on_disconnect=None, peak_minutes_to_wait_on_logoff=None, peak_start_time=None, peak_start_vm_on_connect=None, ramp_down_action_on_disconnect=None, ramp_down_action_on_logoff=None, ramp_down_minutes_to_wait_on_disconnect=None, ramp_down_minutes_to_wait_on_logoff=None, ramp_down_start_time=None, ramp_down_start_vm_on_connect=None, ramp_up_action_on_disconnect=None, ramp_up_action_on_logoff=None, ramp_up_auto_start_hosts=None, ramp_up_minutes_to_wait_on_disconnect=None, ramp_up_minutes_to_wait_on_logoff=None, ramp_up_start_time=None, ramp_up_start_vm_on_connect=None, system_data=None, type=None):
        if days_of_week and not isinstance(days_of_week, list):
            raise TypeError("Expected argument 'days_of_week' to be a list")
        pulumi.set(__self__, "days_of_week", days_of_week)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if off_peak_action_on_disconnect and not isinstance(off_peak_action_on_disconnect, str):
            raise TypeError("Expected argument 'off_peak_action_on_disconnect' to be a str")
        pulumi.set(__self__, "off_peak_action_on_disconnect", off_peak_action_on_disconnect)
        if off_peak_action_on_logoff and not isinstance(off_peak_action_on_logoff, str):
            raise TypeError("Expected argument 'off_peak_action_on_logoff' to be a str")
        pulumi.set(__self__, "off_peak_action_on_logoff", off_peak_action_on_logoff)
        if off_peak_minutes_to_wait_on_disconnect and not isinstance(off_peak_minutes_to_wait_on_disconnect, int):
            raise TypeError("Expected argument 'off_peak_minutes_to_wait_on_disconnect' to be a int")
        pulumi.set(__self__, "off_peak_minutes_to_wait_on_disconnect", off_peak_minutes_to_wait_on_disconnect)
        if off_peak_minutes_to_wait_on_logoff and not isinstance(off_peak_minutes_to_wait_on_logoff, int):
            raise TypeError("Expected argument 'off_peak_minutes_to_wait_on_logoff' to be a int")
        pulumi.set(__self__, "off_peak_minutes_to_wait_on_logoff", off_peak_minutes_to_wait_on_logoff)
        if off_peak_start_time and not isinstance(off_peak_start_time, dict):
            raise TypeError("Expected argument 'off_peak_start_time' to be a dict")
        pulumi.set(__self__, "off_peak_start_time", off_peak_start_time)
        if off_peak_start_vm_on_connect and not isinstance(off_peak_start_vm_on_connect, str):
            raise TypeError("Expected argument 'off_peak_start_vm_on_connect' to be a str")
        pulumi.set(__self__, "off_peak_start_vm_on_connect", off_peak_start_vm_on_connect)
        if peak_action_on_disconnect and not isinstance(peak_action_on_disconnect, str):
            raise TypeError("Expected argument 'peak_action_on_disconnect' to be a str")
        pulumi.set(__self__, "peak_action_on_disconnect", peak_action_on_disconnect)
        if peak_action_on_logoff and not isinstance(peak_action_on_logoff, str):
            raise TypeError("Expected argument 'peak_action_on_logoff' to be a str")
        pulumi.set(__self__, "peak_action_on_logoff", peak_action_on_logoff)
        if peak_minutes_to_wait_on_disconnect and not isinstance(peak_minutes_to_wait_on_disconnect, int):
            raise TypeError("Expected argument 'peak_minutes_to_wait_on_disconnect' to be a int")
        pulumi.set(__self__, "peak_minutes_to_wait_on_disconnect", peak_minutes_to_wait_on_disconnect)
        if peak_minutes_to_wait_on_logoff and not isinstance(peak_minutes_to_wait_on_logoff, int):
            raise TypeError("Expected argument 'peak_minutes_to_wait_on_logoff' to be a int")
        pulumi.set(__self__, "peak_minutes_to_wait_on_logoff", peak_minutes_to_wait_on_logoff)
        if peak_start_time and not isinstance(peak_start_time, dict):
            raise TypeError("Expected argument 'peak_start_time' to be a dict")
        pulumi.set(__self__, "peak_start_time", peak_start_time)
        if peak_start_vm_on_connect and not isinstance(peak_start_vm_on_connect, str):
            raise TypeError("Expected argument 'peak_start_vm_on_connect' to be a str")
        pulumi.set(__self__, "peak_start_vm_on_connect", peak_start_vm_on_connect)
        if ramp_down_action_on_disconnect and not isinstance(ramp_down_action_on_disconnect, str):
            raise TypeError("Expected argument 'ramp_down_action_on_disconnect' to be a str")
        pulumi.set(__self__, "ramp_down_action_on_disconnect", ramp_down_action_on_disconnect)
        if ramp_down_action_on_logoff and not isinstance(ramp_down_action_on_logoff, str):
            raise TypeError("Expected argument 'ramp_down_action_on_logoff' to be a str")
        pulumi.set(__self__, "ramp_down_action_on_logoff", ramp_down_action_on_logoff)
        if ramp_down_minutes_to_wait_on_disconnect and not isinstance(ramp_down_minutes_to_wait_on_disconnect, int):
            raise TypeError("Expected argument 'ramp_down_minutes_to_wait_on_disconnect' to be a int")
        pulumi.set(__self__, "ramp_down_minutes_to_wait_on_disconnect", ramp_down_minutes_to_wait_on_disconnect)
        if ramp_down_minutes_to_wait_on_logoff and not isinstance(ramp_down_minutes_to_wait_on_logoff, int):
            raise TypeError("Expected argument 'ramp_down_minutes_to_wait_on_logoff' to be a int")
        pulumi.set(__self__, "ramp_down_minutes_to_wait_on_logoff", ramp_down_minutes_to_wait_on_logoff)
        if ramp_down_start_time and not isinstance(ramp_down_start_time, dict):
            raise TypeError("Expected argument 'ramp_down_start_time' to be a dict")
        pulumi.set(__self__, "ramp_down_start_time", ramp_down_start_time)
        if ramp_down_start_vm_on_connect and not isinstance(ramp_down_start_vm_on_connect, str):
            raise TypeError("Expected argument 'ramp_down_start_vm_on_connect' to be a str")
        pulumi.set(__self__, "ramp_down_start_vm_on_connect", ramp_down_start_vm_on_connect)
        if ramp_up_action_on_disconnect and not isinstance(ramp_up_action_on_disconnect, str):
            raise TypeError("Expected argument 'ramp_up_action_on_disconnect' to be a str")
        pulumi.set(__self__, "ramp_up_action_on_disconnect", ramp_up_action_on_disconnect)
        if ramp_up_action_on_logoff and not isinstance(ramp_up_action_on_logoff, str):
            raise TypeError("Expected argument 'ramp_up_action_on_logoff' to be a str")
        pulumi.set(__self__, "ramp_up_action_on_logoff", ramp_up_action_on_logoff)
        if ramp_up_auto_start_hosts and not isinstance(ramp_up_auto_start_hosts, str):
            raise TypeError("Expected argument 'ramp_up_auto_start_hosts' to be a str")
        pulumi.set(__self__, "ramp_up_auto_start_hosts", ramp_up_auto_start_hosts)
        if ramp_up_minutes_to_wait_on_disconnect and not isinstance(ramp_up_minutes_to_wait_on_disconnect, int):
            raise TypeError("Expected argument 'ramp_up_minutes_to_wait_on_disconnect' to be a int")
        pulumi.set(__self__, "ramp_up_minutes_to_wait_on_disconnect", ramp_up_minutes_to_wait_on_disconnect)
        if ramp_up_minutes_to_wait_on_logoff and not isinstance(ramp_up_minutes_to_wait_on_logoff, int):
            raise TypeError("Expected argument 'ramp_up_minutes_to_wait_on_logoff' to be a int")
        pulumi.set(__self__, "ramp_up_minutes_to_wait_on_logoff", ramp_up_minutes_to_wait_on_logoff)
        if ramp_up_start_time and not isinstance(ramp_up_start_time, dict):
            raise TypeError("Expected argument 'ramp_up_start_time' to be a dict")
        pulumi.set(__self__, "ramp_up_start_time", ramp_up_start_time)
        if ramp_up_start_vm_on_connect and not isinstance(ramp_up_start_vm_on_connect, str):
            raise TypeError("Expected argument 'ramp_up_start_vm_on_connect' to be a str")
        pulumi.set(__self__, "ramp_up_start_vm_on_connect", ramp_up_start_vm_on_connect)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="daysOfWeek")
    def days_of_week(self) -> Optional[Sequence[str]]:
        """
        Set of days of the week on which this schedule is active.
        """
        return pulumi.get(self, "days_of_week")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="offPeakActionOnDisconnect")
    def off_peak_action_on_disconnect(self) -> Optional[str]:
        """
        Action to be taken after a user disconnect during the off-peak period.
        """
        return pulumi.get(self, "off_peak_action_on_disconnect")

    @property
    @pulumi.getter(name="offPeakActionOnLogoff")
    def off_peak_action_on_logoff(self) -> Optional[str]:
        """
        Action to be taken after a logoff during the off-peak period.
        """
        return pulumi.get(self, "off_peak_action_on_logoff")

    @property
    @pulumi.getter(name="offPeakMinutesToWaitOnDisconnect")
    def off_peak_minutes_to_wait_on_disconnect(self) -> Optional[int]:
        """
        The time in minutes to wait before performing the desired session handling action when a user disconnects during the off-peak period.
        """
        return pulumi.get(self, "off_peak_minutes_to_wait_on_disconnect")

    @property
    @pulumi.getter(name="offPeakMinutesToWaitOnLogoff")
    def off_peak_minutes_to_wait_on_logoff(self) -> Optional[int]:
        """
        The time in minutes to wait before performing the desired session handling action when a user logs off during the off-peak period.
        """
        return pulumi.get(self, "off_peak_minutes_to_wait_on_logoff")

    @property
    @pulumi.getter(name="offPeakStartTime")
    def off_peak_start_time(self) -> Optional['outputs.TimeResponse']:
        """
        Starting time for off-peak period.
        """
        return pulumi.get(self, "off_peak_start_time")

    @property
    @pulumi.getter(name="offPeakStartVMOnConnect")
    def off_peak_start_vm_on_connect(self) -> Optional[str]:
        """
        The desired configuration of Start VM On Connect for the hostpool during the off-peak phase.
        """
        return pulumi.get(self, "off_peak_start_vm_on_connect")

    @property
    @pulumi.getter(name="peakActionOnDisconnect")
    def peak_action_on_disconnect(self) -> Optional[str]:
        """
        Action to be taken after a user disconnect during the peak period.
        """
        return pulumi.get(self, "peak_action_on_disconnect")

    @property
    @pulumi.getter(name="peakActionOnLogoff")
    def peak_action_on_logoff(self) -> Optional[str]:
        """
        Action to be taken after a logoff during the peak period.
        """
        return pulumi.get(self, "peak_action_on_logoff")

    @property
    @pulumi.getter(name="peakMinutesToWaitOnDisconnect")
    def peak_minutes_to_wait_on_disconnect(self) -> Optional[int]:
        """
        The time in minutes to wait before performing the desired session handling action when a user disconnects during the peak period.
        """
        return pulumi.get(self, "peak_minutes_to_wait_on_disconnect")

    @property
    @pulumi.getter(name="peakMinutesToWaitOnLogoff")
    def peak_minutes_to_wait_on_logoff(self) -> Optional[int]:
        """
        The time in minutes to wait before performing the desired session handling action when a user logs off during the peak period.
        """
        return pulumi.get(self, "peak_minutes_to_wait_on_logoff")

    @property
    @pulumi.getter(name="peakStartTime")
    def peak_start_time(self) -> Optional['outputs.TimeResponse']:
        """
        Starting time for peak period.
        """
        return pulumi.get(self, "peak_start_time")

    @property
    @pulumi.getter(name="peakStartVMOnConnect")
    def peak_start_vm_on_connect(self) -> Optional[str]:
        """
        The desired configuration of Start VM On Connect for the hostpool during the peak phase.
        """
        return pulumi.get(self, "peak_start_vm_on_connect")

    @property
    @pulumi.getter(name="rampDownActionOnDisconnect")
    def ramp_down_action_on_disconnect(self) -> Optional[str]:
        """
        Action to be taken after a user disconnect during the ramp down period.
        """
        return pulumi.get(self, "ramp_down_action_on_disconnect")

    @property
    @pulumi.getter(name="rampDownActionOnLogoff")
    def ramp_down_action_on_logoff(self) -> Optional[str]:
        """
        Action to be taken after a logoff during the ramp down period.
        """
        return pulumi.get(self, "ramp_down_action_on_logoff")

    @property
    @pulumi.getter(name="rampDownMinutesToWaitOnDisconnect")
    def ramp_down_minutes_to_wait_on_disconnect(self) -> Optional[int]:
        """
        The time in minutes to wait before performing the desired session handling action when a user disconnects during the ramp down period.
        """
        return pulumi.get(self, "ramp_down_minutes_to_wait_on_disconnect")

    @property
    @pulumi.getter(name="rampDownMinutesToWaitOnLogoff")
    def ramp_down_minutes_to_wait_on_logoff(self) -> Optional[int]:
        """
        The time in minutes to wait before performing the desired session handling action when a user logs off during the ramp down period.
        """
        return pulumi.get(self, "ramp_down_minutes_to_wait_on_logoff")

    @property
    @pulumi.getter(name="rampDownStartTime")
    def ramp_down_start_time(self) -> Optional['outputs.TimeResponse']:
        """
        Starting time for ramp down period.
        """
        return pulumi.get(self, "ramp_down_start_time")

    @property
    @pulumi.getter(name="rampDownStartVMOnConnect")
    def ramp_down_start_vm_on_connect(self) -> Optional[str]:
        """
        The desired configuration of Start VM On Connect for the hostpool during the ramp down phase.
        """
        return pulumi.get(self, "ramp_down_start_vm_on_connect")

    @property
    @pulumi.getter(name="rampUpActionOnDisconnect")
    def ramp_up_action_on_disconnect(self) -> Optional[str]:
        """
        Action to be taken after a user disconnect during the ramp up period.
        """
        return pulumi.get(self, "ramp_up_action_on_disconnect")

    @property
    @pulumi.getter(name="rampUpActionOnLogoff")
    def ramp_up_action_on_logoff(self) -> Optional[str]:
        """
        Action to be taken after a logoff during the ramp up period.
        """
        return pulumi.get(self, "ramp_up_action_on_logoff")

    @property
    @pulumi.getter(name="rampUpAutoStartHosts")
    def ramp_up_auto_start_hosts(self) -> Optional[str]:
        """
        The desired startup behavior during the ramp up period for personal vms in the hostpool.
        """
        return pulumi.get(self, "ramp_up_auto_start_hosts")

    @property
    @pulumi.getter(name="rampUpMinutesToWaitOnDisconnect")
    def ramp_up_minutes_to_wait_on_disconnect(self) -> Optional[int]:
        """
        The time in minutes to wait before performing the desired session handling action when a user disconnects during the ramp up period.
        """
        return pulumi.get(self, "ramp_up_minutes_to_wait_on_disconnect")

    @property
    @pulumi.getter(name="rampUpMinutesToWaitOnLogoff")
    def ramp_up_minutes_to_wait_on_logoff(self) -> Optional[int]:
        """
        The time in minutes to wait before performing the desired session handling action when a user logs off during the ramp up period.
        """
        return pulumi.get(self, "ramp_up_minutes_to_wait_on_logoff")

    @property
    @pulumi.getter(name="rampUpStartTime")
    def ramp_up_start_time(self) -> Optional['outputs.TimeResponse']:
        """
        Starting time for ramp up period.
        """
        return pulumi.get(self, "ramp_up_start_time")

    @property
    @pulumi.getter(name="rampUpStartVMOnConnect")
    def ramp_up_start_vm_on_connect(self) -> Optional[str]:
        """
        The desired configuration of Start VM On Connect for the hostpool during the ramp up phase. If this is disabled, session hosts must be turned on using rampUpAutoStartHosts or by turning them on manually.
        """
        return pulumi.get(self, "ramp_up_start_vm_on_connect")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetScalingPlanPersonalScheduleResult(GetScalingPlanPersonalScheduleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScalingPlanPersonalScheduleResult(
            days_of_week=self.days_of_week,
            id=self.id,
            name=self.name,
            off_peak_action_on_disconnect=self.off_peak_action_on_disconnect,
            off_peak_action_on_logoff=self.off_peak_action_on_logoff,
            off_peak_minutes_to_wait_on_disconnect=self.off_peak_minutes_to_wait_on_disconnect,
            off_peak_minutes_to_wait_on_logoff=self.off_peak_minutes_to_wait_on_logoff,
            off_peak_start_time=self.off_peak_start_time,
            off_peak_start_vm_on_connect=self.off_peak_start_vm_on_connect,
            peak_action_on_disconnect=self.peak_action_on_disconnect,
            peak_action_on_logoff=self.peak_action_on_logoff,
            peak_minutes_to_wait_on_disconnect=self.peak_minutes_to_wait_on_disconnect,
            peak_minutes_to_wait_on_logoff=self.peak_minutes_to_wait_on_logoff,
            peak_start_time=self.peak_start_time,
            peak_start_vm_on_connect=self.peak_start_vm_on_connect,
            ramp_down_action_on_disconnect=self.ramp_down_action_on_disconnect,
            ramp_down_action_on_logoff=self.ramp_down_action_on_logoff,
            ramp_down_minutes_to_wait_on_disconnect=self.ramp_down_minutes_to_wait_on_disconnect,
            ramp_down_minutes_to_wait_on_logoff=self.ramp_down_minutes_to_wait_on_logoff,
            ramp_down_start_time=self.ramp_down_start_time,
            ramp_down_start_vm_on_connect=self.ramp_down_start_vm_on_connect,
            ramp_up_action_on_disconnect=self.ramp_up_action_on_disconnect,
            ramp_up_action_on_logoff=self.ramp_up_action_on_logoff,
            ramp_up_auto_start_hosts=self.ramp_up_auto_start_hosts,
            ramp_up_minutes_to_wait_on_disconnect=self.ramp_up_minutes_to_wait_on_disconnect,
            ramp_up_minutes_to_wait_on_logoff=self.ramp_up_minutes_to_wait_on_logoff,
            ramp_up_start_time=self.ramp_up_start_time,
            ramp_up_start_vm_on_connect=self.ramp_up_start_vm_on_connect,
            system_data=self.system_data,
            type=self.type)


def get_scaling_plan_personal_schedule(resource_group_name: Optional[str] = None,
                                       scaling_plan_name: Optional[str] = None,
                                       scaling_plan_schedule_name: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScalingPlanPersonalScheduleResult:
    """
    Get a ScalingPlanPersonalSchedule.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str scaling_plan_name: The name of the scaling plan.
    :param str scaling_plan_schedule_name: The name of the ScalingPlanSchedule
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['scalingPlanName'] = scaling_plan_name
    __args__['scalingPlanScheduleName'] = scaling_plan_schedule_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:desktopvirtualization/v20240306preview:getScalingPlanPersonalSchedule', __args__, opts=opts, typ=GetScalingPlanPersonalScheduleResult).value

    return AwaitableGetScalingPlanPersonalScheduleResult(
        days_of_week=pulumi.get(__ret__, 'days_of_week'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        off_peak_action_on_disconnect=pulumi.get(__ret__, 'off_peak_action_on_disconnect'),
        off_peak_action_on_logoff=pulumi.get(__ret__, 'off_peak_action_on_logoff'),
        off_peak_minutes_to_wait_on_disconnect=pulumi.get(__ret__, 'off_peak_minutes_to_wait_on_disconnect'),
        off_peak_minutes_to_wait_on_logoff=pulumi.get(__ret__, 'off_peak_minutes_to_wait_on_logoff'),
        off_peak_start_time=pulumi.get(__ret__, 'off_peak_start_time'),
        off_peak_start_vm_on_connect=pulumi.get(__ret__, 'off_peak_start_vm_on_connect'),
        peak_action_on_disconnect=pulumi.get(__ret__, 'peak_action_on_disconnect'),
        peak_action_on_logoff=pulumi.get(__ret__, 'peak_action_on_logoff'),
        peak_minutes_to_wait_on_disconnect=pulumi.get(__ret__, 'peak_minutes_to_wait_on_disconnect'),
        peak_minutes_to_wait_on_logoff=pulumi.get(__ret__, 'peak_minutes_to_wait_on_logoff'),
        peak_start_time=pulumi.get(__ret__, 'peak_start_time'),
        peak_start_vm_on_connect=pulumi.get(__ret__, 'peak_start_vm_on_connect'),
        ramp_down_action_on_disconnect=pulumi.get(__ret__, 'ramp_down_action_on_disconnect'),
        ramp_down_action_on_logoff=pulumi.get(__ret__, 'ramp_down_action_on_logoff'),
        ramp_down_minutes_to_wait_on_disconnect=pulumi.get(__ret__, 'ramp_down_minutes_to_wait_on_disconnect'),
        ramp_down_minutes_to_wait_on_logoff=pulumi.get(__ret__, 'ramp_down_minutes_to_wait_on_logoff'),
        ramp_down_start_time=pulumi.get(__ret__, 'ramp_down_start_time'),
        ramp_down_start_vm_on_connect=pulumi.get(__ret__, 'ramp_down_start_vm_on_connect'),
        ramp_up_action_on_disconnect=pulumi.get(__ret__, 'ramp_up_action_on_disconnect'),
        ramp_up_action_on_logoff=pulumi.get(__ret__, 'ramp_up_action_on_logoff'),
        ramp_up_auto_start_hosts=pulumi.get(__ret__, 'ramp_up_auto_start_hosts'),
        ramp_up_minutes_to_wait_on_disconnect=pulumi.get(__ret__, 'ramp_up_minutes_to_wait_on_disconnect'),
        ramp_up_minutes_to_wait_on_logoff=pulumi.get(__ret__, 'ramp_up_minutes_to_wait_on_logoff'),
        ramp_up_start_time=pulumi.get(__ret__, 'ramp_up_start_time'),
        ramp_up_start_vm_on_connect=pulumi.get(__ret__, 'ramp_up_start_vm_on_connect'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_scaling_plan_personal_schedule)
def get_scaling_plan_personal_schedule_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                              scaling_plan_name: Optional[pulumi.Input[str]] = None,
                                              scaling_plan_schedule_name: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetScalingPlanPersonalScheduleResult]:
    """
    Get a ScalingPlanPersonalSchedule.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str scaling_plan_name: The name of the scaling plan.
    :param str scaling_plan_schedule_name: The name of the ScalingPlanSchedule
    """
    ...
