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
    'ListIdentityProviderSecretsResult',
    'AwaitableListIdentityProviderSecretsResult',
    'list_identity_provider_secrets',
    'list_identity_provider_secrets_output',
]

@pulumi.output_type
class ListIdentityProviderSecretsResult:
    """
    Client or app secret used in IdentityProviders, Aad, OpenID or OAuth.
    """
    def __init__(__self__, client_secret=None):
        if client_secret and not isinstance(client_secret, str):
            raise TypeError("Expected argument 'client_secret' to be a str")
        pulumi.set(__self__, "client_secret", client_secret)

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[str]:
        """
        Client or app secret used in IdentityProviders, Aad, OpenID or OAuth.
        """
        return pulumi.get(self, "client_secret")


class AwaitableListIdentityProviderSecretsResult(ListIdentityProviderSecretsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListIdentityProviderSecretsResult(
            client_secret=self.client_secret)


def list_identity_provider_secrets(identity_provider_name: Optional[str] = None,
                                   resource_group_name: Optional[str] = None,
                                   service_name: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListIdentityProviderSecretsResult:
    """
    Gets the client secret details of the Identity Provider.


    :param str identity_provider_name: Identity Provider Type identifier.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['identityProviderName'] = identity_provider_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20230501preview:listIdentityProviderSecrets', __args__, opts=opts, typ=ListIdentityProviderSecretsResult).value

    return AwaitableListIdentityProviderSecretsResult(
        client_secret=pulumi.get(__ret__, 'client_secret'))


@_utilities.lift_output_func(list_identity_provider_secrets)
def list_identity_provider_secrets_output(identity_provider_name: Optional[pulumi.Input[str]] = None,
                                          resource_group_name: Optional[pulumi.Input[str]] = None,
                                          service_name: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListIdentityProviderSecretsResult]:
    """
    Gets the client secret details of the Identity Provider.


    :param str identity_provider_name: Identity Provider Type identifier.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    ...
