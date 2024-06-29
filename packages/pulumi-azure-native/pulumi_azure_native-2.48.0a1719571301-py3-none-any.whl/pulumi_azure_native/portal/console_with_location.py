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

__all__ = ['ConsoleWithLocationArgs', 'ConsoleWithLocation']

@pulumi.input_type
class ConsoleWithLocationArgs:
    def __init__(__self__, *,
                 location: pulumi.Input[str],
                 console_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ConsoleWithLocation resource.
        :param pulumi.Input[str] location: The provider location
        :param pulumi.Input[str] console_name: The name of the console
        """
        pulumi.set(__self__, "location", location)
        if console_name is not None:
            pulumi.set(__self__, "console_name", console_name)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        The provider location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="consoleName")
    def console_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the console
        """
        return pulumi.get(self, "console_name")

    @console_name.setter
    def console_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "console_name", value)


class ConsoleWithLocation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 console_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Cloud shell console
        Azure REST API version: 2018-10-01. Prior API version in Azure Native 1.x: 2018-10-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] console_name: The name of the console
        :param pulumi.Input[str] location: The provider location
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConsoleWithLocationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Cloud shell console
        Azure REST API version: 2018-10-01. Prior API version in Azure Native 1.x: 2018-10-01.

        :param str resource_name: The name of the resource.
        :param ConsoleWithLocationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConsoleWithLocationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 console_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConsoleWithLocationArgs.__new__(ConsoleWithLocationArgs)

            __props__.__dict__["console_name"] = console_name
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            __props__.__dict__["properties"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:portal/v20181001:ConsoleWithLocation")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ConsoleWithLocation, __self__).__init__(
            'azure-native:portal:ConsoleWithLocation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConsoleWithLocation':
        """
        Get an existing ConsoleWithLocation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConsoleWithLocationArgs.__new__(ConsoleWithLocationArgs)

        __props__.__dict__["properties"] = None
        return ConsoleWithLocation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.ConsolePropertiesResponse']:
        """
        Cloud shell console properties.
        """
        return pulumi.get(self, "properties")

