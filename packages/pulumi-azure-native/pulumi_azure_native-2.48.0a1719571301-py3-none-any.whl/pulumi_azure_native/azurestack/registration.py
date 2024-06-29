# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = ['RegistrationArgs', 'Registration']

@pulumi.input_type
class RegistrationArgs:
    def __init__(__self__, *,
                 registration_token: pulumi.Input[str],
                 resource_group: pulumi.Input[str],
                 location: Optional[pulumi.Input[Union[str, 'Location']]] = None,
                 registration_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Registration resource.
        :param pulumi.Input[str] registration_token: The token identifying registered Azure Stack
        :param pulumi.Input[str] resource_group: Name of the resource group.
        :param pulumi.Input[Union[str, 'Location']] location: Location of the resource.
        :param pulumi.Input[str] registration_name: Name of the Azure Stack registration.
        """
        pulumi.set(__self__, "registration_token", registration_token)
        pulumi.set(__self__, "resource_group", resource_group)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if registration_name is not None:
            pulumi.set(__self__, "registration_name", registration_name)

    @property
    @pulumi.getter(name="registrationToken")
    def registration_token(self) -> pulumi.Input[str]:
        """
        The token identifying registered Azure Stack
        """
        return pulumi.get(self, "registration_token")

    @registration_token.setter
    def registration_token(self, value: pulumi.Input[str]):
        pulumi.set(self, "registration_token", value)

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> pulumi.Input[str]:
        """
        Name of the resource group.
        """
        return pulumi.get(self, "resource_group")

    @resource_group.setter
    def resource_group(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[Union[str, 'Location']]]:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[Union[str, 'Location']]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="registrationName")
    def registration_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Azure Stack registration.
        """
        return pulumi.get(self, "registration_name")

    @registration_name.setter
    def registration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "registration_name", value)


class Registration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[Union[str, 'Location']]] = None,
                 registration_name: Optional[pulumi.Input[str]] = None,
                 registration_token: Optional[pulumi.Input[str]] = None,
                 resource_group: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Registration information.
        Azure REST API version: 2022-06-01. Prior API version in Azure Native 1.x: 2017-06-01.

        Other available API versions: 2020-06-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'Location']] location: Location of the resource.
        :param pulumi.Input[str] registration_name: Name of the Azure Stack registration.
        :param pulumi.Input[str] registration_token: The token identifying registered Azure Stack
        :param pulumi.Input[str] resource_group: Name of the resource group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RegistrationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Registration information.
        Azure REST API version: 2022-06-01. Prior API version in Azure Native 1.x: 2017-06-01.

        Other available API versions: 2020-06-01-preview.

        :param str resource_name: The name of the resource.
        :param RegistrationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RegistrationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[Union[str, 'Location']]] = None,
                 registration_name: Optional[pulumi.Input[str]] = None,
                 registration_token: Optional[pulumi.Input[str]] = None,
                 resource_group: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RegistrationArgs.__new__(RegistrationArgs)

            __props__.__dict__["location"] = location
            __props__.__dict__["registration_name"] = registration_name
            if registration_token is None and not opts.urn:
                raise TypeError("Missing required property 'registration_token'")
            __props__.__dict__["registration_token"] = registration_token
            if resource_group is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group'")
            __props__.__dict__["resource_group"] = resource_group
            __props__.__dict__["billing_model"] = None
            __props__.__dict__["cloud_id"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["object_id"] = None
            __props__.__dict__["tags"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:azurestack/v20160101:Registration"), pulumi.Alias(type_="azure-native:azurestack/v20170601:Registration"), pulumi.Alias(type_="azure-native:azurestack/v20200601preview:Registration"), pulumi.Alias(type_="azure-native:azurestack/v20220601:Registration")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Registration, __self__).__init__(
            'azure-native:azurestack:Registration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Registration':
        """
        Get an existing Registration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RegistrationArgs.__new__(RegistrationArgs)

        __props__.__dict__["billing_model"] = None
        __props__.__dict__["cloud_id"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["object_id"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Registration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="billingModel")
    def billing_model(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the billing mode for the Azure Stack registration.
        """
        return pulumi.get(self, "billing_model")

    @property
    @pulumi.getter(name="cloudId")
    def cloud_id(self) -> pulumi.Output[Optional[str]]:
        """
        The identifier of the registered Azure Stack.
        """
        return pulumi.get(self, "cloud_id")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        The entity tag used for optimistic concurrency when modifying the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Output[Optional[str]]:
        """
        The object identifier associated with the Azure Stack connecting to Azure.
        """
        return pulumi.get(self, "object_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Custom tags for the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of Resource.
        """
        return pulumi.get(self, "type")

