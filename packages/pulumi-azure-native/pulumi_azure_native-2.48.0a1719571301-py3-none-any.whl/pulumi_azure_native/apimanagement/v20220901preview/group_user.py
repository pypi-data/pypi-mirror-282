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

__all__ = ['GroupUserArgs', 'GroupUser']

@pulumi.input_type
class GroupUserArgs:
    def __init__(__self__, *,
                 group_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 user_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a GroupUser resource.
        :param pulumi.Input[str] group_id: Group identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] user_id: User identifier. Must be unique in the current API Management service instance.
        """
        pulumi.set(__self__, "group_id", group_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if user_id is not None:
            pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Input[str]:
        """
        Group identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_id", value)

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
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name of the API Management service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[str]]:
        """
        User identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_id", value)


class GroupUser(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        User details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_id: Group identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] user_id: User identifier. Must be unique in the current API Management service instance.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GroupUserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        User details.

        :param str resource_name: The name of the resource.
        :param GroupUserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GroupUserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GroupUserArgs.__new__(GroupUserArgs)

            if group_id is None and not opts.urn:
                raise TypeError("Missing required property 'group_id'")
            __props__.__dict__["group_id"] = group_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["user_id"] = user_id
            __props__.__dict__["email"] = None
            __props__.__dict__["first_name"] = None
            __props__.__dict__["groups"] = None
            __props__.__dict__["identities"] = None
            __props__.__dict__["last_name"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["note"] = None
            __props__.__dict__["registration_date"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement:GroupUser"), pulumi.Alias(type_="azure-native:apimanagement/v20170301:GroupUser"), pulumi.Alias(type_="azure-native:apimanagement/v20180101:GroupUser"), pulumi.Alias(type_="azure-native:apimanagement/v20180601preview:GroupUser"), pulumi.Alias(type_="azure-native:apimanagement/v20190101:GroupUser"), pulumi.Alias(type_="azure-native:apimanagement/v20191201:GroupUser"), pulumi.Alias(type_="azure-native:apimanagement/v20191201preview:GroupUser"), pulumi.Alias(type_="azure-native:apimanagement/v20200601preview:GroupUser"), pulumi.Alias(type_="azure-native:apimanagement/v20201201:GroupUser"), pulumi.Alias(type_="azure-native:apimanagement/v20210101preview:GroupUser"), pulumi.Alias(type_="azure-native:apimanagement/v20210401preview:GroupUser"), pulumi.Alias(type_="azure-native:apimanagement/v20210801:GroupUser"), pulumi.Alias(type_="azure-native:apimanagement/v20211201preview:GroupUser"), pulumi.Alias(type_="azure-native:apimanagement/v20220401preview:GroupUser"), pulumi.Alias(type_="azure-native:apimanagement/v20220801:GroupUser"), pulumi.Alias(type_="azure-native:apimanagement/v20230301preview:GroupUser"), pulumi.Alias(type_="azure-native:apimanagement/v20230501preview:GroupUser"), pulumi.Alias(type_="azure-native:apimanagement/v20230901preview:GroupUser")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(GroupUser, __self__).__init__(
            'azure-native:apimanagement/v20220901preview:GroupUser',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GroupUser':
        """
        Get an existing GroupUser resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GroupUserArgs.__new__(GroupUserArgs)

        __props__.__dict__["email"] = None
        __props__.__dict__["first_name"] = None
        __props__.__dict__["groups"] = None
        __props__.__dict__["identities"] = None
        __props__.__dict__["last_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["note"] = None
        __props__.__dict__["registration_date"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["type"] = None
        return GroupUser(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[Optional[str]]:
        """
        Email address.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> pulumi.Output[Optional[str]]:
        """
        First name.
        """
        return pulumi.get(self, "first_name")

    @property
    @pulumi.getter
    def groups(self) -> pulumi.Output[Sequence['outputs.GroupContractPropertiesResponse']]:
        """
        Collection of groups user is part of.
        """
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter
    def identities(self) -> pulumi.Output[Optional[Sequence['outputs.UserIdentityContractResponse']]]:
        """
        Collection of user identities.
        """
        return pulumi.get(self, "identities")

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> pulumi.Output[Optional[str]]:
        """
        Last name.
        """
        return pulumi.get(self, "last_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def note(self) -> pulumi.Output[Optional[str]]:
        """
        Optional note about a user set by the administrator.
        """
        return pulumi.get(self, "note")

    @property
    @pulumi.getter(name="registrationDate")
    def registration_date(self) -> pulumi.Output[Optional[str]]:
        """
        Date of user registration. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.
        """
        return pulumi.get(self, "registration_date")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[str]]:
        """
        Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

