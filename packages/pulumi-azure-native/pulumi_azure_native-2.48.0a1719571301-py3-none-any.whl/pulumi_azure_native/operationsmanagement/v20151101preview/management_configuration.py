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

__all__ = ['ManagementConfigurationArgs', 'ManagementConfiguration']

@pulumi.input_type
class ManagementConfigurationArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 management_configuration_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['ManagementConfigurationPropertiesArgs']] = None):
        """
        The set of arguments for constructing a ManagementConfiguration resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to get. The name is case insensitive.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] management_configuration_name: User Management Configuration Name.
        :param pulumi.Input['ManagementConfigurationPropertiesArgs'] properties: Properties for ManagementConfiguration object supported by the OperationsManagement resource provider.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if management_configuration_name is not None:
            pulumi.set(__self__, "management_configuration_name", management_configuration_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group to get. The name is case insensitive.
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
    @pulumi.getter(name="managementConfigurationName")
    def management_configuration_name(self) -> Optional[pulumi.Input[str]]:
        """
        User Management Configuration Name.
        """
        return pulumi.get(self, "management_configuration_name")

    @management_configuration_name.setter
    def management_configuration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "management_configuration_name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['ManagementConfigurationPropertiesArgs']]:
        """
        Properties for ManagementConfiguration object supported by the OperationsManagement resource provider.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['ManagementConfigurationPropertiesArgs']]):
        pulumi.set(self, "properties", value)


class ManagementConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 management_configuration_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['ManagementConfigurationPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The container for solution.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] management_configuration_name: User Management Configuration Name.
        :param pulumi.Input[pulumi.InputType['ManagementConfigurationPropertiesArgs']] properties: Properties for ManagementConfiguration object supported by the OperationsManagement resource provider.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to get. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagementConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The container for solution.

        :param str resource_name: The name of the resource.
        :param ManagementConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagementConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 management_configuration_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['ManagementConfigurationPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ManagementConfigurationArgs.__new__(ManagementConfigurationArgs)

            __props__.__dict__["location"] = location
            __props__.__dict__["management_configuration_name"] = management_configuration_name
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:operationsmanagement:ManagementConfiguration")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ManagementConfiguration, __self__).__init__(
            'azure-native:operationsmanagement/v20151101preview:ManagementConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ManagementConfiguration':
        """
        Get an existing ManagementConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ManagementConfigurationArgs.__new__(ManagementConfigurationArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return ManagementConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.ManagementConfigurationPropertiesResponse']:
        """
        Properties for ManagementConfiguration object supported by the OperationsManagement resource provider.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

