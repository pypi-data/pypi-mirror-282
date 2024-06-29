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
    'GetManagedEnvironmentResult',
    'AwaitableGetManagedEnvironmentResult',
    'get_managed_environment',
    'get_managed_environment_output',
]

@pulumi.output_type
class GetManagedEnvironmentResult:
    """
    An environment for hosting container apps
    """
    def __init__(__self__, app_insights_configuration=None, app_logs_configuration=None, custom_domain_configuration=None, dapr_ai_connection_string=None, dapr_ai_instrumentation_key=None, dapr_configuration=None, default_domain=None, deployment_errors=None, event_stream_endpoint=None, id=None, identity=None, infrastructure_resource_group=None, keda_configuration=None, kind=None, location=None, name=None, open_telemetry_configuration=None, peer_authentication=None, peer_traffic_configuration=None, private_endpoint_connections=None, provisioning_state=None, public_network_access=None, static_ip=None, system_data=None, tags=None, type=None, vnet_configuration=None, workload_profiles=None, zone_redundant=None):
        if app_insights_configuration and not isinstance(app_insights_configuration, dict):
            raise TypeError("Expected argument 'app_insights_configuration' to be a dict")
        pulumi.set(__self__, "app_insights_configuration", app_insights_configuration)
        if app_logs_configuration and not isinstance(app_logs_configuration, dict):
            raise TypeError("Expected argument 'app_logs_configuration' to be a dict")
        pulumi.set(__self__, "app_logs_configuration", app_logs_configuration)
        if custom_domain_configuration and not isinstance(custom_domain_configuration, dict):
            raise TypeError("Expected argument 'custom_domain_configuration' to be a dict")
        pulumi.set(__self__, "custom_domain_configuration", custom_domain_configuration)
        if dapr_ai_connection_string and not isinstance(dapr_ai_connection_string, str):
            raise TypeError("Expected argument 'dapr_ai_connection_string' to be a str")
        pulumi.set(__self__, "dapr_ai_connection_string", dapr_ai_connection_string)
        if dapr_ai_instrumentation_key and not isinstance(dapr_ai_instrumentation_key, str):
            raise TypeError("Expected argument 'dapr_ai_instrumentation_key' to be a str")
        pulumi.set(__self__, "dapr_ai_instrumentation_key", dapr_ai_instrumentation_key)
        if dapr_configuration and not isinstance(dapr_configuration, dict):
            raise TypeError("Expected argument 'dapr_configuration' to be a dict")
        pulumi.set(__self__, "dapr_configuration", dapr_configuration)
        if default_domain and not isinstance(default_domain, str):
            raise TypeError("Expected argument 'default_domain' to be a str")
        pulumi.set(__self__, "default_domain", default_domain)
        if deployment_errors and not isinstance(deployment_errors, str):
            raise TypeError("Expected argument 'deployment_errors' to be a str")
        pulumi.set(__self__, "deployment_errors", deployment_errors)
        if event_stream_endpoint and not isinstance(event_stream_endpoint, str):
            raise TypeError("Expected argument 'event_stream_endpoint' to be a str")
        pulumi.set(__self__, "event_stream_endpoint", event_stream_endpoint)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if infrastructure_resource_group and not isinstance(infrastructure_resource_group, str):
            raise TypeError("Expected argument 'infrastructure_resource_group' to be a str")
        pulumi.set(__self__, "infrastructure_resource_group", infrastructure_resource_group)
        if keda_configuration and not isinstance(keda_configuration, dict):
            raise TypeError("Expected argument 'keda_configuration' to be a dict")
        pulumi.set(__self__, "keda_configuration", keda_configuration)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if open_telemetry_configuration and not isinstance(open_telemetry_configuration, dict):
            raise TypeError("Expected argument 'open_telemetry_configuration' to be a dict")
        pulumi.set(__self__, "open_telemetry_configuration", open_telemetry_configuration)
        if peer_authentication and not isinstance(peer_authentication, dict):
            raise TypeError("Expected argument 'peer_authentication' to be a dict")
        pulumi.set(__self__, "peer_authentication", peer_authentication)
        if peer_traffic_configuration and not isinstance(peer_traffic_configuration, dict):
            raise TypeError("Expected argument 'peer_traffic_configuration' to be a dict")
        pulumi.set(__self__, "peer_traffic_configuration", peer_traffic_configuration)
        if private_endpoint_connections and not isinstance(private_endpoint_connections, list):
            raise TypeError("Expected argument 'private_endpoint_connections' to be a list")
        pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_network_access and not isinstance(public_network_access, str):
            raise TypeError("Expected argument 'public_network_access' to be a str")
        pulumi.set(__self__, "public_network_access", public_network_access)
        if static_ip and not isinstance(static_ip, str):
            raise TypeError("Expected argument 'static_ip' to be a str")
        pulumi.set(__self__, "static_ip", static_ip)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if vnet_configuration and not isinstance(vnet_configuration, dict):
            raise TypeError("Expected argument 'vnet_configuration' to be a dict")
        pulumi.set(__self__, "vnet_configuration", vnet_configuration)
        if workload_profiles and not isinstance(workload_profiles, list):
            raise TypeError("Expected argument 'workload_profiles' to be a list")
        pulumi.set(__self__, "workload_profiles", workload_profiles)
        if zone_redundant and not isinstance(zone_redundant, bool):
            raise TypeError("Expected argument 'zone_redundant' to be a bool")
        pulumi.set(__self__, "zone_redundant", zone_redundant)

    @property
    @pulumi.getter(name="appInsightsConfiguration")
    def app_insights_configuration(self) -> Optional['outputs.AppInsightsConfigurationResponse']:
        """
        Environment level Application Insights configuration
        """
        return pulumi.get(self, "app_insights_configuration")

    @property
    @pulumi.getter(name="appLogsConfiguration")
    def app_logs_configuration(self) -> Optional['outputs.AppLogsConfigurationResponse']:
        """
        Cluster configuration which enables the log daemon to export
        app logs to a destination. Currently only "log-analytics" is
        supported
        """
        return pulumi.get(self, "app_logs_configuration")

    @property
    @pulumi.getter(name="customDomainConfiguration")
    def custom_domain_configuration(self) -> Optional['outputs.CustomDomainConfigurationResponse']:
        """
        Custom domain configuration for the environment
        """
        return pulumi.get(self, "custom_domain_configuration")

    @property
    @pulumi.getter(name="daprAIConnectionString")
    def dapr_ai_connection_string(self) -> Optional[str]:
        """
        Application Insights connection string used by Dapr to export Service to Service communication telemetry
        """
        return pulumi.get(self, "dapr_ai_connection_string")

    @property
    @pulumi.getter(name="daprAIInstrumentationKey")
    def dapr_ai_instrumentation_key(self) -> Optional[str]:
        """
        Azure Monitor instrumentation key used by Dapr to export Service to Service communication telemetry
        """
        return pulumi.get(self, "dapr_ai_instrumentation_key")

    @property
    @pulumi.getter(name="daprConfiguration")
    def dapr_configuration(self) -> Optional['outputs.DaprConfigurationResponse']:
        """
        The configuration of Dapr component.
        """
        return pulumi.get(self, "dapr_configuration")

    @property
    @pulumi.getter(name="defaultDomain")
    def default_domain(self) -> str:
        """
        Default Domain Name for the cluster
        """
        return pulumi.get(self, "default_domain")

    @property
    @pulumi.getter(name="deploymentErrors")
    def deployment_errors(self) -> str:
        """
        Any errors that occurred during deployment or deployment validation
        """
        return pulumi.get(self, "deployment_errors")

    @property
    @pulumi.getter(name="eventStreamEndpoint")
    def event_stream_endpoint(self) -> str:
        """
        The endpoint of the eventstream of the Environment.
        """
        return pulumi.get(self, "event_stream_endpoint")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.ManagedServiceIdentityResponse']:
        """
        Managed identities for the Managed Environment to interact with other Azure services without maintaining any secrets or credentials in code.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="infrastructureResourceGroup")
    def infrastructure_resource_group(self) -> Optional[str]:
        """
        Name of the platform-managed resource group created for the Managed Environment to host infrastructure resources. If a subnet ID is provided, this resource group will be created in the same subscription as the subnet.
        """
        return pulumi.get(self, "infrastructure_resource_group")

    @property
    @pulumi.getter(name="kedaConfiguration")
    def keda_configuration(self) -> Optional['outputs.KedaConfigurationResponse']:
        """
        The configuration of Keda component.
        """
        return pulumi.get(self, "keda_configuration")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of the Environment.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="openTelemetryConfiguration")
    def open_telemetry_configuration(self) -> Optional['outputs.OpenTelemetryConfigurationResponse']:
        """
        Environment Open Telemetry configuration
        """
        return pulumi.get(self, "open_telemetry_configuration")

    @property
    @pulumi.getter(name="peerAuthentication")
    def peer_authentication(self) -> Optional['outputs.ManagedEnvironmentResponsePeerAuthentication']:
        """
        Peer authentication settings for the Managed Environment
        """
        return pulumi.get(self, "peer_authentication")

    @property
    @pulumi.getter(name="peerTrafficConfiguration")
    def peer_traffic_configuration(self) -> Optional['outputs.ManagedEnvironmentResponsePeerTrafficConfiguration']:
        """
        Peer traffic settings for the Managed Environment
        """
        return pulumi.get(self, "peer_traffic_configuration")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence['outputs.PrivateEndpointConnectionResponse']:
        """
        Private endpoint connections to the resource.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the Environment.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[str]:
        """
        Property to allow or block all public traffic. Allowed Values: 'Enabled', 'Disabled'.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="staticIp")
    def static_ip(self) -> str:
        """
        Static IP of the Environment
        """
        return pulumi.get(self, "static_ip")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
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
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vnetConfiguration")
    def vnet_configuration(self) -> Optional['outputs.VnetConfigurationResponse']:
        """
        Vnet configuration for the environment
        """
        return pulumi.get(self, "vnet_configuration")

    @property
    @pulumi.getter(name="workloadProfiles")
    def workload_profiles(self) -> Optional[Sequence['outputs.WorkloadProfileResponse']]:
        """
        Workload profiles configured for the Managed Environment.
        """
        return pulumi.get(self, "workload_profiles")

    @property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[bool]:
        """
        Whether or not this Managed Environment is zone-redundant.
        """
        return pulumi.get(self, "zone_redundant")


class AwaitableGetManagedEnvironmentResult(GetManagedEnvironmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedEnvironmentResult(
            app_insights_configuration=self.app_insights_configuration,
            app_logs_configuration=self.app_logs_configuration,
            custom_domain_configuration=self.custom_domain_configuration,
            dapr_ai_connection_string=self.dapr_ai_connection_string,
            dapr_ai_instrumentation_key=self.dapr_ai_instrumentation_key,
            dapr_configuration=self.dapr_configuration,
            default_domain=self.default_domain,
            deployment_errors=self.deployment_errors,
            event_stream_endpoint=self.event_stream_endpoint,
            id=self.id,
            identity=self.identity,
            infrastructure_resource_group=self.infrastructure_resource_group,
            keda_configuration=self.keda_configuration,
            kind=self.kind,
            location=self.location,
            name=self.name,
            open_telemetry_configuration=self.open_telemetry_configuration,
            peer_authentication=self.peer_authentication,
            peer_traffic_configuration=self.peer_traffic_configuration,
            private_endpoint_connections=self.private_endpoint_connections,
            provisioning_state=self.provisioning_state,
            public_network_access=self.public_network_access,
            static_ip=self.static_ip,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            vnet_configuration=self.vnet_configuration,
            workload_profiles=self.workload_profiles,
            zone_redundant=self.zone_redundant)


def get_managed_environment(environment_name: Optional[str] = None,
                            resource_group_name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedEnvironmentResult:
    """
    Get the properties of a Managed Environment used to host container apps.


    :param str environment_name: Name of the Environment.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['environmentName'] = environment_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:app/v20240202preview:getManagedEnvironment', __args__, opts=opts, typ=GetManagedEnvironmentResult).value

    return AwaitableGetManagedEnvironmentResult(
        app_insights_configuration=pulumi.get(__ret__, 'app_insights_configuration'),
        app_logs_configuration=pulumi.get(__ret__, 'app_logs_configuration'),
        custom_domain_configuration=pulumi.get(__ret__, 'custom_domain_configuration'),
        dapr_ai_connection_string=pulumi.get(__ret__, 'dapr_ai_connection_string'),
        dapr_ai_instrumentation_key=pulumi.get(__ret__, 'dapr_ai_instrumentation_key'),
        dapr_configuration=pulumi.get(__ret__, 'dapr_configuration'),
        default_domain=pulumi.get(__ret__, 'default_domain'),
        deployment_errors=pulumi.get(__ret__, 'deployment_errors'),
        event_stream_endpoint=pulumi.get(__ret__, 'event_stream_endpoint'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        infrastructure_resource_group=pulumi.get(__ret__, 'infrastructure_resource_group'),
        keda_configuration=pulumi.get(__ret__, 'keda_configuration'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        open_telemetry_configuration=pulumi.get(__ret__, 'open_telemetry_configuration'),
        peer_authentication=pulumi.get(__ret__, 'peer_authentication'),
        peer_traffic_configuration=pulumi.get(__ret__, 'peer_traffic_configuration'),
        private_endpoint_connections=pulumi.get(__ret__, 'private_endpoint_connections'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        public_network_access=pulumi.get(__ret__, 'public_network_access'),
        static_ip=pulumi.get(__ret__, 'static_ip'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        vnet_configuration=pulumi.get(__ret__, 'vnet_configuration'),
        workload_profiles=pulumi.get(__ret__, 'workload_profiles'),
        zone_redundant=pulumi.get(__ret__, 'zone_redundant'))


@_utilities.lift_output_func(get_managed_environment)
def get_managed_environment_output(environment_name: Optional[pulumi.Input[str]] = None,
                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedEnvironmentResult]:
    """
    Get the properties of a Managed Environment used to host container apps.


    :param str environment_name: Name of the Environment.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
