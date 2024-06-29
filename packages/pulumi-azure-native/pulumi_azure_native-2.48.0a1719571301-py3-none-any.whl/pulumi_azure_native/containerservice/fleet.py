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
from ._inputs import *

__all__ = ['FleetArgs', 'Fleet']

@pulumi.input_type
class FleetArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 fleet_name: Optional[pulumi.Input[str]] = None,
                 hub_profile: Optional[pulumi.Input['FleetHubProfileArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Fleet resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] fleet_name: The name of the Fleet resource.
        :param pulumi.Input['FleetHubProfileArgs'] hub_profile: The FleetHubProfile configures the Fleet's hub.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if fleet_name is not None:
            pulumi.set(__self__, "fleet_name", fleet_name)
        if hub_profile is not None:
            pulumi.set(__self__, "hub_profile", hub_profile)
        if location is not None:
            pulumi.set(__self__, "location", location)
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
    @pulumi.getter(name="fleetName")
    def fleet_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Fleet resource.
        """
        return pulumi.get(self, "fleet_name")

    @fleet_name.setter
    def fleet_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fleet_name", value)

    @property
    @pulumi.getter(name="hubProfile")
    def hub_profile(self) -> Optional[pulumi.Input['FleetHubProfileArgs']]:
        """
        The FleetHubProfile configures the Fleet's hub.
        """
        return pulumi.get(self, "hub_profile")

    @hub_profile.setter
    def hub_profile(self, value: Optional[pulumi.Input['FleetHubProfileArgs']]):
        pulumi.set(self, "hub_profile", value)

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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Fleet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fleet_name: Optional[pulumi.Input[str]] = None,
                 hub_profile: Optional[pulumi.Input[pulumi.InputType['FleetHubProfileArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The Fleet resource.
        Azure REST API version: 2023-03-15-preview.

        Other available API versions: 2022-07-02-preview, 2023-06-15-preview, 2023-08-15-preview, 2023-10-15, 2024-02-02-preview, 2024-04-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] fleet_name: The name of the Fleet resource.
        :param pulumi.Input[pulumi.InputType['FleetHubProfileArgs']] hub_profile: The FleetHubProfile configures the Fleet's hub.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FleetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Fleet resource.
        Azure REST API version: 2023-03-15-preview.

        Other available API versions: 2022-07-02-preview, 2023-06-15-preview, 2023-08-15-preview, 2023-10-15, 2024-02-02-preview, 2024-04-01.

        :param str resource_name: The name of the resource.
        :param FleetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FleetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fleet_name: Optional[pulumi.Input[str]] = None,
                 hub_profile: Optional[pulumi.Input[pulumi.InputType['FleetHubProfileArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FleetArgs.__new__(FleetArgs)

            __props__.__dict__["fleet_name"] = fleet_name
            __props__.__dict__["hub_profile"] = hub_profile
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["e_tag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:containerservice/v20220602preview:Fleet"), pulumi.Alias(type_="azure-native:containerservice/v20220702preview:Fleet"), pulumi.Alias(type_="azure-native:containerservice/v20220902preview:Fleet"), pulumi.Alias(type_="azure-native:containerservice/v20230315preview:Fleet"), pulumi.Alias(type_="azure-native:containerservice/v20230615preview:Fleet"), pulumi.Alias(type_="azure-native:containerservice/v20230815preview:Fleet"), pulumi.Alias(type_="azure-native:containerservice/v20231015:Fleet"), pulumi.Alias(type_="azure-native:containerservice/v20240202preview:Fleet"), pulumi.Alias(type_="azure-native:containerservice/v20240401:Fleet")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Fleet, __self__).__init__(
            'azure-native:containerservice:Fleet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Fleet':
        """
        Get an existing Fleet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FleetArgs.__new__(FleetArgs)

        __props__.__dict__["e_tag"] = None
        __props__.__dict__["hub_profile"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Fleet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[str]:
        """
        If eTag is provided in the response body, it may also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter(name="hubProfile")
    def hub_profile(self) -> pulumi.Output[Optional['outputs.FleetHubProfileResponse']]:
        """
        The FleetHubProfile configures the Fleet's hub.
        """
        return pulumi.get(self, "hub_profile")

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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

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

