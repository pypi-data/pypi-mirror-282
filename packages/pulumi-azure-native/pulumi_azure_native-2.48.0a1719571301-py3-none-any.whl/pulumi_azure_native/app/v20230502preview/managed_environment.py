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

__all__ = ['ManagedEnvironmentArgs', 'ManagedEnvironment']

@pulumi.input_type
class ManagedEnvironmentArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 app_logs_configuration: Optional[pulumi.Input['AppLogsConfigurationArgs']] = None,
                 custom_domain_configuration: Optional[pulumi.Input['CustomDomainConfigurationArgs']] = None,
                 dapr_ai_connection_string: Optional[pulumi.Input[str]] = None,
                 dapr_ai_instrumentation_key: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 infrastructure_resource_group: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 peer_authentication: Optional[pulumi.Input['ManagedEnvironmentPeerAuthenticationArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vnet_configuration: Optional[pulumi.Input['VnetConfigurationArgs']] = None,
                 workload_profiles: Optional[pulumi.Input[Sequence[pulumi.Input['WorkloadProfileArgs']]]] = None,
                 zone_redundant: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a ManagedEnvironment resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['AppLogsConfigurationArgs'] app_logs_configuration: Cluster configuration which enables the log daemon to export
               app logs to a destination. Currently only "log-analytics" is
               supported
        :param pulumi.Input['CustomDomainConfigurationArgs'] custom_domain_configuration: Custom domain configuration for the environment
        :param pulumi.Input[str] dapr_ai_connection_string: Application Insights connection string used by Dapr to export Service to Service communication telemetry
        :param pulumi.Input[str] dapr_ai_instrumentation_key: Azure Monitor instrumentation key used by Dapr to export Service to Service communication telemetry
        :param pulumi.Input[str] environment_name: Name of the Environment.
        :param pulumi.Input[str] infrastructure_resource_group: Name of the platform-managed resource group created for the Managed Environment to host infrastructure resources. If a subnet ID is provided, this resource group will be created in the same subscription as the subnet.
        :param pulumi.Input[str] kind: Kind of the Environment.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['ManagedEnvironmentPeerAuthenticationArgs'] peer_authentication: Peer authentication settings for the Managed Environment
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input['VnetConfigurationArgs'] vnet_configuration: Vnet configuration for the environment
        :param pulumi.Input[Sequence[pulumi.Input['WorkloadProfileArgs']]] workload_profiles: Workload profiles configured for the Managed Environment.
        :param pulumi.Input[bool] zone_redundant: Whether or not this Managed Environment is zone-redundant.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if app_logs_configuration is not None:
            pulumi.set(__self__, "app_logs_configuration", app_logs_configuration)
        if custom_domain_configuration is not None:
            pulumi.set(__self__, "custom_domain_configuration", custom_domain_configuration)
        if dapr_ai_connection_string is not None:
            pulumi.set(__self__, "dapr_ai_connection_string", dapr_ai_connection_string)
        if dapr_ai_instrumentation_key is not None:
            pulumi.set(__self__, "dapr_ai_instrumentation_key", dapr_ai_instrumentation_key)
        if environment_name is not None:
            pulumi.set(__self__, "environment_name", environment_name)
        if infrastructure_resource_group is not None:
            pulumi.set(__self__, "infrastructure_resource_group", infrastructure_resource_group)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if peer_authentication is not None:
            pulumi.set(__self__, "peer_authentication", peer_authentication)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vnet_configuration is not None:
            pulumi.set(__self__, "vnet_configuration", vnet_configuration)
        if workload_profiles is not None:
            pulumi.set(__self__, "workload_profiles", workload_profiles)
        if zone_redundant is not None:
            pulumi.set(__self__, "zone_redundant", zone_redundant)

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
    @pulumi.getter(name="appLogsConfiguration")
    def app_logs_configuration(self) -> Optional[pulumi.Input['AppLogsConfigurationArgs']]:
        """
        Cluster configuration which enables the log daemon to export
        app logs to a destination. Currently only "log-analytics" is
        supported
        """
        return pulumi.get(self, "app_logs_configuration")

    @app_logs_configuration.setter
    def app_logs_configuration(self, value: Optional[pulumi.Input['AppLogsConfigurationArgs']]):
        pulumi.set(self, "app_logs_configuration", value)

    @property
    @pulumi.getter(name="customDomainConfiguration")
    def custom_domain_configuration(self) -> Optional[pulumi.Input['CustomDomainConfigurationArgs']]:
        """
        Custom domain configuration for the environment
        """
        return pulumi.get(self, "custom_domain_configuration")

    @custom_domain_configuration.setter
    def custom_domain_configuration(self, value: Optional[pulumi.Input['CustomDomainConfigurationArgs']]):
        pulumi.set(self, "custom_domain_configuration", value)

    @property
    @pulumi.getter(name="daprAIConnectionString")
    def dapr_ai_connection_string(self) -> Optional[pulumi.Input[str]]:
        """
        Application Insights connection string used by Dapr to export Service to Service communication telemetry
        """
        return pulumi.get(self, "dapr_ai_connection_string")

    @dapr_ai_connection_string.setter
    def dapr_ai_connection_string(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dapr_ai_connection_string", value)

    @property
    @pulumi.getter(name="daprAIInstrumentationKey")
    def dapr_ai_instrumentation_key(self) -> Optional[pulumi.Input[str]]:
        """
        Azure Monitor instrumentation key used by Dapr to export Service to Service communication telemetry
        """
        return pulumi.get(self, "dapr_ai_instrumentation_key")

    @dapr_ai_instrumentation_key.setter
    def dapr_ai_instrumentation_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dapr_ai_instrumentation_key", value)

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Environment.
        """
        return pulumi.get(self, "environment_name")

    @environment_name.setter
    def environment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment_name", value)

    @property
    @pulumi.getter(name="infrastructureResourceGroup")
    def infrastructure_resource_group(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the platform-managed resource group created for the Managed Environment to host infrastructure resources. If a subnet ID is provided, this resource group will be created in the same subscription as the subnet.
        """
        return pulumi.get(self, "infrastructure_resource_group")

    @infrastructure_resource_group.setter
    def infrastructure_resource_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "infrastructure_resource_group", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of the Environment.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

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
    @pulumi.getter(name="peerAuthentication")
    def peer_authentication(self) -> Optional[pulumi.Input['ManagedEnvironmentPeerAuthenticationArgs']]:
        """
        Peer authentication settings for the Managed Environment
        """
        return pulumi.get(self, "peer_authentication")

    @peer_authentication.setter
    def peer_authentication(self, value: Optional[pulumi.Input['ManagedEnvironmentPeerAuthenticationArgs']]):
        pulumi.set(self, "peer_authentication", value)

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
    @pulumi.getter(name="vnetConfiguration")
    def vnet_configuration(self) -> Optional[pulumi.Input['VnetConfigurationArgs']]:
        """
        Vnet configuration for the environment
        """
        return pulumi.get(self, "vnet_configuration")

    @vnet_configuration.setter
    def vnet_configuration(self, value: Optional[pulumi.Input['VnetConfigurationArgs']]):
        pulumi.set(self, "vnet_configuration", value)

    @property
    @pulumi.getter(name="workloadProfiles")
    def workload_profiles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WorkloadProfileArgs']]]]:
        """
        Workload profiles configured for the Managed Environment.
        """
        return pulumi.get(self, "workload_profiles")

    @workload_profiles.setter
    def workload_profiles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WorkloadProfileArgs']]]]):
        pulumi.set(self, "workload_profiles", value)

    @property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not this Managed Environment is zone-redundant.
        """
        return pulumi.get(self, "zone_redundant")

    @zone_redundant.setter
    def zone_redundant(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "zone_redundant", value)


class ManagedEnvironment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_logs_configuration: Optional[pulumi.Input[pulumi.InputType['AppLogsConfigurationArgs']]] = None,
                 custom_domain_configuration: Optional[pulumi.Input[pulumi.InputType['CustomDomainConfigurationArgs']]] = None,
                 dapr_ai_connection_string: Optional[pulumi.Input[str]] = None,
                 dapr_ai_instrumentation_key: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 infrastructure_resource_group: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 peer_authentication: Optional[pulumi.Input[pulumi.InputType['ManagedEnvironmentPeerAuthenticationArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vnet_configuration: Optional[pulumi.Input[pulumi.InputType['VnetConfigurationArgs']]] = None,
                 workload_profiles: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkloadProfileArgs']]]]] = None,
                 zone_redundant: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        An environment for hosting container apps

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AppLogsConfigurationArgs']] app_logs_configuration: Cluster configuration which enables the log daemon to export
               app logs to a destination. Currently only "log-analytics" is
               supported
        :param pulumi.Input[pulumi.InputType['CustomDomainConfigurationArgs']] custom_domain_configuration: Custom domain configuration for the environment
        :param pulumi.Input[str] dapr_ai_connection_string: Application Insights connection string used by Dapr to export Service to Service communication telemetry
        :param pulumi.Input[str] dapr_ai_instrumentation_key: Azure Monitor instrumentation key used by Dapr to export Service to Service communication telemetry
        :param pulumi.Input[str] environment_name: Name of the Environment.
        :param pulumi.Input[str] infrastructure_resource_group: Name of the platform-managed resource group created for the Managed Environment to host infrastructure resources. If a subnet ID is provided, this resource group will be created in the same subscription as the subnet.
        :param pulumi.Input[str] kind: Kind of the Environment.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[pulumi.InputType['ManagedEnvironmentPeerAuthenticationArgs']] peer_authentication: Peer authentication settings for the Managed Environment
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[pulumi.InputType['VnetConfigurationArgs']] vnet_configuration: Vnet configuration for the environment
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkloadProfileArgs']]]] workload_profiles: Workload profiles configured for the Managed Environment.
        :param pulumi.Input[bool] zone_redundant: Whether or not this Managed Environment is zone-redundant.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagedEnvironmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An environment for hosting container apps

        :param str resource_name: The name of the resource.
        :param ManagedEnvironmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagedEnvironmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_logs_configuration: Optional[pulumi.Input[pulumi.InputType['AppLogsConfigurationArgs']]] = None,
                 custom_domain_configuration: Optional[pulumi.Input[pulumi.InputType['CustomDomainConfigurationArgs']]] = None,
                 dapr_ai_connection_string: Optional[pulumi.Input[str]] = None,
                 dapr_ai_instrumentation_key: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 infrastructure_resource_group: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 peer_authentication: Optional[pulumi.Input[pulumi.InputType['ManagedEnvironmentPeerAuthenticationArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vnet_configuration: Optional[pulumi.Input[pulumi.InputType['VnetConfigurationArgs']]] = None,
                 workload_profiles: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkloadProfileArgs']]]]] = None,
                 zone_redundant: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ManagedEnvironmentArgs.__new__(ManagedEnvironmentArgs)

            __props__.__dict__["app_logs_configuration"] = app_logs_configuration
            __props__.__dict__["custom_domain_configuration"] = custom_domain_configuration
            __props__.__dict__["dapr_ai_connection_string"] = dapr_ai_connection_string
            __props__.__dict__["dapr_ai_instrumentation_key"] = dapr_ai_instrumentation_key
            __props__.__dict__["environment_name"] = environment_name
            __props__.__dict__["infrastructure_resource_group"] = infrastructure_resource_group
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            __props__.__dict__["peer_authentication"] = peer_authentication
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vnet_configuration"] = vnet_configuration
            __props__.__dict__["workload_profiles"] = workload_profiles
            __props__.__dict__["zone_redundant"] = zone_redundant
            __props__.__dict__["dapr_configuration"] = None
            __props__.__dict__["default_domain"] = None
            __props__.__dict__["deployment_errors"] = None
            __props__.__dict__["event_stream_endpoint"] = None
            __props__.__dict__["keda_configuration"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["static_ip"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:app:ManagedEnvironment"), pulumi.Alias(type_="azure-native:app/v20220101preview:ManagedEnvironment"), pulumi.Alias(type_="azure-native:app/v20220301:ManagedEnvironment"), pulumi.Alias(type_="azure-native:app/v20220601preview:ManagedEnvironment"), pulumi.Alias(type_="azure-native:app/v20221001:ManagedEnvironment"), pulumi.Alias(type_="azure-native:app/v20221101preview:ManagedEnvironment"), pulumi.Alias(type_="azure-native:app/v20230401preview:ManagedEnvironment"), pulumi.Alias(type_="azure-native:app/v20230501:ManagedEnvironment"), pulumi.Alias(type_="azure-native:app/v20230801preview:ManagedEnvironment"), pulumi.Alias(type_="azure-native:app/v20231102preview:ManagedEnvironment"), pulumi.Alias(type_="azure-native:app/v20240202preview:ManagedEnvironment"), pulumi.Alias(type_="azure-native:app/v20240301:ManagedEnvironment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ManagedEnvironment, __self__).__init__(
            'azure-native:app/v20230502preview:ManagedEnvironment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ManagedEnvironment':
        """
        Get an existing ManagedEnvironment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ManagedEnvironmentArgs.__new__(ManagedEnvironmentArgs)

        __props__.__dict__["app_logs_configuration"] = None
        __props__.__dict__["custom_domain_configuration"] = None
        __props__.__dict__["dapr_ai_connection_string"] = None
        __props__.__dict__["dapr_ai_instrumentation_key"] = None
        __props__.__dict__["dapr_configuration"] = None
        __props__.__dict__["default_domain"] = None
        __props__.__dict__["deployment_errors"] = None
        __props__.__dict__["event_stream_endpoint"] = None
        __props__.__dict__["infrastructure_resource_group"] = None
        __props__.__dict__["keda_configuration"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["peer_authentication"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["static_ip"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vnet_configuration"] = None
        __props__.__dict__["workload_profiles"] = None
        __props__.__dict__["zone_redundant"] = None
        return ManagedEnvironment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appLogsConfiguration")
    def app_logs_configuration(self) -> pulumi.Output[Optional['outputs.AppLogsConfigurationResponse']]:
        """
        Cluster configuration which enables the log daemon to export
        app logs to a destination. Currently only "log-analytics" is
        supported
        """
        return pulumi.get(self, "app_logs_configuration")

    @property
    @pulumi.getter(name="customDomainConfiguration")
    def custom_domain_configuration(self) -> pulumi.Output[Optional['outputs.CustomDomainConfigurationResponse']]:
        """
        Custom domain configuration for the environment
        """
        return pulumi.get(self, "custom_domain_configuration")

    @property
    @pulumi.getter(name="daprAIConnectionString")
    def dapr_ai_connection_string(self) -> pulumi.Output[Optional[str]]:
        """
        Application Insights connection string used by Dapr to export Service to Service communication telemetry
        """
        return pulumi.get(self, "dapr_ai_connection_string")

    @property
    @pulumi.getter(name="daprAIInstrumentationKey")
    def dapr_ai_instrumentation_key(self) -> pulumi.Output[Optional[str]]:
        """
        Azure Monitor instrumentation key used by Dapr to export Service to Service communication telemetry
        """
        return pulumi.get(self, "dapr_ai_instrumentation_key")

    @property
    @pulumi.getter(name="daprConfiguration")
    def dapr_configuration(self) -> pulumi.Output[Optional['outputs.DaprConfigurationResponse']]:
        """
        The configuration of Dapr component.
        """
        return pulumi.get(self, "dapr_configuration")

    @property
    @pulumi.getter(name="defaultDomain")
    def default_domain(self) -> pulumi.Output[str]:
        """
        Default Domain Name for the cluster
        """
        return pulumi.get(self, "default_domain")

    @property
    @pulumi.getter(name="deploymentErrors")
    def deployment_errors(self) -> pulumi.Output[str]:
        """
        Any errors that occurred during deployment or deployment validation
        """
        return pulumi.get(self, "deployment_errors")

    @property
    @pulumi.getter(name="eventStreamEndpoint")
    def event_stream_endpoint(self) -> pulumi.Output[str]:
        """
        The endpoint of the eventstream of the Environment.
        """
        return pulumi.get(self, "event_stream_endpoint")

    @property
    @pulumi.getter(name="infrastructureResourceGroup")
    def infrastructure_resource_group(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the platform-managed resource group created for the Managed Environment to host infrastructure resources. If a subnet ID is provided, this resource group will be created in the same subscription as the subnet.
        """
        return pulumi.get(self, "infrastructure_resource_group")

    @property
    @pulumi.getter(name="kedaConfiguration")
    def keda_configuration(self) -> pulumi.Output[Optional['outputs.KedaConfigurationResponse']]:
        """
        The configuration of Keda component.
        """
        return pulumi.get(self, "keda_configuration")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of the Environment.
        """
        return pulumi.get(self, "kind")

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
    @pulumi.getter(name="peerAuthentication")
    def peer_authentication(self) -> pulumi.Output[Optional['outputs.ManagedEnvironmentResponsePeerAuthentication']]:
        """
        Peer authentication settings for the Managed Environment
        """
        return pulumi.get(self, "peer_authentication")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the Environment.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="staticIp")
    def static_ip(self) -> pulumi.Output[str]:
        """
        Static IP of the Environment
        """
        return pulumi.get(self, "static_ip")

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

    @property
    @pulumi.getter(name="vnetConfiguration")
    def vnet_configuration(self) -> pulumi.Output[Optional['outputs.VnetConfigurationResponse']]:
        """
        Vnet configuration for the environment
        """
        return pulumi.get(self, "vnet_configuration")

    @property
    @pulumi.getter(name="workloadProfiles")
    def workload_profiles(self) -> pulumi.Output[Optional[Sequence['outputs.WorkloadProfileResponse']]]:
        """
        Workload profiles configured for the Managed Environment.
        """
        return pulumi.get(self, "workload_profiles")

    @property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether or not this Managed Environment is zone-redundant.
        """
        return pulumi.get(self, "zone_redundant")

