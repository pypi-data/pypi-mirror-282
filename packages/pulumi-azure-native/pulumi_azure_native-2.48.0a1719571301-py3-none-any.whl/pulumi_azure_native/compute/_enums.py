# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'Architecture',
    'CachingTypes',
    'CloudServiceSlotType',
    'CloudServiceUpgradeMode',
    'ComponentNames',
    'ConfidentialVMEncryptionType',
    'ConsistencyModeTypes',
    'CopyCompletionErrorReason',
    'DataAccessAuthMode',
    'DedicatedHostLicenseTypes',
    'DeleteOptions',
    'DiffDiskOptions',
    'DiffDiskPlacement',
    'DiskControllerTypes',
    'DiskCreateOption',
    'DiskCreateOptionTypes',
    'DiskDeleteOptionTypes',
    'DiskDetachOptionTypes',
    'DiskEncryptionSetIdentityType',
    'DiskEncryptionSetType',
    'DiskSecurityTypes',
    'DiskStorageAccountTypes',
    'EdgeZoneStorageAccountType',
    'EncryptionType',
    'ExtendedLocationTypes',
    'GalleryApplicationCustomActionParameterType',
    'GalleryExtendedLocationType',
    'GallerySharingPermissionTypes',
    'HostCaching',
    'HyperVGeneration',
    'HyperVGenerationTypes',
    'IPVersion',
    'IPVersions',
    'IntervalInMins',
    'LinuxPatchAssessmentMode',
    'LinuxVMGuestPatchAutomaticByPlatformRebootSetting',
    'LinuxVMGuestPatchMode',
    'NetworkAccessPolicy',
    'NetworkApiVersion',
    'OperatingSystemStateTypes',
    'OperatingSystemTypes',
    'OrchestrationMode',
    'PassNames',
    'PrivateEndpointServiceConnectionStatus',
    'ProtocolTypes',
    'ProximityPlacementGroupType',
    'PublicIPAddressSkuName',
    'PublicIPAddressSkuTier',
    'PublicIPAllocationMethod',
    'PublicNetworkAccess',
    'RepairAction',
    'ReplicationMode',
    'ResourceIdentityType',
    'RestorePointEncryptionType',
    'SecurityEncryptionTypes',
    'SecurityTypes',
    'SettingNames',
    'SnapshotStorageAccountTypes',
    'StatusLevelTypes',
    'StorageAccountType',
    'StorageAccountTypes',
    'UpgradeMode',
    'VirtualMachineEvictionPolicyTypes',
    'VirtualMachinePriorityTypes',
    'VirtualMachineScaleSetScaleInRules',
    'VirtualMachineSizeTypes',
    'WindowsPatchAssessmentMode',
    'WindowsVMGuestPatchAutomaticByPlatformRebootSetting',
    'WindowsVMGuestPatchMode',
]


class Architecture(str, Enum):
    """
    CPU architecture supported by an OS disk.
    """
    X64 = "x64"
    ARM64 = "Arm64"


class CachingTypes(str, Enum):
    """
    Specifies the caching requirements. Possible values are: **None,** **ReadOnly,** **ReadWrite.** The defaulting behavior is: **None for Standard storage. ReadOnly for Premium storage.**
    """
    NONE = "None"
    READ_ONLY = "ReadOnly"
    READ_WRITE = "ReadWrite"


class CloudServiceSlotType(str, Enum):
    """
    Slot type for the cloud service.
    Possible values are <br /><br />**Production**<br /><br />**Staging**<br /><br />
    If not specified, the default value is Production.
    """
    PRODUCTION = "Production"
    STAGING = "Staging"


class CloudServiceUpgradeMode(str, Enum):
    """
    Update mode for the cloud service. Role instances are allocated to update domains when the service is deployed. Updates can be initiated manually in each update domain or initiated automatically in all update domains.
    Possible Values are <br /><br />**Auto**<br /><br />**Manual** <br /><br />**Simultaneous**<br /><br />
    If not specified, the default value is Auto. If set to Manual, PUT UpdateDomain must be called to apply the update. If set to Auto, the update is automatically applied to each update domain in sequence.
    """
    AUTO = "Auto"
    MANUAL = "Manual"
    SIMULTANEOUS = "Simultaneous"


class ComponentNames(str, Enum):
    """
    The component name. Currently, the only allowable value is Microsoft-Windows-Shell-Setup.
    """
    MICROSOFT_WINDOWS_SHELL_SETUP = "Microsoft-Windows-Shell-Setup"


class ConfidentialVMEncryptionType(str, Enum):
    """
    confidential VM encryption types
    """
    ENCRYPTED_VM_GUEST_STATE_ONLY_WITH_PMK = "EncryptedVMGuestStateOnlyWithPmk"
    ENCRYPTED_WITH_PMK = "EncryptedWithPmk"
    ENCRYPTED_WITH_CMK = "EncryptedWithCmk"


class ConsistencyModeTypes(str, Enum):
    """
    ConsistencyMode of the RestorePoint. Can be specified in the input while creating a restore point. For now, only CrashConsistent is accepted as a valid input. Please refer to https://aka.ms/RestorePoints for more details.
    """
    CRASH_CONSISTENT = "CrashConsistent"
    FILE_SYSTEM_CONSISTENT = "FileSystemConsistent"
    APPLICATION_CONSISTENT = "ApplicationConsistent"


