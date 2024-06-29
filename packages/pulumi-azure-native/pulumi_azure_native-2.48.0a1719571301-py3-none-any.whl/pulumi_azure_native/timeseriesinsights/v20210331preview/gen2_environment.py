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

__all__ = ['Gen2EnvironmentArgs', 'Gen2Environment']

@pulumi.input_type
class Gen2EnvironmentArgs:
    def __init__(__self__, *,
                 kind: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 sku: pulumi.Input['SkuArgs'],
                 storage_configuration: pulumi.Input['Gen2StorageConfigurationInputArgs'],
                 time_series_id_properties: pulumi.Input[Sequence[pulumi.Input['TimeSeriesIdPropertyArgs']]],
                 environment_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 warm_store_configuration: Optional[pulumi.Input['WarmStoreConfigurationPropertiesArgs']] = None):
        """
        The set of arguments for constructing a Gen2Environment resource.
        :param pulumi.Input[str] kind: The kind of the environment.
               Expected value is 'Gen2'.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input['SkuArgs'] sku: The sku determines the type of environment, either Gen1 (S1 or S2) or Gen2 (L1). For Gen1 environments the sku determines the capacity of the environment, the ingress rate, and the billing rate.
        :param pulumi.Input['Gen2StorageConfigurationInputArgs'] storage_configuration: The storage configuration provides the connection details that allows the Time Series Insights service to connect to the customer storage account that is used to store the environment's data.
        :param pulumi.Input[Sequence[pulumi.Input['TimeSeriesIdPropertyArgs']]] time_series_id_properties: The list of event properties which will be used to define the environment's time series id.
        :param pulumi.Input[str] environment_name: Name of the environment
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: This value can be set to 'enabled' to avoid breaking changes on existing customer resources and templates. If set to 'disabled', traffic over public interface is not allowed, and private endpoint connections would be the exclusive access method.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value pairs of additional properties for the resource.
        :param pulumi.Input['WarmStoreConfigurationPropertiesArgs'] warm_store_configuration: The warm store configuration provides the details to create a warm store cache that will retain a copy of the environment's data available for faster query.
        """
        pulumi.set(__self__, "kind", 'Gen2')
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sku", sku)
        pulumi.set(__self__, "storage_configuration", storage_configuration)
        pulumi.set(__self__, "time_series_id_properties", time_series_id_properties)
        if environment_name is not None:
            pulumi.set(__self__, "environment_name", environment_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if public_network_access is None:
            public_network_access = 'enabled'
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if warm_store_configuration is not None:
            pulumi.set(__self__, "warm_store_configuration", warm_store_configuration)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        The kind of the environment.
        Expected value is 'Gen2'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of an Azure Resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Input['SkuArgs']:
        """
        The sku determines the type of environment, either Gen1 (S1 or S2) or Gen2 (L1). For Gen1 environments the sku determines the capacity of the environment, the ingress rate, and the billing rate.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input['SkuArgs']):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="storageConfiguration")
    def storage_configuration(self) -> pulumi.Input['Gen2StorageConfigurationInputArgs']:
        """
        The storage configuration provides the connection details that allows the Time Series Insights service to connect to the customer storage account that is used to store the environment's data.
        """
        return pulumi.get(self, "storage_configuration")

    @storage_configuration.setter
    def storage_configuration(self, value: pulumi.Input['Gen2StorageConfigurationInputArgs']):
        pulumi.set(self, "storage_configuration", value)

    @property
    @pulumi.getter(name="timeSeriesIdProperties")
    def time_series_id_properties(self) -> pulumi.Input[Sequence[pulumi.Input['TimeSeriesIdPropertyArgs']]]:
        """
        The list of event properties which will be used to define the environment's time series id.
        """
        return pulumi.get(self, "time_series_id_properties")

    @time_series_id_properties.setter
    def time_series_id_properties(self, value: pulumi.Input[Sequence[pulumi.Input['TimeSeriesIdPropertyArgs']]]):
        pulumi.set(self, "time_series_id_properties", value)

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the environment
        """
        return pulumi.get(self, "environment_name")

    @environment_name.setter
    def environment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]:
        """
        This value can be set to 'enabled' to avoid breaking changes on existing customer resources and templates. If set to 'disabled', traffic over public interface is not allowed, and private endpoint connections would be the exclusive access method.
        """
        return pulumi.get(self, "public_network_access")

    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]):
        pulumi.set(self, "public_network_access", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value pairs of additional properties for the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="warmStoreConfiguration")
    def warm_store_configuration(self) -> Optional[pulumi.Input['WarmStoreConfigurationPropertiesArgs']]:
        """
        The warm store configuration provides the details to create a warm store cache that will retain a copy of the environment's data available for faster query.
        """
        return pulumi.get(self, "warm_store_configuration")

    @warm_store_configuration.setter
    def warm_store_configuration(self, value: Optional[pulumi.Input['WarmStoreConfigurationPropertiesArgs']]):
        pulumi.set(self, "warm_store_configuration", value)


