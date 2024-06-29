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
    'GetWorkspaceNamedValueResult',
    'AwaitableGetWorkspaceNamedValueResult',
    'get_workspace_named_value',
    'get_workspace_named_value_output',
]

@pulumi.output_type
class GetWorkspaceNamedValueResult:
    """
    NamedValue details.
    """
    def __init__(__self__, display_name=None, id=None, key_vault=None, name=None, secret=None, tags=None, type=None, value=None):
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key_vault and not isinstance(key_vault, dict):
            raise TypeError("Expected argument 'key_vault' to be a dict")
        pulumi.set(__self__, "key_vault", key_vault)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if secret and not isinstance(secret, bool):
            raise TypeError("Expected argument 'secret' to be a bool")
        pulumi.set(__self__, "secret", secret)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Unique name of NamedValue. It may contain only letters, digits, period, dash, and underscore characters.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="keyVault")
    def key_vault(self) -> Optional['outputs.KeyVaultContractPropertiesResponse']:
        """
        KeyVault location details of the namedValue.
        """
        return pulumi.get(self, "key_vault")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def secret(self) -> Optional[bool]:
        """
        Determines whether the value is a secret and should be encrypted or not. Default value is false.
        """
        return pulumi.get(self, "secret")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[str]]:
        """
        Optional tags that when provided can be used to filter the NamedValue list.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        Value of the NamedValue. Can contain policy expressions. It may not be empty or consist only of whitespace. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value.
        """
        return pulumi.get(self, "value")


class AwaitableGetWorkspaceNamedValueResult(GetWorkspaceNamedValueResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkspaceNamedValueResult(
            display_name=self.display_name,
            id=self.id,
            key_vault=self.key_vault,
            name=self.name,
            secret=self.secret,
            tags=self.tags,
            type=self.type,
            value=self.value)


def get_workspace_named_value(named_value_id: Optional[str] = None,
                              resource_group_name: Optional[str] = None,
                              service_name: Optional[str] = None,
                              workspace_id: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkspaceNamedValueResult:
    """
    Gets the details of the named value specified by its identifier.


    :param str named_value_id: Identifier of the NamedValue.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    :param str workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
    """
    __args__ = dict()
    __args__['namedValueId'] = named_value_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    __args__['workspaceId'] = workspace_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20230301preview:getWorkspaceNamedValue', __args__, opts=opts, typ=GetWorkspaceNamedValueResult).value

    return AwaitableGetWorkspaceNamedValueResult(
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        key_vault=pulumi.get(__ret__, 'key_vault'),
        name=pulumi.get(__ret__, 'name'),
        secret=pulumi.get(__ret__, 'secret'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(get_workspace_named_value)
def get_workspace_named_value_output(named_value_id: Optional[pulumi.Input[str]] = None,
                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                     service_name: Optional[pulumi.Input[str]] = None,
                                     workspace_id: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkspaceNamedValueResult]:
    """
    Gets the details of the named value specified by its identifier.


    :param str named_value_id: Identifier of the NamedValue.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    :param str workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
    """
    ...
