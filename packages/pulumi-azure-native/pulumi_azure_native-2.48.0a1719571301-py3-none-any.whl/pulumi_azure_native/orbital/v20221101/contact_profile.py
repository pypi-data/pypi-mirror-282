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

__all__ = ['ContactProfileArgs', 'ContactProfile']

@pulumi.input_type
class ContactProfileArgs:
    def __init__(__self__, *,
                 links: pulumi.Input[Sequence[pulumi.Input['ContactProfileLinkArgs']]],
                 network_configuration: pulumi.Input['ContactProfilesPropertiesNetworkConfigurationArgs'],
                 resource_group_name: pulumi.Input[str],
                 auto_tracking_configuration: Optional[pulumi.Input['AutoTrackingConfiguration']] = None,
                 contact_profile_name: Optional[pulumi.Input[str]] = None,
                 event_hub_uri: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 minimum_elevation_degrees: Optional[pulumi.Input[float]] = None,
                 minimum_viable_contact_duration: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 third_party_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['ContactProfileThirdPartyConfigurationArgs']]]] = None):
        """
        The set of arguments for constructing a ContactProfile resource.
        :param pulumi.Input[Sequence[pulumi.Input['ContactProfileLinkArgs']]] links: Links of the Contact Profile. Describes RF links, modem processing, and IP endpoints.
        :param pulumi.Input['ContactProfilesPropertiesNetworkConfigurationArgs'] network_configuration: Network configuration of customer virtual network.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['AutoTrackingConfiguration'] auto_tracking_configuration: Auto-tracking configuration.
        :param pulumi.Input[str] contact_profile_name: Contact Profile name.
        :param pulumi.Input[str] event_hub_uri: ARM resource identifier of the Event Hub used for telemetry. Requires granting Orbital Resource Provider the rights to send telemetry into the hub.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[float] minimum_elevation_degrees: Minimum viable elevation for the contact in decimal degrees. Used for listing the available contacts with a spacecraft at a given ground station.
        :param pulumi.Input[str] minimum_viable_contact_duration: Minimum viable contact duration in ISO 8601 format. Used for listing the available contacts with a spacecraft at a given ground station.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input['ContactProfileThirdPartyConfigurationArgs']]] third_party_configurations: Third-party mission configuration of the Contact Profile. Describes RF links, modem processing, and IP endpoints.
        """
        pulumi.set(__self__, "links", links)
        pulumi.set(__self__, "network_configuration", network_configuration)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if auto_tracking_configuration is not None:
            pulumi.set(__self__, "auto_tracking_configuration", auto_tracking_configuration)
        if contact_profile_name is not None:
            pulumi.set(__self__, "contact_profile_name", contact_profile_name)
        if event_hub_uri is not None:
            pulumi.set(__self__, "event_hub_uri", event_hub_uri)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if minimum_elevation_degrees is not None:
            pulumi.set(__self__, "minimum_elevation_degrees", minimum_elevation_degrees)
        if minimum_viable_contact_duration is not None:
            pulumi.set(__self__, "minimum_viable_contact_duration", minimum_viable_contact_duration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if third_party_configurations is not None:
            pulumi.set(__self__, "third_party_configurations", third_party_configurations)

    @property
    @pulumi.getter
    def links(self) -> pulumi.Input[Sequence[pulumi.Input['ContactProfileLinkArgs']]]:
        """
        Links of the Contact Profile. Describes RF links, modem processing, and IP endpoints.
        """
        return pulumi.get(self, "links")

    @links.setter
    def links(self, value: pulumi.Input[Sequence[pulumi.Input['ContactProfileLinkArgs']]]):
        pulumi.set(self, "links", value)

    @property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> pulumi.Input['ContactProfilesPropertiesNetworkConfigurationArgs']:
        """
        Network configuration of customer virtual network.
        """
        return pulumi.get(self, "network_configuration")

    @network_configuration.setter
    def network_configuration(self, value: pulumi.Input['ContactProfilesPropertiesNetworkConfigurationArgs']):
        pulumi.set(self, "network_configuration", value)

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
    @pulumi.getter(name="autoTrackingConfiguration")
    def auto_tracking_configuration(self) -> Optional[pulumi.Input['AutoTrackingConfiguration']]:
        """
        Auto-tracking configuration.
        """
        return pulumi.get(self, "auto_tracking_configuration")

    @auto_tracking_configuration.setter
    def auto_tracking_configuration(self, value: Optional[pulumi.Input['AutoTrackingConfiguration']]):
        pulumi.set(self, "auto_tracking_configuration", value)

    @property
    @pulumi.getter(name="contactProfileName")
    def contact_profile_name(self) -> Optional[pulumi.Input[str]]:
        """
        Contact Profile name.
        """
        return pulumi.get(self, "contact_profile_name")

    @contact_profile_name.setter
    def contact_profile_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "contact_profile_name", value)

    @property
    @pulumi.getter(name="eventHubUri")
    def event_hub_uri(self) -> Optional[pulumi.Input[str]]:
        """
        ARM resource identifier of the Event Hub used for telemetry. Requires granting Orbital Resource Provider the rights to send telemetry into the hub.
        """
        return pulumi.get(self, "event_hub_uri")

    @event_hub_uri.setter
    def event_hub_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "event_hub_uri", value)

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
    @pulumi.getter(name="minimumElevationDegrees")
    def minimum_elevation_degrees(self) -> Optional[pulumi.Input[float]]:
        """
        Minimum viable elevation for the contact in decimal degrees. Used for listing the available contacts with a spacecraft at a given ground station.
        """
        return pulumi.get(self, "minimum_elevation_degrees")

    @minimum_elevation_degrees.setter
    def minimum_elevation_degrees(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "minimum_elevation_degrees", value)

    @property
    @pulumi.getter(name="minimumViableContactDuration")
    def minimum_viable_contact_duration(self) -> Optional[pulumi.Input[str]]:
        """
        Minimum viable contact duration in ISO 8601 format. Used for listing the available contacts with a spacecraft at a given ground station.
        """
        return pulumi.get(self, "minimum_viable_contact_duration")

    @minimum_viable_contact_duration.setter
    def minimum_viable_contact_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "minimum_viable_contact_duration", value)

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

    @property
    @pulumi.getter(name="thirdPartyConfigurations")
    def third_party_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ContactProfileThirdPartyConfigurationArgs']]]]:
        """
        Third-party mission configuration of the Contact Profile. Describes RF links, modem processing, and IP endpoints.
        """
        return pulumi.get(self, "third_party_configurations")

    @third_party_configurations.setter
    def third_party_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ContactProfileThirdPartyConfigurationArgs']]]]):
        pulumi.set(self, "third_party_configurations", value)


class ContactProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_tracking_configuration: Optional[pulumi.Input['AutoTrackingConfiguration']] = None,
                 contact_profile_name: Optional[pulumi.Input[str]] = None,
                 event_hub_uri: Optional[pulumi.Input[str]] = None,
                 links: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContactProfileLinkArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 minimum_elevation_degrees: Optional[pulumi.Input[float]] = None,
                 minimum_viable_contact_duration: Optional[pulumi.Input[str]] = None,
                 network_configuration: Optional[pulumi.Input[pulumi.InputType['ContactProfilesPropertiesNetworkConfigurationArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 third_party_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContactProfileThirdPartyConfigurationArgs']]]]] = None,
                 __props__=None):
        """
        Customer creates a Contact Profile Resource, which will contain all of the configurations required for scheduling a contact.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input['AutoTrackingConfiguration'] auto_tracking_configuration: Auto-tracking configuration.
        :param pulumi.Input[str] contact_profile_name: Contact Profile name.
        :param pulumi.Input[str] event_hub_uri: ARM resource identifier of the Event Hub used for telemetry. Requires granting Orbital Resource Provider the rights to send telemetry into the hub.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContactProfileLinkArgs']]]] links: Links of the Contact Profile. Describes RF links, modem processing, and IP endpoints.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[float] minimum_elevation_degrees: Minimum viable elevation for the contact in decimal degrees. Used for listing the available contacts with a spacecraft at a given ground station.
        :param pulumi.Input[str] minimum_viable_contact_duration: Minimum viable contact duration in ISO 8601 format. Used for listing the available contacts with a spacecraft at a given ground station.
        :param pulumi.Input[pulumi.InputType['ContactProfilesPropertiesNetworkConfigurationArgs']] network_configuration: Network configuration of customer virtual network.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContactProfileThirdPartyConfigurationArgs']]]] third_party_configurations: Third-party mission configuration of the Contact Profile. Describes RF links, modem processing, and IP endpoints.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ContactProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Customer creates a Contact Profile Resource, which will contain all of the configurations required for scheduling a contact.

        :param str resource_name: The name of the resource.
        :param ContactProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ContactProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_tracking_configuration: Optional[pulumi.Input['AutoTrackingConfiguration']] = None,
                 contact_profile_name: Optional[pulumi.Input[str]] = None,
                 event_hub_uri: Optional[pulumi.Input[str]] = None,
                 links: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContactProfileLinkArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 minimum_elevation_degrees: Optional[pulumi.Input[float]] = None,
                 minimum_viable_contact_duration: Optional[pulumi.Input[str]] = None,
                 network_configuration: Optional[pulumi.Input[pulumi.InputType['ContactProfilesPropertiesNetworkConfigurationArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 third_party_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContactProfileThirdPartyConfigurationArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ContactProfileArgs.__new__(ContactProfileArgs)

            __props__.__dict__["auto_tracking_configuration"] = auto_tracking_configuration
            __props__.__dict__["contact_profile_name"] = contact_profile_name
            __props__.__dict__["event_hub_uri"] = event_hub_uri
            if links is None and not opts.urn:
                raise TypeError("Missing required property 'links'")
            __props__.__dict__["links"] = links
            __props__.__dict__["location"] = location
            __props__.__dict__["minimum_elevation_degrees"] = minimum_elevation_degrees
            __props__.__dict__["minimum_viable_contact_duration"] = minimum_viable_contact_duration
            if network_configuration is None and not opts.urn:
                raise TypeError("Missing required property 'network_configuration'")
            __props__.__dict__["network_configuration"] = network_configuration
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["third_party_configurations"] = third_party_configurations
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:orbital:ContactProfile"), pulumi.Alias(type_="azure-native:orbital/v20220301:ContactProfile")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ContactProfile, __self__).__init__(
            'azure-native:orbital/v20221101:ContactProfile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ContactProfile':
        """
        Get an existing ContactProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ContactProfileArgs.__new__(ContactProfileArgs)

        __props__.__dict__["auto_tracking_configuration"] = None
        __props__.__dict__["event_hub_uri"] = None
        __props__.__dict__["links"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["minimum_elevation_degrees"] = None
        __props__.__dict__["minimum_viable_contact_duration"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_configuration"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["third_party_configurations"] = None
        __props__.__dict__["type"] = None
        return ContactProfile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoTrackingConfiguration")
    def auto_tracking_configuration(self) -> pulumi.Output[Optional[str]]:
        """
        Auto-tracking configuration.
        """
        return pulumi.get(self, "auto_tracking_configuration")

    @property
    @pulumi.getter(name="eventHubUri")
    def event_hub_uri(self) -> pulumi.Output[Optional[str]]:
        """
        ARM resource identifier of the Event Hub used for telemetry. Requires granting Orbital Resource Provider the rights to send telemetry into the hub.
        """
        return pulumi.get(self, "event_hub_uri")

    @property
    @pulumi.getter
    def links(self) -> pulumi.Output[Sequence['outputs.ContactProfileLinkResponse']]:
        """
        Links of the Contact Profile. Describes RF links, modem processing, and IP endpoints.
        """
        return pulumi.get(self, "links")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="minimumElevationDegrees")
    def minimum_elevation_degrees(self) -> pulumi.Output[Optional[float]]:
        """
        Minimum viable elevation for the contact in decimal degrees. Used for listing the available contacts with a spacecraft at a given ground station.
        """
        return pulumi.get(self, "minimum_elevation_degrees")

    @property
    @pulumi.getter(name="minimumViableContactDuration")
    def minimum_viable_contact_duration(self) -> pulumi.Output[Optional[str]]:
        """
        Minimum viable contact duration in ISO 8601 format. Used for listing the available contacts with a spacecraft at a given ground station.
        """
        return pulumi.get(self, "minimum_viable_contact_duration")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> pulumi.Output['outputs.ContactProfilesPropertiesResponseNetworkConfiguration']:
        """
        Network configuration of customer virtual network.
        """
        return pulumi.get(self, "network_configuration")

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
    @pulumi.getter(name="thirdPartyConfigurations")
    def third_party_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.ContactProfileThirdPartyConfigurationResponse']]]:
        """
        Third-party mission configuration of the Contact Profile. Describes RF links, modem processing, and IP endpoints.
        """
        return pulumi.get(self, "third_party_configurations")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

