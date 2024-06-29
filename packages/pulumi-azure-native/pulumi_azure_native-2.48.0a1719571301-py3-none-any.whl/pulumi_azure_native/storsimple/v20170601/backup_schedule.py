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

__all__ = ['BackupScheduleArgs', 'BackupSchedule']

@pulumi.input_type
class BackupScheduleArgs:
    def __init__(__self__, *,
                 backup_policy_name: pulumi.Input[str],
                 backup_type: pulumi.Input['BackupType'],
                 device_name: pulumi.Input[str],
                 manager_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 retention_count: pulumi.Input[float],
                 schedule_recurrence: pulumi.Input['ScheduleRecurrenceArgs'],
                 schedule_status: pulumi.Input['ScheduleStatus'],
                 start_time: pulumi.Input[str],
                 backup_schedule_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input['Kind']] = None):
        """
        The set of arguments for constructing a BackupSchedule resource.
        :param pulumi.Input[str] backup_policy_name: The backup policy name.
        :param pulumi.Input['BackupType'] backup_type: The type of backup which needs to be taken.
        :param pulumi.Input[str] device_name: The device name
        :param pulumi.Input[str] manager_name: The manager name
        :param pulumi.Input[str] resource_group_name: The resource group name
        :param pulumi.Input[float] retention_count: The number of backups to be retained.
        :param pulumi.Input['ScheduleRecurrenceArgs'] schedule_recurrence: The schedule recurrence.
        :param pulumi.Input['ScheduleStatus'] schedule_status: The schedule status.
        :param pulumi.Input[str] start_time: The start time of the schedule.
        :param pulumi.Input[str] backup_schedule_name: The backup schedule name.
        :param pulumi.Input['Kind'] kind: The Kind of the object. Currently only Series8000 is supported
        """
        pulumi.set(__self__, "backup_policy_name", backup_policy_name)
        pulumi.set(__self__, "backup_type", backup_type)
        pulumi.set(__self__, "device_name", device_name)
        pulumi.set(__self__, "manager_name", manager_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "retention_count", retention_count)
        pulumi.set(__self__, "schedule_recurrence", schedule_recurrence)
        pulumi.set(__self__, "schedule_status", schedule_status)
        pulumi.set(__self__, "start_time", start_time)
        if backup_schedule_name is not None:
            pulumi.set(__self__, "backup_schedule_name", backup_schedule_name)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)

    @property
    @pulumi.getter(name="backupPolicyName")
    def backup_policy_name(self) -> pulumi.Input[str]:
        """
        The backup policy name.
        """
        return pulumi.get(self, "backup_policy_name")

    @backup_policy_name.setter
    def backup_policy_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "backup_policy_name", value)

    @property
    @pulumi.getter(name="backupType")
    def backup_type(self) -> pulumi.Input['BackupType']:
        """
        The type of backup which needs to be taken.
        """
        return pulumi.get(self, "backup_type")

    @backup_type.setter
    def backup_type(self, value: pulumi.Input['BackupType']):
        pulumi.set(self, "backup_type", value)

    @property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[str]:
        """
        The device name
        """
        return pulumi.get(self, "device_name")

    @device_name.setter
    def device_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "device_name", value)

    @property
    @pulumi.getter(name="managerName")
    def manager_name(self) -> pulumi.Input[str]:
        """
        The manager name
        """
        return pulumi.get(self, "manager_name")

    @manager_name.setter
    def manager_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "manager_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="retentionCount")
    def retention_count(self) -> pulumi.Input[float]:
        """
        The number of backups to be retained.
        """
        return pulumi.get(self, "retention_count")

    @retention_count.setter
    def retention_count(self, value: pulumi.Input[float]):
        pulumi.set(self, "retention_count", value)

    @property
    @pulumi.getter(name="scheduleRecurrence")
    def schedule_recurrence(self) -> pulumi.Input['ScheduleRecurrenceArgs']:
        """
        The schedule recurrence.
        """
        return pulumi.get(self, "schedule_recurrence")

    @schedule_recurrence.setter
    def schedule_recurrence(self, value: pulumi.Input['ScheduleRecurrenceArgs']):
        pulumi.set(self, "schedule_recurrence", value)

    @property
    @pulumi.getter(name="scheduleStatus")
    def schedule_status(self) -> pulumi.Input['ScheduleStatus']:
        """
        The schedule status.
        """
        return pulumi.get(self, "schedule_status")

    @schedule_status.setter
    def schedule_status(self, value: pulumi.Input['ScheduleStatus']):
        pulumi.set(self, "schedule_status", value)

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Input[str]:
        """
        The start time of the schedule.
        """
        return pulumi.get(self, "start_time")

    @start_time.setter
    def start_time(self, value: pulumi.Input[str]):
        pulumi.set(self, "start_time", value)

    @property
    @pulumi.getter(name="backupScheduleName")
    def backup_schedule_name(self) -> Optional[pulumi.Input[str]]:
        """
        The backup schedule name.
        """
        return pulumi.get(self, "backup_schedule_name")

    @backup_schedule_name.setter
    def backup_schedule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "backup_schedule_name", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input['Kind']]:
        """
        The Kind of the object. Currently only Series8000 is supported
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input['Kind']]):
        pulumi.set(self, "kind", value)


class BackupSchedule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backup_policy_name: Optional[pulumi.Input[str]] = None,
                 backup_schedule_name: Optional[pulumi.Input[str]] = None,
                 backup_type: Optional[pulumi.Input['BackupType']] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input['Kind']] = None,
                 manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 retention_count: Optional[pulumi.Input[float]] = None,
                 schedule_recurrence: Optional[pulumi.Input[pulumi.InputType['ScheduleRecurrenceArgs']]] = None,
                 schedule_status: Optional[pulumi.Input['ScheduleStatus']] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The backup schedule.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backup_policy_name: The backup policy name.
        :param pulumi.Input[str] backup_schedule_name: The backup schedule name.
        :param pulumi.Input['BackupType'] backup_type: The type of backup which needs to be taken.
        :param pulumi.Input[str] device_name: The device name
        :param pulumi.Input['Kind'] kind: The Kind of the object. Currently only Series8000 is supported
        :param pulumi.Input[str] manager_name: The manager name
        :param pulumi.Input[str] resource_group_name: The resource group name
        :param pulumi.Input[float] retention_count: The number of backups to be retained.
        :param pulumi.Input[pulumi.InputType['ScheduleRecurrenceArgs']] schedule_recurrence: The schedule recurrence.
        :param pulumi.Input['ScheduleStatus'] schedule_status: The schedule status.
        :param pulumi.Input[str] start_time: The start time of the schedule.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BackupScheduleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The backup schedule.

        :param str resource_name: The name of the resource.
        :param BackupScheduleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BackupScheduleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backup_policy_name: Optional[pulumi.Input[str]] = None,
                 backup_schedule_name: Optional[pulumi.Input[str]] = None,
                 backup_type: Optional[pulumi.Input['BackupType']] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input['Kind']] = None,
                 manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 retention_count: Optional[pulumi.Input[float]] = None,
                 schedule_recurrence: Optional[pulumi.Input[pulumi.InputType['ScheduleRecurrenceArgs']]] = None,
                 schedule_status: Optional[pulumi.Input['ScheduleStatus']] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BackupScheduleArgs.__new__(BackupScheduleArgs)

            if backup_policy_name is None and not opts.urn:
                raise TypeError("Missing required property 'backup_policy_name'")
            __props__.__dict__["backup_policy_name"] = backup_policy_name
            __props__.__dict__["backup_schedule_name"] = backup_schedule_name
            if backup_type is None and not opts.urn:
                raise TypeError("Missing required property 'backup_type'")
            __props__.__dict__["backup_type"] = backup_type
            if device_name is None and not opts.urn:
                raise TypeError("Missing required property 'device_name'")
            __props__.__dict__["device_name"] = device_name
            __props__.__dict__["kind"] = kind
            if manager_name is None and not opts.urn:
                raise TypeError("Missing required property 'manager_name'")
            __props__.__dict__["manager_name"] = manager_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if retention_count is None and not opts.urn:
                raise TypeError("Missing required property 'retention_count'")
            __props__.__dict__["retention_count"] = retention_count
            if schedule_recurrence is None and not opts.urn:
                raise TypeError("Missing required property 'schedule_recurrence'")
            __props__.__dict__["schedule_recurrence"] = schedule_recurrence
            if schedule_status is None and not opts.urn:
                raise TypeError("Missing required property 'schedule_status'")
            __props__.__dict__["schedule_status"] = schedule_status
            if start_time is None and not opts.urn:
                raise TypeError("Missing required property 'start_time'")
            __props__.__dict__["start_time"] = start_time
            __props__.__dict__["last_successful_run"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:storsimple:BackupSchedule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(BackupSchedule, __self__).__init__(
            'azure-native:storsimple/v20170601:BackupSchedule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BackupSchedule':
        """
        Get an existing BackupSchedule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BackupScheduleArgs.__new__(BackupScheduleArgs)

        __props__.__dict__["backup_type"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["last_successful_run"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["retention_count"] = None
        __props__.__dict__["schedule_recurrence"] = None
        __props__.__dict__["schedule_status"] = None
        __props__.__dict__["start_time"] = None
        __props__.__dict__["type"] = None
        return BackupSchedule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backupType")
    def backup_type(self) -> pulumi.Output[str]:
        """
        The type of backup which needs to be taken.
        """
        return pulumi.get(self, "backup_type")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        The Kind of the object. Currently only Series8000 is supported
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="lastSuccessfulRun")
    def last_successful_run(self) -> pulumi.Output[str]:
        """
        The last successful backup run which was triggered for the schedule.
        """
        return pulumi.get(self, "last_successful_run")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the object.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="retentionCount")
    def retention_count(self) -> pulumi.Output[float]:
        """
        The number of backups to be retained.
        """
        return pulumi.get(self, "retention_count")

    @property
    @pulumi.getter(name="scheduleRecurrence")
    def schedule_recurrence(self) -> pulumi.Output['outputs.ScheduleRecurrenceResponse']:
        """
        The schedule recurrence.
        """
        return pulumi.get(self, "schedule_recurrence")

    @property
    @pulumi.getter(name="scheduleStatus")
    def schedule_status(self) -> pulumi.Output[str]:
        """
        The schedule status.
        """
        return pulumi.get(self, "schedule_status")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[str]:
        """
        The start time of the schedule.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")