class CopyCompletionErrorReason(str, Enum):
    """
    Indicates the error code if the background copy of a resource created via the CopyStart operation fails.
    """
    COPY_SOURCE_NOT_FOUND = "CopySourceNotFound"
    """
    Indicates that the source snapshot was deleted while the background copy of the resource created via CopyStart operation was in progress.
    """


class DataAccessAuthMode(str, Enum):
    """
    Additional authentication requirements when exporting or uploading to a disk or snapshot.
    """
    AZURE_ACTIVE_DIRECTORY = "AzureActiveDirectory"
    """
    When export/upload URL is used, the system checks if the user has an identity in Azure Active Directory and has necessary permissions to export/upload the data. Please refer to aka.ms/DisksAzureADAuth.
    """
    NONE = "None"
    """
    No additional authentication would be performed when accessing export/upload URL.
    """


class DedicatedHostLicenseTypes(str, Enum):
    """
    Specifies the software license type that will be applied to the VMs deployed on the dedicated host. Possible values are: **None,** **Windows_Server_Hybrid,** **Windows_Server_Perpetual.** The default value is: **None.**
    """
    NONE = "None"
    WINDOWS_SERVER_HYBRID = "Windows_Server_Hybrid"
    WINDOWS_SERVER_PERPETUAL = "Windows_Server_Perpetual"


class DeleteOptions(str, Enum):
    """
    Specify what happens to the public IP when the VM is deleted
    """
    DELETE = "Delete"
    DETACH = "Detach"


class DiffDiskOptions(str, Enum):
    """
    Specifies the ephemeral disk settings for operating system disk.
    """
    LOCAL = "Local"


class DiffDiskPlacement(str, Enum):
    """
    Specifies the ephemeral disk placement for operating system disk. Possible values are: **CacheDisk,** **ResourceDisk.** The defaulting behavior is: **CacheDisk** if one is configured for the VM size otherwise **ResourceDisk** is used. Refer to the VM size documentation for Windows VM at https://docs.microsoft.com/azure/virtual-machines/windows/sizes and Linux VM at https://docs.microsoft.com/azure/virtual-machines/linux/sizes to check which VM sizes exposes a cache disk.
    """
    CACHE_DISK = "CacheDisk"
    RESOURCE_DISK = "ResourceDisk"


class DiskControllerTypes(str, Enum):
    """
    Specifies the disk controller type configured for the VM. **Note:** This property will be set to the default disk controller type if not specified provided virtual machine is being created with 'hyperVGeneration' set to V2 based on the capabilities of the operating system disk and VM size from the the specified minimum api version. You need to deallocate the VM before updating its disk controller type unless you are updating the VM size in the VM configuration which implicitly deallocates and reallocates the VM. Minimum api-version: 2022-08-01.
    """
    SCSI = "SCSI"
    NV_ME = "NVMe"


class DiskCreateOption(str, Enum):
    """
    This enumerates the possible sources of a disk's creation.
    """
    EMPTY = "Empty"
    """
    Create an empty data disk of a size given by diskSizeGB.
    """
    ATTACH = "Attach"
    """
    Disk will be attached to a VM.
    """
    FROM_IMAGE = "FromImage"
    """
    Create a new disk from a platform image specified by the given imageReference or galleryImageReference.
    """
    IMPORT_ = "Import"
    """
    Create a disk by importing from a blob specified by a sourceUri in a storage account specified by storageAccountId.
    """
    COPY = "Copy"
    """
    Create a new disk or snapshot by copying from a disk or snapshot specified by the given sourceResourceId.
    """
    RESTORE = "Restore"
    """
    Create a new disk by copying from a backup recovery point.
    """
    UPLOAD = "Upload"
    """
    Create a new disk by obtaining a write token and using it to directly upload the contents of the disk.
    """
    COPY_START = "CopyStart"
    """
    Create a new disk by using a deep copy process, where the resource creation is considered complete only after all data has been copied from the source.
    """
    IMPORT_SECURE = "ImportSecure"
    """
    Similar to Import create option. Create a new Trusted Launch VM or Confidential VM supported disk by importing additional blob for VM guest state specified by securityDataUri in storage account specified by storageAccountId
    """
    UPLOAD_PREPARED_SECURE = "UploadPreparedSecure"
    """
    Similar to Upload create option. Create a new Trusted Launch VM or Confidential VM supported disk and upload using write token in both disk and VM guest state
    """


class DiskCreateOptionTypes(str, Enum):
    """
    Specifies how the virtual machine should be created. Possible values are: **Attach.** This value is used when you are using a specialized disk to create the virtual machine. **FromImage.** This value is used when you are using an image to create the virtual machine. If you are using a platform image, you should also use the imageReference element described above. If you are using a marketplace image, you should also use the plan element previously described.
    """
    FROM_IMAGE = "FromImage"
    EMPTY = "Empty"
    ATTACH = "Attach"


class DiskDeleteOptionTypes(str, Enum):
    """
    Specifies whether OS Disk should be deleted or detached upon VM deletion. Possible values are: **Delete.** If this value is used, the OS disk is deleted when VM is deleted. **Detach.** If this value is used, the os disk is retained after VM is deleted. The default value is set to **Detach**. For an ephemeral OS Disk, the default value is set to **Delete**. The user cannot change the delete option for an ephemeral OS Disk.
    """
    DELETE = "Delete"
    DETACH = "Detach"


