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

__all__ = ['LicenseProfileArgs', 'LicenseProfile']

@pulumi.input_type
class LicenseProfileArgs:
    def __init__(__self__, *,
                 machine_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 assigned_license: Optional[pulumi.Input[str]] = None,
                 license_profile_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a LicenseProfile resource.
        :param pulumi.Input[str] machine_name: The name of the hybrid machine.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] assigned_license: The resource id of the license.
        :param pulumi.Input[str] license_profile_name: The name of the license profile.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "machine_name", machine_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if assigned_license is not None:
            pulumi.set(__self__, "assigned_license", assigned_license)
        if license_profile_name is not None:
            pulumi.set(__self__, "license_profile_name", license_profile_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> pulumi.Input[str]:
        """
        The name of the hybrid machine.
        """
        return pulumi.get(self, "machine_name")

    @machine_name.setter
    def machine_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "machine_name", value)

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
    @pulumi.getter(name="assignedLicense")
    def assigned_license(self) -> Optional[pulumi.Input[str]]:
        """
        The resource id of the license.
        """
        return pulumi.get(self, "assigned_license")

    @assigned_license.setter
    def assigned_license(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "assigned_license", value)

    @property
    @pulumi.getter(name="licenseProfileName")
    def license_profile_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the license profile.
        """
        return pulumi.get(self, "license_profile_name")

    @license_profile_name.setter
    def license_profile_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "license_profile_name", value)

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


class LicenseProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assigned_license: Optional[pulumi.Input[str]] = None,
                 license_profile_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 machine_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Describes a license profile in a hybrid machine.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] assigned_license: The resource id of the license.
        :param pulumi.Input[str] license_profile_name: The name of the license profile.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] machine_name: The name of the hybrid machine.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LicenseProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Describes a license profile in a hybrid machine.

        :param str resource_name: The name of the resource.
        :param LicenseProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LicenseProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assigned_license: Optional[pulumi.Input[str]] = None,
                 license_profile_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 machine_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LicenseProfileArgs.__new__(LicenseProfileArgs)

            __props__.__dict__["assigned_license"] = assigned_license
            __props__.__dict__["license_profile_name"] = license_profile_name
            __props__.__dict__["location"] = location
            if machine_name is None and not opts.urn:
                raise TypeError("Missing required property 'machine_name'")
            __props__.__dict__["machine_name"] = machine_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["assigned_license_immutable_id"] = None
            __props__.__dict__["esu_eligibility"] = None
            __props__.__dict__["esu_key_state"] = None
            __props__.__dict__["esu_keys"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["server_type"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:hybridcompute:LicenseProfile"), pulumi.Alias(type_="azure-native:hybridcompute/v20231003preview:LicenseProfile"), pulumi.Alias(type_="azure-native:hybridcompute/v20240331preview:LicenseProfile"), pulumi.Alias(type_="azure-native:hybridcompute/v20240520preview:LicenseProfile")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(LicenseProfile, __self__).__init__(
            'azure-native:hybridcompute/v20230620preview:LicenseProfile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LicenseProfile':
        """
        Get an existing LicenseProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LicenseProfileArgs.__new__(LicenseProfileArgs)

        __props__.__dict__["assigned_license"] = None
        __props__.__dict__["assigned_license_immutable_id"] = None
        __props__.__dict__["esu_eligibility"] = None
        __props__.__dict__["esu_key_state"] = None
        __props__.__dict__["esu_keys"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["server_type"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return LicenseProfile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="assignedLicense")
    def assigned_license(self) -> pulumi.Output[Optional[str]]:
        """
        The resource id of the license.
        """
        return pulumi.get(self, "assigned_license")

    @property
    @pulumi.getter(name="assignedLicenseImmutableId")
    def assigned_license_immutable_id(self) -> pulumi.Output[str]:
        """
        The guid id of the license.
        """
        return pulumi.get(self, "assigned_license_immutable_id")

    @property
    @pulumi.getter(name="esuEligibility")
    def esu_eligibility(self) -> pulumi.Output[str]:
        """
        Indicates the eligibility state of Esu.
        """
        return pulumi.get(self, "esu_eligibility")

    @property
    @pulumi.getter(name="esuKeyState")
    def esu_key_state(self) -> pulumi.Output[str]:
        """
        Indicates whether there is an ESU Key currently active for the machine.
        """
        return pulumi.get(self, "esu_key_state")

    @property
    @pulumi.getter(name="esuKeys")
    def esu_keys(self) -> pulumi.Output[Sequence['outputs.EsuKeyResponse']]:
        """
        The list of ESU keys.
        """
        return pulumi.get(self, "esu_keys")

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
        The provisioning state, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serverType")
    def server_type(self) -> pulumi.Output[str]:
        """
        The type of the Esu servers.
        """
        return pulumi.get(self, "server_type")

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

