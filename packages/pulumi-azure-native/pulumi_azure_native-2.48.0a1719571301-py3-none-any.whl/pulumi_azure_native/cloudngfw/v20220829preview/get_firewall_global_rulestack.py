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
    'GetFirewallGlobalRulestackResult',
    'AwaitableGetFirewallGlobalRulestackResult',
    'get_firewall_global_rulestack',
    'get_firewall_global_rulestack_output',
]

@pulumi.output_type
class GetFirewallGlobalRulestackResult:
    """
    PAN Rulestack Describe Object
    """
    def __init__(__self__, azure_id=None):
        if azure_id and not isinstance(azure_id, str):
            raise TypeError("Expected argument 'azure_id' to be a str")
        pulumi.set(__self__, "azure_id", azure_id)

    @property
    @pulumi.getter(name="azureId")
    def azure_id(self) -> str:
        """
        rulestack description
        """
        return pulumi.get(self, "azure_id")


class AwaitableGetFirewallGlobalRulestackResult(GetFirewallGlobalRulestackResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFirewallGlobalRulestackResult(
            azure_id=self.azure_id)


def get_firewall_global_rulestack(firewall_name: Optional[str] = None,
                                  resource_group_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFirewallGlobalRulestackResult:
    """
    Get Global Rulestack associated with the Firewall


    :param str firewall_name: Firewall resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['firewallName'] = firewall_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cloudngfw/v20220829preview:getFirewallGlobalRulestack', __args__, opts=opts, typ=GetFirewallGlobalRulestackResult).value

    return AwaitableGetFirewallGlobalRulestackResult(
        azure_id=pulumi.get(__ret__, 'azure_id'))


@_utilities.lift_output_func(get_firewall_global_rulestack)
def get_firewall_global_rulestack_output(firewall_name: Optional[pulumi.Input[str]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFirewallGlobalRulestackResult]:
    """
    Get Global Rulestack associated with the Firewall


    :param str firewall_name: Firewall resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