class DiskDetachOptionTypes(str, Enum):
    """
    Specifies the detach behavior to be used while detaching a disk or which is already in the process of detachment from the virtual machine. Supported values: **ForceDetach.** detachOption: **ForceDetach** is applicable only for managed data disks. If a previous detachment attempt of the data disk did not complete due to an unexpected failure from the virtual machine and the disk is still not released then use force-detach as a last resort option to detach the disk forcibly from the VM. All writes might not have been flushed when using this detach behavior. **This feature is still in preview** mode and is not supported for VirtualMachineScaleSet. To force-detach a data disk update toBeDetached to 'true' along with setting detachOption: 'ForceDetach'.
    """
    FORCE_DETACH = "ForceDetach"


class DiskEncryptionSetIdentityType(str, Enum):
    """
    The type of Managed Identity used by the DiskEncryptionSet. Only SystemAssigned is supported for new creations. Disk Encryption Sets can be updated with Identity type None during migration of subscription to a new Azure Active Directory tenant; it will cause the encrypted resources to lose access to the keys.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"


class DiskEncryptionSetType(str, Enum):
    """
    The type of key used to encrypt the data of the disk.
    """
    ENCRYPTION_AT_REST_WITH_CUSTOMER_KEY = "EncryptionAtRestWithCustomerKey"
    """
    Resource using diskEncryptionSet would be encrypted at rest with Customer managed key that can be changed and revoked by a customer.
    """
    ENCRYPTION_AT_REST_WITH_PLATFORM_AND_CUSTOMER_KEYS = "EncryptionAtRestWithPlatformAndCustomerKeys"
    """
    Resource using diskEncryptionSet would be encrypted at rest with two layers of encryption. One of the keys is Customer managed and the other key is Platform managed.
    """
    CONFIDENTIAL_VM_ENCRYPTED_WITH_CUSTOMER_KEY = "ConfidentialVmEncryptedWithCustomerKey"
    """
    Confidential VM supported disk and VM guest state would be encrypted with customer managed key.
    """


class DiskSecurityTypes(str, Enum):
    """
    Specifies the SecurityType of the VM. Applicable for OS disks only.
    """
    TRUSTED_LAUNCH = "TrustedLaunch"
    """
    Trusted Launch provides security features such as secure boot and virtual Trusted Platform Module (vTPM)
    """
    CONFIDENTIAL_V_M_VM_GUEST_STATE_ONLY_ENCRYPTED_WITH_PLATFORM_KEY = "ConfidentialVM_VMGuestStateOnlyEncryptedWithPlatformKey"
    """
    Indicates Confidential VM disk with only VM guest state encrypted
    """
    CONFIDENTIAL_V_M_DISK_ENCRYPTED_WITH_PLATFORM_KEY = "ConfidentialVM_DiskEncryptedWithPlatformKey"
    """
    Indicates Confidential VM disk with both OS disk and VM guest state encrypted with a platform managed key
    """
    CONFIDENTIAL_V_M_DISK_ENCRYPTED_WITH_CUSTOMER_KEY = "ConfidentialVM_DiskEncryptedWithCustomerKey"
    """
    Indicates Confidential VM disk with both OS disk and VM guest state encrypted with a customer managed key
    """


class DiskStorageAccountTypes(str, Enum):
    """
    The sku name.
    """
    STANDARD_LRS = "Standard_LRS"
    """
    Standard HDD locally redundant storage. Best for backup, non-critical, and infrequent access.
    """
    PREMIUM_LRS = "Premium_LRS"
    """
    Premium SSD locally redundant storage. Best for production and performance sensitive workloads.
    """
    STANDARD_SS_D_LRS = "StandardSSD_LRS"
    """
    Standard SSD locally redundant storage. Best for web servers, lightly used enterprise applications and dev/test.
    """
    ULTRA_SS_D_LRS = "UltraSSD_LRS"
    """
    Ultra SSD locally redundant storage. Best for IO-intensive workloads such as SAP HANA, top tier databases (for example, SQL, Oracle), and other transaction-heavy workloads.
    """
    PREMIUM_ZRS = "Premium_ZRS"
    """
    Premium SSD zone redundant storage. Best for the production workloads that need storage resiliency against zone failures.
    """
    STANDARD_SS_D_ZRS = "StandardSSD_ZRS"
    """
    Standard SSD zone redundant storage. Best for web servers, lightly used enterprise applications and dev/test that need storage resiliency against zone failures.
    """
    PREMIUM_V2_LRS = "PremiumV2_LRS"
    """
    Premium SSD v2 locally redundant storage. Best for production and performance-sensitive workloads that consistently require low latency and high IOPS and throughput.
    """


class EdgeZoneStorageAccountType(str, Enum):
    """
    Specifies the storage account type to be used to store the image. This property is not updatable.
    """
    STANDARD_LRS = "Standard_LRS"
    STANDARD_ZRS = "Standard_ZRS"
    STANDARD_SS_D_LRS = "StandardSSD_LRS"
    PREMIUM_LRS = "Premium_LRS"


class EncryptionType(str, Enum):
    """
    The type of key used to encrypt the data of the disk.
    """
    ENCRYPTION_AT_REST_WITH_PLATFORM_KEY = "EncryptionAtRestWithPlatformKey"
    """
    Disk is encrypted at rest with Platform managed key. It is the default encryption type. This is not a valid encryption type for disk encryption sets.
    """
    ENCRYPTION_AT_REST_WITH_CUSTOMER_KEY = "EncryptionAtRestWithCustomerKey"
    """
    Disk is encrypted at rest with Customer managed key that can be changed and revoked by a customer.
    """
    ENCRYPTION_AT_REST_WITH_PLATFORM_AND_CUSTOMER_KEYS = "EncryptionAtRestWithPlatformAndCustomerKeys"
    """
    Disk is encrypted at rest with 2 layers of encryption. One of the keys is Customer managed and the other key is Platform managed.
    """


class ExtendedLocationTypes(str, Enum):
    """
    The type of the extended location.
    """
    EDGE_ZONE = "EdgeZone"


class GalleryApplicationCustomActionParameterType(str, Enum):
    """
    Specifies the type of the custom action parameter. Possible values are: String, ConfigurationDataBlob or LogOutputBlob
    """
    STRING = "String"
    CONFIGURATION_DATA_BLOB = "ConfigurationDataBlob"
    LOG_OUTPUT_BLOB = "LogOutputBlob"


class GalleryExtendedLocationType(str, Enum):
    """
    It is type of the extended location.
    """
    EDGE_ZONE = "EdgeZone"
    UNKNOWN = "Unknown"


class GallerySharingPermissionTypes(str, Enum):
    """
    This property allows you to specify the permission of sharing gallery. <br><br> Possible values are: <br><br> **Private** <br><br> **Groups** <br><br> **Community**
    """
    PRIVATE = "Private"
    GROUPS = "Groups"
    COMMUNITY = "Community"


class HostCaching(str, Enum):
    """
    The host caching of the disk. Valid values are 'None', 'ReadOnly', and 'ReadWrite'
    """
    NONE = "None"
    READ_ONLY = "ReadOnly"
    READ_WRITE = "ReadWrite"


class HyperVGeneration(str, Enum):
    """
    The hypervisor generation of the Virtual Machine. Applicable to OS disks only.
    """
    V1 = "V1"
    V2 = "V2"


class HyperVGenerationTypes(str, Enum):
    """
    Specifies the HyperVGenerationType of the VirtualMachine created from the image. From API Version 2019-03-01 if the image source is a blob, then we need the user to specify the value, if the source is managed resource like disk or snapshot, we may require the user to specify the property if we cannot deduce it from the source managed resource.
    """
    V1 = "V1"
    V2 = "V2"


class IPVersion(str, Enum):
    """
    Available from Api-Version 2019-07-01 onwards, it represents whether the specific ipconfiguration is IPv4 or IPv6. Default is taken as IPv4. Possible values are: 'IPv4' and 'IPv6'.
    """
    I_PV4 = "IPv4"
    I_PV6 = "IPv6"


class IPVersions(str, Enum):
    """
    Available from Api-Version 2019-07-01 onwards, it represents whether the specific ipconfiguration is IPv4 or IPv6. Default is taken as IPv4. Possible values are: 'IPv4' and 'IPv6'.
    """
    I_PV4 = "IPv4"
    I_PV6 = "IPv6"


class IntervalInMins(str, Enum):
    """
    Interval value in minutes used to create LogAnalytics call rate logs.
    """
    THREE_MINS = "ThreeMins"
    FIVE_MINS = "FiveMins"
    THIRTY_MINS = "ThirtyMins"
    SIXTY_MINS = "SixtyMins"


class LinuxPatchAssessmentMode(str, Enum):
    """
    Specifies the mode of VM Guest Patch Assessment for the IaaS virtual machine.<br /><br /> Possible values are:<br /><br /> **ImageDefault** - You control the timing of patch assessments on a virtual machine. <br /><br /> **AutomaticByPlatform** - The platform will trigger periodic patch assessments. The property provisionVMAgent must be true.
    """
    IMAGE_DEFAULT = "ImageDefault"
    AUTOMATIC_BY_PLATFORM = "AutomaticByPlatform"


class LinuxVMGuestPatchAutomaticByPlatformRebootSetting(str, Enum):
    """
    Specifies the reboot setting for all AutomaticByPlatform patch installation operations.
    """
    UNKNOWN = "Unknown"
    IF_REQUIRED = "IfRequired"
    NEVER = "Never"
    ALWAYS = "Always"


class LinuxVMGuestPatchMode(str, Enum):
    """
    Specifies the mode of VM Guest Patching to IaaS virtual machine or virtual machines associated to virtual machine scale set with OrchestrationMode as Flexible.<br /><br /> Possible values are:<br /><br /> **ImageDefault** - The virtual machine's default patching configuration is used. <br /><br /> **AutomaticByPlatform** - The virtual machine will be automatically updated by the platform. The property provisionVMAgent must be true
    """
    IMAGE_DEFAULT = "ImageDefault"
    AUTOMATIC_BY_PLATFORM = "AutomaticByPlatform"


class NetworkAccessPolicy(str, Enum):
    """
    Policy for accessing the disk via network.
    """
    ALLOW_ALL = "AllowAll"
    """
    The disk can be exported or uploaded to from any network.
    """
    ALLOW_PRIVATE = "AllowPrivate"
    """
    The disk can be exported or uploaded to using a DiskAccess resource's private endpoints.
    """
    DENY_ALL = "DenyAll"
    """
    The disk cannot be exported.
    """


class NetworkApiVersion(str, Enum):
    """
    specifies the Microsoft.Network API version used when creating networking resources in the Network Interface Configurations
    """
    NETWORK_API_VERSION_2020_11_01 = "2020-11-01"


class OperatingSystemStateTypes(str, Enum):
    """
    The OS State. For managed images, use Generalized.
    """
    GENERALIZED = "Generalized"
    """
    Generalized image. Needs to be provisioned during deployment time.
    """
    SPECIALIZED = "Specialized"
    """
    Specialized image. Contains already provisioned OS Disk.
    """


class OperatingSystemTypes(str, Enum):
    """
    This property allows you to specify the type of the OS that is included in the disk if creating a VM from user-image or a specialized VHD. Possible values are: **Windows,** **Linux.**
    """
    WINDOWS = "Windows"
    LINUX = "Linux"


class OrchestrationMode(str, Enum):
    """
    Specifies the orchestration mode for the virtual machine scale set.
    """
    UNIFORM = "Uniform"
    FLEXIBLE = "Flexible"


class PassNames(str, Enum):
    """
    The pass name. Currently, the only allowable value is OobeSystem.
    """
    OOBE_SYSTEM = "OobeSystem"


class PrivateEndpointServiceConnectionStatus(str, Enum):
    """
    Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class ProtocolTypes(str, Enum):
    """
    Specifies the protocol of WinRM listener. Possible values are: **http,** **https.**
    """
    HTTP = "Http"
    HTTPS = "Https"


