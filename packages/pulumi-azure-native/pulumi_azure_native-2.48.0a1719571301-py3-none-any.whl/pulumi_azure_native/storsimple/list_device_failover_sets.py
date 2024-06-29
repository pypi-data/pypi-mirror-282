# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'ListDeviceFailoverSetsResult',
    'AwaitableListDeviceFailoverSetsResult',
    'list_device_failover_sets',
    'list_device_failover_sets_output',
]

@pulumi.output_type
class ListDeviceFailoverSetsResult:
    """
    The list of failover sets.
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.FailoverSetResponse']]:
        """
        The list of failover sets.
        """
        return pulumi.get(self, "value")


class AwaitableListDeviceFailoverSetsResult(ListDeviceFailoverSetsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListDeviceFailoverSetsResult(
            value=self.value)


def list_device_failover_sets(device_name: Optional[str] = None,
                              manager_name: Optional[str] = None,
                              resource_group_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListDeviceFailoverSetsResult:
    """
    Returns all failover sets for a given device and their eligibility for participating in a failover. A failover set refers to a set of volume containers that need to be failed-over as a single unit to maintain data integrity.
    Azure REST API version: 2017-06-01.


    :param str device_name: The device name
    :param str manager_name: The manager name
    :param str resource_group_name: The resource group name
    """
    __args__ = dict()
    __args__['deviceName'] = device_name
    __args__['managerName'] = manager_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:storsimple:listDeviceFailoverSets', __args__, opts=opts, typ=ListDeviceFailoverSetsResult).value

    return AwaitableListDeviceFailoverSetsResult(
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_device_failover_sets)
def list_device_failover_sets_output(device_name: Optional[pulumi.Input[str]] = None,
                                     manager_name: Optional[pulumi.Input[str]] = None,
                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListDeviceFailoverSetsResult]:
    """
    Returns all failover sets for a given device and their eligibility for participating in a failover. A failover set refers to a set of volume containers that need to be failed-over as a single unit to maintain data integrity.
    Azure REST API version: 2017-06-01.


    :param str device_name: The device name
    :param str manager_name: The manager name
    :param str resource_group_name: The resource group name
    """
    ...
