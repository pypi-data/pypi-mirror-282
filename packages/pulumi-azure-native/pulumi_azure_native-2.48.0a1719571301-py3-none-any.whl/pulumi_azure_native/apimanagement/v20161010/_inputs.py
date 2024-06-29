# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'AdditionalRegionArgs',
    'ApiManagementServiceSkuPropertiesArgs',
    'CertificateInformationArgs',
    'HostnameConfigurationArgs',
    'VirtualNetworkConfigurationArgs',
]

@pulumi.input_type
class AdditionalRegionArgs:
    def __init__(__self__, *,
                 location: pulumi.Input[str],
                 sku_type: pulumi.Input['SkuType'],
                 sku_unit_count: Optional[pulumi.Input[int]] = None,
                 vpnconfiguration: Optional[pulumi.Input['VirtualNetworkConfigurationArgs']] = None):
        """
        Description of an additional API Management resource location.
        :param pulumi.Input[str] location: The location name of the additional region among Azure Data center regions.
        :param pulumi.Input['SkuType'] sku_type: The SKU type in the location.
        :param pulumi.Input[int] sku_unit_count: The SKU Unit count at the location. The maximum SKU Unit count depends on the SkuType. Maximum allowed for Developer SKU is 1, for Standard SKU is 4, and for Premium SKU is 10, at a location.
        :param pulumi.Input['VirtualNetworkConfigurationArgs'] vpnconfiguration: Virtual network configuration for the location.
        """
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "sku_type", sku_type)
        if sku_unit_count is None:
            sku_unit_count = 1
        if sku_unit_count is not None:
            pulumi.set(__self__, "sku_unit_count", sku_unit_count)
        if vpnconfiguration is not None:
            pulumi.set(__self__, "vpnconfiguration", vpnconfiguration)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        The location name of the additional region among Azure Data center regions.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="skuType")
    def sku_type(self) -> pulumi.Input['SkuType']:
        """
        The SKU type in the location.
        """
        return pulumi.get(self, "sku_type")

    @sku_type.setter
    def sku_type(self, value: pulumi.Input['SkuType']):
        pulumi.set(self, "sku_type", value)

    @property
    @pulumi.getter(name="skuUnitCount")
    def sku_unit_count(self) -> Optional[pulumi.Input[int]]:
        """
        The SKU Unit count at the location. The maximum SKU Unit count depends on the SkuType. Maximum allowed for Developer SKU is 1, for Standard SKU is 4, and for Premium SKU is 10, at a location.
        """
        return pulumi.get(self, "sku_unit_count")

    @sku_unit_count.setter
    def sku_unit_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "sku_unit_count", value)

    @property
    @pulumi.getter
    def vpnconfiguration(self) -> Optional[pulumi.Input['VirtualNetworkConfigurationArgs']]:
        """
        Virtual network configuration for the location.
        """
        return pulumi.get(self, "vpnconfiguration")

    @vpnconfiguration.setter
    def vpnconfiguration(self, value: Optional[pulumi.Input['VirtualNetworkConfigurationArgs']]):
        pulumi.set(self, "vpnconfiguration", value)


@pulumi.input_type
class ApiManagementServiceSkuPropertiesArgs:
    def __init__(__self__, *,
                 name: pulumi.Input['SkuType'],
                 capacity: Optional[pulumi.Input[int]] = None):
        """
        API Management service resource SKU properties.
        :param pulumi.Input['SkuType'] name: Name of the Sku.
        :param pulumi.Input[int] capacity: Capacity of the SKU (number of deployed units of the SKU). The default value is 1.
        """
        pulumi.set(__self__, "name", name)
        if capacity is None:
            capacity = 1
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input['SkuType']:
        """
        Name of the Sku.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input['SkuType']):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[int]]:
        """
        Capacity of the SKU (number of deployed units of the SKU). The default value is 1.
        """
        return pulumi.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "capacity", value)


@pulumi.input_type
class CertificateInformationArgs:
    def __init__(__self__, *,
                 expiry: pulumi.Input[str],
                 subject: pulumi.Input[str],
                 thumbprint: pulumi.Input[str]):
        """
        SSL certificate information.
        :param pulumi.Input[str] expiry: Expiration date of the certificate. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.
        :param pulumi.Input[str] subject: Subject of the certificate.
        :param pulumi.Input[str] thumbprint: Thumbprint of the certificate.
        """
        pulumi.set(__self__, "expiry", expiry)
        pulumi.set(__self__, "subject", subject)
        pulumi.set(__self__, "thumbprint", thumbprint)

    @property
    @pulumi.getter
    def expiry(self) -> pulumi.Input[str]:
        """
        Expiration date of the certificate. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.
        """
        return pulumi.get(self, "expiry")

    @expiry.setter
    def expiry(self, value: pulumi.Input[str]):
        pulumi.set(self, "expiry", value)

    @property
    @pulumi.getter
    def subject(self) -> pulumi.Input[str]:
        """
        Subject of the certificate.
        """
        return pulumi.get(self, "subject")

    @subject.setter
    def subject(self, value: pulumi.Input[str]):
        pulumi.set(self, "subject", value)

    @property
    @pulumi.getter
    def thumbprint(self) -> pulumi.Input[str]:
        """
        Thumbprint of the certificate.
        """
        return pulumi.get(self, "thumbprint")

    @thumbprint.setter
    def thumbprint(self, value: pulumi.Input[str]):
        pulumi.set(self, "thumbprint", value)


@pulumi.input_type
class HostnameConfigurationArgs:
    def __init__(__self__, *,
                 certificate: pulumi.Input['CertificateInformationArgs'],
                 hostname: pulumi.Input[str],
                 type: pulumi.Input['HostnameType']):
        """
        Custom hostname configuration.
        :param pulumi.Input['CertificateInformationArgs'] certificate: Certificate information.
        :param pulumi.Input[str] hostname: Hostname.
        :param pulumi.Input['HostnameType'] type: Hostname type.
        """
        pulumi.set(__self__, "certificate", certificate)
        pulumi.set(__self__, "hostname", hostname)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def certificate(self) -> pulumi.Input['CertificateInformationArgs']:
        """
        Certificate information.
        """
        return pulumi.get(self, "certificate")

    @certificate.setter
    def certificate(self, value: pulumi.Input['CertificateInformationArgs']):
        pulumi.set(self, "certificate", value)

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Input[str]:
        """
        Hostname.
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: pulumi.Input[str]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input['HostnameType']:
        """
        Hostname type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input['HostnameType']):
        pulumi.set(self, "type", value)


@pulumi.input_type
class VirtualNetworkConfigurationArgs:
    def __init__(__self__, *,
                 location: Optional[pulumi.Input[str]] = None,
                 subnet_resource_id: Optional[pulumi.Input[str]] = None):
        """
        Configuration of a virtual network to which API Management service is deployed.
        :param pulumi.Input[str] location: The location of the virtual network.
        :param pulumi.Input[str] subnet_resource_id: The full resource ID of a subnet in a virtual network to deploy the API Management service in.
        """
        if location is not None:
            pulumi.set(__self__, "location", location)
        if subnet_resource_id is not None:
            pulumi.set(__self__, "subnet_resource_id", subnet_resource_id)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the virtual network.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="subnetResourceId")
    def subnet_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The full resource ID of a subnet in a virtual network to deploy the API Management service in.
        """
        return pulumi.get(self, "subnet_resource_id")

    @subnet_resource_id.setter
    def subnet_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_resource_id", value)


