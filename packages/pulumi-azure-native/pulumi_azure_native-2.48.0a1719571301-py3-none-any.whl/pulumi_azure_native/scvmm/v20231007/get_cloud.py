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
    'GetCloudResult',
    'AwaitableGetCloudResult',
    'get_cloud',
    'get_cloud_output',
]

@pulumi.output_type
class GetCloudResult:
    """
    The Clouds resource definition.
    """
    def __init__(__self__, cloud_capacity=None, cloud_name=None, extended_location=None, id=None, inventory_item_id=None, location=None, name=None, provisioning_state=None, storage_qos_policies=None, system_data=None, tags=None, type=None, uuid=None, vmm_server_id=None):
        if cloud_capacity and not isinstance(cloud_capacity, dict):
            raise TypeError("Expected argument 'cloud_capacity' to be a dict")
        pulumi.set(__self__, "cloud_capacity", cloud_capacity)
        if cloud_name and not isinstance(cloud_name, str):
            raise TypeError("Expected argument 'cloud_name' to be a str")
        pulumi.set(__self__, "cloud_name", cloud_name)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if inventory_item_id and not isinstance(inventory_item_id, str):
            raise TypeError("Expected argument 'inventory_item_id' to be a str")
        pulumi.set(__self__, "inventory_item_id", inventory_item_id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if storage_qos_policies and not isinstance(storage_qos_policies, list):
            raise TypeError("Expected argument 'storage_qos_policies' to be a list")
        pulumi.set(__self__, "storage_qos_policies", storage_qos_policies)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if uuid and not isinstance(uuid, str):
            raise TypeError("Expected argument 'uuid' to be a str")
        pulumi.set(__self__, "uuid", uuid)
        if vmm_server_id and not isinstance(vmm_server_id, str):
            raise TypeError("Expected argument 'vmm_server_id' to be a str")
        pulumi.set(__self__, "vmm_server_id", vmm_server_id)

    @property
    @pulumi.getter(name="cloudCapacity")
    def cloud_capacity(self) -> 'outputs.CloudCapacityResponse':
        """
        Capacity of the cloud.
        """
        return pulumi.get(self, "cloud_capacity")

    @property
    @pulumi.getter(name="cloudName")
    def cloud_name(self) -> str:
        """
        Name of the cloud in VmmServer.
        """
        return pulumi.get(self, "cloud_name")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> 'outputs.ExtendedLocationResponse':
        """
        The extended location.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="inventoryItemId")
    def inventory_item_id(self) -> Optional[str]:
        """
        Gets or sets the inventory Item ID for the resource.
        """
        return pulumi.get(self, "inventory_item_id")

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
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="storageQosPolicies")
    def storage_qos_policies(self) -> Sequence['outputs.StorageQosPolicyResponse']:
        """
        List of QoS policies available for the cloud.
        """
        return pulumi.get(self, "storage_qos_policies")

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
    @pulumi.getter
    def uuid(self) -> Optional[str]:
        """
        Unique ID of the cloud.
        """
        return pulumi.get(self, "uuid")

    @property
    @pulumi.getter(name="vmmServerId")
    def vmm_server_id(self) -> Optional[str]:
        """
        ARM Id of the vmmServer resource in which this resource resides.
        """
        return pulumi.get(self, "vmm_server_id")


class AwaitableGetCloudResult(GetCloudResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCloudResult(
            cloud_capacity=self.cloud_capacity,
            cloud_name=self.cloud_name,
            extended_location=self.extended_location,
            id=self.id,
            inventory_item_id=self.inventory_item_id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            storage_qos_policies=self.storage_qos_policies,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            uuid=self.uuid,
            vmm_server_id=self.vmm_server_id)


def get_cloud(cloud_resource_name: Optional[str] = None,
              resource_group_name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCloudResult:
    """
    Implements Cloud GET method.


    :param str cloud_resource_name: Name of the Cloud.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['cloudResourceName'] = cloud_resource_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:scvmm/v20231007:getCloud', __args__, opts=opts, typ=GetCloudResult).value

    return AwaitableGetCloudResult(
        cloud_capacity=pulumi.get(__ret__, 'cloud_capacity'),
        cloud_name=pulumi.get(__ret__, 'cloud_name'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        id=pulumi.get(__ret__, 'id'),
        inventory_item_id=pulumi.get(__ret__, 'inventory_item_id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        storage_qos_policies=pulumi.get(__ret__, 'storage_qos_policies'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        uuid=pulumi.get(__ret__, 'uuid'),
        vmm_server_id=pulumi.get(__ret__, 'vmm_server_id'))


@_utilities.lift_output_func(get_cloud)
def get_cloud_output(cloud_resource_name: Optional[pulumi.Input[str]] = None,
                     resource_group_name: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCloudResult]:
    """
    Implements Cloud GET method.


    :param str cloud_resource_name: Name of the Cloud.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
