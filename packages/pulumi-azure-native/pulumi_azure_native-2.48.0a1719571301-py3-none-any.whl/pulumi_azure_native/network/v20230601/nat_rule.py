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

__all__ = ['NatRuleInitArgs', 'NatRule']

@pulumi.input_type
class NatRuleInitArgs:
    def __init__(__self__, *,
                 gateway_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 external_mappings: Optional[pulumi.Input[Sequence[pulumi.Input['VpnNatRuleMappingArgs']]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 internal_mappings: Optional[pulumi.Input[Sequence[pulumi.Input['VpnNatRuleMappingArgs']]]] = None,
                 ip_configuration_id: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input[Union[str, 'VpnNatRuleMode']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nat_rule_name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[Union[str, 'VpnNatRuleType']]] = None):
        """
        The set of arguments for constructing a NatRule resource.
        :param pulumi.Input[str] gateway_name: The name of the gateway.
        :param pulumi.Input[str] resource_group_name: The resource group name of the VpnGateway.
        :param pulumi.Input[Sequence[pulumi.Input['VpnNatRuleMappingArgs']]] external_mappings: The private IP address external mapping for NAT.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[Sequence[pulumi.Input['VpnNatRuleMappingArgs']]] internal_mappings: The private IP address internal mapping for NAT.
        :param pulumi.Input[str] ip_configuration_id: The IP Configuration ID this NAT rule applies to.
        :param pulumi.Input[Union[str, 'VpnNatRuleMode']] mode: The Source NAT direction of a VPN NAT.
        :param pulumi.Input[str] name: The name of the resource that is unique within a resource group. This name can be used to access the resource.
        :param pulumi.Input[str] nat_rule_name: The name of the nat rule.
        :param pulumi.Input[Union[str, 'VpnNatRuleType']] type: The type of NAT rule for VPN NAT.
        """
        pulumi.set(__self__, "gateway_name", gateway_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if external_mappings is not None:
            pulumi.set(__self__, "external_mappings", external_mappings)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if internal_mappings is not None:
            pulumi.set(__self__, "internal_mappings", internal_mappings)
        if ip_configuration_id is not None:
            pulumi.set(__self__, "ip_configuration_id", ip_configuration_id)
        if mode is not None:
            pulumi.set(__self__, "mode", mode)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if nat_rule_name is not None:
            pulumi.set(__self__, "nat_rule_name", nat_rule_name)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="gatewayName")
    def gateway_name(self) -> pulumi.Input[str]:
        """
        The name of the gateway.
        """
        return pulumi.get(self, "gateway_name")

    @gateway_name.setter
    def gateway_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "gateway_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name of the VpnGateway.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="externalMappings")
    def external_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VpnNatRuleMappingArgs']]]]:
        """
        The private IP address external mapping for NAT.
        """
        return pulumi.get(self, "external_mappings")

    @external_mappings.setter
    def external_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VpnNatRuleMappingArgs']]]]):
        pulumi.set(self, "external_mappings", value)

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
    @pulumi.getter(name="internalMappings")
    def internal_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VpnNatRuleMappingArgs']]]]:
        """
        The private IP address internal mapping for NAT.
        """
        return pulumi.get(self, "internal_mappings")

    @internal_mappings.setter
    def internal_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VpnNatRuleMappingArgs']]]]):
        pulumi.set(self, "internal_mappings", value)

    @property
    @pulumi.getter(name="ipConfigurationId")
    def ip_configuration_id(self) -> Optional[pulumi.Input[str]]:
        """
        The IP Configuration ID this NAT rule applies to.
        """
        return pulumi.get(self, "ip_configuration_id")

    @ip_configuration_id.setter
    def ip_configuration_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_configuration_id", value)

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[Union[str, 'VpnNatRuleMode']]]:
        """
        The Source NAT direction of a VPN NAT.
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: Optional[pulumi.Input[Union[str, 'VpnNatRuleMode']]]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="natRuleName")
    def nat_rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the nat rule.
        """
        return pulumi.get(self, "nat_rule_name")

    @nat_rule_name.setter
    def nat_rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "nat_rule_name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[str, 'VpnNatRuleType']]]:
        """
        The type of NAT rule for VPN NAT.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[str, 'VpnNatRuleType']]]):
        pulumi.set(self, "type", value)


class NatRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 external_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnNatRuleMappingArgs']]]]] = None,
                 gateway_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 internal_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnNatRuleMappingArgs']]]]] = None,
                 ip_configuration_id: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input[Union[str, 'VpnNatRuleMode']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nat_rule_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[Union[str, 'VpnNatRuleType']]] = None,
                 __props__=None):
        """
        VpnGatewayNatRule Resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnNatRuleMappingArgs']]]] external_mappings: The private IP address external mapping for NAT.
        :param pulumi.Input[str] gateway_name: The name of the gateway.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnNatRuleMappingArgs']]]] internal_mappings: The private IP address internal mapping for NAT.
        :param pulumi.Input[str] ip_configuration_id: The IP Configuration ID this NAT rule applies to.
        :param pulumi.Input[Union[str, 'VpnNatRuleMode']] mode: The Source NAT direction of a VPN NAT.
        :param pulumi.Input[str] name: The name of the resource that is unique within a resource group. This name can be used to access the resource.
        :param pulumi.Input[str] nat_rule_name: The name of the nat rule.
        :param pulumi.Input[str] resource_group_name: The resource group name of the VpnGateway.
        :param pulumi.Input[Union[str, 'VpnNatRuleType']] type: The type of NAT rule for VPN NAT.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NatRuleInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        VpnGatewayNatRule Resource.

        :param str resource_name: The name of the resource.
        :param NatRuleInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NatRuleInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 external_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnNatRuleMappingArgs']]]]] = None,
                 gateway_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 internal_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnNatRuleMappingArgs']]]]] = None,
                 ip_configuration_id: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input[Union[str, 'VpnNatRuleMode']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nat_rule_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[Union[str, 'VpnNatRuleType']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NatRuleInitArgs.__new__(NatRuleInitArgs)

            __props__.__dict__["external_mappings"] = external_mappings
            if gateway_name is None and not opts.urn:
                raise TypeError("Missing required property 'gateway_name'")
            __props__.__dict__["gateway_name"] = gateway_name
            __props__.__dict__["id"] = id
            __props__.__dict__["internal_mappings"] = internal_mappings
            __props__.__dict__["ip_configuration_id"] = ip_configuration_id
            __props__.__dict__["mode"] = mode
            __props__.__dict__["name"] = name
            __props__.__dict__["nat_rule_name"] = nat_rule_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["type"] = type
            __props__.__dict__["egress_vpn_site_link_connections"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["ingress_vpn_site_link_connections"] = None
            __props__.__dict__["provisioning_state"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:NatRule"), pulumi.Alias(type_="azure-native:network/v20200801:NatRule"), pulumi.Alias(type_="azure-native:network/v20201101:NatRule"), pulumi.Alias(type_="azure-native:network/v20210201:NatRule"), pulumi.Alias(type_="azure-native:network/v20210301:NatRule"), pulumi.Alias(type_="azure-native:network/v20210501:NatRule"), pulumi.Alias(type_="azure-native:network/v20210801:NatRule"), pulumi.Alias(type_="azure-native:network/v20220101:NatRule"), pulumi.Alias(type_="azure-native:network/v20220501:NatRule"), pulumi.Alias(type_="azure-native:network/v20220701:NatRule"), pulumi.Alias(type_="azure-native:network/v20220901:NatRule"), pulumi.Alias(type_="azure-native:network/v20221101:NatRule"), pulumi.Alias(type_="azure-native:network/v20230201:NatRule"), pulumi.Alias(type_="azure-native:network/v20230401:NatRule"), pulumi.Alias(type_="azure-native:network/v20230501:NatRule"), pulumi.Alias(type_="azure-native:network/v20230901:NatRule"), pulumi.Alias(type_="azure-native:network/v20231101:NatRule"), pulumi.Alias(type_="azure-native:network/v20240101:NatRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NatRule, __self__).__init__(
            'azure-native:network/v20230601:NatRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NatRule':
        """
        Get an existing NatRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NatRuleInitArgs.__new__(NatRuleInitArgs)

        __props__.__dict__["egress_vpn_site_link_connections"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["external_mappings"] = None
        __props__.__dict__["ingress_vpn_site_link_connections"] = None
        __props__.__dict__["internal_mappings"] = None
        __props__.__dict__["ip_configuration_id"] = None
        __props__.__dict__["mode"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["type"] = None
        return NatRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="egressVpnSiteLinkConnections")
    def egress_vpn_site_link_connections(self) -> pulumi.Output[Sequence['outputs.SubResourceResponse']]:
        """
        List of egress VpnSiteLinkConnections.
        """
        return pulumi.get(self, "egress_vpn_site_link_connections")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="externalMappings")
    def external_mappings(self) -> pulumi.Output[Optional[Sequence['outputs.VpnNatRuleMappingResponse']]]:
        """
        The private IP address external mapping for NAT.
        """
        return pulumi.get(self, "external_mappings")

    @property
    @pulumi.getter(name="ingressVpnSiteLinkConnections")
    def ingress_vpn_site_link_connections(self) -> pulumi.Output[Sequence['outputs.SubResourceResponse']]:
        """
        List of ingress VpnSiteLinkConnections.
        """
        return pulumi.get(self, "ingress_vpn_site_link_connections")

    @property
    @pulumi.getter(name="internalMappings")
    def internal_mappings(self) -> pulumi.Output[Optional[Sequence['outputs.VpnNatRuleMappingResponse']]]:
        """
        The private IP address internal mapping for NAT.
        """
        return pulumi.get(self, "internal_mappings")

    @property
    @pulumi.getter(name="ipConfigurationId")
    def ip_configuration_id(self) -> pulumi.Output[Optional[str]]:
        """
        The IP Configuration ID this NAT rule applies to.
        """
        return pulumi.get(self, "ip_configuration_id")

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Output[Optional[str]]:
        """
        The Source NAT direction of a VPN NAT.
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the NAT Rule resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

