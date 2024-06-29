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
    'GetCustomIPPrefixResult',
    'AwaitableGetCustomIPPrefixResult',
    'get_custom_ip_prefix',
    'get_custom_ip_prefix_output',
]

@pulumi.output_type
class GetCustomIPPrefixResult:
    """
    Custom IP prefix resource.
    """
    def __init__(__self__, asn=None, authorization_message=None, child_custom_ip_prefixes=None, cidr=None, commissioned_state=None, custom_ip_prefix_parent=None, etag=None, express_route_advertise=None, extended_location=None, failed_reason=None, geo=None, id=None, location=None, name=None, no_internet_advertise=None, prefix_type=None, provisioning_state=None, public_ip_prefixes=None, resource_guid=None, signed_message=None, tags=None, type=None, zones=None):
        if asn and not isinstance(asn, str):
            raise TypeError("Expected argument 'asn' to be a str")
        pulumi.set(__self__, "asn", asn)
        if authorization_message and not isinstance(authorization_message, str):
            raise TypeError("Expected argument 'authorization_message' to be a str")
        pulumi.set(__self__, "authorization_message", authorization_message)
        if child_custom_ip_prefixes and not isinstance(child_custom_ip_prefixes, list):
            raise TypeError("Expected argument 'child_custom_ip_prefixes' to be a list")
        pulumi.set(__self__, "child_custom_ip_prefixes", child_custom_ip_prefixes)
        if cidr and not isinstance(cidr, str):
            raise TypeError("Expected argument 'cidr' to be a str")
        pulumi.set(__self__, "cidr", cidr)
        if commissioned_state and not isinstance(commissioned_state, str):
            raise TypeError("Expected argument 'commissioned_state' to be a str")
        pulumi.set(__self__, "commissioned_state", commissioned_state)
        if custom_ip_prefix_parent and not isinstance(custom_ip_prefix_parent, dict):
            raise TypeError("Expected argument 'custom_ip_prefix_parent' to be a dict")
        pulumi.set(__self__, "custom_ip_prefix_parent", custom_ip_prefix_parent)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if express_route_advertise and not isinstance(express_route_advertise, bool):
            raise TypeError("Expected argument 'express_route_advertise' to be a bool")
        pulumi.set(__self__, "express_route_advertise", express_route_advertise)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if failed_reason and not isinstance(failed_reason, str):
            raise TypeError("Expected argument 'failed_reason' to be a str")
        pulumi.set(__self__, "failed_reason", failed_reason)
        if geo and not isinstance(geo, str):
            raise TypeError("Expected argument 'geo' to be a str")
        pulumi.set(__self__, "geo", geo)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if no_internet_advertise and not isinstance(no_internet_advertise, bool):
            raise TypeError("Expected argument 'no_internet_advertise' to be a bool")
        pulumi.set(__self__, "no_internet_advertise", no_internet_advertise)
        if prefix_type and not isinstance(prefix_type, str):
            raise TypeError("Expected argument 'prefix_type' to be a str")
        pulumi.set(__self__, "prefix_type", prefix_type)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_ip_prefixes and not isinstance(public_ip_prefixes, list):
            raise TypeError("Expected argument 'public_ip_prefixes' to be a list")
        pulumi.set(__self__, "public_ip_prefixes", public_ip_prefixes)
        if resource_guid and not isinstance(resource_guid, str):
            raise TypeError("Expected argument 'resource_guid' to be a str")
        pulumi.set(__self__, "resource_guid", resource_guid)
        if signed_message and not isinstance(signed_message, str):
            raise TypeError("Expected argument 'signed_message' to be a str")
        pulumi.set(__self__, "signed_message", signed_message)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if zones and not isinstance(zones, list):
            raise TypeError("Expected argument 'zones' to be a list")
        pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter
    def asn(self) -> Optional[str]:
        """
        The ASN for CIDR advertising. Should be an integer as string.
        """
        return pulumi.get(self, "asn")

    @property
    @pulumi.getter(name="authorizationMessage")
    def authorization_message(self) -> Optional[str]:
        """
        Authorization message for WAN validation.
        """
        return pulumi.get(self, "authorization_message")

    @property
    @pulumi.getter(name="childCustomIpPrefixes")
    def child_custom_ip_prefixes(self) -> Sequence['outputs.SubResourceResponse']:
        """
        The list of all Children for IPv6 /48 CustomIpPrefix.
        """
        return pulumi.get(self, "child_custom_ip_prefixes")

    @property
    @pulumi.getter
    def cidr(self) -> Optional[str]:
        """
        The prefix range in CIDR notation. Should include the start address and the prefix length.
        """
        return pulumi.get(self, "cidr")

    @property
    @pulumi.getter(name="commissionedState")
    def commissioned_state(self) -> Optional[str]:
        """
        The commissioned state of the Custom IP Prefix.
        """
        return pulumi.get(self, "commissioned_state")

    @property
    @pulumi.getter(name="customIpPrefixParent")
    def custom_ip_prefix_parent(self) -> Optional['outputs.SubResourceResponse']:
        """
        The Parent CustomIpPrefix for IPv6 /64 CustomIpPrefix.
        """
        return pulumi.get(self, "custom_ip_prefix_parent")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="expressRouteAdvertise")
    def express_route_advertise(self) -> Optional[bool]:
        """
        Whether to do express route advertise.
        """
        return pulumi.get(self, "express_route_advertise")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional['outputs.ExtendedLocationResponse']:
        """
        The extended location of the custom IP prefix.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="failedReason")
    def failed_reason(self) -> str:
        """
        The reason why resource is in failed state.
        """
        return pulumi.get(self, "failed_reason")

    @property
    @pulumi.getter
    def geo(self) -> Optional[str]:
        """
        The Geo for CIDR advertising. Should be an Geo code.
        """
        return pulumi.get(self, "geo")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
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
    @pulumi.getter(name="noInternetAdvertise")
    def no_internet_advertise(self) -> Optional[bool]:
        """
        Whether to Advertise the range to Internet.
        """
        return pulumi.get(self, "no_internet_advertise")

    @property
    @pulumi.getter(name="prefixType")
    def prefix_type(self) -> Optional[str]:
        """
        Type of custom IP prefix. Should be Singular, Parent, or Child.
        """
        return pulumi.get(self, "prefix_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the custom IP prefix resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicIpPrefixes")
    def public_ip_prefixes(self) -> Sequence['outputs.SubResourceResponse']:
        """
        The list of all referenced PublicIpPrefixes.
        """
        return pulumi.get(self, "public_ip_prefixes")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> str:
        """
        The resource GUID property of the custom IP prefix resource.
        """
        return pulumi.get(self, "resource_guid")

    @property
    @pulumi.getter(name="signedMessage")
    def signed_message(self) -> Optional[str]:
        """
        Signed message for WAN validation.
        """
        return pulumi.get(self, "signed_message")

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
    @pulumi.getter
    def zones(self) -> Optional[Sequence[str]]:
        """
        A list of availability zones denoting the IP allocated for the resource needs to come from.
        """
        return pulumi.get(self, "zones")


class AwaitableGetCustomIPPrefixResult(GetCustomIPPrefixResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCustomIPPrefixResult(
            asn=self.asn,
            authorization_message=self.authorization_message,
            child_custom_ip_prefixes=self.child_custom_ip_prefixes,
            cidr=self.cidr,
            commissioned_state=self.commissioned_state,
            custom_ip_prefix_parent=self.custom_ip_prefix_parent,
            etag=self.etag,
            express_route_advertise=self.express_route_advertise,
            extended_location=self.extended_location,
            failed_reason=self.failed_reason,
            geo=self.geo,
            id=self.id,
            location=self.location,
            name=self.name,
            no_internet_advertise=self.no_internet_advertise,
            prefix_type=self.prefix_type,
            provisioning_state=self.provisioning_state,
            public_ip_prefixes=self.public_ip_prefixes,
            resource_guid=self.resource_guid,
            signed_message=self.signed_message,
            tags=self.tags,
            type=self.type,
            zones=self.zones)


def get_custom_ip_prefix(custom_ip_prefix_name: Optional[str] = None,
                         expand: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCustomIPPrefixResult:
    """
    Gets the specified custom IP prefix in a specified resource group.


    :param str custom_ip_prefix_name: The name of the custom IP prefix.
    :param str expand: Expands referenced resources.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['customIpPrefixName'] = custom_ip_prefix_name
    __args__['expand'] = expand
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20231101:getCustomIPPrefix', __args__, opts=opts, typ=GetCustomIPPrefixResult).value

    return AwaitableGetCustomIPPrefixResult(
        asn=pulumi.get(__ret__, 'asn'),
        authorization_message=pulumi.get(__ret__, 'authorization_message'),
        child_custom_ip_prefixes=pulumi.get(__ret__, 'child_custom_ip_prefixes'),
        cidr=pulumi.get(__ret__, 'cidr'),
        commissioned_state=pulumi.get(__ret__, 'commissioned_state'),
        custom_ip_prefix_parent=pulumi.get(__ret__, 'custom_ip_prefix_parent'),
        etag=pulumi.get(__ret__, 'etag'),
        express_route_advertise=pulumi.get(__ret__, 'express_route_advertise'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        failed_reason=pulumi.get(__ret__, 'failed_reason'),
        geo=pulumi.get(__ret__, 'geo'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        no_internet_advertise=pulumi.get(__ret__, 'no_internet_advertise'),
        prefix_type=pulumi.get(__ret__, 'prefix_type'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        public_ip_prefixes=pulumi.get(__ret__, 'public_ip_prefixes'),
        resource_guid=pulumi.get(__ret__, 'resource_guid'),
        signed_message=pulumi.get(__ret__, 'signed_message'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        zones=pulumi.get(__ret__, 'zones'))


@_utilities.lift_output_func(get_custom_ip_prefix)
def get_custom_ip_prefix_output(custom_ip_prefix_name: Optional[pulumi.Input[str]] = None,
                                expand: Optional[pulumi.Input[Optional[str]]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCustomIPPrefixResult]:
    """
    Gets the specified custom IP prefix in a specified resource group.


    :param str custom_ip_prefix_name: The name of the custom IP prefix.
    :param str expand: Expands referenced resources.
    :param str resource_group_name: The name of the resource group.
    """
    ...
