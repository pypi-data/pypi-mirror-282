# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ServiceArgs', 'Service']

@pulumi.input_type
class ServiceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 admin_domain_name: Optional[pulumi.Input[str]] = None,
                 billing_domain_name: Optional[pulumi.Input[str]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 quantity: Optional[pulumi.Input[float]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Service resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the Windows IoT Device Service.
        :param pulumi.Input[str] admin_domain_name: Windows IoT Device Service OEM AAD domain
        :param pulumi.Input[str] billing_domain_name: Windows IoT Device Service ODM AAD domain
        :param pulumi.Input[str] device_name: The name of the Windows IoT Device Service.
        :param pulumi.Input[str] location: The Azure Region where the resource lives
        :param pulumi.Input[str] notes: Windows IoT Device Service notes.
        :param pulumi.Input[float] quantity: Windows IoT Device Service device allocation,
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if admin_domain_name is not None:
            pulumi.set(__self__, "admin_domain_name", admin_domain_name)
        if billing_domain_name is not None:
            pulumi.set(__self__, "billing_domain_name", billing_domain_name)
        if device_name is not None:
            pulumi.set(__self__, "device_name", device_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if notes is not None:
            pulumi.set(__self__, "notes", notes)
        if quantity is not None:
            pulumi.set(__self__, "quantity", quantity)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the Windows IoT Device Service.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="adminDomainName")
    def admin_domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        Windows IoT Device Service OEM AAD domain
        """
        return pulumi.get(self, "admin_domain_name")

    @admin_domain_name.setter
    def admin_domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "admin_domain_name", value)

    @property
    @pulumi.getter(name="billingDomainName")
    def billing_domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        Windows IoT Device Service ODM AAD domain
        """
        return pulumi.get(self, "billing_domain_name")

    @billing_domain_name.setter
    def billing_domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "billing_domain_name", value)

    @property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Windows IoT Device Service.
        """
        return pulumi.get(self, "device_name")

    @device_name.setter
    def device_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "device_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Region where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[str]]:
        """
        Windows IoT Device Service notes.
        """
        return pulumi.get(self, "notes")

    @notes.setter
    def notes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notes", value)

    @property
    @pulumi.getter
    def quantity(self) -> Optional[pulumi.Input[float]]:
        """
        Windows IoT Device Service device allocation,
        """
        return pulumi.get(self, "quantity")

    @quantity.setter
    def quantity(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "quantity", value)

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


class Service(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_domain_name: Optional[pulumi.Input[str]] = None,
                 billing_domain_name: Optional[pulumi.Input[str]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 quantity: Optional[pulumi.Input[float]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The description of the Windows IoT Device Service.
        Azure REST API version: 2019-06-01. Prior API version in Azure Native 1.x: 2019-06-01.

        Other available API versions: 2018-02-16-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] admin_domain_name: Windows IoT Device Service OEM AAD domain
        :param pulumi.Input[str] billing_domain_name: Windows IoT Device Service ODM AAD domain
        :param pulumi.Input[str] device_name: The name of the Windows IoT Device Service.
        :param pulumi.Input[str] location: The Azure Region where the resource lives
        :param pulumi.Input[str] notes: Windows IoT Device Service notes.
        :param pulumi.Input[float] quantity: Windows IoT Device Service device allocation,
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the Windows IoT Device Service.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServiceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The description of the Windows IoT Device Service.
        Azure REST API version: 2019-06-01. Prior API version in Azure Native 1.x: 2019-06-01.

        Other available API versions: 2018-02-16-preview.

        :param str resource_name: The name of the resource.
        :param ServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_domain_name: Optional[pulumi.Input[str]] = None,
                 billing_domain_name: Optional[pulumi.Input[str]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 quantity: Optional[pulumi.Input[float]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServiceArgs.__new__(ServiceArgs)

            __props__.__dict__["admin_domain_name"] = admin_domain_name
            __props__.__dict__["billing_domain_name"] = billing_domain_name
            __props__.__dict__["device_name"] = device_name
            __props__.__dict__["location"] = location
            __props__.__dict__["notes"] = notes
            __props__.__dict__["quantity"] = quantity
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["start_date"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:windowsiot/v20180216preview:Service"), pulumi.Alias(type_="azure-native:windowsiot/v20190601:Service")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Service, __self__).__init__(
            'azure-native:windowsiot:Service',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Service':
        """
        Get an existing Service resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServiceArgs.__new__(ServiceArgs)

        __props__.__dict__["admin_domain_name"] = None
        __props__.__dict__["billing_domain_name"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["notes"] = None
        __props__.__dict__["quantity"] = None
        __props__.__dict__["start_date"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Service(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adminDomainName")
    def admin_domain_name(self) -> pulumi.Output[Optional[str]]:
        """
        Windows IoT Device Service OEM AAD domain
        """
        return pulumi.get(self, "admin_domain_name")

    @property
    @pulumi.getter(name="billingDomainName")
    def billing_domain_name(self) -> pulumi.Output[Optional[str]]:
        """
        Windows IoT Device Service ODM AAD domain
        """
        return pulumi.get(self, "billing_domain_name")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The Azure Region where the resource lives
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
    def notes(self) -> pulumi.Output[Optional[str]]:
        """
        Windows IoT Device Service notes.
        """
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter
    def quantity(self) -> pulumi.Output[Optional[float]]:
        """
        Windows IoT Device Service device allocation,
        """
        return pulumi.get(self, "quantity")

    @property
    @pulumi.getter(name="startDate")
    def start_date(self) -> pulumi.Output[str]:
        """
        Windows IoT Device Service start date,
        """
        return pulumi.get(self, "start_date")

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
        The type of the resource.
        """
        return pulumi.get(self, "type")

