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
    Represents a Schedule to execute a task.
    """
    def __init__(__self__, frequency=None, id=None, name=None, provisioning_state=None, state=None, system_data=None, time=None, time_zone=None, type=None):
        if frequency and not isinstance(frequency, str):
            raise TypeError("Expected argument 'frequency' to be a str")
        pulumi.set(__self__, "frequency", frequency)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if time and not isinstance(time, str):
            raise TypeError("Expected argument 'time' to be a str")
        pulumi.set(__self__, "time", time)
        if time_zone and not isinstance(time_zone, str):
            raise TypeError("Expected argument 'time_zone' to be a str")
        pulumi.set(__self__, "time_zone", time_zone)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def frequency(self) -> str:
        """
        The frequency of this scheduled task.
        """
        return pulumi.get(self, "frequency")

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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        Indicates whether or not this scheduled task is enabled.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def time(self) -> str:
        """
        The target time to trigger the action. The format is HH:MM.
        """
        return pulumi.get(self, "time")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> str:
        """
        The IANA timezone id at which the schedule should execute.
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
            frequency=self.frequency,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            state=self.state,
            system_data=self.system_data,
            time=self.time,
            time_zone=self.time_zone,
            type=self.type)


def get_schedule(pool_name: Optional[str] = None,
                 project_name: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 schedule_name: Optional[str] = None,
                 top: Optional[int] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScheduleResult:
    """
    Gets a schedule resource.


    :param str pool_name: Name of the pool.
    :param str project_name: The name of the project.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str schedule_name: The name of the schedule that uniquely identifies it.
    :param int top: The maximum number of resources to return from the operation. Example: '$top=10'.
    """
    __args__ = dict()
    __args__['poolName'] = pool_name
    __args__['projectName'] = project_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['scheduleName'] = schedule_name
    __args__['top'] = top
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:devcenter/v20230401:getSchedule', __args__, opts=opts, typ=GetScheduleResult).value

    return AwaitableGetScheduleResult(
        frequency=pulumi.get(__ret__, 'frequency'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        state=pulumi.get(__ret__, 'state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        time=pulumi.get(__ret__, 'time'),
        time_zone=pulumi.get(__ret__, 'time_zone'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_schedule)
def get_schedule_output(pool_name: Optional[pulumi.Input[str]] = None,
                        project_name: Optional[pulumi.Input[str]] = None,
                        resource_group_name: Optional[pulumi.Input[str]] = None,
                        schedule_name: Optional[pulumi.Input[str]] = None,
                        top: Optional[pulumi.Input[Optional[int]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetScheduleResult]:
    """
    Gets a schedule resource.


    :param str pool_name: Name of the pool.
    :param str project_name: The name of the project.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str schedule_name: The name of the schedule that uniquely identifies it.
    :param int top: The maximum number of resources to return from the operation. Example: '$top=10'.
    """
    ...
