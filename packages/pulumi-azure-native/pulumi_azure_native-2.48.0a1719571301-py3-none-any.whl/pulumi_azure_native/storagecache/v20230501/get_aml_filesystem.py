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
    'GetAmlFilesystemResult',
    'AwaitableGetAmlFilesystemResult',
    'get_aml_filesystem',
    'get_aml_filesystem_output',
]

@pulumi.output_type
class GetAmlFilesystemResult:
    """
    An AML file system instance. Follows Azure Resource Manager standards: https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/resource-api-reference.md
    """
    def __init__(__self__, client_info=None, encryption_settings=None, filesystem_subnet=None, health=None, hsm=None, id=None, identity=None, location=None, maintenance_window=None, name=None, provisioning_state=None, sku=None, storage_capacity_ti_b=None, system_data=None, tags=None, throughput_provisioned_m_bps=None, type=None, zones=None):
        if client_info and not isinstance(client_info, dict):
            raise TypeError("Expected argument 'client_info' to be a dict")
        pulumi.set(__self__, "client_info", client_info)
        if encryption_settings and not isinstance(encryption_settings, dict):
            raise TypeError("Expected argument 'encryption_settings' to be a dict")
        pulumi.set(__self__, "encryption_settings", encryption_settings)
        if filesystem_subnet and not isinstance(filesystem_subnet, str):
            raise TypeError("Expected argument 'filesystem_subnet' to be a str")
        pulumi.set(__self__, "filesystem_subnet", filesystem_subnet)
        if health and not isinstance(health, dict):
            raise TypeError("Expected argument 'health' to be a dict")
        pulumi.set(__self__, "health", health)
        if hsm and not isinstance(hsm, dict):
            raise TypeError("Expected argument 'hsm' to be a dict")
        pulumi.set(__self__, "hsm", hsm)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if maintenance_window and not isinstance(maintenance_window, dict):
            raise TypeError("Expected argument 'maintenance_window' to be a dict")
        pulumi.set(__self__, "maintenance_window", maintenance_window)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if storage_capacity_ti_b and not isinstance(storage_capacity_ti_b, float):
            raise TypeError("Expected argument 'storage_capacity_ti_b' to be a float")
        pulumi.set(__self__, "storage_capacity_ti_b", storage_capacity_ti_b)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if throughput_provisioned_m_bps and not isinstance(throughput_provisioned_m_bps, int):
            raise TypeError("Expected argument 'throughput_provisioned_m_bps' to be a int")
        pulumi.set(__self__, "throughput_provisioned_m_bps", throughput_provisioned_m_bps)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if zones and not isinstance(zones, list):
            raise TypeError("Expected argument 'zones' to be a list")
        pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter(name="clientInfo")
    def client_info(self) -> 'outputs.AmlFilesystemClientInfoResponse':
        """
        Client information for the AML file system.
        """
        return pulumi.get(self, "client_info")

    @property
    @pulumi.getter(name="encryptionSettings")
    def encryption_settings(self) -> Optional['outputs.AmlFilesystemEncryptionSettingsResponse']:
        """
        Specifies encryption settings of the AML file system.
        """
        return pulumi.get(self, "encryption_settings")

    @property
    @pulumi.getter(name="filesystemSubnet")
    def filesystem_subnet(self) -> str:
        """
        Subnet used for managing the AML file system and for client-facing operations. This subnet should have at least a /24 subnet mask within the VNET's address space.
        """
        return pulumi.get(self, "filesystem_subnet")

    @property
    @pulumi.getter
    def health(self) -> 'outputs.AmlFilesystemHealthResponse':
        """
        Health of the AML file system.
        """
        return pulumi.get(self, "health")

    @property
    @pulumi.getter
    def hsm(self) -> Optional['outputs.AmlFilesystemResponseHsm']:
        """
        Hydration and archive settings and status
        """
        return pulumi.get(self, "hsm")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.AmlFilesystemIdentityResponse']:
        """
        The managed identity used by the AML file system, if configured.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> 'outputs.AmlFilesystemResponseMaintenanceWindow':
        """
        Start time of a 30-minute weekly maintenance window.
        """
        return pulumi.get(self, "maintenance_window")

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
        ARM provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuNameResponse']:
        """
        SKU for the resource.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="storageCapacityTiB")
    def storage_capacity_ti_b(self) -> float:
        """
        The size of the AML file system, in TiB. This might be rounded up.
        """
        return pulumi.get(self, "storage_capacity_ti_b")

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
    @pulumi.getter(name="throughputProvisionedMBps")
    def throughput_provisioned_m_bps(self) -> int:
        """
        Throughput provisioned in MB per sec, calculated as storageCapacityTiB * per-unit storage throughput
        """
        return pulumi.get(self, "throughput_provisioned_m_bps")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[str]]:
        """
        Availability zones for resources. This field should only contain a single element in the array.
        """
        return pulumi.get(self, "zones")


class AwaitableGetAmlFilesystemResult(GetAmlFilesystemResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAmlFilesystemResult(
            client_info=self.client_info,
            encryption_settings=self.encryption_settings,
            filesystem_subnet=self.filesystem_subnet,
            health=self.health,
            hsm=self.hsm,
            id=self.id,
            identity=self.identity,
            location=self.location,
            maintenance_window=self.maintenance_window,
            name=self.name,
            provisioning_state=self.provisioning_state,
            sku=self.sku,
            storage_capacity_ti_b=self.storage_capacity_ti_b,
            system_data=self.system_data,
            tags=self.tags,
            throughput_provisioned_m_bps=self.throughput_provisioned_m_bps,
            type=self.type,
            zones=self.zones)


def get_aml_filesystem(aml_filesystem_name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAmlFilesystemResult:
    """
    Returns an AML file system.


    :param str aml_filesystem_name: Name for the AML file system. Allows alphanumerics, underscores, and hyphens. Start and end with alphanumeric.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['amlFilesystemName'] = aml_filesystem_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:storagecache/v20230501:getAmlFilesystem', __args__, opts=opts, typ=GetAmlFilesystemResult).value

    return AwaitableGetAmlFilesystemResult(
        client_info=pulumi.get(__ret__, 'client_info'),
        encryption_settings=pulumi.get(__ret__, 'encryption_settings'),
        filesystem_subnet=pulumi.get(__ret__, 'filesystem_subnet'),
        health=pulumi.get(__ret__, 'health'),
        hsm=pulumi.get(__ret__, 'hsm'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        location=pulumi.get(__ret__, 'location'),
        maintenance_window=pulumi.get(__ret__, 'maintenance_window'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        sku=pulumi.get(__ret__, 'sku'),
        storage_capacity_ti_b=pulumi.get(__ret__, 'storage_capacity_ti_b'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        throughput_provisioned_m_bps=pulumi.get(__ret__, 'throughput_provisioned_m_bps'),
        type=pulumi.get(__ret__, 'type'),
        zones=pulumi.get(__ret__, 'zones'))


@_utilities.lift_output_func(get_aml_filesystem)
def get_aml_filesystem_output(aml_filesystem_name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAmlFilesystemResult]:
    """
    Returns an AML file system.


    :param str aml_filesystem_name: Name for the AML file system. Allows alphanumerics, underscores, and hyphens. Start and end with alphanumeric.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
