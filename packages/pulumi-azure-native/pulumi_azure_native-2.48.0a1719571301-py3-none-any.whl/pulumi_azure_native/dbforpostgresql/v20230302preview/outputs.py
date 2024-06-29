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
from ._enums import *

__all__ = [
    'AuthConfigResponse',
    'DataEncryptionResponse',
    'IdentityPropertiesResponse',
    'MaintenanceWindowResponse',
    'PrivateEndpointPropertyResponse',
    'PrivateEndpointResponse',
    'PrivateLinkServiceConnectionStateResponse',
    'ServerNameItemResponse',
    'SimplePrivateEndpointConnectionResponse',
    'SystemDataResponse',
    'UserAssignedIdentityResponse',
]

@pulumi.output_type
class AuthConfigResponse(dict):
    """
    Authentication configuration of a cluster.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "activeDirectoryAuth":
            suggest = "active_directory_auth"
        elif key == "passwordAuth":
            suggest = "password_auth"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AuthConfigResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AuthConfigResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AuthConfigResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 active_directory_auth: Optional[str] = None,
                 password_auth: Optional[str] = None):
        """
        Authentication configuration of a cluster.
        """
        if active_directory_auth is not None:
            pulumi.set(__self__, "active_directory_auth", active_directory_auth)
        if password_auth is not None:
            pulumi.set(__self__, "password_auth", password_auth)

    @property
    @pulumi.getter(name="activeDirectoryAuth")
    def active_directory_auth(self) -> Optional[str]:
        return pulumi.get(self, "active_directory_auth")

    @property
    @pulumi.getter(name="passwordAuth")
    def password_auth(self) -> Optional[str]:
        return pulumi.get(self, "password_auth")


@pulumi.output_type
class DataEncryptionResponse(dict):
    """
    The data encryption properties of a cluster.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "primaryKeyUri":
            suggest = "primary_key_uri"
        elif key == "primaryUserAssignedIdentityId":
            suggest = "primary_user_assigned_identity_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DataEncryptionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DataEncryptionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DataEncryptionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 primary_key_uri: Optional[str] = None,
                 primary_user_assigned_identity_id: Optional[str] = None,
                 type: Optional[str] = None):
        """
        The data encryption properties of a cluster.
        :param str primary_key_uri: URI for the key in keyvault for data encryption of the primary server.
        :param str primary_user_assigned_identity_id: Resource Id for the User assigned identity to be used for data encryption of the primary server.
        """
        if primary_key_uri is not None:
            pulumi.set(__self__, "primary_key_uri", primary_key_uri)
        if primary_user_assigned_identity_id is not None:
            pulumi.set(__self__, "primary_user_assigned_identity_id", primary_user_assigned_identity_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="primaryKeyUri")
    def primary_key_uri(self) -> Optional[str]:
        """
        URI for the key in keyvault for data encryption of the primary server.
        """
        return pulumi.get(self, "primary_key_uri")

    @property
    @pulumi.getter(name="primaryUserAssignedIdentityId")
    def primary_user_assigned_identity_id(self) -> Optional[str]:
        """
        Resource Id for the User assigned identity to be used for data encryption of the primary server.
        """
        return pulumi.get(self, "primary_user_assigned_identity_id")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")


@pulumi.output_type
class IdentityPropertiesResponse(dict):
    """
    Describes the identity of the cluster.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "userAssignedIdentities":
            suggest = "user_assigned_identities"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IdentityPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IdentityPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IdentityPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: Optional[str] = None,
                 user_assigned_identities: Optional[Mapping[str, 'outputs.UserAssignedIdentityResponse']] = None):
        """
        Describes the identity of the cluster.
        :param Mapping[str, 'UserAssignedIdentityResponse'] user_assigned_identities: The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.
        """
        if type is not None:
            pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, 'outputs.UserAssignedIdentityResponse']]:
        """
        The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.
        """
        return pulumi.get(self, "user_assigned_identities")


@pulumi.output_type
class MaintenanceWindowResponse(dict):
    """
    Schedule settings for regular cluster updates.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "customWindow":
            suggest = "custom_window"
        elif key == "dayOfWeek":
            suggest = "day_of_week"
        elif key == "startHour":
            suggest = "start_hour"
        elif key == "startMinute":
            suggest = "start_minute"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MaintenanceWindowResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MaintenanceWindowResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MaintenanceWindowResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 custom_window: Optional[str] = None,
                 day_of_week: Optional[int] = None,
                 start_hour: Optional[int] = None,
                 start_minute: Optional[int] = None):
        """
        Schedule settings for regular cluster updates.
        :param str custom_window: Indicates whether custom maintenance window is enabled or not.
        :param int day_of_week: Preferred day of the week for maintenance window.
        :param int start_hour: Start hour within preferred day of the week for maintenance window.
        :param int start_minute: Start minute within the start hour for maintenance window.
        """
        if custom_window is not None:
            pulumi.set(__self__, "custom_window", custom_window)
        if day_of_week is not None:
            pulumi.set(__self__, "day_of_week", day_of_week)
        if start_hour is not None:
            pulumi.set(__self__, "start_hour", start_hour)
        if start_minute is not None:
            pulumi.set(__self__, "start_minute", start_minute)

    @property
    @pulumi.getter(name="customWindow")
    def custom_window(self) -> Optional[str]:
        """
        Indicates whether custom maintenance window is enabled or not.
        """
        return pulumi.get(self, "custom_window")

    @property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[int]:
        """
        Preferred day of the week for maintenance window.
        """
        return pulumi.get(self, "day_of_week")

    @property
    @pulumi.getter(name="startHour")
    def start_hour(self) -> Optional[int]:
        """
        Start hour within preferred day of the week for maintenance window.
        """
        return pulumi.get(self, "start_hour")

    @property
    @pulumi.getter(name="startMinute")
    def start_minute(self) -> Optional[int]:
        """
        Start minute within the start hour for maintenance window.
        """
        return pulumi.get(self, "start_minute")


