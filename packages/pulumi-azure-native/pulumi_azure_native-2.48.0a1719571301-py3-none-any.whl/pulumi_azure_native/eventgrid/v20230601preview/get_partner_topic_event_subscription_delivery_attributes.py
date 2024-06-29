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
    'GetPartnerTopicEventSubscriptionDeliveryAttributesResult',
    'AwaitableGetPartnerTopicEventSubscriptionDeliveryAttributesResult',
    'get_partner_topic_event_subscription_delivery_attributes',
    'get_partner_topic_event_subscription_delivery_attributes_output',
]

@pulumi.output_type
class GetPartnerTopicEventSubscriptionDeliveryAttributesResult:
    """
    Result of the Get delivery attributes operation.
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence[Any]]:
        """
        A collection of DeliveryAttributeMapping
        """
        return pulumi.get(self, "value")


class AwaitableGetPartnerTopicEventSubscriptionDeliveryAttributesResult(GetPartnerTopicEventSubscriptionDeliveryAttributesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPartnerTopicEventSubscriptionDeliveryAttributesResult(
            value=self.value)


def get_partner_topic_event_subscription_delivery_attributes(event_subscription_name: Optional[str] = None,
                                                             partner_topic_name: Optional[str] = None,
                                                             resource_group_name: Optional[str] = None,
                                                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPartnerTopicEventSubscriptionDeliveryAttributesResult:
    """
    Get all delivery attributes for an event subscription of a partner topic.


    :param str event_subscription_name: Name of the event subscription to be created. Event subscription names must be between 3 and 100 characters in length and use alphanumeric letters only.
    :param str partner_topic_name: Name of the partner topic.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    """
    __args__ = dict()
    __args__['eventSubscriptionName'] = event_subscription_name
    __args__['partnerTopicName'] = partner_topic_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:eventgrid/v20230601preview:getPartnerTopicEventSubscriptionDeliveryAttributes', __args__, opts=opts, typ=GetPartnerTopicEventSubscriptionDeliveryAttributesResult).value

    return AwaitableGetPartnerTopicEventSubscriptionDeliveryAttributesResult(
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(get_partner_topic_event_subscription_delivery_attributes)
def get_partner_topic_event_subscription_delivery_attributes_output(event_subscription_name: Optional[pulumi.Input[str]] = None,
                                                                    partner_topic_name: Optional[pulumi.Input[str]] = None,
                                                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPartnerTopicEventSubscriptionDeliveryAttributesResult]:
    """
    Get all delivery attributes for an event subscription of a partner topic.


    :param str event_subscription_name: Name of the event subscription to be created. Event subscription names must be between 3 and 100 characters in length and use alphanumeric letters only.
    :param str partner_topic_name: Name of the partner topic.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    """
    ...
