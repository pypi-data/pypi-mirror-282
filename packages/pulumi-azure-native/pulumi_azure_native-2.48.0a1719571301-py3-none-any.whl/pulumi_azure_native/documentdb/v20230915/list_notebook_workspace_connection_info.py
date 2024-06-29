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
    'ListNotebookWorkspaceConnectionInfoResult',
    'AwaitableListNotebookWorkspaceConnectionInfoResult',
    'list_notebook_workspace_connection_info',
    'list_notebook_workspace_connection_info_output',
]

@pulumi.output_type
class ListNotebookWorkspaceConnectionInfoResult:
    """
    The connection info for the given notebook workspace
    """
    def __init__(__self__, auth_token=None, notebook_server_endpoint=None):
        if auth_token and not isinstance(auth_token, str):
            raise TypeError("Expected argument 'auth_token' to be a str")
        pulumi.set(__self__, "auth_token", auth_token)
        if notebook_server_endpoint and not isinstance(notebook_server_endpoint, str):
            raise TypeError("Expected argument 'notebook_server_endpoint' to be a str")
        pulumi.set(__self__, "notebook_server_endpoint", notebook_server_endpoint)

    @property
    @pulumi.getter(name="authToken")
    def auth_token(self) -> str:
        """
        Specifies auth token used for connecting to Notebook server (uses token-based auth).
        """
        return pulumi.get(self, "auth_token")

    @property
    @pulumi.getter(name="notebookServerEndpoint")
    def notebook_server_endpoint(self) -> str:
        """
        Specifies the endpoint of Notebook server.
        """
        return pulumi.get(self, "notebook_server_endpoint")


class AwaitableListNotebookWorkspaceConnectionInfoResult(ListNotebookWorkspaceConnectionInfoResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListNotebookWorkspaceConnectionInfoResult(
            auth_token=self.auth_token,
            notebook_server_endpoint=self.notebook_server_endpoint)


def list_notebook_workspace_connection_info(account_name: Optional[str] = None,
                                            notebook_workspace_name: Optional[str] = None,
                                            resource_group_name: Optional[str] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListNotebookWorkspaceConnectionInfoResult:
    """
    Retrieves the connection info for the notebook workspace


    :param str account_name: Cosmos DB database account name.
    :param str notebook_workspace_name: The name of the notebook workspace resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['notebookWorkspaceName'] = notebook_workspace_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:documentdb/v20230915:listNotebookWorkspaceConnectionInfo', __args__, opts=opts, typ=ListNotebookWorkspaceConnectionInfoResult).value

    return AwaitableListNotebookWorkspaceConnectionInfoResult(
        auth_token=pulumi.get(__ret__, 'auth_token'),
        notebook_server_endpoint=pulumi.get(__ret__, 'notebook_server_endpoint'))


@_utilities.lift_output_func(list_notebook_workspace_connection_info)
def list_notebook_workspace_connection_info_output(account_name: Optional[pulumi.Input[str]] = None,
                                                   notebook_workspace_name: Optional[pulumi.Input[str]] = None,
                                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListNotebookWorkspaceConnectionInfoResult]:
    """
    Retrieves the connection info for the notebook workspace


    :param str account_name: Cosmos DB database account name.
    :param str notebook_workspace_name: The name of the notebook workspace resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
