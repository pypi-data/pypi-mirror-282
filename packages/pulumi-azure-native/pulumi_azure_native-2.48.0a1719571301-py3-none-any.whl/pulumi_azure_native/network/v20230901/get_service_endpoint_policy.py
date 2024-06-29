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
    'GetServiceEndpointPolicyResult',
    'AwaitableGetServiceEndpointPolicyResult',
    'get_service_endpoint_policy',
    'get_service_endpoint_policy_output',
]

@pulumi.output_type
class GetServiceEndpointPolicyResult:
    """
    Service End point policy resource.
    """
    def __init__(__self__, contextual_service_endpoint_policies=None, etag=None, id=None, kind=None, location=None, name=None, provisioning_state=None, resource_guid=None, service_alias=None, service_endpoint_policy_definitions=None, subnets=None, tags=None, type=None):
        if contextual_service_endpoint_policies and not isinstance(contextual_service_endpoint_policies, list):
            raise TypeError("Expected argument 'contextual_service_endpoint_policies' to be a list")
        pulumi.set(__self__, "contextual_service_endpoint_policies", contextual_service_endpoint_policies)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
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
        if resource_guid and not isinstance(resource_guid, str):
            raise TypeError("Expected argument 'resource_guid' to be a str")
        pulumi.set(__self__, "resource_guid", resource_guid)
        if service_alias and not isinstance(service_alias, str):
            raise TypeError("Expected argument 'service_alias' to be a str")
        pulumi.set(__self__, "service_alias", service_alias)
        if service_endpoint_policy_definitions and not isinstance(service_endpoint_policy_definitions, list):
            raise TypeError("Expected argument 'service_endpoint_policy_definitions' to be a list")
        pulumi.set(__self__, "service_endpoint_policy_definitions", service_endpoint_policy_definitions)
        if subnets and not isinstance(subnets, list):
            raise TypeError("Expected argument 'subnets' to be a list")
        pulumi.set(__self__, "subnets", subnets)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="contextualServiceEndpointPolicies")
    def contextual_service_endpoint_policies(self) -> Optional[Sequence[str]]:
        """
        A collection of contextual service endpoint policy.
        """
        return pulumi.get(self, "contextual_service_endpoint_policies")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of service endpoint policy. This is metadata used for the Azure portal experience.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the service endpoint policy resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> str:
        """
        The resource GUID property of the service endpoint policy resource.
        """
        return pulumi.get(self, "resource_guid")

    @property
    @pulumi.getter(name="serviceAlias")
    def service_alias(self) -> Optional[str]:
        """
        The alias indicating if the policy belongs to a service
        """
        return pulumi.get(self, "service_alias")

    @property
    @pulumi.getter(name="serviceEndpointPolicyDefinitions")
    def service_endpoint_policy_definitions(self) -> Optional[Sequence['outputs.ServiceEndpointPolicyDefinitionResponse']]:
        """
        A collection of service endpoint policy definitions of the service endpoint policy.
        """
        return pulumi.get(self, "service_endpoint_policy_definitions")

    @property
    @pulumi.getter
    def subnets(self) -> Sequence['outputs.SubnetResponse']:
        """
        A collection of references to subnets.
        """
        return pulumi.get(self, "subnets")

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


class AwaitableGetServiceEndpointPolicyResult(GetServiceEndpointPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceEndpointPolicyResult(
            contextual_service_endpoint_policies=self.contextual_service_endpoint_policies,
            etag=self.etag,
            id=self.id,
            kind=self.kind,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            resource_guid=self.resource_guid,
            service_alias=self.service_alias,
            service_endpoint_policy_definitions=self.service_endpoint_policy_definitions,
            subnets=self.subnets,
            tags=self.tags,
            type=self.type)


def get_service_endpoint_policy(expand: Optional[str] = None,
                                resource_group_name: Optional[str] = None,
                                service_endpoint_policy_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceEndpointPolicyResult:
    """
    Gets the specified service Endpoint Policies in a specified resource group.


    :param str expand: Expands referenced resources.
    :param str resource_group_name: The name of the resource group.
    :param str service_endpoint_policy_name: The name of the service endpoint policy.
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceEndpointPolicyName'] = service_endpoint_policy_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20230901:getServiceEndpointPolicy', __args__, opts=opts, typ=GetServiceEndpointPolicyResult).value

    return AwaitableGetServiceEndpointPolicyResult(
        contextual_service_endpoint_policies=pulumi.get(__ret__, 'contextual_service_endpoint_policies'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        resource_guid=pulumi.get(__ret__, 'resource_guid'),
        service_alias=pulumi.get(__ret__, 'service_alias'),
        service_endpoint_policy_definitions=pulumi.get(__ret__, 'service_endpoint_policy_definitions'),
        subnets=pulumi.get(__ret__, 'subnets'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_service_endpoint_policy)
def get_service_endpoint_policy_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                                       resource_group_name: Optional[pulumi.Input[str]] = None,
                                       service_endpoint_policy_name: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServiceEndpointPolicyResult]:
    """
    Gets the specified service Endpoint Policies in a specified resource group.


    :param str expand: Expands referenced resources.
    :param str resource_group_name: The name of the resource group.
    :param str service_endpoint_policy_name: The name of the service endpoint policy.
    """
    ...
