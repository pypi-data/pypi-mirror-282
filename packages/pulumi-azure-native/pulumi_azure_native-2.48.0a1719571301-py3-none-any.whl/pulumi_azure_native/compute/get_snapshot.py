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
    'GetSnapshotResult',
    'AwaitableGetSnapshotResult',
    'get_snapshot',
    'get_snapshot_output',
]

@pulumi.output_type
class GetSnapshotResult:
    """
    Snapshot resource.
    """
    def __init__(__self__, completion_percent=None, copy_completion_error=None, creation_data=None, data_access_auth_mode=None, disk_access_id=None, disk_size_bytes=None, disk_size_gb=None, disk_state=None, encryption=None, encryption_settings_collection=None, extended_location=None, hyper_v_generation=None, id=None, incremental=None, incremental_snapshot_family_id=None, location=None, managed_by=None, name=None, network_access_policy=None, os_type=None, provisioning_state=None, public_network_access=None, purchase_plan=None, security_profile=None, sku=None, supported_capabilities=None, supports_hibernation=None, tags=None, time_created=None, type=None, unique_id=None):
        if completion_percent and not isinstance(completion_percent, float):
            raise TypeError("Expected argument 'completion_percent' to be a float")
        pulumi.set(__self__, "completion_percent", completion_percent)
        if copy_completion_error and not isinstance(copy_completion_error, dict):
            raise TypeError("Expected argument 'copy_completion_error' to be a dict")
        pulumi.set(__self__, "copy_completion_error", copy_completion_error)
        if creation_data and not isinstance(creation_data, dict):
            raise TypeError("Expected argument 'creation_data' to be a dict")
        pulumi.set(__self__, "creation_data", creation_data)
        if data_access_auth_mode and not isinstance(data_access_auth_mode, str):
            raise TypeError("Expected argument 'data_access_auth_mode' to be a str")
        pulumi.set(__self__, "data_access_auth_mode", data_access_auth_mode)
        if disk_access_id and not isinstance(disk_access_id, str):
            raise TypeError("Expected argument 'disk_access_id' to be a str")
        pulumi.set(__self__, "disk_access_id", disk_access_id)
        if disk_size_bytes and not isinstance(disk_size_bytes, float):
            raise TypeError("Expected argument 'disk_size_bytes' to be a float")
        pulumi.set(__self__, "disk_size_bytes", disk_size_bytes)
        if disk_size_gb and not isinstance(disk_size_gb, int):
            raise TypeError("Expected argument 'disk_size_gb' to be a int")
        pulumi.set(__self__, "disk_size_gb", disk_size_gb)
        if disk_state and not isinstance(disk_state, str):
            raise TypeError("Expected argument 'disk_state' to be a str")
        pulumi.set(__self__, "disk_state", disk_state)
        if encryption and not isinstance(encryption, dict):
            raise TypeError("Expected argument 'encryption' to be a dict")
        pulumi.set(__self__, "encryption", encryption)
        if encryption_settings_collection and not isinstance(encryption_settings_collection, dict):
            raise TypeError("Expected argument 'encryption_settings_collection' to be a dict")
        pulumi.set(__self__, "encryption_settings_collection", encryption_settings_collection)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if hyper_v_generation and not isinstance(hyper_v_generation, str):
            raise TypeError("Expected argument 'hyper_v_generation' to be a str")
        pulumi.set(__self__, "hyper_v_generation", hyper_v_generation)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if incremental and not isinstance(incremental, bool):
            raise TypeError("Expected argument 'incremental' to be a bool")
        pulumi.set(__self__, "incremental", incremental)
        if incremental_snapshot_family_id and not isinstance(incremental_snapshot_family_id, str):
            raise TypeError("Expected argument 'incremental_snapshot_family_id' to be a str")
        pulumi.set(__self__, "incremental_snapshot_family_id", incremental_snapshot_family_id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if managed_by and not isinstance(managed_by, str):
            raise TypeError("Expected argument 'managed_by' to be a str")
        pulumi.set(__self__, "managed_by", managed_by)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_access_policy and not isinstance(network_access_policy, str):
            raise TypeError("Expected argument 'network_access_policy' to be a str")
        pulumi.set(__self__, "network_access_policy", network_access_policy)
        if os_type and not isinstance(os_type, str):
            raise TypeError("Expected argument 'os_type' to be a str")
        pulumi.set(__self__, "os_type", os_type)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_network_access and not isinstance(public_network_access, str):
            raise TypeError("Expected argument 'public_network_access' to be a str")
        pulumi.set(__self__, "public_network_access", public_network_access)
        if purchase_plan and not isinstance(purchase_plan, dict):
            raise TypeError("Expected argument 'purchase_plan' to be a dict")
        pulumi.set(__self__, "purchase_plan", purchase_plan)
        if security_profile and not isinstance(security_profile, dict):
            raise TypeError("Expected argument 'security_profile' to be a dict")
        pulumi.set(__self__, "security_profile", security_profile)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if supported_capabilities and not isinstance(supported_capabilities, dict):
            raise TypeError("Expected argument 'supported_capabilities' to be a dict")
        pulumi.set(__self__, "supported_capabilities", supported_capabilities)
        if supports_hibernation and not isinstance(supports_hibernation, bool):
            raise TypeError("Expected argument 'supports_hibernation' to be a bool")
        pulumi.set(__self__, "supports_hibernation", supports_hibernation)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if unique_id and not isinstance(unique_id, str):
            raise TypeError("Expected argument 'unique_id' to be a str")
        pulumi.set(__self__, "unique_id", unique_id)

    @property
    @pulumi.getter(name="completionPercent")
    def completion_percent(self) -> Optional[float]:
        """
        Percentage complete for the background copy when a resource is created via the CopyStart operation.
        """
        return pulumi.get(self, "completion_percent")

    @property
    @pulumi.getter(name="copyCompletionError")
    def copy_completion_error(self) -> Optional['outputs.CopyCompletionErrorResponse']:
        """
        Indicates the error details if the background copy of a resource created via the CopyStart operation fails.
        """
        return pulumi.get(self, "copy_completion_error")

    @property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> 'outputs.CreationDataResponse':
        """
        Disk source information. CreationData information cannot be changed after the disk has been created.
        """
        return pulumi.get(self, "creation_data")

    @property
    @pulumi.getter(name="dataAccessAuthMode")
    def data_access_auth_mode(self) -> Optional[str]:
        """
        Additional authentication requirements when exporting or uploading to a disk or snapshot.
        """
        return pulumi.get(self, "data_access_auth_mode")

    @property
    @pulumi.getter(name="diskAccessId")
    def disk_access_id(self) -> Optional[str]:
        """
        ARM id of the DiskAccess resource for using private endpoints on disks.
        """
        return pulumi.get(self, "disk_access_id")

    @property
    @pulumi.getter(name="diskSizeBytes")
    def disk_size_bytes(self) -> float:
        """
        The size of the disk in bytes. This field is read only.
        """
        return pulumi.get(self, "disk_size_bytes")

    @property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[int]:
        """
        If creationData.createOption is Empty, this field is mandatory and it indicates the size of the disk to create. If this field is present for updates or creation with other options, it indicates a resize. Resizes are only allowed if the disk is not attached to a running VM, and can only increase the disk's size.
        """
        return pulumi.get(self, "disk_size_gb")

    @property
    @pulumi.getter(name="diskState")
    def disk_state(self) -> str:
        """
        The state of the snapshot.
        """
        return pulumi.get(self, "disk_state")

    @property
    @pulumi.getter
    def encryption(self) -> Optional['outputs.EncryptionResponse']:
        """
        Encryption property can be used to encrypt data at rest with customer managed keys or platform managed keys.
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter(name="encryptionSettingsCollection")
    def encryption_settings_collection(self) -> Optional['outputs.EncryptionSettingsCollectionResponse']:
        """
        Encryption settings collection used be Azure Disk Encryption, can contain multiple encryption settings per disk or snapshot.
        """
        return pulumi.get(self, "encryption_settings_collection")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional['outputs.ExtendedLocationResponse']:
        """
        The extended location where the snapshot will be created. Extended location cannot be changed.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(self) -> Optional[str]:
        """
        The hypervisor generation of the Virtual Machine. Applicable to OS disks only.
        """
        return pulumi.get(self, "hyper_v_generation")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def incremental(self) -> Optional[bool]:
        """
        Whether a snapshot is incremental. Incremental snapshots on the same disk occupy less space than full snapshots and can be diffed.
        """
        return pulumi.get(self, "incremental")

    @property
    @pulumi.getter(name="incrementalSnapshotFamilyId")
    def incremental_snapshot_family_id(self) -> str:
        """
        Incremental snapshots for a disk share an incremental snapshot family id. The Get Page Range Diff API can only be called on incremental snapshots with the same family id.
        """
        return pulumi.get(self, "incremental_snapshot_family_id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> str:
        """
        Unused. Always Null.
        """
        return pulumi.get(self, "managed_by")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkAccessPolicy")
    def network_access_policy(self) -> Optional[str]:
        """
        Policy for accessing the disk via network.
        """
        return pulumi.get(self, "network_access_policy")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[str]:
        """
        The Operating System type.
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The disk provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[str]:
        """
        Policy for controlling export on the disk.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="purchasePlan")
    def purchase_plan(self) -> Optional['outputs.PurchasePlanResponse']:
        """
        Purchase plan information for the image from which the source disk for the snapshot was originally created.
        """
        return pulumi.get(self, "purchase_plan")

    @property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional['outputs.DiskSecurityProfileResponse']:
        """
        Contains the security related information for the resource.
        """
        return pulumi.get(self, "security_profile")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SnapshotSkuResponse']:
        """
        The snapshots sku name. Can be Standard_LRS, Premium_LRS, or Standard_ZRS. This is an optional parameter for incremental snapshot and the default behavior is the SKU will be set to the same sku as the previous snapshot
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="supportedCapabilities")
    def supported_capabilities(self) -> Optional['outputs.SupportedCapabilitiesResponse']:
        """
        List of supported capabilities for the image from which the source disk from the snapshot was originally created.
        """
        return pulumi.get(self, "supported_capabilities")

    @property
    @pulumi.getter(name="supportsHibernation")
    def supports_hibernation(self) -> Optional[bool]:
        """
        Indicates the OS on a snapshot supports hibernation.
        """
        return pulumi.get(self, "supports_hibernation")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The time when the snapshot was created.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> str:
        """
        Unique Guid identifying the resource.
        """
        return pulumi.get(self, "unique_id")


class AwaitableGetSnapshotResult(GetSnapshotResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSnapshotResult(
            completion_percent=self.completion_percent,
            copy_completion_error=self.copy_completion_error,
            creation_data=self.creation_data,
            data_access_auth_mode=self.data_access_auth_mode,
            disk_access_id=self.disk_access_id,
            disk_size_bytes=self.disk_size_bytes,
            disk_size_gb=self.disk_size_gb,
            disk_state=self.disk_state,
            encryption=self.encryption,
            encryption_settings_collection=self.encryption_settings_collection,
            extended_location=self.extended_location,
            hyper_v_generation=self.hyper_v_generation,
            id=self.id,
            incremental=self.incremental,
            incremental_snapshot_family_id=self.incremental_snapshot_family_id,
            location=self.location,
            managed_by=self.managed_by,
            name=self.name,
            network_access_policy=self.network_access_policy,
            os_type=self.os_type,
            provisioning_state=self.provisioning_state,
            public_network_access=self.public_network_access,
            purchase_plan=self.purchase_plan,
            security_profile=self.security_profile,
            sku=self.sku,
            supported_capabilities=self.supported_capabilities,
            supports_hibernation=self.supports_hibernation,
            tags=self.tags,
            time_created=self.time_created,
            type=self.type,
            unique_id=self.unique_id)


def get_snapshot(resource_group_name: Optional[str] = None,
                 snapshot_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSnapshotResult:
    """
    Gets information about a snapshot.
    Azure REST API version: 2022-07-02.

    Other available API versions: 2016-04-30-preview, 2017-03-30, 2018-06-01, 2023-01-02, 2023-04-02, 2023-10-02.


    :param str resource_group_name: The name of the resource group.
    :param str snapshot_name: The name of the snapshot that is being created. The name can't be changed after the snapshot is created. Supported characters for the name are a-z, A-Z, 0-9, _ and -. The max name length is 80 characters.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['snapshotName'] = snapshot_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:compute:getSnapshot', __args__, opts=opts, typ=GetSnapshotResult).value

    return AwaitableGetSnapshotResult(
        completion_percent=pulumi.get(__ret__, 'completion_percent'),
        copy_completion_error=pulumi.get(__ret__, 'copy_completion_error'),
        creation_data=pulumi.get(__ret__, 'creation_data'),
        data_access_auth_mode=pulumi.get(__ret__, 'data_access_auth_mode'),
        disk_access_id=pulumi.get(__ret__, 'disk_access_id'),
        disk_size_bytes=pulumi.get(__ret__, 'disk_size_bytes'),
        disk_size_gb=pulumi.get(__ret__, 'disk_size_gb'),
        disk_state=pulumi.get(__ret__, 'disk_state'),
        encryption=pulumi.get(__ret__, 'encryption'),
        encryption_settings_collection=pulumi.get(__ret__, 'encryption_settings_collection'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        hyper_v_generation=pulumi.get(__ret__, 'hyper_v_generation'),
        id=pulumi.get(__ret__, 'id'),
        incremental=pulumi.get(__ret__, 'incremental'),
        incremental_snapshot_family_id=pulumi.get(__ret__, 'incremental_snapshot_family_id'),
        location=pulumi.get(__ret__, 'location'),
        managed_by=pulumi.get(__ret__, 'managed_by'),
        name=pulumi.get(__ret__, 'name'),
        network_access_policy=pulumi.get(__ret__, 'network_access_policy'),
        os_type=pulumi.get(__ret__, 'os_type'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        public_network_access=pulumi.get(__ret__, 'public_network_access'),
        purchase_plan=pulumi.get(__ret__, 'purchase_plan'),
        security_profile=pulumi.get(__ret__, 'security_profile'),
        sku=pulumi.get(__ret__, 'sku'),
        supported_capabilities=pulumi.get(__ret__, 'supported_capabilities'),
        supports_hibernation=pulumi.get(__ret__, 'supports_hibernation'),
        tags=pulumi.get(__ret__, 'tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        type=pulumi.get(__ret__, 'type'),
        unique_id=pulumi.get(__ret__, 'unique_id'))


@_utilities.lift_output_func(get_snapshot)
def get_snapshot_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                        snapshot_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSnapshotResult]:
    """
    Gets information about a snapshot.
    Azure REST API version: 2022-07-02.

    Other available API versions: 2016-04-30-preview, 2017-03-30, 2018-06-01, 2023-01-02, 2023-04-02, 2023-10-02.


    :param str resource_group_name: The name of the resource group.
    :param str snapshot_name: The name of the snapshot that is being created. The name can't be changed after the snapshot is created. Supported characters for the name are a-z, A-Z, 0-9, _ and -. The max name length is 80 characters.
    """
    ...
