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
    'GetWorkloadNetworkDhcpResult',
    'AwaitableGetWorkloadNetworkDhcpResult',
    'get_workload_network_dhcp',
    'get_workload_network_dhcp_output',
]

@pulumi.output_type
class GetWorkloadNetworkDhcpResult:
    """
    NSX DHCP
    """
    def __init__(__self__, dhcp_type=None, display_name=None, id=None, name=None, provisioning_state=None, revision=None, segments=None, type=None):
        if dhcp_type and not isinstance(dhcp_type, str):
            raise TypeError("Expected argument 'dhcp_type' to be a str")
        pulumi.set(__self__, "dhcp_type", dhcp_type)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if revision and not isinstance(revision, float):
            raise TypeError("Expected argument 'revision' to be a float")
        pulumi.set(__self__, "revision", revision)
        if segments and not isinstance(segments, list):
            raise TypeError("Expected argument 'segments' to be a list")
        pulumi.set(__self__, "segments", segments)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="dhcpType")
    def dhcp_type(self) -> str:
        """
        Type of DHCP: SERVER or RELAY.
        """
        return pulumi.get(self, "dhcp_type")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        Display name of the DHCP entity.
        """
        return pulumi.get(self, "display_name")

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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def revision(self) -> Optional[float]:
        """
        NSX revision number.
        """
        return pulumi.get(self, "revision")

    @property
    @pulumi.getter
    def segments(self) -> Sequence[str]:
        """
        NSX Segments consuming DHCP.
        """
        return pulumi.get(self, "segments")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetWorkloadNetworkDhcpResult(GetWorkloadNetworkDhcpResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkloadNetworkDhcpResult(
            dhcp_type=self.dhcp_type,
            display_name=self.display_name,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            revision=self.revision,
            segments=self.segments,
            type=self.type)


def get_workload_network_dhcp(dhcp_id: Optional[str] = None,
                              private_cloud_name: Optional[str] = None,
                              resource_group_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkloadNetworkDhcpResult:
    """
    NSX DHCP


    :param str dhcp_id: NSX DHCP identifier. Generally the same as the DHCP display name
    :param str private_cloud_name: Name of the private cloud
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['dhcpId'] = dhcp_id
    __args__['privateCloudName'] = private_cloud_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:avs/v20210101preview:getWorkloadNetworkDhcp', __args__, opts=opts, typ=GetWorkloadNetworkDhcpResult).value

    return AwaitableGetWorkloadNetworkDhcpResult(
        dhcp_type=pulumi.get(__ret__, 'dhcp_type'),
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        revision=pulumi.get(__ret__, 'revision'),
        segments=pulumi.get(__ret__, 'segments'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_workload_network_dhcp)
def get_workload_network_dhcp_output(dhcp_id: Optional[pulumi.Input[str]] = None,
                                     private_cloud_name: Optional[pulumi.Input[str]] = None,
                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkloadNetworkDhcpResult]:
    """
    NSX DHCP


    :param str dhcp_id: NSX DHCP identifier. Generally the same as the DHCP display name
    :param str private_cloud_name: Name of the private cloud
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
