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

__all__ = ['IntegrationAccountPartnerArgs', 'IntegrationAccountPartner']

@pulumi.input_type
class IntegrationAccountPartnerArgs:
    def __init__(__self__, *,
                 integration_account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 content: Optional[pulumi.Input['PartnerContentArgs']] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 partner_name: Optional[pulumi.Input[str]] = None,
                 partner_type: Optional[pulumi.Input['PartnerType']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IntegrationAccountPartner resource.
        :param pulumi.Input[str] integration_account_name: The integration account name.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input['PartnerContentArgs'] content: The partner content.
        :param pulumi.Input[str] id: The resource id.
        :param pulumi.Input[str] location: The resource location.
        :param Any metadata: The metadata.
        :param pulumi.Input[str] name: The resource name.
        :param pulumi.Input[str] partner_name: The integration account partner name.
        :param pulumi.Input['PartnerType'] partner_type: The partner type.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        :param pulumi.Input[str] type: The resource type.
        """
        pulumi.set(__self__, "integration_account_name", integration_account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if content is not None:
            pulumi.set(__self__, "content", content)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if partner_name is not None:
            pulumi.set(__self__, "partner_name", partner_name)
        if partner_type is not None:
            pulumi.set(__self__, "partner_type", partner_type)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="integrationAccountName")
    def integration_account_name(self) -> pulumi.Input[str]:
        """
        The integration account name.
        """
        return pulumi.get(self, "integration_account_name")

    @integration_account_name.setter
    def integration_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "integration_account_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input['PartnerContentArgs']]:
        """
        The partner content.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: Optional[pulumi.Input['PartnerContentArgs']]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource id.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        """
        The metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[Any]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="partnerName")
    def partner_name(self) -> Optional[pulumi.Input[str]]:
        """
        The integration account partner name.
        """
        return pulumi.get(self, "partner_name")

    @partner_name.setter
    def partner_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partner_name", value)

    @property
    @pulumi.getter(name="partnerType")
    def partner_type(self) -> Optional[pulumi.Input['PartnerType']]:
        """
        The partner type.
        """
        return pulumi.get(self, "partner_type")

    @partner_type.setter
    def partner_type(self, value: Optional[pulumi.Input['PartnerType']]):
        pulumi.set(self, "partner_type", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class IntegrationAccountPartner(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content: Optional[pulumi.Input[pulumi.InputType['PartnerContentArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 integration_account_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 partner_name: Optional[pulumi.Input[str]] = None,
                 partner_type: Optional[pulumi.Input['PartnerType']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a IntegrationAccountPartner resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['PartnerContentArgs']] content: The partner content.
        :param pulumi.Input[str] id: The resource id.
        :param pulumi.Input[str] integration_account_name: The integration account name.
        :param pulumi.Input[str] location: The resource location.
        :param Any metadata: The metadata.
        :param pulumi.Input[str] name: The resource name.
        :param pulumi.Input[str] partner_name: The integration account partner name.
        :param pulumi.Input['PartnerType'] partner_type: The partner type.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        :param pulumi.Input[str] type: The resource type.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IntegrationAccountPartnerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a IntegrationAccountPartner resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param IntegrationAccountPartnerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IntegrationAccountPartnerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content: Optional[pulumi.Input[pulumi.InputType['PartnerContentArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 integration_account_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 partner_name: Optional[pulumi.Input[str]] = None,
                 partner_type: Optional[pulumi.Input['PartnerType']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IntegrationAccountPartnerArgs.__new__(IntegrationAccountPartnerArgs)

            __props__.__dict__["content"] = content
            __props__.__dict__["id"] = id
            if integration_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'integration_account_name'")
            __props__.__dict__["integration_account_name"] = integration_account_name
            __props__.__dict__["location"] = location
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["name"] = name
            __props__.__dict__["partner_name"] = partner_name
            __props__.__dict__["partner_type"] = partner_type
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["type"] = type
            __props__.__dict__["changed_time"] = None
            __props__.__dict__["created_time"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:logic:IntegrationAccountPartner"), pulumi.Alias(type_="azure-native:logic/v20160601:IntegrationAccountPartner"), pulumi.Alias(type_="azure-native:logic/v20180701preview:IntegrationAccountPartner"), pulumi.Alias(type_="azure-native:logic/v20190501:IntegrationAccountPartner")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(IntegrationAccountPartner, __self__).__init__(
            'azure-native:logic/v20150801preview:IntegrationAccountPartner',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IntegrationAccountPartner':
        """
        Get an existing IntegrationAccountPartner resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IntegrationAccountPartnerArgs.__new__(IntegrationAccountPartnerArgs)

        __props__.__dict__["changed_time"] = None
        __props__.__dict__["content"] = None
        __props__.__dict__["created_time"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["partner_type"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return IntegrationAccountPartner(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> pulumi.Output[str]:
        """
        The changed time.
        """
        return pulumi.get(self, "changed_time")

    @property
    @pulumi.getter
    def content(self) -> pulumi.Output[Optional['outputs.PartnerContentResponse']]:
        """
        The partner content.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[str]:
        """
        The created time.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Any]]:
        """
        The metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnerType")
    def partner_type(self) -> pulumi.Output[Optional[str]]:
        """
        The partner type.
        """
        return pulumi.get(self, "partner_type")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

