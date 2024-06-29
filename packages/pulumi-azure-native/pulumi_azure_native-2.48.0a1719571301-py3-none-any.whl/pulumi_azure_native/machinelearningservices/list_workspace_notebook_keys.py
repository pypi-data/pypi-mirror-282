# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'ListWorkspaceNotebookKeysResult',
    'AwaitableListWorkspaceNotebookKeysResult',
    'list_workspace_notebook_keys',
    'list_workspace_notebook_keys_output',
]

@pulumi.output_type
class ListWorkspaceNotebookKeysResult:
    def __init__(__self__, primary_access_key=None, secondary_access_key=None):
        if primary_access_key and not isinstance(primary_access_key, str):
            raise TypeError("Expected argument 'primary_access_key' to be a str")
        pulumi.set(__self__, "primary_access_key", primary_access_key)
        if secondary_access_key and not isinstance(secondary_access_key, str):
            raise TypeError("Expected argument 'secondary_access_key' to be a str")
        pulumi.set(__self__, "secondary_access_key", secondary_access_key)

    @property
    @pulumi.getter(name="primaryAccessKey")
    def primary_access_key(self) -> str:
        return pulumi.get(self, "primary_access_key")

    @property
    @pulumi.getter(name="secondaryAccessKey")
    def secondary_access_key(self) -> str:
        return pulumi.get(self, "secondary_access_key")


class AwaitableListWorkspaceNotebookKeysResult(ListWorkspaceNotebookKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListWorkspaceNotebookKeysResult(
            primary_access_key=self.primary_access_key,
            secondary_access_key=self.secondary_access_key)


def list_workspace_notebook_keys(resource_group_name: Optional[str] = None,
                                 workspace_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListWorkspaceNotebookKeysResult:
    """
    List keys of a notebook.
    Azure REST API version: 2023-04-01.

    Other available API versions: 2022-01-01-preview, 2023-04-01-preview, 2023-06-01-preview, 2023-08-01-preview, 2023-10-01, 2024-01-01-preview, 2024-04-01, 2024-04-01-preview.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningservices:listWorkspaceNotebookKeys', __args__, opts=opts, typ=ListWorkspaceNotebookKeysResult).value

    return AwaitableListWorkspaceNotebookKeysResult(
        primary_access_key=pulumi.get(__ret__, 'primary_access_key'),
        secondary_access_key=pulumi.get(__ret__, 'secondary_access_key'))


@_utilities.lift_output_func(list_workspace_notebook_keys)
def list_workspace_notebook_keys_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                        workspace_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListWorkspaceNotebookKeysResult]:
    """
    List keys of a notebook.
    Azure REST API version: 2023-04-01.

    Other available API versions: 2022-01-01-preview, 2023-04-01-preview, 2023-06-01-preview, 2023-08-01-preview, 2023-10-01, 2024-01-01-preview, 2024-04-01, 2024-04-01-preview.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    ...
