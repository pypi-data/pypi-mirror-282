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
    'ListWorkspaceNotebookAccessTokenResult',
    'AwaitableListWorkspaceNotebookAccessTokenResult',
    'list_workspace_notebook_access_token',
    'list_workspace_notebook_access_token_output',
]

@pulumi.output_type
class ListWorkspaceNotebookAccessTokenResult:
    def __init__(__self__, access_token=None, expires_in=None, host_name=None, notebook_resource_id=None, public_dns=None, refresh_token=None, scope=None, token_type=None):
        if access_token and not isinstance(access_token, str):
            raise TypeError("Expected argument 'access_token' to be a str")
        pulumi.set(__self__, "access_token", access_token)
        if expires_in and not isinstance(expires_in, int):
            raise TypeError("Expected argument 'expires_in' to be a int")
        pulumi.set(__self__, "expires_in", expires_in)
        if host_name and not isinstance(host_name, str):
            raise TypeError("Expected argument 'host_name' to be a str")
        pulumi.set(__self__, "host_name", host_name)
        if notebook_resource_id and not isinstance(notebook_resource_id, str):
            raise TypeError("Expected argument 'notebook_resource_id' to be a str")
        pulumi.set(__self__, "notebook_resource_id", notebook_resource_id)
        if public_dns and not isinstance(public_dns, str):
            raise TypeError("Expected argument 'public_dns' to be a str")
        pulumi.set(__self__, "public_dns", public_dns)
        if refresh_token and not isinstance(refresh_token, str):
            raise TypeError("Expected argument 'refresh_token' to be a str")
        pulumi.set(__self__, "refresh_token", refresh_token)
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        pulumi.set(__self__, "scope", scope)
        if token_type and not isinstance(token_type, str):
            raise TypeError("Expected argument 'token_type' to be a str")
        pulumi.set(__self__, "token_type", token_type)

    @property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> str:
        return pulumi.get(self, "access_token")

    @property
    @pulumi.getter(name="expiresIn")
    def expires_in(self) -> int:
        return pulumi.get(self, "expires_in")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> str:
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter(name="notebookResourceId")
    def notebook_resource_id(self) -> str:
        return pulumi.get(self, "notebook_resource_id")

    @property
    @pulumi.getter(name="publicDns")
    def public_dns(self) -> str:
        return pulumi.get(self, "public_dns")

    @property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> str:
        return pulumi.get(self, "refresh_token")

    @property
    @pulumi.getter
    def scope(self) -> str:
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="tokenType")
    def token_type(self) -> str:
        return pulumi.get(self, "token_type")


class AwaitableListWorkspaceNotebookAccessTokenResult(ListWorkspaceNotebookAccessTokenResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListWorkspaceNotebookAccessTokenResult(
            access_token=self.access_token,
            expires_in=self.expires_in,
            host_name=self.host_name,
            notebook_resource_id=self.notebook_resource_id,
            public_dns=self.public_dns,
            refresh_token=self.refresh_token,
            scope=self.scope,
            token_type=self.token_type)


def list_workspace_notebook_access_token(resource_group_name: Optional[str] = None,
                                         workspace_name: Optional[str] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListWorkspaceNotebookAccessTokenResult:
    """
    return notebook access token and refresh token


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningservices/v20220101preview:listWorkspaceNotebookAccessToken', __args__, opts=opts, typ=ListWorkspaceNotebookAccessTokenResult).value

    return AwaitableListWorkspaceNotebookAccessTokenResult(
        access_token=pulumi.get(__ret__, 'access_token'),
        expires_in=pulumi.get(__ret__, 'expires_in'),
        host_name=pulumi.get(__ret__, 'host_name'),
        notebook_resource_id=pulumi.get(__ret__, 'notebook_resource_id'),
        public_dns=pulumi.get(__ret__, 'public_dns'),
        refresh_token=pulumi.get(__ret__, 'refresh_token'),
        scope=pulumi.get(__ret__, 'scope'),
        token_type=pulumi.get(__ret__, 'token_type'))


@_utilities.lift_output_func(list_workspace_notebook_access_token)
def list_workspace_notebook_access_token_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                                workspace_name: Optional[pulumi.Input[str]] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListWorkspaceNotebookAccessTokenResult]:
    """
    return notebook access token and refresh token


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    ...
