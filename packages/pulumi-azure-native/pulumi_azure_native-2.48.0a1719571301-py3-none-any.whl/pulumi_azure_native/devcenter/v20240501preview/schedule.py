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
from ._enums import *

__all__ = ['ScheduleArgs', 'Schedule']

@pulumi.input_type
class ScheduleArgs:
    def __init__(__self__, *,
                 frequency: pulumi.Input[Union[str, 'ScheduledFrequency']],
                 pool_name: pulumi.Input[str],
                 project_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 time: pulumi.Input[str],
                 time_zone: pulumi.Input[str],
                 type: pulumi.Input[Union[str, 'ScheduledType']],
                 location: Optional[pulumi.Input[str]] = None,
                 schedule_name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'ScheduleEnableStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 top: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Schedule resource.
        :param pulumi.Input[Union[str, 'ScheduledFrequency']] frequency: The frequency of this scheduled task.
        :param pulumi.Input[str] pool_name: Name of the pool.
        :param pulumi.Input[str] project_name: The name of the project.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] time: The target time to trigger the action. The format is HH:MM.
        :param pulumi.Input[str] time_zone: The IANA timezone id at which the schedule should execute.
        :param pulumi.Input[Union[str, 'ScheduledType']] type: Supported type this scheduled task represents.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] schedule_name: The name of the schedule that uniquely identifies it.
        :param pulumi.Input[Union[str, 'ScheduleEnableStatus']] state: Indicates whether or not this scheduled task is enabled.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[int] top: The maximum number of resources to return from the operation. Example: '$top=10'.
        """
        pulumi.set(__self__, "frequency", frequency)
        pulumi.set(__self__, "pool_name", pool_name)
        pulumi.set(__self__, "project_name", project_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "time", time)
        pulumi.set(__self__, "time_zone", time_zone)
        pulumi.set(__self__, "type", type)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if schedule_name is not None:
            pulumi.set(__self__, "schedule_name", schedule_name)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if top is not None:
            pulumi.set(__self__, "top", top)

    @property
    @pulumi.getter
    def frequency(self) -> pulumi.Input[Union[str, 'ScheduledFrequency']]:
        """
        The frequency of this scheduled task.
        """
        return pulumi.get(self, "frequency")

    @frequency.setter
    def frequency(self, value: pulumi.Input[Union[str, 'ScheduledFrequency']]):
        pulumi.set(self, "frequency", value)

    @property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> pulumi.Input[str]:
        """
        Name of the pool.
        """
        return pulumi.get(self, "pool_name")

    @pool_name.setter
    def pool_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "pool_name", value)

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Input[str]:
        """
        The name of the project.
        """
        return pulumi.get(self, "project_name")

    @project_name.setter
    def project_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_name", value)

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
    @pulumi.getter
    def time(self) -> pulumi.Input[str]:
        """
        The target time to trigger the action. The format is HH:MM.
        """
        return pulumi.get(self, "time")

    @time.setter
    def time(self, value: pulumi.Input[str]):
        pulumi.set(self, "time", value)

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Input[str]:
        """
        The IANA timezone id at which the schedule should execute.
        """
        return pulumi.get(self, "time_zone")

    @time_zone.setter
    def time_zone(self, value: pulumi.Input[str]):
        pulumi.set(self, "time_zone", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[str, 'ScheduledType']]:
        """
        Supported type this scheduled task represents.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[Union[str, 'ScheduledType']]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="scheduleName")
    def schedule_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the schedule that uniquely identifies it.
        """
        return pulumi.get(self, "schedule_name")

    @schedule_name.setter
    def schedule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schedule_name", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[str, 'ScheduleEnableStatus']]]:
        """
        Indicates whether or not this scheduled task is enabled.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[str, 'ScheduleEnableStatus']]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def top(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum number of resources to return from the operation. Example: '$top=10'.
        """
        return pulumi.get(self, "top")

    @top.setter
    def top(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "top", value)


class Schedule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 frequency: Optional[pulumi.Input[Union[str, 'ScheduledFrequency']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schedule_name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'ScheduleEnableStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 time: Optional[pulumi.Input[str]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
                 top: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[Union[str, 'ScheduledType']]] = None,
                 __props__=None):
        """
        Represents a Schedule to execute a task.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'ScheduledFrequency']] frequency: The frequency of this scheduled task.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] pool_name: Name of the pool.
        :param pulumi.Input[str] project_name: The name of the project.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] schedule_name: The name of the schedule that uniquely identifies it.
        :param pulumi.Input[Union[str, 'ScheduleEnableStatus']] state: Indicates whether or not this scheduled task is enabled.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] time: The target time to trigger the action. The format is HH:MM.
        :param pulumi.Input[str] time_zone: The IANA timezone id at which the schedule should execute.
        :param pulumi.Input[int] top: The maximum number of resources to return from the operation. Example: '$top=10'.
        :param pulumi.Input[Union[str, 'ScheduledType']] type: Supported type this scheduled task represents.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScheduleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a Schedule to execute a task.

        :param str resource_name: The name of the resource.
        :param ScheduleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScheduleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 frequency: Optional[pulumi.Input[Union[str, 'ScheduledFrequency']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schedule_name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'ScheduleEnableStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 time: Optional[pulumi.Input[str]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
                 top: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[Union[str, 'ScheduledType']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ScheduleArgs.__new__(ScheduleArgs)

            if frequency is None and not opts.urn:
                raise TypeError("Missing required property 'frequency'")
            __props__.__dict__["frequency"] = frequency
            __props__.__dict__["location"] = location
            if pool_name is None and not opts.urn:
                raise TypeError("Missing required property 'pool_name'")
            __props__.__dict__["pool_name"] = pool_name
            if project_name is None and not opts.urn:
                raise TypeError("Missing required property 'project_name'")
            __props__.__dict__["project_name"] = project_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["schedule_name"] = schedule_name
            __props__.__dict__["state"] = state
            __props__.__dict__["tags"] = tags
            if time is None and not opts.urn:
                raise TypeError("Missing required property 'time'")
            __props__.__dict__["time"] = time
            if time_zone is None and not opts.urn:
                raise TypeError("Missing required property 'time_zone'")
            __props__.__dict__["time_zone"] = time_zone
            __props__.__dict__["top"] = top
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:devcenter:Schedule"), pulumi.Alias(type_="azure-native:devcenter/v20220801preview:Schedule"), pulumi.Alias(type_="azure-native:devcenter/v20220901preview:Schedule"), pulumi.Alias(type_="azure-native:devcenter/v20221012preview:Schedule"), pulumi.Alias(type_="azure-native:devcenter/v20221111preview:Schedule"), pulumi.Alias(type_="azure-native:devcenter/v20230101preview:Schedule"), pulumi.Alias(type_="azure-native:devcenter/v20230401:Schedule"), pulumi.Alias(type_="azure-native:devcenter/v20230801preview:Schedule"), pulumi.Alias(type_="azure-native:devcenter/v20231001preview:Schedule"), pulumi.Alias(type_="azure-native:devcenter/v20240201:Schedule"), pulumi.Alias(type_="azure-native:devcenter/v20240601preview:Schedule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Schedule, __self__).__init__(
            'azure-native:devcenter/v20240501preview:Schedule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Schedule':
        """
        Get an existing Schedule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ScheduleArgs.__new__(ScheduleArgs)

        __props__.__dict__["frequency"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["time"] = None
        __props__.__dict__["time_zone"] = None
        __props__.__dict__["type"] = None
        return Schedule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def frequency(self) -> pulumi.Output[str]:
        """
        The frequency of this scheduled task.
        """
        return pulumi.get(self, "frequency")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[str]]:
        """
        Indicates whether or not this scheduled task is enabled.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def time(self) -> pulumi.Output[str]:
        """
        The target time to trigger the action. The format is HH:MM.
        """
        return pulumi.get(self, "time")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[str]:
        """
        The IANA timezone id at which the schedule should execute.
        """
        return pulumi.get(self, "time_zone")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

