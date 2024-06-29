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
    'GetNamespaceTopicEventSubscriptionResult',
    'AwaitableGetNamespaceTopicEventSubscriptionResult',
    'get_namespace_topic_event_subscription',
    'get_namespace_topic_event_subscription_output',
]

@pulumi.output_type
class GetNamespaceTopicEventSubscriptionResult:
    """
    Event Subscription.
    """
    def __init__(__self__, delivery_configuration=None, event_delivery_schema=None, filters_configuration=None, id=None, name=None, provisioning_state=None, system_data=None, type=None):
        if delivery_configuration and not isinstance(delivery_configuration, dict):
            raise TypeError("Expected argument 'delivery_configuration' to be a dict")
        pulumi.set(__self__, "delivery_configuration", delivery_configuration)
        if event_delivery_schema and not isinstance(event_delivery_schema, str):
            raise TypeError("Expected argument 'event_delivery_schema' to be a str")
        pulumi.set(__self__, "event_delivery_schema", event_delivery_schema)
        if filters_configuration and not isinstance(filters_configuration, dict):
            raise TypeError("Expected argument 'filters_configuration' to be a dict")
        pulumi.set(__self__, "filters_configuration", filters_configuration)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="deliveryConfiguration")
    def delivery_configuration(self) -> Optional['outputs.DeliveryConfigurationResponse']:
        """
        Information about the delivery configuration of the event subscription.
        """
        return pulumi.get(self, "delivery_configuration")

    @property
    @pulumi.getter(name="eventDeliverySchema")
    def event_delivery_schema(self) -> Optional[str]:
        """
        The event delivery schema for the event subscription.
        """
        return pulumi.get(self, "event_delivery_schema")

    @property
    @pulumi.getter(name="filtersConfiguration")
    def filters_configuration(self) -> Optional['outputs.FiltersConfigurationResponse']:
        """
        Information about the filter for the event subscription.
        """
        return pulumi.get(self, "filters_configuration")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified identifier of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the event subscription.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to Event Subscription resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetNamespaceTopicEventSubscriptionResult(GetNamespaceTopicEventSubscriptionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNamespaceTopicEventSubscriptionResult(
            delivery_configuration=self.delivery_configuration,
            event_delivery_schema=self.event_delivery_schema,
            filters_configuration=self.filters_configuration,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_namespace_topic_event_subscription(event_subscription_name: Optional[str] = None,
                                           namespace_name: Optional[str] = None,
                                           resource_group_name: Optional[str] = None,
                                           topic_name: Optional[str] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNamespaceTopicEventSubscriptionResult:
    """
    Get properties of an event subscription of a namespace topic.
    Azure REST API version: 2023-06-01-preview.

    Other available API versions: 2023-12-15-preview, 2024-06-01-preview.


    :param str event_subscription_name: Name of the event subscription to be created. Event subscription names must be between 3 and 100 characters in length and use alphanumeric letters only.
    :param str namespace_name: Name of the namespace.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    :param str topic_name: Name of the namespace topic.
    """
    __args__ = dict()
    __args__['eventSubscriptionName'] = event_subscription_name
    __args__['namespaceName'] = namespace_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['topicName'] = topic_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:eventgrid:getNamespaceTopicEventSubscription', __args__, opts=opts, typ=GetNamespaceTopicEventSubscriptionResult).value

    return AwaitableGetNamespaceTopicEventSubscriptionResult(
        delivery_configuration=pulumi.get(__ret__, 'delivery_configuration'),
        event_delivery_schema=pulumi.get(__ret__, 'event_delivery_schema'),
        filters_configuration=pulumi.get(__ret__, 'filters_configuration'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_namespace_topic_event_subscription)
def get_namespace_topic_event_subscription_output(event_subscription_name: Optional[pulumi.Input[str]] = None,
                                                  namespace_name: Optional[pulumi.Input[str]] = None,
                                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                                  topic_name: Optional[pulumi.Input[str]] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNamespaceTopicEventSubscriptionResult]:
    """
    Get properties of an event subscription of a namespace topic.
    Azure REST API version: 2023-06-01-preview.

    Other available API versions: 2023-12-15-preview, 2024-06-01-preview.


    :param str event_subscription_name: Name of the event subscription to be created. Event subscription names must be between 3 and 100 characters in length and use alphanumeric letters only.
    :param str namespace_name: Name of the namespace.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    :param str topic_name: Name of the namespace topic.
    """
    ...
