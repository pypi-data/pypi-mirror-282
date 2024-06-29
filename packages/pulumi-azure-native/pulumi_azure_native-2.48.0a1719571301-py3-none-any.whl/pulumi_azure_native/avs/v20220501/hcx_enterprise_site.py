# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['HcxEnterpriseSiteArgs', 'HcxEnterpriseSite']

@pulumi.input_type
class HcxEnterpriseSiteArgs:
    def __init__(__self__, *,
                 private_cloud_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 hcx_enterprise_site_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a HcxEnterpriseSite resource.
        :param pulumi.Input[str] private_cloud_name: The name of the private cloud.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] hcx_enterprise_site_name: Name of the HCX Enterprise Site in the private cloud
        """
        pulumi.set(__self__, "private_cloud_name", private_cloud_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if hcx_enterprise_site_name is not None:
            pulumi.set(__self__, "hcx_enterprise_site_name", hcx_enterprise_site_name)

    @property
    @pulumi.getter(name="privateCloudName")
    def private_cloud_name(self) -> pulumi.Input[str]:
        """
        The name of the private cloud.
        """
        return pulumi.get(self, "private_cloud_name")

    @private_cloud_name.setter
    def private_cloud_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "private_cloud_name", value)

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
    @pulumi.getter(name="hcxEnterpriseSiteName")
    def hcx_enterprise_site_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the HCX Enterprise Site in the private cloud
        """
        return pulumi.get(self, "hcx_enterprise_site_name")

    @hcx_enterprise_site_name.setter
    def hcx_enterprise_site_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hcx_enterprise_site_name", value)


class HcxEnterpriseSite(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hcx_enterprise_site_name: Optional[pulumi.Input[str]] = None,
                 private_cloud_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An HCX Enterprise Site resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] hcx_enterprise_site_name: Name of the HCX Enterprise Site in the private cloud
        :param pulumi.Input[str] private_cloud_name: The name of the private cloud.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HcxEnterpriseSiteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An HCX Enterprise Site resource

        :param str resource_name: The name of the resource.
        :param HcxEnterpriseSiteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HcxEnterpriseSiteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hcx_enterprise_site_name: Optional[pulumi.Input[str]] = None,
                 private_cloud_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HcxEnterpriseSiteArgs.__new__(HcxEnterpriseSiteArgs)

            __props__.__dict__["hcx_enterprise_site_name"] = hcx_enterprise_site_name
            if private_cloud_name is None and not opts.urn:
                raise TypeError("Missing required property 'private_cloud_name'")
            __props__.__dict__["private_cloud_name"] = private_cloud_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["activation_key"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:avs:HcxEnterpriseSite"), pulumi.Alias(type_="azure-native:avs/v20200320:HcxEnterpriseSite"), pulumi.Alias(type_="azure-native:avs/v20200717preview:HcxEnterpriseSite"), pulumi.Alias(type_="azure-native:avs/v20210101preview:HcxEnterpriseSite"), pulumi.Alias(type_="azure-native:avs/v20210601:HcxEnterpriseSite"), pulumi.Alias(type_="azure-native:avs/v20211201:HcxEnterpriseSite"), pulumi.Alias(type_="azure-native:avs/v20230301:HcxEnterpriseSite"), pulumi.Alias(type_="azure-native:avs/v20230901:HcxEnterpriseSite")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(HcxEnterpriseSite, __self__).__init__(
            'azure-native:avs/v20220501:HcxEnterpriseSite',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'HcxEnterpriseSite':
        """
        Get an existing HcxEnterpriseSite resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = HcxEnterpriseSiteArgs.__new__(HcxEnterpriseSiteArgs)

        __props__.__dict__["activation_key"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["type"] = None
        return HcxEnterpriseSite(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="activationKey")
    def activation_key(self) -> pulumi.Output[str]:
        """
        The activation key
        """
        return pulumi.get(self, "activation_key")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the HCX Enterprise Site
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

