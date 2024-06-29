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
    'ListprovisionedClusterInstanceAdminKubeconfigResult',
    'AwaitableListprovisionedClusterInstanceAdminKubeconfigResult',
    'listprovisioned_cluster_instance_admin_kubeconfig',
    'listprovisioned_cluster_instance_admin_kubeconfig_output',
]

@pulumi.output_type
class ListprovisionedClusterInstanceAdminKubeconfigResult:
    """
    The list kubeconfig result response.
    """
    def __init__(__self__, error=None, id=None, name=None, properties=None, resource_id=None, status=None):
        if error and not isinstance(error, dict):
            raise TypeError("Expected argument 'error' to be a dict")
        pulumi.set(__self__, "error", error)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if resource_id and not isinstance(resource_id, str):
            raise TypeError("Expected argument 'resource_id' to be a str")
        pulumi.set(__self__, "resource_id", resource_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def error(self) -> Optional['outputs.ListCredentialResponseResponseError']:
        return pulumi.get(self, "error")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Operation Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Operation Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.ListCredentialResponseResponseProperties':
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> str:
        """
        ARM Resource Id of the provisioned cluster instance
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Provisioning state of the resource
        """
        return pulumi.get(self, "status")


class AwaitableListprovisionedClusterInstanceAdminKubeconfigResult(ListprovisionedClusterInstanceAdminKubeconfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListprovisionedClusterInstanceAdminKubeconfigResult(
            error=self.error,
            id=self.id,
            name=self.name,
            properties=self.properties,
            resource_id=self.resource_id,
            status=self.status)


def listprovisioned_cluster_instance_admin_kubeconfig(connected_cluster_resource_uri: Optional[str] = None,
                                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListprovisionedClusterInstanceAdminKubeconfigResult:
    """
    Lists the admin credentials of a provisioned cluster instance used only in direct mode.


    :param str connected_cluster_resource_uri: The fully qualified Azure Resource manager identifier of the connected cluster resource.
    """
    __args__ = dict()
    __args__['connectedClusterResourceUri'] = connected_cluster_resource_uri
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:hybridcontainerservice/v20231115preview:listprovisionedClusterInstanceAdminKubeconfig', __args__, opts=opts, typ=ListprovisionedClusterInstanceAdminKubeconfigResult).value

    return AwaitableListprovisionedClusterInstanceAdminKubeconfigResult(
        error=pulumi.get(__ret__, 'error'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        resource_id=pulumi.get(__ret__, 'resource_id'),
        status=pulumi.get(__ret__, 'status'))


@_utilities.lift_output_func(listprovisioned_cluster_instance_admin_kubeconfig)
def listprovisioned_cluster_instance_admin_kubeconfig_output(connected_cluster_resource_uri: Optional[pulumi.Input[str]] = None,
                                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListprovisionedClusterInstanceAdminKubeconfigResult]:
    """
    Lists the admin credentials of a provisioned cluster instance used only in direct mode.


    :param str connected_cluster_resource_uri: The fully qualified Azure Resource manager identifier of the connected cluster resource.
    """
    ...
