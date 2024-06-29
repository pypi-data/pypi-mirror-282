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
    'GetTargetResult',
    'AwaitableGetTargetResult',
    'get_target',
    'get_target_output',
]

@pulumi.output_type
class GetTargetResult:
    """
    A Target resource belonging to an Instance resource.
    """
    def __init__(__self__, components=None, extended_location=None, id=None, location=None, name=None, provisioning_state=None, reconciliation_policy=None, scope=None, system_data=None, tags=None, topologies=None, type=None, version=None):
        if components and not isinstance(components, list):
            raise TypeError("Expected argument 'components' to be a list")
        pulumi.set(__self__, "components", components)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if reconciliation_policy and not isinstance(reconciliation_policy, dict):
            raise TypeError("Expected argument 'reconciliation_policy' to be a dict")
        pulumi.set(__self__, "reconciliation_policy", reconciliation_policy)
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        pulumi.set(__self__, "scope", scope)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if topologies and not isinstance(topologies, list):
            raise TypeError("Expected argument 'topologies' to be a list")
        pulumi.set(__self__, "topologies", topologies)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def components(self) -> Optional[Sequence['outputs.ComponentPropertiesResponse']]:
        """
        A list of components.
        """
        return pulumi.get(self, "components")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> 'outputs.ExtendedLocationResponse':
        """
        Edge location of the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="reconciliationPolicy")
    def reconciliation_policy(self) -> Optional['outputs.ReconciliationPolicyResponse']:
        """
        Reconciliation Policy.
        """
        return pulumi.get(self, "reconciliation_policy")

    @property
    @pulumi.getter
    def scope(self) -> Optional[str]:
        """
        Deployment scope (such as Kubernetes namespace).
        """
        return pulumi.get(self, "scope")

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
    def topologies(self) -> Optional[Sequence['outputs.TopologiesPropertiesResponse']]:
        """
        Defines the device topology for a target or instance.
        """
        return pulumi.get(self, "topologies")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        Version of the particular resource.
        """
        return pulumi.get(self, "version")


class AwaitableGetTargetResult(GetTargetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTargetResult(
            components=self.components,
            extended_location=self.extended_location,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            reconciliation_policy=self.reconciliation_policy,
            scope=self.scope,
            system_data=self.system_data,
            tags=self.tags,
            topologies=self.topologies,
            type=self.type,
            version=self.version)


def get_target(name: Optional[str] = None,
               resource_group_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTargetResult:
    """
    Get a Target
    Azure REST API version: 2023-10-04-preview.


    :param str name: Name of target.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:iotoperationsorchestrator:getTarget', __args__, opts=opts, typ=GetTargetResult).value

    return AwaitableGetTargetResult(
        components=pulumi.get(__ret__, 'components'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        reconciliation_policy=pulumi.get(__ret__, 'reconciliation_policy'),
        scope=pulumi.get(__ret__, 'scope'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        topologies=pulumi.get(__ret__, 'topologies'),
        type=pulumi.get(__ret__, 'type'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_target)
def get_target_output(name: Optional[pulumi.Input[str]] = None,
                      resource_group_name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTargetResult]:
    """
    Get a Target
    Azure REST API version: 2023-10-04-preview.


    :param str name: Name of target.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
