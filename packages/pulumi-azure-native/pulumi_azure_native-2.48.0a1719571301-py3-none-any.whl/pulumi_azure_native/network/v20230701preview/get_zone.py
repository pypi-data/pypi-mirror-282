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
    'GetZoneResult',
    'AwaitableGetZoneResult',
    'get_zone',
    'get_zone_output',
]

@pulumi.output_type
class GetZoneResult:
    """
    Describes a DNS zone.
    """
    def __init__(__self__, etag=None, id=None, location=None, max_number_of_record_sets=None, max_number_of_records_per_record_set=None, name=None, name_servers=None, number_of_record_sets=None, registration_virtual_networks=None, resolution_virtual_networks=None, signing_keys=None, system_data=None, tags=None, type=None, zone_type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if max_number_of_record_sets and not isinstance(max_number_of_record_sets, float):
            raise TypeError("Expected argument 'max_number_of_record_sets' to be a float")
        pulumi.set(__self__, "max_number_of_record_sets", max_number_of_record_sets)
        if max_number_of_records_per_record_set and not isinstance(max_number_of_records_per_record_set, float):
            raise TypeError("Expected argument 'max_number_of_records_per_record_set' to be a float")
        pulumi.set(__self__, "max_number_of_records_per_record_set", max_number_of_records_per_record_set)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if name_servers and not isinstance(name_servers, list):
            raise TypeError("Expected argument 'name_servers' to be a list")
        pulumi.set(__self__, "name_servers", name_servers)
        if number_of_record_sets and not isinstance(number_of_record_sets, float):
            raise TypeError("Expected argument 'number_of_record_sets' to be a float")
        pulumi.set(__self__, "number_of_record_sets", number_of_record_sets)
        if registration_virtual_networks and not isinstance(registration_virtual_networks, list):
            raise TypeError("Expected argument 'registration_virtual_networks' to be a list")
        pulumi.set(__self__, "registration_virtual_networks", registration_virtual_networks)
        if resolution_virtual_networks and not isinstance(resolution_virtual_networks, list):
            raise TypeError("Expected argument 'resolution_virtual_networks' to be a list")
        pulumi.set(__self__, "resolution_virtual_networks", resolution_virtual_networks)
        if signing_keys and not isinstance(signing_keys, list):
            raise TypeError("Expected argument 'signing_keys' to be a list")
        pulumi.set(__self__, "signing_keys", signing_keys)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if zone_type and not isinstance(zone_type, str):
            raise TypeError("Expected argument 'zone_type' to be a str")
        pulumi.set(__self__, "zone_type", zone_type)

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        The etag of the zone.
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
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maxNumberOfRecordSets")
    def max_number_of_record_sets(self) -> float:
        """
        The maximum number of record sets that can be created in this DNS zone.  This is a read-only property and any attempt to set this value will be ignored.
        """
        return pulumi.get(self, "max_number_of_record_sets")

    @property
    @pulumi.getter(name="maxNumberOfRecordsPerRecordSet")
    def max_number_of_records_per_record_set(self) -> float:
        """
        The maximum number of records per record set that can be created in this DNS zone.  This is a read-only property and any attempt to set this value will be ignored.
        """
        return pulumi.get(self, "max_number_of_records_per_record_set")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nameServers")
    def name_servers(self) -> Sequence[str]:
        """
        The name servers for this DNS zone. This is a read-only property and any attempt to set this value will be ignored.
        """
        return pulumi.get(self, "name_servers")

    @property
    @pulumi.getter(name="numberOfRecordSets")
    def number_of_record_sets(self) -> float:
        """
        The current number of record sets in this DNS zone.  This is a read-only property and any attempt to set this value will be ignored.
        """
        return pulumi.get(self, "number_of_record_sets")

    @property
    @pulumi.getter(name="registrationVirtualNetworks")
    def registration_virtual_networks(self) -> Optional[Sequence['outputs.SubResourceResponse']]:
        """
        A list of references to virtual networks that register hostnames in this DNS zone. This is a only when ZoneType is Private.
        """
        return pulumi.get(self, "registration_virtual_networks")

    @property
    @pulumi.getter(name="resolutionVirtualNetworks")
    def resolution_virtual_networks(self) -> Optional[Sequence['outputs.SubResourceResponse']]:
        """
        A list of references to virtual networks that resolve records in this DNS zone. This is a only when ZoneType is Private.
        """
        return pulumi.get(self, "resolution_virtual_networks")

    @property
    @pulumi.getter(name="signingKeys")
    def signing_keys(self) -> Sequence['outputs.SigningKeyResponse']:
        """
        The list of signing keys.
        """
        return pulumi.get(self, "signing_keys")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

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
    @pulumi.getter(name="zoneType")
    def zone_type(self) -> Optional[str]:
        """
        The type of this DNS zone (Public or Private).
        """
        return pulumi.get(self, "zone_type")


class AwaitableGetZoneResult(GetZoneResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetZoneResult(
            etag=self.etag,
            id=self.id,
            location=self.location,
            max_number_of_record_sets=self.max_number_of_record_sets,
            max_number_of_records_per_record_set=self.max_number_of_records_per_record_set,
            name=self.name,
            name_servers=self.name_servers,
            number_of_record_sets=self.number_of_record_sets,
            registration_virtual_networks=self.registration_virtual_networks,
            resolution_virtual_networks=self.resolution_virtual_networks,
            signing_keys=self.signing_keys,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            zone_type=self.zone_type)


def get_zone(resource_group_name: Optional[str] = None,
             zone_name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetZoneResult:
    """
    Gets a DNS zone. Retrieves the zone properties, but not the record sets within the zone.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str zone_name: The name of the DNS zone (without a terminating dot).
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['zoneName'] = zone_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20230701preview:getZone', __args__, opts=opts, typ=GetZoneResult).value

    return AwaitableGetZoneResult(
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        max_number_of_record_sets=pulumi.get(__ret__, 'max_number_of_record_sets'),
        max_number_of_records_per_record_set=pulumi.get(__ret__, 'max_number_of_records_per_record_set'),
        name=pulumi.get(__ret__, 'name'),
        name_servers=pulumi.get(__ret__, 'name_servers'),
        number_of_record_sets=pulumi.get(__ret__, 'number_of_record_sets'),
        registration_virtual_networks=pulumi.get(__ret__, 'registration_virtual_networks'),
        resolution_virtual_networks=pulumi.get(__ret__, 'resolution_virtual_networks'),
        signing_keys=pulumi.get(__ret__, 'signing_keys'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        zone_type=pulumi.get(__ret__, 'zone_type'))


@_utilities.lift_output_func(get_zone)
def get_zone_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                    zone_name: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetZoneResult]:
    """
    Gets a DNS zone. Retrieves the zone properties, but not the record sets within the zone.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str zone_name: The name of the DNS zone (without a terminating dot).
    """
    ...
