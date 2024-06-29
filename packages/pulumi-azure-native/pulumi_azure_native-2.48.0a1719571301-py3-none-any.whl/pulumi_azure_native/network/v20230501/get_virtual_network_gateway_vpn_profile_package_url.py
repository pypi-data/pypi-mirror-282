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
    'GetVirtualNetworkGatewayVpnProfilePackageUrlResult',
    'AwaitableGetVirtualNetworkGatewayVpnProfilePackageUrlResult',
    'get_virtual_network_gateway_vpn_profile_package_url',
    'get_virtual_network_gateway_vpn_profile_package_url_output',
]

@pulumi.output_type
class GetVirtualNetworkGatewayVpnProfilePackageUrlResult:
    def __init__(__self__, value=None):
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


class AwaitableGetVirtualNetworkGatewayVpnProfilePackageUrlResult(GetVirtualNetworkGatewayVpnProfilePackageUrlResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualNetworkGatewayVpnProfilePackageUrlResult(
            value=self.value)


def get_virtual_network_gateway_vpn_profile_package_url(resource_group_name: Optional[str] = None,
                                                        virtual_network_gateway_name: Optional[str] = None,
                                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualNetworkGatewayVpnProfilePackageUrlResult:
    """
    Gets pre-generated VPN profile for P2S client of the virtual network gateway in the specified resource group. The profile needs to be generated first using generateVpnProfile.


    :param str resource_group_name: The name of the resource group.
    :param str virtual_network_gateway_name: The name of the virtual network gateway.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['virtualNetworkGatewayName'] = virtual_network_gateway_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20230501:getVirtualNetworkGatewayVpnProfilePackageUrl', __args__, opts=opts, typ=GetVirtualNetworkGatewayVpnProfilePackageUrlResult).value

    return AwaitableGetVirtualNetworkGatewayVpnProfilePackageUrlResult(
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(get_virtual_network_gateway_vpn_profile_package_url)
def get_virtual_network_gateway_vpn_profile_package_url_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                                               virtual_network_gateway_name: Optional[pulumi.Input[str]] = None,
                                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualNetworkGatewayVpnProfilePackageUrlResult]:
    """
    Gets pre-generated VPN profile for P2S client of the virtual network gateway in the specified resource group. The profile needs to be generated first using generateVpnProfile.


    :param str resource_group_name: The name of the resource group.
    :param str virtual_network_gateway_name: The name of the virtual network gateway.
    """
    ...
