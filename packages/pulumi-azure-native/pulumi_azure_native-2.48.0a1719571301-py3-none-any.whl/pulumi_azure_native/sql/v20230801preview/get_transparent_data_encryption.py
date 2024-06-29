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
    'GetTransparentDataEncryptionResult',
    'AwaitableGetTransparentDataEncryptionResult',
    'get_transparent_data_encryption',
    'get_transparent_data_encryption_output',
]

@pulumi.output_type
class GetTransparentDataEncryptionResult:
    """
    A logical database transparent data encryption state.
    """
    def __init__(__self__, id=None, name=None, state=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        Specifies the state of the transparent data encryption.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetTransparentDataEncryptionResult(GetTransparentDataEncryptionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTransparentDataEncryptionResult(
            id=self.id,
            name=self.name,
            state=self.state,
            type=self.type)


def get_transparent_data_encryption(database_name: Optional[str] = None,
                                    resource_group_name: Optional[str] = None,
                                    server_name: Optional[str] = None,
                                    tde_name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTransparentDataEncryptionResult:
    """
    Gets a logical database's transparent data encryption.


    :param str database_name: The name of the logical database for which the transparent data encryption is defined.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    :param str tde_name: The name of the transparent data encryption configuration.
    """
    __args__ = dict()
    __args__['databaseName'] = database_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    __args__['tdeName'] = tde_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20230801preview:getTransparentDataEncryption', __args__, opts=opts, typ=GetTransparentDataEncryptionResult).value

    return AwaitableGetTransparentDataEncryptionResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        state=pulumi.get(__ret__, 'state'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_transparent_data_encryption)
def get_transparent_data_encryption_output(database_name: Optional[pulumi.Input[str]] = None,
                                           resource_group_name: Optional[pulumi.Input[str]] = None,
                                           server_name: Optional[pulumi.Input[str]] = None,
                                           tde_name: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTransparentDataEncryptionResult]:
    """
    Gets a logical database's transparent data encryption.


    :param str database_name: The name of the logical database for which the transparent data encryption is defined.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    :param str tde_name: The name of the transparent data encryption configuration.
    """
    ...
