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
from ._enums import *
from ._inputs import *

__all__ = ['LogicalNetworkArgs', 'LogicalNetwork']

@pulumi.input_type
class LogicalNetworkArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 dhcp_options: Optional[pulumi.Input['LogicalNetworkPropertiesDhcpOptionsArgs']] = None,
                 extended_location: Optional[pulumi.Input['ExtendedLocationArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 logical_network_name: Optional[pulumi.Input[str]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input['SubnetArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vm_switch_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a LogicalNetwork resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['LogicalNetworkPropertiesDhcpOptionsArgs'] dhcp_options: DhcpOptions contains an array of DNS servers available to VMs deployed in the logical network. Standard DHCP option for a subnet overrides logical network DHCP options.
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: The extendedLocation of the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] logical_network_name: Name of the logical network
        :param pulumi.Input[Sequence[pulumi.Input['SubnetArgs']]] subnets: Subnet - list of subnets under the logical network
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] vm_switch_name: name of the network switch to be used for VMs
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if dhcp_options is not None:
            pulumi.set(__self__, "dhcp_options", dhcp_options)
        if extended_location is not None:
            pulumi.set(__self__, "extended_location", extended_location)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if logical_network_name is not None:
            pulumi.set(__self__, "logical_network_name", logical_network_name)
        if subnets is not None:
            pulumi.set(__self__, "subnets", subnets)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vm_switch_name is not None:
            pulumi.set(__self__, "vm_switch_name", vm_switch_name)

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
    @pulumi.getter(name="dhcpOptions")
    def dhcp_options(self) -> Optional[pulumi.Input['LogicalNetworkPropertiesDhcpOptionsArgs']]:
        """
        DhcpOptions contains an array of DNS servers available to VMs deployed in the logical network. Standard DHCP option for a subnet overrides logical network DHCP options.
        """
        return pulumi.get(self, "dhcp_options")

    @dhcp_options.setter
    def dhcp_options(self, value: Optional[pulumi.Input['LogicalNetworkPropertiesDhcpOptionsArgs']]):
        pulumi.set(self, "dhcp_options", value)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input['ExtendedLocationArgs']]:
        """
        The extendedLocation of the resource.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input['ExtendedLocationArgs']]):
        pulumi.set(self, "extended_location", value)

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
    @pulumi.getter(name="logicalNetworkName")
    def logical_network_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the logical network
        """
        return pulumi.get(self, "logical_network_name")

    @logical_network_name.setter
    def logical_network_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "logical_network_name", value)

    @property
    @pulumi.getter
    def subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SubnetArgs']]]]:
        """
        Subnet - list of subnets under the logical network
        """
        return pulumi.get(self, "subnets")

    @subnets.setter
    def subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SubnetArgs']]]]):
        pulumi.set(self, "subnets", value)

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

    @property
    @pulumi.getter(name="vmSwitchName")
    def vm_switch_name(self) -> Optional[pulumi.Input[str]]:
        """
        name of the network switch to be used for VMs
        """
        return pulumi.get(self, "vm_switch_name")

    @vm_switch_name.setter
    def vm_switch_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vm_switch_name", value)


class LogicalNetwork(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dhcp_options: Optional[pulumi.Input[pulumi.InputType['LogicalNetworkPropertiesDhcpOptionsArgs']]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 logical_network_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vm_switch_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The logical network resource definition.
        Azure REST API version: 2023-09-01-preview.

        Other available API versions: 2024-01-01, 2024-02-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['LogicalNetworkPropertiesDhcpOptionsArgs']] dhcp_options: DhcpOptions contains an array of DNS servers available to VMs deployed in the logical network. Standard DHCP option for a subnet overrides logical network DHCP options.
        :param pulumi.Input[pulumi.InputType['ExtendedLocationArgs']] extended_location: The extendedLocation of the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] logical_network_name: Name of the logical network
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetArgs']]]] subnets: Subnet - list of subnets under the logical network
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] vm_switch_name: name of the network switch to be used for VMs
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LogicalNetworkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The logical network resource definition.
        Azure REST API version: 2023-09-01-preview.

        Other available API versions: 2024-01-01, 2024-02-01-preview.

        :param str resource_name: The name of the resource.
        :param LogicalNetworkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LogicalNetworkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dhcp_options: Optional[pulumi.Input[pulumi.InputType['LogicalNetworkPropertiesDhcpOptionsArgs']]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 logical_network_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vm_switch_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LogicalNetworkArgs.__new__(LogicalNetworkArgs)

            __props__.__dict__["dhcp_options"] = dhcp_options
            __props__.__dict__["extended_location"] = extended_location
            __props__.__dict__["location"] = location
            __props__.__dict__["logical_network_name"] = logical_network_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["subnets"] = subnets
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vm_switch_name"] = vm_switch_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:azurestackhci/v20230901preview:LogicalNetwork"), pulumi.Alias(type_="azure-native:azurestackhci/v20240101:LogicalNetwork"), pulumi.Alias(type_="azure-native:azurestackhci/v20240201preview:LogicalNetwork")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(LogicalNetwork, __self__).__init__(
            'azure-native:azurestackhci:LogicalNetwork',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LogicalNetwork':
        """
        Get an existing LogicalNetwork resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LogicalNetworkArgs.__new__(LogicalNetworkArgs)

        __props__.__dict__["dhcp_options"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["subnets"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vm_switch_name"] = None
        return LogicalNetwork(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dhcpOptions")
    def dhcp_options(self) -> pulumi.Output[Optional['outputs.LogicalNetworkPropertiesResponseDhcpOptions']]:
        """
        DhcpOptions contains an array of DNS servers available to VMs deployed in the logical network. Standard DHCP option for a subnet overrides logical network DHCP options.
        """
        return pulumi.get(self, "dhcp_options")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional['outputs.ExtendedLocationResponse']]:
        """
        The extendedLocation of the resource.
        """
        return pulumi.get(self, "extended_location")

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
        Provisioning state of the logical network.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.LogicalNetworkStatusResponse']:
        """
        The observed state of logical networks
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def subnets(self) -> pulumi.Output[Optional[Sequence['outputs.SubnetResponse']]]:
        """
        Subnet - list of subnets under the logical network
        """
        return pulumi.get(self, "subnets")

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

    @property
    @pulumi.getter(name="vmSwitchName")
    def vm_switch_name(self) -> pulumi.Output[Optional[str]]:
        """
        name of the network switch to be used for VMs
        """
        return pulumi.get(self, "vm_switch_name")

