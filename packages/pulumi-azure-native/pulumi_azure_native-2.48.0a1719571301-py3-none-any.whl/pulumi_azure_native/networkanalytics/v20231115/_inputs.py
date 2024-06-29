# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'DataProductNetworkAclsArgs',
    'EncryptionKeyDetailsArgs',
    'IPRulesArgs',
    'ManagedResourceGroupConfigurationArgs',
    'ManagedServiceIdentityArgs',
    'VirtualNetworkRuleArgs',
]

@pulumi.input_type
class DataProductNetworkAclsArgs:
    def __init__(__self__, *,
                 allowed_query_ip_range_list: pulumi.Input[Sequence[pulumi.Input[str]]],
                 default_action: pulumi.Input[Union[str, 'DefaultAction']],
                 ip_rules: pulumi.Input[Sequence[pulumi.Input['IPRulesArgs']]],
                 virtual_network_rule: pulumi.Input[Sequence[pulumi.Input['VirtualNetworkRuleArgs']]]):
        """
        Data Product Network rule set
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_query_ip_range_list: The list of query ips in the format of CIDR allowed to connect to query/visualization endpoint.
        :param pulumi.Input[Union[str, 'DefaultAction']] default_action: Default Action
        :param pulumi.Input[Sequence[pulumi.Input['IPRulesArgs']]] ip_rules: IP rule with specific IP or IP range in CIDR format.
        :param pulumi.Input[Sequence[pulumi.Input['VirtualNetworkRuleArgs']]] virtual_network_rule: Virtual Network Rule
        """
        pulumi.set(__self__, "allowed_query_ip_range_list", allowed_query_ip_range_list)
        pulumi.set(__self__, "default_action", default_action)
        pulumi.set(__self__, "ip_rules", ip_rules)
        pulumi.set(__self__, "virtual_network_rule", virtual_network_rule)

    @property
    @pulumi.getter(name="allowedQueryIpRangeList")
    def allowed_query_ip_range_list(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The list of query ips in the format of CIDR allowed to connect to query/visualization endpoint.
        """
        return pulumi.get(self, "allowed_query_ip_range_list")

    @allowed_query_ip_range_list.setter
    def allowed_query_ip_range_list(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "allowed_query_ip_range_list", value)

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> pulumi.Input[Union[str, 'DefaultAction']]:
        """
        Default Action
        """
        return pulumi.get(self, "default_action")

    @default_action.setter
    def default_action(self, value: pulumi.Input[Union[str, 'DefaultAction']]):
        pulumi.set(self, "default_action", value)

    @property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> pulumi.Input[Sequence[pulumi.Input['IPRulesArgs']]]:
        """
        IP rule with specific IP or IP range in CIDR format.
        """
        return pulumi.get(self, "ip_rules")

    @ip_rules.setter
    def ip_rules(self, value: pulumi.Input[Sequence[pulumi.Input['IPRulesArgs']]]):
        pulumi.set(self, "ip_rules", value)

    @property
    @pulumi.getter(name="virtualNetworkRule")
    def virtual_network_rule(self) -> pulumi.Input[Sequence[pulumi.Input['VirtualNetworkRuleArgs']]]:
        """
        Virtual Network Rule
        """
        return pulumi.get(self, "virtual_network_rule")

    @virtual_network_rule.setter
    def virtual_network_rule(self, value: pulumi.Input[Sequence[pulumi.Input['VirtualNetworkRuleArgs']]]):
        pulumi.set(self, "virtual_network_rule", value)


@pulumi.input_type
class EncryptionKeyDetailsArgs:
    def __init__(__self__, *,
                 key_name: pulumi.Input[str],
                 key_vault_uri: pulumi.Input[str],
                 key_version: pulumi.Input[str]):
        """
        Encryption key details.
        :param pulumi.Input[str] key_name: The name of the key vault key.
        :param pulumi.Input[str] key_vault_uri: The Uri of the key vault.
        :param pulumi.Input[str] key_version: The version of the key vault key.
        """
        pulumi.set(__self__, "key_name", key_name)
        pulumi.set(__self__, "key_vault_uri", key_vault_uri)
        pulumi.set(__self__, "key_version", key_version)

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Input[str]:
        """
        The name of the key vault key.
        """
        return pulumi.get(self, "key_name")

    @key_name.setter
    def key_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_name", value)

    @property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> pulumi.Input[str]:
        """
        The Uri of the key vault.
        """
        return pulumi.get(self, "key_vault_uri")

    @key_vault_uri.setter
    def key_vault_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_vault_uri", value)

    @property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> pulumi.Input[str]:
        """
        The version of the key vault key.
        """
        return pulumi.get(self, "key_version")

    @key_version.setter
    def key_version(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_version", value)


@pulumi.input_type
class IPRulesArgs:
    def __init__(__self__, *,
                 action: pulumi.Input[str],
                 value: Optional[pulumi.Input[str]] = None):
        """
        IP rule with specific IP or IP range in CIDR format.
        :param pulumi.Input[str] action: The action of virtual network rule.
        :param pulumi.Input[str] value: IP Rules Value
        """
        pulumi.set(__self__, "action", action)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input[str]:
        """
        The action of virtual network rule.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input[str]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        IP Rules Value
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ManagedResourceGroupConfigurationArgs:
    def __init__(__self__, *,
                 location: pulumi.Input[str],
                 name: pulumi.Input[str]):
        """
        ManagedResourceGroup related properties
        :param pulumi.Input[str] location: Managed Resource Group location
        :param pulumi.Input[str] name: Name of managed resource group
        """
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        Managed Resource Group location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of managed resource group
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[Union[str, 'ManagedServiceIdentityType']],
                 user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Managed service identity (system assigned and/or user assigned identities)
        :param pulumi.Input[Union[str, 'ManagedServiceIdentityType']] type: Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_assigned_identities: The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.
        """
        pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[str, 'ManagedServiceIdentityType']]:
        """
        Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[Union[str, 'ManagedServiceIdentityType']]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.
        """
        return pulumi.get(self, "user_assigned_identities")

    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "user_assigned_identities", value)


@pulumi.input_type
class VirtualNetworkRuleArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 action: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None):
        """
        Virtual Network Rule
        :param pulumi.Input[str] id: Resource ID of a subnet
        :param pulumi.Input[str] action: The action of virtual network rule.
        :param pulumi.Input[str] state: Gets the state of virtual network rule.
        """
        pulumi.set(__self__, "id", id)
        if action is not None:
            pulumi.set(__self__, "action", action)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        Resource ID of a subnet
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[str]]:
        """
        The action of virtual network rule.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        Gets the state of virtual network rule.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)


