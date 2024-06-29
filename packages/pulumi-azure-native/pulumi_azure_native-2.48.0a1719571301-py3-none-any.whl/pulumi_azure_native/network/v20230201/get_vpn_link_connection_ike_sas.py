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
    'GetVpnLinkConnectionIkeSasResult',
    'AwaitableGetVpnLinkConnectionIkeSasResult',
    'get_vpn_link_connection_ike_sas',
    'get_vpn_link_connection_ike_sas_output',
]

@pulumi.output_type
class GetVpnLinkConnectionIkeSasResult:
    def __init__(__self__, value=None):
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


class AwaitableGetVpnLinkConnectionIkeSasResult(GetVpnLinkConnectionIkeSasResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpnLinkConnectionIkeSasResult(
            value=self.value)


def get_vpn_link_connection_ike_sas(connection_name: Optional[str] = None,
                                    gateway_name: Optional[str] = None,
                                    link_connection_name: Optional[str] = None,
                                    resource_group_name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpnLinkConnectionIkeSasResult:
    """
    Lists IKE Security Associations for Vpn Site Link Connection in the specified resource group.


    :param str connection_name: The name of the vpn connection.
    :param str gateway_name: The name of the gateway.
    :param str link_connection_name: The name of the vpn link connection.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['connectionName'] = connection_name
    __args__['gatewayName'] = gateway_name
    __args__['linkConnectionName'] = link_connection_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20230201:getVpnLinkConnectionIkeSas', __args__, opts=opts, typ=GetVpnLinkConnectionIkeSasResult).value

    return AwaitableGetVpnLinkConnectionIkeSasResult(
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(get_vpn_link_connection_ike_sas)
def get_vpn_link_connection_ike_sas_output(connection_name: Optional[pulumi.Input[str]] = None,
                                           gateway_name: Optional[pulumi.Input[str]] = None,
                                           link_connection_name: Optional[pulumi.Input[str]] = None,
                                           resource_group_name: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVpnLinkConnectionIkeSasResult]:
    """
    Lists IKE Security Associations for Vpn Site Link Connection in the specified resource group.


    :param str connection_name: The name of the vpn connection.
    :param str gateway_name: The name of the gateway.
    :param str link_connection_name: The name of the vpn link connection.
    :param str resource_group_name: The name of the resource group.
    """
    ...
