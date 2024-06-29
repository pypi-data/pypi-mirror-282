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
    'GetVirtualNetworkGatewayConnectionIkeSasResult',
    'AwaitableGetVirtualNetworkGatewayConnectionIkeSasResult',
    'get_virtual_network_gateway_connection_ike_sas',
    'get_virtual_network_gateway_connection_ike_sas_output',
]

@pulumi.output_type
class GetVirtualNetworkGatewayConnectionIkeSasResult:
    def __init__(__self__, value=None):
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


class AwaitableGetVirtualNetworkGatewayConnectionIkeSasResult(GetVirtualNetworkGatewayConnectionIkeSasResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualNetworkGatewayConnectionIkeSasResult(
            value=self.value)


def get_virtual_network_gateway_connection_ike_sas(resource_group_name: Optional[str] = None,
                                                   virtual_network_gateway_connection_name: Optional[str] = None,
                                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualNetworkGatewayConnectionIkeSasResult:
    """
    Lists IKE Security Associations for the virtual network gateway connection in the specified resource group.


    :param str resource_group_name: The name of the resource group.
    :param str virtual_network_gateway_connection_name: The name of the virtual network gateway Connection.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['virtualNetworkGatewayConnectionName'] = virtual_network_gateway_connection_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20230601:getVirtualNetworkGatewayConnectionIkeSas', __args__, opts=opts, typ=GetVirtualNetworkGatewayConnectionIkeSasResult).value

    return AwaitableGetVirtualNetworkGatewayConnectionIkeSasResult(
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(get_virtual_network_gateway_connection_ike_sas)
def get_virtual_network_gateway_connection_ike_sas_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                                          virtual_network_gateway_connection_name: Optional[pulumi.Input[str]] = None,
                                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualNetworkGatewayConnectionIkeSasResult]:
    """
    Lists IKE Security Associations for the virtual network gateway connection in the specified resource group.


    :param str resource_group_name: The name of the resource group.
    :param str virtual_network_gateway_connection_name: The name of the virtual network gateway Connection.
    """
    ...
