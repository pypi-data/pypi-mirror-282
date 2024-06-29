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
from ._enums import *
from ._inputs import *

__all__ = ['GroundStationArgs', 'GroundStation']

@pulumi.input_type
class GroundStationArgs:
    def __init__(__self__, *,
                 capabilities: pulumi.Input[Sequence[pulumi.Input[Union[str, 'Capability']]]],
                 global_communications_site: pulumi.Input['GroundStationsPropertiesGlobalCommunicationsSiteArgs'],
                 resource_group_name: pulumi.Input[str],
                 altitude_meters: Optional[pulumi.Input[float]] = None,
                 city: Optional[pulumi.Input[str]] = None,
                 ground_station_name: Optional[pulumi.Input[str]] = None,
                 latitude_degrees: Optional[pulumi.Input[float]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 longitude_degrees: Optional[pulumi.Input[float]] = None,
                 provider_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a GroundStation resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'Capability']]]] capabilities: Ground station capabilities.
        :param pulumi.Input['GroundStationsPropertiesGlobalCommunicationsSiteArgs'] global_communications_site: A reference to global communications site.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[float] altitude_meters: Altitude of the ground station.
        :param pulumi.Input[str] city: City of ground station.
        :param pulumi.Input[str] ground_station_name: Ground Station name.
        :param pulumi.Input[float] latitude_degrees: Latitude of the ground station in decimal degrees.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[float] longitude_degrees: Longitude of the ground station in decimal degrees.
        :param pulumi.Input[str] provider_name: Ground station provider name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "capabilities", capabilities)
        pulumi.set(__self__, "global_communications_site", global_communications_site)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if altitude_meters is not None:
            pulumi.set(__self__, "altitude_meters", altitude_meters)
        if city is not None:
            pulumi.set(__self__, "city", city)
        if ground_station_name is not None:
            pulumi.set(__self__, "ground_station_name", ground_station_name)
        if latitude_degrees is not None:
            pulumi.set(__self__, "latitude_degrees", latitude_degrees)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if longitude_degrees is not None:
            pulumi.set(__self__, "longitude_degrees", longitude_degrees)
        if provider_name is not None:
            pulumi.set(__self__, "provider_name", provider_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def capabilities(self) -> pulumi.Input[Sequence[pulumi.Input[Union[str, 'Capability']]]]:
        """
        Ground station capabilities.
        """
        return pulumi.get(self, "capabilities")

    @capabilities.setter
    def capabilities(self, value: pulumi.Input[Sequence[pulumi.Input[Union[str, 'Capability']]]]):
        pulumi.set(self, "capabilities", value)

    @property
    @pulumi.getter(name="globalCommunicationsSite")
    def global_communications_site(self) -> pulumi.Input['GroundStationsPropertiesGlobalCommunicationsSiteArgs']:
        """
        A reference to global communications site.
        """
        return pulumi.get(self, "global_communications_site")

    @global_communications_site.setter
    def global_communications_site(self, value: pulumi.Input['GroundStationsPropertiesGlobalCommunicationsSiteArgs']):
        pulumi.set(self, "global_communications_site", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="altitudeMeters")
    def altitude_meters(self) -> Optional[pulumi.Input[float]]:
        """
        Altitude of the ground station.
        """
        return pulumi.get(self, "altitude_meters")

    @altitude_meters.setter
    def altitude_meters(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "altitude_meters", value)

    @property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[str]]:
        """
        City of ground station.
        """
        return pulumi.get(self, "city")

    @city.setter
    def city(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "city", value)

    @property
    @pulumi.getter(name="groundStationName")
    def ground_station_name(self) -> Optional[pulumi.Input[str]]:
        """
        Ground Station name.
        """
        return pulumi.get(self, "ground_station_name")

    @ground_station_name.setter
    def ground_station_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ground_station_name", value)

    @property
    @pulumi.getter(name="latitudeDegrees")
    def latitude_degrees(self) -> Optional[pulumi.Input[float]]:
        """
        Latitude of the ground station in decimal degrees.
        """
        return pulumi.get(self, "latitude_degrees")

    @latitude_degrees.setter
    def latitude_degrees(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "latitude_degrees", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="longitudeDegrees")
    def longitude_degrees(self) -> Optional[pulumi.Input[float]]:
        """
        Longitude of the ground station in decimal degrees.
        """
        return pulumi.get(self, "longitude_degrees")

    @longitude_degrees.setter
    def longitude_degrees(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "longitude_degrees", value)

    @property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> Optional[pulumi.Input[str]]:
        """
        Ground station provider name.
        """
        return pulumi.get(self, "provider_name")

    @provider_name.setter
    def provider_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provider_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class GroundStation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 altitude_meters: Optional[pulumi.Input[float]] = None,
                 capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Capability']]]]] = None,
                 city: Optional[pulumi.Input[str]] = None,
                 global_communications_site: Optional[pulumi.Input[pulumi.InputType['GroundStationsPropertiesGlobalCommunicationsSiteArgs']]] = None,
                 ground_station_name: Optional[pulumi.Input[str]] = None,
                 latitude_degrees: Optional[pulumi.Input[float]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 longitude_degrees: Optional[pulumi.Input[float]] = None,
                 provider_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Ground Station contains one or more antennas.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] altitude_meters: Altitude of the ground station.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'Capability']]]] capabilities: Ground station capabilities.
        :param pulumi.Input[str] city: City of ground station.
        :param pulumi.Input[pulumi.InputType['GroundStationsPropertiesGlobalCommunicationsSiteArgs']] global_communications_site: A reference to global communications site.
        :param pulumi.Input[str] ground_station_name: Ground Station name.
        :param pulumi.Input[float] latitude_degrees: Latitude of the ground station in decimal degrees.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[float] longitude_degrees: Longitude of the ground station in decimal degrees.
        :param pulumi.Input[str] provider_name: Ground station provider name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GroundStationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Ground Station contains one or more antennas.

        :param str resource_name: The name of the resource.
        :param GroundStationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GroundStationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 altitude_meters: Optional[pulumi.Input[float]] = None,
                 capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Capability']]]]] = None,
                 city: Optional[pulumi.Input[str]] = None,
                 global_communications_site: Optional[pulumi.Input[pulumi.InputType['GroundStationsPropertiesGlobalCommunicationsSiteArgs']]] = None,
                 ground_station_name: Optional[pulumi.Input[str]] = None,
                 latitude_degrees: Optional[pulumi.Input[float]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 longitude_degrees: Optional[pulumi.Input[float]] = None,
                 provider_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GroundStationArgs.__new__(GroundStationArgs)

            __props__.__dict__["altitude_meters"] = altitude_meters
            if capabilities is None and not opts.urn:
                raise TypeError("Missing required property 'capabilities'")
            __props__.__dict__["capabilities"] = capabilities
            __props__.__dict__["city"] = city
            if global_communications_site is None and not opts.urn:
                raise TypeError("Missing required property 'global_communications_site'")
            __props__.__dict__["global_communications_site"] = global_communications_site
            __props__.__dict__["ground_station_name"] = ground_station_name
            __props__.__dict__["latitude_degrees"] = latitude_degrees
            __props__.__dict__["location"] = location
            __props__.__dict__["longitude_degrees"] = longitude_degrees
            __props__.__dict__["provider_name"] = provider_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["release_mode"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:orbital:GroundStation"), pulumi.Alias(type_="azure-native:orbital/v20240301:GroundStation")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(GroundStation, __self__).__init__(
            'azure-native:orbital/v20240301preview:GroundStation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GroundStation':
        """
        Get an existing GroundStation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GroundStationArgs.__new__(GroundStationArgs)

        __props__.__dict__["altitude_meters"] = None
        __props__.__dict__["capabilities"] = None
        __props__.__dict__["city"] = None
        __props__.__dict__["global_communications_site"] = None
        __props__.__dict__["latitude_degrees"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["longitude_degrees"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provider_name"] = None
        __props__.__dict__["release_mode"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return GroundStation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="altitudeMeters")
    def altitude_meters(self) -> pulumi.Output[Optional[float]]:
        """
        Altitude of the ground station.
        """
        return pulumi.get(self, "altitude_meters")

    @property
    @pulumi.getter
    def capabilities(self) -> pulumi.Output[Sequence[str]]:
        """
        Ground station capabilities.
        """
        return pulumi.get(self, "capabilities")

    @property
    @pulumi.getter
    def city(self) -> pulumi.Output[Optional[str]]:
        """
        City of ground station.
        """
        return pulumi.get(self, "city")

    @property
    @pulumi.getter(name="globalCommunicationsSite")
    def global_communications_site(self) -> pulumi.Output['outputs.GroundStationsPropertiesResponseGlobalCommunicationsSite']:
        """
        A reference to global communications site.
        """
        return pulumi.get(self, "global_communications_site")

    @property
    @pulumi.getter(name="latitudeDegrees")
    def latitude_degrees(self) -> pulumi.Output[Optional[float]]:
        """
        Latitude of the ground station in decimal degrees.
        """
        return pulumi.get(self, "latitude_degrees")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="longitudeDegrees")
    def longitude_degrees(self) -> pulumi.Output[Optional[float]]:
        """
        Longitude of the ground station in decimal degrees.
        """
        return pulumi.get(self, "longitude_degrees")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> pulumi.Output[Optional[str]]:
        """
        Ground station provider name.
        """
        return pulumi.get(self, "provider_name")

    @property
    @pulumi.getter(name="releaseMode")
    def release_mode(self) -> pulumi.Output[str]:
        """
        Release Status of a ground station.
        """
        return pulumi.get(self, "release_mode")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

