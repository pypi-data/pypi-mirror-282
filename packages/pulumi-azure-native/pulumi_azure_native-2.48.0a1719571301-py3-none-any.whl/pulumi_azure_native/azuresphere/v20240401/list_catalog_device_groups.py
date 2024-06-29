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
    'ListCatalogDeviceGroupsResult',
    'AwaitableListCatalogDeviceGroupsResult',
    'list_catalog_device_groups',
    'list_catalog_device_groups_output',
]

@pulumi.output_type
class ListCatalogDeviceGroupsResult:
    """
    The response of a DeviceGroup list operation.
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
    def next_link(self) -> Optional[str]:
        """
        The link to the next page of items
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Sequence['outputs.DeviceGroupResponse']:
        """
        The DeviceGroup items on this page
        """
        return pulumi.get(self, "value")


class AwaitableListCatalogDeviceGroupsResult(ListCatalogDeviceGroupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListCatalogDeviceGroupsResult(
            next_link=self.next_link,
            value=self.value)


def list_catalog_device_groups(catalog_name: Optional[str] = None,
                               device_group_name: Optional[str] = None,
                               filter: Optional[str] = None,
                               maxpagesize: Optional[int] = None,
                               resource_group_name: Optional[str] = None,
                               skip: Optional[int] = None,
                               top: Optional[int] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListCatalogDeviceGroupsResult:
    """
    List the device groups for the catalog.


    :param str catalog_name: Name of catalog
    :param str device_group_name: Device Group name.
    :param str filter: Filter the result list using the given expression
    :param int maxpagesize: The maximum number of result items per page.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param int skip: The number of result items to skip.
    :param int top: The number of result items to return.
    """
    __args__ = dict()
    __args__['catalogName'] = catalog_name
    __args__['deviceGroupName'] = device_group_name
    __args__['filter'] = filter
    __args__['maxpagesize'] = maxpagesize
    __args__['resourceGroupName'] = resource_group_name
    __args__['skip'] = skip
    __args__['top'] = top
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azuresphere/v20240401:listCatalogDeviceGroups', __args__, opts=opts, typ=ListCatalogDeviceGroupsResult).value

    return AwaitableListCatalogDeviceGroupsResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_catalog_device_groups)
def list_catalog_device_groups_output(catalog_name: Optional[pulumi.Input[str]] = None,
                                      device_group_name: Optional[pulumi.Input[Optional[str]]] = None,
                                      filter: Optional[pulumi.Input[Optional[str]]] = None,
                                      maxpagesize: Optional[pulumi.Input[Optional[int]]] = None,
                                      resource_group_name: Optional[pulumi.Input[str]] = None,
                                      skip: Optional[pulumi.Input[Optional[int]]] = None,
                                      top: Optional[pulumi.Input[Optional[int]]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListCatalogDeviceGroupsResult]:
    """
    List the device groups for the catalog.


    :param str catalog_name: Name of catalog
    :param str device_group_name: Device Group name.
    :param str filter: Filter the result list using the given expression
    :param int maxpagesize: The maximum number of result items per page.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param int skip: The number of result items to skip.
    :param int top: The number of result items to return.
    """
    ...
