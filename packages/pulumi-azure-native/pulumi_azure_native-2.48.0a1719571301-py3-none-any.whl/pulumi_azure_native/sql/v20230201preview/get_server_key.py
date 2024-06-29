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
    'GetServerKeyResult',
    'AwaitableGetServerKeyResult',
    'get_server_key',
    'get_server_key_output',
]

@pulumi.output_type
class GetServerKeyResult:
    """
    A server key.
    """
    def __init__(__self__, auto_rotation_enabled=None, creation_date=None, id=None, kind=None, location=None, name=None, subregion=None, thumbprint=None, type=None):
        if auto_rotation_enabled and not isinstance(auto_rotation_enabled, bool):
            raise TypeError("Expected argument 'auto_rotation_enabled' to be a bool")
        pulumi.set(__self__, "auto_rotation_enabled", auto_rotation_enabled)
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        pulumi.set(__self__, "creation_date", creation_date)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if subregion and not isinstance(subregion, str):
            raise TypeError("Expected argument 'subregion' to be a str")
        pulumi.set(__self__, "subregion", subregion)
        if thumbprint and not isinstance(thumbprint, str):
            raise TypeError("Expected argument 'thumbprint' to be a str")
        pulumi.set(__self__, "thumbprint", thumbprint)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="autoRotationEnabled")
    def auto_rotation_enabled(self) -> bool:
        """
        Key auto rotation opt-in flag. Either true or false.
        """
        return pulumi.get(self, "auto_rotation_enabled")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> str:
        """
        The server key creation date.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of encryption protector. This is metadata used for the Azure portal experience.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def subregion(self) -> str:
        """
        Subregion of the server key.
        """
        return pulumi.get(self, "subregion")

    @property
    @pulumi.getter
    def thumbprint(self) -> str:
        """
        Thumbprint of the server key.
        """
        return pulumi.get(self, "thumbprint")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetServerKeyResult(GetServerKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerKeyResult(
            auto_rotation_enabled=self.auto_rotation_enabled,
            creation_date=self.creation_date,
            id=self.id,
            kind=self.kind,
            location=self.location,
            name=self.name,
            subregion=self.subregion,
            thumbprint=self.thumbprint,
            type=self.type)


def get_server_key(key_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   server_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerKeyResult:
    """
    Gets a server key.


    :param str key_name: The name of the server key to be retrieved.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    __args__ = dict()
    __args__['keyName'] = key_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20230201preview:getServerKey', __args__, opts=opts, typ=GetServerKeyResult).value

    return AwaitableGetServerKeyResult(
        auto_rotation_enabled=pulumi.get(__ret__, 'auto_rotation_enabled'),
        creation_date=pulumi.get(__ret__, 'creation_date'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        subregion=pulumi.get(__ret__, 'subregion'),
        thumbprint=pulumi.get(__ret__, 'thumbprint'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_server_key)
def get_server_key_output(key_name: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          server_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServerKeyResult]:
    """
    Gets a server key.


    :param str key_name: The name of the server key to be retrieved.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    ...
