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

__all__ = [
    'GetMongoClusterFirewallRuleResult',
    'AwaitableGetMongoClusterFirewallRuleResult',
    'get_mongo_cluster_firewall_rule',
    'get_mongo_cluster_firewall_rule_output',
]

@pulumi.output_type
class GetMongoClusterFirewallRuleResult:
    """
    Represents a mongo cluster firewall rule.
    """
    def __init__(__self__, end_ip_address=None, id=None, name=None, provisioning_state=None, start_ip_address=None, system_data=None, type=None):
        if end_ip_address and not isinstance(end_ip_address, str):
            raise TypeError("Expected argument 'end_ip_address' to be a str")
        pulumi.set(__self__, "end_ip_address", end_ip_address)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if start_ip_address and not isinstance(start_ip_address, str):
            raise TypeError("Expected argument 'start_ip_address' to be a str")
        pulumi.set(__self__, "start_ip_address", start_ip_address)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> str:
        """
        The end IP address of the mongo cluster firewall rule. Must be IPv4 format.
        """
        return pulumi.get(self, "end_ip_address")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the firewall rule.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> str:
        """
        The start IP address of the mongo cluster firewall rule. Must be IPv4 format.
        """
        return pulumi.get(self, "start_ip_address")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetMongoClusterFirewallRuleResult(GetMongoClusterFirewallRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMongoClusterFirewallRuleResult(
            end_ip_address=self.end_ip_address,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            start_ip_address=self.start_ip_address,
            system_data=self.system_data,
            type=self.type)


def get_mongo_cluster_firewall_rule(firewall_rule_name: Optional[str] = None,
                                    mongo_cluster_name: Optional[str] = None,
                                    resource_group_name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMongoClusterFirewallRuleResult:
    """
    Gets information about a mongo cluster firewall rule.


    :param str firewall_rule_name: The name of the mongo cluster firewall rule.
    :param str mongo_cluster_name: The name of the mongo cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['firewallRuleName'] = firewall_rule_name
    __args__['mongoClusterName'] = mongo_cluster_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:documentdb/v20231115preview:getMongoClusterFirewallRule', __args__, opts=opts, typ=GetMongoClusterFirewallRuleResult).value

    return AwaitableGetMongoClusterFirewallRuleResult(
        end_ip_address=pulumi.get(__ret__, 'end_ip_address'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        start_ip_address=pulumi.get(__ret__, 'start_ip_address'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_mongo_cluster_firewall_rule)
def get_mongo_cluster_firewall_rule_output(firewall_rule_name: Optional[pulumi.Input[str]] = None,
                                           mongo_cluster_name: Optional[pulumi.Input[str]] = None,
                                           resource_group_name: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMongoClusterFirewallRuleResult]:
    """
    Gets information about a mongo cluster firewall rule.


    :param str firewall_rule_name: The name of the mongo cluster firewall rule.
    :param str mongo_cluster_name: The name of the mongo cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
