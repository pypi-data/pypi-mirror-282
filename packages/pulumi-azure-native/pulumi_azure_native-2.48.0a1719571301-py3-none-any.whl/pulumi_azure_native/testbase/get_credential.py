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
    'GetCredentialResult',
    'AwaitableGetCredentialResult',
    'get_credential',
    'get_credential_output',
]

@pulumi.output_type
class GetCredentialResult:
    """
    The test base credential resource.
    """
    def __init__(__self__, credential_type=None, display_name=None, id=None, name=None, system_data=None, type=None):
        if credential_type and not isinstance(credential_type, str):
            raise TypeError("Expected argument 'credential_type' to be a str")
        pulumi.set(__self__, "credential_type", credential_type)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="credentialType")
    def credential_type(self) -> str:
        """
        Credential type.
        """
        return pulumi.get(self, "credential_type")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Credential display name.
        """
        return pulumi.get(self, "display_name")

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


class AwaitableGetCredentialResult(GetCredentialResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCredentialResult(
            credential_type=self.credential_type,
            display_name=self.display_name,
            id=self.id,
            name=self.name,
            system_data=self.system_data,
            type=self.type)


def get_credential(credential_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   test_base_account_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCredentialResult:
    """
    Gets a test base credential Resource
    Azure REST API version: 2023-11-01-preview.


    :param str credential_name: The credential resource name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str test_base_account_name: The resource name of the Test Base Account.
    """
    __args__ = dict()
    __args__['credentialName'] = credential_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['testBaseAccountName'] = test_base_account_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:testbase:getCredential', __args__, opts=opts, typ=GetCredentialResult).value

    return AwaitableGetCredentialResult(
        credential_type=pulumi.get(__ret__, 'credential_type'),
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_credential)
def get_credential_output(credential_name: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          test_base_account_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCredentialResult]:
    """
    Gets a test base credential Resource
    Azure REST API version: 2023-11-01-preview.


    :param str credential_name: The credential resource name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str test_base_account_name: The resource name of the Test Base Account.
    """
    ...
