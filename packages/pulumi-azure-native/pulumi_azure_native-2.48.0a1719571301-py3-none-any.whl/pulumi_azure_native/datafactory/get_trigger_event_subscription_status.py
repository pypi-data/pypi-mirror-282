# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetTriggerEventSubscriptionStatusResult',
    'AwaitableGetTriggerEventSubscriptionStatusResult',
    'get_trigger_event_subscription_status',
    'get_trigger_event_subscription_status_output',
]

@pulumi.output_type
class GetTriggerEventSubscriptionStatusResult:
    """
    Defines the response of a trigger subscription operation.
    """
    def __init__(__self__, status=None, trigger_name=None):
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if trigger_name and not isinstance(trigger_name, str):
            raise TypeError("Expected argument 'trigger_name' to be a str")
        pulumi.set(__self__, "trigger_name", trigger_name)

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Event Subscription Status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="triggerName")
    def trigger_name(self) -> str:
        """
        Trigger name.
        """
        return pulumi.get(self, "trigger_name")


class AwaitableGetTriggerEventSubscriptionStatusResult(GetTriggerEventSubscriptionStatusResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTriggerEventSubscriptionStatusResult(
            status=self.status,
            trigger_name=self.trigger_name)


def get_trigger_event_subscription_status(factory_name: Optional[str] = None,
                                          resource_group_name: Optional[str] = None,
                                          trigger_name: Optional[str] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTriggerEventSubscriptionStatusResult:
    """
    Get a trigger's event subscription status.
    Azure REST API version: 2018-06-01.


    :param str factory_name: The factory name.
    :param str resource_group_name: The resource group name.
    :param str trigger_name: The trigger name.
    """
    __args__ = dict()
    __args__['factoryName'] = factory_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['triggerName'] = trigger_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:datafactory:getTriggerEventSubscriptionStatus', __args__, opts=opts, typ=GetTriggerEventSubscriptionStatusResult).value

    return AwaitableGetTriggerEventSubscriptionStatusResult(
        status=pulumi.get(__ret__, 'status'),
        trigger_name=pulumi.get(__ret__, 'trigger_name'))


@_utilities.lift_output_func(get_trigger_event_subscription_status)
def get_trigger_event_subscription_status_output(factory_name: Optional[pulumi.Input[str]] = None,
                                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                                 trigger_name: Optional[pulumi.Input[str]] = None,
                                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTriggerEventSubscriptionStatusResult]:
    """
    Get a trigger's event subscription status.
    Azure REST API version: 2018-06-01.


    :param str factory_name: The factory name.
    :param str resource_group_name: The resource group name.
    :param str trigger_name: The trigger name.
    """
    ...
