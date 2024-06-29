# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'ListGeodataByIpResult',
    'AwaitableListGeodataByIpResult',
    'list_geodata_by_ip',
    'list_geodata_by_ip_output',
]

@pulumi.output_type
class ListGeodataByIpResult:
    """
    Geodata information for a given IP address
    """
    def __init__(__self__, asn=None, carrier=None, city=None, city_confidence_factor=None, continent=None, country=None, country_confidence_factor=None, ip_addr=None, ip_routing_type=None, latitude=None, longitude=None, organization=None, organization_type=None, region=None, state=None, state_code=None, state_confidence_factor=None):
        if asn and not isinstance(asn, str):
            raise TypeError("Expected argument 'asn' to be a str")
        pulumi.set(__self__, "asn", asn)
        if carrier and not isinstance(carrier, str):
            raise TypeError("Expected argument 'carrier' to be a str")
        pulumi.set(__self__, "carrier", carrier)
        if city and not isinstance(city, str):
            raise TypeError("Expected argument 'city' to be a str")
        pulumi.set(__self__, "city", city)
        if city_confidence_factor and not isinstance(city_confidence_factor, int):
            raise TypeError("Expected argument 'city_confidence_factor' to be a int")
        pulumi.set(__self__, "city_confidence_factor", city_confidence_factor)
        if continent and not isinstance(continent, str):
            raise TypeError("Expected argument 'continent' to be a str")
        pulumi.set(__self__, "continent", continent)
        if country and not isinstance(country, str):
            raise TypeError("Expected argument 'country' to be a str")
        pulumi.set(__self__, "country", country)
        if country_confidence_factor and not isinstance(country_confidence_factor, int):
            raise TypeError("Expected argument 'country_confidence_factor' to be a int")
        pulumi.set(__self__, "country_confidence_factor", country_confidence_factor)
        if ip_addr and not isinstance(ip_addr, str):
            raise TypeError("Expected argument 'ip_addr' to be a str")
        pulumi.set(__self__, "ip_addr", ip_addr)
        if ip_routing_type and not isinstance(ip_routing_type, str):
            raise TypeError("Expected argument 'ip_routing_type' to be a str")
        pulumi.set(__self__, "ip_routing_type", ip_routing_type)
        if latitude and not isinstance(latitude, str):
            raise TypeError("Expected argument 'latitude' to be a str")
        pulumi.set(__self__, "latitude", latitude)
        if longitude and not isinstance(longitude, str):
            raise TypeError("Expected argument 'longitude' to be a str")
        pulumi.set(__self__, "longitude", longitude)
        if organization and not isinstance(organization, str):
            raise TypeError("Expected argument 'organization' to be a str")
        pulumi.set(__self__, "organization", organization)
        if organization_type and not isinstance(organization_type, str):
            raise TypeError("Expected argument 'organization_type' to be a str")
        pulumi.set(__self__, "organization_type", organization_type)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if state_code and not isinstance(state_code, str):
            raise TypeError("Expected argument 'state_code' to be a str")
        pulumi.set(__self__, "state_code", state_code)
        if state_confidence_factor and not isinstance(state_confidence_factor, int):
            raise TypeError("Expected argument 'state_confidence_factor' to be a int")
        pulumi.set(__self__, "state_confidence_factor", state_confidence_factor)

    @property
    @pulumi.getter
    def asn(self) -> Optional[str]:
        """
        The autonomous system number associated with this IP address
        """
        return pulumi.get(self, "asn")

    @property
    @pulumi.getter
    def carrier(self) -> Optional[str]:
        """
        The name of the carrier for this IP address
        """
        return pulumi.get(self, "carrier")

    @property
    @pulumi.getter
    def city(self) -> Optional[str]:
        """
        The city this IP address is located in
        """
        return pulumi.get(self, "city")

    @property
    @pulumi.getter(name="cityConfidenceFactor")
    def city_confidence_factor(self) -> Optional[int]:
        """
        A numeric rating of confidence that the value in the 'city' field is correct, on a scale of 0-100
        """
        return pulumi.get(self, "city_confidence_factor")

    @property
    @pulumi.getter
    def continent(self) -> Optional[str]:
        """
        The continent this IP address is located on
        """
        return pulumi.get(self, "continent")

    @property
    @pulumi.getter
    def country(self) -> Optional[str]:
        """
        The county this IP address is located in
        """
        return pulumi.get(self, "country")

    @property
    @pulumi.getter(name="countryConfidenceFactor")
    def country_confidence_factor(self) -> Optional[int]:
        """
        A numeric rating of confidence that the value in the 'country' field is correct on a scale of 0-100
        """
        return pulumi.get(self, "country_confidence_factor")

    @property
    @pulumi.getter(name="ipAddr")
    def ip_addr(self) -> Optional[str]:
        """
        The dotted-decimal or colon-separated string representation of the IP address
        """
        return pulumi.get(self, "ip_addr")

    @property
    @pulumi.getter(name="ipRoutingType")
    def ip_routing_type(self) -> Optional[str]:
        """
        A description of the connection type of this IP address
        """
        return pulumi.get(self, "ip_routing_type")

    @property
    @pulumi.getter
    def latitude(self) -> Optional[str]:
        """
        The latitude of this IP address
        """
        return pulumi.get(self, "latitude")

    @property
    @pulumi.getter
    def longitude(self) -> Optional[str]:
        """
        The longitude of this IP address
        """
        return pulumi.get(self, "longitude")

    @property
    @pulumi.getter
    def organization(self) -> Optional[str]:
        """
        The name of the organization for this IP address
        """
        return pulumi.get(self, "organization")

    @property
    @pulumi.getter(name="organizationType")
    def organization_type(self) -> Optional[str]:
        """
        The type of the organization for this IP address
        """
        return pulumi.get(self, "organization_type")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        """
        The geographic region this IP address is located in
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The state this IP address is located in
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="stateCode")
    def state_code(self) -> Optional[str]:
        """
        The abbreviated name for the state this IP address is located in
        """
        return pulumi.get(self, "state_code")

    @property
    @pulumi.getter(name="stateConfidenceFactor")
    def state_confidence_factor(self) -> Optional[int]:
        """
        A numeric rating of confidence that the value in the 'state' field is correct on a scale of 0-100
        """
        return pulumi.get(self, "state_confidence_factor")


class AwaitableListGeodataByIpResult(ListGeodataByIpResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListGeodataByIpResult(
            asn=self.asn,
            carrier=self.carrier,
            city=self.city,
            city_confidence_factor=self.city_confidence_factor,
            continent=self.continent,
            country=self.country,
            country_confidence_factor=self.country_confidence_factor,
            ip_addr=self.ip_addr,
            ip_routing_type=self.ip_routing_type,
            latitude=self.latitude,
            longitude=self.longitude,
            organization=self.organization,
            organization_type=self.organization_type,
            region=self.region,
            state=self.state,
            state_code=self.state_code,
            state_confidence_factor=self.state_confidence_factor)


def list_geodata_by_ip(enrichment_type: Optional[str] = None,
                       ip_address: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       workspace_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListGeodataByIpResult:
    """
    Get geodata for a single IP address
    Azure REST API version: 2024-01-01-preview.


    :param str enrichment_type: Enrichment type
    :param str ip_address: The dotted-decimal or colon-separated string representation of the IP address
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['enrichmentType'] = enrichment_type
    __args__['ipAddress'] = ip_address
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights:listGeodataByIp', __args__, opts=opts, typ=ListGeodataByIpResult).value

    return AwaitableListGeodataByIpResult(
        asn=pulumi.get(__ret__, 'asn'),
        carrier=pulumi.get(__ret__, 'carrier'),
        city=pulumi.get(__ret__, 'city'),
        city_confidence_factor=pulumi.get(__ret__, 'city_confidence_factor'),
        continent=pulumi.get(__ret__, 'continent'),
        country=pulumi.get(__ret__, 'country'),
        country_confidence_factor=pulumi.get(__ret__, 'country_confidence_factor'),
        ip_addr=pulumi.get(__ret__, 'ip_addr'),
        ip_routing_type=pulumi.get(__ret__, 'ip_routing_type'),
        latitude=pulumi.get(__ret__, 'latitude'),
        longitude=pulumi.get(__ret__, 'longitude'),
        organization=pulumi.get(__ret__, 'organization'),
        organization_type=pulumi.get(__ret__, 'organization_type'),
        region=pulumi.get(__ret__, 'region'),
        state=pulumi.get(__ret__, 'state'),
        state_code=pulumi.get(__ret__, 'state_code'),
        state_confidence_factor=pulumi.get(__ret__, 'state_confidence_factor'))


@_utilities.lift_output_func(list_geodata_by_ip)
def list_geodata_by_ip_output(enrichment_type: Optional[pulumi.Input[str]] = None,
                              ip_address: Optional[pulumi.Input[Optional[str]]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              workspace_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListGeodataByIpResult]:
    """
    Get geodata for a single IP address
    Azure REST API version: 2024-01-01-preview.


    :param str enrichment_type: Enrichment type
    :param str ip_address: The dotted-decimal or colon-separated string representation of the IP address
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    ...
