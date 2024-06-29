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
    'GetWorkspaceManagerGroupResult',
    'AwaitableGetWorkspaceManagerGroupResult',
    'get_workspace_manager_group',
    'get_workspace_manager_group_output',
]

@pulumi.output_type
class GetWorkspaceManagerGroupResult:
    """
    The workspace manager group
    """
    def __init__(__self__, description=None, display_name=None, etag=None, id=None, member_resource_names=None, name=None, system_data=None, type=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if member_resource_names and not isinstance(member_resource_names, list):
            raise TypeError("Expected argument 'member_resource_names' to be a list")
        pulumi.set(__self__, "member_resource_names", member_resource_names)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the workspace manager group
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name of the workspace manager group
        """
        return pulumi.get(self, "display_name")

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
    @pulumi.getter(name="memberResourceNames")
    def member_resource_names(self) -> Sequence[str]:
        """
        The names of the workspace manager members participating in this group.
        """
        return pulumi.get(self, "member_resource_names")

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
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetWorkspaceManagerGroupResult(GetWorkspaceManagerGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkspaceManagerGroupResult(
            description=self.description,
            display_name=self.display_name,
            etag=self.etag,
            id=self.id,
            member_resource_names=self.member_resource_names,
            name=self.name,
            system_data=self.system_data,
            type=self.type)


def get_workspace_manager_group(resource_group_name: Optional[str] = None,
                                workspace_manager_group_name: Optional[str] = None,
                                workspace_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkspaceManagerGroupResult:
    """
    Gets a workspace manager group


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_manager_group_name: The name of the workspace manager group
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceManagerGroupName'] = workspace_manager_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20230901preview:getWorkspaceManagerGroup', __args__, opts=opts, typ=GetWorkspaceManagerGroupResult).value

    return AwaitableGetWorkspaceManagerGroupResult(
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        member_resource_names=pulumi.get(__ret__, 'member_resource_names'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_workspace_manager_group)
def get_workspace_manager_group_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                       workspace_manager_group_name: Optional[pulumi.Input[str]] = None,
                                       workspace_name: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkspaceManagerGroupResult]:
    """
    Gets a workspace manager group


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_manager_group_name: The name of the workspace manager group
    :param str workspace_name: The name of the workspace.
    """
    ...
