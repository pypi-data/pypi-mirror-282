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

__all__ = ['InternalNetworkArgs', 'InternalNetwork']

@pulumi.input_type
class InternalNetworkArgs:
    def __init__(__self__, *,
                 l3_isolation_domain_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 vlan_id: pulumi.Input[int],
                 annotation: Optional[pulumi.Input[str]] = None,
                 bgp_configuration: Optional[pulumi.Input['BgpConfigurationArgs']] = None,
                 connected_i_pv4_subnets: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectedSubnetArgs']]]] = None,
                 connected_i_pv6_subnets: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectedSubnetArgs']]]] = None,
                 export_route_policy_id: Optional[pulumi.Input[str]] = None,
                 import_route_policy_id: Optional[pulumi.Input[str]] = None,
                 internal_network_name: Optional[pulumi.Input[str]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 static_route_configuration: Optional[pulumi.Input['StaticRouteConfigurationArgs']] = None):
        """
        The set of arguments for constructing a InternalNetwork resource.
        :param pulumi.Input[str] l3_isolation_domain_name: Name of the L3IsolationDomain
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[int] vlan_id: Vlan identifier. Example: 1001.
        :param pulumi.Input[str] annotation: Switch configuration description.
        :param pulumi.Input['BgpConfigurationArgs'] bgp_configuration: BGP configuration properties
        :param pulumi.Input[Sequence[pulumi.Input['ConnectedSubnetArgs']]] connected_i_pv4_subnets: List with object connected IPv4 Subnets.
        :param pulumi.Input[Sequence[pulumi.Input['ConnectedSubnetArgs']]] connected_i_pv6_subnets: List with object connected IPv6 Subnets.
        :param pulumi.Input[str] export_route_policy_id: ARM resource ID of importRoutePolicy.
        :param pulumi.Input[str] import_route_policy_id: ARM resource ID of importRoutePolicy.
        :param pulumi.Input[str] internal_network_name: Name of the InternalNetwork
        :param pulumi.Input[int] mtu: Maximum transmission unit. Default value is 1500.
        :param pulumi.Input['StaticRouteConfigurationArgs'] static_route_configuration: Static Route Configuration properties.
        """
        pulumi.set(__self__, "l3_isolation_domain_name", l3_isolation_domain_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "vlan_id", vlan_id)
        if annotation is not None:
            pulumi.set(__self__, "annotation", annotation)
        if bgp_configuration is not None:
            pulumi.set(__self__, "bgp_configuration", bgp_configuration)
        if connected_i_pv4_subnets is not None:
            pulumi.set(__self__, "connected_i_pv4_subnets", connected_i_pv4_subnets)
        if connected_i_pv6_subnets is not None:
            pulumi.set(__self__, "connected_i_pv6_subnets", connected_i_pv6_subnets)
        if export_route_policy_id is not None:
            pulumi.set(__self__, "export_route_policy_id", export_route_policy_id)
        if import_route_policy_id is not None:
            pulumi.set(__self__, "import_route_policy_id", import_route_policy_id)
        if internal_network_name is not None:
            pulumi.set(__self__, "internal_network_name", internal_network_name)
        if mtu is None:
            mtu = 1500
        if mtu is not None:
            pulumi.set(__self__, "mtu", mtu)
        if static_route_configuration is not None:
            pulumi.set(__self__, "static_route_configuration", static_route_configuration)

    @property
    @pulumi.getter(name="l3IsolationDomainName")
    def l3_isolation_domain_name(self) -> pulumi.Input[str]:
        """
        Name of the L3IsolationDomain
        """
        return pulumi.get(self, "l3_isolation_domain_name")

    @l3_isolation_domain_name.setter
    def l3_isolation_domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "l3_isolation_domain_name", value)

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
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> pulumi.Input[int]:
        """
        Vlan identifier. Example: 1001.
        """
        return pulumi.get(self, "vlan_id")

    @vlan_id.setter
    def vlan_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "vlan_id", value)

    @property
    @pulumi.getter
    def annotation(self) -> Optional[pulumi.Input[str]]:
        """
        Switch configuration description.
        """
        return pulumi.get(self, "annotation")

    @annotation.setter
    def annotation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "annotation", value)

    @property
    @pulumi.getter(name="bgpConfiguration")
    def bgp_configuration(self) -> Optional[pulumi.Input['BgpConfigurationArgs']]:
        """
        BGP configuration properties
        """
        return pulumi.get(self, "bgp_configuration")

    @bgp_configuration.setter
    def bgp_configuration(self, value: Optional[pulumi.Input['BgpConfigurationArgs']]):
        pulumi.set(self, "bgp_configuration", value)

    @property
    @pulumi.getter(name="connectedIPv4Subnets")
    def connected_i_pv4_subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConnectedSubnetArgs']]]]:
        """
        List with object connected IPv4 Subnets.
        """
        return pulumi.get(self, "connected_i_pv4_subnets")

    @connected_i_pv4_subnets.setter
    def connected_i_pv4_subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectedSubnetArgs']]]]):
        pulumi.set(self, "connected_i_pv4_subnets", value)

    @property
    @pulumi.getter(name="connectedIPv6Subnets")
    def connected_i_pv6_subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConnectedSubnetArgs']]]]:
        """
        List with object connected IPv6 Subnets.
        """
        return pulumi.get(self, "connected_i_pv6_subnets")

    @connected_i_pv6_subnets.setter
    def connected_i_pv6_subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectedSubnetArgs']]]]):
        pulumi.set(self, "connected_i_pv6_subnets", value)

    @property
    @pulumi.getter(name="exportRoutePolicyId")
    def export_route_policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        ARM resource ID of importRoutePolicy.
        """
        return pulumi.get(self, "export_route_policy_id")

    @export_route_policy_id.setter
    def export_route_policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "export_route_policy_id", value)

    @property
    @pulumi.getter(name="importRoutePolicyId")
    def import_route_policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        ARM resource ID of importRoutePolicy.
        """
        return pulumi.get(self, "import_route_policy_id")

    @import_route_policy_id.setter
    def import_route_policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "import_route_policy_id", value)

    @property
    @pulumi.getter(name="internalNetworkName")
    def internal_network_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the InternalNetwork
        """
        return pulumi.get(self, "internal_network_name")

    @internal_network_name.setter
    def internal_network_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "internal_network_name", value)

    @property
    @pulumi.getter
    def mtu(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum transmission unit. Default value is 1500.
        """
        return pulumi.get(self, "mtu")

    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "mtu", value)

    @property
    @pulumi.getter(name="staticRouteConfiguration")
    def static_route_configuration(self) -> Optional[pulumi.Input['StaticRouteConfigurationArgs']]:
        """
        Static Route Configuration properties.
        """
        return pulumi.get(self, "static_route_configuration")

    @static_route_configuration.setter
    def static_route_configuration(self, value: Optional[pulumi.Input['StaticRouteConfigurationArgs']]):
        pulumi.set(self, "static_route_configuration", value)


