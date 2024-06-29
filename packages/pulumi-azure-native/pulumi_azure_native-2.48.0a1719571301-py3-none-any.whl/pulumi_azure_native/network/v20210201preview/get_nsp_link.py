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
    'GetNspLinkResult',
    'AwaitableGetNspLinkResult',
    'get_nsp_link',
    'get_nsp_link_output',
]

@pulumi.output_type
class GetNspLinkResult:
    """
    The network security perimeter link resource
    """
    def __init__(__self__, auto_approved_remote_perimeter_resource_id=None, description=None, etag=None, id=None, local_inbound_profiles=None, local_outbound_profiles=None, name=None, provisioning_state=None, remote_inbound_profiles=None, remote_outbound_profiles=None, remote_perimeter_guid=None, remote_perimeter_location=None, status=None, type=None):
        if auto_approved_remote_perimeter_resource_id and not isinstance(auto_approved_remote_perimeter_resource_id, str):
            raise TypeError("Expected argument 'auto_approved_remote_perimeter_resource_id' to be a str")
        pulumi.set(__self__, "auto_approved_remote_perimeter_resource_id", auto_approved_remote_perimeter_resource_id)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if local_inbound_profiles and not isinstance(local_inbound_profiles, list):
            raise TypeError("Expected argument 'local_inbound_profiles' to be a list")
        pulumi.set(__self__, "local_inbound_profiles", local_inbound_profiles)
        if local_outbound_profiles and not isinstance(local_outbound_profiles, list):
            raise TypeError("Expected argument 'local_outbound_profiles' to be a list")
        pulumi.set(__self__, "local_outbound_profiles", local_outbound_profiles)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if remote_inbound_profiles and not isinstance(remote_inbound_profiles, list):
            raise TypeError("Expected argument 'remote_inbound_profiles' to be a list")
        pulumi.set(__self__, "remote_inbound_profiles", remote_inbound_profiles)
        if remote_outbound_profiles and not isinstance(remote_outbound_profiles, list):
            raise TypeError("Expected argument 'remote_outbound_profiles' to be a list")
        pulumi.set(__self__, "remote_outbound_profiles", remote_outbound_profiles)
        if remote_perimeter_guid and not isinstance(remote_perimeter_guid, str):
            raise TypeError("Expected argument 'remote_perimeter_guid' to be a str")
        pulumi.set(__self__, "remote_perimeter_guid", remote_perimeter_guid)
        if remote_perimeter_location and not isinstance(remote_perimeter_location, str):
            raise TypeError("Expected argument 'remote_perimeter_location' to be a str")
        pulumi.set(__self__, "remote_perimeter_location", remote_perimeter_location)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="autoApprovedRemotePerimeterResourceId")
    def auto_approved_remote_perimeter_resource_id(self) -> Optional[str]:
        """
        Perimeter ARM Id for the remote NSP with which the link gets created in Auto-approval mode. It should be used when the NSP admin have Microsoft.Network/networkSecurityPerimeters/linkPerimeter/action permission on the remote NSP resource.
        """
        return pulumi.get(self, "auto_approved_remote_perimeter_resource_id")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A message passed to the owner of the remote NSP link resource with this connection request. In case of Auto-approved flow, it is default to 'Auto Approved'. Restricted to 140 chars.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="localInboundProfiles")
    def local_inbound_profiles(self) -> Optional[Sequence[str]]:
        """
        Local Inbound profile names to which Inbound is allowed. Use ['*'] to allow inbound to all profiles. It's default value is ['*'].
        """
        return pulumi.get(self, "local_inbound_profiles")

    @property
    @pulumi.getter(name="localOutboundProfiles")
    def local_outbound_profiles(self) -> Sequence[str]:
        """
        Local Outbound profile names from which Outbound is allowed. In current version, it is readonly property and it's value is set to ['*'] to allow outbound from all profiles. In later version, user will be able to modify it.
        """
        return pulumi.get(self, "local_outbound_profiles")

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
        The provisioning state of the NSP Link resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="remoteInboundProfiles")
    def remote_inbound_profiles(self) -> Optional[Sequence[str]]:
        """
        Remote Inbound profile names to which Inbound is allowed. Use ['*'] to allow inbound to all profiles. This property can only be updated in auto-approval mode. It's default value is ['*'].
        """
        return pulumi.get(self, "remote_inbound_profiles")

    @property
    @pulumi.getter(name="remoteOutboundProfiles")
    def remote_outbound_profiles(self) -> Sequence[str]:
        """
        Remote Outbound profile names from which Outbound is allowed. In current version, it is readonly property and it's value is set to ['*'] to allow outbound from all profiles. In later version, user will be able to modify it.
        """
        return pulumi.get(self, "remote_outbound_profiles")

    @property
    @pulumi.getter(name="remotePerimeterGuid")
    def remote_perimeter_guid(self) -> str:
        """
        Remote NSP Guid with which the link gets created.
        """
        return pulumi.get(self, "remote_perimeter_guid")

    @property
    @pulumi.getter(name="remotePerimeterLocation")
    def remote_perimeter_location(self) -> str:
        """
        Remote NSP location with which the link gets created.
        """
        return pulumi.get(self, "remote_perimeter_location")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The NSP link state.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetNspLinkResult(GetNspLinkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNspLinkResult(
            auto_approved_remote_perimeter_resource_id=self.auto_approved_remote_perimeter_resource_id,
            description=self.description,
            etag=self.etag,
            id=self.id,
            local_inbound_profiles=self.local_inbound_profiles,
            local_outbound_profiles=self.local_outbound_profiles,
            name=self.name,
            provisioning_state=self.provisioning_state,
            remote_inbound_profiles=self.remote_inbound_profiles,
            remote_outbound_profiles=self.remote_outbound_profiles,
            remote_perimeter_guid=self.remote_perimeter_guid,
            remote_perimeter_location=self.remote_perimeter_location,
            status=self.status,
            type=self.type)


def get_nsp_link(link_name: Optional[str] = None,
                 network_security_perimeter_name: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNspLinkResult:
    """
    Gets the specified NSP link resource.


    :param str link_name: The name of the NSP link.
    :param str network_security_perimeter_name: The name of the network security perimeter.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['linkName'] = link_name
    __args__['networkSecurityPerimeterName'] = network_security_perimeter_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20210201preview:getNspLink', __args__, opts=opts, typ=GetNspLinkResult).value

    return AwaitableGetNspLinkResult(
        auto_approved_remote_perimeter_resource_id=pulumi.get(__ret__, 'auto_approved_remote_perimeter_resource_id'),
        description=pulumi.get(__ret__, 'description'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        local_inbound_profiles=pulumi.get(__ret__, 'local_inbound_profiles'),
        local_outbound_profiles=pulumi.get(__ret__, 'local_outbound_profiles'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        remote_inbound_profiles=pulumi.get(__ret__, 'remote_inbound_profiles'),
        remote_outbound_profiles=pulumi.get(__ret__, 'remote_outbound_profiles'),
        remote_perimeter_guid=pulumi.get(__ret__, 'remote_perimeter_guid'),
        remote_perimeter_location=pulumi.get(__ret__, 'remote_perimeter_location'),
        status=pulumi.get(__ret__, 'status'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_nsp_link)
def get_nsp_link_output(link_name: Optional[pulumi.Input[str]] = None,
                        network_security_perimeter_name: Optional[pulumi.Input[str]] = None,
                        resource_group_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNspLinkResult]:
    """
    Gets the specified NSP link resource.


    :param str link_name: The name of the NSP link.
    :param str network_security_perimeter_name: The name of the network security perimeter.
    :param str resource_group_name: The name of the resource group.
    """
    ...
