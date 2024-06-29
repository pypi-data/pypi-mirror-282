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
    'GetSnapshotResult',
    'AwaitableGetSnapshotResult',
    'get_snapshot',
    'get_snapshot_output',
]

@pulumi.output_type
class GetSnapshotResult:
    """
    Concrete proxy resource types can be created by aliasing this type using a specific property type.
    """
    def __init__(__self__, id=None, name=None, provisioning_state=None, source=None, status=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if source and not isinstance(source, str):
            raise TypeError("Expected argument 'source' to be a str")
        pulumi.set(__self__, "source", source)
        if status and not isinstance(status, dict):
            raise TypeError("Expected argument 'status' to be a dict")
        pulumi.set(__self__, "status", status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

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
    @pulumi.getter
    def source(self) -> str:
        """
        Reference to the source volume
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.ResourceOperationalStatusResponse':
        """
        The status of the resource.
        """
        return pulumi.get(self, "status")

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


class AwaitableGetSnapshotResult(GetSnapshotResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSnapshotResult(
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            source=self.source,
            status=self.status,
            system_data=self.system_data,
            type=self.type)


def get_snapshot(pool_name: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 snapshot_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSnapshotResult:
    """
    Get a Snapshot
    Azure REST API version: 2023-07-01-preview.


    :param str pool_name: Pool Object
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str snapshot_name: Volume Snapshot Resource
    """
    __args__ = dict()
    __args__['poolName'] = pool_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['snapshotName'] = snapshot_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerstorage:getSnapshot', __args__, opts=opts, typ=GetSnapshotResult).value

    return AwaitableGetSnapshotResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        source=pulumi.get(__ret__, 'source'),
        status=pulumi.get(__ret__, 'status'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_snapshot)
def get_snapshot_output(pool_name: Optional[pulumi.Input[str]] = None,
                        resource_group_name: Optional[pulumi.Input[str]] = None,
                        snapshot_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSnapshotResult]:
    """
    Get a Snapshot
    Azure REST API version: 2023-07-01-preview.


    :param str pool_name: Pool Object
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str snapshot_name: Volume Snapshot Resource
    """
    ...
