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
    'Gen2StorageConfigurationInputArgs',
    'LocalTimestampTimeZoneOffsetArgs',
    'LocalTimestampArgs',
    'ReferenceDataSetKeyPropertyArgs',
    'SkuArgs',
    'TimeSeriesIdPropertyArgs',
    'WarmStoreConfigurationPropertiesArgs',
]

@pulumi.input_type
class Gen2StorageConfigurationInputArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 management_key: pulumi.Input[str]):
        """
        The storage configuration provides the connection details that allows the Time Series Insights service to connect to the customer storage account that is used to store the environment's data.
        :param pulumi.Input[str] account_name: The name of the storage account that will hold the environment's Gen2 data.
        :param pulumi.Input[str] management_key: The value of the management key that grants the Time Series Insights service write access to the storage account. This property is not shown in environment responses.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "management_key", management_key)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The name of the storage account that will hold the environment's Gen2 data.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="managementKey")
    def management_key(self) -> pulumi.Input[str]:
        """
        The value of the management key that grants the Time Series Insights service write access to the storage account. This property is not shown in environment responses.
        """
        return pulumi.get(self, "management_key")

    @management_key.setter
    def management_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "management_key", value)


@pulumi.input_type
class LocalTimestampTimeZoneOffsetArgs:
    def __init__(__self__, *,
                 property_name: Optional[pulumi.Input[str]] = None):
        """
        An object that represents the offset information for the local timestamp format specified. Should not be specified for LocalTimestampFormat - Embedded.
        :param pulumi.Input[str] property_name: The event property that will be contain the offset information to calculate the local timestamp. When the LocalTimestampFormat is Iana, the property name will contain the name of the column which contains IANA Timezone Name (eg: Americas/Los Angeles). When LocalTimestampFormat is Timespan, it contains the name of property which contains values representing the offset (eg: P1D or 1.00:00:00)
        """
        if property_name is not None:
            pulumi.set(__self__, "property_name", property_name)

    @property
    @pulumi.getter(name="propertyName")
    def property_name(self) -> Optional[pulumi.Input[str]]:
        """
        The event property that will be contain the offset information to calculate the local timestamp. When the LocalTimestampFormat is Iana, the property name will contain the name of the column which contains IANA Timezone Name (eg: Americas/Los Angeles). When LocalTimestampFormat is Timespan, it contains the name of property which contains values representing the offset (eg: P1D or 1.00:00:00)
        """
        return pulumi.get(self, "property_name")

    @property_name.setter
    def property_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "property_name", value)


@pulumi.input_type
class LocalTimestampArgs:
    def __init__(__self__, *,
                 format: Optional[pulumi.Input[Union[str, 'LocalTimestampFormat']]] = None,
                 time_zone_offset: Optional[pulumi.Input['LocalTimestampTimeZoneOffsetArgs']] = None):
        """
        An object that represents the local timestamp property. It contains the format of local timestamp that needs to be used and the corresponding timezone offset information. If a value isn't specified for localTimestamp, or if null, then the local timestamp will not be ingressed with the events.
        :param pulumi.Input[Union[str, 'LocalTimestampFormat']] format: An enum that represents the format of the local timestamp property that needs to be set.
        :param pulumi.Input['LocalTimestampTimeZoneOffsetArgs'] time_zone_offset: An object that represents the offset information for the local timestamp format specified. Should not be specified for LocalTimestampFormat - Embedded.
        """
        if format is not None:
            pulumi.set(__self__, "format", format)
        if time_zone_offset is not None:
            pulumi.set(__self__, "time_zone_offset", time_zone_offset)

    @property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[Union[str, 'LocalTimestampFormat']]]:
        """
        An enum that represents the format of the local timestamp property that needs to be set.
        """
        return pulumi.get(self, "format")

    @format.setter
    def format(self, value: Optional[pulumi.Input[Union[str, 'LocalTimestampFormat']]]):
        pulumi.set(self, "format", value)

    @property
    @pulumi.getter(name="timeZoneOffset")
    def time_zone_offset(self) -> Optional[pulumi.Input['LocalTimestampTimeZoneOffsetArgs']]:
        """
        An object that represents the offset information for the local timestamp format specified. Should not be specified for LocalTimestampFormat - Embedded.
        """
        return pulumi.get(self, "time_zone_offset")

    @time_zone_offset.setter
    def time_zone_offset(self, value: Optional[pulumi.Input['LocalTimestampTimeZoneOffsetArgs']]):
        pulumi.set(self, "time_zone_offset", value)


@pulumi.input_type
class ReferenceDataSetKeyPropertyArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[Union[str, 'ReferenceDataKeyPropertyType']]] = None):
        """
        A key property for the reference data set. A reference data set can have multiple key properties.
        :param pulumi.Input[str] name: The name of the key property.
        :param pulumi.Input[Union[str, 'ReferenceDataKeyPropertyType']] type: The type of the key property.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the key property.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[str, 'ReferenceDataKeyPropertyType']]]:
        """
        The type of the key property.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[str, 'ReferenceDataKeyPropertyType']]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *,
                 capacity: pulumi.Input[int],
                 name: pulumi.Input[Union[str, 'SkuName']]):
        """
        The sku determines the type of environment, either Gen1 (S1 or S2) or Gen2 (L1). For Gen1 environments the sku determines the capacity of the environment, the ingress rate, and the billing rate.
        :param pulumi.Input[int] capacity: The capacity of the sku. For Gen1 environments, this value can be changed to support scale out of environments after they have been created.
        :param pulumi.Input[Union[str, 'SkuName']] name: The name of this SKU.
        """
        pulumi.set(__self__, "capacity", capacity)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def capacity(self) -> pulumi.Input[int]:
        """
        The capacity of the sku. For Gen1 environments, this value can be changed to support scale out of environments after they have been created.
        """
        return pulumi.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: pulumi.Input[int]):
        pulumi.set(self, "capacity", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[str, 'SkuName']]:
        """
        The name of this SKU.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[Union[str, 'SkuName']]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class TimeSeriesIdPropertyArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[Union[str, 'PropertyType']]] = None):
        """
        The structure of the property that a time series id can have. An environment can have multiple such properties.
        :param pulumi.Input[str] name: The name of the property.
        :param pulumi.Input[Union[str, 'PropertyType']] type: The type of the property.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the property.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[str, 'PropertyType']]]:
        """
        The type of the property.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[str, 'PropertyType']]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class WarmStoreConfigurationPropertiesArgs:
    def __init__(__self__, *,
                 data_retention: pulumi.Input[str]):
        """
        The warm store configuration provides the details to create a warm store cache that will retain a copy of the environment's data available for faster query.
        :param pulumi.Input[str] data_retention: ISO8601 timespan specifying the number of days the environment's events will be available for query from the warm store.
        """
        pulumi.set(__self__, "data_retention", data_retention)

    @property
    @pulumi.getter(name="dataRetention")
    def data_retention(self) -> pulumi.Input[str]:
        """
        ISO8601 timespan specifying the number of days the environment's events will be available for query from the warm store.
        """
        return pulumi.get(self, "data_retention")

    @data_retention.setter
    def data_retention(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_retention", value)


