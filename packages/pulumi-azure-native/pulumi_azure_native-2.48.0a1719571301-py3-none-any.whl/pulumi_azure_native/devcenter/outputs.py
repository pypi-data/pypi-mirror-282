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
from ._enums import *

__all__ = [
    'CapabilityResponse',
    'CatalogConflictErrorResponse',
    'CatalogErrorDetailsResponse',
    'CatalogSyncErrorResponse',
    'DevCenterProjectCatalogSettingsResponse',
    'DevCenterSkuResponse',
    'EnvironmentRoleResponse',
    'GitCatalogResponse',
    'HealthStatusDetailResponse',
    'ImageReferenceResponse',
    'ImageValidationErrorDetailsResponse',
    'ManagedServiceIdentityResponse',
    'ProjectEnvironmentTypeUpdatePropertiesResponseCreatorRoleAssignment',
    'ProjectNetworkSettingsResponse',
    'SkuResponse',
    'StopOnDisconnectConfigurationResponse',
    'SyncStatsResponse',
    'SystemDataResponse',
    'UserAssignedIdentityResponse',
    'UserRoleAssignmentResponse',
]

@pulumi.output_type
class CapabilityResponse(dict):
    """
    A name/value pair to describe a capability.
    """
    def __init__(__self__, *,
                 name: str,
                 value: str):
        """
        A name/value pair to describe a capability.
        :param str name: Name of the capability.
        :param str value: Value of the capability.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the capability.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        Value of the capability.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class CatalogConflictErrorResponse(dict):
    """
    An individual conflict error.
    """
    def __init__(__self__, *,
                 name: str,
                 path: str):
        """
        An individual conflict error.
        :param str name: Name of the conflicting catalog item.
        :param str path: The path of the file that has a conflicting name.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the conflicting catalog item.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def path(self) -> str:
        """
        The path of the file that has a conflicting name.
        """
        return pulumi.get(self, "path")


@pulumi.output_type
class CatalogErrorDetailsResponse(dict):
    """
    Catalog error details
    """
    def __init__(__self__, *,
                 code: Optional[str] = None,
                 message: Optional[str] = None):
        """
        Catalog error details
        :param str code: An identifier for the error.
        :param str message: A message describing the error.
        """
        if code is not None:
            pulumi.set(__self__, "code", code)
        if message is not None:
            pulumi.set(__self__, "message", message)

    @property
    @pulumi.getter
    def code(self) -> Optional[str]:
        """
        An identifier for the error.
        """
        return pulumi.get(self, "code")

    @property
    @pulumi.getter
    def message(self) -> Optional[str]:
        """
        A message describing the error.
        """
        return pulumi.get(self, "message")


@pulumi.output_type
class CatalogSyncErrorResponse(dict):
    """
    An individual synchronization error.
    """
    def __init__(__self__, *,
                 error_details: Sequence['outputs.CatalogErrorDetailsResponse'],
                 path: str):
        """
        An individual synchronization error.
        :param Sequence['CatalogErrorDetailsResponse'] error_details: Errors associated with the file.
        :param str path: The path of the file the error is associated with.
        """
        pulumi.set(__self__, "error_details", error_details)
        pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter(name="errorDetails")
    def error_details(self) -> Sequence['outputs.CatalogErrorDetailsResponse']:
        """
        Errors associated with the file.
        """
        return pulumi.get(self, "error_details")

    @property
    @pulumi.getter
    def path(self) -> str:
        """
        The path of the file the error is associated with.
        """
        return pulumi.get(self, "path")


@pulumi.output_type
class DevCenterProjectCatalogSettingsResponse(dict):
    """
    Project catalog settings for project catalogs under a project associated to this dev center.
    """
    def __init__(__self__, *,
                 catalog_item_sync_enable_status: Optional[str] = None):
        """
        Project catalog settings for project catalogs under a project associated to this dev center.
        :param str catalog_item_sync_enable_status: Whether project catalogs associated with projects in this dev center can be configured to sync catalog items.
        """
        if catalog_item_sync_enable_status is not None:
            pulumi.set(__self__, "catalog_item_sync_enable_status", catalog_item_sync_enable_status)

    @property
    @pulumi.getter(name="catalogItemSyncEnableStatus")
    def catalog_item_sync_enable_status(self) -> Optional[str]:
        """
        Whether project catalogs associated with projects in this dev center can be configured to sync catalog items.
        """
        return pulumi.get(self, "catalog_item_sync_enable_status")


