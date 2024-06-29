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
    'GetVpnSiteResult',
    'AwaitableGetVpnSiteResult',
    'get_vpn_site',
    'get_vpn_site_output',
]

@pulumi.output_type
class GetVpnSiteResult:
    """
    VpnSite Resource.
    """
    def __init__(__self__, address_space=None, bgp_properties=None, device_properties=None, etag=None, id=None, ip_address=None, is_security_site=None, location=None, name=None, o365_policy=None, provisioning_state=None, site_key=None, tags=None, type=None, virtual_wan=None, vpn_site_links=None):
        if address_space and not isinstance(address_space, dict):
            raise TypeError("Expected argument 'address_space' to be a dict")
        pulumi.set(__self__, "address_space", address_space)
        if bgp_properties and not isinstance(bgp_properties, dict):
            raise TypeError("Expected argument 'bgp_properties' to be a dict")
        pulumi.set(__self__, "bgp_properties", bgp_properties)
        if device_properties and not isinstance(device_properties, dict):
            raise TypeError("Expected argument 'device_properties' to be a dict")
        pulumi.set(__self__, "device_properties", device_properties)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_address and not isinstance(ip_address, str):
            raise TypeError("Expected argument 'ip_address' to be a str")
        pulumi.set(__self__, "ip_address", ip_address)
        if is_security_site and not isinstance(is_security_site, bool):
            raise TypeError("Expected argument 'is_security_site' to be a bool")
        pulumi.set(__self__, "is_security_site", is_security_site)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if o365_policy and not isinstance(o365_policy, dict):
            raise TypeError("Expected argument 'o365_policy' to be a dict")
        pulumi.set(__self__, "o365_policy", o365_policy)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if site_key and not isinstance(site_key, str):
            raise TypeError("Expected argument 'site_key' to be a str")
        pulumi.set(__self__, "site_key", site_key)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_wan and not isinstance(virtual_wan, dict):
            raise TypeError("Expected argument 'virtual_wan' to be a dict")
        pulumi.set(__self__, "virtual_wan", virtual_wan)
        if vpn_site_links and not isinstance(vpn_site_links, list):
            raise TypeError("Expected argument 'vpn_site_links' to be a list")
        pulumi.set(__self__, "vpn_site_links", vpn_site_links)

    @property
    @pulumi.getter(name="addressSpace")
    def address_space(self) -> Optional['outputs.AddressSpaceResponse']:
        """
        The AddressSpace that contains an array of IP address ranges.
        """
        return pulumi.get(self, "address_space")

    @property
    @pulumi.getter(name="bgpProperties")
    def bgp_properties(self) -> Optional['outputs.BgpSettingsResponse']:
        """
        The set of bgp properties.
        """
        return pulumi.get(self, "bgp_properties")

    @property
    @pulumi.getter(name="deviceProperties")
    def device_properties(self) -> Optional['outputs.DevicePropertiesResponse']:
        """
        The device properties.
        """
        return pulumi.get(self, "device_properties")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[str]:
        """
        The ip-address for the vpn-site.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="isSecuritySite")
    def is_security_site(self) -> Optional[bool]:
        """
        IsSecuritySite flag.
        """
        return pulumi.get(self, "is_security_site")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="o365Policy")
    def o365_policy(self) -> Optional['outputs.O365PolicyPropertiesResponse']:
        """
        Office365 Policy.
        """
        return pulumi.get(self, "o365_policy")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the VPN site resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="siteKey")
    def site_key(self) -> Optional[str]:
        """
        The key for vpn-site that can be used for connections.
        """
        return pulumi.get(self, "site_key")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualWan")
    def virtual_wan(self) -> Optional['outputs.SubResourceResponse']:
        """
        The VirtualWAN to which the vpnSite belongs.
        """
        return pulumi.get(self, "virtual_wan")

    @property
    @pulumi.getter(name="vpnSiteLinks")
    def vpn_site_links(self) -> Optional[Sequence['outputs.VpnSiteLinkResponse']]:
        """
        List of all vpn site links.
        """
        return pulumi.get(self, "vpn_site_links")


class AwaitableGetVpnSiteResult(GetVpnSiteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpnSiteResult(
            address_space=self.address_space,
            bgp_properties=self.bgp_properties,
            device_properties=self.device_properties,
            etag=self.etag,
            id=self.id,
            ip_address=self.ip_address,
            is_security_site=self.is_security_site,
            location=self.location,
            name=self.name,
            o365_policy=self.o365_policy,
            provisioning_state=self.provisioning_state,
            site_key=self.site_key,
            tags=self.tags,
            type=self.type,
            virtual_wan=self.virtual_wan,
            vpn_site_links=self.vpn_site_links)


def get_vpn_site(resource_group_name: Optional[str] = None,
                 vpn_site_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpnSiteResult:
    """
    Retrieves the details of a VPN site.


    :param str resource_group_name: The resource group name of the VpnSite.
    :param str vpn_site_name: The name of the VpnSite being retrieved.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['vpnSiteName'] = vpn_site_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20230201:getVpnSite', __args__, opts=opts, typ=GetVpnSiteResult).value

    return AwaitableGetVpnSiteResult(
        address_space=pulumi.get(__ret__, 'address_space'),
        bgp_properties=pulumi.get(__ret__, 'bgp_properties'),
        device_properties=pulumi.get(__ret__, 'device_properties'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        ip_address=pulumi.get(__ret__, 'ip_address'),
        is_security_site=pulumi.get(__ret__, 'is_security_site'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        o365_policy=pulumi.get(__ret__, 'o365_policy'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        site_key=pulumi.get(__ret__, 'site_key'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        virtual_wan=pulumi.get(__ret__, 'virtual_wan'),
        vpn_site_links=pulumi.get(__ret__, 'vpn_site_links'))


@_utilities.lift_output_func(get_vpn_site)
def get_vpn_site_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                        vpn_site_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVpnSiteResult]:
    """
    Retrieves the details of a VPN site.


    :param str resource_group_name: The resource group name of the VpnSite.
    :param str vpn_site_name: The name of the VpnSite being retrieved.
    """
    ...
