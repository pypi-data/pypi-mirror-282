# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'CatalogItemSyncEnableStatus',
    'CatalogItemType',
    'CatalogSyncType',
    'DomainJoinType',
    'EnvironmentTypeEnableStatus',
    'HibernateSupport',
    'IdentityType',
    'LicenseType',
    'LocalAdminStatus',
    'ManagedServiceIdentityType',
    'ScheduleEnableStatus',
    'ScheduledFrequency',
    'ScheduledType',
    'SingleSignOnStatus',
    'SkuTier',
    'StopOnDisconnectEnableStatus',
    'VirtualNetworkType',
]


class CatalogItemSyncEnableStatus(str, Enum):
    """
    Whether project catalogs associated with projects in this dev center can be configured to sync catalog items.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class CatalogItemType(str, Enum):
    """
    Indicates catalog item types.
    """
    ENVIRONMENT_DEFINITION = "EnvironmentDefinition"


class CatalogSyncType(str, Enum):
    """
    Indicates the type of sync that is configured for the catalog.
    """
    MANUAL = "Manual"
    SCHEDULED = "Scheduled"


class DomainJoinType(str, Enum):
    """
    AAD Join type.
    """
    HYBRID_AZURE_AD_JOIN = "HybridAzureADJoin"
    AZURE_AD_JOIN = "AzureADJoin"


class EnvironmentTypeEnableStatus(str, Enum):
    """
    Defines whether this Environment Type can be used in this Project.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class HibernateSupport(str, Enum):
    """
    Indicates whether Dev Boxes created with this definition are capable of hibernation. Not all images are capable of supporting hibernation. To find out more see https://aka.ms/devbox/hibernate
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class IdentityType(str, Enum):
    """
    Values can be systemAssignedIdentity or userAssignedIdentity
    """
    SYSTEM_ASSIGNED_IDENTITY = "systemAssignedIdentity"
    USER_ASSIGNED_IDENTITY = "userAssignedIdentity"
    DELEGATED_RESOURCE_IDENTITY = "delegatedResourceIdentity"


class LicenseType(str, Enum):
    """
    Specifies the license type indicating the caller has already acquired licenses for the Dev Boxes that will be created.
    """
    WINDOWS_CLIENT = "Windows_Client"


class LocalAdminStatus(str, Enum):
    """
    Indicates whether owners of Dev Boxes in this pool are added as local administrators on the Dev Box.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class ManagedServiceIdentityType(str, Enum):
    """
    Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"


class ScheduleEnableStatus(str, Enum):
    """
    Indicates whether or not this scheduled task is enabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ScheduledFrequency(str, Enum):
    """
    The frequency of this scheduled task.
    """
    DAILY = "Daily"


class ScheduledType(str, Enum):
    """
    Supported type this scheduled task represents.
    """
    STOP_DEV_BOX = "StopDevBox"


class SingleSignOnStatus(str, Enum):
    """
    Indicates whether Dev Boxes in this pool are created with single sign on enabled. The also requires that single sign on be enabled on the tenant.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class SkuTier(str, Enum):
    """
    This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT.
    """
    FREE = "Free"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"


class StopOnDisconnectEnableStatus(str, Enum):
    """
    Whether the feature to stop the Dev Box on disconnect once the grace period has lapsed is enabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class VirtualNetworkType(str, Enum):
    """
    Indicates whether the pool uses a Virtual Network managed by Microsoft or a customer provided network.
    """
    MANAGED = "Managed"
    UNMANAGED = "Unmanaged"
