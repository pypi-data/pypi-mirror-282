# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetIPv6FirewallRuleResult',
    'AwaitableGetIPv6FirewallRuleResult',
    'get_i_pv6_firewall_rule',
    'get_i_pv6_firewall_rule_output',
]

@pulumi.output_type
class GetIPv6FirewallRuleResult:
    """
    An IPv6 server firewall rule.
    """
    def __init__(__self__, end_i_pv6_address=None, id=None, name=None, start_i_pv6_address=None, type=None):
        if end_i_pv6_address and not isinstance(end_i_pv6_address, str):
            raise TypeError("Expected argument 'end_i_pv6_address' to be a str")
        pulumi.set(__self__, "end_i_pv6_address", end_i_pv6_address)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if start_i_pv6_address and not isinstance(start_i_pv6_address, str):
            raise TypeError("Expected argument 'start_i_pv6_address' to be a str")
        pulumi.set(__self__, "start_i_pv6_address", start_i_pv6_address)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="endIPv6Address")
    def end_i_pv6_address(self) -> Optional[str]:
        """
        The end IP address of the firewall rule. Must be IPv6 format. Must be greater than or equal to startIpAddress.
        """
        return pulumi.get(self, "end_i_pv6_address")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="startIPv6Address")
    def start_i_pv6_address(self) -> Optional[str]:
        """
        The start IP address of the firewall rule. Must be IPv6 format.
        """
        return pulumi.get(self, "start_i_pv6_address")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetIPv6FirewallRuleResult(GetIPv6FirewallRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIPv6FirewallRuleResult(
            end_i_pv6_address=self.end_i_pv6_address,
            id=self.id,
            name=self.name,
            start_i_pv6_address=self.start_i_pv6_address,
            type=self.type)


def get_i_pv6_firewall_rule(firewall_rule_name: Optional[str] = None,
                            resource_group_name: Optional[str] = None,
                            server_name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIPv6FirewallRuleResult:
    """
    Gets an IPv6 firewall rule.


    :param str firewall_rule_name: The name of the firewall rule.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    __args__ = dict()
    __args__['firewallRuleName'] = firewall_rule_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20230201preview:getIPv6FirewallRule', __args__, opts=opts, typ=GetIPv6FirewallRuleResult).value

    return AwaitableGetIPv6FirewallRuleResult(
        end_i_pv6_address=pulumi.get(__ret__, 'end_i_pv6_address'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        start_i_pv6_address=pulumi.get(__ret__, 'start_i_pv6_address'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_i_pv6_firewall_rule)
def get_i_pv6_firewall_rule_output(firewall_rule_name: Optional[pulumi.Input[str]] = None,
                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                   server_name: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIPv6FirewallRuleResult]:
    """
    Gets an IPv6 firewall rule.


    :param str firewall_rule_name: The name of the firewall rule.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    ...
