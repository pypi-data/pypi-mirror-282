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

__all__ = ['ServiceArgs', 'Service']

@pulumi.input_type
class ServiceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 auth_options: Optional[pulumi.Input['DataPlaneAuthOptionsArgs']] = None,
                 disable_local_auth: Optional[pulumi.Input[bool]] = None,
                 disabled_data_exfiltration_options: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'SearchDisabledDataExfiltrationOption']]]]] = None,
                 encryption_with_cmk: Optional[pulumi.Input['EncryptionWithCmkArgs']] = None,
                 hosting_mode: Optional[pulumi.Input['HostingMode']] = None,
                 identity: Optional[pulumi.Input['IdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_rule_set: Optional[pulumi.Input['NetworkRuleSetArgs']] = None,
                 partition_count: Optional[pulumi.Input[int]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 replica_count: Optional[pulumi.Input[int]] = None,
                 search_service_name: Optional[pulumi.Input[str]] = None,
                 semantic_search: Optional[pulumi.Input[Union[str, 'SearchSemanticSearch']]] = None,
                 sku: Optional[pulumi.Input['SkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Service resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the current subscription. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input['DataPlaneAuthOptionsArgs'] auth_options: Defines the options for how the data plane API of a search service authenticates requests. This cannot be set if 'disableLocalAuth' is set to true.
        :param pulumi.Input[bool] disable_local_auth: When set to true, calls to the search service will not be permitted to utilize API keys for authentication. This cannot be set to true if 'dataPlaneAuthOptions' are defined.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'SearchDisabledDataExfiltrationOption']]]] disabled_data_exfiltration_options: A list of data exfiltration scenarios that are explicitly disallowed for the search service. Currently, the only supported value is 'All' to disable all possible data export scenarios with more fine grained controls planned for the future.
        :param pulumi.Input['EncryptionWithCmkArgs'] encryption_with_cmk: Specifies any policy regarding encryption of resources (such as indexes) using customer manager keys within a search service.
        :param pulumi.Input['HostingMode'] hosting_mode: Applicable only for the standard3 SKU. You can set this property to enable up to 3 high density partitions that allow up to 1000 indexes, which is much higher than the maximum indexes allowed for any other SKU. For the standard3 SKU, the value is either 'default' or 'highDensity'. For all other SKUs, this value must be 'default'.
        :param pulumi.Input['IdentityArgs'] identity: The identity of the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['NetworkRuleSetArgs'] network_rule_set: Network specific rules that determine how the Azure AI Search service may be reached.
        :param pulumi.Input[int] partition_count: The number of partitions in the search service; if specified, it can be 1, 2, 3, 4, 6, or 12. Values greater than 1 are only valid for standard SKUs. For 'standard3' services with hostingMode set to 'highDensity', the allowed values are between 1 and 3.
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: This value can be set to 'enabled' to avoid breaking changes on existing customer resources and templates. If set to 'disabled', traffic over public interface is not allowed, and private endpoint connections would be the exclusive access method.
        :param pulumi.Input[int] replica_count: The number of replicas in the search service. If specified, it must be a value between 1 and 12 inclusive for standard SKUs or between 1 and 3 inclusive for basic SKU.
        :param pulumi.Input[str] search_service_name: The name of the Azure AI Search service to create or update. Search service names must only contain lowercase letters, digits or dashes, cannot use dash as the first two or last one characters, cannot contain consecutive dashes, and must be between 2 and 60 characters in length. Search service names must be globally unique since they are part of the service URI (https://<name>.search.windows.net). You cannot change the service name after the service is created.
        :param pulumi.Input[Union[str, 'SearchSemanticSearch']] semantic_search: Sets options that control the availability of semantic search. This configuration is only possible for certain Azure AI Search SKUs in certain locations.
        :param pulumi.Input['SkuArgs'] sku: The SKU of the search service, which determines price tier and capacity limits. This property is required when creating a new search service.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if auth_options is not None:
            pulumi.set(__self__, "auth_options", auth_options)
        if disable_local_auth is not None:
            pulumi.set(__self__, "disable_local_auth", disable_local_auth)
        if disabled_data_exfiltration_options is not None:
            pulumi.set(__self__, "disabled_data_exfiltration_options", disabled_data_exfiltration_options)
        if encryption_with_cmk is not None:
            pulumi.set(__self__, "encryption_with_cmk", encryption_with_cmk)
        if hosting_mode is None:
            hosting_mode = 'default'
        if hosting_mode is not None:
            pulumi.set(__self__, "hosting_mode", hosting_mode)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if network_rule_set is not None:
            pulumi.set(__self__, "network_rule_set", network_rule_set)
        if partition_count is None:
            partition_count = 1
        if partition_count is not None:
            pulumi.set(__self__, "partition_count", partition_count)
        if public_network_access is None:
            public_network_access = 'enabled'
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)
        if replica_count is None:
            replica_count = 1
        if replica_count is not None:
            pulumi.set(__self__, "replica_count", replica_count)
        if search_service_name is not None:
            pulumi.set(__self__, "search_service_name", search_service_name)
        if semantic_search is not None:
            pulumi.set(__self__, "semantic_search", semantic_search)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the current subscription. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="authOptions")
    def auth_options(self) -> Optional[pulumi.Input['DataPlaneAuthOptionsArgs']]:
        """
        Defines the options for how the data plane API of a search service authenticates requests. This cannot be set if 'disableLocalAuth' is set to true.
        """
        return pulumi.get(self, "auth_options")

    @auth_options.setter
    def auth_options(self, value: Optional[pulumi.Input['DataPlaneAuthOptionsArgs']]):
        pulumi.set(self, "auth_options", value)

    @property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[bool]]:
        """
        When set to true, calls to the search service will not be permitted to utilize API keys for authentication. This cannot be set to true if 'dataPlaneAuthOptions' are defined.
        """
        return pulumi.get(self, "disable_local_auth")

    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_local_auth", value)

    @property
    @pulumi.getter(name="disabledDataExfiltrationOptions")
    def disabled_data_exfiltration_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'SearchDisabledDataExfiltrationOption']]]]]:
        """
        A list of data exfiltration scenarios that are explicitly disallowed for the search service. Currently, the only supported value is 'All' to disable all possible data export scenarios with more fine grained controls planned for the future.
        """
        return pulumi.get(self, "disabled_data_exfiltration_options")

    @disabled_data_exfiltration_options.setter
    def disabled_data_exfiltration_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'SearchDisabledDataExfiltrationOption']]]]]):
        pulumi.set(self, "disabled_data_exfiltration_options", value)

    @property
    @pulumi.getter(name="encryptionWithCmk")
    def encryption_with_cmk(self) -> Optional[pulumi.Input['EncryptionWithCmkArgs']]:
        """
        Specifies any policy regarding encryption of resources (such as indexes) using customer manager keys within a search service.
        """
        return pulumi.get(self, "encryption_with_cmk")

    @encryption_with_cmk.setter
    def encryption_with_cmk(self, value: Optional[pulumi.Input['EncryptionWithCmkArgs']]):
        pulumi.set(self, "encryption_with_cmk", value)

    @property
    @pulumi.getter(name="hostingMode")
    def hosting_mode(self) -> Optional[pulumi.Input['HostingMode']]:
        """
        Applicable only for the standard3 SKU. You can set this property to enable up to 3 high density partitions that allow up to 1000 indexes, which is much higher than the maximum indexes allowed for any other SKU. For the standard3 SKU, the value is either 'default' or 'highDensity'. For all other SKUs, this value must be 'default'.
        """
        return pulumi.get(self, "hosting_mode")

    @hosting_mode.setter
    def hosting_mode(self, value: Optional[pulumi.Input['HostingMode']]):
        pulumi.set(self, "hosting_mode", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['IdentityArgs']]:
        """
        The identity of the resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['IdentityArgs']]):
        pulumi.set(self, "identity", value)

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
    @pulumi.getter(name="networkRuleSet")
    def network_rule_set(self) -> Optional[pulumi.Input['NetworkRuleSetArgs']]:
        """
        Network specific rules that determine how the Azure AI Search service may be reached.
        """
        return pulumi.get(self, "network_rule_set")

    @network_rule_set.setter
    def network_rule_set(self, value: Optional[pulumi.Input['NetworkRuleSetArgs']]):
        pulumi.set(self, "network_rule_set", value)

    @property
    @pulumi.getter(name="partitionCount")
    def partition_count(self) -> Optional[pulumi.Input[int]]:
        """
        The number of partitions in the search service; if specified, it can be 1, 2, 3, 4, 6, or 12. Values greater than 1 are only valid for standard SKUs. For 'standard3' services with hostingMode set to 'highDensity', the allowed values are between 1 and 3.
        """
        return pulumi.get(self, "partition_count")

    @partition_count.setter
    def partition_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "partition_count", value)

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
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[pulumi.Input[int]]:
        """
        The number of replicas in the search service. If specified, it must be a value between 1 and 12 inclusive for standard SKUs or between 1 and 3 inclusive for basic SKU.
        """
        return pulumi.get(self, "replica_count")

    @replica_count.setter
    def replica_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "replica_count", value)

    @property
    @pulumi.getter(name="searchServiceName")
    def search_service_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Azure AI Search service to create or update. Search service names must only contain lowercase letters, digits or dashes, cannot use dash as the first two or last one characters, cannot contain consecutive dashes, and must be between 2 and 60 characters in length. Search service names must be globally unique since they are part of the service URI (https://<name>.search.windows.net). You cannot change the service name after the service is created.
        """
        return pulumi.get(self, "search_service_name")

    @search_service_name.setter
    def search_service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "search_service_name", value)

    @property
    @pulumi.getter(name="semanticSearch")
    def semantic_search(self) -> Optional[pulumi.Input[Union[str, 'SearchSemanticSearch']]]:
        """
        Sets options that control the availability of semantic search. This configuration is only possible for certain Azure AI Search SKUs in certain locations.
        """
        return pulumi.get(self, "semantic_search")

    @semantic_search.setter
    def semantic_search(self, value: Optional[pulumi.Input[Union[str, 'SearchSemanticSearch']]]):
        pulumi.set(self, "semantic_search", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SkuArgs']]:
        """
        The SKU of the search service, which determines price tier and capacity limits. This property is required when creating a new search service.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuArgs']]):
        pulumi.set(self, "sku", value)

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


class Service(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_options: Optional[pulumi.Input[pulumi.InputType['DataPlaneAuthOptionsArgs']]] = None,
                 disable_local_auth: Optional[pulumi.Input[bool]] = None,
                 disabled_data_exfiltration_options: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'SearchDisabledDataExfiltrationOption']]]]] = None,
                 encryption_with_cmk: Optional[pulumi.Input[pulumi.InputType['EncryptionWithCmkArgs']]] = None,
                 hosting_mode: Optional[pulumi.Input['HostingMode']] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_rule_set: Optional[pulumi.Input[pulumi.InputType['NetworkRuleSetArgs']]] = None,
                 partition_count: Optional[pulumi.Input[int]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 replica_count: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 search_service_name: Optional[pulumi.Input[str]] = None,
                 semantic_search: Optional[pulumi.Input[Union[str, 'SearchSemanticSearch']]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Describes an Azure AI Search service and its current state.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['DataPlaneAuthOptionsArgs']] auth_options: Defines the options for how the data plane API of a search service authenticates requests. This cannot be set if 'disableLocalAuth' is set to true.
        :param pulumi.Input[bool] disable_local_auth: When set to true, calls to the search service will not be permitted to utilize API keys for authentication. This cannot be set to true if 'dataPlaneAuthOptions' are defined.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'SearchDisabledDataExfiltrationOption']]]] disabled_data_exfiltration_options: A list of data exfiltration scenarios that are explicitly disallowed for the search service. Currently, the only supported value is 'All' to disable all possible data export scenarios with more fine grained controls planned for the future.
        :param pulumi.Input[pulumi.InputType['EncryptionWithCmkArgs']] encryption_with_cmk: Specifies any policy regarding encryption of resources (such as indexes) using customer manager keys within a search service.
        :param pulumi.Input['HostingMode'] hosting_mode: Applicable only for the standard3 SKU. You can set this property to enable up to 3 high density partitions that allow up to 1000 indexes, which is much higher than the maximum indexes allowed for any other SKU. For the standard3 SKU, the value is either 'default' or 'highDensity'. For all other SKUs, this value must be 'default'.
        :param pulumi.Input[pulumi.InputType['IdentityArgs']] identity: The identity of the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[pulumi.InputType['NetworkRuleSetArgs']] network_rule_set: Network specific rules that determine how the Azure AI Search service may be reached.
        :param pulumi.Input[int] partition_count: The number of partitions in the search service; if specified, it can be 1, 2, 3, 4, 6, or 12. Values greater than 1 are only valid for standard SKUs. For 'standard3' services with hostingMode set to 'highDensity', the allowed values are between 1 and 3.
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: This value can be set to 'enabled' to avoid breaking changes on existing customer resources and templates. If set to 'disabled', traffic over public interface is not allowed, and private endpoint connections would be the exclusive access method.
        :param pulumi.Input[int] replica_count: The number of replicas in the search service. If specified, it must be a value between 1 and 12 inclusive for standard SKUs or between 1 and 3 inclusive for basic SKU.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the current subscription. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] search_service_name: The name of the Azure AI Search service to create or update. Search service names must only contain lowercase letters, digits or dashes, cannot use dash as the first two or last one characters, cannot contain consecutive dashes, and must be between 2 and 60 characters in length. Search service names must be globally unique since they are part of the service URI (https://<name>.search.windows.net). You cannot change the service name after the service is created.
        :param pulumi.Input[Union[str, 'SearchSemanticSearch']] semantic_search: Sets options that control the availability of semantic search. This configuration is only possible for certain Azure AI Search SKUs in certain locations.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: The SKU of the search service, which determines price tier and capacity limits. This property is required when creating a new search service.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServiceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Describes an Azure AI Search service and its current state.

        :param str resource_name: The name of the resource.
        :param ServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_options: Optional[pulumi.Input[pulumi.InputType['DataPlaneAuthOptionsArgs']]] = None,
                 disable_local_auth: Optional[pulumi.Input[bool]] = None,
                 disabled_data_exfiltration_options: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'SearchDisabledDataExfiltrationOption']]]]] = None,
                 encryption_with_cmk: Optional[pulumi.Input[pulumi.InputType['EncryptionWithCmkArgs']]] = None,
                 hosting_mode: Optional[pulumi.Input['HostingMode']] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_rule_set: Optional[pulumi.Input[pulumi.InputType['NetworkRuleSetArgs']]] = None,
                 partition_count: Optional[pulumi.Input[int]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 replica_count: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 search_service_name: Optional[pulumi.Input[str]] = None,
                 semantic_search: Optional[pulumi.Input[Union[str, 'SearchSemanticSearch']]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServiceArgs.__new__(ServiceArgs)

            __props__.__dict__["auth_options"] = auth_options
            __props__.__dict__["disable_local_auth"] = disable_local_auth
            __props__.__dict__["disabled_data_exfiltration_options"] = disabled_data_exfiltration_options
            __props__.__dict__["encryption_with_cmk"] = encryption_with_cmk
            if hosting_mode is None:
                hosting_mode = 'default'
            __props__.__dict__["hosting_mode"] = hosting_mode
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["network_rule_set"] = network_rule_set
            if partition_count is None:
                partition_count = 1
            __props__.__dict__["partition_count"] = partition_count
            if public_network_access is None:
                public_network_access = 'enabled'
            __props__.__dict__["public_network_access"] = public_network_access
            if replica_count is None:
                replica_count = 1
            __props__.__dict__["replica_count"] = replica_count
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["search_service_name"] = search_service_name
            __props__.__dict__["semantic_search"] = semantic_search
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["e_tag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["private_endpoint_connections"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["shared_private_link_resources"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["status_details"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:search:Service"), pulumi.Alias(type_="azure-native:search/v20150819:Service"), pulumi.Alias(type_="azure-native:search/v20191001preview:Service"), pulumi.Alias(type_="azure-native:search/v20200313:Service"), pulumi.Alias(type_="azure-native:search/v20200801:Service"), pulumi.Alias(type_="azure-native:search/v20200801preview:Service"), pulumi.Alias(type_="azure-native:search/v20210401preview:Service"), pulumi.Alias(type_="azure-native:search/v20220901:Service"), pulumi.Alias(type_="azure-native:search/v20231101:Service"), pulumi.Alias(type_="azure-native:search/v20240301preview:Service")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Service, __self__).__init__(
            'azure-native:search/v20240601preview:Service',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Service':
        """
        Get an existing Service resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServiceArgs.__new__(ServiceArgs)

        __props__.__dict__["auth_options"] = None
        __props__.__dict__["disable_local_auth"] = None
        __props__.__dict__["disabled_data_exfiltration_options"] = None
        __props__.__dict__["e_tag"] = None
        __props__.__dict__["encryption_with_cmk"] = None
        __props__.__dict__["hosting_mode"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_rule_set"] = None
        __props__.__dict__["partition_count"] = None
        __props__.__dict__["private_endpoint_connections"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_network_access"] = None
        __props__.__dict__["replica_count"] = None
        __props__.__dict__["semantic_search"] = None
        __props__.__dict__["shared_private_link_resources"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["status_details"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Service(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authOptions")
    def auth_options(self) -> pulumi.Output[Optional['outputs.DataPlaneAuthOptionsResponse']]:
        """
        Defines the options for how the data plane API of a search service authenticates requests. This cannot be set if 'disableLocalAuth' is set to true.
        """
        return pulumi.get(self, "auth_options")

    @property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> pulumi.Output[Optional[bool]]:
        """
        When set to true, calls to the search service will not be permitted to utilize API keys for authentication. This cannot be set to true if 'dataPlaneAuthOptions' are defined.
        """
        return pulumi.get(self, "disable_local_auth")

    @property
    @pulumi.getter(name="disabledDataExfiltrationOptions")
    def disabled_data_exfiltration_options(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of data exfiltration scenarios that are explicitly disallowed for the search service. Currently, the only supported value is 'All' to disable all possible data export scenarios with more fine grained controls planned for the future.
        """
        return pulumi.get(self, "disabled_data_exfiltration_options")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[str]:
        """
        A system generated property representing the service's etag that can be for optimistic concurrency control during updates.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter(name="encryptionWithCmk")
    def encryption_with_cmk(self) -> pulumi.Output[Optional['outputs.EncryptionWithCmkResponse']]:
        """
        Specifies any policy regarding encryption of resources (such as indexes) using customer manager keys within a search service.
        """
        return pulumi.get(self, "encryption_with_cmk")

    @property
    @pulumi.getter(name="hostingMode")
    def hosting_mode(self) -> pulumi.Output[Optional[str]]:
        """
        Applicable only for the standard3 SKU. You can set this property to enable up to 3 high density partitions that allow up to 1000 indexes, which is much higher than the maximum indexes allowed for any other SKU. For the standard3 SKU, the value is either 'default' or 'highDensity'. For all other SKUs, this value must be 'default'.
        """
        return pulumi.get(self, "hosting_mode")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityResponse']]:
        """
        The identity of the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
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
    @pulumi.getter(name="networkRuleSet")
    def network_rule_set(self) -> pulumi.Output[Optional['outputs.NetworkRuleSetResponse']]:
        """
        Network specific rules that determine how the Azure AI Search service may be reached.
        """
        return pulumi.get(self, "network_rule_set")

    @property
    @pulumi.getter(name="partitionCount")
    def partition_count(self) -> pulumi.Output[Optional[int]]:
        """
        The number of partitions in the search service; if specified, it can be 1, 2, 3, 4, 6, or 12. Values greater than 1 are only valid for standard SKUs. For 'standard3' services with hostingMode set to 'highDensity', the allowed values are between 1 and 3.
        """
        return pulumi.get(self, "partition_count")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Sequence['outputs.PrivateEndpointConnectionResponse']]:
        """
        The list of private endpoint connections to the Azure AI Search service.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The state of the last provisioning operation performed on the search service. Provisioning is an intermediate state that occurs while service capacity is being established. After capacity is set up, provisioningState changes to either 'Succeeded' or 'Failed'. Client applications can poll provisioning status (the recommended polling interval is from 30 seconds to one minute) by using the Get Search Service operation to see when an operation is completed. If you are using the free service, this value tends to come back as 'Succeeded' directly in the call to Create search service. This is because the free service uses capacity that is already set up.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[str]]:
        """
        This value can be set to 'enabled' to avoid breaking changes on existing customer resources and templates. If set to 'disabled', traffic over public interface is not allowed, and private endpoint connections would be the exclusive access method.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> pulumi.Output[Optional[int]]:
        """
        The number of replicas in the search service. If specified, it must be a value between 1 and 12 inclusive for standard SKUs or between 1 and 3 inclusive for basic SKU.
        """
        return pulumi.get(self, "replica_count")

    @property
    @pulumi.getter(name="semanticSearch")
    def semantic_search(self) -> pulumi.Output[Optional[str]]:
        """
        Sets options that control the availability of semantic search. This configuration is only possible for certain Azure AI Search SKUs in certain locations.
        """
        return pulumi.get(self, "semantic_search")

    @property
    @pulumi.getter(name="sharedPrivateLinkResources")
    def shared_private_link_resources(self) -> pulumi.Output[Sequence['outputs.SharedPrivateLinkResourceResponse']]:
        """
        The list of shared private link resources managed by the Azure AI Search service.
        """
        return pulumi.get(self, "shared_private_link_resources")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        The SKU of the search service, which determines price tier and capacity limits. This property is required when creating a new search service.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the search service. Possible values include: 'running': The search service is running and no provisioning operations are underway. 'provisioning': The search service is being provisioned or scaled up or down. 'deleting': The search service is being deleted. 'degraded': The search service is degraded. This can occur when the underlying search units are not healthy. The search service is most likely operational, but performance might be slow and some requests might be dropped. 'disabled': The search service is disabled. In this state, the service will reject all API requests. 'error': The search service is in an error state. 'stopped': The search service is in a subscription that's disabled. If your service is in the degraded, disabled, or error states, it means the Azure AI Search team is actively investigating the underlying issue. Dedicated services in these states are still chargeable based on the number of search units provisioned.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusDetails")
    def status_details(self) -> pulumi.Output[str]:
        """
        The details of the search service status.
        """
        return pulumi.get(self, "status_details")

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

