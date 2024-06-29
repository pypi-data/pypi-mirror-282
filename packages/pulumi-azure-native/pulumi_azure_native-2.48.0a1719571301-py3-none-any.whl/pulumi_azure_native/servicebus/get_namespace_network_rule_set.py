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

__all__ = [
    'GetNamespaceNetworkRuleSetResult',
    'AwaitableGetNamespaceNetworkRuleSetResult',
    'get_namespace_network_rule_set',
    'get_namespace_network_rule_set_output',
]

@pulumi.output_type
class GetNamespaceNetworkRuleSetResult:
    """
    Description of NetworkRuleSet resource.
    """
    def __init__(__self__, default_action=None, id=None, ip_rules=None, location=None, name=None, public_network_access=None, system_data=None, trusted_service_access_enabled=None, type=None, virtual_network_rules=None):
        if default_action and not isinstance(default_action, str):
            raise TypeError("Expected argument 'default_action' to be a str")
        pulumi.set(__self__, "default_action", default_action)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_rules and not isinstance(ip_rules, list):
            raise TypeError("Expected argument 'ip_rules' to be a list")
        pulumi.set(__self__, "ip_rules", ip_rules)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if public_network_access and not isinstance(public_network_access, str):
            raise TypeError("Expected argument 'public_network_access' to be a str")
        pulumi.set(__self__, "public_network_access", public_network_access)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if trusted_service_access_enabled and not isinstance(trusted_service_access_enabled, bool):
            raise TypeError("Expected argument 'trusted_service_access_enabled' to be a bool")
        pulumi.set(__self__, "trusted_service_access_enabled", trusted_service_access_enabled)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_network_rules and not isinstance(virtual_network_rules, list):
            raise TypeError("Expected argument 'virtual_network_rules' to be a list")
        pulumi.set(__self__, "virtual_network_rules", virtual_network_rules)

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[str]:
        """
        Default Action for Network Rule Set
        """
        return pulumi.get(self, "default_action")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> Optional[Sequence['outputs.NWRuleSetIpRulesResponse']]:
        """
        List of IpRules
        """
        return pulumi.get(self, "ip_rules")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[str]:
        """
        This determines if traffic is allowed over public network. By default it is enabled.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system meta data relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="trustedServiceAccessEnabled")
    def trusted_service_access_enabled(self) -> Optional[bool]:
        """
        Value that indicates whether Trusted Service Access is Enabled or not.
        """
        return pulumi.get(self, "trusted_service_access_enabled")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualNetworkRules")
    def virtual_network_rules(self) -> Optional[Sequence['outputs.NWRuleSetVirtualNetworkRulesResponse']]:
        """
        List VirtualNetwork Rules
        """
        return pulumi.get(self, "virtual_network_rules")


class AwaitableGetNamespaceNetworkRuleSetResult(GetNamespaceNetworkRuleSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNamespaceNetworkRuleSetResult(
            default_action=self.default_action,
            id=self.id,
            ip_rules=self.ip_rules,
            location=self.location,
            name=self.name,
            public_network_access=self.public_network_access,
            system_data=self.system_data,
            trusted_service_access_enabled=self.trusted_service_access_enabled,
            type=self.type,
            virtual_network_rules=self.virtual_network_rules)


def get_namespace_network_rule_set(namespace_name: Optional[str] = None,
                                   resource_group_name: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNamespaceNetworkRuleSetResult:
    """
    Gets NetworkRuleSet for a Namespace.
    Azure REST API version: 2022-01-01-preview.

    Other available API versions: 2022-10-01-preview.


    :param str namespace_name: The namespace name
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['namespaceName'] = namespace_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:servicebus:getNamespaceNetworkRuleSet', __args__, opts=opts, typ=GetNamespaceNetworkRuleSetResult).value

    return AwaitableGetNamespaceNetworkRuleSetResult(
        default_action=pulumi.get(__ret__, 'default_action'),
        id=pulumi.get(__ret__, 'id'),
        ip_rules=pulumi.get(__ret__, 'ip_rules'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        public_network_access=pulumi.get(__ret__, 'public_network_access'),
        system_data=pulumi.get(__ret__, 'system_data'),
        trusted_service_access_enabled=pulumi.get(__ret__, 'trusted_service_access_enabled'),
        type=pulumi.get(__ret__, 'type'),
        virtual_network_rules=pulumi.get(__ret__, 'virtual_network_rules'))


@_utilities.lift_output_func(get_namespace_network_rule_set)
def get_namespace_network_rule_set_output(namespace_name: Optional[pulumi.Input[str]] = None,
                                          resource_group_name: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNamespaceNetworkRuleSetResult]:
    """
    Gets NetworkRuleSet for a Namespace.
    Azure REST API version: 2022-01-01-preview.

    Other available API versions: 2022-10-01-preview.


    :param str namespace_name: The namespace name
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    ...
