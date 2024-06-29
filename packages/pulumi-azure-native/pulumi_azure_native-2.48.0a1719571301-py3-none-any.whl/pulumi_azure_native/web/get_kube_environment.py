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

__all__ = [
    'GetKubeEnvironmentResult',
    'AwaitableGetKubeEnvironmentResult',
    'get_kube_environment',
    'get_kube_environment_output',
]

@pulumi.output_type
class GetKubeEnvironmentResult:
    """
    A Kubernetes cluster specialized for web workloads by Azure App Service
    """
    def __init__(__self__, aks_resource_id=None, app_logs_configuration=None, arc_configuration=None, container_apps_configuration=None, default_domain=None, deployment_errors=None, environment_type=None, extended_location=None, id=None, internal_load_balancer_enabled=None, kind=None, location=None, name=None, provisioning_state=None, static_ip=None, tags=None, type=None):
        if aks_resource_id and not isinstance(aks_resource_id, str):
            raise TypeError("Expected argument 'aks_resource_id' to be a str")
        pulumi.set(__self__, "aks_resource_id", aks_resource_id)
        if app_logs_configuration and not isinstance(app_logs_configuration, dict):
            raise TypeError("Expected argument 'app_logs_configuration' to be a dict")
        pulumi.set(__self__, "app_logs_configuration", app_logs_configuration)
        if arc_configuration and not isinstance(arc_configuration, dict):
            raise TypeError("Expected argument 'arc_configuration' to be a dict")
        pulumi.set(__self__, "arc_configuration", arc_configuration)
        if container_apps_configuration and not isinstance(container_apps_configuration, dict):
            raise TypeError("Expected argument 'container_apps_configuration' to be a dict")
        pulumi.set(__self__, "container_apps_configuration", container_apps_configuration)
        if default_domain and not isinstance(default_domain, str):
            raise TypeError("Expected argument 'default_domain' to be a str")
        pulumi.set(__self__, "default_domain", default_domain)
        if deployment_errors and not isinstance(deployment_errors, str):
            raise TypeError("Expected argument 'deployment_errors' to be a str")
        pulumi.set(__self__, "deployment_errors", deployment_errors)
        if environment_type and not isinstance(environment_type, str):
            raise TypeError("Expected argument 'environment_type' to be a str")
        pulumi.set(__self__, "environment_type", environment_type)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if internal_load_balancer_enabled and not isinstance(internal_load_balancer_enabled, bool):
            raise TypeError("Expected argument 'internal_load_balancer_enabled' to be a bool")
        pulumi.set(__self__, "internal_load_balancer_enabled", internal_load_balancer_enabled)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if static_ip and not isinstance(static_ip, str):
            raise TypeError("Expected argument 'static_ip' to be a str")
        pulumi.set(__self__, "static_ip", static_ip)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="aksResourceID")
    def aks_resource_id(self) -> Optional[str]:
        return pulumi.get(self, "aks_resource_id")

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
    @pulumi.getter(name="arcConfiguration")
    def arc_configuration(self) -> Optional['outputs.ArcConfigurationResponse']:
        """
        Cluster configuration which determines the ARC cluster
        components types. Eg: Choosing between BuildService kind,
        FrontEnd Service ArtifactsStorageType etc.
        """
        return pulumi.get(self, "arc_configuration")

    @property
    @pulumi.getter(name="containerAppsConfiguration")
    def container_apps_configuration(self) -> Optional['outputs.ContainerAppsConfigurationResponse']:
        """
        Cluster configuration for Container Apps Environments to configure Dapr Instrumentation Key and VNET Configuration
        """
        return pulumi.get(self, "container_apps_configuration")

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
    @pulumi.getter(name="environmentType")
    def environment_type(self) -> Optional[str]:
        """
        Type of Kubernetes Environment. Only supported for Container App Environments with value as Managed
        """
        return pulumi.get(self, "environment_type")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional['outputs.ExtendedLocationResponse']:
        """
        Extended Location.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="internalLoadBalancerEnabled")
    def internal_load_balancer_enabled(self) -> Optional[bool]:
        """
        Only visible within Vnet/Subnet
        """
        return pulumi.get(self, "internal_load_balancer_enabled")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource Location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the Kubernetes Environment.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="staticIp")
    def static_ip(self) -> Optional[str]:
        """
        Static IP of the KubeEnvironment
        """
        return pulumi.get(self, "static_ip")

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
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetKubeEnvironmentResult(GetKubeEnvironmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKubeEnvironmentResult(
            aks_resource_id=self.aks_resource_id,
            app_logs_configuration=self.app_logs_configuration,
            arc_configuration=self.arc_configuration,
            container_apps_configuration=self.container_apps_configuration,
            default_domain=self.default_domain,
            deployment_errors=self.deployment_errors,
            environment_type=self.environment_type,
            extended_location=self.extended_location,
            id=self.id,
            internal_load_balancer_enabled=self.internal_load_balancer_enabled,
            kind=self.kind,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            static_ip=self.static_ip,
            tags=self.tags,
            type=self.type)


def get_kube_environment(name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKubeEnvironmentResult:
    """
    Description for Get the properties of a Kubernetes Environment.
    Azure REST API version: 2022-09-01.

    Other available API versions: 2023-01-01, 2023-12-01.


    :param str name: Name of the Kubernetes Environment.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:web:getKubeEnvironment', __args__, opts=opts, typ=GetKubeEnvironmentResult).value

    return AwaitableGetKubeEnvironmentResult(
        aks_resource_id=pulumi.get(__ret__, 'aks_resource_id'),
        app_logs_configuration=pulumi.get(__ret__, 'app_logs_configuration'),
        arc_configuration=pulumi.get(__ret__, 'arc_configuration'),
        container_apps_configuration=pulumi.get(__ret__, 'container_apps_configuration'),
        default_domain=pulumi.get(__ret__, 'default_domain'),
        deployment_errors=pulumi.get(__ret__, 'deployment_errors'),
        environment_type=pulumi.get(__ret__, 'environment_type'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        id=pulumi.get(__ret__, 'id'),
        internal_load_balancer_enabled=pulumi.get(__ret__, 'internal_load_balancer_enabled'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        static_ip=pulumi.get(__ret__, 'static_ip'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_kube_environment)
def get_kube_environment_output(name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKubeEnvironmentResult]:
    """
    Description for Get the properties of a Kubernetes Environment.
    Azure REST API version: 2022-09-01.

    Other available API versions: 2023-01-01, 2023-12-01.


    :param str name: Name of the Kubernetes Environment.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    ...
