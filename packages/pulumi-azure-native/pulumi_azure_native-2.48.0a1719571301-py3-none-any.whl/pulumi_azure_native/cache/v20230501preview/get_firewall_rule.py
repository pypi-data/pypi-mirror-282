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
    A firewall rule on a redis cache has a name, and describes a contiguous range of IP addresses permitted to connect
    """
    def __init__(__self__, end_ip=None, id=None, name=None, start_ip=None, type=None):
        if end_ip and not isinstance(end_ip, str):
            raise TypeError("Expected argument 'end_ip' to be a str")
        pulumi.set(__self__, "end_ip", end_ip)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if start_ip and not isinstance(start_ip, str):
            raise TypeError("Expected argument 'start_ip' to be a str")
        pulumi.set(__self__, "start_ip", start_ip)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="endIP")
    def end_ip(self) -> str:
        """
        highest IP address included in the range
        """
        return pulumi.get(self, "end_ip")

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
    @pulumi.getter(name="startIP")
    def start_ip(self) -> str:
        """
        lowest IP address included in the range
        """
        return pulumi.get(self, "start_ip")

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
            end_ip=self.end_ip,
            id=self.id,
            name=self.name,
            start_ip=self.start_ip,
            type=self.type)


def get_firewall_rule(cache_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      rule_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFirewallRuleResult:
    """
    Gets a single firewall rule in a specified redis cache.


    :param str cache_name: The name of the Redis cache.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str rule_name: The name of the firewall rule.
    """
    __args__ = dict()
    __args__['cacheName'] = cache_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['ruleName'] = rule_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cache/v20230501preview:getFirewallRule', __args__, opts=opts, typ=GetFirewallRuleResult).value

    return AwaitableGetFirewallRuleResult(
        end_ip=pulumi.get(__ret__, 'end_ip'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        start_ip=pulumi.get(__ret__, 'start_ip'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_firewall_rule)
def get_firewall_rule_output(cache_name: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             rule_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFirewallRuleResult]:
    """
    Gets a single firewall rule in a specified redis cache.


    :param str cache_name: The name of the Redis cache.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str rule_name: The name of the firewall rule.
    """
    ...
