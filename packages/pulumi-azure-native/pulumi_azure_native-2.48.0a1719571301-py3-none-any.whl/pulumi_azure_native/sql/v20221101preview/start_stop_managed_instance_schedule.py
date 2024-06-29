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
from ._inputs import *

__all__ = ['StartStopManagedInstanceScheduleArgs', 'StartStopManagedInstanceSchedule']

@pulumi.input_type
class StartStopManagedInstanceScheduleArgs:
    def __init__(__self__, *,
                 managed_instance_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 schedule_list: pulumi.Input[Sequence[pulumi.Input['ScheduleItemArgs']]],
                 description: Optional[pulumi.Input[str]] = None,
                 start_stop_schedule_name: Optional[pulumi.Input[str]] = None,
                 time_zone_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a StartStopManagedInstanceSchedule resource.
        :param pulumi.Input[str] managed_instance_name: The name of the managed instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[Sequence[pulumi.Input['ScheduleItemArgs']]] schedule_list: Schedule list.
        :param pulumi.Input[str] description: The description of the schedule.
        :param pulumi.Input[str] start_stop_schedule_name: Name of the managed instance Start/Stop schedule.
        :param pulumi.Input[str] time_zone_id: The time zone of the schedule.
        """
        pulumi.set(__self__, "managed_instance_name", managed_instance_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "schedule_list", schedule_list)
        if description is None:
            description = ''
        if description is not None:
            pulumi.set(__self__, "description", description)
        if start_stop_schedule_name is not None:
            pulumi.set(__self__, "start_stop_schedule_name", start_stop_schedule_name)
        if time_zone_id is None:
            time_zone_id = 'UTC'
        if time_zone_id is not None:
            pulumi.set(__self__, "time_zone_id", time_zone_id)

    @property
    @pulumi.getter(name="managedInstanceName")
    def managed_instance_name(self) -> pulumi.Input[str]:
        """
        The name of the managed instance.
        """
        return pulumi.get(self, "managed_instance_name")

    @managed_instance_name.setter
    def managed_instance_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "managed_instance_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="scheduleList")
    def schedule_list(self) -> pulumi.Input[Sequence[pulumi.Input['ScheduleItemArgs']]]:
        """
        Schedule list.
        """
        return pulumi.get(self, "schedule_list")

    @schedule_list.setter
    def schedule_list(self, value: pulumi.Input[Sequence[pulumi.Input['ScheduleItemArgs']]]):
        pulumi.set(self, "schedule_list", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the schedule.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="startStopScheduleName")
    def start_stop_schedule_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the managed instance Start/Stop schedule.
        """
        return pulumi.get(self, "start_stop_schedule_name")

    @start_stop_schedule_name.setter
    def start_stop_schedule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_stop_schedule_name", value)

    @property
    @pulumi.getter(name="timeZoneId")
    def time_zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The time zone of the schedule.
        """
        return pulumi.get(self, "time_zone_id")

    @time_zone_id.setter
    def time_zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_zone_id", value)


class StartStopManagedInstanceSchedule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 managed_instance_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schedule_list: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScheduleItemArgs']]]]] = None,
                 start_stop_schedule_name: Optional[pulumi.Input[str]] = None,
                 time_zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Managed instance's Start/Stop schedule.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the schedule.
        :param pulumi.Input[str] managed_instance_name: The name of the managed instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScheduleItemArgs']]]] schedule_list: Schedule list.
        :param pulumi.Input[str] start_stop_schedule_name: Name of the managed instance Start/Stop schedule.
        :param pulumi.Input[str] time_zone_id: The time zone of the schedule.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StartStopManagedInstanceScheduleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Managed instance's Start/Stop schedule.

        :param str resource_name: The name of the resource.
        :param StartStopManagedInstanceScheduleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StartStopManagedInstanceScheduleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 managed_instance_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schedule_list: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScheduleItemArgs']]]]] = None,
                 start_stop_schedule_name: Optional[pulumi.Input[str]] = None,
                 time_zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StartStopManagedInstanceScheduleArgs.__new__(StartStopManagedInstanceScheduleArgs)

            if description is None:
                description = ''
            __props__.__dict__["description"] = description
            if managed_instance_name is None and not opts.urn:
                raise TypeError("Missing required property 'managed_instance_name'")
            __props__.__dict__["managed_instance_name"] = managed_instance_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if schedule_list is None and not opts.urn:
                raise TypeError("Missing required property 'schedule_list'")
            __props__.__dict__["schedule_list"] = schedule_list
            __props__.__dict__["start_stop_schedule_name"] = start_stop_schedule_name
            if time_zone_id is None:
                time_zone_id = 'UTC'
            __props__.__dict__["time_zone_id"] = time_zone_id
            __props__.__dict__["name"] = None
            __props__.__dict__["next_execution_time"] = None
            __props__.__dict__["next_run_action"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:sql:StartStopManagedInstanceSchedule"), pulumi.Alias(type_="azure-native:sql/v20220801preview:StartStopManagedInstanceSchedule"), pulumi.Alias(type_="azure-native:sql/v20230201preview:StartStopManagedInstanceSchedule"), pulumi.Alias(type_="azure-native:sql/v20230501preview:StartStopManagedInstanceSchedule"), pulumi.Alias(type_="azure-native:sql/v20230801preview:StartStopManagedInstanceSchedule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(StartStopManagedInstanceSchedule, __self__).__init__(
            'azure-native:sql/v20221101preview:StartStopManagedInstanceSchedule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StartStopManagedInstanceSchedule':
        """
        Get an existing StartStopManagedInstanceSchedule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StartStopManagedInstanceScheduleArgs.__new__(StartStopManagedInstanceScheduleArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["next_execution_time"] = None
        __props__.__dict__["next_run_action"] = None
        __props__.__dict__["schedule_list"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["time_zone_id"] = None
        __props__.__dict__["type"] = None
        return StartStopManagedInstanceSchedule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the schedule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nextExecutionTime")
    def next_execution_time(self) -> pulumi.Output[str]:
        """
        Timestamp when the next action will be executed in the corresponding schedule time zone.
        """
        return pulumi.get(self, "next_execution_time")

    @property
    @pulumi.getter(name="nextRunAction")
    def next_run_action(self) -> pulumi.Output[str]:
        """
        Next action to be executed (Start or Stop)
        """
        return pulumi.get(self, "next_run_action")

    @property
    @pulumi.getter(name="scheduleList")
    def schedule_list(self) -> pulumi.Output[Sequence['outputs.ScheduleItemResponse']]:
        """
        Schedule list.
        """
        return pulumi.get(self, "schedule_list")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        System data of the scheduled resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="timeZoneId")
    def time_zone_id(self) -> pulumi.Output[Optional[str]]:
        """
        The time zone of the schedule.
        """
        return pulumi.get(self, "time_zone_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