@pulumi.output_type
class PrivateEndpointPropertyResponse(dict):
    """
    Property to represent resource id of the private endpoint.
    """
    def __init__(__self__, *,
                 id: Optional[str] = None):
        """
        Property to represent resource id of the private endpoint.
        :param str id: Resource id of the private endpoint.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource id of the private endpoint.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class PrivateEndpointResponse(dict):
    """
    The private endpoint resource.
    """
    def __init__(__self__, *,
                 id: str):
        """
        The private endpoint resource.
        :param str id: The ARM identifier for private endpoint.
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ARM identifier for private endpoint.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    """
    A collection of information about the state of the connection between service consumer and provider.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "actionsRequired":
            suggest = "actions_required"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrivateLinkServiceConnectionStateResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrivateLinkServiceConnectionStateResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrivateLinkServiceConnectionStateResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 actions_required: Optional[str] = None,
                 description: Optional[str] = None,
                 status: Optional[str] = None):
        """
        A collection of information about the state of the connection between service consumer and provider.
        :param str actions_required: A message indicating if changes on the service provider require any updates on the consumer.
        :param str description: The reason for approval/rejection of the connection.
        :param str status: Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        if actions_required is not None:
            pulumi.set(__self__, "actions_required", actions_required)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[str]:
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        return pulumi.get(self, "actions_required")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The reason for approval/rejection of the connection.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class ServerNameItemResponse(dict):
    """
    The name object for a server.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "fullyQualifiedDomainName":
            suggest = "fully_qualified_domain_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServerNameItemResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServerNameItemResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServerNameItemResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 fully_qualified_domain_name: str,
                 name: Optional[str] = None):
        """
        The name object for a server.
        :param str fully_qualified_domain_name: The fully qualified domain name of a server.
        :param str name: The name of a server.
        """
        pulumi.set(__self__, "fully_qualified_domain_name", fully_qualified_domain_name)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="fullyQualifiedDomainName")
    def fully_qualified_domain_name(self) -> str:
        """
        The fully qualified domain name of a server.
        """
        return pulumi.get(self, "fully_qualified_domain_name")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of a server.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class SimplePrivateEndpointConnectionResponse(dict):
    """
    A private endpoint connection.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "systemData":
            suggest = "system_data"
        elif key == "groupIds":
            suggest = "group_ids"
        elif key == "privateEndpoint":
            suggest = "private_endpoint"
        elif key == "privateLinkServiceConnectionState":
            suggest = "private_link_service_connection_state"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SimplePrivateEndpointConnectionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SimplePrivateEndpointConnectionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SimplePrivateEndpointConnectionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 id: str,
                 name: str,
                 system_data: 'outputs.SystemDataResponse',
                 type: str,
                 group_ids: Optional[Sequence[str]] = None,
                 private_endpoint: Optional['outputs.PrivateEndpointPropertyResponse'] = None,
                 private_link_service_connection_state: Optional['outputs.PrivateLinkServiceConnectionStateResponse'] = None):
        """
        A private endpoint connection.
        :param str id: Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        :param str name: The name of the resource
        :param 'SystemDataResponse' system_data: Azure Resource Manager metadata containing createdBy and modifiedBy information.
        :param str type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        :param Sequence[str] group_ids: Group ids of the private endpoint connection.
        :param 'PrivateEndpointPropertyResponse' private_endpoint: Private endpoint which the connection belongs to.
        :param 'PrivateLinkServiceConnectionStateResponse' private_link_service_connection_state: A collection of information about the state of the connection between service consumer and provider.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "system_data", system_data)
        pulumi.set(__self__, "type", type)
        if group_ids is not None:
            pulumi.set(__self__, "group_ids", group_ids)
        if private_endpoint is not None:
            pulumi.set(__self__, "private_endpoint", private_endpoint)
        if private_link_service_connection_state is not None:
            pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)

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

    @property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Optional[Sequence[str]]:
        """
        Group ids of the private endpoint connection.
        """
        return pulumi.get(self, "group_ids")

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional['outputs.PrivateEndpointPropertyResponse']:
        """
        Private endpoint which the connection belongs to.
        """
        return pulumi.get(self, "private_endpoint")

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional['outputs.PrivateLinkServiceConnectionStateResponse']:
        """
        A collection of information about the state of the connection between service consumer and provider.
        """
        return pulumi.get(self, "private_link_service_connection_state")


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


