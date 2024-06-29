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
    'GetUpdateRunResult',
    'AwaitableGetUpdateRunResult',
    'get_update_run',
    'get_update_run_output',
]

@pulumi.output_type
class GetUpdateRunResult:
    """
    A multi-stage process to perform update operations across members of a Fleet.
    """
    def __init__(__self__, e_tag=None, id=None, managed_cluster_update=None, name=None, provisioning_state=None, status=None, strategy=None, system_data=None, type=None):
        if e_tag and not isinstance(e_tag, str):
            raise TypeError("Expected argument 'e_tag' to be a str")
        pulumi.set(__self__, "e_tag", e_tag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if managed_cluster_update and not isinstance(managed_cluster_update, dict):
            raise TypeError("Expected argument 'managed_cluster_update' to be a dict")
        pulumi.set(__self__, "managed_cluster_update", managed_cluster_update)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if status and not isinstance(status, dict):
            raise TypeError("Expected argument 'status' to be a dict")
        pulumi.set(__self__, "status", status)
        if strategy and not isinstance(strategy, dict):
            raise TypeError("Expected argument 'strategy' to be a dict")
        pulumi.set(__self__, "strategy", strategy)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> str:
        """
        If eTag is provided in the response body, it may also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="managedClusterUpdate")
    def managed_cluster_update(self) -> 'outputs.ManagedClusterUpdateResponse':
        """
        The update to be applied to all clusters in the UpdateRun. The managedClusterUpdate can be modified until the run is started.
        """
        return pulumi.get(self, "managed_cluster_update")

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
        The provisioning state of the UpdateRun resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.UpdateRunStatusResponse':
        """
        The status of the UpdateRun.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def strategy(self) -> Optional['outputs.UpdateRunStrategyResponse']:
        """
        The strategy defines the order in which the clusters will be updated.
        If not set, all members will be updated sequentially. The UpdateRun status will show a single UpdateStage and a single UpdateGroup targeting all members.
        The strategy of the UpdateRun can be modified until the run is started.
        """
        return pulumi.get(self, "strategy")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetUpdateRunResult(GetUpdateRunResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUpdateRunResult(
            e_tag=self.e_tag,
            id=self.id,
            managed_cluster_update=self.managed_cluster_update,
            name=self.name,
            provisioning_state=self.provisioning_state,
            status=self.status,
            strategy=self.strategy,
            system_data=self.system_data,
            type=self.type)


def get_update_run(fleet_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   update_run_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUpdateRunResult:
    """
    Get a UpdateRun


    :param str fleet_name: The name of the Fleet resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str update_run_name: The name of the UpdateRun resource.
    """
    __args__ = dict()
    __args__['fleetName'] = fleet_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['updateRunName'] = update_run_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerservice/v20230315preview:getUpdateRun', __args__, opts=opts, typ=GetUpdateRunResult).value

    return AwaitableGetUpdateRunResult(
        e_tag=pulumi.get(__ret__, 'e_tag'),
        id=pulumi.get(__ret__, 'id'),
        managed_cluster_update=pulumi.get(__ret__, 'managed_cluster_update'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        status=pulumi.get(__ret__, 'status'),
        strategy=pulumi.get(__ret__, 'strategy'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_update_run)
def get_update_run_output(fleet_name: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          update_run_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUpdateRunResult]:
    """
    Get a UpdateRun


    :param str fleet_name: The name of the Fleet resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str update_run_name: The name of the UpdateRun resource.
    """
    ...
