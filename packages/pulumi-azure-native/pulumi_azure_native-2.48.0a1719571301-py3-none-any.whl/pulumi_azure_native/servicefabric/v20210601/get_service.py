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
    'GetServiceResult',
    'AwaitableGetServiceResult',
    'get_service',
    'get_service_output',
]

@pulumi.output_type
class GetServiceResult:
    """
    The service resource.
    """
    def __init__(__self__, correlation_scheme=None, default_move_cost=None, etag=None, id=None, location=None, name=None, partition_description=None, placement_constraints=None, provisioning_state=None, service_dns_name=None, service_kind=None, service_load_metrics=None, service_package_activation_mode=None, service_placement_policies=None, service_type_name=None, system_data=None, tags=None, type=None):
        if correlation_scheme and not isinstance(correlation_scheme, list):
            raise TypeError("Expected argument 'correlation_scheme' to be a list")
        pulumi.set(__self__, "correlation_scheme", correlation_scheme)
        if default_move_cost and not isinstance(default_move_cost, str):
            raise TypeError("Expected argument 'default_move_cost' to be a str")
        pulumi.set(__self__, "default_move_cost", default_move_cost)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if partition_description and not isinstance(partition_description, dict):
            raise TypeError("Expected argument 'partition_description' to be a dict")
        pulumi.set(__self__, "partition_description", partition_description)
        if placement_constraints and not isinstance(placement_constraints, str):
            raise TypeError("Expected argument 'placement_constraints' to be a str")
        pulumi.set(__self__, "placement_constraints", placement_constraints)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if service_dns_name and not isinstance(service_dns_name, str):
            raise TypeError("Expected argument 'service_dns_name' to be a str")
        pulumi.set(__self__, "service_dns_name", service_dns_name)
        if service_kind and not isinstance(service_kind, str):
            raise TypeError("Expected argument 'service_kind' to be a str")
        pulumi.set(__self__, "service_kind", service_kind)
        if service_load_metrics and not isinstance(service_load_metrics, list):
            raise TypeError("Expected argument 'service_load_metrics' to be a list")
        pulumi.set(__self__, "service_load_metrics", service_load_metrics)
        if service_package_activation_mode and not isinstance(service_package_activation_mode, str):
            raise TypeError("Expected argument 'service_package_activation_mode' to be a str")
        pulumi.set(__self__, "service_package_activation_mode", service_package_activation_mode)
        if service_placement_policies and not isinstance(service_placement_policies, list):
            raise TypeError("Expected argument 'service_placement_policies' to be a list")
        pulumi.set(__self__, "service_placement_policies", service_placement_policies)
        if service_type_name and not isinstance(service_type_name, str):
            raise TypeError("Expected argument 'service_type_name' to be a str")
        pulumi.set(__self__, "service_type_name", service_type_name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="correlationScheme")
    def correlation_scheme(self) -> Optional[Sequence['outputs.ServiceCorrelationDescriptionResponse']]:
        """
        A list that describes the correlation of the service with other services.
        """
        return pulumi.get(self, "correlation_scheme")

    @property
    @pulumi.getter(name="defaultMoveCost")
    def default_move_cost(self) -> Optional[str]:
        """
        Specifies the move cost for the service.
        """
        return pulumi.get(self, "default_move_cost")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Azure resource etag.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Azure resource identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        It will be deprecated in New API, resource location depends on the parent resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Azure resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partitionDescription")
    def partition_description(self) -> Optional[Any]:
        """
        Describes how the service is partitioned.
        """
        return pulumi.get(self, "partition_description")

    @property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(self) -> Optional[str]:
        """
        The placement constraints as a string. Placement constraints are boolean expressions on node properties and allow for restricting a service to particular nodes based on the service requirements. For example, to place a service on nodes where NodeType is blue specify the following: "NodeColor == blue)".
        """
        return pulumi.get(self, "placement_constraints")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The current deployment or provisioning state, which only appears in the response
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serviceDnsName")
    def service_dns_name(self) -> Optional[str]:
        """
        Dns name used for the service. If this is specified, then the service can be accessed via its DNS name instead of service name.
        """
        return pulumi.get(self, "service_dns_name")

    @property
    @pulumi.getter(name="serviceKind")
    def service_kind(self) -> str:
        """
        The kind of service (Stateless or Stateful).
        """
        return pulumi.get(self, "service_kind")

    @property
    @pulumi.getter(name="serviceLoadMetrics")
    def service_load_metrics(self) -> Optional[Sequence['outputs.ServiceLoadMetricDescriptionResponse']]:
        """
        The service load metrics is given as an array of ServiceLoadMetricDescription objects.
        """
        return pulumi.get(self, "service_load_metrics")

    @property
    @pulumi.getter(name="servicePackageActivationMode")
    def service_package_activation_mode(self) -> Optional[str]:
        """
        The activation Mode of the service package
        """
        return pulumi.get(self, "service_package_activation_mode")

    @property
    @pulumi.getter(name="servicePlacementPolicies")
    def service_placement_policies(self) -> Optional[Sequence['outputs.ServicePlacementPolicyDescriptionResponse']]:
        """
        A list that describes the correlation of the service with other services.
        """
        return pulumi.get(self, "service_placement_policies")

    @property
    @pulumi.getter(name="serviceTypeName")
    def service_type_name(self) -> Optional[str]:
        """
        The name of the service type
        """
        return pulumi.get(self, "service_type_name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Azure resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Azure resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetServiceResult(GetServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceResult(
            correlation_scheme=self.correlation_scheme,
            default_move_cost=self.default_move_cost,
            etag=self.etag,
            id=self.id,
            location=self.location,
            name=self.name,
            partition_description=self.partition_description,
            placement_constraints=self.placement_constraints,
            provisioning_state=self.provisioning_state,
            service_dns_name=self.service_dns_name,
            service_kind=self.service_kind,
            service_load_metrics=self.service_load_metrics,
            service_package_activation_mode=self.service_package_activation_mode,
            service_placement_policies=self.service_placement_policies,
            service_type_name=self.service_type_name,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_service(application_name: Optional[str] = None,
                cluster_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                service_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceResult:
    """
    Get a Service Fabric service resource created or in the process of being created in the Service Fabric application resource.


    :param str application_name: The name of the application resource.
    :param str cluster_name: The name of the cluster resource.
    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the service resource in the format of {applicationName}~{serviceName}.
    """
    __args__ = dict()
    __args__['applicationName'] = application_name
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:servicefabric/v20210601:getService', __args__, opts=opts, typ=GetServiceResult).value

    return AwaitableGetServiceResult(
        correlation_scheme=pulumi.get(__ret__, 'correlation_scheme'),
        default_move_cost=pulumi.get(__ret__, 'default_move_cost'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        partition_description=pulumi.get(__ret__, 'partition_description'),
        placement_constraints=pulumi.get(__ret__, 'placement_constraints'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        service_dns_name=pulumi.get(__ret__, 'service_dns_name'),
        service_kind=pulumi.get(__ret__, 'service_kind'),
        service_load_metrics=pulumi.get(__ret__, 'service_load_metrics'),
        service_package_activation_mode=pulumi.get(__ret__, 'service_package_activation_mode'),
        service_placement_policies=pulumi.get(__ret__, 'service_placement_policies'),
        service_type_name=pulumi.get(__ret__, 'service_type_name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_service)
def get_service_output(application_name: Optional[pulumi.Input[str]] = None,
                       cluster_name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       service_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServiceResult]:
    """
    Get a Service Fabric service resource created or in the process of being created in the Service Fabric application resource.


    :param str application_name: The name of the application resource.
    :param str cluster_name: The name of the cluster resource.
    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the service resource in the format of {applicationName}~{serviceName}.
    """
    ...
