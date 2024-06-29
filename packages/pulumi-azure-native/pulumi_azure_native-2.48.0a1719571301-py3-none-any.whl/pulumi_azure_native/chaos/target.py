# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = ['TargetArgs', 'Target']

@pulumi.input_type
class TargetArgs:
    def __init__(__self__, *,
                 parent_provider_namespace: pulumi.Input[str],
                 parent_resource_name: pulumi.Input[str],
                 parent_resource_type: pulumi.Input[str],
                 properties: Any,
                 resource_group_name: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 target_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Target resource.
        :param pulumi.Input[str] parent_provider_namespace: String that represents a resource provider namespace.
        :param pulumi.Input[str] parent_resource_name: String that represents a resource name.
        :param pulumi.Input[str] parent_resource_type: String that represents a resource type.
        :param Any properties: The properties of the target resource.
        :param pulumi.Input[str] resource_group_name: String that represents an Azure resource group.
        :param pulumi.Input[str] location: Location of the target resource.
        :param pulumi.Input[str] target_name: String that represents a Target resource name.
        """
        pulumi.set(__self__, "parent_provider_namespace", parent_provider_namespace)
        pulumi.set(__self__, "parent_resource_name", parent_resource_name)
        pulumi.set(__self__, "parent_resource_type", parent_resource_type)
        pulumi.set(__self__, "properties", properties)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if target_name is not None:
            pulumi.set(__self__, "target_name", target_name)

    @property
    @pulumi.getter(name="parentProviderNamespace")
    def parent_provider_namespace(self) -> pulumi.Input[str]:
        """
        String that represents a resource provider namespace.
        """
        return pulumi.get(self, "parent_provider_namespace")

    @parent_provider_namespace.setter
    def parent_provider_namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "parent_provider_namespace", value)

    @property
    @pulumi.getter(name="parentResourceName")
    def parent_resource_name(self) -> pulumi.Input[str]:
        """
        String that represents a resource name.
        """
        return pulumi.get(self, "parent_resource_name")

    @parent_resource_name.setter
    def parent_resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "parent_resource_name", value)

    @property
    @pulumi.getter(name="parentResourceType")
    def parent_resource_type(self) -> pulumi.Input[str]:
        """
        String that represents a resource type.
        """
        return pulumi.get(self, "parent_resource_type")

    @parent_resource_type.setter
    def parent_resource_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "parent_resource_type", value)

    @property
    @pulumi.getter
    def properties(self) -> Any:
        """
        The properties of the target resource.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Any):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        String that represents an Azure resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Location of the target resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="targetName")
    def target_name(self) -> Optional[pulumi.Input[str]]:
        """
        String that represents a Target resource name.
        """
        return pulumi.get(self, "target_name")

    @target_name.setter
    def target_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_name", value)


class Target(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 parent_provider_namespace: Optional[pulumi.Input[str]] = None,
                 parent_resource_name: Optional[pulumi.Input[str]] = None,
                 parent_resource_type: Optional[pulumi.Input[str]] = None,
                 properties: Optional[Any] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 target_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Model that represents a Target resource.
        Azure REST API version: 2023-04-15-preview. Prior API version in Azure Native 1.x: 2021-09-15-preview.

        Other available API versions: 2023-09-01-preview, 2023-10-27-preview, 2023-11-01, 2024-01-01, 2024-03-22-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: Location of the target resource.
        :param pulumi.Input[str] parent_provider_namespace: String that represents a resource provider namespace.
        :param pulumi.Input[str] parent_resource_name: String that represents a resource name.
        :param pulumi.Input[str] parent_resource_type: String that represents a resource type.
        :param Any properties: The properties of the target resource.
        :param pulumi.Input[str] resource_group_name: String that represents an Azure resource group.
        :param pulumi.Input[str] target_name: String that represents a Target resource name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TargetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Model that represents a Target resource.
        Azure REST API version: 2023-04-15-preview. Prior API version in Azure Native 1.x: 2021-09-15-preview.

        Other available API versions: 2023-09-01-preview, 2023-10-27-preview, 2023-11-01, 2024-01-01, 2024-03-22-preview.

        :param str resource_name: The name of the resource.
        :param TargetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TargetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 parent_provider_namespace: Optional[pulumi.Input[str]] = None,
                 parent_resource_name: Optional[pulumi.Input[str]] = None,
                 parent_resource_type: Optional[pulumi.Input[str]] = None,
                 properties: Optional[Any] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 target_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TargetArgs.__new__(TargetArgs)

            __props__.__dict__["location"] = location
            if parent_provider_namespace is None and not opts.urn:
                raise TypeError("Missing required property 'parent_provider_namespace'")
            __props__.__dict__["parent_provider_namespace"] = parent_provider_namespace
            if parent_resource_name is None and not opts.urn:
                raise TypeError("Missing required property 'parent_resource_name'")
            __props__.__dict__["parent_resource_name"] = parent_resource_name
            if parent_resource_type is None and not opts.urn:
                raise TypeError("Missing required property 'parent_resource_type'")
            __props__.__dict__["parent_resource_type"] = parent_resource_type
            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["target_name"] = target_name
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:chaos/v20210915preview:Target"), pulumi.Alias(type_="azure-native:chaos/v20220701preview:Target"), pulumi.Alias(type_="azure-native:chaos/v20221001preview:Target"), pulumi.Alias(type_="azure-native:chaos/v20230401preview:Target"), pulumi.Alias(type_="azure-native:chaos/v20230415preview:Target"), pulumi.Alias(type_="azure-native:chaos/v20230901preview:Target"), pulumi.Alias(type_="azure-native:chaos/v20231027preview:Target"), pulumi.Alias(type_="azure-native:chaos/v20231101:Target"), pulumi.Alias(type_="azure-native:chaos/v20240101:Target"), pulumi.Alias(type_="azure-native:chaos/v20240322preview:Target")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Target, __self__).__init__(
            'azure-native:chaos:Target',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Target':
        """
        Get an existing Target resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TargetArgs.__new__(TargetArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return Target(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Location of the target resource.
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
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]:
        """
        The properties of the target resource.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata of the target resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

