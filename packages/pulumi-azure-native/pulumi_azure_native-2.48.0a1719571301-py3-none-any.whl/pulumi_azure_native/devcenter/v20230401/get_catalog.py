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
    'GetCatalogResult',
    'AwaitableGetCatalogResult',
    'get_catalog',
    'get_catalog_output',
]

@pulumi.output_type
class GetCatalogResult:
    """
    Represents a catalog.
    """
    def __init__(__self__, ado_git=None, git_hub=None, id=None, last_sync_time=None, name=None, provisioning_state=None, sync_state=None, system_data=None, type=None):
        if ado_git and not isinstance(ado_git, dict):
            raise TypeError("Expected argument 'ado_git' to be a dict")
        pulumi.set(__self__, "ado_git", ado_git)
        if git_hub and not isinstance(git_hub, dict):
            raise TypeError("Expected argument 'git_hub' to be a dict")
        pulumi.set(__self__, "git_hub", git_hub)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_sync_time and not isinstance(last_sync_time, str):
            raise TypeError("Expected argument 'last_sync_time' to be a str")
        pulumi.set(__self__, "last_sync_time", last_sync_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if sync_state and not isinstance(sync_state, str):
            raise TypeError("Expected argument 'sync_state' to be a str")
        pulumi.set(__self__, "sync_state", sync_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="adoGit")
    def ado_git(self) -> Optional['outputs.GitCatalogResponse']:
        """
        Properties for an Azure DevOps catalog type.
        """
        return pulumi.get(self, "ado_git")

    @property
    @pulumi.getter(name="gitHub")
    def git_hub(self) -> Optional['outputs.GitCatalogResponse']:
        """
        Properties for a GitHub catalog type.
        """
        return pulumi.get(self, "git_hub")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastSyncTime")
    def last_sync_time(self) -> str:
        """
        When the catalog was last synced.
        """
        return pulumi.get(self, "last_sync_time")

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
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="syncState")
    def sync_state(self) -> str:
        """
        The synchronization state of the catalog.
        """
        return pulumi.get(self, "sync_state")

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


class AwaitableGetCatalogResult(GetCatalogResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCatalogResult(
            ado_git=self.ado_git,
            git_hub=self.git_hub,
            id=self.id,
            last_sync_time=self.last_sync_time,
            name=self.name,
            provisioning_state=self.provisioning_state,
            sync_state=self.sync_state,
            system_data=self.system_data,
            type=self.type)


def get_catalog(catalog_name: Optional[str] = None,
                dev_center_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCatalogResult:
    """
    Gets a catalog


    :param str catalog_name: The name of the Catalog.
    :param str dev_center_name: The name of the devcenter.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['catalogName'] = catalog_name
    __args__['devCenterName'] = dev_center_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:devcenter/v20230401:getCatalog', __args__, opts=opts, typ=GetCatalogResult).value

    return AwaitableGetCatalogResult(
        ado_git=pulumi.get(__ret__, 'ado_git'),
        git_hub=pulumi.get(__ret__, 'git_hub'),
        id=pulumi.get(__ret__, 'id'),
        last_sync_time=pulumi.get(__ret__, 'last_sync_time'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        sync_state=pulumi.get(__ret__, 'sync_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_catalog)
def get_catalog_output(catalog_name: Optional[pulumi.Input[str]] = None,
                       dev_center_name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCatalogResult]:
    """
    Gets a catalog


    :param str catalog_name: The name of the Catalog.
    :param str dev_center_name: The name of the devcenter.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
