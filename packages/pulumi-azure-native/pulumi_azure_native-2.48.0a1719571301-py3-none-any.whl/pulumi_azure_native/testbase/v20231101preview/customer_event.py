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
from ._inputs import *

__all__ = ['CustomerEventArgs', 'CustomerEvent']

@pulumi.input_type
class CustomerEventArgs:
    def __init__(__self__, *,
                 event_name: pulumi.Input[str],
                 receivers: pulumi.Input[Sequence[pulumi.Input['NotificationEventReceiverArgs']]],
                 resource_group_name: pulumi.Input[str],
                 test_base_account_name: pulumi.Input[str],
                 customer_event_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CustomerEvent resource.
        :param pulumi.Input[str] event_name: The name of the event subscribed to.
        :param pulumi.Input[Sequence[pulumi.Input['NotificationEventReceiverArgs']]] receivers: The notification event receivers.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] test_base_account_name: The resource name of the Test Base Account.
        :param pulumi.Input[str] customer_event_name: The resource name of the Test Base Customer event.
        """
        pulumi.set(__self__, "event_name", event_name)
        pulumi.set(__self__, "receivers", receivers)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "test_base_account_name", test_base_account_name)
        if customer_event_name is not None:
            pulumi.set(__self__, "customer_event_name", customer_event_name)

    @property
    @pulumi.getter(name="eventName")
    def event_name(self) -> pulumi.Input[str]:
        """
        The name of the event subscribed to.
        """
        return pulumi.get(self, "event_name")

    @event_name.setter
    def event_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "event_name", value)

    @property
    @pulumi.getter
    def receivers(self) -> pulumi.Input[Sequence[pulumi.Input['NotificationEventReceiverArgs']]]:
        """
        The notification event receivers.
        """
        return pulumi.get(self, "receivers")

    @receivers.setter
    def receivers(self, value: pulumi.Input[Sequence[pulumi.Input['NotificationEventReceiverArgs']]]):
        pulumi.set(self, "receivers", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="testBaseAccountName")
    def test_base_account_name(self) -> pulumi.Input[str]:
        """
        The resource name of the Test Base Account.
        """
        return pulumi.get(self, "test_base_account_name")

    @test_base_account_name.setter
    def test_base_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "test_base_account_name", value)

    @property
    @pulumi.getter(name="customerEventName")
    def customer_event_name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name of the Test Base Customer event.
        """
        return pulumi.get(self, "customer_event_name")

    @customer_event_name.setter
    def customer_event_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "customer_event_name", value)


class CustomerEvent(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 customer_event_name: Optional[pulumi.Input[str]] = None,
                 event_name: Optional[pulumi.Input[str]] = None,
                 receivers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationEventReceiverArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 test_base_account_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The Customer Notification Event resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] customer_event_name: The resource name of the Test Base Customer event.
        :param pulumi.Input[str] event_name: The name of the event subscribed to.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationEventReceiverArgs']]]] receivers: The notification event receivers.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] test_base_account_name: The resource name of the Test Base Account.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CustomerEventArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Customer Notification Event resource.

        :param str resource_name: The name of the resource.
        :param CustomerEventArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomerEventArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 customer_event_name: Optional[pulumi.Input[str]] = None,
                 event_name: Optional[pulumi.Input[str]] = None,
                 receivers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationEventReceiverArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 test_base_account_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CustomerEventArgs.__new__(CustomerEventArgs)

            __props__.__dict__["customer_event_name"] = customer_event_name
            if event_name is None and not opts.urn:
                raise TypeError("Missing required property 'event_name'")
            __props__.__dict__["event_name"] = event_name
            if receivers is None and not opts.urn:
                raise TypeError("Missing required property 'receivers'")
            __props__.__dict__["receivers"] = receivers
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if test_base_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'test_base_account_name'")
            __props__.__dict__["test_base_account_name"] = test_base_account_name
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:testbase:CustomerEvent"), pulumi.Alias(type_="azure-native:testbase/v20201216preview:CustomerEvent"), pulumi.Alias(type_="azure-native:testbase/v20220401preview:CustomerEvent")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CustomerEvent, __self__).__init__(
            'azure-native:testbase/v20231101preview:CustomerEvent',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CustomerEvent':
        """
        Get an existing CustomerEvent resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CustomerEventArgs.__new__(CustomerEventArgs)

        __props__.__dict__["event_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["receivers"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return CustomerEvent(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="eventName")
    def event_name(self) -> pulumi.Output[str]:
        """
        The name of the event subscribed to.
        """
        return pulumi.get(self, "event_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def receivers(self) -> pulumi.Output[Sequence['outputs.NotificationEventReceiverResponse']]:
        """
        The notification event receivers.
        """
        return pulumi.get(self, "receivers")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

