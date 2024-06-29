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
    'ListMobileNetworkSimGroupsResult',
    'AwaitableListMobileNetworkSimGroupsResult',
    'list_mobile_network_sim_groups',
    'list_mobile_network_sim_groups_output',
]

@pulumi.output_type
class ListMobileNetworkSimGroupsResult:
    """
    Response for list SIM groups API service call.
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
        The URL to get the next set of results.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.SimGroupResponse']]:
        """
        A list of SIM groups in a resource group.
        """
        return pulumi.get(self, "value")


class AwaitableListMobileNetworkSimGroupsResult(ListMobileNetworkSimGroupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListMobileNetworkSimGroupsResult(
            next_link=self.next_link,
            value=self.value)


def list_mobile_network_sim_groups(mobile_network_name: Optional[str] = None,
                                   resource_group_name: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListMobileNetworkSimGroupsResult:
    """
    Gets all the SIM groups assigned to a mobile network.
    Azure REST API version: 2024-04-01.


    :param str mobile_network_name: The name of the mobile network.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['mobileNetworkName'] = mobile_network_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:mobilenetwork:listMobileNetworkSimGroups', __args__, opts=opts, typ=ListMobileNetworkSimGroupsResult).value

    return AwaitableListMobileNetworkSimGroupsResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_mobile_network_sim_groups)
def list_mobile_network_sim_groups_output(mobile_network_name: Optional[pulumi.Input[str]] = None,
                                          resource_group_name: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListMobileNetworkSimGroupsResult]:
    """
    Gets all the SIM groups assigned to a mobile network.
    Azure REST API version: 2024-04-01.


    :param str mobile_network_name: The name of the mobile network.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
