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

__all__ = ['RestorePointCollectionArgs', 'RestorePointCollection']

@pulumi.input_type
class RestorePointCollectionArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 restore_point_collection_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input['RestorePointCollectionSourcePropertiesArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a RestorePointCollection resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] restore_point_collection_name: The name of the restore point collection.
        :param pulumi.Input['RestorePointCollectionSourcePropertiesArgs'] source: The properties of the source resource that this restore point collection is created from.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if restore_point_collection_name is not None:
            pulumi.set(__self__, "restore_point_collection_name", restore_point_collection_name)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="restorePointCollectionName")
    def restore_point_collection_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the restore point collection.
        """
        return pulumi.get(self, "restore_point_collection_name")

    @restore_point_collection_name.setter
    def restore_point_collection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "restore_point_collection_name", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input['RestorePointCollectionSourcePropertiesArgs']]:
        """
        The properties of the source resource that this restore point collection is created from.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input['RestorePointCollectionSourcePropertiesArgs']]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class RestorePointCollection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 restore_point_collection_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['RestorePointCollectionSourcePropertiesArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create or update Restore Point collection parameters.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] restore_point_collection_name: The name of the restore point collection.
        :param pulumi.Input[pulumi.InputType['RestorePointCollectionSourcePropertiesArgs']] source: The properties of the source resource that this restore point collection is created from.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RestorePointCollectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create or update Restore Point collection parameters.

        :param str resource_name: The name of the resource.
        :param RestorePointCollectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RestorePointCollectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 restore_point_collection_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['RestorePointCollectionSourcePropertiesArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RestorePointCollectionArgs.__new__(RestorePointCollectionArgs)

            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["restore_point_collection_name"] = restore_point_collection_name
            __props__.__dict__["source"] = source
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["restore_point_collection_id"] = None
            __props__.__dict__["restore_points"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:compute:RestorePointCollection"), pulumi.Alias(type_="azure-native:compute/v20210301:RestorePointCollection"), pulumi.Alias(type_="azure-native:compute/v20210401:RestorePointCollection"), pulumi.Alias(type_="azure-native:compute/v20210701:RestorePointCollection"), pulumi.Alias(type_="azure-native:compute/v20211101:RestorePointCollection"), pulumi.Alias(type_="azure-native:compute/v20220301:RestorePointCollection"), pulumi.Alias(type_="azure-native:compute/v20220801:RestorePointCollection"), pulumi.Alias(type_="azure-native:compute/v20221101:RestorePointCollection"), pulumi.Alias(type_="azure-native:compute/v20230701:RestorePointCollection"), pulumi.Alias(type_="azure-native:compute/v20230901:RestorePointCollection"), pulumi.Alias(type_="azure-native:compute/v20240301:RestorePointCollection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(RestorePointCollection, __self__).__init__(
            'azure-native:compute/v20230301:RestorePointCollection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RestorePointCollection':
        """
        Get an existing RestorePointCollection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RestorePointCollectionArgs.__new__(RestorePointCollectionArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["restore_point_collection_id"] = None
        __props__.__dict__["restore_points"] = None
        __props__.__dict__["source"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return RestorePointCollection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the restore point collection.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="restorePointCollectionId")
    def restore_point_collection_id(self) -> pulumi.Output[str]:
        """
        The unique id of the restore point collection.
        """
        return pulumi.get(self, "restore_point_collection_id")

    @property
    @pulumi.getter(name="restorePoints")
    def restore_points(self) -> pulumi.Output[Sequence['outputs.RestorePointResponse']]:
        """
        A list containing all restore points created under this restore point collection.
        """
        return pulumi.get(self, "restore_points")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional['outputs.RestorePointCollectionSourcePropertiesResponse']]:
        """
        The properties of the source resource that this restore point collection is created from.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

