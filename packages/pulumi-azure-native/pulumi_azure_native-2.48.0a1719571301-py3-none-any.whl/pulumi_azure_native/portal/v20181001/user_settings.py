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

__all__ = ['UserSettingsArgs', 'UserSettings']

@pulumi.input_type
class UserSettingsArgs:
    def __init__(__self__, *,
                 properties: pulumi.Input['UserPropertiesArgs'],
                 user_settings_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a UserSettings resource.
        :param pulumi.Input['UserPropertiesArgs'] properties: The cloud shell user settings properties.
        :param pulumi.Input[str] user_settings_name: The name of the user settings
        """
        pulumi.set(__self__, "properties", properties)
        if user_settings_name is not None:
            pulumi.set(__self__, "user_settings_name", user_settings_name)

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Input['UserPropertiesArgs']:
        """
        The cloud shell user settings properties.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: pulumi.Input['UserPropertiesArgs']):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="userSettingsName")
    def user_settings_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the user settings
        """
        return pulumi.get(self, "user_settings_name")

    @user_settings_name.setter
    def user_settings_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_settings_name", value)


class UserSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['UserPropertiesArgs']]] = None,
                 user_settings_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Response to get user settings

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['UserPropertiesArgs']] properties: The cloud shell user settings properties.
        :param pulumi.Input[str] user_settings_name: The name of the user settings
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserSettingsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Response to get user settings

        :param str resource_name: The name of the resource.
        :param UserSettingsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserSettingsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['UserPropertiesArgs']]] = None,
                 user_settings_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserSettingsArgs.__new__(UserSettingsArgs)

            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__.__dict__["properties"] = properties
            __props__.__dict__["user_settings_name"] = user_settings_name
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:portal:UserSettings")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(UserSettings, __self__).__init__(
            'azure-native:portal/v20181001:UserSettings',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'UserSettings':
        """
        Get an existing UserSettings resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = UserSettingsArgs.__new__(UserSettingsArgs)

        __props__.__dict__["properties"] = None
        return UserSettings(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.UserPropertiesResponse']:
        """
        The cloud shell user settings properties.
        """
        return pulumi.get(self, "properties")