class Gen2Environment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 storage_configuration: Optional[pulumi.Input[pulumi.InputType['Gen2StorageConfigurationInputArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 time_series_id_properties: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TimeSeriesIdPropertyArgs']]]]] = None,
                 warm_store_configuration: Optional[pulumi.Input[pulumi.InputType['WarmStoreConfigurationPropertiesArgs']]] = None,
                 __props__=None):
        """
        An environment is a set of time-series data available for query, and is the top level Azure Time Series Insights resource. Gen2 environments do not have set data retention limits.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] environment_name: Name of the environment
        :param pulumi.Input[str] kind: The kind of the environment.
               Expected value is 'Gen2'.
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: This value can be set to 'enabled' to avoid breaking changes on existing customer resources and templates. If set to 'disabled', traffic over public interface is not allowed, and private endpoint connections would be the exclusive access method.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: The sku determines the type of environment, either Gen1 (S1 or S2) or Gen2 (L1). For Gen1 environments the sku determines the capacity of the environment, the ingress rate, and the billing rate.
        :param pulumi.Input[pulumi.InputType['Gen2StorageConfigurationInputArgs']] storage_configuration: The storage configuration provides the connection details that allows the Time Series Insights service to connect to the customer storage account that is used to store the environment's data.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value pairs of additional properties for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TimeSeriesIdPropertyArgs']]]] time_series_id_properties: The list of event properties which will be used to define the environment's time series id.
        :param pulumi.Input[pulumi.InputType['WarmStoreConfigurationPropertiesArgs']] warm_store_configuration: The warm store configuration provides the details to create a warm store cache that will retain a copy of the environment's data available for faster query.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Gen2EnvironmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An environment is a set of time-series data available for query, and is the top level Azure Time Series Insights resource. Gen2 environments do not have set data retention limits.

        :param str resource_name: The name of the resource.
        :param Gen2EnvironmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(Gen2EnvironmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 storage_configuration: Optional[pulumi.Input[pulumi.InputType['Gen2StorageConfigurationInputArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 time_series_id_properties: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TimeSeriesIdPropertyArgs']]]]] = None,
                 warm_store_configuration: Optional[pulumi.Input[pulumi.InputType['WarmStoreConfigurationPropertiesArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = Gen2EnvironmentArgs.__new__(Gen2EnvironmentArgs)

            __props__.__dict__["environment_name"] = environment_name
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'Gen2'
            __props__.__dict__["location"] = location
            if public_network_access is None:
                public_network_access = 'enabled'
            __props__.__dict__["public_network_access"] = public_network_access
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__.__dict__["sku"] = sku
            if storage_configuration is None and not opts.urn:
                raise TypeError("Missing required property 'storage_configuration'")
            __props__.__dict__["storage_configuration"] = storage_configuration
            __props__.__dict__["tags"] = tags
            if time_series_id_properties is None and not opts.urn:
                raise TypeError("Missing required property 'time_series_id_properties'")
            __props__.__dict__["time_series_id_properties"] = time_series_id_properties
            __props__.__dict__["warm_store_configuration"] = warm_store_configuration
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["data_access_fqdn"] = None
            __props__.__dict__["data_access_id"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["private_endpoint_connections"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:timeseriesinsights:Gen2Environment"), pulumi.Alias(type_="azure-native:timeseriesinsights/v20170228preview:Gen2Environment"), pulumi.Alias(type_="azure-native:timeseriesinsights/v20171115:Gen2Environment"), pulumi.Alias(type_="azure-native:timeseriesinsights/v20180815preview:Gen2Environment"), pulumi.Alias(type_="azure-native:timeseriesinsights/v20200515:Gen2Environment"), pulumi.Alias(type_="azure-native:timeseriesinsights/v20210630preview:Gen2Environment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Gen2Environment, __self__).__init__(
            'azure-native:timeseriesinsights/v20210331preview:Gen2Environment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Gen2Environment':
        """
        Get an existing Gen2Environment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = Gen2EnvironmentArgs.__new__(Gen2EnvironmentArgs)

        __props__.__dict__["creation_time"] = None
        __props__.__dict__["data_access_fqdn"] = None
        __props__.__dict__["data_access_id"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["private_endpoint_connections"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_network_access"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["storage_configuration"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["time_series_id_properties"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["warm_store_configuration"] = None
        return Gen2Environment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        The time the resource was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="dataAccessFqdn")
    def data_access_fqdn(self) -> pulumi.Output[str]:
        """
        The fully qualified domain name used to access the environment data, e.g. to query the environment's events or upload reference data for the environment.
        """
        return pulumi.get(self, "data_access_fqdn")

    @property
    @pulumi.getter(name="dataAccessId")
    def data_access_id(self) -> pulumi.Output[str]:
        """
        An id used to access the environment data, e.g. to query the environment's events or upload reference data for the environment.
        """
        return pulumi.get(self, "data_access_id")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The kind of the environment.
        Expected value is 'Gen2'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Sequence['outputs.PrivateEndpointConnectionResponse']]:
        """
        The list of private endpoint connections to the environment.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[str]]:
        """
        If 'enabled', public network access is allowed. If 'disabled', traffic over public interface is not allowed, and private endpoint connections would be the exclusive access method.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.SkuResponse']:
        """
        The sku determines the type of environment, either Gen1 (S1 or S2) or Gen2 (L1). For Gen1 environments the sku determines the capacity of the environment, the ingress rate, and the billing rate.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.EnvironmentStatusResponse']:
        """
        An object that represents the status of the environment, and its internal state in the Time Series Insights service.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageConfiguration")
    def storage_configuration(self) -> pulumi.Output['outputs.Gen2StorageConfigurationOutputResponse']:
        """
        The storage configuration provides the connection details that allows the Time Series Insights service to connect to the customer storage account that is used to store the environment's data.
        """
        return pulumi.get(self, "storage_configuration")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeSeriesIdProperties")
    def time_series_id_properties(self) -> pulumi.Output[Sequence['outputs.TimeSeriesIdPropertyResponse']]:
        """
        The list of event properties which will be used to define the environment's time series id.
        """
        return pulumi.get(self, "time_series_id_properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="warmStoreConfiguration")
    def warm_store_configuration(self) -> pulumi.Output[Optional['outputs.WarmStoreConfigurationPropertiesResponse']]:
        """
        The warm store configuration provides the details to create a warm store cache that will retain a copy of the environment's data available for faster query.
        """
        return pulumi.get(self, "warm_store_configuration")

