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
from ._inputs import *

__all__ = ['ContactArgs', 'Contact']

@pulumi.input_type
class ContactArgs:
    def __init__(__self__, *,
                 contact_profile: pulumi.Input['ContactsPropertiesContactProfileArgs'],
                 ground_station_name: pulumi.Input[str],
                 reservation_end_time: pulumi.Input[str],
                 reservation_start_time: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 spacecraft_name: pulumi.Input[str],
                 contact_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Contact resource.
        :param pulumi.Input['ContactsPropertiesContactProfileArgs'] contact_profile: The reference to the contact profile resource.
        :param pulumi.Input[str] ground_station_name: Azure Ground Station name.
        :param pulumi.Input[str] reservation_end_time: Reservation end time of a contact (ISO 8601 UTC standard).
        :param pulumi.Input[str] reservation_start_time: Reservation start time of a contact (ISO 8601 UTC standard).
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] spacecraft_name: Spacecraft ID.
        :param pulumi.Input[str] contact_name: Contact name.
        """
        pulumi.set(__self__, "contact_profile", contact_profile)
        pulumi.set(__self__, "ground_station_name", ground_station_name)
        pulumi.set(__self__, "reservation_end_time", reservation_end_time)
        pulumi.set(__self__, "reservation_start_time", reservation_start_time)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "spacecraft_name", spacecraft_name)
        if contact_name is not None:
            pulumi.set(__self__, "contact_name", contact_name)

    @property
    @pulumi.getter(name="contactProfile")
    def contact_profile(self) -> pulumi.Input['ContactsPropertiesContactProfileArgs']:
        """
        The reference to the contact profile resource.
        """
        return pulumi.get(self, "contact_profile")

    @contact_profile.setter
    def contact_profile(self, value: pulumi.Input['ContactsPropertiesContactProfileArgs']):
        pulumi.set(self, "contact_profile", value)

    @property
    @pulumi.getter(name="groundStationName")
    def ground_station_name(self) -> pulumi.Input[str]:
        """
        Azure Ground Station name.
        """
        return pulumi.get(self, "ground_station_name")

    @ground_station_name.setter
    def ground_station_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "ground_station_name", value)

    @property
    @pulumi.getter(name="reservationEndTime")
    def reservation_end_time(self) -> pulumi.Input[str]:
        """
        Reservation end time of a contact (ISO 8601 UTC standard).
        """
        return pulumi.get(self, "reservation_end_time")

    @reservation_end_time.setter
    def reservation_end_time(self, value: pulumi.Input[str]):
        pulumi.set(self, "reservation_end_time", value)

    @property
    @pulumi.getter(name="reservationStartTime")
    def reservation_start_time(self) -> pulumi.Input[str]:
        """
        Reservation start time of a contact (ISO 8601 UTC standard).
        """
        return pulumi.get(self, "reservation_start_time")

    @reservation_start_time.setter
    def reservation_start_time(self, value: pulumi.Input[str]):
        pulumi.set(self, "reservation_start_time", value)

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
    @pulumi.getter(name="spacecraftName")
    def spacecraft_name(self) -> pulumi.Input[str]:
        """
        Spacecraft ID.
        """
        return pulumi.get(self, "spacecraft_name")

    @spacecraft_name.setter
    def spacecraft_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "spacecraft_name", value)

    @property
    @pulumi.getter(name="contactName")
    def contact_name(self) -> Optional[pulumi.Input[str]]:
        """
        Contact name.
        """
        return pulumi.get(self, "contact_name")

    @contact_name.setter
    def contact_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "contact_name", value)


class Contact(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 contact_name: Optional[pulumi.Input[str]] = None,
                 contact_profile: Optional[pulumi.Input[pulumi.InputType['ContactsPropertiesContactProfileArgs']]] = None,
                 ground_station_name: Optional[pulumi.Input[str]] = None,
                 reservation_end_time: Optional[pulumi.Input[str]] = None,
                 reservation_start_time: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 spacecraft_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Customer creates a contact resource for a spacecraft resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] contact_name: Contact name.
        :param pulumi.Input[pulumi.InputType['ContactsPropertiesContactProfileArgs']] contact_profile: The reference to the contact profile resource.
        :param pulumi.Input[str] ground_station_name: Azure Ground Station name.
        :param pulumi.Input[str] reservation_end_time: Reservation end time of a contact (ISO 8601 UTC standard).
        :param pulumi.Input[str] reservation_start_time: Reservation start time of a contact (ISO 8601 UTC standard).
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] spacecraft_name: Spacecraft ID.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ContactArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Customer creates a contact resource for a spacecraft resource.

        :param str resource_name: The name of the resource.
        :param ContactArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ContactArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 contact_name: Optional[pulumi.Input[str]] = None,
                 contact_profile: Optional[pulumi.Input[pulumi.InputType['ContactsPropertiesContactProfileArgs']]] = None,
                 ground_station_name: Optional[pulumi.Input[str]] = None,
                 reservation_end_time: Optional[pulumi.Input[str]] = None,
                 reservation_start_time: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 spacecraft_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ContactArgs.__new__(ContactArgs)

            __props__.__dict__["contact_name"] = contact_name
            if contact_profile is None and not opts.urn:
                raise TypeError("Missing required property 'contact_profile'")
            __props__.__dict__["contact_profile"] = contact_profile
            if ground_station_name is None and not opts.urn:
                raise TypeError("Missing required property 'ground_station_name'")
            __props__.__dict__["ground_station_name"] = ground_station_name
            if reservation_end_time is None and not opts.urn:
                raise TypeError("Missing required property 'reservation_end_time'")
            __props__.__dict__["reservation_end_time"] = reservation_end_time
            if reservation_start_time is None and not opts.urn:
                raise TypeError("Missing required property 'reservation_start_time'")
            __props__.__dict__["reservation_start_time"] = reservation_start_time
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if spacecraft_name is None and not opts.urn:
                raise TypeError("Missing required property 'spacecraft_name'")
            __props__.__dict__["spacecraft_name"] = spacecraft_name
            __props__.__dict__["antenna_configuration"] = None
            __props__.__dict__["end_azimuth_degrees"] = None
            __props__.__dict__["end_elevation_degrees"] = None
            __props__.__dict__["error_message"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["maximum_elevation_degrees"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["rx_end_time"] = None
            __props__.__dict__["rx_start_time"] = None
            __props__.__dict__["start_azimuth_degrees"] = None
            __props__.__dict__["start_elevation_degrees"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["tx_end_time"] = None
            __props__.__dict__["tx_start_time"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:orbital:Contact"), pulumi.Alias(type_="azure-native:orbital/v20221101:Contact")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Contact, __self__).__init__(
            'azure-native:orbital/v20220301:Contact',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Contact':
        """
        Get an existing Contact resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ContactArgs.__new__(ContactArgs)

        __props__.__dict__["antenna_configuration"] = None
        __props__.__dict__["contact_profile"] = None
        __props__.__dict__["end_azimuth_degrees"] = None
        __props__.__dict__["end_elevation_degrees"] = None
        __props__.__dict__["error_message"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["ground_station_name"] = None
        __props__.__dict__["maximum_elevation_degrees"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["reservation_end_time"] = None
        __props__.__dict__["reservation_start_time"] = None
        __props__.__dict__["rx_end_time"] = None
        __props__.__dict__["rx_start_time"] = None
        __props__.__dict__["start_azimuth_degrees"] = None
        __props__.__dict__["start_elevation_degrees"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tx_end_time"] = None
        __props__.__dict__["tx_start_time"] = None
        __props__.__dict__["type"] = None
        return Contact(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="antennaConfiguration")
    def antenna_configuration(self) -> pulumi.Output['outputs.ContactsPropertiesResponseAntennaConfiguration']:
        """
        The configuration associated with the allocated antenna.
        """
        return pulumi.get(self, "antenna_configuration")

    @property
    @pulumi.getter(name="contactProfile")
    def contact_profile(self) -> pulumi.Output['outputs.ContactsPropertiesResponseContactProfile']:
        """
        The reference to the contact profile resource.
        """
        return pulumi.get(self, "contact_profile")

    @property
    @pulumi.getter(name="endAzimuthDegrees")
    def end_azimuth_degrees(self) -> pulumi.Output[float]:
        """
        Azimuth of the antenna at the end of the contact in decimal degrees.
        """
        return pulumi.get(self, "end_azimuth_degrees")

    @property
    @pulumi.getter(name="endElevationDegrees")
    def end_elevation_degrees(self) -> pulumi.Output[float]:
        """
        Spacecraft elevation above the horizon at contact end.
        """
        return pulumi.get(self, "end_elevation_degrees")

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> pulumi.Output[str]:
        """
        Any error message while scheduling a contact.
        """
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="groundStationName")
    def ground_station_name(self) -> pulumi.Output[str]:
        """
        Azure Ground Station name.
        """
        return pulumi.get(self, "ground_station_name")

    @property
    @pulumi.getter(name="maximumElevationDegrees")
    def maximum_elevation_degrees(self) -> pulumi.Output[float]:
        """
        Maximum elevation of the antenna during the contact in decimal degrees.
        """
        return pulumi.get(self, "maximum_elevation_degrees")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="reservationEndTime")
    def reservation_end_time(self) -> pulumi.Output[str]:
        """
        Reservation end time of a contact (ISO 8601 UTC standard).
        """
        return pulumi.get(self, "reservation_end_time")

    @property
    @pulumi.getter(name="reservationStartTime")
    def reservation_start_time(self) -> pulumi.Output[str]:
        """
        Reservation start time of a contact (ISO 8601 UTC standard).
        """
        return pulumi.get(self, "reservation_start_time")

    @property
    @pulumi.getter(name="rxEndTime")
    def rx_end_time(self) -> pulumi.Output[str]:
        """
        Receive end time of a contact (ISO 8601 UTC standard).
        """
        return pulumi.get(self, "rx_end_time")

    @property
    @pulumi.getter(name="rxStartTime")
    def rx_start_time(self) -> pulumi.Output[str]:
        """
        Receive start time of a contact (ISO 8601 UTC standard).
        """
        return pulumi.get(self, "rx_start_time")

    @property
    @pulumi.getter(name="startAzimuthDegrees")
    def start_azimuth_degrees(self) -> pulumi.Output[float]:
        """
        Azimuth of the antenna at the start of the contact in decimal degrees.
        """
        return pulumi.get(self, "start_azimuth_degrees")

    @property
    @pulumi.getter(name="startElevationDegrees")
    def start_elevation_degrees(self) -> pulumi.Output[float]:
        """
        Spacecraft elevation above the horizon at contact start.
        """
        return pulumi.get(self, "start_elevation_degrees")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Status of a contact.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="txEndTime")
    def tx_end_time(self) -> pulumi.Output[str]:
        """
        Transmit end time of a contact (ISO 8601 UTC standard).
        """
        return pulumi.get(self, "tx_end_time")

    @property
    @pulumi.getter(name="txStartTime")
    def tx_start_time(self) -> pulumi.Output[str]:
        """
        Transmit start time of a contact (ISO 8601 UTC standard).
        """
        return pulumi.get(self, "tx_start_time")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

