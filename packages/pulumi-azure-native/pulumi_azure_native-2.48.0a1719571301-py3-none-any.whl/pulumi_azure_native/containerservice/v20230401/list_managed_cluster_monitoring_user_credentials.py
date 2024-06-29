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
    'ListManagedClusterMonitoringUserCredentialsResult',
    'AwaitableListManagedClusterMonitoringUserCredentialsResult',
    'list_managed_cluster_monitoring_user_credentials',
    'list_managed_cluster_monitoring_user_credentials_output',
]

@pulumi.output_type
class ListManagedClusterMonitoringUserCredentialsResult:
    """
    The list credential result response.
    """
    def __init__(__self__, kubeconfigs=None):
        if kubeconfigs and not isinstance(kubeconfigs, list):
            raise TypeError("Expected argument 'kubeconfigs' to be a list")
        pulumi.set(__self__, "kubeconfigs", kubeconfigs)

    @property
    @pulumi.getter
    def kubeconfigs(self) -> Sequence['outputs.CredentialResultResponse']:
        """
        Base64-encoded Kubernetes configuration file.
        """
        return pulumi.get(self, "kubeconfigs")


class AwaitableListManagedClusterMonitoringUserCredentialsResult(ListManagedClusterMonitoringUserCredentialsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListManagedClusterMonitoringUserCredentialsResult(
            kubeconfigs=self.kubeconfigs)


def list_managed_cluster_monitoring_user_credentials(resource_group_name: Optional[str] = None,
                                                     resource_name: Optional[str] = None,
                                                     server_fqdn: Optional[str] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListManagedClusterMonitoringUserCredentialsResult:
    """
    The list credential result response.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the managed cluster resource.
    :param str server_fqdn: server fqdn type for credentials to be returned
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    __args__['serverFqdn'] = server_fqdn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerservice/v20230401:listManagedClusterMonitoringUserCredentials', __args__, opts=opts, typ=ListManagedClusterMonitoringUserCredentialsResult).value

    return AwaitableListManagedClusterMonitoringUserCredentialsResult(
        kubeconfigs=pulumi.get(__ret__, 'kubeconfigs'))


@_utilities.lift_output_func(list_managed_cluster_monitoring_user_credentials)
def list_managed_cluster_monitoring_user_credentials_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                                            resource_name: Optional[pulumi.Input[str]] = None,
                                                            server_fqdn: Optional[pulumi.Input[Optional[str]]] = None,
                                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListManagedClusterMonitoringUserCredentialsResult]:
    """
    The list credential result response.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the managed cluster resource.
    :param str server_fqdn: server fqdn type for credentials to be returned
    """
    ...
