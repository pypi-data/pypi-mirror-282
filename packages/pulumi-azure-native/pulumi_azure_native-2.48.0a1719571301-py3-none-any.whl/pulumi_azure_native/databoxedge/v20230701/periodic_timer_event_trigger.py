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

__all__ = ['PeriodicTimerEventTriggerArgs', 'PeriodicTimerEventTrigger']

@pulumi.input_type
class PeriodicTimerEventTriggerArgs:
    def __init__(__self__, *,
                 device_name: pulumi.Input[str],
                 kind: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 sink_info: pulumi.Input['RoleSinkInfoArgs'],
                 source_info: pulumi.Input['PeriodicTimerSourceInfoArgs'],
                 custom_context_tag: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PeriodicTimerEventTrigger resource.
        :param pulumi.Input[str] device_name: Creates or updates a trigger
        :param pulumi.Input[str] kind: Trigger Kind.
               Expected value is 'PeriodicTimerEvent'.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input['RoleSinkInfoArgs'] sink_info: Role Sink information.
        :param pulumi.Input['PeriodicTimerSourceInfoArgs'] source_info: Periodic timer details.
        :param pulumi.Input[str] custom_context_tag: A custom context tag typically used to correlate the trigger against its usage. For example, if a periodic timer trigger is intended for certain specific IoT modules in the device, the tag can be the name or the image URL of the module.
        :param pulumi.Input[str] name: The trigger name.
        """
        pulumi.set(__self__, "device_name", device_name)
        pulumi.set(__self__, "kind", 'PeriodicTimerEvent')
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sink_info", sink_info)
        pulumi.set(__self__, "source_info", source_info)
        if custom_context_tag is not None:
            pulumi.set(__self__, "custom_context_tag", custom_context_tag)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[str]:
        """
        Creates or updates a trigger
        """
        return pulumi.get(self, "device_name")

    @device_name.setter
    def device_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "device_name", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        Trigger Kind.
        Expected value is 'PeriodicTimerEvent'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="sinkInfo")
    def sink_info(self) -> pulumi.Input['RoleSinkInfoArgs']:
        """
        Role Sink information.
        """
        return pulumi.get(self, "sink_info")

    @sink_info.setter
    def sink_info(self, value: pulumi.Input['RoleSinkInfoArgs']):
        pulumi.set(self, "sink_info", value)

    @property
    @pulumi.getter(name="sourceInfo")
    def source_info(self) -> pulumi.Input['PeriodicTimerSourceInfoArgs']:
        """
        Periodic timer details.
        """
        return pulumi.get(self, "source_info")

    @source_info.setter
    def source_info(self, value: pulumi.Input['PeriodicTimerSourceInfoArgs']):
        pulumi.set(self, "source_info", value)

    @property
    @pulumi.getter(name="customContextTag")
    def custom_context_tag(self) -> Optional[pulumi.Input[str]]:
        """
        A custom context tag typically used to correlate the trigger against its usage. For example, if a periodic timer trigger is intended for certain specific IoT modules in the device, the tag can be the name or the image URL of the module.
        """
        return pulumi.get(self, "custom_context_tag")

    @custom_context_tag.setter
    def custom_context_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_context_tag", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The trigger name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class PeriodicTimerEventTrigger(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_context_tag: Optional[pulumi.Input[str]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sink_info: Optional[pulumi.Input[pulumi.InputType['RoleSinkInfoArgs']]] = None,
                 source_info: Optional[pulumi.Input[pulumi.InputType['PeriodicTimerSourceInfoArgs']]] = None,
                 __props__=None):
        """
        Trigger details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] custom_context_tag: A custom context tag typically used to correlate the trigger against its usage. For example, if a periodic timer trigger is intended for certain specific IoT modules in the device, the tag can be the name or the image URL of the module.
        :param pulumi.Input[str] device_name: Creates or updates a trigger
        :param pulumi.Input[str] kind: Trigger Kind.
               Expected value is 'PeriodicTimerEvent'.
        :param pulumi.Input[str] name: The trigger name.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[pulumi.InputType['RoleSinkInfoArgs']] sink_info: Role Sink information.
        :param pulumi.Input[pulumi.InputType['PeriodicTimerSourceInfoArgs']] source_info: Periodic timer details.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PeriodicTimerEventTriggerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Trigger details.

        :param str resource_name: The name of the resource.
        :param PeriodicTimerEventTriggerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PeriodicTimerEventTriggerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_context_tag: Optional[pulumi.Input[str]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sink_info: Optional[pulumi.Input[pulumi.InputType['RoleSinkInfoArgs']]] = None,
                 source_info: Optional[pulumi.Input[pulumi.InputType['PeriodicTimerSourceInfoArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PeriodicTimerEventTriggerArgs.__new__(PeriodicTimerEventTriggerArgs)

            __props__.__dict__["custom_context_tag"] = custom_context_tag
            if device_name is None and not opts.urn:
                raise TypeError("Missing required property 'device_name'")
            __props__.__dict__["device_name"] = device_name
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'PeriodicTimerEvent'
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sink_info is None and not opts.urn:
                raise TypeError("Missing required property 'sink_info'")
            __props__.__dict__["sink_info"] = sink_info
            if source_info is None and not opts.urn:
                raise TypeError("Missing required property 'source_info'")
            __props__.__dict__["source_info"] = source_info
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:databoxedge:PeriodicTimerEventTrigger"), pulumi.Alias(type_="azure-native:databoxedge/v20190301:PeriodicTimerEventTrigger"), pulumi.Alias(type_="azure-native:databoxedge/v20190701:PeriodicTimerEventTrigger"), pulumi.Alias(type_="azure-native:databoxedge/v20190801:PeriodicTimerEventTrigger"), pulumi.Alias(type_="azure-native:databoxedge/v20200501preview:PeriodicTimerEventTrigger"), pulumi.Alias(type_="azure-native:databoxedge/v20200901:PeriodicTimerEventTrigger"), pulumi.Alias(type_="azure-native:databoxedge/v20200901preview:PeriodicTimerEventTrigger"), pulumi.Alias(type_="azure-native:databoxedge/v20201201:PeriodicTimerEventTrigger"), pulumi.Alias(type_="azure-native:databoxedge/v20210201:PeriodicTimerEventTrigger"), pulumi.Alias(type_="azure-native:databoxedge/v20210201preview:PeriodicTimerEventTrigger"), pulumi.Alias(type_="azure-native:databoxedge/v20210601:PeriodicTimerEventTrigger"), pulumi.Alias(type_="azure-native:databoxedge/v20210601preview:PeriodicTimerEventTrigger"), pulumi.Alias(type_="azure-native:databoxedge/v20220301:PeriodicTimerEventTrigger"), pulumi.Alias(type_="azure-native:databoxedge/v20220401preview:PeriodicTimerEventTrigger"), pulumi.Alias(type_="azure-native:databoxedge/v20221201preview:PeriodicTimerEventTrigger"), pulumi.Alias(type_="azure-native:databoxedge/v20230101preview:PeriodicTimerEventTrigger"), pulumi.Alias(type_="azure-native:databoxedge/v20231201:PeriodicTimerEventTrigger")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PeriodicTimerEventTrigger, __self__).__init__(
            'azure-native:databoxedge/v20230701:PeriodicTimerEventTrigger',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PeriodicTimerEventTrigger':
        """
        Get an existing PeriodicTimerEventTrigger resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PeriodicTimerEventTriggerArgs.__new__(PeriodicTimerEventTriggerArgs)

        __props__.__dict__["custom_context_tag"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["sink_info"] = None
        __props__.__dict__["source_info"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return PeriodicTimerEventTrigger(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customContextTag")
    def custom_context_tag(self) -> pulumi.Output[Optional[str]]:
        """
        A custom context tag typically used to correlate the trigger against its usage. For example, if a periodic timer trigger is intended for certain specific IoT modules in the device, the tag can be the name or the image URL of the module.
        """
        return pulumi.get(self, "custom_context_tag")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Trigger Kind.
        Expected value is 'PeriodicTimerEvent'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The object name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sinkInfo")
    def sink_info(self) -> pulumi.Output['outputs.RoleSinkInfoResponse']:
        """
        Role Sink information.
        """
        return pulumi.get(self, "sink_info")

    @property
    @pulumi.getter(name="sourceInfo")
    def source_info(self) -> pulumi.Output['outputs.PeriodicTimerSourceInfoResponse']:
        """
        Periodic timer details.
        """
        return pulumi.get(self, "source_info")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of Trigger
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")

