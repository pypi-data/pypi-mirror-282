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
    'ListWebhookEventsResult',
    'AwaitableListWebhookEventsResult',
    'list_webhook_events',
    'list_webhook_events_output',
]

@pulumi.output_type
class ListWebhookEventsResult:
    """
    The result of a request to list events for a webhook.
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[str]:
        """
        The URI that can be used to request the next list of events.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.EventResponse']]:
        """
        The list of events. Since this list may be incomplete, the nextLink field should be used to request the next list of events.
        """
        return pulumi.get(self, "value")


class AwaitableListWebhookEventsResult(ListWebhookEventsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListWebhookEventsResult(
            next_link=self.next_link,
            value=self.value)


def list_webhook_events(registry_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        webhook_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListWebhookEventsResult:
    """
    Lists recent events for the specified webhook.


    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str webhook_name: The name of the webhook.
    """
    __args__ = dict()
    __args__['registryName'] = registry_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['webhookName'] = webhook_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerregistry/v20230801preview:listWebhookEvents', __args__, opts=opts, typ=ListWebhookEventsResult).value

    return AwaitableListWebhookEventsResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_webhook_events)
def list_webhook_events_output(registry_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               webhook_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListWebhookEventsResult]:
    """
    Lists recent events for the specified webhook.


    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str webhook_name: The name of the webhook.
    """
    ...
