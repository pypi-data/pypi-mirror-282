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

__all__ = ['AutoScaleVCoreArgs', 'AutoScaleVCore']

@pulumi.input_type
class AutoScaleVCoreArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 sku: pulumi.Input['AutoScaleVCoreSkuArgs'],
                 capacity_limit: Optional[pulumi.Input[int]] = None,
                 capacity_object_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 system_data: Optional[pulumi.Input['SystemDataArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vcore_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AutoScaleVCore resource.
        :param pulumi.Input[str] resource_group_name: The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
        :param pulumi.Input['AutoScaleVCoreSkuArgs'] sku: The SKU of the auto scale v-core resource.
        :param pulumi.Input[int] capacity_limit: The maximum capacity of an auto scale v-core resource.
        :param pulumi.Input[str] capacity_object_id: The object ID of the capacity resource associated with the auto scale v-core resource.
        :param pulumi.Input[str] location: Location of the PowerBI Dedicated resource.
        :param pulumi.Input['SystemDataArgs'] system_data: Metadata pertaining to creation and last modification of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value pairs of additional resource provisioning properties.
        :param pulumi.Input[str] vcore_name: The name of the auto scale v-core. It must be a minimum of 3 characters, and a maximum of 63.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sku", sku)
        if capacity_limit is not None:
            pulumi.set(__self__, "capacity_limit", capacity_limit)
        if capacity_object_id is not None:
            pulumi.set(__self__, "capacity_object_id", capacity_object_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if system_data is not None:
            pulumi.set(__self__, "system_data", system_data)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vcore_name is not None:
            pulumi.set(__self__, "vcore_name", vcore_name)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Input['AutoScaleVCoreSkuArgs']:
        """
        The SKU of the auto scale v-core resource.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input['AutoScaleVCoreSkuArgs']):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="capacityLimit")
    def capacity_limit(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum capacity of an auto scale v-core resource.
        """
        return pulumi.get(self, "capacity_limit")

    @capacity_limit.setter
    def capacity_limit(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "capacity_limit", value)

    @property
    @pulumi.getter(name="capacityObjectId")
    def capacity_object_id(self) -> Optional[pulumi.Input[str]]:
        """
        The object ID of the capacity resource associated with the auto scale v-core resource.
        """
        return pulumi.get(self, "capacity_object_id")

    @capacity_object_id.setter
    def capacity_object_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "capacity_object_id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Location of the PowerBI Dedicated resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> Optional[pulumi.Input['SystemDataArgs']]:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @system_data.setter
    def system_data(self, value: Optional[pulumi.Input['SystemDataArgs']]):
        pulumi.set(self, "system_data", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value pairs of additional resource provisioning properties.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="vcoreName")
    def vcore_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the auto scale v-core. It must be a minimum of 3 characters, and a maximum of 63.
        """
        return pulumi.get(self, "vcore_name")

    @vcore_name.setter
    def vcore_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vcore_name", value)


class AutoScaleVCore(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capacity_limit: Optional[pulumi.Input[int]] = None,
                 capacity_object_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['AutoScaleVCoreSkuArgs']]] = None,
                 system_data: Optional[pulumi.Input[pulumi.InputType['SystemDataArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vcore_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents an instance of an auto scale v-core resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] capacity_limit: The maximum capacity of an auto scale v-core resource.
        :param pulumi.Input[str] capacity_object_id: The object ID of the capacity resource associated with the auto scale v-core resource.
        :param pulumi.Input[str] location: Location of the PowerBI Dedicated resource.
        :param pulumi.Input[str] resource_group_name: The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
        :param pulumi.Input[pulumi.InputType['AutoScaleVCoreSkuArgs']] sku: The SKU of the auto scale v-core resource.
        :param pulumi.Input[pulumi.InputType['SystemDataArgs']] system_data: Metadata pertaining to creation and last modification of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value pairs of additional resource provisioning properties.
        :param pulumi.Input[str] vcore_name: The name of the auto scale v-core. It must be a minimum of 3 characters, and a maximum of 63.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AutoScaleVCoreArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents an instance of an auto scale v-core resource.

        :param str resource_name: The name of the resource.
        :param AutoScaleVCoreArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AutoScaleVCoreArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capacity_limit: Optional[pulumi.Input[int]] = None,
                 capacity_object_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['AutoScaleVCoreSkuArgs']]] = None,
                 system_data: Optional[pulumi.Input[pulumi.InputType['SystemDataArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vcore_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AutoScaleVCoreArgs.__new__(AutoScaleVCoreArgs)

            __props__.__dict__["capacity_limit"] = capacity_limit
            __props__.__dict__["capacity_object_id"] = capacity_object_id
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__.__dict__["sku"] = sku
            __props__.__dict__["system_data"] = system_data
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vcore_name"] = vcore_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:powerbidedicated:AutoScaleVCore")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AutoScaleVCore, __self__).__init__(
            'azure-native:powerbidedicated/v20210101:AutoScaleVCore',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AutoScaleVCore':
        """
        Get an existing AutoScaleVCore resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AutoScaleVCoreArgs.__new__(AutoScaleVCoreArgs)

        __props__.__dict__["capacity_limit"] = None
        __props__.__dict__["capacity_object_id"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return AutoScaleVCore(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="capacityLimit")
    def capacity_limit(self) -> pulumi.Output[Optional[int]]:
        """
        The maximum capacity of an auto scale v-core resource.
        """
        return pulumi.get(self, "capacity_limit")

    @property
    @pulumi.getter(name="capacityObjectId")
    def capacity_object_id(self) -> pulumi.Output[Optional[str]]:
        """
        The object ID of the capacity resource associated with the auto scale v-core resource.
        """
        return pulumi.get(self, "capacity_object_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Location of the PowerBI Dedicated resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the PowerBI Dedicated resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The current deployment state of an auto scale v-core resource. The provisioningState is to indicate states for resource provisioning.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.AutoScaleVCoreSkuResponse']:
        """
        The SKU of the auto scale v-core resource.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[Optional['outputs.SystemDataResponse']]:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value pairs of additional resource provisioning properties.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the PowerBI Dedicated resource.
        """
        return pulumi.get(self, "type")

