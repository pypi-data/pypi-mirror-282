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

__all__ = ['VolumeArgs', 'Volume']

@pulumi.input_type
class VolumeArgs:
    def __init__(__self__, *,
                 elastic_san_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 size_gi_b: pulumi.Input[float],
                 volume_group_name: pulumi.Input[str],
                 creation_data: Optional[pulumi.Input['SourceCreationDataArgs']] = None,
                 managed_by: Optional[pulumi.Input['ManagedByInfoArgs']] = None,
                 volume_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Volume resource.
        :param pulumi.Input[str] elastic_san_name: The name of the ElasticSan.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[float] size_gi_b: Volume size.
        :param pulumi.Input[str] volume_group_name: The name of the VolumeGroup.
        :param pulumi.Input['SourceCreationDataArgs'] creation_data: State of the operation on the resource.
        :param pulumi.Input['ManagedByInfoArgs'] managed_by: Parent resource information.
        :param pulumi.Input[str] volume_name: The name of the Volume.
        """
        pulumi.set(__self__, "elastic_san_name", elastic_san_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "size_gi_b", size_gi_b)
        pulumi.set(__self__, "volume_group_name", volume_group_name)
        if creation_data is not None:
            pulumi.set(__self__, "creation_data", creation_data)
        if managed_by is not None:
            pulumi.set(__self__, "managed_by", managed_by)
        if volume_name is not None:
            pulumi.set(__self__, "volume_name", volume_name)

    @property
    @pulumi.getter(name="elasticSanName")
    def elastic_san_name(self) -> pulumi.Input[str]:
        """
        The name of the ElasticSan.
        """
        return pulumi.get(self, "elastic_san_name")

    @elastic_san_name.setter
    def elastic_san_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "elastic_san_name", value)

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
    @pulumi.getter(name="sizeGiB")
    def size_gi_b(self) -> pulumi.Input[float]:
        """
        Volume size.
        """
        return pulumi.get(self, "size_gi_b")

    @size_gi_b.setter
    def size_gi_b(self, value: pulumi.Input[float]):
        pulumi.set(self, "size_gi_b", value)

    @property
    @pulumi.getter(name="volumeGroupName")
    def volume_group_name(self) -> pulumi.Input[str]:
        """
        The name of the VolumeGroup.
        """
        return pulumi.get(self, "volume_group_name")

    @volume_group_name.setter
    def volume_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "volume_group_name", value)

    @property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> Optional[pulumi.Input['SourceCreationDataArgs']]:
        """
        State of the operation on the resource.
        """
        return pulumi.get(self, "creation_data")

    @creation_data.setter
    def creation_data(self, value: Optional[pulumi.Input['SourceCreationDataArgs']]):
        pulumi.set(self, "creation_data", value)

    @property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> Optional[pulumi.Input['ManagedByInfoArgs']]:
        """
        Parent resource information.
        """
        return pulumi.get(self, "managed_by")

    @managed_by.setter
    def managed_by(self, value: Optional[pulumi.Input['ManagedByInfoArgs']]):
        pulumi.set(self, "managed_by", value)

    @property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Volume.
        """
        return pulumi.get(self, "volume_name")

    @volume_name.setter
    def volume_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_name", value)


class Volume(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 creation_data: Optional[pulumi.Input[pulumi.InputType['SourceCreationDataArgs']]] = None,
                 elastic_san_name: Optional[pulumi.Input[str]] = None,
                 managed_by: Optional[pulumi.Input[pulumi.InputType['ManagedByInfoArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 size_gi_b: Optional[pulumi.Input[float]] = None,
                 volume_group_name: Optional[pulumi.Input[str]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Response for Volume request.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['SourceCreationDataArgs']] creation_data: State of the operation on the resource.
        :param pulumi.Input[str] elastic_san_name: The name of the ElasticSan.
        :param pulumi.Input[pulumi.InputType['ManagedByInfoArgs']] managed_by: Parent resource information.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[float] size_gi_b: Volume size.
        :param pulumi.Input[str] volume_group_name: The name of the VolumeGroup.
        :param pulumi.Input[str] volume_name: The name of the Volume.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VolumeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Response for Volume request.

        :param str resource_name: The name of the resource.
        :param VolumeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VolumeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 creation_data: Optional[pulumi.Input[pulumi.InputType['SourceCreationDataArgs']]] = None,
                 elastic_san_name: Optional[pulumi.Input[str]] = None,
                 managed_by: Optional[pulumi.Input[pulumi.InputType['ManagedByInfoArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 size_gi_b: Optional[pulumi.Input[float]] = None,
                 volume_group_name: Optional[pulumi.Input[str]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VolumeArgs.__new__(VolumeArgs)

            __props__.__dict__["creation_data"] = creation_data
            if elastic_san_name is None and not opts.urn:
                raise TypeError("Missing required property 'elastic_san_name'")
            __props__.__dict__["elastic_san_name"] = elastic_san_name
            __props__.__dict__["managed_by"] = managed_by
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if size_gi_b is None and not opts.urn:
                raise TypeError("Missing required property 'size_gi_b'")
            __props__.__dict__["size_gi_b"] = size_gi_b
            if volume_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'volume_group_name'")
            __props__.__dict__["volume_group_name"] = volume_group_name
            __props__.__dict__["volume_name"] = volume_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["storage_target"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["volume_id"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:elasticsan:Volume"), pulumi.Alias(type_="azure-native:elasticsan/v20211120preview:Volume"), pulumi.Alias(type_="azure-native:elasticsan/v20221201preview:Volume"), pulumi.Alias(type_="azure-native:elasticsan/v20240501:Volume")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Volume, __self__).__init__(
            'azure-native:elasticsan/v20230101:Volume',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Volume':
        """
        Get an existing Volume resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VolumeArgs.__new__(VolumeArgs)

        __props__.__dict__["creation_data"] = None
        __props__.__dict__["managed_by"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["size_gi_b"] = None
        __props__.__dict__["storage_target"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["volume_id"] = None
        return Volume(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> pulumi.Output[Optional['outputs.SourceCreationDataResponse']]:
        """
        State of the operation on the resource.
        """
        return pulumi.get(self, "creation_data")

    @property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> pulumi.Output[Optional['outputs.ManagedByInfoResponse']]:
        """
        Parent resource information.
        """
        return pulumi.get(self, "managed_by")

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
        State of the operation on the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sizeGiB")
    def size_gi_b(self) -> pulumi.Output[float]:
        """
        Volume size.
        """
        return pulumi.get(self, "size_gi_b")

    @property
    @pulumi.getter(name="storageTarget")
    def storage_target(self) -> pulumi.Output['outputs.IscsiTargetInfoResponse']:
        """
        Storage target information
        """
        return pulumi.get(self, "storage_target")

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

    @property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> pulumi.Output[str]:
        """
        Unique Id of the volume in GUID format
        """
        return pulumi.get(self, "volume_id")

