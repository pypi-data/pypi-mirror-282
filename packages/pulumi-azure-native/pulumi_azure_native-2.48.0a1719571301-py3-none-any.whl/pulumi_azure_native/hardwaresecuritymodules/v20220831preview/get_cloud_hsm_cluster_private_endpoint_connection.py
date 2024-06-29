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
    'GetCloudHsmClusterPrivateEndpointConnectionResult',
    'AwaitableGetCloudHsmClusterPrivateEndpointConnectionResult',
    'get_cloud_hsm_cluster_private_endpoint_connection',
    'get_cloud_hsm_cluster_private_endpoint_connection_output',
]

@pulumi.output_type
class GetCloudHsmClusterPrivateEndpointConnectionResult:
    """
    The private endpoint connection resource.
    """
    def __init__(__self__, etag=None, group_ids=None, id=None, name=None, private_endpoint=None, private_link_service_connection_state=None, provisioning_state=None, system_data=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if group_ids and not isinstance(group_ids, list):
            raise TypeError("Expected argument 'group_ids' to be a list")
        pulumi.set(__self__, "group_ids", group_ids)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_endpoint and not isinstance(private_endpoint, dict):
            raise TypeError("Expected argument 'private_endpoint' to be a dict")
        pulumi.set(__self__, "private_endpoint", private_endpoint)
        if private_link_service_connection_state and not isinstance(private_link_service_connection_state, dict):
            raise TypeError("Expected argument 'private_link_service_connection_state' to be a dict")
        pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Modified whenever there is a change in the state of private endpoint connection.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Sequence[str]:
        """
        The group ids for the private endpoint resource.
        """
        return pulumi.get(self, "group_ids")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
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
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional['outputs.PrivateEndpointResponse']:
        """
        The private endpoint resource.
        """
        return pulumi.get(self, "private_endpoint")

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> 'outputs.PrivateLinkServiceConnectionStateResponse':
        """
        A collection of information about the state of the connection between service consumer and provider.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the private endpoint connection resource.
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


class AwaitableGetCloudHsmClusterPrivateEndpointConnectionResult(GetCloudHsmClusterPrivateEndpointConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCloudHsmClusterPrivateEndpointConnectionResult(
            etag=self.etag,
            group_ids=self.group_ids,
            id=self.id,
            name=self.name,
            private_endpoint=self.private_endpoint,
            private_link_service_connection_state=self.private_link_service_connection_state,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_cloud_hsm_cluster_private_endpoint_connection(cloud_hsm_cluster_name: Optional[str] = None,
                                                      pe_connection_name: Optional[str] = None,
                                                      resource_group_name: Optional[str] = None,
                                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCloudHsmClusterPrivateEndpointConnectionResult:
    """
    Gets the private endpoint connection for the Cloud Hsm Cluster.


    :param str cloud_hsm_cluster_name: The name of the Cloud HSM Cluster within the specified resource group. Cloud HSM Cluster names must be between 3 and 24 characters in length.
    :param str pe_connection_name: Name of the private endpoint connection associated with the Cloud HSM Cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['cloudHsmClusterName'] = cloud_hsm_cluster_name
    __args__['peConnectionName'] = pe_connection_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:hardwaresecuritymodules/v20220831preview:getCloudHsmClusterPrivateEndpointConnection', __args__, opts=opts, typ=GetCloudHsmClusterPrivateEndpointConnectionResult).value

    return AwaitableGetCloudHsmClusterPrivateEndpointConnectionResult(
        etag=pulumi.get(__ret__, 'etag'),
        group_ids=pulumi.get(__ret__, 'group_ids'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        private_endpoint=pulumi.get(__ret__, 'private_endpoint'),
        private_link_service_connection_state=pulumi.get(__ret__, 'private_link_service_connection_state'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_cloud_hsm_cluster_private_endpoint_connection)
def get_cloud_hsm_cluster_private_endpoint_connection_output(cloud_hsm_cluster_name: Optional[pulumi.Input[str]] = None,
                                                             pe_connection_name: Optional[pulumi.Input[str]] = None,
                                                             resource_group_name: Optional[pulumi.Input[str]] = None,
                                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCloudHsmClusterPrivateEndpointConnectionResult]:
    """
    Gets the private endpoint connection for the Cloud Hsm Cluster.


    :param str cloud_hsm_cluster_name: The name of the Cloud HSM Cluster within the specified resource group. Cloud HSM Cluster names must be between 3 and 24 characters in length.
    :param str pe_connection_name: Name of the private endpoint connection associated with the Cloud HSM Cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
