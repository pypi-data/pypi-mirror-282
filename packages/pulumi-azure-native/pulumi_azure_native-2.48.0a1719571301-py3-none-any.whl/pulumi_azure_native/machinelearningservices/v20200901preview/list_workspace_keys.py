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
    'ListWorkspaceKeysResult',
    'AwaitableListWorkspaceKeysResult',
    'list_workspace_keys',
    'list_workspace_keys_output',
]

@pulumi.output_type
class ListWorkspaceKeysResult:
    def __init__(__self__, app_insights_instrumentation_key=None, container_registry_credentials=None, user_storage_key=None, user_storage_resource_id=None):
        if app_insights_instrumentation_key and not isinstance(app_insights_instrumentation_key, str):
            raise TypeError("Expected argument 'app_insights_instrumentation_key' to be a str")
        pulumi.set(__self__, "app_insights_instrumentation_key", app_insights_instrumentation_key)
        if container_registry_credentials and not isinstance(container_registry_credentials, dict):
            raise TypeError("Expected argument 'container_registry_credentials' to be a dict")
        pulumi.set(__self__, "container_registry_credentials", container_registry_credentials)
        if user_storage_key and not isinstance(user_storage_key, str):
            raise TypeError("Expected argument 'user_storage_key' to be a str")
        pulumi.set(__self__, "user_storage_key", user_storage_key)
        if user_storage_resource_id and not isinstance(user_storage_resource_id, str):
            raise TypeError("Expected argument 'user_storage_resource_id' to be a str")
        pulumi.set(__self__, "user_storage_resource_id", user_storage_resource_id)

    @property
    @pulumi.getter(name="appInsightsInstrumentationKey")
    def app_insights_instrumentation_key(self) -> str:
        return pulumi.get(self, "app_insights_instrumentation_key")

    @property
    @pulumi.getter(name="containerRegistryCredentials")
    def container_registry_credentials(self) -> 'outputs.RegistryListCredentialsResultResponse':
        return pulumi.get(self, "container_registry_credentials")

    @property
    @pulumi.getter(name="userStorageKey")
    def user_storage_key(self) -> str:
        return pulumi.get(self, "user_storage_key")

    @property
    @pulumi.getter(name="userStorageResourceId")
    def user_storage_resource_id(self) -> str:
        return pulumi.get(self, "user_storage_resource_id")


class AwaitableListWorkspaceKeysResult(ListWorkspaceKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListWorkspaceKeysResult(
            app_insights_instrumentation_key=self.app_insights_instrumentation_key,
            container_registry_credentials=self.container_registry_credentials,
            user_storage_key=self.user_storage_key,
            user_storage_resource_id=self.user_storage_resource_id)


def list_workspace_keys(resource_group_name: Optional[str] = None,
                        workspace_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListWorkspaceKeysResult:
    """
    Lists all the keys associated with this workspace. This includes keys for the storage account, app insights and password for container registry


    :param str resource_group_name: Name of the resource group in which workspace is located.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningservices/v20200901preview:listWorkspaceKeys', __args__, opts=opts, typ=ListWorkspaceKeysResult).value

    return AwaitableListWorkspaceKeysResult(
        app_insights_instrumentation_key=pulumi.get(__ret__, 'app_insights_instrumentation_key'),
        container_registry_credentials=pulumi.get(__ret__, 'container_registry_credentials'),
        user_storage_key=pulumi.get(__ret__, 'user_storage_key'),
        user_storage_resource_id=pulumi.get(__ret__, 'user_storage_resource_id'))


@_utilities.lift_output_func(list_workspace_keys)
def list_workspace_keys_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                               workspace_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListWorkspaceKeysResult]:
    """
    Lists all the keys associated with this workspace. This includes keys for the storage account, app insights and password for container registry


    :param str resource_group_name: Name of the resource group in which workspace is located.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    ...
