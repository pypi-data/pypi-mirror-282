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
    'GetEndpointResult',
    'AwaitableGetEndpointResult',
    'get_endpoint',
    'get_endpoint_output',
]

@pulumi.output_type
class GetEndpointResult:
    """
    Class representing a Traffic Manager endpoint.
    """
    def __init__(__self__, always_serve=None, custom_headers=None, endpoint_location=None, endpoint_monitor_status=None, endpoint_status=None, geo_mapping=None, id=None, min_child_endpoints=None, min_child_endpoints_i_pv4=None, min_child_endpoints_i_pv6=None, name=None, priority=None, subnets=None, target=None, target_resource_id=None, type=None, weight=None):
        if always_serve and not isinstance(always_serve, str):
            raise TypeError("Expected argument 'always_serve' to be a str")
        pulumi.set(__self__, "always_serve", always_serve)
        if custom_headers and not isinstance(custom_headers, list):
            raise TypeError("Expected argument 'custom_headers' to be a list")
        pulumi.set(__self__, "custom_headers", custom_headers)
        if endpoint_location and not isinstance(endpoint_location, str):
            raise TypeError("Expected argument 'endpoint_location' to be a str")
        pulumi.set(__self__, "endpoint_location", endpoint_location)
        if endpoint_monitor_status and not isinstance(endpoint_monitor_status, str):
            raise TypeError("Expected argument 'endpoint_monitor_status' to be a str")
        pulumi.set(__self__, "endpoint_monitor_status", endpoint_monitor_status)
        if endpoint_status and not isinstance(endpoint_status, str):
            raise TypeError("Expected argument 'endpoint_status' to be a str")
        pulumi.set(__self__, "endpoint_status", endpoint_status)
        if geo_mapping and not isinstance(geo_mapping, list):
            raise TypeError("Expected argument 'geo_mapping' to be a list")
        pulumi.set(__self__, "geo_mapping", geo_mapping)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if min_child_endpoints and not isinstance(min_child_endpoints, float):
            raise TypeError("Expected argument 'min_child_endpoints' to be a float")
        pulumi.set(__self__, "min_child_endpoints", min_child_endpoints)
        if min_child_endpoints_i_pv4 and not isinstance(min_child_endpoints_i_pv4, float):
            raise TypeError("Expected argument 'min_child_endpoints_i_pv4' to be a float")
        pulumi.set(__self__, "min_child_endpoints_i_pv4", min_child_endpoints_i_pv4)
        if min_child_endpoints_i_pv6 and not isinstance(min_child_endpoints_i_pv6, float):
            raise TypeError("Expected argument 'min_child_endpoints_i_pv6' to be a float")
        pulumi.set(__self__, "min_child_endpoints_i_pv6", min_child_endpoints_i_pv6)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if priority and not isinstance(priority, float):
            raise TypeError("Expected argument 'priority' to be a float")
        pulumi.set(__self__, "priority", priority)
        if subnets and not isinstance(subnets, list):
            raise TypeError("Expected argument 'subnets' to be a list")
        pulumi.set(__self__, "subnets", subnets)
        if target and not isinstance(target, str):
            raise TypeError("Expected argument 'target' to be a str")
        pulumi.set(__self__, "target", target)
        if target_resource_id and not isinstance(target_resource_id, str):
            raise TypeError("Expected argument 'target_resource_id' to be a str")
        pulumi.set(__self__, "target_resource_id", target_resource_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if weight and not isinstance(weight, float):
            raise TypeError("Expected argument 'weight' to be a float")
        pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter(name="alwaysServe")
    def always_serve(self) -> Optional[str]:
        """
        If Always Serve is enabled, probing for endpoint health will be disabled and endpoints will be included in the traffic routing method.
        """
        return pulumi.get(self, "always_serve")

    @property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> Optional[Sequence['outputs.EndpointPropertiesResponseCustomHeaders']]:
        """
        List of custom headers.
        """
        return pulumi.get(self, "custom_headers")

    @property
    @pulumi.getter(name="endpointLocation")
    def endpoint_location(self) -> Optional[str]:
        """
        Specifies the location of the external or nested endpoints when using the 'Performance' traffic routing method.
        """
        return pulumi.get(self, "endpoint_location")

    @property
    @pulumi.getter(name="endpointMonitorStatus")
    def endpoint_monitor_status(self) -> Optional[str]:
        """
        The monitoring status of the endpoint.
        """
        return pulumi.get(self, "endpoint_monitor_status")

    @property
    @pulumi.getter(name="endpointStatus")
    def endpoint_status(self) -> Optional[str]:
        """
        The status of the endpoint. If the endpoint is Enabled, it is probed for endpoint health and is included in the traffic routing method.
        """
        return pulumi.get(self, "endpoint_status")

    @property
    @pulumi.getter(name="geoMapping")
    def geo_mapping(self) -> Optional[Sequence[str]]:
        """
        The list of countries/regions mapped to this endpoint when using the 'Geographic' traffic routing method. Please consult Traffic Manager Geographic documentation for a full list of accepted values.
        """
        return pulumi.get(self, "geo_mapping")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficManagerProfiles/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="minChildEndpoints")
    def min_child_endpoints(self) -> Optional[float]:
        """
        The minimum number of endpoints that must be available in the child profile in order for the parent profile to be considered available. Only applicable to endpoint of type 'NestedEndpoints'.
        """
        return pulumi.get(self, "min_child_endpoints")

    @property
    @pulumi.getter(name="minChildEndpointsIPv4")
    def min_child_endpoints_i_pv4(self) -> Optional[float]:
        """
        The minimum number of IPv4 (DNS record type A) endpoints that must be available in the child profile in order for the parent profile to be considered available. Only applicable to endpoint of type 'NestedEndpoints'.
        """
        return pulumi.get(self, "min_child_endpoints_i_pv4")

    @property
    @pulumi.getter(name="minChildEndpointsIPv6")
    def min_child_endpoints_i_pv6(self) -> Optional[float]:
        """
        The minimum number of IPv6 (DNS record type AAAA) endpoints that must be available in the child profile in order for the parent profile to be considered available. Only applicable to endpoint of type 'NestedEndpoints'.
        """
        return pulumi.get(self, "min_child_endpoints_i_pv6")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> Optional[float]:
        """
        The priority of this endpoint when using the 'Priority' traffic routing method. Possible values are from 1 to 1000, lower values represent higher priority. This is an optional parameter.  If specified, it must be specified on all endpoints, and no two endpoints can share the same priority value.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def subnets(self) -> Optional[Sequence['outputs.EndpointPropertiesResponseSubnets']]:
        """
        The list of subnets, IP addresses, and/or address ranges mapped to this endpoint when using the 'Subnet' traffic routing method. An empty list will match all ranges not covered by other endpoints.
        """
        return pulumi.get(self, "subnets")

    @property
    @pulumi.getter
    def target(self) -> Optional[str]:
        """
        The fully-qualified DNS name or IP address of the endpoint. Traffic Manager returns this value in DNS responses to direct traffic to this endpoint.
        """
        return pulumi.get(self, "target")

    @property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> Optional[str]:
        """
        The Azure Resource URI of the of the endpoint. Not applicable to endpoints of type 'ExternalEndpoints'.
        """
        return pulumi.get(self, "target_resource_id")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type of the resource. Ex- Microsoft.Network/trafficManagerProfiles.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def weight(self) -> Optional[float]:
        """
        The weight of this endpoint when using the 'Weighted' traffic routing method. Possible values are from 1 to 1000.
        """
        return pulumi.get(self, "weight")


class AwaitableGetEndpointResult(GetEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEndpointResult(
            always_serve=self.always_serve,
            custom_headers=self.custom_headers,
            endpoint_location=self.endpoint_location,
            endpoint_monitor_status=self.endpoint_monitor_status,
            endpoint_status=self.endpoint_status,
            geo_mapping=self.geo_mapping,
            id=self.id,
            min_child_endpoints=self.min_child_endpoints,
            min_child_endpoints_i_pv4=self.min_child_endpoints_i_pv4,
            min_child_endpoints_i_pv6=self.min_child_endpoints_i_pv6,
            name=self.name,
            priority=self.priority,
            subnets=self.subnets,
            target=self.target,
            target_resource_id=self.target_resource_id,
            type=self.type,
            weight=self.weight)


def get_endpoint(endpoint_name: Optional[str] = None,
                 endpoint_type: Optional[str] = None,
                 profile_name: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEndpointResult:
    """
    Gets a Traffic Manager endpoint.
    Azure REST API version: 2022-04-01.

    Other available API versions: 2017-03-01, 2018-02-01, 2022-04-01-preview.


    :param str endpoint_name: The name of the Traffic Manager endpoint.
    :param str endpoint_type: The type of the Traffic Manager endpoint.
    :param str profile_name: The name of the Traffic Manager profile.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['endpointName'] = endpoint_name
    __args__['endpointType'] = endpoint_type
    __args__['profileName'] = profile_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network:getEndpoint', __args__, opts=opts, typ=GetEndpointResult).value

    return AwaitableGetEndpointResult(
        always_serve=pulumi.get(__ret__, 'always_serve'),
        custom_headers=pulumi.get(__ret__, 'custom_headers'),
        endpoint_location=pulumi.get(__ret__, 'endpoint_location'),
        endpoint_monitor_status=pulumi.get(__ret__, 'endpoint_monitor_status'),
        endpoint_status=pulumi.get(__ret__, 'endpoint_status'),
        geo_mapping=pulumi.get(__ret__, 'geo_mapping'),
        id=pulumi.get(__ret__, 'id'),
        min_child_endpoints=pulumi.get(__ret__, 'min_child_endpoints'),
        min_child_endpoints_i_pv4=pulumi.get(__ret__, 'min_child_endpoints_i_pv4'),
        min_child_endpoints_i_pv6=pulumi.get(__ret__, 'min_child_endpoints_i_pv6'),
        name=pulumi.get(__ret__, 'name'),
        priority=pulumi.get(__ret__, 'priority'),
        subnets=pulumi.get(__ret__, 'subnets'),
        target=pulumi.get(__ret__, 'target'),
        target_resource_id=pulumi.get(__ret__, 'target_resource_id'),
        type=pulumi.get(__ret__, 'type'),
        weight=pulumi.get(__ret__, 'weight'))


@_utilities.lift_output_func(get_endpoint)
def get_endpoint_output(endpoint_name: Optional[pulumi.Input[str]] = None,
                        endpoint_type: Optional[pulumi.Input[str]] = None,
                        profile_name: Optional[pulumi.Input[str]] = None,
                        resource_group_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEndpointResult]:
    """
    Gets a Traffic Manager endpoint.
    Azure REST API version: 2022-04-01.

    Other available API versions: 2017-03-01, 2018-02-01, 2022-04-01-preview.


    :param str endpoint_name: The name of the Traffic Manager endpoint.
    :param str endpoint_type: The type of the Traffic Manager endpoint.
    :param str profile_name: The name of the Traffic Manager profile.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