class ProximityPlacementGroupType(str, Enum):
    """
    Specifies the type of the proximity placement group. Possible values are: **Standard** : Co-locate resources within an Azure region or Availability Zone. **Ultra** : For future use.
    """
    STANDARD = "Standard"
    ULTRA = "Ultra"


class PublicIPAddressSkuName(str, Enum):
    """
    Specify public IP sku name
    """
    BASIC = "Basic"
    STANDARD = "Standard"


class PublicIPAddressSkuTier(str, Enum):
    """
    Specify public IP sku tier
    """
    REGIONAL = "Regional"
    GLOBAL_ = "Global"


class PublicIPAllocationMethod(str, Enum):
    """
    Specify the public IP allocation type
    """
    DYNAMIC = "Dynamic"
    STATIC = "Static"


class PublicNetworkAccess(str, Enum):
    """
    Policy for controlling export on the disk.
    """
    ENABLED = "Enabled"
    """
    You can generate a SAS URI to access the underlying data of the disk publicly on the internet when NetworkAccessPolicy is set to AllowAll. You can access the data via the SAS URI only from your trusted Azure VNET when NetworkAccessPolicy is set to AllowPrivate.
    """
    DISABLED = "Disabled"
    """
    You cannot access the underlying data of the disk publicly on the internet even when NetworkAccessPolicy is set to AllowAll. You can access the data via the SAS URI only from your trusted Azure VNET when NetworkAccessPolicy is set to AllowPrivate.
    """


