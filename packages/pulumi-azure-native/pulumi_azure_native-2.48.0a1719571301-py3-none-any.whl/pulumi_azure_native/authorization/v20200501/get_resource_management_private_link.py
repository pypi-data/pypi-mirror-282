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
    'GetResourceManagementPrivateLinkResult',
    'AwaitableGetResourceManagementPrivateLinkResult',
    'get_resource_management_private_link',
    'get_resource_management_private_link_output',
]

@pulumi.output_type
class GetResourceManagementPrivateLinkResult:
    def __init__(__self__, id=None, location=None, name=None, properties=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The rmplResourceID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        the region of the rmpl
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The rmpl Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.ResourceManagementPrivateLinkEndpointConnectionsResponse':
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The operation type.
        """
        return pulumi.get(self, "type")


class AwaitableGetResourceManagementPrivateLinkResult(GetResourceManagementPrivateLinkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResourceManagementPrivateLinkResult(
            id=self.id,
            location=self.location,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_resource_management_private_link(resource_group_name: Optional[str] = None,
                                         rmpl_name: Optional[str] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResourceManagementPrivateLinkResult:
    """
    Get a resource management private link(resource-level).


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str rmpl_name: The name of the resource management private link.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['rmplName'] = rmpl_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:authorization/v20200501:getResourceManagementPrivateLink', __args__, opts=opts, typ=GetResourceManagementPrivateLinkResult).value

    return AwaitableGetResourceManagementPrivateLinkResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_resource_management_private_link)
def get_resource_management_private_link_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                                rmpl_name: Optional[pulumi.Input[str]] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResourceManagementPrivateLinkResult]:
    """
    Get a resource management private link(resource-level).


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str rmpl_name: The name of the resource management private link.
    """
    ...