@pulumi.output_type
class DevCenterSkuResponse(dict):
    """
    The resource model definition representing SKU for DevCenter resources
    """
    def __init__(__self__, *,
                 capabilities: Sequence['outputs.CapabilityResponse'],
                 locations: Sequence[str],
                 name: str,
                 resource_type: str,
                 capacity: Optional[int] = None,
                 family: Optional[str] = None,
                 size: Optional[str] = None,
                 tier: Optional[str] = None):
        """
        The resource model definition representing SKU for DevCenter resources
        :param Sequence['CapabilityResponse'] capabilities: Collection of name/value pairs to describe the SKU capabilities.
        :param Sequence[str] locations: SKU supported locations.
        :param str name: The name of the SKU. E.g. P3. It is typically a letter+number code
        :param str resource_type: The name of the resource type
        :param int capacity: If the SKU supports scale out/in then the capacity integer should be included. If scale out/in is not possible for the resource this may be omitted.
        :param str family: If the service has different generations of hardware, for the same SKU, then that can be captured here.
        :param str size: The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code. 
        :param str tier: This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT.
        """
        pulumi.set(__self__, "capabilities", capabilities)
        pulumi.set(__self__, "locations", locations)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_type", resource_type)
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)
        if family is not None:
            pulumi.set(__self__, "family", family)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def capabilities(self) -> Sequence['outputs.CapabilityResponse']:
        """
        Collection of name/value pairs to describe the SKU capabilities.
        """
        return pulumi.get(self, "capabilities")

    @property
    @pulumi.getter
    def locations(self) -> Sequence[str]:
        """
        SKU supported locations.
        """
        return pulumi.get(self, "locations")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the SKU. E.g. P3. It is typically a letter+number code
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> str:
        """
        The name of the resource type
        """
        return pulumi.get(self, "resource_type")

    @property
    @pulumi.getter
    def capacity(self) -> Optional[int]:
        """
        If the SKU supports scale out/in then the capacity integer should be included. If scale out/in is not possible for the resource this may be omitted.
        """
        return pulumi.get(self, "capacity")

    @property
    @pulumi.getter
    def family(self) -> Optional[str]:
        """
        If the service has different generations of hardware, for the same SKU, then that can be captured here.
        """
        return pulumi.get(self, "family")

    @property
    @pulumi.getter
    def size(self) -> Optional[str]:
        """
        The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code. 
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def tier(self) -> Optional[str]:
        """
        This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT.
        """
        return pulumi.get(self, "tier")


@pulumi.output_type
class EnvironmentRoleResponse(dict):
    """
    A role that can be assigned to a user.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "roleName":
            suggest = "role_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EnvironmentRoleResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EnvironmentRoleResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EnvironmentRoleResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 description: str,
                 role_name: str):
        """
        A role that can be assigned to a user.
        :param str description: This is a description of the Role Assignment.
        :param str role_name: The common name of the Role Assignment. This is a descriptive name such as 'AcrPush'.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "role_name", role_name)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        This is a description of the Role Assignment.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> str:
        """
        The common name of the Role Assignment. This is a descriptive name such as 'AcrPush'.
        """
        return pulumi.get(self, "role_name")


@pulumi.output_type
class GitCatalogResponse(dict):
    """
    Properties for a Git repository catalog.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "secretIdentifier":
            suggest = "secret_identifier"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GitCatalogResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GitCatalogResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GitCatalogResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 branch: Optional[str] = None,
                 path: Optional[str] = None,
                 secret_identifier: Optional[str] = None,
                 uri: Optional[str] = None):
        """
        Properties for a Git repository catalog.
        :param str branch: Git branch.
        :param str path: The folder where the catalog items can be found inside the repository.
        :param str secret_identifier: A reference to the Key Vault secret containing a security token to authenticate to a Git repository.
        :param str uri: Git URI.
        """
        if branch is not None:
            pulumi.set(__self__, "branch", branch)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if secret_identifier is not None:
            pulumi.set(__self__, "secret_identifier", secret_identifier)
        if uri is not None:
            pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter
    def branch(self) -> Optional[str]:
        """
        Git branch.
        """
        return pulumi.get(self, "branch")

    @property
    @pulumi.getter
    def path(self) -> Optional[str]:
        """
        The folder where the catalog items can be found inside the repository.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="secretIdentifier")
    def secret_identifier(self) -> Optional[str]:
        """
        A reference to the Key Vault secret containing a security token to authenticate to a Git repository.
        """
        return pulumi.get(self, "secret_identifier")

    @property
    @pulumi.getter
    def uri(self) -> Optional[str]:
        """
        Git URI.
        """
        return pulumi.get(self, "uri")


@pulumi.output_type
class HealthStatusDetailResponse(dict):
    """
    Pool health status detail.
    """
    def __init__(__self__, *,
                 code: str,
                 message: str):
        """
        Pool health status detail.
        :param str code: An identifier for the issue.
        :param str message: A message describing the issue, intended to be suitable for display in a user interface
        """
        pulumi.set(__self__, "code", code)
        pulumi.set(__self__, "message", message)

    @property
    @pulumi.getter
    def code(self) -> str:
        """
        An identifier for the issue.
        """
        return pulumi.get(self, "code")

    @property
    @pulumi.getter
    def message(self) -> str:
        """
        A message describing the issue, intended to be suitable for display in a user interface
        """
        return pulumi.get(self, "message")


@pulumi.output_type
class ImageReferenceResponse(dict):
    """
    Image reference information
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "exactVersion":
            suggest = "exact_version"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ImageReferenceResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ImageReferenceResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ImageReferenceResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 exact_version: str,
                 id: Optional[str] = None):
        """
        Image reference information
        :param str exact_version: The actual version of the image after use. When id references a gallery image latest version, this will indicate the actual version in use.
        :param str id: Image ID, or Image version ID. When Image ID is provided, its latest version will be used.
        """
        pulumi.set(__self__, "exact_version", exact_version)
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="exactVersion")
    def exact_version(self) -> str:
        """
        The actual version of the image after use. When id references a gallery image latest version, this will indicate the actual version in use.
        """
        return pulumi.get(self, "exact_version")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Image ID, or Image version ID. When Image ID is provided, its latest version will be used.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class ImageValidationErrorDetailsResponse(dict):
    """
    Image validation error details
    """
    def __init__(__self__, *,
                 code: Optional[str] = None,
                 message: Optional[str] = None):
        """
        Image validation error details
        :param str code: An identifier for the error.
        :param str message: A message describing the error.
        """
        if code is not None:
            pulumi.set(__self__, "code", code)
        if message is not None:
            pulumi.set(__self__, "message", message)

    @property
    @pulumi.getter
    def code(self) -> Optional[str]:
        """
        An identifier for the error.
        """
        return pulumi.get(self, "code")

    @property
    @pulumi.getter
    def message(self) -> Optional[str]:
        """
        A message describing the error.
        """
        return pulumi.get(self, "message")


