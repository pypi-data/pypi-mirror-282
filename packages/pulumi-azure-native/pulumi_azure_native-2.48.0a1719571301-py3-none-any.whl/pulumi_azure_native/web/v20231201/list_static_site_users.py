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
    'ListStaticSiteUsersResult',
    'AwaitableListStaticSiteUsersResult',
    'list_static_site_users',
    'list_static_site_users_output',
]

@pulumi.output_type
class ListStaticSiteUsersResult:
    """
    Collection of static site custom users.
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> str:
        """
        Link to next page of resources.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Sequence['outputs.StaticSiteUserARMResourceResponse']:
        """
        Collection of resources.
        """
        return pulumi.get(self, "value")


class AwaitableListStaticSiteUsersResult(ListStaticSiteUsersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListStaticSiteUsersResult(
            next_link=self.next_link,
            value=self.value)


def list_static_site_users(authprovider: Optional[str] = None,
                           name: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListStaticSiteUsersResult:
    """
    Description for Gets the list of users of a static site.


    :param str authprovider: The auth provider for the users.
    :param str name: Name of the static site.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    __args__ = dict()
    __args__['authprovider'] = authprovider
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20231201:listStaticSiteUsers', __args__, opts=opts, typ=ListStaticSiteUsersResult).value

    return AwaitableListStaticSiteUsersResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_static_site_users)
def list_static_site_users_output(authprovider: Optional[pulumi.Input[str]] = None,
                                  name: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListStaticSiteUsersResult]:
    """
    Description for Gets the list of users of a static site.


    :param str authprovider: The auth provider for the users.
    :param str name: Name of the static site.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    ...
