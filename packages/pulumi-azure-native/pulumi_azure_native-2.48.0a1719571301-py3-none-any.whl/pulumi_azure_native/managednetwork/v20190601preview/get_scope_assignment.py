# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetScopeAssignmentResult',
    'AwaitableGetScopeAssignmentResult',
    'get_scope_assignment',
    'get_scope_assignment_output',
]

@pulumi.output_type
class GetScopeAssignmentResult:
    """
    The Managed Network resource
    """
    def __init__(__self__, assigned_managed_network=None, etag=None, id=None, location=None, name=None, provisioning_state=None, type=None):
        if assigned_managed_network and not isinstance(assigned_managed_network, str):
            raise TypeError("Expected argument 'assigned_managed_network' to be a str")
        pulumi.set(__self__, "assigned_managed_network", assigned_managed_network)
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
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="assignedManagedNetwork")
    def assigned_managed_network(self) -> Optional[str]:
        """
        The managed network ID with scope will be assigned to.
        """
        return pulumi.get(self, "assigned_managed_network")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
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
        Provisioning state of the ManagedNetwork resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
        """
        return pulumi.get(self, "type")


class AwaitableGetScopeAssignmentResult(GetScopeAssignmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScopeAssignmentResult(
            assigned_managed_network=self.assigned_managed_network,
            etag=self.etag,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            type=self.type)


def get_scope_assignment(scope: Optional[str] = None,
                         scope_assignment_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScopeAssignmentResult:
    """
    Get the specified scope assignment.


    :param str scope: The base resource of the scope assignment.
    :param str scope_assignment_name: The name of the scope assignment to get.
    """
    __args__ = dict()
    __args__['scope'] = scope
    __args__['scopeAssignmentName'] = scope_assignment_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:managednetwork/v20190601preview:getScopeAssignment', __args__, opts=opts, typ=GetScopeAssignmentResult).value

    return AwaitableGetScopeAssignmentResult(
        assigned_managed_network=pulumi.get(__ret__, 'assigned_managed_network'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_scope_assignment)
def get_scope_assignment_output(scope: Optional[pulumi.Input[str]] = None,
                                scope_assignment_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetScopeAssignmentResult]:
    """
    Get the specified scope assignment.


    :param str scope: The base resource of the scope assignment.
    :param str scope_assignment_name: The name of the scope assignment to get.
    """
    ...