@pulumi.output_type
class ManagedServiceIdentityResponse(dict):
    """
    Managed service identity (system assigned and/or user assigned identities)
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"
        elif key == "userAssignedIdentities":
            suggest = "user_assigned_identities"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ManagedServiceIdentityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ManagedServiceIdentityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ManagedServiceIdentityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: str,
                 user_assigned_identities: Optional[Mapping[str, 'outputs.UserAssignedIdentityResponse']] = None):
        """
        Managed service identity (system assigned and/or user assigned identities)
        :param str principal_id: The service principal ID of the system assigned identity. This property will only be provided for a system assigned identity.
        :param str tenant_id: The tenant ID of the system assigned identity. This property will only be provided for a system assigned identity.
        :param str type: Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
        :param Mapping[str, 'UserAssignedIdentityResponse'] user_assigned_identities: The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The service principal ID of the system assigned identity. This property will only be provided for a system assigned identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant ID of the system assigned identity. This property will only be provided for a system assigned identity.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, 'outputs.UserAssignedIdentityResponse']]:
        """
        The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.
        """
        return pulumi.get(self, "user_assigned_identities")


@pulumi.output_type
class ProjectEnvironmentTypeUpdatePropertiesResponseCreatorRoleAssignment(dict):
    """
    The role definition assigned to the environment creator on backing resources.
    """
    def __init__(__self__, *,
                 roles: Optional[Mapping[str, 'outputs.EnvironmentRoleResponse']] = None):
        """
        The role definition assigned to the environment creator on backing resources.
        :param Mapping[str, 'EnvironmentRoleResponse'] roles: A map of roles to assign to the environment creator.
        """
        if roles is not None:
            pulumi.set(__self__, "roles", roles)

    @property
    @pulumi.getter
    def roles(self) -> Optional[Mapping[str, 'outputs.EnvironmentRoleResponse']]:
        """
        A map of roles to assign to the environment creator.
        """
        return pulumi.get(self, "roles")


