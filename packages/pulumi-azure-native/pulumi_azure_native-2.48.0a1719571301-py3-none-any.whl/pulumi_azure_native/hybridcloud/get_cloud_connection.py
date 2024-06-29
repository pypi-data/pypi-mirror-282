# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetCloudConnectionResult',
    'AwaitableGetCloudConnectionResult',
    'get_cloud_connection',
    'get_cloud_connection_output',
]

@pulumi.output_type
class GetCloudConnectionResult:
    """
    Resource which represents the managed network connection between Azure Gateways and remote cloud gateways.
    """
    def __init__(__self__, cloud_connector=None, etag=None, id=None, location=None, name=None, provisioning_state=None, remote_resource_id=None, shared_key=None, system_data=None, tags=None, type=None, virtual_hub=None):
        if cloud_connector and not isinstance(cloud_connector, dict):
            raise TypeError("Expected argument 'cloud_connector' to be a dict")
        pulumi.set(__self__, "cloud_connector", cloud_connector)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if remote_resource_id and not isinstance(remote_resource_id, str):
            raise TypeError("Expected argument 'remote_resource_id' to be a str")
        pulumi.set(__self__, "remote_resource_id", remote_resource_id)
        if shared_key and not isinstance(shared_key, str):
            raise TypeError("Expected argument 'shared_key' to be a str")
        pulumi.set(__self__, "shared_key", shared_key)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_hub and not isinstance(virtual_hub, dict):
            raise TypeError("Expected argument 'virtual_hub' to be a dict")
        pulumi.set(__self__, "virtual_hub", virtual_hub)

    @property
    @pulumi.getter(name="cloudConnector")
    def cloud_connector(self) -> Optional['outputs.ResourceReferenceResponse']:
        """
        The cloud connector which discovered the remote resource.
        """
        return pulumi.get(self, "cloud_connector")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
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
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

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
        The provisioning state of the cloud collection resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="remoteResourceId")
    def remote_resource_id(self) -> Optional[str]:
        """
        Identifier for the remote cloud resource
        """
        return pulumi.get(self, "remote_resource_id")

    @property
    @pulumi.getter(name="sharedKey")
    def shared_key(self) -> Optional[str]:
        """
        Shared key of the cloud connection.
        """
        return pulumi.get(self, "shared_key")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> Optional['outputs.ResourceReferenceResponse']:
        """
        The virtualHub to which the cloud connection belongs.
        """
        return pulumi.get(self, "virtual_hub")


class AwaitableGetCloudConnectionResult(GetCloudConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCloudConnectionResult(
            cloud_connector=self.cloud_connector,
            etag=self.etag,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            remote_resource_id=self.remote_resource_id,
            shared_key=self.shared_key,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            virtual_hub=self.virtual_hub)


def get_cloud_connection(cloud_connection_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCloudConnectionResult:
    """
    Gets the specified cloud connection in a specified resource group.
    Azure REST API version: 2023-01-01-preview.


    :param str cloud_connection_name: The name of the cloud connection resource
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['cloudConnectionName'] = cloud_connection_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:hybridcloud:getCloudConnection', __args__, opts=opts, typ=GetCloudConnectionResult).value

    return AwaitableGetCloudConnectionResult(
        cloud_connector=pulumi.get(__ret__, 'cloud_connector'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        remote_resource_id=pulumi.get(__ret__, 'remote_resource_id'),
        shared_key=pulumi.get(__ret__, 'shared_key'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        virtual_hub=pulumi.get(__ret__, 'virtual_hub'))


@_utilities.lift_output_func(get_cloud_connection)
def get_cloud_connection_output(cloud_connection_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCloudConnectionResult]:
    """
    Gets the specified cloud connection in a specified resource group.
    Azure REST API version: 2023-01-01-preview.


    :param str cloud_connection_name: The name of the cloud connection resource
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
