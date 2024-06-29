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

__all__ = ['ComponentArgs', 'Component']

@pulumi.input_type
class ComponentArgs:
    def __init__(__self__, *,
                 application_type: Optional[pulumi.Input[Union[str, 'ApplicationType']]] = None,
                 kind: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 disable_ip_masking: Optional[pulumi.Input[bool]] = None,
                 disable_local_auth: Optional[pulumi.Input[bool]] = None,
                 flow_type: Optional[pulumi.Input[Union[str, 'FlowType']]] = None,
                 force_customer_storage_for_profiler: Optional[pulumi.Input[bool]] = None,
                 hockey_app_id: Optional[pulumi.Input[str]] = None,
                 immediate_purge_data_on30_days: Optional[pulumi.Input[bool]] = None,
                 ingestion_mode: Optional[pulumi.Input[Union[str, 'IngestionMode']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_network_access_for_ingestion: Optional[pulumi.Input[Union[str, 'PublicNetworkAccessType']]] = None,
                 public_network_access_for_query: Optional[pulumi.Input[Union[str, 'PublicNetworkAccessType']]] = None,
                 request_source: Optional[pulumi.Input[Union[str, 'RequestSource']]] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 retention_in_days: Optional[pulumi.Input[int]] = None,
                 sampling_percentage: Optional[pulumi.Input[float]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_resource_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Component resource.
        :param pulumi.Input[Union[str, 'ApplicationType']] application_type: Type of application being monitored.
        :param pulumi.Input[str] kind: The kind of application that this component refers to, used to customize UI. This value is a freeform string, values should typically be one of the following: web, ios, other, store, java, phone.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[bool] disable_ip_masking: Disable IP masking.
        :param pulumi.Input[bool] disable_local_auth: Disable Non-AAD based Auth.
        :param pulumi.Input[Union[str, 'FlowType']] flow_type: Used by the Application Insights system to determine what kind of flow this component was created by. This is to be set to 'Bluefield' when creating/updating a component via the REST API.
        :param pulumi.Input[bool] force_customer_storage_for_profiler: Force users to create their own storage account for profiler and debugger.
        :param pulumi.Input[str] hockey_app_id: The unique application ID created when a new application is added to HockeyApp, used for communications with HockeyApp.
        :param pulumi.Input[bool] immediate_purge_data_on30_days: Purge data immediately after 30 days.
        :param pulumi.Input[Union[str, 'IngestionMode']] ingestion_mode: Indicates the flow of the ingestion.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[Union[str, 'PublicNetworkAccessType']] public_network_access_for_ingestion: The network access type for accessing Application Insights ingestion.
        :param pulumi.Input[Union[str, 'PublicNetworkAccessType']] public_network_access_for_query: The network access type for accessing Application Insights query.
        :param pulumi.Input[Union[str, 'RequestSource']] request_source: Describes what tool created this Application Insights component. Customers using this API should set this to the default 'rest'.
        :param pulumi.Input[str] resource_name: The name of the Application Insights component resource.
        :param pulumi.Input[int] retention_in_days: Retention period in days.
        :param pulumi.Input[float] sampling_percentage: Percentage of the data produced by the application being monitored that is being sampled for Application Insights telemetry.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] workspace_resource_id: Resource Id of the log analytics workspace which the data will be ingested to. This property is required to create an application with this API version. Applications from older versions will not have this property.
        """
        if application_type is None:
            application_type = 'web'
        pulumi.set(__self__, "application_type", application_type)
        pulumi.set(__self__, "kind", kind)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if disable_ip_masking is not None:
            pulumi.set(__self__, "disable_ip_masking", disable_ip_masking)
        if disable_local_auth is not None:
            pulumi.set(__self__, "disable_local_auth", disable_local_auth)
        if flow_type is None:
            flow_type = 'Bluefield'
        if flow_type is not None:
            pulumi.set(__self__, "flow_type", flow_type)
        if force_customer_storage_for_profiler is not None:
            pulumi.set(__self__, "force_customer_storage_for_profiler", force_customer_storage_for_profiler)
        if hockey_app_id is not None:
            pulumi.set(__self__, "hockey_app_id", hockey_app_id)
        if immediate_purge_data_on30_days is not None:
            pulumi.set(__self__, "immediate_purge_data_on30_days", immediate_purge_data_on30_days)
        if ingestion_mode is None:
            ingestion_mode = 'LogAnalytics'
        if ingestion_mode is not None:
            pulumi.set(__self__, "ingestion_mode", ingestion_mode)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if public_network_access_for_ingestion is not None:
            pulumi.set(__self__, "public_network_access_for_ingestion", public_network_access_for_ingestion)
        if public_network_access_for_query is not None:
            pulumi.set(__self__, "public_network_access_for_query", public_network_access_for_query)
        if request_source is None:
            request_source = 'rest'
        if request_source is not None:
            pulumi.set(__self__, "request_source", request_source)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if retention_in_days is not None:
            pulumi.set(__self__, "retention_in_days", retention_in_days)
        if sampling_percentage is not None:
            pulumi.set(__self__, "sampling_percentage", sampling_percentage)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if workspace_resource_id is not None:
            pulumi.set(__self__, "workspace_resource_id", workspace_resource_id)

    @property
    @pulumi.getter(name="applicationType")
    def application_type(self) -> pulumi.Input[Union[str, 'ApplicationType']]:
        """
        Type of application being monitored.
        """
        return pulumi.get(self, "application_type")

    @application_type.setter
    def application_type(self, value: pulumi.Input[Union[str, 'ApplicationType']]):
        pulumi.set(self, "application_type", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        The kind of application that this component refers to, used to customize UI. This value is a freeform string, values should typically be one of the following: web, ios, other, store, java, phone.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

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
    @pulumi.getter(name="disableIpMasking")
    def disable_ip_masking(self) -> Optional[pulumi.Input[bool]]:
        """
        Disable IP masking.
        """
        return pulumi.get(self, "disable_ip_masking")

    @disable_ip_masking.setter
    def disable_ip_masking(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_ip_masking", value)

    @property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[bool]]:
        """
        Disable Non-AAD based Auth.
        """
        return pulumi.get(self, "disable_local_auth")

    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_local_auth", value)

    @property
    @pulumi.getter(name="flowType")
    def flow_type(self) -> Optional[pulumi.Input[Union[str, 'FlowType']]]:
        """
        Used by the Application Insights system to determine what kind of flow this component was created by. This is to be set to 'Bluefield' when creating/updating a component via the REST API.
        """
        return pulumi.get(self, "flow_type")

    @flow_type.setter
    def flow_type(self, value: Optional[pulumi.Input[Union[str, 'FlowType']]]):
        pulumi.set(self, "flow_type", value)

    @property
    @pulumi.getter(name="forceCustomerStorageForProfiler")
    def force_customer_storage_for_profiler(self) -> Optional[pulumi.Input[bool]]:
        """
        Force users to create their own storage account for profiler and debugger.
        """
        return pulumi.get(self, "force_customer_storage_for_profiler")

    @force_customer_storage_for_profiler.setter
    def force_customer_storage_for_profiler(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_customer_storage_for_profiler", value)

    @property
    @pulumi.getter(name="hockeyAppId")
    def hockey_app_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique application ID created when a new application is added to HockeyApp, used for communications with HockeyApp.
        """
        return pulumi.get(self, "hockey_app_id")

    @hockey_app_id.setter
    def hockey_app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hockey_app_id", value)

    @property
    @pulumi.getter(name="immediatePurgeDataOn30Days")
    def immediate_purge_data_on30_days(self) -> Optional[pulumi.Input[bool]]:
        """
        Purge data immediately after 30 days.
        """
        return pulumi.get(self, "immediate_purge_data_on30_days")

    @immediate_purge_data_on30_days.setter
    def immediate_purge_data_on30_days(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "immediate_purge_data_on30_days", value)

    @property
    @pulumi.getter(name="ingestionMode")
    def ingestion_mode(self) -> Optional[pulumi.Input[Union[str, 'IngestionMode']]]:
        """
        Indicates the flow of the ingestion.
        """
        return pulumi.get(self, "ingestion_mode")

    @ingestion_mode.setter
    def ingestion_mode(self, value: Optional[pulumi.Input[Union[str, 'IngestionMode']]]):
        pulumi.set(self, "ingestion_mode", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="publicNetworkAccessForIngestion")
    def public_network_access_for_ingestion(self) -> Optional[pulumi.Input[Union[str, 'PublicNetworkAccessType']]]:
        """
        The network access type for accessing Application Insights ingestion.
        """
        return pulumi.get(self, "public_network_access_for_ingestion")

    @public_network_access_for_ingestion.setter
    def public_network_access_for_ingestion(self, value: Optional[pulumi.Input[Union[str, 'PublicNetworkAccessType']]]):
        pulumi.set(self, "public_network_access_for_ingestion", value)

    @property
    @pulumi.getter(name="publicNetworkAccessForQuery")
    def public_network_access_for_query(self) -> Optional[pulumi.Input[Union[str, 'PublicNetworkAccessType']]]:
        """
        The network access type for accessing Application Insights query.
        """
        return pulumi.get(self, "public_network_access_for_query")

    @public_network_access_for_query.setter
    def public_network_access_for_query(self, value: Optional[pulumi.Input[Union[str, 'PublicNetworkAccessType']]]):
        pulumi.set(self, "public_network_access_for_query", value)

    @property
    @pulumi.getter(name="requestSource")
    def request_source(self) -> Optional[pulumi.Input[Union[str, 'RequestSource']]]:
        """
        Describes what tool created this Application Insights component. Customers using this API should set this to the default 'rest'.
        """
        return pulumi.get(self, "request_source")

    @request_source.setter
    def request_source(self, value: Optional[pulumi.Input[Union[str, 'RequestSource']]]):
        pulumi.set(self, "request_source", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Application Insights component resource.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> Optional[pulumi.Input[int]]:
        """
        Retention period in days.
        """
        return pulumi.get(self, "retention_in_days")

    @retention_in_days.setter
    def retention_in_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retention_in_days", value)

    @property
    @pulumi.getter(name="samplingPercentage")
    def sampling_percentage(self) -> Optional[pulumi.Input[float]]:
        """
        Percentage of the data produced by the application being monitored that is being sampled for Application Insights telemetry.
        """
        return pulumi.get(self, "sampling_percentage")

    @sampling_percentage.setter
    def sampling_percentage(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "sampling_percentage", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="workspaceResourceId")
    def workspace_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Id of the log analytics workspace which the data will be ingested to. This property is required to create an application with this API version. Applications from older versions will not have this property.
        """
        return pulumi.get(self, "workspace_resource_id")

    @workspace_resource_id.setter
    def workspace_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace_resource_id", value)


class Component(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_type: Optional[pulumi.Input[Union[str, 'ApplicationType']]] = None,
                 disable_ip_masking: Optional[pulumi.Input[bool]] = None,
                 disable_local_auth: Optional[pulumi.Input[bool]] = None,
                 flow_type: Optional[pulumi.Input[Union[str, 'FlowType']]] = None,
                 force_customer_storage_for_profiler: Optional[pulumi.Input[bool]] = None,
                 hockey_app_id: Optional[pulumi.Input[str]] = None,
                 immediate_purge_data_on30_days: Optional[pulumi.Input[bool]] = None,
                 ingestion_mode: Optional[pulumi.Input[Union[str, 'IngestionMode']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_network_access_for_ingestion: Optional[pulumi.Input[Union[str, 'PublicNetworkAccessType']]] = None,
                 public_network_access_for_query: Optional[pulumi.Input[Union[str, 'PublicNetworkAccessType']]] = None,
                 request_source: Optional[pulumi.Input[Union[str, 'RequestSource']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 retention_in_days: Optional[pulumi.Input[int]] = None,
                 sampling_percentage: Optional[pulumi.Input[float]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An Application Insights component definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'ApplicationType']] application_type: Type of application being monitored.
        :param pulumi.Input[bool] disable_ip_masking: Disable IP masking.
        :param pulumi.Input[bool] disable_local_auth: Disable Non-AAD based Auth.
        :param pulumi.Input[Union[str, 'FlowType']] flow_type: Used by the Application Insights system to determine what kind of flow this component was created by. This is to be set to 'Bluefield' when creating/updating a component via the REST API.
        :param pulumi.Input[bool] force_customer_storage_for_profiler: Force users to create their own storage account for profiler and debugger.
        :param pulumi.Input[str] hockey_app_id: The unique application ID created when a new application is added to HockeyApp, used for communications with HockeyApp.
        :param pulumi.Input[bool] immediate_purge_data_on30_days: Purge data immediately after 30 days.
        :param pulumi.Input[Union[str, 'IngestionMode']] ingestion_mode: Indicates the flow of the ingestion.
        :param pulumi.Input[str] kind: The kind of application that this component refers to, used to customize UI. This value is a freeform string, values should typically be one of the following: web, ios, other, store, java, phone.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[Union[str, 'PublicNetworkAccessType']] public_network_access_for_ingestion: The network access type for accessing Application Insights ingestion.
        :param pulumi.Input[Union[str, 'PublicNetworkAccessType']] public_network_access_for_query: The network access type for accessing Application Insights query.
        :param pulumi.Input[Union[str, 'RequestSource']] request_source: Describes what tool created this Application Insights component. Customers using this API should set this to the default 'rest'.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name_: The name of the Application Insights component resource.
        :param pulumi.Input[int] retention_in_days: Retention period in days.
        :param pulumi.Input[float] sampling_percentage: Percentage of the data produced by the application being monitored that is being sampled for Application Insights telemetry.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] workspace_resource_id: Resource Id of the log analytics workspace which the data will be ingested to. This property is required to create an application with this API version. Applications from older versions will not have this property.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ComponentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Application Insights component definition.

        :param str resource_name: The name of the resource.
        :param ComponentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ComponentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_type: Optional[pulumi.Input[Union[str, 'ApplicationType']]] = None,
                 disable_ip_masking: Optional[pulumi.Input[bool]] = None,
                 disable_local_auth: Optional[pulumi.Input[bool]] = None,
                 flow_type: Optional[pulumi.Input[Union[str, 'FlowType']]] = None,
                 force_customer_storage_for_profiler: Optional[pulumi.Input[bool]] = None,
                 hockey_app_id: Optional[pulumi.Input[str]] = None,
                 immediate_purge_data_on30_days: Optional[pulumi.Input[bool]] = None,
                 ingestion_mode: Optional[pulumi.Input[Union[str, 'IngestionMode']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_network_access_for_ingestion: Optional[pulumi.Input[Union[str, 'PublicNetworkAccessType']]] = None,
                 public_network_access_for_query: Optional[pulumi.Input[Union[str, 'PublicNetworkAccessType']]] = None,
                 request_source: Optional[pulumi.Input[Union[str, 'RequestSource']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 retention_in_days: Optional[pulumi.Input[int]] = None,
                 sampling_percentage: Optional[pulumi.Input[float]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ComponentArgs.__new__(ComponentArgs)

            if application_type is None:
                application_type = 'web'
            if application_type is None and not opts.urn:
                raise TypeError("Missing required property 'application_type'")
            __props__.__dict__["application_type"] = application_type
            __props__.__dict__["disable_ip_masking"] = disable_ip_masking
            __props__.__dict__["disable_local_auth"] = disable_local_auth
            if flow_type is None:
                flow_type = 'Bluefield'
            __props__.__dict__["flow_type"] = flow_type
            __props__.__dict__["force_customer_storage_for_profiler"] = force_customer_storage_for_profiler
            __props__.__dict__["hockey_app_id"] = hockey_app_id
            __props__.__dict__["immediate_purge_data_on30_days"] = immediate_purge_data_on30_days
            if ingestion_mode is None:
                ingestion_mode = 'LogAnalytics'
            __props__.__dict__["ingestion_mode"] = ingestion_mode
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            __props__.__dict__["public_network_access_for_ingestion"] = public_network_access_for_ingestion
            __props__.__dict__["public_network_access_for_query"] = public_network_access_for_query
            if request_source is None:
                request_source = 'rest'
            __props__.__dict__["request_source"] = request_source
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["retention_in_days"] = retention_in_days
            __props__.__dict__["sampling_percentage"] = sampling_percentage
            __props__.__dict__["tags"] = tags
            __props__.__dict__["workspace_resource_id"] = workspace_resource_id
            __props__.__dict__["app_id"] = None
            __props__.__dict__["application_id"] = None
            __props__.__dict__["connection_string"] = None
            __props__.__dict__["creation_date"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["hockey_app_token"] = None
            __props__.__dict__["instrumentation_key"] = None
            __props__.__dict__["la_migration_date"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["private_link_scoped_resources"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["tenant_id"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:insights:Component"), pulumi.Alias(type_="azure-native:insights/v20150501:Component"), pulumi.Alias(type_="azure-native:insights/v20180501preview:Component"), pulumi.Alias(type_="azure-native:insights/v20200202preview:Component")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Component, __self__).__init__(
            'azure-native:insights/v20200202:Component',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Component':
        """
        Get an existing Component resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ComponentArgs.__new__(ComponentArgs)

        __props__.__dict__["app_id"] = None
        __props__.__dict__["application_id"] = None
        __props__.__dict__["application_type"] = None
        __props__.__dict__["connection_string"] = None
        __props__.__dict__["creation_date"] = None
        __props__.__dict__["disable_ip_masking"] = None
        __props__.__dict__["disable_local_auth"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["flow_type"] = None
        __props__.__dict__["force_customer_storage_for_profiler"] = None
        __props__.__dict__["hockey_app_id"] = None
        __props__.__dict__["hockey_app_token"] = None
        __props__.__dict__["immediate_purge_data_on30_days"] = None
        __props__.__dict__["ingestion_mode"] = None
        __props__.__dict__["instrumentation_key"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["la_migration_date"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["private_link_scoped_resources"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_network_access_for_ingestion"] = None
        __props__.__dict__["public_network_access_for_query"] = None
        __props__.__dict__["request_source"] = None
        __props__.__dict__["retention_in_days"] = None
        __props__.__dict__["sampling_percentage"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["tenant_id"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["workspace_resource_id"] = None
        return Component(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[str]:
        """
        Application Insights Unique ID for your Application.
        """
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[str]:
        """
        The unique ID of your application. This field mirrors the 'Name' field and cannot be changed.
        """
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter(name="applicationType")
    def application_type(self) -> pulumi.Output[str]:
        """
        Type of application being monitored.
        """
        return pulumi.get(self, "application_type")

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> pulumi.Output[str]:
        """
        Application Insights component connection string.
        """
        return pulumi.get(self, "connection_string")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[str]:
        """
        Creation Date for the Application Insights component, in ISO 8601 format.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter(name="disableIpMasking")
    def disable_ip_masking(self) -> pulumi.Output[Optional[bool]]:
        """
        Disable IP masking.
        """
        return pulumi.get(self, "disable_ip_masking")

    @property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> pulumi.Output[Optional[bool]]:
        """
        Disable Non-AAD based Auth.
        """
        return pulumi.get(self, "disable_local_auth")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Resource etag
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="flowType")
    def flow_type(self) -> pulumi.Output[Optional[str]]:
        """
        Used by the Application Insights system to determine what kind of flow this component was created by. This is to be set to 'Bluefield' when creating/updating a component via the REST API.
        """
        return pulumi.get(self, "flow_type")

    @property
    @pulumi.getter(name="forceCustomerStorageForProfiler")
    def force_customer_storage_for_profiler(self) -> pulumi.Output[Optional[bool]]:
        """
        Force users to create their own storage account for profiler and debugger.
        """
        return pulumi.get(self, "force_customer_storage_for_profiler")

    @property
    @pulumi.getter(name="hockeyAppId")
    def hockey_app_id(self) -> pulumi.Output[Optional[str]]:
        """
        The unique application ID created when a new application is added to HockeyApp, used for communications with HockeyApp.
        """
        return pulumi.get(self, "hockey_app_id")

    @property
    @pulumi.getter(name="hockeyAppToken")
    def hockey_app_token(self) -> pulumi.Output[str]:
        """
        Token used to authenticate communications with between Application Insights and HockeyApp.
        """
        return pulumi.get(self, "hockey_app_token")

    @property
    @pulumi.getter(name="immediatePurgeDataOn30Days")
    def immediate_purge_data_on30_days(self) -> pulumi.Output[Optional[bool]]:
        """
        Purge data immediately after 30 days.
        """
        return pulumi.get(self, "immediate_purge_data_on30_days")

    @property
    @pulumi.getter(name="ingestionMode")
    def ingestion_mode(self) -> pulumi.Output[Optional[str]]:
        """
        Indicates the flow of the ingestion.
        """
        return pulumi.get(self, "ingestion_mode")

    @property
    @pulumi.getter(name="instrumentationKey")
    def instrumentation_key(self) -> pulumi.Output[str]:
        """
        Application Insights Instrumentation key. A read-only value that applications can use to identify the destination for all telemetry sent to Azure Application Insights. This value will be supplied upon construction of each new Application Insights component.
        """
        return pulumi.get(self, "instrumentation_key")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The kind of application that this component refers to, used to customize UI. This value is a freeform string, values should typically be one of the following: web, ios, other, store, java, phone.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="laMigrationDate")
    def la_migration_date(self) -> pulumi.Output[str]:
        """
        The date which the component got migrated to LA, in ISO 8601 format.
        """
        return pulumi.get(self, "la_migration_date")

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
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateLinkScopedResources")
    def private_link_scoped_resources(self) -> pulumi.Output[Sequence['outputs.PrivateLinkScopedResourceResponse']]:
        """
        List of linked private link scope resources.
        """
        return pulumi.get(self, "private_link_scoped_resources")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Current state of this component: whether or not is has been provisioned within the resource group it is defined. Users cannot change this value but are able to read from it. Values will include Succeeded, Deploying, Canceled, and Failed.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccessForIngestion")
    def public_network_access_for_ingestion(self) -> pulumi.Output[Optional[str]]:
        """
        The network access type for accessing Application Insights ingestion.
        """
        return pulumi.get(self, "public_network_access_for_ingestion")

    @property
    @pulumi.getter(name="publicNetworkAccessForQuery")
    def public_network_access_for_query(self) -> pulumi.Output[Optional[str]]:
        """
        The network access type for accessing Application Insights query.
        """
        return pulumi.get(self, "public_network_access_for_query")

    @property
    @pulumi.getter(name="requestSource")
    def request_source(self) -> pulumi.Output[Optional[str]]:
        """
        Describes what tool created this Application Insights component. Customers using this API should set this to the default 'rest'.
        """
        return pulumi.get(self, "request_source")

    @property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> pulumi.Output[Optional[int]]:
        """
        Retention period in days.
        """
        return pulumi.get(self, "retention_in_days")

    @property
    @pulumi.getter(name="samplingPercentage")
    def sampling_percentage(self) -> pulumi.Output[Optional[float]]:
        """
        Percentage of the data produced by the application being monitored that is being sampled for Application Insights telemetry.
        """
        return pulumi.get(self, "sampling_percentage")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        Azure Tenant Id.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="workspaceResourceId")
    def workspace_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        Resource Id of the log analytics workspace which the data will be ingested to. This property is required to create an application with this API version. Applications from older versions will not have this property.
        """
        return pulumi.get(self, "workspace_resource_id")