@pulumi.output_type
class ProjectNetworkSettingsResponse(dict):
    """
    Network settings for the project.
    """
    def __init__(__self__, *,
                 microsoft_hosted_network_enable_status: str):
        """
        Network settings for the project.
        :param str microsoft_hosted_network_enable_status: Indicates whether pools in this Dev Center can use Microsoft Hosted Networks. Defaults to Enabled if not set.
        """
        pulumi.set(__self__, "microsoft_hosted_network_enable_status", microsoft_hosted_network_enable_status)

    @property
    @pulumi.getter(name="microsoftHostedNetworkEnableStatus")
    def microsoft_hosted_network_enable_status(self) -> str:
        """
        Indicates whether pools in this Dev Center can use Microsoft Hosted Networks. Defaults to Enabled if not set.
        """
        return pulumi.get(self, "microsoft_hosted_network_enable_status")


@pulumi.output_type
class SkuResponse(dict):
    """
    The resource model definition representing SKU
    """
    def __init__(__self__, *,
                 name: str,
                 capacity: Optional[int] = None,
                 family: Optional[str] = None,
                 size: Optional[str] = None,
                 tier: Optional[str] = None):
        """
        The resource model definition representing SKU
        :param str name: The name of the SKU. E.g. P3. It is typically a letter+number code
        :param int capacity: If the SKU supports scale out/in then the capacity integer should be included. If scale out/in is not possible for the resource this may be omitted.
        :param str family: If the service has different generations of hardware, for the same SKU, then that can be captured here.
        :param str size: The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code. 
        :param str tier: This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT.
        """
        pulumi.set(__self__, "name", name)
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)
        if family is not None:
            pulumi.set(__self__, "family", family)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the SKU. E.g. P3. It is typically a letter+number code
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def capacity(self) -> Optional[int]:
        """
        If the SKU supports scale out/in then the capacity integer should be included. If scale out/in is not possible for the resource this may be omitted.
        """
        return pulumi.get(self, "capacity")

    @property
    @pulumi.getter
    def family(self) -> Optional[str]:
        """
        If the service has different generations of hardware, for the same SKU, then that can be captured here.
        """
        return pulumi.get(self, "family")

    @property
    @pulumi.getter
    def size(self) -> Optional[str]:
        """
        The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code. 
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def tier(self) -> Optional[str]:
        """
        This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT.
        """
        return pulumi.get(self, "tier")


@pulumi.output_type
class StopOnDisconnectConfigurationResponse(dict):
    """
    Stop on disconnect configuration settings for Dev Boxes created in this pool.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "gracePeriodMinutes":
            suggest = "grace_period_minutes"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in StopOnDisconnectConfigurationResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        StopOnDisconnectConfigurationResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        StopOnDisconnectConfigurationResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 grace_period_minutes: Optional[int] = None,
                 status: Optional[str] = None):
        """
        Stop on disconnect configuration settings for Dev Boxes created in this pool.
        :param int grace_period_minutes: The specified time in minutes to wait before stopping a Dev Box once disconnect is detected.
        :param str status: Whether the feature to stop the Dev Box on disconnect once the grace period has lapsed is enabled.
        """
        if grace_period_minutes is not None:
            pulumi.set(__self__, "grace_period_minutes", grace_period_minutes)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="gracePeriodMinutes")
    def grace_period_minutes(self) -> Optional[int]:
        """
        The specified time in minutes to wait before stopping a Dev Box once disconnect is detected.
        """
        return pulumi.get(self, "grace_period_minutes")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Whether the feature to stop the Dev Box on disconnect once the grace period has lapsed is enabled.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class SyncStatsResponse(dict):
    """
    Stats of the synchronization.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "synchronizationErrors":
            suggest = "synchronization_errors"
        elif key == "validationErrors":
            suggest = "validation_errors"
        elif key == "syncedCatalogItemTypes":
            suggest = "synced_catalog_item_types"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SyncStatsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SyncStatsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SyncStatsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 added: int,
                 removed: int,
                 synchronization_errors: int,
                 unchanged: int,
                 updated: int,
                 validation_errors: int,
                 synced_catalog_item_types: Optional[Sequence[str]] = None):
        """
        Stats of the synchronization.
        :param int added: Count of catalog items added during synchronization.
        :param int removed: Count of catalog items removed during synchronization.
        :param int synchronization_errors: Count of synchronization errors that occured during synchronization.
        :param int unchanged: Count of catalog items that were unchanged during synchronization.
        :param int updated: Count of catalog items updated during synchronization.
        :param int validation_errors: Count of catalog items that had validation errors during synchronization.
        :param Sequence[str] synced_catalog_item_types: Indicates catalog item types that were synced.
        """
        pulumi.set(__self__, "added", added)
        pulumi.set(__self__, "removed", removed)
        pulumi.set(__self__, "synchronization_errors", synchronization_errors)
        pulumi.set(__self__, "unchanged", unchanged)
        pulumi.set(__self__, "updated", updated)
        pulumi.set(__self__, "validation_errors", validation_errors)
        if synced_catalog_item_types is not None:
            pulumi.set(__self__, "synced_catalog_item_types", synced_catalog_item_types)

    @property
    @pulumi.getter
    def added(self) -> int:
        """
        Count of catalog items added during synchronization.
        """
        return pulumi.get(self, "added")

    @property
    @pulumi.getter
    def removed(self) -> int:
        """
        Count of catalog items removed during synchronization.
        """
        return pulumi.get(self, "removed")

    @property
    @pulumi.getter(name="synchronizationErrors")
    def synchronization_errors(self) -> int:
        """
        Count of synchronization errors that occured during synchronization.
        """
        return pulumi.get(self, "synchronization_errors")

    @property
    @pulumi.getter
    def unchanged(self) -> int:
        """
        Count of catalog items that were unchanged during synchronization.
        """
        return pulumi.get(self, "unchanged")

    @property
    @pulumi.getter
    def updated(self) -> int:
        """
        Count of catalog items updated during synchronization.
        """
        return pulumi.get(self, "updated")

    @property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> int:
        """
        Count of catalog items that had validation errors during synchronization.
        """
        return pulumi.get(self, "validation_errors")

    @property
    @pulumi.getter(name="syncedCatalogItemTypes")
    def synced_catalog_item_types(self) -> Optional[Sequence[str]]:
        """
        Indicates catalog item types that were synced.
        """
        return pulumi.get(self, "synced_catalog_item_types")


@pulumi.output_type
class SystemDataResponse(dict):
    """
    Metadata pertaining to creation and last modification of the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdAt":
            suggest = "created_at"
        elif key == "createdBy":
            suggest = "created_by"
        elif key == "createdByType":
            suggest = "created_by_type"
        elif key == "lastModifiedAt":
            suggest = "last_modified_at"
        elif key == "lastModifiedBy":
            suggest = "last_modified_by"
        elif key == "lastModifiedByType":
            suggest = "last_modified_by_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SystemDataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_at: Optional[str] = None,
                 created_by: Optional[str] = None,
                 created_by_type: Optional[str] = None,
                 last_modified_at: Optional[str] = None,
                 last_modified_by: Optional[str] = None,
                 last_modified_by_type: Optional[str] = None):
        """
        Metadata pertaining to creation and last modification of the resource.
        :param str created_at: The timestamp of resource creation (UTC).
        :param str created_by: The identity that created the resource.
        :param str created_by_type: The type of identity that created the resource.
        :param str last_modified_at: The timestamp of resource last modification (UTC)
        :param str last_modified_by: The identity that last modified the resource.
        :param str last_modified_by_type: The type of identity that last modified the resource.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")


@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    """
    User assigned identity properties
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "clientId":
            suggest = "client_id"
        elif key == "principalId":
            suggest = "principal_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UserAssignedIdentityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UserAssignedIdentityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UserAssignedIdentityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 client_id: str,
                 principal_id: str):
        """
        User assigned identity properties
        :param str client_id: The client ID of the assigned identity.
        :param str principal_id: The principal ID of the assigned identity.
        """
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "principal_id", principal_id)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        """
        The client ID of the assigned identity.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The principal ID of the assigned identity.
        """
        return pulumi.get(self, "principal_id")


@pulumi.output_type
class UserRoleAssignmentResponse(dict):
    """
    Mapping of user object ID to role assignments.
    """
    def __init__(__self__, *,
                 roles: Optional[Mapping[str, 'outputs.EnvironmentRoleResponse']] = None):
        """
        Mapping of user object ID to role assignments.
        :param Mapping[str, 'EnvironmentRoleResponse'] roles: A map of roles to assign to the parent user.
        """
        if roles is not None:
            pulumi.set(__self__, "roles", roles)

    @property
    @pulumi.getter
    def roles(self) -> Optional[Mapping[str, 'outputs.EnvironmentRoleResponse']]:
        """
        A map of roles to assign to the parent user.
        """
        return pulumi.get(self, "roles")


