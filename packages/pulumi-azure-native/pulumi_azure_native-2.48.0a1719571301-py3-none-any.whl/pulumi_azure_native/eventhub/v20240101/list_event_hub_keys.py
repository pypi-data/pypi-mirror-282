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
    'ListEventHubKeysResult',
    'AwaitableListEventHubKeysResult',
    'list_event_hub_keys',
    'list_event_hub_keys_output',
]

@pulumi.output_type
class ListEventHubKeysResult:
    """
    Namespace/EventHub Connection String
    """
    def __init__(__self__, alias_primary_connection_string=None, alias_secondary_connection_string=None, key_name=None, primary_connection_string=None, primary_key=None, secondary_connection_string=None, secondary_key=None):
        if alias_primary_connection_string and not isinstance(alias_primary_connection_string, str):
            raise TypeError("Expected argument 'alias_primary_connection_string' to be a str")
        pulumi.set(__self__, "alias_primary_connection_string", alias_primary_connection_string)
        if alias_secondary_connection_string and not isinstance(alias_secondary_connection_string, str):
            raise TypeError("Expected argument 'alias_secondary_connection_string' to be a str")
        pulumi.set(__self__, "alias_secondary_connection_string", alias_secondary_connection_string)
        if key_name and not isinstance(key_name, str):
            raise TypeError("Expected argument 'key_name' to be a str")
        pulumi.set(__self__, "key_name", key_name)
        if primary_connection_string and not isinstance(primary_connection_string, str):
            raise TypeError("Expected argument 'primary_connection_string' to be a str")
        pulumi.set(__self__, "primary_connection_string", primary_connection_string)
        if primary_key and not isinstance(primary_key, str):
            raise TypeError("Expected argument 'primary_key' to be a str")
        pulumi.set(__self__, "primary_key", primary_key)
        if secondary_connection_string and not isinstance(secondary_connection_string, str):
            raise TypeError("Expected argument 'secondary_connection_string' to be a str")
        pulumi.set(__self__, "secondary_connection_string", secondary_connection_string)
        if secondary_key and not isinstance(secondary_key, str):
            raise TypeError("Expected argument 'secondary_key' to be a str")
        pulumi.set(__self__, "secondary_key", secondary_key)

    @property
    @pulumi.getter(name="aliasPrimaryConnectionString")
    def alias_primary_connection_string(self) -> str:
        """
        Primary connection string of the alias if GEO DR is enabled
        """
        return pulumi.get(self, "alias_primary_connection_string")

    @property
    @pulumi.getter(name="aliasSecondaryConnectionString")
    def alias_secondary_connection_string(self) -> str:
        """
        Secondary  connection string of the alias if GEO DR is enabled
        """
        return pulumi.get(self, "alias_secondary_connection_string")

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> str:
        """
        A string that describes the AuthorizationRule.
        """
        return pulumi.get(self, "key_name")

    @property
    @pulumi.getter(name="primaryConnectionString")
    def primary_connection_string(self) -> str:
        """
        Primary connection string of the created namespace AuthorizationRule.
        """
        return pulumi.get(self, "primary_connection_string")

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> str:
        """
        A base64-encoded 256-bit primary key for signing and validating the SAS token.
        """
        return pulumi.get(self, "primary_key")

    @property
    @pulumi.getter(name="secondaryConnectionString")
    def secondary_connection_string(self) -> str:
        """
        Secondary connection string of the created namespace AuthorizationRule.
        """
        return pulumi.get(self, "secondary_connection_string")

    @property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> str:
        """
        A base64-encoded 256-bit primary key for signing and validating the SAS token.
        """
        return pulumi.get(self, "secondary_key")


class AwaitableListEventHubKeysResult(ListEventHubKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListEventHubKeysResult(
            alias_primary_connection_string=self.alias_primary_connection_string,
            alias_secondary_connection_string=self.alias_secondary_connection_string,
            key_name=self.key_name,
            primary_connection_string=self.primary_connection_string,
            primary_key=self.primary_key,
            secondary_connection_string=self.secondary_connection_string,
            secondary_key=self.secondary_key)


def list_event_hub_keys(authorization_rule_name: Optional[str] = None,
                        event_hub_name: Optional[str] = None,
                        namespace_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListEventHubKeysResult:
    """
    Gets the ACS and SAS connection strings for the Event Hub.


    :param str authorization_rule_name: The authorization rule name.
    :param str event_hub_name: The Event Hub name
    :param str namespace_name: The Namespace name
    :param str resource_group_name: Name of the resource group within the azure subscription.
    """
    __args__ = dict()
    __args__['authorizationRuleName'] = authorization_rule_name
    __args__['eventHubName'] = event_hub_name
    __args__['namespaceName'] = namespace_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:eventhub/v20240101:listEventHubKeys', __args__, opts=opts, typ=ListEventHubKeysResult).value

    return AwaitableListEventHubKeysResult(
        alias_primary_connection_string=pulumi.get(__ret__, 'alias_primary_connection_string'),
        alias_secondary_connection_string=pulumi.get(__ret__, 'alias_secondary_connection_string'),
        key_name=pulumi.get(__ret__, 'key_name'),
        primary_connection_string=pulumi.get(__ret__, 'primary_connection_string'),
        primary_key=pulumi.get(__ret__, 'primary_key'),
        secondary_connection_string=pulumi.get(__ret__, 'secondary_connection_string'),
        secondary_key=pulumi.get(__ret__, 'secondary_key'))


@_utilities.lift_output_func(list_event_hub_keys)
def list_event_hub_keys_output(authorization_rule_name: Optional[pulumi.Input[str]] = None,
                               event_hub_name: Optional[pulumi.Input[str]] = None,
                               namespace_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListEventHubKeysResult]:
    """
    Gets the ACS and SAS connection strings for the Event Hub.


    :param str authorization_rule_name: The authorization rule name.
    :param str event_hub_name: The Event Hub name
    :param str namespace_name: The Namespace name
    :param str resource_group_name: Name of the resource group within the azure subscription.
    """
    ...
