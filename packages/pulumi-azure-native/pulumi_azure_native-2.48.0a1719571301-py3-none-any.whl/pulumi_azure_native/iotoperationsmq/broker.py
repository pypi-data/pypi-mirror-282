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
from ._enums import *
from ._inputs import *

__all__ = ['BrokerArgs', 'Broker']

@pulumi.input_type
class BrokerArgs:
    def __init__(__self__, *,
                 auth_image: pulumi.Input['ContainerImageArgs'],
                 broker_image: pulumi.Input['ContainerImageArgs'],
                 extended_location: pulumi.Input['ExtendedLocationPropertyArgs'],
                 health_manager_image: pulumi.Input['ContainerImageArgs'],
                 mode: pulumi.Input[Union[str, 'RunMode']],
                 mq_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 broker_name: Optional[pulumi.Input[str]] = None,
                 broker_node_tolerations: Optional[pulumi.Input['NodeTolerationsArgs']] = None,
                 cardinality: Optional[pulumi.Input['CardinalityArgs']] = None,
                 diagnostics: Optional[pulumi.Input['BrokerDiagnosticsArgs']] = None,
                 disk_backed_message_buffer_settings: Optional[pulumi.Input['DiskBackedMessageBufferSettingsArgs']] = None,
                 encrypt_internal_traffic: Optional[pulumi.Input[bool]] = None,
                 health_manager_node_tolerations: Optional[pulumi.Input['NodeTolerationsArgs']] = None,
                 internal_certs: Optional[pulumi.Input['CertManagerCertOptionsArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 memory_profile: Optional[pulumi.Input[Union[str, 'BrokerMemoryProfile']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Broker resource.
        :param pulumi.Input['ContainerImageArgs'] auth_image: The details of Authentication Docker Image.
        :param pulumi.Input['ContainerImageArgs'] broker_image: The details of Broker Docker Image.
        :param pulumi.Input['ExtendedLocationPropertyArgs'] extended_location: Extended Location
        :param pulumi.Input['ContainerImageArgs'] health_manager_image: The details of Health Manager Docker Image.
        :param pulumi.Input[Union[str, 'RunMode']] mode: The Running Mode of the Broker Deployment.
        :param pulumi.Input[str] mq_name: Name of MQ resource
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] broker_name: Name of MQ broker resource
        :param pulumi.Input['NodeTolerationsArgs'] broker_node_tolerations: The details of Node Tolerations for Broker Pods.
        :param pulumi.Input['CardinalityArgs'] cardinality: The cardinality details of the broker.
        :param pulumi.Input['BrokerDiagnosticsArgs'] diagnostics: The diagnostic details of the broker deployment.
        :param pulumi.Input['DiskBackedMessageBufferSettingsArgs'] disk_backed_message_buffer_settings: The settings of the disk-backed message buffer.
        :param pulumi.Input[bool] encrypt_internal_traffic: The setting to enable or disable encryption of internal Traffic.
        :param pulumi.Input['NodeTolerationsArgs'] health_manager_node_tolerations: The details of Node Tolerations for Health Manager Pods.
        :param pulumi.Input['CertManagerCertOptionsArgs'] internal_certs: Details of the internal CA cert that will be used to secure communication between pods.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Union[str, 'BrokerMemoryProfile']] memory_profile: Memory profile of broker.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "auth_image", auth_image)
        pulumi.set(__self__, "broker_image", broker_image)
        pulumi.set(__self__, "extended_location", extended_location)
        pulumi.set(__self__, "health_manager_image", health_manager_image)
        pulumi.set(__self__, "mode", mode)
        pulumi.set(__self__, "mq_name", mq_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if broker_name is not None:
            pulumi.set(__self__, "broker_name", broker_name)
        if broker_node_tolerations is not None:
            pulumi.set(__self__, "broker_node_tolerations", broker_node_tolerations)
        if cardinality is not None:
            pulumi.set(__self__, "cardinality", cardinality)
        if diagnostics is not None:
            pulumi.set(__self__, "diagnostics", diagnostics)
        if disk_backed_message_buffer_settings is not None:
            pulumi.set(__self__, "disk_backed_message_buffer_settings", disk_backed_message_buffer_settings)
        if encrypt_internal_traffic is None:
            encrypt_internal_traffic = True
        if encrypt_internal_traffic is not None:
            pulumi.set(__self__, "encrypt_internal_traffic", encrypt_internal_traffic)
        if health_manager_node_tolerations is not None:
            pulumi.set(__self__, "health_manager_node_tolerations", health_manager_node_tolerations)
        if internal_certs is not None:
            pulumi.set(__self__, "internal_certs", internal_certs)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if memory_profile is None:
            memory_profile = 'medium'
        if memory_profile is not None:
            pulumi.set(__self__, "memory_profile", memory_profile)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="authImage")
    def auth_image(self) -> pulumi.Input['ContainerImageArgs']:
        """
        The details of Authentication Docker Image.
        """
        return pulumi.get(self, "auth_image")

    @auth_image.setter
    def auth_image(self, value: pulumi.Input['ContainerImageArgs']):
        pulumi.set(self, "auth_image", value)

    @property
    @pulumi.getter(name="brokerImage")
    def broker_image(self) -> pulumi.Input['ContainerImageArgs']:
        """
        The details of Broker Docker Image.
        """
        return pulumi.get(self, "broker_image")

    @broker_image.setter
    def broker_image(self, value: pulumi.Input['ContainerImageArgs']):
        pulumi.set(self, "broker_image", value)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input['ExtendedLocationPropertyArgs']:
        """
        Extended Location
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: pulumi.Input['ExtendedLocationPropertyArgs']):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter(name="healthManagerImage")
    def health_manager_image(self) -> pulumi.Input['ContainerImageArgs']:
        """
        The details of Health Manager Docker Image.
        """
        return pulumi.get(self, "health_manager_image")

    @health_manager_image.setter
    def health_manager_image(self, value: pulumi.Input['ContainerImageArgs']):
        pulumi.set(self, "health_manager_image", value)

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Input[Union[str, 'RunMode']]:
        """
        The Running Mode of the Broker Deployment.
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: pulumi.Input[Union[str, 'RunMode']]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter(name="mqName")
    def mq_name(self) -> pulumi.Input[str]:
        """
        Name of MQ resource
        """
        return pulumi.get(self, "mq_name")

    @mq_name.setter
    def mq_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "mq_name", value)

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
    @pulumi.getter(name="brokerName")
    def broker_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of MQ broker resource
        """
        return pulumi.get(self, "broker_name")

    @broker_name.setter
    def broker_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "broker_name", value)

    @property
    @pulumi.getter(name="brokerNodeTolerations")
    def broker_node_tolerations(self) -> Optional[pulumi.Input['NodeTolerationsArgs']]:
        """
        The details of Node Tolerations for Broker Pods.
        """
        return pulumi.get(self, "broker_node_tolerations")

    @broker_node_tolerations.setter
    def broker_node_tolerations(self, value: Optional[pulumi.Input['NodeTolerationsArgs']]):
        pulumi.set(self, "broker_node_tolerations", value)

    @property
    @pulumi.getter
    def cardinality(self) -> Optional[pulumi.Input['CardinalityArgs']]:
        """
        The cardinality details of the broker.
        """
        return pulumi.get(self, "cardinality")

    @cardinality.setter
    def cardinality(self, value: Optional[pulumi.Input['CardinalityArgs']]):
        pulumi.set(self, "cardinality", value)

    @property
    @pulumi.getter
    def diagnostics(self) -> Optional[pulumi.Input['BrokerDiagnosticsArgs']]:
        """
        The diagnostic details of the broker deployment.
        """
        return pulumi.get(self, "diagnostics")

    @diagnostics.setter
    def diagnostics(self, value: Optional[pulumi.Input['BrokerDiagnosticsArgs']]):
        pulumi.set(self, "diagnostics", value)

    @property
    @pulumi.getter(name="diskBackedMessageBufferSettings")
    def disk_backed_message_buffer_settings(self) -> Optional[pulumi.Input['DiskBackedMessageBufferSettingsArgs']]:
        """
        The settings of the disk-backed message buffer.
        """
        return pulumi.get(self, "disk_backed_message_buffer_settings")

    @disk_backed_message_buffer_settings.setter
    def disk_backed_message_buffer_settings(self, value: Optional[pulumi.Input['DiskBackedMessageBufferSettingsArgs']]):
        pulumi.set(self, "disk_backed_message_buffer_settings", value)

    @property
    @pulumi.getter(name="encryptInternalTraffic")
    def encrypt_internal_traffic(self) -> Optional[pulumi.Input[bool]]:
        """
        The setting to enable or disable encryption of internal Traffic.
        """
        return pulumi.get(self, "encrypt_internal_traffic")

    @encrypt_internal_traffic.setter
    def encrypt_internal_traffic(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "encrypt_internal_traffic", value)

    @property
    @pulumi.getter(name="healthManagerNodeTolerations")
    def health_manager_node_tolerations(self) -> Optional[pulumi.Input['NodeTolerationsArgs']]:
        """
        The details of Node Tolerations for Health Manager Pods.
        """
        return pulumi.get(self, "health_manager_node_tolerations")

    @health_manager_node_tolerations.setter
    def health_manager_node_tolerations(self, value: Optional[pulumi.Input['NodeTolerationsArgs']]):
        pulumi.set(self, "health_manager_node_tolerations", value)

    @property
    @pulumi.getter(name="internalCerts")
    def internal_certs(self) -> Optional[pulumi.Input['CertManagerCertOptionsArgs']]:
        """
        Details of the internal CA cert that will be used to secure communication between pods.
        """
        return pulumi.get(self, "internal_certs")

    @internal_certs.setter
    def internal_certs(self, value: Optional[pulumi.Input['CertManagerCertOptionsArgs']]):
        pulumi.set(self, "internal_certs", value)

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
    @pulumi.getter(name="memoryProfile")
    def memory_profile(self) -> Optional[pulumi.Input[Union[str, 'BrokerMemoryProfile']]]:
        """
        Memory profile of broker.
        """
        return pulumi.get(self, "memory_profile")

    @memory_profile.setter
    def memory_profile(self, value: Optional[pulumi.Input[Union[str, 'BrokerMemoryProfile']]]):
        pulumi.set(self, "memory_profile", value)

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


class Broker(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_image: Optional[pulumi.Input[pulumi.InputType['ContainerImageArgs']]] = None,
                 broker_image: Optional[pulumi.Input[pulumi.InputType['ContainerImageArgs']]] = None,
                 broker_name: Optional[pulumi.Input[str]] = None,
                 broker_node_tolerations: Optional[pulumi.Input[pulumi.InputType['NodeTolerationsArgs']]] = None,
                 cardinality: Optional[pulumi.Input[pulumi.InputType['CardinalityArgs']]] = None,
                 diagnostics: Optional[pulumi.Input[pulumi.InputType['BrokerDiagnosticsArgs']]] = None,
                 disk_backed_message_buffer_settings: Optional[pulumi.Input[pulumi.InputType['DiskBackedMessageBufferSettingsArgs']]] = None,
                 encrypt_internal_traffic: Optional[pulumi.Input[bool]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationPropertyArgs']]] = None,
                 health_manager_image: Optional[pulumi.Input[pulumi.InputType['ContainerImageArgs']]] = None,
                 health_manager_node_tolerations: Optional[pulumi.Input[pulumi.InputType['NodeTolerationsArgs']]] = None,
                 internal_certs: Optional[pulumi.Input[pulumi.InputType['CertManagerCertOptionsArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 memory_profile: Optional[pulumi.Input[Union[str, 'BrokerMemoryProfile']]] = None,
                 mode: Optional[pulumi.Input[Union[str, 'RunMode']]] = None,
                 mq_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        MQ broker resource
        Azure REST API version: 2023-10-04-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ContainerImageArgs']] auth_image: The details of Authentication Docker Image.
        :param pulumi.Input[pulumi.InputType['ContainerImageArgs']] broker_image: The details of Broker Docker Image.
        :param pulumi.Input[str] broker_name: Name of MQ broker resource
        :param pulumi.Input[pulumi.InputType['NodeTolerationsArgs']] broker_node_tolerations: The details of Node Tolerations for Broker Pods.
        :param pulumi.Input[pulumi.InputType['CardinalityArgs']] cardinality: The cardinality details of the broker.
        :param pulumi.Input[pulumi.InputType['BrokerDiagnosticsArgs']] diagnostics: The diagnostic details of the broker deployment.
        :param pulumi.Input[pulumi.InputType['DiskBackedMessageBufferSettingsArgs']] disk_backed_message_buffer_settings: The settings of the disk-backed message buffer.
        :param pulumi.Input[bool] encrypt_internal_traffic: The setting to enable or disable encryption of internal Traffic.
        :param pulumi.Input[pulumi.InputType['ExtendedLocationPropertyArgs']] extended_location: Extended Location
        :param pulumi.Input[pulumi.InputType['ContainerImageArgs']] health_manager_image: The details of Health Manager Docker Image.
        :param pulumi.Input[pulumi.InputType['NodeTolerationsArgs']] health_manager_node_tolerations: The details of Node Tolerations for Health Manager Pods.
        :param pulumi.Input[pulumi.InputType['CertManagerCertOptionsArgs']] internal_certs: Details of the internal CA cert that will be used to secure communication between pods.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Union[str, 'BrokerMemoryProfile']] memory_profile: Memory profile of broker.
        :param pulumi.Input[Union[str, 'RunMode']] mode: The Running Mode of the Broker Deployment.
        :param pulumi.Input[str] mq_name: Name of MQ resource
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BrokerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        MQ broker resource
        Azure REST API version: 2023-10-04-preview.

        :param str resource_name: The name of the resource.
        :param BrokerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BrokerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_image: Optional[pulumi.Input[pulumi.InputType['ContainerImageArgs']]] = None,
                 broker_image: Optional[pulumi.Input[pulumi.InputType['ContainerImageArgs']]] = None,
                 broker_name: Optional[pulumi.Input[str]] = None,
                 broker_node_tolerations: Optional[pulumi.Input[pulumi.InputType['NodeTolerationsArgs']]] = None,
                 cardinality: Optional[pulumi.Input[pulumi.InputType['CardinalityArgs']]] = None,
                 diagnostics: Optional[pulumi.Input[pulumi.InputType['BrokerDiagnosticsArgs']]] = None,
                 disk_backed_message_buffer_settings: Optional[pulumi.Input[pulumi.InputType['DiskBackedMessageBufferSettingsArgs']]] = None,
                 encrypt_internal_traffic: Optional[pulumi.Input[bool]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationPropertyArgs']]] = None,
                 health_manager_image: Optional[pulumi.Input[pulumi.InputType['ContainerImageArgs']]] = None,
                 health_manager_node_tolerations: Optional[pulumi.Input[pulumi.InputType['NodeTolerationsArgs']]] = None,
                 internal_certs: Optional[pulumi.Input[pulumi.InputType['CertManagerCertOptionsArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 memory_profile: Optional[pulumi.Input[Union[str, 'BrokerMemoryProfile']]] = None,
                 mode: Optional[pulumi.Input[Union[str, 'RunMode']]] = None,
                 mq_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BrokerArgs.__new__(BrokerArgs)

            if auth_image is None and not opts.urn:
                raise TypeError("Missing required property 'auth_image'")
            __props__.__dict__["auth_image"] = auth_image
            if broker_image is None and not opts.urn:
                raise TypeError("Missing required property 'broker_image'")
            __props__.__dict__["broker_image"] = broker_image
            __props__.__dict__["broker_name"] = broker_name
            __props__.__dict__["broker_node_tolerations"] = broker_node_tolerations
            __props__.__dict__["cardinality"] = cardinality
            __props__.__dict__["diagnostics"] = diagnostics
            __props__.__dict__["disk_backed_message_buffer_settings"] = disk_backed_message_buffer_settings
            if encrypt_internal_traffic is None:
                encrypt_internal_traffic = True
            __props__.__dict__["encrypt_internal_traffic"] = encrypt_internal_traffic
            if extended_location is None and not opts.urn:
                raise TypeError("Missing required property 'extended_location'")
            __props__.__dict__["extended_location"] = extended_location
            if health_manager_image is None and not opts.urn:
                raise TypeError("Missing required property 'health_manager_image'")
            __props__.__dict__["health_manager_image"] = health_manager_image
            __props__.__dict__["health_manager_node_tolerations"] = health_manager_node_tolerations
            __props__.__dict__["internal_certs"] = internal_certs
            __props__.__dict__["location"] = location
            if memory_profile is None:
                memory_profile = 'medium'
            __props__.__dict__["memory_profile"] = memory_profile
            if mode is None and not opts.urn:
                raise TypeError("Missing required property 'mode'")
            __props__.__dict__["mode"] = mode
            if mq_name is None and not opts.urn:
                raise TypeError("Missing required property 'mq_name'")
            __props__.__dict__["mq_name"] = mq_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:iotoperationsmq/v20231004preview:Broker")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Broker, __self__).__init__(
            'azure-native:iotoperationsmq:Broker',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Broker':
        """
        Get an existing Broker resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BrokerArgs.__new__(BrokerArgs)

        __props__.__dict__["auth_image"] = None
        __props__.__dict__["broker_image"] = None
        __props__.__dict__["broker_node_tolerations"] = None
        __props__.__dict__["cardinality"] = None
        __props__.__dict__["diagnostics"] = None
        __props__.__dict__["disk_backed_message_buffer_settings"] = None
        __props__.__dict__["encrypt_internal_traffic"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["health_manager_image"] = None
        __props__.__dict__["health_manager_node_tolerations"] = None
        __props__.__dict__["internal_certs"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["memory_profile"] = None
        __props__.__dict__["mode"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Broker(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authImage")
    def auth_image(self) -> pulumi.Output['outputs.ContainerImageResponse']:
        """
        The details of Authentication Docker Image.
        """
        return pulumi.get(self, "auth_image")

    @property
    @pulumi.getter(name="brokerImage")
    def broker_image(self) -> pulumi.Output['outputs.ContainerImageResponse']:
        """
        The details of Broker Docker Image.
        """
        return pulumi.get(self, "broker_image")

    @property
    @pulumi.getter(name="brokerNodeTolerations")
    def broker_node_tolerations(self) -> pulumi.Output[Optional['outputs.NodeTolerationsResponse']]:
        """
        The details of Node Tolerations for Broker Pods.
        """
        return pulumi.get(self, "broker_node_tolerations")

    @property
    @pulumi.getter
    def cardinality(self) -> pulumi.Output[Optional['outputs.CardinalityResponse']]:
        """
        The cardinality details of the broker.
        """
        return pulumi.get(self, "cardinality")

    @property
    @pulumi.getter
    def diagnostics(self) -> pulumi.Output[Optional['outputs.BrokerDiagnosticsResponse']]:
        """
        The diagnostic details of the broker deployment.
        """
        return pulumi.get(self, "diagnostics")

    @property
    @pulumi.getter(name="diskBackedMessageBufferSettings")
    def disk_backed_message_buffer_settings(self) -> pulumi.Output[Optional['outputs.DiskBackedMessageBufferSettingsResponse']]:
        """
        The settings of the disk-backed message buffer.
        """
        return pulumi.get(self, "disk_backed_message_buffer_settings")

    @property
    @pulumi.getter(name="encryptInternalTraffic")
    def encrypt_internal_traffic(self) -> pulumi.Output[Optional[bool]]:
        """
        The setting to enable or disable encryption of internal Traffic.
        """
        return pulumi.get(self, "encrypt_internal_traffic")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output['outputs.ExtendedLocationPropertyResponse']:
        """
        Extended Location
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="healthManagerImage")
    def health_manager_image(self) -> pulumi.Output['outputs.ContainerImageResponse']:
        """
        The details of Health Manager Docker Image.
        """
        return pulumi.get(self, "health_manager_image")

    @property
    @pulumi.getter(name="healthManagerNodeTolerations")
    def health_manager_node_tolerations(self) -> pulumi.Output[Optional['outputs.NodeTolerationsResponse']]:
        """
        The details of Node Tolerations for Health Manager Pods.
        """
        return pulumi.get(self, "health_manager_node_tolerations")

    @property
    @pulumi.getter(name="internalCerts")
    def internal_certs(self) -> pulumi.Output[Optional['outputs.CertManagerCertOptionsResponse']]:
        """
        Details of the internal CA cert that will be used to secure communication between pods.
        """
        return pulumi.get(self, "internal_certs")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="memoryProfile")
    def memory_profile(self) -> pulumi.Output[Optional[str]]:
        """
        Memory profile of broker.
        """
        return pulumi.get(self, "memory_profile")

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Output[str]:
        """
        The Running Mode of the Broker Deployment.
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

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

