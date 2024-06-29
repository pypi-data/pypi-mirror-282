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

__all__ = ['ResourceGuardInitArgs', 'ResourceGuard']

@pulumi.input_type
class ResourceGuardInitArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 e_tag: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['ResourceGuardArgs']] = None,
                 resource_guards_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ResourceGuard resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] e_tag: Optional ETag.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input['ResourceGuardArgs'] properties: ResourceGuardResource properties
        :param pulumi.Input[str] resource_guards_name: The name of ResourceGuard
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if e_tag is not None:
            pulumi.set(__self__, "e_tag", e_tag)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if resource_guards_name is not None:
            pulumi.set(__self__, "resource_guards_name", resource_guards_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[pulumi.Input[str]]:
        """
        Optional ETag.
        """
        return pulumi.get(self, "e_tag")

    @e_tag.setter
    def e_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "e_tag", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['ResourceGuardArgs']]:
        """
        ResourceGuardResource properties
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['ResourceGuardArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="resourceGuardsName")
    def resource_guards_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of ResourceGuard
        """
        return pulumi.get(self, "resource_guards_name")

    @resource_guards_name.setter
    def resource_guards_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_guards_name", value)

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


class ResourceGuard(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['ResourceGuardArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_guards_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a ResourceGuard resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] e_tag: Optional ETag.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[pulumi.InputType['ResourceGuardArgs']] properties: ResourceGuardResource properties
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_guards_name: The name of ResourceGuard
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ResourceGuardInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ResourceGuard resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ResourceGuardInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResourceGuardInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['ResourceGuardArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_guards_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ResourceGuardInitArgs.__new__(ResourceGuardInitArgs)

            __props__.__dict__["e_tag"] = e_tag
            __props__.__dict__["location"] = location
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_guards_name"] = resource_guards_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:dataprotection:ResourceGuard"), pulumi.Alias(type_="azure-native:dataprotection/v20210701:ResourceGuard"), pulumi.Alias(type_="azure-native:dataprotection/v20211001preview:ResourceGuard"), pulumi.Alias(type_="azure-native:dataprotection/v20211201preview:ResourceGuard"), pulumi.Alias(type_="azure-native:dataprotection/v20220101:ResourceGuard"), pulumi.Alias(type_="azure-native:dataprotection/v20220201preview:ResourceGuard"), pulumi.Alias(type_="azure-native:dataprotection/v20220301:ResourceGuard"), pulumi.Alias(type_="azure-native:dataprotection/v20220331preview:ResourceGuard"), pulumi.Alias(type_="azure-native:dataprotection/v20220401:ResourceGuard"), pulumi.Alias(type_="azure-native:dataprotection/v20220501:ResourceGuard"), pulumi.Alias(type_="azure-native:dataprotection/v20220901preview:ResourceGuard"), pulumi.Alias(type_="azure-native:dataprotection/v20221001preview:ResourceGuard"), pulumi.Alias(type_="azure-native:dataprotection/v20221101preview:ResourceGuard"), pulumi.Alias(type_="azure-native:dataprotection/v20221201:ResourceGuard"), pulumi.Alias(type_="azure-native:dataprotection/v20230101:ResourceGuard"), pulumi.Alias(type_="azure-native:dataprotection/v20230501:ResourceGuard"), pulumi.Alias(type_="azure-native:dataprotection/v20230601preview:ResourceGuard"), pulumi.Alias(type_="azure-native:dataprotection/v20230801preview:ResourceGuard"), pulumi.Alias(type_="azure-native:dataprotection/v20231101:ResourceGuard"), pulumi.Alias(type_="azure-native:dataprotection/v20231201:ResourceGuard"), pulumi.Alias(type_="azure-native:dataprotection/v20240201preview:ResourceGuard"), pulumi.Alias(type_="azure-native:dataprotection/v20240301:ResourceGuard"), pulumi.Alias(type_="azure-native:dataprotection/v20240401:ResourceGuard")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ResourceGuard, __self__).__init__(
            'azure-native:dataprotection/v20230401preview:ResourceGuard',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ResourceGuard':
        """
        Get an existing ResourceGuard resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ResourceGuardInitArgs.__new__(ResourceGuardInitArgs)

        __props__.__dict__["e_tag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return ResourceGuard(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[Optional[str]]:
        """
        Optional ETag.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name associated with the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.ResourceGuardResponse']:
        """
        ResourceGuardResource properties
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
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
    def type(self) -> pulumi.Output[str]:
        """
        Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/...
        """
        return pulumi.get(self, "type")

