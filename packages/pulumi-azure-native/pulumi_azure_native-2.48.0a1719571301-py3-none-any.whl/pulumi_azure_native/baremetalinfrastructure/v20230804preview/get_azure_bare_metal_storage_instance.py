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
    'GetAzureBareMetalStorageInstanceResult',
    'AwaitableGetAzureBareMetalStorageInstanceResult',
    'get_azure_bare_metal_storage_instance',
    'get_azure_bare_metal_storage_instance_output',
]

@pulumi.output_type
class GetAzureBareMetalStorageInstanceResult:
    """
    AzureBareMetalStorageInstance info on Azure (ARM properties and AzureBareMetalStorage properties)
    """
    def __init__(__self__, azure_bare_metal_storage_instance_unique_identifier=None, id=None, location=None, name=None, storage_properties=None, system_data=None, tags=None, type=None):
        if azure_bare_metal_storage_instance_unique_identifier and not isinstance(azure_bare_metal_storage_instance_unique_identifier, str):
            raise TypeError("Expected argument 'azure_bare_metal_storage_instance_unique_identifier' to be a str")
        pulumi.set(__self__, "azure_bare_metal_storage_instance_unique_identifier", azure_bare_metal_storage_instance_unique_identifier)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if storage_properties and not isinstance(storage_properties, dict):
            raise TypeError("Expected argument 'storage_properties' to be a dict")
        pulumi.set(__self__, "storage_properties", storage_properties)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="azureBareMetalStorageInstanceUniqueIdentifier")
    def azure_bare_metal_storage_instance_unique_identifier(self) -> Optional[str]:
        """
        Specifies the AzureBareMetaStorageInstance unique ID.
        """
        return pulumi.get(self, "azure_bare_metal_storage_instance_unique_identifier")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
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
    @pulumi.getter(name="storageProperties")
    def storage_properties(self) -> Optional['outputs.StoragePropertiesResponse']:
        """
        Specifies the storage properties for the AzureBareMetalStorage instance.
        """
        return pulumi.get(self, "storage_properties")

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


class AwaitableGetAzureBareMetalStorageInstanceResult(GetAzureBareMetalStorageInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAzureBareMetalStorageInstanceResult(
            azure_bare_metal_storage_instance_unique_identifier=self.azure_bare_metal_storage_instance_unique_identifier,
            id=self.id,
            location=self.location,
            name=self.name,
            storage_properties=self.storage_properties,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_azure_bare_metal_storage_instance(azure_bare_metal_storage_instance_name: Optional[str] = None,
                                          resource_group_name: Optional[str] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAzureBareMetalStorageInstanceResult:
    """
    Gets an Azure Bare Metal Storage instance for the specified subscription, resource group, and instance name.


    :param str azure_bare_metal_storage_instance_name: Name of the Azure Bare Metal Storage Instance, also known as the ResourceName.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['azureBareMetalStorageInstanceName'] = azure_bare_metal_storage_instance_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:baremetalinfrastructure/v20230804preview:getAzureBareMetalStorageInstance', __args__, opts=opts, typ=GetAzureBareMetalStorageInstanceResult).value

    return AwaitableGetAzureBareMetalStorageInstanceResult(
        azure_bare_metal_storage_instance_unique_identifier=pulumi.get(__ret__, 'azure_bare_metal_storage_instance_unique_identifier'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        storage_properties=pulumi.get(__ret__, 'storage_properties'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_azure_bare_metal_storage_instance)
def get_azure_bare_metal_storage_instance_output(azure_bare_metal_storage_instance_name: Optional[pulumi.Input[str]] = None,
                                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAzureBareMetalStorageInstanceResult]:
    """
    Gets an Azure Bare Metal Storage instance for the specified subscription, resource group, and instance name.


    :param str azure_bare_metal_storage_instance_name: Name of the Azure Bare Metal Storage Instance, also known as the ResourceName.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
