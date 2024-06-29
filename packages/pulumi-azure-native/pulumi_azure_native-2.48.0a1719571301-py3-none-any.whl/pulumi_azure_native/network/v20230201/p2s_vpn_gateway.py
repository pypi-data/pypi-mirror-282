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

__all__ = ['P2sVpnGatewayArgs', 'P2sVpnGateway']

@pulumi.input_type
class P2sVpnGatewayArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 custom_dns_servers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 gateway_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 is_routing_preference_internet: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 p2_s_connection_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['P2SConnectionConfigurationArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_hub: Optional[pulumi.Input['SubResourceArgs']] = None,
                 vpn_gateway_scale_unit: Optional[pulumi.Input[int]] = None,
                 vpn_server_configuration: Optional[pulumi.Input['SubResourceArgs']] = None):
        """
        The set of arguments for constructing a P2sVpnGateway resource.
        :param pulumi.Input[str] resource_group_name: The resource group name of the P2SVpnGateway.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] custom_dns_servers: List of all customer specified DNS servers IP addresses.
        :param pulumi.Input[str] gateway_name: The name of the gateway.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[bool] is_routing_preference_internet: Enable Routing Preference property for the Public IP Interface of the P2SVpnGateway.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Sequence[pulumi.Input['P2SConnectionConfigurationArgs']]] p2_s_connection_configurations: List of all p2s connection configurations of the gateway.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input['SubResourceArgs'] virtual_hub: The VirtualHub to which the gateway belongs.
        :param pulumi.Input[int] vpn_gateway_scale_unit: The scale unit for this p2s vpn gateway.
        :param pulumi.Input['SubResourceArgs'] vpn_server_configuration: The VpnServerConfiguration to which the p2sVpnGateway is attached to.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if custom_dns_servers is not None:
            pulumi.set(__self__, "custom_dns_servers", custom_dns_servers)
        if gateway_name is not None:
            pulumi.set(__self__, "gateway_name", gateway_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if is_routing_preference_internet is not None:
            pulumi.set(__self__, "is_routing_preference_internet", is_routing_preference_internet)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if p2_s_connection_configurations is not None:
            pulumi.set(__self__, "p2_s_connection_configurations", p2_s_connection_configurations)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if virtual_hub is not None:
            pulumi.set(__self__, "virtual_hub", virtual_hub)
        if vpn_gateway_scale_unit is not None:
            pulumi.set(__self__, "vpn_gateway_scale_unit", vpn_gateway_scale_unit)
        if vpn_server_configuration is not None:
            pulumi.set(__self__, "vpn_server_configuration", vpn_server_configuration)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name of the P2SVpnGateway.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="customDnsServers")
    def custom_dns_servers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of all customer specified DNS servers IP addresses.
        """
        return pulumi.get(self, "custom_dns_servers")

    @custom_dns_servers.setter
    def custom_dns_servers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "custom_dns_servers", value)

    @property
    @pulumi.getter(name="gatewayName")
    def gateway_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the gateway.
        """
        return pulumi.get(self, "gateway_name")

    @gateway_name.setter
    def gateway_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gateway_name", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="isRoutingPreferenceInternet")
    def is_routing_preference_internet(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable Routing Preference property for the Public IP Interface of the P2SVpnGateway.
        """
        return pulumi.get(self, "is_routing_preference_internet")

    @is_routing_preference_internet.setter
    def is_routing_preference_internet(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_routing_preference_internet", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="p2SConnectionConfigurations")
    def p2_s_connection_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['P2SConnectionConfigurationArgs']]]]:
        """
        List of all p2s connection configurations of the gateway.
        """
        return pulumi.get(self, "p2_s_connection_configurations")

    @p2_s_connection_configurations.setter
    def p2_s_connection_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['P2SConnectionConfigurationArgs']]]]):
        pulumi.set(self, "p2_s_connection_configurations", value)

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
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        The VirtualHub to which the gateway belongs.
        """
        return pulumi.get(self, "virtual_hub")

    @virtual_hub.setter
    def virtual_hub(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "virtual_hub", value)

    @property
    @pulumi.getter(name="vpnGatewayScaleUnit")
    def vpn_gateway_scale_unit(self) -> Optional[pulumi.Input[int]]:
        """
        The scale unit for this p2s vpn gateway.
        """
        return pulumi.get(self, "vpn_gateway_scale_unit")

    @vpn_gateway_scale_unit.setter
    def vpn_gateway_scale_unit(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "vpn_gateway_scale_unit", value)

    @property
    @pulumi.getter(name="vpnServerConfiguration")
    def vpn_server_configuration(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        The VpnServerConfiguration to which the p2sVpnGateway is attached to.
        """
        return pulumi.get(self, "vpn_server_configuration")

    @vpn_server_configuration.setter
    def vpn_server_configuration(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "vpn_server_configuration", value)


