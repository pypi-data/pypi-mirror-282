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
    'GetWorkspaceManagerMemberResult',
    'AwaitableGetWorkspaceManagerMemberResult',
    'get_workspace_manager_member',
    'get_workspace_manager_member_output',
]

@pulumi.output_type
class GetWorkspaceManagerMemberResult:
    """
    The workspace manager member
    """
    def __init__(__self__, etag=None, id=None, name=None, system_data=None, target_workspace_resource_id=None, target_workspace_tenant_id=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if target_workspace_resource_id and not isinstance(target_workspace_resource_id, str):
            raise TypeError("Expected argument 'target_workspace_resource_id' to be a str")
        pulumi.set(__self__, "target_workspace_resource_id", target_workspace_resource_id)
        if target_workspace_tenant_id and not isinstance(target_workspace_tenant_id, str):
            raise TypeError("Expected argument 'target_workspace_tenant_id' to be a str")
        pulumi.set(__self__, "target_workspace_tenant_id", target_workspace_tenant_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Resource Etag.
        """
        return pulumi.get(self, "etag")

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
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="targetWorkspaceResourceId")
    def target_workspace_resource_id(self) -> str:
        """
        Fully qualified resource ID of the target Sentinel workspace joining the given Sentinel workspace manager
        """
        return pulumi.get(self, "target_workspace_resource_id")

    @property
    @pulumi.getter(name="targetWorkspaceTenantId")
    def target_workspace_tenant_id(self) -> str:
        """
        Tenant id of the target Sentinel workspace joining the given Sentinel workspace manager
        """
        return pulumi.get(self, "target_workspace_tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetWorkspaceManagerMemberResult(GetWorkspaceManagerMemberResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkspaceManagerMemberResult(
            etag=self.etag,
            id=self.id,
            name=self.name,
            system_data=self.system_data,
            target_workspace_resource_id=self.target_workspace_resource_id,
            target_workspace_tenant_id=self.target_workspace_tenant_id,
            type=self.type)


def get_workspace_manager_member(resource_group_name: Optional[str] = None,
                                 workspace_manager_member_name: Optional[str] = None,
                                 workspace_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkspaceManagerMemberResult:
    """
    Gets a workspace manager member


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_manager_member_name: The name of the workspace manager member
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceManagerMemberName'] = workspace_manager_member_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20230701preview:getWorkspaceManagerMember', __args__, opts=opts, typ=GetWorkspaceManagerMemberResult).value

    return AwaitableGetWorkspaceManagerMemberResult(
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        target_workspace_resource_id=pulumi.get(__ret__, 'target_workspace_resource_id'),
        target_workspace_tenant_id=pulumi.get(__ret__, 'target_workspace_tenant_id'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_workspace_manager_member)
def get_workspace_manager_member_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                        workspace_manager_member_name: Optional[pulumi.Input[str]] = None,
                                        workspace_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkspaceManagerMemberResult]:
    """
    Gets a workspace manager member


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_manager_member_name: The name of the workspace manager member
    :param str workspace_name: The name of the workspace.
    """
    ...
