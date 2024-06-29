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
    'GetAuthorizationProviderResult',
    'AwaitableGetAuthorizationProviderResult',
    'get_authorization_provider',
    'get_authorization_provider_output',
]

@pulumi.output_type
class GetAuthorizationProviderResult:
    """
    Authorization Provider contract.
    """
    def __init__(__self__, display_name=None, id=None, identity_provider=None, name=None, oauth2=None, type=None):
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity_provider and not isinstance(identity_provider, str):
            raise TypeError("Expected argument 'identity_provider' to be a str")
        pulumi.set(__self__, "identity_provider", identity_provider)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if oauth2 and not isinstance(oauth2, dict):
            raise TypeError("Expected argument 'oauth2' to be a dict")
        pulumi.set(__self__, "oauth2", oauth2)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        Authorization Provider name. Must be 1 to 300 characters long.
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
    @pulumi.getter(name="identityProvider")
    def identity_provider(self) -> Optional[str]:
        """
        Identity provider name. Must be 1 to 300 characters long.
        """
        return pulumi.get(self, "identity_provider")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def oauth2(self) -> Optional['outputs.AuthorizationProviderOAuth2SettingsResponse']:
        """
        OAuth2 settings
        """
        return pulumi.get(self, "oauth2")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetAuthorizationProviderResult(GetAuthorizationProviderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAuthorizationProviderResult(
            display_name=self.display_name,
            id=self.id,
            identity_provider=self.identity_provider,
            name=self.name,
            oauth2=self.oauth2,
            type=self.type)


def get_authorization_provider(authorization_provider_id: Optional[str] = None,
                               resource_group_name: Optional[str] = None,
                               service_name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAuthorizationProviderResult:
    """
    Gets the details of the authorization provider specified by its identifier.


    :param str authorization_provider_id: Identifier of the authorization provider.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['authorizationProviderId'] = authorization_provider_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20230301preview:getAuthorizationProvider', __args__, opts=opts, typ=GetAuthorizationProviderResult).value

    return AwaitableGetAuthorizationProviderResult(
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        identity_provider=pulumi.get(__ret__, 'identity_provider'),
        name=pulumi.get(__ret__, 'name'),
        oauth2=pulumi.get(__ret__, 'oauth2'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_authorization_provider)
def get_authorization_provider_output(authorization_provider_id: Optional[pulumi.Input[str]] = None,
                                      resource_group_name: Optional[pulumi.Input[str]] = None,
                                      service_name: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAuthorizationProviderResult]:
    """
    Gets the details of the authorization provider specified by its identifier.


    :param str authorization_provider_id: Identifier of the authorization provider.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    ...
