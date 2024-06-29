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
    'GetCredentialSetResult',
    'AwaitableGetCredentialSetResult',
    'get_credential_set',
    'get_credential_set_output',
]

@pulumi.output_type
class GetCredentialSetResult:
    """
    An object that represents a credential set resource for a container registry.
    """
    def __init__(__self__, auth_credentials=None, creation_date=None, id=None, identity=None, login_server=None, name=None, provisioning_state=None, system_data=None, type=None):
        if auth_credentials and not isinstance(auth_credentials, list):
            raise TypeError("Expected argument 'auth_credentials' to be a list")
        pulumi.set(__self__, "auth_credentials", auth_credentials)
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        pulumi.set(__self__, "creation_date", creation_date)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if login_server and not isinstance(login_server, str):
            raise TypeError("Expected argument 'login_server' to be a str")
        pulumi.set(__self__, "login_server", login_server)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="authCredentials")
    def auth_credentials(self) -> Optional[Sequence['outputs.AuthCredentialResponse']]:
        """
        List of authentication credentials stored for an upstream.
        Usually consists of a primary and an optional secondary credential.
        """
        return pulumi.get(self, "auth_credentials")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> str:
        """
        The creation date of credential store resource.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.IdentityPropertiesResponse']:
        """
        Identities associated with the resource. This is used to access the KeyVault secrets.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="loginServer")
    def login_server(self) -> Optional[str]:
        """
        The credentials are stored for this upstream or login server.
        """
        return pulumi.get(self, "login_server")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetCredentialSetResult(GetCredentialSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCredentialSetResult(
            auth_credentials=self.auth_credentials,
            creation_date=self.creation_date,
            id=self.id,
            identity=self.identity,
            login_server=self.login_server,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_credential_set(credential_set_name: Optional[str] = None,
                       registry_name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCredentialSetResult:
    """
    Gets the properties of the specified credential set resource.
    Azure REST API version: 2023-01-01-preview.

    Other available API versions: 2023-06-01-preview, 2023-07-01, 2023-08-01-preview, 2023-11-01-preview.


    :param str credential_set_name: The name of the credential set.
    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['credentialSetName'] = credential_set_name
    __args__['registryName'] = registry_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerregistry:getCredentialSet', __args__, opts=opts, typ=GetCredentialSetResult).value

    return AwaitableGetCredentialSetResult(
        auth_credentials=pulumi.get(__ret__, 'auth_credentials'),
        creation_date=pulumi.get(__ret__, 'creation_date'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        login_server=pulumi.get(__ret__, 'login_server'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_credential_set)
def get_credential_set_output(credential_set_name: Optional[pulumi.Input[str]] = None,
                              registry_name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCredentialSetResult]:
    """
    Gets the properties of the specified credential set resource.
    Azure REST API version: 2023-01-01-preview.

    Other available API versions: 2023-06-01-preview, 2023-07-01, 2023-08-01-preview, 2023-11-01-preview.


    :param str credential_set_name: The name of the credential set.
    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