class InternalNetwork(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotation: Optional[pulumi.Input[str]] = None,
                 bgp_configuration: Optional[pulumi.Input[pulumi.InputType['BgpConfigurationArgs']]] = None,
                 connected_i_pv4_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectedSubnetArgs']]]]] = None,
                 connected_i_pv6_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectedSubnetArgs']]]]] = None,
                 export_route_policy_id: Optional[pulumi.Input[str]] = None,
                 import_route_policy_id: Optional[pulumi.Input[str]] = None,
                 internal_network_name: Optional[pulumi.Input[str]] = None,
                 l3_isolation_domain_name: Optional[pulumi.Input[str]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 static_route_configuration: Optional[pulumi.Input[pulumi.InputType['StaticRouteConfigurationArgs']]] = None,
                 vlan_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Defines the InternalNetwork item.
        Azure REST API version: 2023-02-01-preview. Prior API version in Azure Native 1.x: 2023-02-01-preview.

        Other available API versions: 2023-06-15.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] annotation: Switch configuration description.
        :param pulumi.Input[pulumi.InputType['BgpConfigurationArgs']] bgp_configuration: BGP configuration properties
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectedSubnetArgs']]]] connected_i_pv4_subnets: List with object connected IPv4 Subnets.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectedSubnetArgs']]]] connected_i_pv6_subnets: List with object connected IPv6 Subnets.
        :param pulumi.Input[str] export_route_policy_id: ARM resource ID of importRoutePolicy.
        :param pulumi.Input[str] import_route_policy_id: ARM resource ID of importRoutePolicy.
        :param pulumi.Input[str] internal_network_name: Name of the InternalNetwork
        :param pulumi.Input[str] l3_isolation_domain_name: Name of the L3IsolationDomain
        :param pulumi.Input[int] mtu: Maximum transmission unit. Default value is 1500.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[pulumi.InputType['StaticRouteConfigurationArgs']] static_route_configuration: Static Route Configuration properties.
        :param pulumi.Input[int] vlan_id: Vlan identifier. Example: 1001.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InternalNetworkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Defines the InternalNetwork item.
        Azure REST API version: 2023-02-01-preview. Prior API version in Azure Native 1.x: 2023-02-01-preview.

        Other available API versions: 2023-06-15.

        :param str resource_name: The name of the resource.
        :param InternalNetworkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InternalNetworkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotation: Optional[pulumi.Input[str]] = None,
                 bgp_configuration: Optional[pulumi.Input[pulumi.InputType['BgpConfigurationArgs']]] = None,
                 connected_i_pv4_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectedSubnetArgs']]]]] = None,
                 connected_i_pv6_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectedSubnetArgs']]]]] = None,
                 export_route_policy_id: Optional[pulumi.Input[str]] = None,
                 import_route_policy_id: Optional[pulumi.Input[str]] = None,
                 internal_network_name: Optional[pulumi.Input[str]] = None,
                 l3_isolation_domain_name: Optional[pulumi.Input[str]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 static_route_configuration: Optional[pulumi.Input[pulumi.InputType['StaticRouteConfigurationArgs']]] = None,
                 vlan_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InternalNetworkArgs.__new__(InternalNetworkArgs)

            __props__.__dict__["annotation"] = annotation
            __props__.__dict__["bgp_configuration"] = bgp_configuration
            __props__.__dict__["connected_i_pv4_subnets"] = connected_i_pv4_subnets
            __props__.__dict__["connected_i_pv6_subnets"] = connected_i_pv6_subnets
            __props__.__dict__["export_route_policy_id"] = export_route_policy_id
            __props__.__dict__["import_route_policy_id"] = import_route_policy_id
            __props__.__dict__["internal_network_name"] = internal_network_name
            if l3_isolation_domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'l3_isolation_domain_name'")
            __props__.__dict__["l3_isolation_domain_name"] = l3_isolation_domain_name
            if mtu is None:
                mtu = 1500
            __props__.__dict__["mtu"] = mtu
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["static_route_configuration"] = static_route_configuration
            if vlan_id is None and not opts.urn:
                raise TypeError("Missing required property 'vlan_id'")
            __props__.__dict__["vlan_id"] = vlan_id
            __props__.__dict__["administrative_state"] = None
            __props__.__dict__["bfd_disabled_on_resources"] = None
            __props__.__dict__["bfd_for_static_routes_disabled_on_resources"] = None
            __props__.__dict__["bgp_disabled_on_resources"] = None
            __props__.__dict__["disabled_on_resources"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:managednetworkfabric/v20230201preview:InternalNetwork"), pulumi.Alias(type_="azure-native:managednetworkfabric/v20230615:InternalNetwork")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(InternalNetwork, __self__).__init__(
            'azure-native:managednetworkfabric:InternalNetwork',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'InternalNetwork':
        """
        Get an existing InternalNetwork resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InternalNetworkArgs.__new__(InternalNetworkArgs)

        __props__.__dict__["administrative_state"] = None
        __props__.__dict__["annotation"] = None
        __props__.__dict__["bfd_disabled_on_resources"] = None
        __props__.__dict__["bfd_for_static_routes_disabled_on_resources"] = None
        __props__.__dict__["bgp_configuration"] = None
        __props__.__dict__["bgp_disabled_on_resources"] = None
        __props__.__dict__["connected_i_pv4_subnets"] = None
        __props__.__dict__["connected_i_pv6_subnets"] = None
        __props__.__dict__["disabled_on_resources"] = None
        __props__.__dict__["export_route_policy_id"] = None
        __props__.__dict__["import_route_policy_id"] = None
        __props__.__dict__["mtu"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["static_route_configuration"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vlan_id"] = None
        return InternalNetwork(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> pulumi.Output[str]:
        """
        Administrative state of the InternalNetwork. Example: Enabled | Disabled.
        """
        return pulumi.get(self, "administrative_state")

    @property
    @pulumi.getter
    def annotation(self) -> pulumi.Output[Optional[str]]:
        """
        Switch configuration description.
        """
        return pulumi.get(self, "annotation")

    @property
    @pulumi.getter(name="bfdDisabledOnResources")
    def bfd_disabled_on_resources(self) -> pulumi.Output[Sequence[str]]:
        """
        List of resources the BFD for BGP is disabled on. Can be either entire NetworkFabric or NetworkRack.
        """
        return pulumi.get(self, "bfd_disabled_on_resources")

    @property
    @pulumi.getter(name="bfdForStaticRoutesDisabledOnResources")
    def bfd_for_static_routes_disabled_on_resources(self) -> pulumi.Output[Sequence[str]]:
        """
        List of resources the BFD of StaticRoutes is disabled on. Can be either entire NetworkFabric or NetworkRack.
        """
        return pulumi.get(self, "bfd_for_static_routes_disabled_on_resources")

    @property
    @pulumi.getter(name="bgpConfiguration")
    def bgp_configuration(self) -> pulumi.Output[Optional['outputs.BgpConfigurationResponse']]:
        """
        BGP configuration properties
        """
        return pulumi.get(self, "bgp_configuration")

    @property
    @pulumi.getter(name="bgpDisabledOnResources")
    def bgp_disabled_on_resources(self) -> pulumi.Output[Sequence[str]]:
        """
        List of resources the BGP is disabled on. Can be either entire NetworkFabric or NetworkRack.
        """
        return pulumi.get(self, "bgp_disabled_on_resources")

    @property
    @pulumi.getter(name="connectedIPv4Subnets")
    def connected_i_pv4_subnets(self) -> pulumi.Output[Optional[Sequence['outputs.ConnectedSubnetResponse']]]:
        """
        List with object connected IPv4 Subnets.
        """
        return pulumi.get(self, "connected_i_pv4_subnets")

    @property
    @pulumi.getter(name="connectedIPv6Subnets")
    def connected_i_pv6_subnets(self) -> pulumi.Output[Optional[Sequence['outputs.ConnectedSubnetResponse']]]:
        """
        List with object connected IPv6 Subnets.
        """
        return pulumi.get(self, "connected_i_pv6_subnets")

    @property
    @pulumi.getter(name="disabledOnResources")
    def disabled_on_resources(self) -> pulumi.Output[Sequence[str]]:
        """
        List of resources the InternalNetwork is disabled on. Can be either entire NetworkFabric or NetworkRack.
        """
        return pulumi.get(self, "disabled_on_resources")

    @property
    @pulumi.getter(name="exportRoutePolicyId")
    def export_route_policy_id(self) -> pulumi.Output[Optional[str]]:
        """
        ARM resource ID of importRoutePolicy.
        """
        return pulumi.get(self, "export_route_policy_id")

    @property
    @pulumi.getter(name="importRoutePolicyId")
    def import_route_policy_id(self) -> pulumi.Output[Optional[str]]:
        """
        ARM resource ID of importRoutePolicy.
        """
        return pulumi.get(self, "import_route_policy_id")

    @property
    @pulumi.getter
    def mtu(self) -> pulumi.Output[Optional[int]]:
        """
        Maximum transmission unit. Default value is 1500.
        """
        return pulumi.get(self, "mtu")

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
        Gets the provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="staticRouteConfiguration")
    def static_route_configuration(self) -> pulumi.Output[Optional['outputs.StaticRouteConfigurationResponse']]:
        """
        Static Route Configuration properties.
        """
        return pulumi.get(self, "static_route_configuration")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> pulumi.Output[int]:
        """
        Vlan identifier. Example: 1001.
        """
        return pulumi.get(self, "vlan_id")

