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
    'GetBgpPeerResult',
    'AwaitableGetBgpPeerResult',
    'get_bgp_peer',
    'get_bgp_peer_output',
]

@pulumi.output_type
class GetBgpPeerResult:
    """
    A BgpPeer resource for an Arc connected cluster (Microsoft.Kubernetes/connectedClusters)
    """
    def __init__(__self__, id=None, my_asn=None, name=None, peer_address=None, peer_asn=None, provisioning_state=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if my_asn and not isinstance(my_asn, int):
            raise TypeError("Expected argument 'my_asn' to be a int")
        pulumi.set(__self__, "my_asn", my_asn)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if peer_address and not isinstance(peer_address, str):
            raise TypeError("Expected argument 'peer_address' to be a str")
        pulumi.set(__self__, "peer_address", peer_address)
        if peer_asn and not isinstance(peer_asn, int):
            raise TypeError("Expected argument 'peer_asn' to be a int")
        pulumi.set(__self__, "peer_asn", peer_asn)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="myAsn")
    def my_asn(self) -> int:
        """
        My ASN
        """
        return pulumi.get(self, "my_asn")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peerAddress")
    def peer_address(self) -> str:
        """
        Peer Address
        """
        return pulumi.get(self, "peer_address")

    @property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> int:
        """
        Peer ASN
        """
        return pulumi.get(self, "peer_asn")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Resource provision state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetBgpPeerResult(GetBgpPeerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBgpPeerResult(
            id=self.id,
            my_asn=self.my_asn,
            name=self.name,
            peer_address=self.peer_address,
            peer_asn=self.peer_asn,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_bgp_peer(bgp_peer_name: Optional[str] = None,
                 resource_uri: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBgpPeerResult:
    """
    Get a BgpPeer
    Azure REST API version: 2024-03-01.

    Other available API versions: 2023-10-01-preview.


    :param str bgp_peer_name: The name of the BgpPeer
    :param str resource_uri: The fully qualified Azure Resource manager identifier of the resource.
    """
    __args__ = dict()
    __args__['bgpPeerName'] = bgp_peer_name
    __args__['resourceUri'] = resource_uri
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:kubernetesruntime:getBgpPeer', __args__, opts=opts, typ=GetBgpPeerResult).value

    return AwaitableGetBgpPeerResult(
        id=pulumi.get(__ret__, 'id'),
        my_asn=pulumi.get(__ret__, 'my_asn'),
        name=pulumi.get(__ret__, 'name'),
        peer_address=pulumi.get(__ret__, 'peer_address'),
        peer_asn=pulumi.get(__ret__, 'peer_asn'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_bgp_peer)
def get_bgp_peer_output(bgp_peer_name: Optional[pulumi.Input[str]] = None,
                        resource_uri: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBgpPeerResult]:
    """
    Get a BgpPeer
    Azure REST API version: 2024-03-01.

    Other available API versions: 2023-10-01-preview.


    :param str bgp_peer_name: The name of the BgpPeer
    :param str resource_uri: The fully qualified Azure Resource manager identifier of the resource.
    """
    ...
