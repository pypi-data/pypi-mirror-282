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

__all__ = ['AvailabilitySetArgs', 'AvailabilitySet']

@pulumi.input_type
class AvailabilitySetArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 availability_set_name: Optional[pulumi.Input[str]] = None,
                 extended_location: Optional[pulumi.Input['ExtendedLocationArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vmm_server_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AvailabilitySet resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] availability_set_name: Name of the availability set.
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: The extended location.
        :param pulumi.Input[str] location: Gets or sets the location.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] vmm_server_id: ARM Id of the vmmServer resource in which this resource resides.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if availability_set_name is not None:
            pulumi.set(__self__, "availability_set_name", availability_set_name)
        if extended_location is not None:
            pulumi.set(__self__, "extended_location", extended_location)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vmm_server_id is not None:
            pulumi.set(__self__, "vmm_server_id", vmm_server_id)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="availabilitySetName")
    def availability_set_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the availability set.
        """
        return pulumi.get(self, "availability_set_name")

    @availability_set_name.setter
    def availability_set_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability_set_name", value)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input['ExtendedLocationArgs']]:
        """
        The extended location.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input['ExtendedLocationArgs']]):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="vmmServerId")
    def vmm_server_id(self) -> Optional[pulumi.Input[str]]:
        """
        ARM Id of the vmmServer resource in which this resource resides.
        """
        return pulumi.get(self, "vmm_server_id")

    @vmm_server_id.setter
    def vmm_server_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vmm_server_id", value)


class AvailabilitySet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability_set_name: Optional[pulumi.Input[str]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vmm_server_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The AvailabilitySets resource definition.
        Azure REST API version: 2022-05-21-preview. Prior API version in Azure Native 1.x: 2020-06-05-preview.

        Other available API versions: 2023-04-01-preview, 2023-10-07.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] availability_set_name: Name of the availability set.
        :param pulumi.Input[pulumi.InputType['ExtendedLocationArgs']] extended_location: The extended location.
        :param pulumi.Input[str] location: Gets or sets the location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] vmm_server_id: ARM Id of the vmmServer resource in which this resource resides.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AvailabilitySetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AvailabilitySets resource definition.
        Azure REST API version: 2022-05-21-preview. Prior API version in Azure Native 1.x: 2020-06-05-preview.

        Other available API versions: 2023-04-01-preview, 2023-10-07.

        :param str resource_name: The name of the resource.
        :param AvailabilitySetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AvailabilitySetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability_set_name: Optional[pulumi.Input[str]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vmm_server_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AvailabilitySetArgs.__new__(AvailabilitySetArgs)

            __props__.__dict__["availability_set_name"] = availability_set_name
            __props__.__dict__["extended_location"] = extended_location
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vmm_server_id"] = vmm_server_id
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:scvmm/v20200605preview:AvailabilitySet"), pulumi.Alias(type_="azure-native:scvmm/v20220521preview:AvailabilitySet"), pulumi.Alias(type_="azure-native:scvmm/v20230401preview:AvailabilitySet"), pulumi.Alias(type_="azure-native:scvmm/v20231007:AvailabilitySet")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AvailabilitySet, __self__).__init__(
            'azure-native:scvmm:AvailabilitySet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AvailabilitySet':
        """
        Get an existing AvailabilitySet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AvailabilitySetArgs.__new__(AvailabilitySetArgs)

        __props__.__dict__["availability_set_name"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vmm_server_id"] = None
        return AvailabilitySet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="availabilitySetName")
    def availability_set_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the availability set.
        """
        return pulumi.get(self, "availability_set_name")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional['outputs.ExtendedLocationResponse']]:
        """
        The extended location.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Gets or sets the provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system data.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource Type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vmmServerId")
    def vmm_server_id(self) -> pulumi.Output[Optional[str]]:
        """
        ARM Id of the vmmServer resource in which this resource resides.
        """
        return pulumi.get(self, "vmm_server_id")