class P2sVpnGateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_dns_servers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 gateway_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 is_routing_preference_internet: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 p2_s_connection_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['P2SConnectionConfigurationArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_hub: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 vpn_gateway_scale_unit: Optional[pulumi.Input[int]] = None,
                 vpn_server_configuration: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 __props__=None):
        """
        P2SVpnGateway Resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] custom_dns_servers: List of all customer specified DNS servers IP addresses.
        :param pulumi.Input[str] gateway_name: The name of the gateway.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[bool] is_routing_preference_internet: Enable Routing Preference property for the Public IP Interface of the P2SVpnGateway.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['P2SConnectionConfigurationArgs']]]] p2_s_connection_configurations: List of all p2s connection configurations of the gateway.
        :param pulumi.Input[str] resource_group_name: The resource group name of the P2SVpnGateway.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] virtual_hub: The VirtualHub to which the gateway belongs.
        :param pulumi.Input[int] vpn_gateway_scale_unit: The scale unit for this p2s vpn gateway.
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] vpn_server_configuration: The VpnServerConfiguration to which the p2sVpnGateway is attached to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: P2sVpnGatewayArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        P2SVpnGateway Resource.

        :param str resource_name: The name of the resource.
        :param P2sVpnGatewayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(P2sVpnGatewayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_dns_servers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 gateway_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 is_routing_preference_internet: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 p2_s_connection_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['P2SConnectionConfigurationArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_hub: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 vpn_gateway_scale_unit: Optional[pulumi.Input[int]] = None,
                 vpn_server_configuration: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = P2sVpnGatewayArgs.__new__(P2sVpnGatewayArgs)

            __props__.__dict__["custom_dns_servers"] = custom_dns_servers
            __props__.__dict__["gateway_name"] = gateway_name
            __props__.__dict__["id"] = id
            __props__.__dict__["is_routing_preference_internet"] = is_routing_preference_internet
            __props__.__dict__["location"] = location
            __props__.__dict__["p2_s_connection_configurations"] = p2_s_connection_configurations
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["virtual_hub"] = virtual_hub
            __props__.__dict__["vpn_gateway_scale_unit"] = vpn_gateway_scale_unit
            __props__.__dict__["vpn_server_configuration"] = vpn_server_configuration
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["vpn_client_connection_health"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20180801:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20181001:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20181101:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20181201:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20190201:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20190401:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20190601:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20190701:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20190801:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20190901:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20191101:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20191201:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20200301:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20200401:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20200501:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20200601:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20200701:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20200801:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20201101:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20210201:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20210301:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20210501:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20210801:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20220101:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20220501:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20220701:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20220901:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20221101:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20230401:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20230501:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20230601:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20230901:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20231101:P2sVpnGateway"), pulumi.Alias(type_="azure-native:network/v20240101:P2sVpnGateway")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(P2sVpnGateway, __self__).__init__(
            'azure-native:network/v20230201:P2sVpnGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'P2sVpnGateway':
        """
        Get an existing P2sVpnGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = P2sVpnGatewayArgs.__new__(P2sVpnGatewayArgs)

        __props__.__dict__["custom_dns_servers"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["is_routing_preference_internet"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["p2_s_connection_configurations"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_hub"] = None
        __props__.__dict__["vpn_client_connection_health"] = None
        __props__.__dict__["vpn_gateway_scale_unit"] = None
        __props__.__dict__["vpn_server_configuration"] = None
        return P2sVpnGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customDnsServers")
    def custom_dns_servers(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of all customer specified DNS servers IP addresses.
        """
        return pulumi.get(self, "custom_dns_servers")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="isRoutingPreferenceInternet")
    def is_routing_preference_internet(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable Routing Preference property for the Public IP Interface of the P2SVpnGateway.
        """
        return pulumi.get(self, "is_routing_preference_internet")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="p2SConnectionConfigurations")
    def p2_s_connection_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.P2SConnectionConfigurationResponse']]]:
        """
        List of all p2s connection configurations of the gateway.
        """
        return pulumi.get(self, "p2_s_connection_configurations")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the P2S VPN gateway resource.
        """
        return pulumi.get(self, "provisioning_state")

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
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        The VirtualHub to which the gateway belongs.
        """
        return pulumi.get(self, "virtual_hub")

    @property
    @pulumi.getter(name="vpnClientConnectionHealth")
    def vpn_client_connection_health(self) -> pulumi.Output['outputs.VpnClientConnectionHealthResponse']:
        """
        All P2S VPN clients' connection health status.
        """
        return pulumi.get(self, "vpn_client_connection_health")

    @property
    @pulumi.getter(name="vpnGatewayScaleUnit")
    def vpn_gateway_scale_unit(self) -> pulumi.Output[Optional[int]]:
        """
        The scale unit for this p2s vpn gateway.
        """
        return pulumi.get(self, "vpn_gateway_scale_unit")

    @property
    @pulumi.getter(name="vpnServerConfiguration")
    def vpn_server_configuration(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        The VpnServerConfiguration to which the p2sVpnGateway is attached to.
        """
        return pulumi.get(self, "vpn_server_configuration")

