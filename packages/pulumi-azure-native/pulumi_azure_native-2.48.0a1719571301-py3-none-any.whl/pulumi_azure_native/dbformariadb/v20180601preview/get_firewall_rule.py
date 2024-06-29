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
    'GetFirewallRuleResult',
    'AwaitableGetFirewallRuleResult',
    'get_firewall_rule',
    'get_firewall_rule_output',
]

@pulumi.output_type
class GetFirewallRuleResult:
    """
    Represents a server firewall rule.
    """
    def __init__(__self__, end_ip_address=None, id=None, name=None, start_ip_address=None, type=None):
        if end_ip_address and not isinstance(end_ip_address, str):
            raise TypeError("Expected argument 'end_ip_address' to be a str")
        pulumi.set(__self__, "end_ip_address", end_ip_address)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if start_ip_address and not isinstance(start_ip_address, str):
            raise TypeError("Expected argument 'start_ip_address' to be a str")
        pulumi.set(__self__, "start_ip_address", start_ip_address)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> str:
        """
        The end IP address of the server firewall rule. Must be IPv4 format.
        """
        return pulumi.get(self, "end_ip_address")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> str:
        """
        The start IP address of the server firewall rule. Must be IPv4 format.
        """
        return pulumi.get(self, "start_ip_address")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetFirewallRuleResult(GetFirewallRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFirewallRuleResult(
            end_ip_address=self.end_ip_address,
            id=self.id,
            name=self.name,
            start_ip_address=self.start_ip_address,
            type=self.type)


def get_firewall_rule(firewall_rule_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      server_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFirewallRuleResult:
    """
    Gets information about a server firewall rule.


    :param str firewall_rule_name: The name of the server firewall rule.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    __args__ = dict()
    __args__['firewallRuleName'] = firewall_rule_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:dbformariadb/v20180601preview:getFirewallRule', __args__, opts=opts, typ=GetFirewallRuleResult).value

    return AwaitableGetFirewallRuleResult(
        end_ip_address=pulumi.get(__ret__, 'end_ip_address'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        start_ip_address=pulumi.get(__ret__, 'start_ip_address'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_firewall_rule)
def get_firewall_rule_output(firewall_rule_name: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             server_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFirewallRuleResult]:
    """
    Gets information about a server firewall rule.


    :param str firewall_rule_name: The name of the server firewall rule.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    ...
