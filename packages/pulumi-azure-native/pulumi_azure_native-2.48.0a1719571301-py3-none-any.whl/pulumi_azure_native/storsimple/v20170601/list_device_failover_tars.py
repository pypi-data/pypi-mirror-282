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
    'ListDeviceFailoverTarsResult',
    'AwaitableListDeviceFailoverTarsResult',
    'list_device_failover_tars',
    'list_device_failover_tars_output',
]

@pulumi.output_type
class ListDeviceFailoverTarsResult:
    """
    The list of all devices in a resource and their eligibility status as a failover target device.
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.FailoverTargetResponse']]:
        """
        The list of all the failover targets.
        """
        return pulumi.get(self, "value")


class AwaitableListDeviceFailoverTarsResult(ListDeviceFailoverTarsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListDeviceFailoverTarsResult(
            value=self.value)


def list_device_failover_tars(manager_name: Optional[str] = None,
                              resource_group_name: Optional[str] = None,
                              source_device_name: Optional[str] = None,
                              volume_containers: Optional[Sequence[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListDeviceFailoverTarsResult:
    """
    Given a list of volume containers to be failed over from a source device, this method returns the eligibility result, as a failover target, for all devices under that resource.


    :param str manager_name: The manager name
    :param str resource_group_name: The resource group name
    :param str source_device_name: The source device name on which failover is performed.
    :param Sequence[str] volume_containers: The list of path IDs of the volume containers that needs to be failed-over, for which we want to fetch the eligible targets.
    """
    __args__ = dict()
    __args__['managerName'] = manager_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['sourceDeviceName'] = source_device_name
    __args__['volumeContainers'] = volume_containers
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:storsimple/v20170601:listDeviceFailoverTars', __args__, opts=opts, typ=ListDeviceFailoverTarsResult).value

    return AwaitableListDeviceFailoverTarsResult(
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_device_failover_tars)
def list_device_failover_tars_output(manager_name: Optional[pulumi.Input[str]] = None,
                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                     source_device_name: Optional[pulumi.Input[str]] = None,
                                     volume_containers: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListDeviceFailoverTarsResult]:
    """
    Given a list of volume containers to be failed over from a source device, this method returns the eligibility result, as a failover target, for all devices under that resource.


    :param str manager_name: The manager name
    :param str resource_group_name: The resource group name
    :param str source_device_name: The source device name on which failover is performed.
    :param Sequence[str] volume_containers: The list of path IDs of the volume containers that needs to be failed-over, for which we want to fetch the eligible targets.
    """
    ...