class RepairAction(str, Enum):
    """
    Type of repair action (replace, restart, reimage) that will be used for repairing unhealthy virtual machines in the scale set. Default value is replace.
    """
    REPLACE = "Replace"
    RESTART = "Restart"
    REIMAGE = "Reimage"


class ReplicationMode(str, Enum):
    """
    Optional parameter which specifies the mode to be used for replication. This property is not updatable.
    """
    FULL = "Full"
    SHALLOW = "Shallow"


class ResourceIdentityType(str, Enum):
    """
    The type of identity used for the virtual machine. The type 'SystemAssigned, UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the virtual machine.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"


class RestorePointEncryptionType(str, Enum):
    """
    The type of key used to encrypt the data of the disk restore point.
    """
    ENCRYPTION_AT_REST_WITH_PLATFORM_KEY = "EncryptionAtRestWithPlatformKey"
    """
    Disk Restore Point is encrypted at rest with Platform managed key. 
    """
    ENCRYPTION_AT_REST_WITH_CUSTOMER_KEY = "EncryptionAtRestWithCustomerKey"
    """
    Disk Restore Point is encrypted at rest with Customer managed key that can be changed and revoked by a customer.
    """
    ENCRYPTION_AT_REST_WITH_PLATFORM_AND_CUSTOMER_KEYS = "EncryptionAtRestWithPlatformAndCustomerKeys"
    """
    Disk Restore Point is encrypted at rest with 2 layers of encryption. One of the keys is Customer managed and the other key is Platform managed.
    """


class SecurityEncryptionTypes(str, Enum):
    """
    Specifies the EncryptionType of the managed disk. It is set to DiskWithVMGuestState for encryption of the managed disk along with VMGuestState blob, and VMGuestStateOnly for encryption of just the VMGuestState blob. **Note:** It can be set for only Confidential VMs.
    """
    VM_GUEST_STATE_ONLY = "VMGuestStateOnly"
    DISK_WITH_VM_GUEST_STATE = "DiskWithVMGuestState"


class SecurityTypes(str, Enum):
    """
    Specifies the SecurityType of the virtual machine. It has to be set to any specified value to enable UefiSettings. The default behavior is: UefiSettings will not be enabled unless this property is set.
    """
    TRUSTED_LAUNCH = "TrustedLaunch"
    CONFIDENTIAL_VM = "ConfidentialVM"


class SettingNames(str, Enum):
    """
    Specifies the name of the setting to which the content applies. Possible values are: FirstLogonCommands and AutoLogon.
    """
    AUTO_LOGON = "AutoLogon"
    FIRST_LOGON_COMMANDS = "FirstLogonCommands"


class SnapshotStorageAccountTypes(str, Enum):
    """
    The sku name.
    """
    STANDARD_LRS = "Standard_LRS"
    """
    Standard HDD locally redundant storage
    """
    PREMIUM_LRS = "Premium_LRS"
    """
    Premium SSD locally redundant storage
    """
    STANDARD_ZRS = "Standard_ZRS"
    """
    Standard zone redundant storage
    """


class StatusLevelTypes(str, Enum):
    """
    The level code.
    """
    INFO = "Info"
    WARNING = "Warning"
    ERROR = "Error"


class StorageAccountType(str, Enum):
    """
    Specifies the storage account type to be used to store the image. This property is not updatable.
    """
    STANDARD_LRS = "Standard_LRS"
    STANDARD_ZRS = "Standard_ZRS"
    PREMIUM_LRS = "Premium_LRS"


class StorageAccountTypes(str, Enum):
    """
    Specifies the storage account type for the managed disk. NOTE: UltraSSD_LRS can only be used with data disks, it cannot be used with OS Disk.
    """
    STANDARD_LRS = "Standard_LRS"
    PREMIUM_LRS = "Premium_LRS"
    STANDARD_SS_D_LRS = "StandardSSD_LRS"
    ULTRA_SS_D_LRS = "UltraSSD_LRS"
    PREMIUM_ZRS = "Premium_ZRS"
    STANDARD_SS_D_ZRS = "StandardSSD_ZRS"
    PREMIUM_V2_LRS = "PremiumV2_LRS"


class UpgradeMode(str, Enum):
    """
    Specifies the mode of an upgrade to virtual machines in the scale set.<br /><br /> Possible values are:<br /><br /> **Manual** - You  control the application of updates to virtual machines in the scale set. You do this by using the manualUpgrade action.<br /><br /> **Automatic** - All virtual machines in the scale set are  automatically updated at the same time.
    """
    AUTOMATIC = "Automatic"
    MANUAL = "Manual"
    ROLLING = "Rolling"


class VirtualMachineEvictionPolicyTypes(str, Enum):
    """
    Specifies the eviction policy for the Azure Spot virtual machine and Azure Spot scale set. For Azure Spot virtual machines, both 'Deallocate' and 'Delete' are supported and the minimum api-version is 2019-03-01. For Azure Spot scale sets, both 'Deallocate' and 'Delete' are supported and the minimum api-version is 2017-10-30-preview.
    """
    DEALLOCATE = "Deallocate"
    DELETE = "Delete"


class VirtualMachinePriorityTypes(str, Enum):
    """
    Specifies the priority for the virtual machines in the scale set. Minimum api-version: 2017-10-30-preview.
    """
    REGULAR = "Regular"
    LOW = "Low"
    SPOT = "Spot"


class VirtualMachineScaleSetScaleInRules(str, Enum):
    DEFAULT = "Default"
    OLDEST_VM = "OldestVM"
    NEWEST_VM = "NewestVM"


class VirtualMachineSizeTypes(str, Enum):
    """
    Specifies the size of the virtual machine. The enum data type is currently deprecated and will be removed by December 23rd 2023. The recommended way to get the list of available sizes is using these APIs: [List all available virtual machine sizes in an availability set](https://docs.microsoft.com/rest/api/compute/availabilitysets/listavailablesizes), [List all available virtual machine sizes in a region]( https://docs.microsoft.com/rest/api/compute/resourceskus/list), [List all available virtual machine sizes for resizing](https://docs.microsoft.com/rest/api/compute/virtualmachines/listavailablesizes). For more information about virtual machine sizes, see [Sizes for virtual machines](https://docs.microsoft.com/azure/virtual-machines/sizes). The available VM sizes depend on region and availability set.
    """
    BASIC_A0 = "Basic_A0"
    BASIC_A1 = "Basic_A1"
    BASIC_A2 = "Basic_A2"
    BASIC_A3 = "Basic_A3"
    BASIC_A4 = "Basic_A4"
    STANDARD_A0 = "Standard_A0"
    STANDARD_A1 = "Standard_A1"
    STANDARD_A2 = "Standard_A2"
    STANDARD_A3 = "Standard_A3"
    STANDARD_A4 = "Standard_A4"
    STANDARD_A5 = "Standard_A5"
    STANDARD_A6 = "Standard_A6"
    STANDARD_A7 = "Standard_A7"
    STANDARD_A8 = "Standard_A8"
    STANDARD_A9 = "Standard_A9"
    STANDARD_A10 = "Standard_A10"
    STANDARD_A11 = "Standard_A11"
    STANDARD_A1_V2 = "Standard_A1_v2"
    STANDARD_A2_V2 = "Standard_A2_v2"
    STANDARD_A4_V2 = "Standard_A4_v2"
    STANDARD_A8_V2 = "Standard_A8_v2"
    STANDARD_A2M_V2 = "Standard_A2m_v2"
    STANDARD_A4M_V2 = "Standard_A4m_v2"
    STANDARD_A8M_V2 = "Standard_A8m_v2"
    STANDARD_B1S = "Standard_B1s"
    STANDARD_B1MS = "Standard_B1ms"
    STANDARD_B2S = "Standard_B2s"
    STANDARD_B2MS = "Standard_B2ms"
    STANDARD_B4MS = "Standard_B4ms"
    STANDARD_B8MS = "Standard_B8ms"
    STANDARD_D1 = "Standard_D1"
    STANDARD_D2 = "Standard_D2"
    STANDARD_D3 = "Standard_D3"
    STANDARD_D4 = "Standard_D4"
    STANDARD_D11 = "Standard_D11"
    STANDARD_D12 = "Standard_D12"
    STANDARD_D13 = "Standard_D13"
    STANDARD_D14 = "Standard_D14"
    STANDARD_D1_V2 = "Standard_D1_v2"
    STANDARD_D2_V2 = "Standard_D2_v2"
    STANDARD_D3_V2 = "Standard_D3_v2"
    STANDARD_D4_V2 = "Standard_D4_v2"
    STANDARD_D5_V2 = "Standard_D5_v2"
    STANDARD_D2_V3 = "Standard_D2_v3"
    STANDARD_D4_V3 = "Standard_D4_v3"
    STANDARD_D8_V3 = "Standard_D8_v3"
    STANDARD_D16_V3 = "Standard_D16_v3"
    STANDARD_D32_V3 = "Standard_D32_v3"
    STANDARD_D64_V3 = "Standard_D64_v3"
    STANDARD_D2S_V3 = "Standard_D2s_v3"
    STANDARD_D4S_V3 = "Standard_D4s_v3"
    STANDARD_D8S_V3 = "Standard_D8s_v3"
    STANDARD_D16S_V3 = "Standard_D16s_v3"
    STANDARD_D32S_V3 = "Standard_D32s_v3"
    STANDARD_D64S_V3 = "Standard_D64s_v3"
    STANDARD_D11_V2 = "Standard_D11_v2"
    STANDARD_D12_V2 = "Standard_D12_v2"
    STANDARD_D13_V2 = "Standard_D13_v2"
    STANDARD_D14_V2 = "Standard_D14_v2"
    STANDARD_D15_V2 = "Standard_D15_v2"
    STANDARD_DS1 = "Standard_DS1"
    STANDARD_DS2 = "Standard_DS2"
    STANDARD_DS3 = "Standard_DS3"
    STANDARD_DS4 = "Standard_DS4"
    STANDARD_DS11 = "Standard_DS11"
    STANDARD_DS12 = "Standard_DS12"
    STANDARD_DS13 = "Standard_DS13"
    STANDARD_DS14 = "Standard_DS14"
    STANDARD_DS1_V2 = "Standard_DS1_v2"
    STANDARD_DS2_V2 = "Standard_DS2_v2"
    STANDARD_DS3_V2 = "Standard_DS3_v2"
    STANDARD_DS4_V2 = "Standard_DS4_v2"
    STANDARD_DS5_V2 = "Standard_DS5_v2"
    STANDARD_DS11_V2 = "Standard_DS11_v2"
    STANDARD_DS12_V2 = "Standard_DS12_v2"
    STANDARD_DS13_V2 = "Standard_DS13_v2"
    STANDARD_DS14_V2 = "Standard_DS14_v2"
    STANDARD_DS15_V2 = "Standard_DS15_v2"
    STANDARD_DS13_4_V2 = "Standard_DS13-4_v2"
    STANDARD_DS13_2_V2 = "Standard_DS13-2_v2"
    STANDARD_DS14_8_V2 = "Standard_DS14-8_v2"
    STANDARD_DS14_4_V2 = "Standard_DS14-4_v2"
    STANDARD_E2_V3 = "Standard_E2_v3"
    STANDARD_E4_V3 = "Standard_E4_v3"
    STANDARD_E8_V3 = "Standard_E8_v3"
    STANDARD_E16_V3 = "Standard_E16_v3"
    STANDARD_E32_V3 = "Standard_E32_v3"
    STANDARD_E64_V3 = "Standard_E64_v3"
    STANDARD_E2S_V3 = "Standard_E2s_v3"
    STANDARD_E4S_V3 = "Standard_E4s_v3"
    STANDARD_E8S_V3 = "Standard_E8s_v3"
    STANDARD_E16S_V3 = "Standard_E16s_v3"
    STANDARD_E32S_V3 = "Standard_E32s_v3"
    STANDARD_E64S_V3 = "Standard_E64s_v3"
    STANDARD_E32_16_V3 = "Standard_E32-16_v3"
    STANDARD_E32_8S_V3 = "Standard_E32-8s_v3"
    STANDARD_E64_32S_V3 = "Standard_E64-32s_v3"
    STANDARD_E64_16S_V3 = "Standard_E64-16s_v3"
    STANDARD_F1 = "Standard_F1"
    STANDARD_F2 = "Standard_F2"
    STANDARD_F4 = "Standard_F4"
    STANDARD_F8 = "Standard_F8"
    STANDARD_F16 = "Standard_F16"
    STANDARD_F1S = "Standard_F1s"
    STANDARD_F2S = "Standard_F2s"
    STANDARD_F4S = "Standard_F4s"
    STANDARD_F8S = "Standard_F8s"
    STANDARD_F16S = "Standard_F16s"
    STANDARD_F2S_V2 = "Standard_F2s_v2"
    STANDARD_F4S_V2 = "Standard_F4s_v2"
    STANDARD_F8S_V2 = "Standard_F8s_v2"
    STANDARD_F16S_V2 = "Standard_F16s_v2"
    STANDARD_F32S_V2 = "Standard_F32s_v2"
    STANDARD_F64S_V2 = "Standard_F64s_v2"
    STANDARD_F72S_V2 = "Standard_F72s_v2"
    STANDARD_G1 = "Standard_G1"
    STANDARD_G2 = "Standard_G2"
    STANDARD_G3 = "Standard_G3"
    STANDARD_G4 = "Standard_G4"
    STANDARD_G5 = "Standard_G5"
    STANDARD_GS1 = "Standard_GS1"
    STANDARD_GS2 = "Standard_GS2"
    STANDARD_GS3 = "Standard_GS3"
    STANDARD_GS4 = "Standard_GS4"
    STANDARD_GS5 = "Standard_GS5"
    STANDARD_GS4_8 = "Standard_GS4-8"
    STANDARD_GS4_4 = "Standard_GS4-4"
    STANDARD_GS5_16 = "Standard_GS5-16"
    STANDARD_GS5_8 = "Standard_GS5-8"
    STANDARD_H8 = "Standard_H8"
    STANDARD_H16 = "Standard_H16"
    STANDARD_H8M = "Standard_H8m"
    STANDARD_H16M = "Standard_H16m"
    STANDARD_H16R = "Standard_H16r"
    STANDARD_H16MR = "Standard_H16mr"
    STANDARD_L4S = "Standard_L4s"
    STANDARD_L8S = "Standard_L8s"
    STANDARD_L16S = "Standard_L16s"
    STANDARD_L32S = "Standard_L32s"
    STANDARD_M64S = "Standard_M64s"
    STANDARD_M64MS = "Standard_M64ms"
    STANDARD_M128S = "Standard_M128s"
    STANDARD_M128MS = "Standard_M128ms"
    STANDARD_M64_32MS = "Standard_M64-32ms"
    STANDARD_M64_16MS = "Standard_M64-16ms"
    STANDARD_M128_64MS = "Standard_M128-64ms"
    STANDARD_M128_32MS = "Standard_M128-32ms"
    STANDARD_NC6 = "Standard_NC6"
    STANDARD_NC12 = "Standard_NC12"
    STANDARD_NC24 = "Standard_NC24"
    STANDARD_NC24R = "Standard_NC24r"
    STANDARD_NC6S_V2 = "Standard_NC6s_v2"
    STANDARD_NC12S_V2 = "Standard_NC12s_v2"
    STANDARD_NC24S_V2 = "Standard_NC24s_v2"
    STANDARD_NC24RS_V2 = "Standard_NC24rs_v2"
    STANDARD_NC6S_V3 = "Standard_NC6s_v3"
    STANDARD_NC12S_V3 = "Standard_NC12s_v3"
    STANDARD_NC24S_V3 = "Standard_NC24s_v3"
    STANDARD_NC24RS_V3 = "Standard_NC24rs_v3"
    STANDARD_ND6S = "Standard_ND6s"
    STANDARD_ND12S = "Standard_ND12s"
    STANDARD_ND24S = "Standard_ND24s"
    STANDARD_ND24RS = "Standard_ND24rs"
    STANDARD_NV6 = "Standard_NV6"
    STANDARD_NV12 = "Standard_NV12"
    STANDARD_NV24 = "Standard_NV24"


class WindowsPatchAssessmentMode(str, Enum):
    """
    Specifies the mode of VM Guest patch assessment for the IaaS virtual machine.<br /><br /> Possible values are:<br /><br /> **ImageDefault** - You control the timing of patch assessments on a virtual machine.<br /><br /> **AutomaticByPlatform** - The platform will trigger periodic patch assessments. The property provisionVMAgent must be true. 
    """
    IMAGE_DEFAULT = "ImageDefault"
    AUTOMATIC_BY_PLATFORM = "AutomaticByPlatform"


class WindowsVMGuestPatchAutomaticByPlatformRebootSetting(str, Enum):
    """
    Specifies the reboot setting for all AutomaticByPlatform patch installation operations.
    """
    UNKNOWN = "Unknown"
    IF_REQUIRED = "IfRequired"
    NEVER = "Never"
    ALWAYS = "Always"


class WindowsVMGuestPatchMode(str, Enum):
    """
    Specifies the mode of VM Guest Patching to IaaS virtual machine or virtual machines associated to virtual machine scale set with OrchestrationMode as Flexible.<br /><br /> Possible values are:<br /><br /> **Manual** - You  control the application of patches to a virtual machine. You do this by applying patches manually inside the VM. In this mode, automatic updates are disabled; the property WindowsConfiguration.enableAutomaticUpdates must be false<br /><br /> **AutomaticByOS** - The virtual machine will automatically be updated by the OS. The property WindowsConfiguration.enableAutomaticUpdates must be true. <br /><br /> **AutomaticByPlatform** - the virtual machine will automatically updated by the platform. The properties provisionVMAgent and WindowsConfiguration.enableAutomaticUpdates must be true 
    """
    MANUAL = "Manual"
    AUTOMATIC_BY_OS = "AutomaticByOS"
    AUTOMATIC_BY_PLATFORM = "AutomaticByPlatform"
