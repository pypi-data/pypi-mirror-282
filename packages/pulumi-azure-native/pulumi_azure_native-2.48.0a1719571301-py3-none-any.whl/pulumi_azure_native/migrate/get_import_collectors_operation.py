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
    'GetImportCollectorsOperationResult',
    'AwaitableGetImportCollectorsOperationResult',
    'get_import_collectors_operation',
    'get_import_collectors_operation_output',
]

@pulumi.output_type
class GetImportCollectorsOperationResult:
    """
    Import collector resource.
    """
    def __init__(__self__, created_timestamp=None, discovery_site_id=None, id=None, name=None, provisioning_state=None, system_data=None, type=None, updated_timestamp=None):
        if created_timestamp and not isinstance(created_timestamp, str):
            raise TypeError("Expected argument 'created_timestamp' to be a str")
        pulumi.set(__self__, "created_timestamp", created_timestamp)
        if discovery_site_id and not isinstance(discovery_site_id, str):
            raise TypeError("Expected argument 'discovery_site_id' to be a str")
        pulumi.set(__self__, "discovery_site_id", discovery_site_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if updated_timestamp and not isinstance(updated_timestamp, str):
            raise TypeError("Expected argument 'updated_timestamp' to be a str")
        pulumi.set(__self__, "updated_timestamp", updated_timestamp)

    @property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> str:
        """
        Gets the Timestamp when collector was created.
        """
        return pulumi.get(self, "created_timestamp")

    @property
    @pulumi.getter(name="discoverySiteId")
    def discovery_site_id(self) -> Optional[str]:
        """
        Gets the discovery site id.
        """
        return pulumi.get(self, "discovery_site_id")

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
    def provisioning_state(self) -> Optional[str]:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

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

    @property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> str:
        """
        Timestamp when collector was last updated.
        """
        return pulumi.get(self, "updated_timestamp")


class AwaitableGetImportCollectorsOperationResult(GetImportCollectorsOperationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetImportCollectorsOperationResult(
            created_timestamp=self.created_timestamp,
            discovery_site_id=self.discovery_site_id,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type,
            updated_timestamp=self.updated_timestamp)


def get_import_collectors_operation(import_collector_name: Optional[str] = None,
                                    project_name: Optional[str] = None,
                                    resource_group_name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetImportCollectorsOperationResult:
    """
    Get a ImportCollector
    Azure REST API version: 2023-03-15.

    Other available API versions: 2023-04-01-preview.


    :param str import_collector_name: Import collector ARM name
    :param str project_name: Assessment Project Name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['importCollectorName'] = import_collector_name
    __args__['projectName'] = project_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:migrate:getImportCollectorsOperation', __args__, opts=opts, typ=GetImportCollectorsOperationResult).value

    return AwaitableGetImportCollectorsOperationResult(
        created_timestamp=pulumi.get(__ret__, 'created_timestamp'),
        discovery_site_id=pulumi.get(__ret__, 'discovery_site_id'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        updated_timestamp=pulumi.get(__ret__, 'updated_timestamp'))


@_utilities.lift_output_func(get_import_collectors_operation)
def get_import_collectors_operation_output(import_collector_name: Optional[pulumi.Input[str]] = None,
                                           project_name: Optional[pulumi.Input[str]] = None,
                                           resource_group_name: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetImportCollectorsOperationResult]:
    """
    Get a ImportCollector
    Azure REST API version: 2023-03-15.

    Other available API versions: 2023-04-01-preview.


    :param str import_collector_name: Import collector ARM name
    :param str project_name: Assessment Project Name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
