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
    'GetUpdateRunResult',
    'AwaitableGetUpdateRunResult',
    'get_update_run',
    'get_update_run_output',
]

@pulumi.output_type
class GetUpdateRunResult:
    """
    Details of an Update run
    """
    def __init__(__self__, description=None, duration=None, end_time_utc=None, error_message=None, id=None, last_updated_time=None, last_updated_time_utc=None, location=None, name=None, provisioning_state=None, start_time_utc=None, state=None, status=None, steps=None, system_data=None, time_started=None, type=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if duration and not isinstance(duration, str):
            raise TypeError("Expected argument 'duration' to be a str")
        pulumi.set(__self__, "duration", duration)
        if end_time_utc and not isinstance(end_time_utc, str):
            raise TypeError("Expected argument 'end_time_utc' to be a str")
        pulumi.set(__self__, "end_time_utc", end_time_utc)
        if error_message and not isinstance(error_message, str):
            raise TypeError("Expected argument 'error_message' to be a str")
        pulumi.set(__self__, "error_message", error_message)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_updated_time and not isinstance(last_updated_time, str):
            raise TypeError("Expected argument 'last_updated_time' to be a str")
        pulumi.set(__self__, "last_updated_time", last_updated_time)
        if last_updated_time_utc and not isinstance(last_updated_time_utc, str):
            raise TypeError("Expected argument 'last_updated_time_utc' to be a str")
        pulumi.set(__self__, "last_updated_time_utc", last_updated_time_utc)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if start_time_utc and not isinstance(start_time_utc, str):
            raise TypeError("Expected argument 'start_time_utc' to be a str")
        pulumi.set(__self__, "start_time_utc", start_time_utc)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if steps and not isinstance(steps, list):
            raise TypeError("Expected argument 'steps' to be a list")
        pulumi.set(__self__, "steps", steps)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if time_started and not isinstance(time_started, str):
            raise TypeError("Expected argument 'time_started' to be a str")
        pulumi.set(__self__, "time_started", time_started)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        More detailed description of the step.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def duration(self) -> Optional[str]:
        """
        Duration of the update run.
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter(name="endTimeUtc")
    def end_time_utc(self) -> Optional[str]:
        """
        When the step reached a terminal state.
        """
        return pulumi.get(self, "end_time_utc")

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[str]:
        """
        Error message, specified if the step is in a failed state.
        """
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[str]:
        """
        Timestamp of the most recently completed step in the update run.
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter(name="lastUpdatedTimeUtc")
    def last_updated_time_utc(self) -> Optional[str]:
        """
        Completion time of this step or the last completed sub-step.
        """
        return pulumi.get(self, "last_updated_time_utc")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the UpdateRuns proxy resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="startTimeUtc")
    def start_time_utc(self) -> Optional[str]:
        """
        When the step started, or empty if it has not started executing.
        """
        return pulumi.get(self, "start_time_utc")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        State of the update run.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Status of the step, bubbled up from the ECE action plan for installation attempts. Values are: 'Success', 'Error', 'InProgress', and 'Unknown status'.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def steps(self) -> Optional[Sequence['outputs.StepResponse']]:
        """
        Recursive model for child steps of this step.
        """
        return pulumi.get(self, "steps")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="timeStarted")
    def time_started(self) -> Optional[str]:
        """
        Timestamp of the update run was started.
        """
        return pulumi.get(self, "time_started")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetUpdateRunResult(GetUpdateRunResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUpdateRunResult(
            description=self.description,
            duration=self.duration,
            end_time_utc=self.end_time_utc,
            error_message=self.error_message,
            id=self.id,
            last_updated_time=self.last_updated_time,
            last_updated_time_utc=self.last_updated_time_utc,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            start_time_utc=self.start_time_utc,
            state=self.state,
            status=self.status,
            steps=self.steps,
            system_data=self.system_data,
            time_started=self.time_started,
            type=self.type)


def get_update_run(cluster_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   update_name: Optional[str] = None,
                   update_run_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUpdateRunResult:
    """
    Get the Update run for a specified update


    :param str cluster_name: The name of the cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str update_name: The name of the Update
    :param str update_run_name: The name of the Update Run
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['updateName'] = update_name
    __args__['updateRunName'] = update_run_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azurestackhci/v20240215preview:getUpdateRun', __args__, opts=opts, typ=GetUpdateRunResult).value

    return AwaitableGetUpdateRunResult(
        description=pulumi.get(__ret__, 'description'),
        duration=pulumi.get(__ret__, 'duration'),
        end_time_utc=pulumi.get(__ret__, 'end_time_utc'),
        error_message=pulumi.get(__ret__, 'error_message'),
        id=pulumi.get(__ret__, 'id'),
        last_updated_time=pulumi.get(__ret__, 'last_updated_time'),
        last_updated_time_utc=pulumi.get(__ret__, 'last_updated_time_utc'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        start_time_utc=pulumi.get(__ret__, 'start_time_utc'),
        state=pulumi.get(__ret__, 'state'),
        status=pulumi.get(__ret__, 'status'),
        steps=pulumi.get(__ret__, 'steps'),
        system_data=pulumi.get(__ret__, 'system_data'),
        time_started=pulumi.get(__ret__, 'time_started'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_update_run)
def get_update_run_output(cluster_name: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          update_name: Optional[pulumi.Input[str]] = None,
                          update_run_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUpdateRunResult]:
    """
    Get the Update run for a specified update


    :param str cluster_name: The name of the cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str update_name: The name of the Update
    :param str update_run_name: The name of the Update Run
    """
    ...
