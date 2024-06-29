# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['TrustedIdProviderArgs', 'TrustedIdProvider']

@pulumi.input_type
class TrustedIdProviderArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 id_provider: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 trusted_id_provider_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a TrustedIdProvider resource.
        :param pulumi.Input[str] account_name: The name of the Data Lake Store account.
        :param pulumi.Input[str] id_provider: The URL of this trusted identity provider.
        :param pulumi.Input[str] resource_group_name: The name of the Azure resource group.
        :param pulumi.Input[str] trusted_id_provider_name: The name of the trusted identity provider. This is used for differentiation of providers in the account.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "id_provider", id_provider)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if trusted_id_provider_name is not None:
            pulumi.set(__self__, "trusted_id_provider_name", trusted_id_provider_name)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The name of the Data Lake Store account.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="idProvider")
    def id_provider(self) -> pulumi.Input[str]:
        """
        The URL of this trusted identity provider.
        """
        return pulumi.get(self, "id_provider")

    @id_provider.setter
    def id_provider(self, value: pulumi.Input[str]):
        pulumi.set(self, "id_provider", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Azure resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="trustedIdProviderName")
    def trusted_id_provider_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the trusted identity provider. This is used for differentiation of providers in the account.
        """
        return pulumi.get(self, "trusted_id_provider_name")

    @trusted_id_provider_name.setter
    def trusted_id_provider_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "trusted_id_provider_name", value)


class TrustedIdProvider(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 id_provider: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 trusted_id_provider_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Data Lake Store trusted identity provider information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the Data Lake Store account.
        :param pulumi.Input[str] id_provider: The URL of this trusted identity provider.
        :param pulumi.Input[str] resource_group_name: The name of the Azure resource group.
        :param pulumi.Input[str] trusted_id_provider_name: The name of the trusted identity provider. This is used for differentiation of providers in the account.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TrustedIdProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Data Lake Store trusted identity provider information.

        :param str resource_name: The name of the resource.
        :param TrustedIdProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TrustedIdProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 id_provider: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 trusted_id_provider_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TrustedIdProviderArgs.__new__(TrustedIdProviderArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            if id_provider is None and not opts.urn:
                raise TypeError("Missing required property 'id_provider'")
            __props__.__dict__["id_provider"] = id_provider
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["trusted_id_provider_name"] = trusted_id_provider_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:datalakestore:TrustedIdProvider")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(TrustedIdProvider, __self__).__init__(
            'azure-native:datalakestore/v20161101:TrustedIdProvider',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TrustedIdProvider':
        """
        Get an existing TrustedIdProvider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TrustedIdProviderArgs.__new__(TrustedIdProviderArgs)

        __props__.__dict__["id_provider"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        return TrustedIdProvider(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="idProvider")
    def id_provider(self) -> pulumi.Output[str]:
        """
        The URL of this trusted identity provider.
        """
        return pulumi.get(self, "id_provider")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

