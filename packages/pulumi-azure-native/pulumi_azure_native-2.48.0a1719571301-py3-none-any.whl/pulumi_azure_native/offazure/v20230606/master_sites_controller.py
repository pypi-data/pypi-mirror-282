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

__all__ = ['MasterSitesControllerArgs', 'MasterSitesController']

@pulumi.input_type
class MasterSitesControllerArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 allow_multiple_sites: Optional[pulumi.Input[bool]] = None,
                 customer_storage_account_arm_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'MasterSitePropertiesPublicNetworkAccess']]] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
                 sites: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a MasterSitesController resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[bool] allow_multiple_sites: Gets or sets a value indicating whether multiple sites per site type are
               allowed.
        :param pulumi.Input[str] customer_storage_account_arm_id: Gets or sets a value for customer storage account ARM id.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Union[str, 'MasterSitePropertiesPublicNetworkAccess']] public_network_access: Gets or sets the state of public network access.
        :param pulumi.Input[str] site_name: Site name
        :param pulumi.Input[Sequence[pulumi.Input[str]]] sites: Gets or sets the sites that are a part of Master Site.
                           The key
               should contain the Site ARM name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if allow_multiple_sites is not None:
            pulumi.set(__self__, "allow_multiple_sites", allow_multiple_sites)
        if customer_storage_account_arm_id is not None:
            pulumi.set(__self__, "customer_storage_account_arm_id", customer_storage_account_arm_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)
        if site_name is not None:
            pulumi.set(__self__, "site_name", site_name)
        if sites is not None:
            pulumi.set(__self__, "sites", sites)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="allowMultipleSites")
    def allow_multiple_sites(self) -> Optional[pulumi.Input[bool]]:
        """
        Gets or sets a value indicating whether multiple sites per site type are
        allowed.
        """
        return pulumi.get(self, "allow_multiple_sites")

    @allow_multiple_sites.setter
    def allow_multiple_sites(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_multiple_sites", value)

    @property
    @pulumi.getter(name="customerStorageAccountArmId")
    def customer_storage_account_arm_id(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets a value for customer storage account ARM id.
        """
        return pulumi.get(self, "customer_storage_account_arm_id")

    @customer_storage_account_arm_id.setter
    def customer_storage_account_arm_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "customer_storage_account_arm_id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[str, 'MasterSitePropertiesPublicNetworkAccess']]]:
        """
        Gets or sets the state of public network access.
        """
        return pulumi.get(self, "public_network_access")

    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[str, 'MasterSitePropertiesPublicNetworkAccess']]]):
        pulumi.set(self, "public_network_access", value)

    @property
    @pulumi.getter(name="siteName")
    def site_name(self) -> Optional[pulumi.Input[str]]:
        """
        Site name
        """
        return pulumi.get(self, "site_name")

    @site_name.setter
    def site_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "site_name", value)

    @property
    @pulumi.getter
    def sites(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Gets or sets the sites that are a part of Master Site.
                    The key
        should contain the Site ARM name.
        """
        return pulumi.get(self, "sites")

    @sites.setter
    def sites(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "sites", value)

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


class MasterSitesController(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_multiple_sites: Optional[pulumi.Input[bool]] = None,
                 customer_storage_account_arm_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'MasterSitePropertiesPublicNetworkAccess']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
                 sites: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        A MasterSite

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_multiple_sites: Gets or sets a value indicating whether multiple sites per site type are
               allowed.
        :param pulumi.Input[str] customer_storage_account_arm_id: Gets or sets a value for customer storage account ARM id.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Union[str, 'MasterSitePropertiesPublicNetworkAccess']] public_network_access: Gets or sets the state of public network access.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] site_name: Site name
        :param pulumi.Input[Sequence[pulumi.Input[str]]] sites: Gets or sets the sites that are a part of Master Site.
                           The key
               should contain the Site ARM name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MasterSitesControllerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A MasterSite

        :param str resource_name: The name of the resource.
        :param MasterSitesControllerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MasterSitesControllerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_multiple_sites: Optional[pulumi.Input[bool]] = None,
                 customer_storage_account_arm_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'MasterSitePropertiesPublicNetworkAccess']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
                 sites: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MasterSitesControllerArgs.__new__(MasterSitesControllerArgs)

            __props__.__dict__["allow_multiple_sites"] = allow_multiple_sites
            __props__.__dict__["customer_storage_account_arm_id"] = customer_storage_account_arm_id
            __props__.__dict__["location"] = location
            __props__.__dict__["public_network_access"] = public_network_access
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["site_name"] = site_name
            __props__.__dict__["sites"] = sites
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["nested_sites"] = None
            __props__.__dict__["private_endpoint_connections"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:offazure:MasterSitesController"), pulumi.Alias(type_="azure-native:offazure/v20200707:MasterSitesController"), pulumi.Alias(type_="azure-native:offazure/v20231001preview:MasterSitesController")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(MasterSitesController, __self__).__init__(
            'azure-native:offazure/v20230606:MasterSitesController',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'MasterSitesController':
        """
        Get an existing MasterSitesController resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MasterSitesControllerArgs.__new__(MasterSitesControllerArgs)

        __props__.__dict__["allow_multiple_sites"] = None
        __props__.__dict__["customer_storage_account_arm_id"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["nested_sites"] = None
        __props__.__dict__["private_endpoint_connections"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_network_access"] = None
        __props__.__dict__["sites"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return MasterSitesController(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowMultipleSites")
    def allow_multiple_sites(self) -> pulumi.Output[Optional[bool]]:
        """
        Gets or sets a value indicating whether multiple sites per site type are
        allowed.
        """
        return pulumi.get(self, "allow_multiple_sites")

    @property
    @pulumi.getter(name="customerStorageAccountArmId")
    def customer_storage_account_arm_id(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets a value for customer storage account ARM id.
        """
        return pulumi.get(self, "customer_storage_account_arm_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
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
    @pulumi.getter(name="nestedSites")
    def nested_sites(self) -> pulumi.Output[Sequence[str]]:
        """
        Gets the nested sites under Master Site.
        """
        return pulumi.get(self, "nested_sites")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Sequence['outputs.PrivateEndpointConnectionResponse']]:
        """
        Gets the private endpoint connections.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        provisioning state enum
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the state of public network access.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter
    def sites(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Gets or sets the sites that are a part of Master Site.
                    The key
        should contain the Site ARM name.
        """
        return pulumi.get(self, "sites")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

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
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

