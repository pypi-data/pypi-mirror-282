# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['AccessControlRecordArgs', 'AccessControlRecord']

@pulumi.input_type
class AccessControlRecordArgs:
    def __init__(__self__, *,
                 initiator_name: pulumi.Input[str],
                 manager_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 access_control_record_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input['Kind']] = None):
        """
        The set of arguments for constructing a AccessControlRecord resource.
        :param pulumi.Input[str] initiator_name: The iSCSI initiator name (IQN).
        :param pulumi.Input[str] manager_name: The manager name
        :param pulumi.Input[str] resource_group_name: The resource group name
        :param pulumi.Input[str] access_control_record_name: The name of the access control record.
        :param pulumi.Input['Kind'] kind: The Kind of the object. Currently only Series8000 is supported
        """
        pulumi.set(__self__, "initiator_name", initiator_name)
        pulumi.set(__self__, "manager_name", manager_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if access_control_record_name is not None:
            pulumi.set(__self__, "access_control_record_name", access_control_record_name)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)

    @property
    @pulumi.getter(name="initiatorName")
    def initiator_name(self) -> pulumi.Input[str]:
        """
        The iSCSI initiator name (IQN).
        """
        return pulumi.get(self, "initiator_name")

    @initiator_name.setter
    def initiator_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "initiator_name", value)

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
    @pulumi.getter(name="accessControlRecordName")
    def access_control_record_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the access control record.
        """
        return pulumi.get(self, "access_control_record_name")

    @access_control_record_name.setter
    def access_control_record_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_control_record_name", value)

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


class AccessControlRecord(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_control_record_name: Optional[pulumi.Input[str]] = None,
                 initiator_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input['Kind']] = None,
                 manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The access control record.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_control_record_name: The name of the access control record.
        :param pulumi.Input[str] initiator_name: The iSCSI initiator name (IQN).
        :param pulumi.Input['Kind'] kind: The Kind of the object. Currently only Series8000 is supported
        :param pulumi.Input[str] manager_name: The manager name
        :param pulumi.Input[str] resource_group_name: The resource group name
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccessControlRecordArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The access control record.

        :param str resource_name: The name of the resource.
        :param AccessControlRecordArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccessControlRecordArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_control_record_name: Optional[pulumi.Input[str]] = None,
                 initiator_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input['Kind']] = None,
                 manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccessControlRecordArgs.__new__(AccessControlRecordArgs)

            __props__.__dict__["access_control_record_name"] = access_control_record_name
            if initiator_name is None and not opts.urn:
                raise TypeError("Missing required property 'initiator_name'")
            __props__.__dict__["initiator_name"] = initiator_name
            __props__.__dict__["kind"] = kind
            if manager_name is None and not opts.urn:
                raise TypeError("Missing required property 'manager_name'")
            __props__.__dict__["manager_name"] = manager_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["volume_count"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:storsimple:AccessControlRecord"), pulumi.Alias(type_="azure-native:storsimple/v20161001:AccessControlRecord")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AccessControlRecord, __self__).__init__(
            'azure-native:storsimple/v20170601:AccessControlRecord',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AccessControlRecord':
        """
        Get an existing AccessControlRecord resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AccessControlRecordArgs.__new__(AccessControlRecordArgs)

        __props__.__dict__["initiator_name"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["volume_count"] = None
        return AccessControlRecord(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="initiatorName")
    def initiator_name(self) -> pulumi.Output[str]:
        """
        The iSCSI initiator name (IQN).
        """
        return pulumi.get(self, "initiator_name")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        The Kind of the object. Currently only Series8000 is supported
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the object.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="volumeCount")
    def volume_count(self) -> pulumi.Output[int]:
        """
        The number of volumes using the access control record.
        """
        return pulumi.get(self, "volume_count")

